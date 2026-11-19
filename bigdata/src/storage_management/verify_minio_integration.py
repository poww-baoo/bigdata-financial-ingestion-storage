"""Kiểm chứng Storage trên MinIO thật với 1.000 giao dịch mẫu, không cần Kafka.

Chỉ dùng bucket trống cho prepare. Finish yêu cầu dừng writer và reader.
python -m src.storage_management.verify_minio_integration --prepare
python -m src.storage_management.verify_minio_integration --finish --writers-stopped
"""
import argparse
import hashlib
import io
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import urlopen

import pandas as pd
import pyarrow.parquet as pq

from src.config import (
    LAKE_BRONZE_PATH, LAKE_QUARANTINE_PATH, MINIO_BUCKET_NAME, MINIO_ENDPOINT,
    PROJECT_ROOT,
)
from src.ingestion_sink.spark_kafka_to_lake import (
    validate_transaction, write_parquet_partitions_to_minio,
)
from src.storage_management.compact_small_files import compact_partitions, read_object
from src.storage_management.init_minio_buckets import get_minio_client, inspect_datalake
from src.storage_management.query_verification import (
    create_duckdb_s3_connection, verify_datalake_storage,
)

EVIDENCE = PROJECT_ROOT / 'docs' / 'tv3_evidence'


def write_json(name, value):
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    (EVIDENCE / name).write_text(json.dumps(value, indent=2, ensure_ascii=False, default=str), encoding='utf-8')


def snapshot():
    client = get_minio_client()
    con = create_duckdb_s3_connection()
    try:
        con.read_parquet(
            f's3://{MINIO_BUCKET_NAME}/{LAKE_BRONZE_PATH}/*/*/*.parquet',
            hive_partitioning=True).create_view('transactions')
        cursor = con.execute('SELECT * FROM transactions ORDER BY transaction_id')
        columns = [column[0] for column in cursor.description]
        rows = [dict(zip(columns, row)) for row in cursor.fetchall()]
        digest = hashlib.sha256(json.dumps(rows, sort_keys=True, default=str).encode()).hexdigest()
    finally:
        con.close()
    objects = list(client.list_objects(MINIO_BUCKET_NAME, recursive=True))
    bronze = [obj for obj in objects if obj.object_name.startswith(LAKE_BRONZE_PATH + '/') and obj.object_name.endswith('.parquet')]
    quarantine = [obj for obj in objects if obj.object_name.startswith(LAKE_QUARANTINE_PATH + '/') and obj.object_name.endswith('.parquet')]
    partitions = sorted({obj.object_name.rsplit('/', 1)[0] for obj in bronze})
    inventory = [{'key': obj.object_name, 'bytes': obj.size} for obj in bronze]
    codecs = set()
    for obj in bronze:
        parquet = pq.ParquetFile(io.BytesIO(read_object(client, obj.object_name)))
        for index in range(parquet.metadata.num_row_groups):
            group = parquet.metadata.row_group(index)
            codecs.update(group.column(col).compression for col in range(group.num_columns))
    quarantine_hash = hashlib.sha256()
    for obj in sorted(quarantine, key=lambda obj: obj.object_name):
        quarantine_hash.update(obj.object_name.encode())
        quarantine_hash.update(read_object(client, obj.object_name))
    return {'row_count': len(rows), 'rows_sha256': digest, 'bronze_files': len(bronze),
            'bronze_bytes': sum(obj.size for obj in bronze), 'partitions': partitions,
            'compression': sorted(codecs), 'quarantine_files': len(quarantine),
            'quarantine_sha256': quarantine_hash.hexdigest(), 'objects': inventory}


def prepare():
    client = get_minio_client()
    # Không seed hoặc sửa policy khi bucket đang có dữ liệu của người dùng.
    if client.bucket_exists(MINIO_BUCKET_NAME) and next(iter(client.list_objects(MINIO_BUCKET_NAME, recursive=True)), None):
        raise RuntimeError('Prepare cần bucket trống. Hãy dùng MINIO_BUCKET_NAME riêng cho kiểm chứng.')
    inspect_datalake()
    source = pd.read_csv(PROJECT_ROOT / 'data' / 'sample_transactions.csv').to_dict('records')
    rows = []
    for repeat in range(100):
        for index, original in enumerate(source):
            record = dict(original)
            record.update(transaction_id=f'TV3-{repeat:03d}-{index:02d}',
                          tx_date=original['event_time'][:10],
                          ingested_at='2026-11-10T00:00:00+00:00',
                          kafka_partition=index % 3, kafka_offset=repeat * 10 + index)
            # Dữ liệu demo tổng hợp hai đơn vị tiền để kiểm tra không cộng lẫn.
            if repeat % 10 == 0:
                record['currency'] = 'USD'
                record['amount'] = round(record['amount'] / 25000, 2)
            ok, reason = validate_transaction(record)
            if not ok:
                raise ValueError(reason)
            rows.append(record)
    for start in range(0, len(rows), 200):
        write_parquet_partitions_to_minio(client, rows[start:start + 200], LAKE_BRONZE_PATH, ['tx_date', 'tx_type'])
    bad_rows = []
    for index in range(6):
        bad = dict(rows[index], transaction_id=f'TV3-BAD-{index}', amount=-1.0)
        ok, reason = validate_transaction(bad)
        assert not ok
        bad_rows.append({'raw_json': json.dumps(bad), 'error_reason': reason,
                         'rejected_date': '2026-11-10', 'kafka_partition': index % 3,
                         'kafka_offset': 1000 + index, 'ingested_at': '2026-11-10T00:00:00+00:00'})
    write_parquet_partitions_to_minio(client, bad_rows, LAKE_QUARANTINE_PATH, ['rejected_date'])
    baseline = snapshot()
    assert baseline['row_count'] == 1000 and baseline['compression'] == ['SNAPPY']
    # Bucket phải chặn GET không có thông tin đăng nhập.
    url = f'http://{MINIO_ENDPOINT}/{MINIO_BUCKET_NAME}/{baseline["objects"][0]["key"]}'
    try:
        with urlopen(url, timeout=10) as response:
            response.read()
        raise AssertionError('Bucket đang cho phép đọc ẩn danh')
    except HTTPError as exc:
        assert exc.code == 403, exc.code
    baseline['anonymous_get_status'] = 403
    write_json('before.json', baseline)
    verify_datalake_storage(output_dir=EVIDENCE / 'before', expected_records=1000)
    inspect_datalake()
    print(f'[PREPARE PASS] 1000 giao dịch, 6 bản ghi cách ly, {baseline["bronze_files"]} file Bronze.')


def finish(writers_stopped):
    if not writers_stopped:
        raise ValueError('Dừng writer/reader rồi truyền --writers-stopped')
    before = json.loads((EVIDENCE / 'before.json').read_text())
    current = snapshot()
    if current['rows_sha256'] != before['rows_sha256']:
        raise ValueError('Dữ liệu đã đổi sau prepare; dừng kiểm chứng')
    dry = compact_partitions()
    assert snapshot() == current, 'Dry-run đã sửa dữ liệu'
    report = compact_partitions(apply=True, writers_stopped=True)
    after = snapshot()
    for key in ['row_count', 'rows_sha256', 'partitions', 'compression', 'quarantine_files', 'quarantine_sha256']:
        assert before[key] == after[key], f'Sai lệch {key}'
    assert after['bronze_files'] < before['bronze_files']
    verify_datalake_storage(output_dir=EVIDENCE / 'after', expected_records=1000)
    for name in ['by_partition.csv', 'by_channel.csv', 'sample.csv', 'quarantine.csv', 'totals.csv']:
        assert (EVIDENCE / 'before' / name).read_bytes() == (EVIDENCE / 'after' / name).read_bytes(), name
    assert compact_partitions(apply=True, writers_stopped=True)['groups_planned'] == 0
    write_json('after.json', after)
    write_json('result.json', {
        'passed': True, 'completed_at_utc': datetime.now(timezone.utc).isoformat(),
        'endpoint': MINIO_ENDPOINT, 'bucket': MINIO_BUCKET_NAME,
        'fixture': '1000 synthetic transactions derived from sample CSV; 6 rejected records; no Kafka required',
        'rows_before': before['row_count'], 'rows_after': after['row_count'],
        'files_before': before['bronze_files'], 'files_after': after['bronze_files'],
        'full_rows_sha256_unchanged': True, 'aggregates_unchanged': True,
        'quarantine_unchanged': True, 'dry_run_unchanged': True, 'second_apply_noop': True,
        'anonymous_get_status': before['anonymous_get_status'],
        'dry_run': dry, 'compaction': report,
    })
    inspect_datalake()
    print('[INTEGRATION PASS] Dữ liệu và tổng tiền giữ nguyên; compaction hoàn tất trên MinIO thật.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    phase = parser.add_mutually_exclusive_group(required=True)
    phase.add_argument('--prepare', action='store_true')
    phase.add_argument('--finish', action='store_true')
    parser.add_argument('--writers-stopped', action='store_true')
    args = parser.parse_args()
    prepare() if args.prepare else finish(args.writers_stopped)
