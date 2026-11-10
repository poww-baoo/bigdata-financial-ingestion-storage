"""Đối soát Parquet bằng DuckDB và xuất CSV bàn giao cho nhóm Processing."""
import argparse
import json
from pathlib import Path

import duckdb

from src.config import (
    LAKE_BRONZE_PATH, LAKE_QUARANTINE_PATH, MINIO_ACCESS_KEY,
    MINIO_BUCKET_NAME, MINIO_ENDPOINT, MINIO_SECRET_KEY, PROJECT_ROOT,
)


def create_duckdb_s3_connection():
    con = duckdb.connect(":memory:")
    con.execute("INSTALL httpfs; LOAD httpfs;")
    for key, value in {"s3_endpoint": MINIO_ENDPOINT,
                       "s3_access_key_id": MINIO_ACCESS_KEY,
                       "s3_secret_access_key": MINIO_SECRET_KEY,
                       "s3_url_style": "path"}.items():
        con.execute(f"SET {key} = ?", [value])
    con.execute("SET s3_use_ssl=false")
    return con


def verify_datalake_storage(bronze_glob=None, quarantine_glob=None,
                            output_dir=None, expected_records=None):
    """Truy vấn local hoặc S3; lỗi đọc Bronze phải khiến lệnh thất bại."""
    bronze_glob = bronze_glob or f"s3://{MINIO_BUCKET_NAME}/{LAKE_BRONZE_PATH}/*/*/*.parquet"
    remote = bronze_glob.startswith("s3://")
    con = create_duckdb_s3_connection() if remote else duckdb.connect(":memory:")
    output = Path(output_dir or PROJECT_ROOT / "docs" / "storage_verification")
    output.mkdir(parents=True, exist_ok=True)
    try:
        con.read_parquet(bronze_glob, hive_partitioning=True).create_view("transactions")
        queries = {
            "schema": "DESCRIBE transactions",
            "totals": """SELECT COUNT(*) AS total_records,
                COUNT(DISTINCT transaction_id) AS unique_transactions,
                COUNT(*) - COUNT(DISTINCT transaction_id) AS duplicate_records,
                COUNT(*) FILTER (WHERE transaction_id IS NULL OR trim(transaction_id) = ''
                    OR amount IS NULL OR NOT isfinite(amount) OR amount <= 0) AS invalid_records
                FROM transactions""",
            "by_partition": """SELECT tx_date, tx_type, currency, COUNT(*) AS total_transactions,
                ROUND(SUM(amount), 2) AS total_amount FROM transactions
                GROUP BY tx_date, tx_type, currency ORDER BY tx_date, tx_type, currency""",
            "by_channel": """SELECT tx_date, payment_channel, currency,
                COUNT(*) AS total_transactions, ROUND(SUM(amount), 2) AS total_amount
                FROM transactions GROUP BY tx_date, payment_channel, currency
                ORDER BY tx_date, payment_channel, currency""",
            "sample": "SELECT * FROM transactions ORDER BY transaction_id LIMIT 20",
        }
        totals = None
        for name, sql in queries.items():
            frame = con.execute(sql).df()
            frame.to_csv(output / f"{name}.csv", index=False)
            print(f"\n[{name}]\n{frame.to_string(index=False)}")
            if name == "totals":
                totals = {key: int(value) for key, value in frame.iloc[0].items()}
        if quarantine_glob is None and remote:
            # Phân biệt bucket rỗng với lỗi quyền/kết nối: list_objects có lỗi sẽ raise.
            from src.storage_management.init_minio_buckets import get_minio_client
            objects = get_minio_client().list_objects(
                MINIO_BUCKET_NAME, prefix=LAKE_QUARANTINE_PATH.rstrip('/') + '/', recursive=True)
            if any(obj.object_name.endswith('.parquet') for obj in objects):
                quarantine_glob = f"s3://{MINIO_BUCKET_NAME}/{LAKE_QUARANTINE_PATH}/*/*.parquet"
        if quarantine_glob:
            con.read_parquet(quarantine_glob, hive_partitioning=True).create_view("quarantine")
            frame = con.execute("""SELECT rejected_date, error_reason, COUNT(*) AS rejected_records
                FROM quarantine GROUP BY rejected_date, error_reason
                ORDER BY rejected_date, error_reason""").df()
            frame.to_csv(output / "quarantine.csv", index=False)
            print(f"\n[quarantine]\n{frame.to_string(index=False)}")
        else:
            print("[quarantine] Không có dữ liệu cách ly để truy vấn.")
        passed = (totals["duplicate_records"] == 0 and totals["invalid_records"] == 0
                  and (expected_records is None or totals["total_records"] == expected_records))
        report = {**totals, "expected_records": expected_records, "passed": passed}
        (output / "summary.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
        if not passed:
            raise ValueError(f"Đối soát thất bại: {report}")
        return report
    finally:
        con.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bronze-glob", help="Mặc định đọc MinIO; có thể truyền glob Parquet local")
    parser.add_argument("--quarantine-glob")
    parser.add_argument("--output-dir")
    parser.add_argument("--expected-records", type=int)
    args = parser.parse_args()
    verify_datalake_storage(**vars(args))
