"""Gộp Parquet theo partition. Mặc định chỉ xem kế hoạch; dừng writer/reader khi apply."""
import argparse
import io
import json
import tempfile
import uuid
from collections import defaultdict

import pyarrow as pa
import pyarrow.parquet as pq

from src.config import LAKE_BRONZE_PATH, MINIO_BUCKET_NAME
from src.storage_management.init_minio_buckets import get_minio_client


def read_object(client, key):
    response = client.get_object(MINIO_BUCKET_NAME, key)
    try:
        return response.read()
    finally:
        response.close()
        response.release_conn()


def compact_partitions(apply=False, writers_stopped=False, target_mb=128, client=None):
    if target_mb <= 0:
        raise ValueError("target_mb phải > 0")
    if apply and not writers_stopped:
        raise ValueError("Dừng ingestion và reader, rồi truyền --writers-stopped trước khi --apply")
    client = client or get_minio_client()
    # Journal ngoài Bronze: DuckDB không quét nhầm file tạm.
    journal_prefix = "maintenance/compaction/"
    pending = list(client.list_objects(MINIO_BUCKET_NAME, prefix=journal_prefix, recursive=True))
    if pending:
        raise RuntimeError("Có journal compaction chưa hoàn tất. Khôi phục theo tài liệu TV3 trước khi chạy lại.")
    partitions = defaultdict(list)
    for obj in client.list_objects(MINIO_BUCKET_NAME, prefix=LAKE_BRONZE_PATH.rstrip('/') + '/', recursive=True):
        if obj.object_name.endswith('.parquet'):
            partitions[obj.object_name.rsplit('/', 1)[0]].append(obj)
    report = {"partitions_scanned": len(partitions), "partitions_compacted": 0,
              "files_before": sum(map(len, partitions.values())), "files_after": sum(map(len, partitions.values())),
              "groups_planned": 0, "rows_rewritten": 0, "applied": apply}
    target = target_mb * 1024 * 1024
    for partition, objects in sorted(partitions.items()):
        # Chỉ gom các file nhỏ, giới hạn tổng byte nén mỗi nhóm.
        groups, group, size = [], [], 0
        for obj in sorted(objects, key=lambda obj: obj.object_name):
            if obj.size >= target:
                continue
            if group and size + obj.size > target:
                groups.append(group)
                group, size = [], 0
            group.append(obj)
            size += obj.size
        if group:
            groups.append(group)
        changed = False
        for group in groups:
            if len(group) < 2:
                continue
            report['groups_planned'] += 1
            print(f"[COMPACTION] {partition}: {len(group)} file -> 1; apply={apply}")
            if not apply:
                continue
            run_id = uuid.uuid4().hex
            destination = f"{partition}/compacted-{run_id}.snappy.parquet"
            journal_key = f"{journal_prefix}{run_id}.json"
            journal = {"sources": [obj.object_name for obj in group], "destination": destination}
            rows = 0
            # Đọc từng file, ghi từng batch; không giữ cả partition trong RAM.
            with tempfile.TemporaryFile() as output:
                writer = None
                try:
                    for obj in group:
                        parquet = pq.ParquetFile(io.BytesIO(read_object(client, obj.object_name)))
                        if writer is None:
                            schema = parquet.schema_arrow.remove_metadata()
                            writer = pq.ParquetWriter(output, schema, compression='snappy')
                        elif not parquet.schema_arrow.equals(schema, check_metadata=False):
                            raise ValueError(f"Schema không đồng nhất: {obj.object_name}")
                        for batch in parquet.iter_batches(batch_size=65536):
                            writer.write_table(pa.Table.from_batches([batch], schema=schema))
                            rows += batch.num_rows
                finally:
                    if writer:
                        writer.close()
                output.seek(0)
                if pq.ParquetFile(output).metadata.num_rows != rows:
                    raise RuntimeError("Số bản ghi file gộp không khớp")
                journal['rows'] = rows
                payload = json.dumps(journal).encode()
                client.put_object(MINIO_BUCKET_NAME, journal_key, io.BytesIO(payload), len(payload))
                length = output.seek(0, 2)
                output.seek(0)
                client.put_object(MINIO_BUCKET_NAME, destination, output, length)
            # Xác minh file đọc lại trước khi xóa bất kỳ nguồn nào.
            uploaded = pq.ParquetFile(io.BytesIO(read_object(client, destination)))
            if uploaded.metadata.num_rows != rows or not uploaded.schema_arrow.equals(schema, check_metadata=False):
                raise RuntimeError("File upload không hợp lệ; giữ nguồn và journal để phục hồi")
            for obj in group:
                client.remove_object(MINIO_BUCKET_NAME, obj.object_name)
            client.remove_object(MINIO_BUCKET_NAME, journal_key)
            report['files_after'] -= len(group) - 1
            report['rows_rewritten'] += rows
            changed = True
        if changed:
            report['partitions_compacted'] += 1
    print(json.dumps(report, indent=2))
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true')
    parser.add_argument('--writers-stopped', action='store_true')
    parser.add_argument('--target-mb', type=int, default=128)
    compact_partitions(**vars(parser.parse_args()))
