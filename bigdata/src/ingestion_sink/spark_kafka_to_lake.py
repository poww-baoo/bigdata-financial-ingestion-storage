"""
===============================================================================
THÀNH VIÊN 2: INGESTION -> STORAGE STREAMING ENGINE
===============================================================================
Chức năng:
1. Đọc luồng dữ liệu giao dịch từ Kafka topic `financial_tx` theo micro-batch.
2. Kiểm tra tính toàn vẹn dữ liệu (Veracity & Schema Validation):
   - Tách bản ghi hợp lệ (`amount > 0`, đủ trường bắt buộc, đúng danh mục `tx_type`)
     và khử trùng lặp theo `transaction_id` (Deduplication).
   - Tách bản ghi lỗi vào vùng cách ly `quarantine/bad_transactions` trên MinIO
     kèm nguyên nhân lỗi (`error_reason`) và đẩy cảnh báo vào `financial_tx_dlq`.
3. Ghi dữ liệu hợp lệ xuống MinIO Data Lake dưới định dạng cột **Apache Parquet**
   (nén Snappy) có phân vùng 2 cấp: `tx_date=YYYY-MM-DD/tx_type=...`.
4. Lưu trạng thái Offset/Checkpoint để đảm bảo khả năng chịu lỗi (Fault Tolerance).

Hỗ trợ 2 chế độ vận hành:
- `--engine pyspark` : Chạy bằng PySpark Structured Streaming + Hadoop AWS S3A.
- `--engine microbatch`: Chạy bằng Python Confluent-Kafka + PyArrow Parquet S3
  (nhẹ, không cần cài Java/Hadoop phức tạp trên Windows mà vẫn tạo đúng cây thư
  mục Partition Parquet chuẩn trên MinIO).

Cách chạy:
    python -m src.ingestion_sink.spark_kafka_to_lake --engine microbatch --max-batches 5
    python -m src.ingestion_sink.spark_kafka_to_lake --engine pyspark
"""

import argparse
import io
import json
import time
import uuid
from datetime import datetime, timezone

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from confluent_kafka import Consumer, KafkaError, Producer
from minio import Minio

from src.config import (
    KAFKA_BOOTSTRAP_SERVERS,
    KAFKA_TOPIC_DLQ,
    KAFKA_TOPIC_TRANSACTIONS,
    LAKE_BRONZE_PATH,
    LAKE_CHECKPOINT_PATH,
    LAKE_QUARANTINE_PATH,
    MINIO_ACCESS_KEY,
    MINIO_BUCKET_NAME,
    MINIO_ENDPOINT,
    MINIO_S3_ENDPOINT,
    MINIO_SECRET_KEY,
    VALID_TX_TYPES,
)


def validate_transaction(record: dict) -> tuple[bool, str]:
    """Kiểm tra luật hợp lệ của bản ghi giao dịch tài chính."""
    if not isinstance(record, dict):
        return False, "INVALID_JSON_OBJECT"
    if not record.get("transaction_id"):
        return False, "MISSING_TRANSACTION_ID"
    if not record.get("sender_id") or not record.get("receiver_id"):
        return False, "MISSING_ACCOUNT_ID"
    if record.get("tx_type") not in VALID_TX_TYPES:
        return False, f"INVALID_TX_TYPE:{record.get('tx_type')}"
    try:
        amount = float(record.get("amount", 0))
        if amount <= 0:
            return False, f"NON_POSITIVE_AMOUNT:{amount}"
    except (TypeError, ValueError):
        return False, "INVALID_AMOUNT_NUMBER"
    return True, "OK"


def write_parquet_partitions_to_minio(
    minio_client: Minio,
    records: list[dict],
    base_prefix: str,
    partition_cols: list[str],
) -> int:
    """
    Ghi danh sách bản ghi xuống MinIO dưới định dạng Parquet (nén Snappy)
    theo đúng chuẩn phân vùng Hive-style: `col1=val1/col2=val2/part-xxx.snappy.parquet`.
    """
    if not records:
        return 0

    df = pd.DataFrame(records)
    files_written = 0

    for part_values, group_df in df.groupby(partition_cols, dropna=False):
        if not isinstance(part_values, tuple):
            part_values = (part_values,)

        part_path = "/".join(
            f"{col}={val}" for col, val in zip(partition_cols, part_values)
        )
        file_name = f"part-{uuid.uuid4().hex[:12]}.snappy.parquet"
        object_key = f"{base_prefix}/{part_path}/{file_name}"

        # Bỏ các cột khóa partition khỏi bên trong file Parquet (chuẩn Hive Partitioning)
        data_df = group_df.drop(columns=partition_cols)
        table = pa.Table.from_pandas(data_df, preserve_index=False)

        buf = io.BytesIO()
        pq.write_table(table, buf, compression="snappy")
        buf.seek(0)

        minio_client.put_object(
            bucket_name=MINIO_BUCKET_NAME,
            object_name=object_key,
            data=buf,
            length=buf.getbuffer().nbytes,
            content_type="application/octet-stream",
        )
        files_written += 1

    return files_written


def save_checkpoint_to_minio(minio_client: Minio, stats: dict) -> None:
    """Lưu trạng thái Checkpoint (offset & thống kê batch) lên MinIO."""
    payload = json.dumps(stats, indent=2).encode("utf-8")
    minio_client.put_object(
        bucket_name=MINIO_BUCKET_NAME,
        object_name=f"{LAKE_CHECKPOINT_PATH}/latest_checkpoint.json",
        data=io.BytesIO(payload),
        length=len(payload),
        content_type="application/json",
    )


def run_microbatch_engine(
    batch_size: int = 5000,
    batch_timeout_sec: float = 5.0,
    max_empty_batches: int = 3,
    consumer_group: str = "spark-lakehouse-sink-group",
) -> dict:
    """
    Chạy luồng Ingestion -> Storage theo cơ chế Micro-Batch:
    Kafka -> Validate & Deduplicate -> MinIO Parquet Partitioned (`tx_date/tx_type`).
    """
    minio_client = Minio(
        MINIO_ENDPOINT,
        access_key=MINIO_ACCESS_KEY,
        secret_key=MINIO_SECRET_KEY,
        secure=False,
    )
    if not minio_client.bucket_exists(MINIO_BUCKET_NAME):
        minio_client.make_bucket(MINIO_BUCKET_NAME)

    consumer = Consumer(
        {
            "bootstrap.servers": KAFKA_BOOTSTRAP_SERVERS,
            "group.id": consumer_group,
            "auto.offset.reset": "earliest",
            "enable.auto.commit": False,
        }
    )
    dlq_producer = Producer({"bootstrap.servers": KAFKA_BOOTSTRAP_SERVERS})
    consumer.subscribe([KAFKA_TOPIC_TRANSACTIONS])

    seen_tx_ids: set[str] = set()
    summary = {
        "batches_processed": 0,
        "total_consumed": 0,
        "valid_written": 0,
        "duplicates_dropped": 0,
        "quarantined_written": 0,
        "parquet_files_created": 0,
    }

    empty_streak = 0
    print(
        f"[STREAMING SINK] Đang lắng nghe Kafka topic '{KAFKA_TOPIC_TRANSACTIONS}' "
        f"-> Ghi xuống s3a://{MINIO_BUCKET_NAME}/{LAKE_BRONZE_PATH}..."
    )

    try:
        while empty_streak < max_empty_batches:
            batch_valid = []
            batch_quarantine = []
            batch_start = time.perf_counter()
            ingested_ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
            today_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")

            while len(batch_valid) + len(batch_quarantine) < batch_size:
                remaining = batch_timeout_sec - (time.perf_counter() - batch_start)
                if remaining <= 0:
                    break
                msg = consumer.poll(timeout=min(0.5, max(0.05, remaining)))
                if msg is None:
                    continue
                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        continue
                    print(f"[STREAMING SINK] Kafka error: {msg.error()}")
                    continue

                summary["total_consumed"] += 1
                raw_text = msg.value().decode("utf-8", errors="replace")

                try:
                    record = json.loads(raw_text)
                except json.JSONDecodeError:
                    batch_quarantine.append(
                        {
                            "raw_payload": raw_text,
                            "error_reason": "MALFORMED_JSON",
                            "kafka_partition": msg.partition(),
                            "kafka_offset": msg.offset(),
                            "ingested_at": ingested_ts,
                            "rejected_date": today_str,
                        }
                    )
                    continue

                is_valid, reason = validate_transaction(record)
                if not is_valid:
                    quarantine_item = {
                        "raw_payload": raw_text,
                        "error_reason": reason,
                        "kafka_partition": msg.partition(),
                        "kafka_offset": msg.offset(),
                        "ingested_at": ingested_ts,
                        "rejected_date": str(record.get("event_time", today_str))[:10],
                    }
                    batch_quarantine.append(quarantine_item)
                    dlq_producer.produce(
                        KAFKA_TOPIC_DLQ,
                        key=reason.encode("utf-8"),
                        value=json.dumps(quarantine_item).encode("utf-8"),
                    )
                    continue

                tx_id = record["transaction_id"]
                if tx_id in seen_tx_ids:
                    summary["duplicates_dropped"] += 1
                    continue
                seen_tx_ids.add(tx_id)

                record["tx_date"] = str(record["event_time"])[:10]
                record["ingested_at"] = ingested_ts
                record["kafka_partition"] = msg.partition()
                record["kafka_offset"] = msg.offset()
                batch_valid.append(record)

            if not batch_valid and not batch_quarantine:
                empty_streak += 1
                continue

            empty_streak = 0
            summary["batches_processed"] += 1

            # 1. Ghi luồng hợp lệ xuống Bronze Data Lake (Partition: tx_date / tx_type)
            if batch_valid:
                files_created = write_parquet_partitions_to_minio(
                    minio_client=minio_client,
                    records=batch_valid,
                    base_prefix=LAKE_BRONZE_PATH,
                    partition_cols=["tx_date", "tx_type"],
                )
                summary["valid_written"] += len(batch_valid)
                summary["parquet_files_created"] += files_created

            # 2. Ghi luồng lỗi xuống vùng cách ly Quarantine (Partition: rejected_date)
            if batch_quarantine:
                write_parquet_partitions_to_minio(
                    minio_client=minio_client,
                    records=batch_quarantine,
                    base_prefix=LAKE_QUARANTINE_PATH,
                    partition_cols=["rejected_date"],
                )
                dlq_producer.flush()
                summary["quarantined_written"] += len(batch_quarantine)

            # 3. Commit Kafka Offset & lưu Checkpoint sau khi đã ghi xuống Storage an toàn
            consumer.commit(asynchronous=False)
            save_checkpoint_to_minio(minio_client, summary)

            print(
                f"[BATCH #{summary['batches_processed']}] Đã ghi: {len(batch_valid):,} hợp lệ | "
                f"Cách ly (Quarantine): {len(batch_quarantine):,} | "
                f"Lọc trùng tích lũy: {summary['duplicates_dropped']:,}"
            )
    finally:
        consumer.close()

    print(
        f"[STREAMING SINK] Hoàn tất đồng bộ! Tổng đọc: {summary['total_consumed']:,} | "
        f"Lưu hợp lệ: {summary['valid_written']:,} | Lọc trùng: {summary['duplicates_dropped']:,} | "
        f"Cách ly lỗi: {summary['quarantined_written']:,}"
    )
    return summary


def run_pyspark_structured_streaming() -> None:
    """
    Chạy bằng PySpark Structured Streaming chính quy (dùng khi cụm/máy đã cài
    Java 11/17 và gói org.apache.spark:spark-sql-kafka + hadoop-aws).
    """
    from pyspark.sql import SparkSession
    from pyspark.sql import functions as F
    from pyspark.sql.types import (
        DoubleType,
        IntegerType,
        StringType,
        StructField,
        StructType,
    )

    spark = (
        SparkSession.builder.appName("Financial-Kafka-To-MinIO-DataLake")
        .config(
            "spark.jars.packages",
            "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1,org.apache.hadoop:hadoop-aws:3.3.4",
        )
        .config("spark.hadoop.fs.s3a.endpoint", MINIO_S3_ENDPOINT)
        .config("spark.hadoop.fs.s3a.access.key", MINIO_ACCESS_KEY)
        .config("spark.hadoop.fs.s3a.secret.key", MINIO_SECRET_KEY)
        .config("spark.hadoop.fs.s3a.path.style.access", "true")
        .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
        .getOrCreate()
    )
    spark.sparkContext.setLogLevel("WARN")

    tx_schema = StructType(
        [
            StructField("transaction_id", StringType(), True),
            StructField("event_time", StringType(), True),
            StructField("step", IntegerType(), True),
            StructField("tx_type", StringType(), True),
            StructField("amount", DoubleType(), True),
            StructField("currency", StringType(), True),
            StructField("sender_id", StringType(), True),
            StructField("sender_old_balance", DoubleType(), True),
            StructField("sender_new_balance", DoubleType(), True),
            StructField("receiver_id", StringType(), True),
            StructField("payment_channel", StringType(), True),
            StructField("is_fraud_label", IntegerType(), True),
        ]
    )

    raw_stream = (
        spark.readStream.format("kafka")
        .option("kafka.bootstrap.servers", KAFKA_BOOTSTRAP_SERVERS)
        .option("subscribe", KAFKA_TOPIC_TRANSACTIONS)
        .option("startingOffsets", "earliest")
        .load()
    )

    parsed_df = (
        raw_stream.selectExpr(
            "CAST(value AS STRING) as raw_json",
            "partition as kafka_partition",
            "offset as kafka_offset",
        )
        .withColumn("data", F.from_json(F.col("raw_json"), tx_schema))
        .select("raw_json", "kafka_partition", "kafka_offset", "data.*")
        .withColumn("event_timestamp", F.to_timestamp("event_time"))
        .withColumn("tx_date", F.to_date("event_timestamp"))
        .withColumn("ingested_at", F.current_timestamp())
    )

    valid_condition = (
        F.col("transaction_id").isNotNull()
        & F.col("sender_id").isNotNull()
        & F.col("receiver_id").isNotNull()
        & (F.col("amount") > 0)
        & F.col("tx_type").isin(list(VALID_TX_TYPES))
    )

    valid_stream = (
        parsed_df.filter(valid_condition)
        .drop("raw_json")
        .withWatermark("event_timestamp", "10 minutes")
        .dropDuplicates(["transaction_id"])
    )

    quarantine_stream = parsed_df.filter(~valid_condition).select(
        "raw_json",
        "kafka_partition",
        "kafka_offset",
        "ingested_at",
        F.coalesce(F.col("tx_date").cast("string"), F.current_date().cast("string")).alias(
            "rejected_date"
        ),
    )

    valid_query = (
        valid_stream.writeStream.format("parquet")
        .option("path", f"s3a://{MINIO_BUCKET_NAME}/{LAKE_BRONZE_PATH}")
        .option(
            "checkpointLocation",
            f"s3a://{MINIO_BUCKET_NAME}/{LAKE_CHECKPOINT_PATH}/valid",
        )
        .partitionBy("tx_date", "tx_type")
        .trigger(processingTime="10 seconds")
        .outputMode("append")
        .start()
    )

    quarantine_query = (
        quarantine_stream.writeStream.format("parquet")
        .option("path", f"s3a://{MINIO_BUCKET_NAME}/{LAKE_QUARANTINE_PATH}")
        .option(
            "checkpointLocation",
            f"s3a://{MINIO_BUCKET_NAME}/{LAKE_CHECKPOINT_PATH}/quarantine",
        )
        .partitionBy("rejected_date")
        .trigger(processingTime="10 seconds")
        .outputMode("append")
        .start()
    )

    spark.streams.awaitAnyTermination()
    valid_query.stop()
    quarantine_query.stop()


def main():
    parser = argparse.ArgumentParser(description="Kafka to MinIO Data Lake Streaming Sink")
    parser.add_argument(
        "--engine",
        choices=["microbatch", "pyspark"],
        default="microbatch",
        help="Chọn engine chạy đồng bộ (mặc định: microbatch)",
    )
    parser.add_argument("--batch-size", type=int, default=5000, help="Kích thước mỗi micro-batch")
    parser.add_argument(
        "--max-empty-batches",
        type=int,
        default=3,
        help="Số lần poll rỗng liên tiếp trước khi tự dừng",
    )
    args = parser.parse_args()

    if args.engine == "pyspark":
        run_pyspark_structured_streaming()
    else:
        run_microbatch_engine(
            batch_size=args.batch_size,
            max_empty_batches=args.max_empty_batches,
        )


if __name__ == "__main__":
    main()
