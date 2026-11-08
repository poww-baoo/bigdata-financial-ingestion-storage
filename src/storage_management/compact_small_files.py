"""
===============================================================================
THÀNH VIÊN 3: GIẢI QUYẾT BÀI TOÁN SMALL FILES PROBLEM (PARQUET COMPACTION)
===============================================================================
Chức năng:
Khi hệ thống Streaming chạy liên tục theo micro-batch (ví dụ 10 giây/lần), mỗi
partition `tx_date=.../tx_type=...` sẽ sinh ra nhiều file Parquet nhỏ, làm giảm
tốc độ đọc của Spark/DuckDB.
Script này thực hiện gộp (Compaction / Optimize) các file Parquet nhỏ trong cùng
một Partition thành một file Parquet lớn tối ưu duy nhất.

Cách chạy:
    python -m src.storage_management.compact_small_files
"""

import io
import uuid
from collections import defaultdict

import pyarrow as pa
import pyarrow.parquet as pq
from minio import Minio

from src.config import (
    LAKE_BRONZE_PATH,
    MINIO_ACCESS_KEY,
    MINIO_BUCKET_NAME,
    MINIO_ENDPOINT,
    MINIO_SECRET_KEY,
)


def compact_partitions() -> dict:
    client = Minio(
        MINIO_ENDPOINT,
        access_key=MINIO_ACCESS_KEY,
        secret_key=MINIO_SECRET_KEY,
        secure=False,
    )

    partition_files = defaultdict(list)
    for obj in client.list_objects(MINIO_BUCKET_NAME, prefix=LAKE_BRONZE_PATH, recursive=True):
        if obj.object_name.endswith(".parquet"):
            partition_prefix = "/".join(obj.object_name.split("/")[:-1])
            partition_files[partition_prefix].append(obj.object_name)

    report = {
        "partitions_scanned": len(partition_files),
        "partitions_compacted": 0,
        "files_before": sum(len(v) for v in partition_files.values()),
        "files_after": 0,
    }

    print(
        f"[COMPACTION] Quét {report['partitions_scanned']} phân vùng "
        f"(Tổng số file trước khi gộp: {report['files_before']})"
    )

    for part_prefix, object_keys in sorted(partition_files.items()):
        if len(object_keys) <= 1:
            report["files_after"] += len(object_keys)
            continue

        tables = []
        for key in object_keys:
            resp = client.get_object(MINIO_BUCKET_NAME, key)
            try:
                data = io.BytesIO(resp.read())
                tables.append(pq.read_table(data))
            finally:
                resp.close()
                resp.release_conn()

        merged_table = pa.concat_tables(tables, promote_options="default")
        out_buf = io.BytesIO()
        pq.write_table(merged_table, out_buf, compression="snappy")
        out_buf.seek(0)

        compacted_key = f"{part_prefix}/compacted-{uuid.uuid4().hex[:10]}.snappy.parquet"
        client.put_object(
            bucket_name=MINIO_BUCKET_NAME,
            object_name=compacted_key,
            data=out_buf,
            length=out_buf.getbuffer().nbytes,
            content_type="application/octet-stream",
        )

        # Xóa các file nhỏ cũ sau khi đã ghi thành công file gộp
        for old_key in object_keys:
            client.remove_object(MINIO_BUCKET_NAME, old_key)

        report["partitions_compacted"] += 1
        report["files_after"] += 1
        print(
            f"  + Đã gộp [{part_prefix}]: {len(object_keys)} file nhỏ -> 1 file chuẩn "
            f"({merged_table.num_rows:,} bản ghi)"
        )

    print(
        f"[COMPACTION] Hoàn tất! Số lượng file giảm từ {report['files_before']} -> {report['files_after']}"
    )
    return report


if __name__ == "__main__":
    compact_partitions()
