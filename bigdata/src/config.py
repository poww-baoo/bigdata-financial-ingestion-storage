"""
Module cấu hình trung tâm và định nghĩa Data Contract (Input/Output Schema)
dùng chung cho cả 4 thành viên trong nhóm.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Tự động nạp file .env ở thư mục gốc dự án
PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

# --- 1. Cấu hình Apache Kafka ---
KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
KAFKA_TOPIC_TRANSACTIONS = os.getenv("KAFKA_TOPIC_TRANSACTIONS", "financial_tx")
KAFKA_TOPIC_DLQ = os.getenv("KAFKA_TOPIC_DLQ", "financial_tx_dlq")
KAFKA_NUM_PARTITIONS = int(os.getenv("KAFKA_NUM_PARTITIONS", "3"))

# --- 2. Cấu hình MinIO / S3 Data Lake ---
MINIO_ENDPOINT = os.getenv("MINIO_ENDPOINT", "localhost:9000")
MINIO_S3_ENDPOINT = os.getenv("MINIO_S3_ENDPOINT", "http://localhost:9000")
MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY", "minioadmin")
MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY", "minioadmin123")
MINIO_BUCKET_NAME = os.getenv("MINIO_BUCKET_NAME", "financial-datalake")

# --- 3. Đường dẫn phân vùng trong Data Lake ---
LAKE_BRONZE_PATH = os.getenv("LAKE_BRONZE_PATH", "bronze/transactions")
LAKE_QUARANTINE_PATH = os.getenv("LAKE_QUARANTINE_PATH", "quarantine/bad_transactions")
LAKE_CHECKPOINT_PATH = os.getenv("LAKE_CHECKPOINT_PATH", "checkpoints/transactions_stream_chk")

# --- 4. Danh mục hợp lệ theo Data Contract (Mục 5.3 & 5.4) ---
VALID_TX_TYPES = {"PAYMENT", "TRANSFER", "CASH_OUT", "CASH_IN", "DEBIT"}
VALID_CHANNELS = {"MOBILE_APP", "WEB", "POS", "ATM"}
VALID_CURRENCIES = {"VND", "USD"}

REQUIRED_FIELDS = [
    "transaction_id",
    "event_time",
    "step",
    "tx_type",
    "amount",
    "currency",
    "sender_id",
    "sender_old_balance",
    "sender_new_balance",
    "receiver_id",
    "payment_channel",
    "is_fraud_label",
]
