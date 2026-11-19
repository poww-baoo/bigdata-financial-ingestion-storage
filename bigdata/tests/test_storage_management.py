"""Kiểm chứng TV3 không cần Docker: S3 giả lập và Parquet/DuckDB thật."""
import io
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

import pyarrow as pa
import pyarrow.parquet as pq

from src.storage_management.compact_small_files import compact_partitions
from src.storage_management.query_verification import verify_datalake_storage

PREFIX = 'bronze/transactions/tx_date=2026-11-10/tx_type=TRANSFER'


def parquet_bytes(rows):
    buffer = io.BytesIO()
    pq.write_table(pa.Table.from_pylist(rows), buffer, compression='snappy')
    return buffer.getvalue()


class Response(io.BytesIO):
    def release_conn(self):
        pass


class MemoryS3:
    def __init__(self):
        self.objects = {f'{PREFIX}/part-{i}.snappy.parquet': parquet_bytes([
            {'transaction_id': f'TX{i}', 'amount': float(i + 1),
             'currency': 'VND', 'payment_channel': 'WEB'}]) for i in range(3)}
        self.fail_delete = False

    def list_objects(self, bucket, prefix='', recursive=True):
        return [SimpleNamespace(object_name=key, size=len(data))
                for key, data in self.objects.items() if key.startswith(prefix)]

    def get_object(self, bucket, key):
        return Response(self.objects[key])

    def put_object(self, bucket, key, data, length):
        self.objects[key] = data.read(length)

    def remove_object(self, bucket, key):
        if self.fail_delete:
            raise OSError('simulated interruption')
        self.objects.pop(key, None)


class StorageTests(unittest.TestCase):
    def test_compaction_preserves_data_and_is_idempotent(self):
        client = MemoryS3()
        original = dict(client.objects)
        compact_partitions(client=client)
        self.assertEqual(client.objects, original)
        report = compact_partitions(apply=True, writers_stopped=True, client=client)
        self.assertEqual((report['files_before'], report['files_after']), (3, 1))
        merged = pq.read_table(io.BytesIO(next(iter(client.objects.values()))))
        self.assertEqual(merged.num_rows, 3)
        self.assertEqual(sum(merged['amount'].to_pylist()), 6.0)
        self.assertEqual(sorted(merged['transaction_id'].to_pylist()), ['TX0', 'TX1', 'TX2'])
        self.assertEqual(compact_partitions(apply=True, writers_stopped=True, client=client)['groups_planned'], 0)

    def test_interruption_keeps_journal_and_blocks_retry(self):
        client = MemoryS3()
        client.fail_delete = True
        with self.assertRaises(OSError):
            compact_partitions(apply=True, writers_stopped=True, client=client)
        self.assertEqual(sum(key.startswith(PREFIX + '/part-') for key in client.objects), 3)
        with self.assertRaises(RuntimeError):
            compact_partitions(client=client)

    def test_requires_maintenance_window(self):
        with self.assertRaises(ValueError):
            compact_partitions(apply=True, client=MemoryS3())

    def test_sql_export_and_failed_reconciliation(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            client = MemoryS3()
            for key, data in client.objects.items():
                path = root / key
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(data)
            glob = str(root / 'bronze/transactions/*/*/*.parquet')
            output = root / 'exports'
            result = verify_datalake_storage(glob, output_dir=output, expected_records=3)
            self.assertTrue(result['passed'])
            self.assertTrue((output / 'by_channel.csv').exists())
            with self.assertRaises(ValueError):
                verify_datalake_storage(glob, output_dir=output, expected_records=4)
            (root / PREFIX / 'duplicate.parquet').write_bytes(next(iter(client.objects.values())))
            with self.assertRaises(ValueError):
                verify_datalake_storage(glob, output_dir=output)


if __name__ == '__main__':
    unittest.main()
