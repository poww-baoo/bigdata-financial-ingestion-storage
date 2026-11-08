# Đồ án Nhập môn Dữ liệu lớn: Quy trình Ingestion → Storage (Giao dịch Tài chính)

Dự án thiết kế và triển khai quy trình **Ingestion → Storage** cho luồng dữ liệu giao dịch thanh toán tài chính thời gian thực sử dụng **Apache Kafka (KRaft)**, **PySpark Structured Streaming / Micro-batch Engine**, **MinIO (S3 Data Lake)**, **Apache Parquet (Snappy)** và **DuckDB SQL**.

---

## 1. Cấu trúc Thư mục Dự án

```text
.
├── plan.md                              # Bản kế hoạch tổng thể & phân công 4 thành viên
├── docker-compose.yml                   # Hạ tầng Docker: Kafka (KRaft), Kafka-UI, MinIO
├── .env                                 # Cấu hình biến môi trường dùng chung
├── requirements.txt                     # Danh sách thư viện Python
├── src/
│   ├── config.py                        # Cấu hình trung tâm & Data Contract
│   ├── producer/
│   │   └── transaction_producer.py      # [Thành viên 1] Phát luồng giao dịch + Fault/Duplicate Injection
│   ├── ingestion_sink/
│   │   └── spark_kafka_to_lake.py       # [Thành viên 2] Đọc Kafka -> Validate/Dedup -> Ghi Parquet lên MinIO
│   ├── storage_management/
│   │   ├── init_minio_buckets.py        # [Thành viên 3] Kiểm tra cấu trúc Bucket & Partition trên MinIO
│   │   ├── compact_small_files.py       # [Thành viên 3] Gộp file Parquet nhỏ (Small Files Compaction)
│   │   └── query_verification.py        # [Thành viên 3] Truy vấn SQL (DuckDB) đối soát trực tiếp từ S3/MinIO
│   └── benchmark/
│       └── run_benchmarks.py            # [Thành viên 4] Chạy 4 kịch bản thực nghiệm & vẽ biểu đồ đánh giá
├── data/
│   └── sample_transactions.csv          # Dữ liệu giao dịch mẫu phục vụ kiểm thử nhanh
└── docs/
    ├── charts/                          # Biểu đồ kết quả thực nghiệm (.png)
    └── screenshots/                     # Ảnh chụp giao diện Kafka UI, MinIO Console, Terminal
```

---

## 2. Hướng dẫn Cài đặt & Chạy Demo Từng Bước (Khả năng tái lập - Mục 5.8)

### Bước 1: Khởi động hạ tầng Docker (Kafka + Kafka UI + MinIO)
```powershell
docker compose up -d
```
- **Kafka UI:** Truy cập `http://localhost:8080` (kiểm tra topic `financial_tx` gồm 3 Partitions và `financial_tx_dlq`).
- **MinIO Web Console:** Truy cập `http://localhost:9001` (Tài khoản: `minioadmin` / Mật khẩu: `minioadmin123`).

### Bước 2: Cài đặt thư viện Python
```powershell
pip install -r requirements.txt
```

### Bước 3: Phát luồng dữ liệu giao dịch vào Kafka (Thành viên 1)
Bơm `20.000` giao dịch với tốc độ `5.000 msg/s` (kèm 2% bản ghi lỗi giả lập và 1% bản ghi trùng lặp):
```powershell
python -m src.producer.transaction_producer --count 20000 --rate 5000 --fault-rate 0.02 --dup-rate 0.01
```

### Bước 4: Chạy luồng đồng bộ Ingestion → Storage (Thành viên 2)
Đọc từ Kafka, lọc bản ghi lỗi sang vùng cách ly (`quarantine`), khử trùng lặp theo `transaction_id`, và ghi bản ghi hợp lệ xuống MinIO dưới định dạng **Parquet (Snappy)** phân vùng theo `tx_date/tx_type`:
```powershell
python -m src.ingestion_sink.spark_kafka_to_lake --engine microbatch --batch-size 5000
```
*(Nếu chạy bằng cụm PySpark Structured Streaming đầy đủ: `python -m src.ingestion_sink.spark_kafka_to_lake --engine pyspark`)*

### Bước 5: Kiểm tra Phân vùng, Gộp file nhỏ & Truy vấn SQL đối soát (Thành viên 3)
```powershell
# 1. Xem thống kê các Partition và số file Parquet trên MinIO
python -m src.storage_management.init_minio_buckets

# 2. Gộp các file Parquet nhỏ trong từng Partition (Compaction)
python -m src.storage_management.compact_small_files

# 3. Truy vấn SQL trực tiếp trên MinIO bằng DuckDB để đối soát dữ liệu
python -m src.storage_management.query_verification
```

### Bước 6: Chạy Thực nghiệm Benchmark & Xuất Biểu đồ Báo cáo (Thành viên 4)
```powershell
python -m src.benchmark.run_benchmarks --records 50000
```
Các biểu đồ kết quả sẽ được lưu tự động tại `docs/charts/`:
- `exp2_storage_compression.png` (So sánh dung lượng Raw JSON vs CSV vs Parquet Snappy)
- `exp3_partition_pruning.png` (Tốc độ truy vấn SQL có và không có Partition Pruning)
- `exp4_veracity_accuracy.png` (Độ chính xác khử trùng & lọc lỗi Quarantine)
