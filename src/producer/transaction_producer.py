"""
===============================================================================
THÀNH VIÊN 1: TRANSACTION PRODUCER (NGUỒN PHÁT LUỒNG GIAO DỊCH VÀO KAFKA)
===============================================================================
Chức năng:
1. Đọc dữ liệu giao dịch tài chính từ file CSV (PaySim / Sample CSV) hoặc sinh
   luồng giao dịch thời gian thực theo chuẩn Data Contract.
2. Đẩy vào Kafka topic `financial_tx` với Partition Key = `tx_type` để phân tải
   đều vào các Kafka Partitions.
3. Hỗ trợ giả lập lỗi (Fault Injection: amount <= 0, thiếu trường, JSON hỏng)
   và giả lập trùng lặp (Duplicate Injection) để kiểm chứng tính năng Veracity.

Cách chạy:
    python -m src.producer.transaction_producer --count 10000 --rate 2000
"""

import argparse
import csv
import json
import random
import sys
import time
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path

from confluent_kafka import Producer

from src.config import (
    KAFKA_BOOTSTRAP_SERVERS,
    KAFKA_TOPIC_TRANSACTIONS,
    PROJECT_ROOT,
)

TX_TYPES = ["PAYMENT", "TRANSFER", "CASH_OUT", "CASH_IN", "DEBIT"]
CHANNELS = ["MOBILE_APP", "WEB", "POS", "ATM"]


def create_kafka_producer() -> Producer:
    """Khởi tạo Kafka Producer hiệu năng cao."""
    conf = {
        "bootstrap.servers": KAFKA_BOOTSTRAP_SERVERS,
        "client.id": "financial-tx-producer",
        "linger.ms": 10,
        "batch.num.messages": 5000,
        "compression.type": "snappy",
        "acks": "1",
    }
    return Producer(conf)


def generate_synthetic_record(seq_id: int, base_date: datetime) -> dict:
    """Sinh một bản ghi giao dịch tài chính chuẩn theo cấu trúc PaySim."""
    tx_type = random.choices(
        TX_TYPES, weights=[0.35, 0.25, 0.20, 0.15, 0.05], k=1
    )[0]
    amount = round(random.uniform(10_000, 50_000_000), 2)
    old_bal = round(random.uniform(amount, amount + 100_000_000), 2)
    new_bal = (
        round(old_bal + amount, 2)
        if tx_type == "CASH_IN"
        else round(max(0.0, old_bal - amount), 2)
    )

    # Phân bổ qua 3 ngày để minh họa rõ Partition theo tx_date trên MinIO
    day_offset = seq_id % 3
    event_dt = base_date - timedelta(days=day_offset) + timedelta(
        seconds=random.randint(0, 86399)
    )

    return {
        "transaction_id": f"TXN-{event_dt.strftime('%Y%m%d')}-{seq_id:08d}-{uuid.uuid4().hex[:6].upper()}",
        "event_time": event_dt.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z",
        "step": (seq_id // 1000) + 1,
        "tx_type": tx_type,
        "amount": amount,
        "currency": "VND",
        "sender_id": f"C{random.randint(100000000, 999999999)}",
        "sender_old_balance": old_bal,
        "sender_new_balance": new_bal,
        "receiver_id": f"M{random.randint(100000000, 999999999)}",
        "payment_channel": random.choice(CHANNELS),
        "is_fraud_label": 1 if (tx_type in ("TRANSFER", "CASH_OUT") and amount > 42_000_000) else 0,
    }


def inject_fault(record: dict) -> dict:
    """Biến đổi bản ghi hợp lệ thành bản ghi lỗi để kiểm thử vùng Quarantine (DLQ)."""
    fault_mode = random.choice(["negative_amount", "missing_sender", "invalid_tx_type"])
    corrupted = dict(record)
    if fault_mode == "negative_amount":
        corrupted["amount"] = -abs(corrupted["amount"])
    elif fault_mode == "missing_sender":
        corrupted["sender_id"] = None
    elif fault_mode == "invalid_tx_type":
        corrupted["tx_type"] = "UNKNOWN_TYPE"
    return corrupted


def load_csv_records(csv_path: Path):
    """Đọc bản ghi từ file CSV mẫu hoặc file PaySim gốc."""
    with csv_path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for idx, row in enumerate(reader, start=1):
            yield {
                "transaction_id": row.get("transaction_id") or f"CSV-TXN-{idx:08d}",
                "event_time": row.get("event_time")
                or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z"),
                "step": int(row.get("step", 1)),
                "tx_type": row.get("type") or row.get("tx_type", "PAYMENT"),
                "amount": float(row.get("amount", 0.0)),
                "currency": row.get("currency", "VND"),
                "sender_id": row.get("nameOrig") or row.get("sender_id"),
                "sender_old_balance": float(row.get("oldbalanceOrg") or row.get("sender_old_balance", 0.0)),
                "sender_new_balance": float(row.get("newbalanceOrig") or row.get("sender_new_balance", 0.0)),
                "receiver_id": row.get("nameDest") or row.get("receiver_id"),
                "payment_channel": row.get("payment_channel", "MOBILE_APP"),
                "is_fraud_label": int(row.get("isFraud") or row.get("is_fraud_label", 0)),
            }


def run_producer(
    count: int,
    rate: int,
    fault_rate: float,
    dup_rate: float,
    csv_file: str | None = None,
) -> dict:
    producer = create_kafka_producer()
    base_date = datetime.now(timezone.utc)

    stats = {
        "total_sent": 0,
        "valid_sent": 0,
        "fault_injected": 0,
        "duplicates_sent": 0,
    }

    csv_iter = load_csv_records(Path(csv_file)) if csv_file else None
    start_time = time.perf_counter()

    print(
        f"[PRODUCER] Bắt đầu gửi {count:,} sự kiện vào topic '{KAFKA_TOPIC_TRANSACTIONS}' "
        f"(Tốc độ mục tiêu: {rate:,} msg/s | Tỷ lệ lỗi: {fault_rate*100:.1f}% | Tỷ lệ trùng: {dup_rate*100:.1f}%)"
    )

    for i in range(1, count + 1):
        try:
            record = next(csv_iter) if csv_iter else generate_synthetic_record(i, base_date)
        except StopIteration:
            record = generate_synthetic_record(i, base_date)

        # Kiểm tra xem có bơm lỗi (Fault Injection) hay không
        if random.random() < fault_rate:
            bad_record = inject_fault(record)
            key = str(bad_record.get("tx_type") or "ERROR").encode("utf-8")
            producer.produce(
                KAFKA_TOPIC_TRANSACTIONS,
                key=key,
                value=json.dumps(bad_record).encode("utf-8"),
            )
            stats["fault_injected"] += 1
            stats["total_sent"] += 1
        else:
            key = str(record["tx_type"]).encode("utf-8")
            payload = json.dumps(record).encode("utf-8")
            producer.produce(KAFKA_TOPIC_TRANSACTIONS, key=key, value=payload)
            stats["valid_sent"] += 1
            stats["total_sent"] += 1

            # Kiểm tra xem có gửi bản sao trùng lặp (Duplicate Injection) hay không
            if random.random() < dup_rate:
                producer.produce(KAFKA_TOPIC_TRANSACTIONS, key=key, value=payload)
                stats["duplicates_sent"] += 1
                stats["total_sent"] += 1

        if i % 1000 == 0:
            producer.poll(0)
            elapsed = time.perf_counter() - start_time
            expected_time = i / max(1, rate)
            if expected_time > elapsed:
                time.sleep(expected_time - elapsed)

    producer.flush()
    duration = max(0.001, time.perf_counter() - start_time)
    stats["duration_sec"] = round(duration, 3)
    stats["throughput_msg_sec"] = round(stats["total_sent"] / duration, 2)

    print(
        f"[PRODUCER] Hoàn tất! Tổng gửi: {stats['total_sent']:,} bản ghi trong {stats['duration_sec']}s "
        f"({stats['throughput_msg_sec']:,} msg/s) | Hợp lệ gốc: {stats['valid_sent']:,} | "
        f"Trùng lặp: {stats['duplicates_sent']:,} | Lỗi giả lập: {stats['fault_injected']:,}"
    )
    return stats


def main():
    parser = argparse.ArgumentParser(description="Kafka Financial Transaction Producer")
    parser.add_argument("--count", type=int, default=10000, help="Số lượng giao dịch gốc cần phát")
    parser.add_argument("--rate", type=int, default=2000, help="Tốc độ gửi tối đa (msg/sec)")
    parser.add_argument("--fault-rate", type=float, default=0.02, help="Tỷ lệ bản ghi lỗi giả lập (0.0 - 1.0)")
    parser.add_argument("--dup-rate", type=float, default=0.01, help="Tỷ lệ gửi lặp bản ghi (0.0 - 1.0)")
    parser.add_argument("--csv", type=str, default=None, help="Đường dẫn file CSV nguồn (nếu có)")
    args = parser.parse_args()

    try:
        run_producer(
            count=args.count,
            rate=args.rate,
            fault_rate=args.fault_rate,
            dup_rate=args.dup_rate,
            csv_file=args.csv,
        )
    except KeyboardInterrupt:
        print("\n[PRODUCER] Đã dừng theo yêu cầu người dùng.")
        sys.exit(0)


if __name__ == "__main__":
    main()
