"""
===============================================================================
THÀNH VIÊN 3: TRUY VẤN KIỂM CHỨNG DỮ LIỆU ĐÃ LƯU TRONG DATA LAKE (DUCKDB SQL)
===============================================================================
Chức năng:
Chứng minh sản phẩm đầu ra tối thiểu của giai đoạn Ingestion -> Storage (Mục 4):
1. Đọc trực tiếp dữ liệu Parquet có phân vùng (`tx_date` / `tx_type`) từ MinIO.
2. Hiển thị Schema thực tế, thống kê số lượng giao dịch và tổng giá trị tiền tệ
   theo từng Partition.
3. Kiểm toán vùng cách ly lỗi (`quarantine/bad_transactions`) theo nguyên nhân lỗi.

Cách chạy:
    python -m src.storage_management.query_verification
"""

import duckdb

from src.config import (
    LAKE_BRONZE_PATH,
    LAKE_QUARANTINE_PATH,
    MINIO_ACCESS_KEY,
    MINIO_BUCKET_NAME,
    MINIO_ENDPOINT,
    MINIO_SECRET_KEY,
)


def create_duckdb_s3_connection() -> duckdb.DuckDBPyConnection:
    con = duckdb.connect(database=":memory:")
    con.execute("INSTALL httpfs; LOAD httpfs;")
    con.execute(f"SET s3_endpoint='{MINIO_ENDPOINT}';")
    con.execute(f"SET s3_access_key_id='{MINIO_ACCESS_KEY}';")
    con.execute(f"SET s3_secret_access_key='{MINIO_SECRET_KEY}';")
    con.execute("SET s3_use_ssl=false;")
    con.execute("SET s3_url_style='path';")
    return con


def verify_datalake_storage() -> None:
    con = create_duckdb_s3_connection()
    bronze_glob = f"s3://{MINIO_BUCKET_NAME}/{LAKE_BRONZE_PATH}/*/*/*.parquet"
    quarantine_glob = f"s3://{MINIO_BUCKET_NAME}/{LAKE_QUARANTINE_PATH}/*/*.parquet"

    print("=======================================================================")
    print("1. KIỂM TRA SCHEMA BẢNG GIAO DỊCH HỢP LỆ (BRONZE PARQUET PARTITIONED)")
    print("=======================================================================")
    try:
        schema_df = con.execute(
            f"DESCRIBE SELECT * FROM read_parquet('{bronze_glob}', hive_partitioning=true);"
        ).df()
        print(schema_df[["column_name", "column_type"]].to_string(index=False))

        print("\n=======================================================================")
        print("2. THỐNG KÊ ĐỐI SOÁT THEO PARTITION (tx_date & tx_type)")
        print("=======================================================================")
        part_df = con.execute(
            f"""
            SELECT
                tx_date,
                tx_type,
                COUNT(*) AS total_transactions,
                ROUND(SUM(amount), 2) AS total_amount_vnd,
                SUM(is_fraud_label) AS suspected_fraud_count
            FROM read_parquet('{bronze_glob}', hive_partitioning=true)
            GROUP BY tx_date, tx_type
            ORDER BY tx_date DESC, total_transactions DESC;
            """
        ).df()
        print(part_df.to_string(index=False))

        print("\n=======================================================================")
        print("3. 5 BẢN GHI MẪU ĐỌC TRỰC TIẾP TỪ MINIO DATA LAKE")
        print("=======================================================================")
        sample_df = con.execute(
            f"""
            SELECT transaction_id, tx_date, tx_type, amount, sender_id, receiver_id, payment_channel
            FROM read_parquet('{bronze_glob}', hive_partitioning=true)
            LIMIT 5;
            """
        ).df()
        print(sample_df.to_string(index=False))
    except Exception as exc:
        print(f"[THÔNG BÁO] Chưa đọc được dữ liệu Bronze trên MinIO: {exc}")

    print("\n=======================================================================")
    print("4. THỐNG KÊ VÙNG CÁCH LY BẢN GHI LỖI (QUARANTINE / DLQ AUDIT)")
    print("=======================================================================")
    try:
        quar_df = con.execute(
            f"""
            SELECT
                rejected_date,
                error_reason,
                COUNT(*) AS rejected_records
            FROM read_parquet('{quarantine_glob}', hive_partitioning=true)
            GROUP BY rejected_date, error_reason
            ORDER BY rejected_records DESC;
            """
        ).df()
        print(quar_df.to_string(index=False))
    except Exception as exc:
        print(f"[THÔNG BÁO] Chưa có bản ghi lỗi trong vùng Quarantine: {exc}")


if __name__ == "__main__":
    verify_datalake_storage()
