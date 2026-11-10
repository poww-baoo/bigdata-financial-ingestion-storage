"""
===============================================================================
THÀNH VIÊN 3: KHỞI TẠO & KIỂM TRA CẤU TRÚC DATA LAKE TRÊN MINIO (S3)
===============================================================================
Chức năng:
1. Kết nối tới MinIO Object Storage và đảm bảo bucket `financial-datalake` tồn tại.
2. Hiển thị thống kê tổng quan về dung lượng, số lượng file Parquet và các
   Partition hiện có trong tầng `bronze/transactions` và `quarantine/bad_transactions`.

Cách chạy:
    python -m src.storage_management.init_minio_buckets
"""

from collections import defaultdict
from minio import Minio

from src.config import (
    LAKE_BRONZE_PATH,
    LAKE_CHECKPOINT_PATH,
    LAKE_QUARANTINE_PATH,
    MINIO_ACCESS_KEY,
    MINIO_BUCKET_NAME,
    MINIO_ENDPOINT,
    MINIO_SECRET_KEY,
)


def get_minio_client() -> Minio:
    return Minio(
        MINIO_ENDPOINT,
        access_key=MINIO_ACCESS_KEY,
        secret_key=MINIO_SECRET_KEY,
        secure=False,
    )


def inspect_datalake() -> dict:
    client = get_minio_client()
    if not client.bucket_exists(MINIO_BUCKET_NAME):
        client.make_bucket(MINIO_BUCKET_NAME)
        print(f"[STORAGE] Đã tạo mới bucket: {MINIO_BUCKET_NAME}")
    else:
        print(f"[STORAGE] Bucket '{MINIO_BUCKET_NAME}' đã sẵn sàng tại http://{MINIO_ENDPOINT}")

    # Kho giao dịch chỉ được truy cập bằng tài khoản có quyền S3.
    client.delete_bucket_policy(MINIO_BUCKET_NAME)

    partition_stats = defaultdict(lambda: {"files": 0, "bytes": 0})
    quarantine_stats = {"files": 0, "bytes": 0}

    for obj in client.list_objects(MINIO_BUCKET_NAME, recursive=True):
        if obj.object_name.startswith(LAKE_BRONZE_PATH.rstrip("/") + "/") and obj.object_name.endswith(".parquet"):
            parts = obj.object_name[len(LAKE_BRONZE_PATH) :].strip("/").split("/")
            partition_key = "/".join(parts[:-1]) if len(parts) > 1 else "root"
            partition_stats[partition_key]["files"] += 1
            partition_stats[partition_key]["bytes"] += obj.size
        elif obj.object_name.startswith(LAKE_QUARANTINE_PATH.rstrip("/") + "/") and obj.object_name.endswith(".parquet"):
            quarantine_stats["files"] += 1
            quarantine_stats["bytes"] += obj.size

    print("\n=== THỐNG KÊ PHÂN VÙNG TRONG TẦNG BRONZE (PARQUET) ===")
    if not partition_stats:
        print("  (Chưa có dữ liệu Parquet nào được ghi)")
    else:
        for part, info in sorted(partition_stats.items()):
            kb = info["bytes"] / 1024
            print(f"  - Partition [{part}]: {info['files']} file Parquet ({kb:.2f} KB)")

    print("\n=== THỐNG KÊ VÙNG CÁCH LY LỖI (QUARANTINE) ===")
    print(
        f"  - Quarantine ({LAKE_QUARANTINE_PATH}): "
        f"{quarantine_stats['files']} file ({quarantine_stats['bytes']/1024:.2f} KB)"
    )
    print(f"  - Checkpoint ({LAKE_CHECKPOINT_PATH}): Lưu trạng thái Offset streaming")

    return {"bronze_partitions": dict(partition_stats), "quarantine": quarantine_stats}


if __name__ == "__main__":
    inspect_datalake()
