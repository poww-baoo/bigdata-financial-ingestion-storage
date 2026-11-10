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
│   ├── sample_transactions.csv          # File mẫu đính kèm trên GitHub (10 dòng minh họa schema)
│   └── paysim_full.csv                  # [Tải từ Kaggle - ~493MB, 6.3M dòng] (Được gitignore vì >100MB)
└── docs/
    ├── charts/                          # Biểu đồ kết quả thực nghiệm (.png)
    └── screenshots/                     # Ảnh chụp giao diện Kafka UI, MinIO Console, Terminal
```

---

## 2. Nguồn Dữ liệu Lớn (Big Data Dataset) & Lưu ý quan trọng

Do GitHub giới hạn dung lượng mỗi file tối đa **100 MB**, trên repository chỉ đính kèm sẵn file mẫu `data/sample_transactions.csv` (theo đúng hướng dẫn tại **Mục 7** của đề cương: *"nộp đường dẫn nguồn dữ liệu, dữ liệu mẫu hoặc script sinh dữ liệu; không bắt buộc nộp toàn bộ dữ liệu lớn"*).

Khi chạy thực nghiệm Big Data để lấy số liệu báo cáo, nhóm sử dụng **1 trong 2 nguồn dữ liệu lớn** sau:

1. **Cách A – Dùng bộ dữ liệu thực tế PaySim từ Kaggle (6.362.620 giao dịch, ~493 MB):**
   - **Link tải chính thức:** [https://www.kaggle.com/datasets/ealaxi/paysim1](https://www.kaggle.com/datasets/ealaxi/paysim1)
   - Sau khi tải về, giải nén và đổi tên file CSV thành `data/paysim_full.csv` (file này đã được cấu hình trong `.gitignore` để không bị lỗi khi `git push`).
   - Chạy Producer phát trực tiếp từ file thật:
     ```powershell
     python -m src.producer.transaction_producer --csv data/paysim_full.csv --count 500000 --rate 5000
     ```

2. **Cách B – Dùng Script tự sinh hàng trăm nghìn / hàng triệu giao dịch (Không cần tải CSV 500MB):**
   - Nếu không truyền tham số `--csv`, `transaction_producer.py` sẽ tự động sinh luồng giao dịch lớn theo đúng phân phối của PaySim:
     ```powershell
     python -m src.producer.transaction_producer --count 200000 --rate 5000
     ```

---

## 3. Hướng dẫn Cài đặt & Chạy Demo Từng Bước (Khả năng tái lập - Mục 5.8)

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

# 2. Xem kế hoạch gộp file nhỏ (chưa thay đổi dữ liệu)
python -m src.storage_management.compact_small_files

# 3. Truy vấn SQL trực tiếp trên MinIO bằng DuckDB để đối soát dữ liệu
python -m src.storage_management.query_verification
```

Chi tiết phần người 3, cách áp dụng compaction khi đã dừng ingestion/reader và giải thích các khái niệm: [Tài liệu thành viên 3](docs/tv3_report_contribution.md).

Phần Storage đã được kiểm chứng trên MinIO thật: **1.000 giao dịch, 45 → 9 file, dữ liệu và tổng tiền giữ nguyên, 6 bản ghi cách ly**. Xem [kết quả kiểm chứng](docs/tv3_evidence/result.json), [dữ liệu bàn giao](docs/tv3_evidence/after/) và ảnh [trước](docs/screenshots/tv3_minio_before_compaction.png)/[sau gộp](docs/screenshots/tv3_minio_after_compaction.png).

### Bước 6: Chạy Thực nghiệm Benchmark & Xuất Biểu đồ Báo cáo (Thành viên 4)
```powershell
python -m src.benchmark.run_benchmarks --records 50000
```
Các biểu đồ kết quả sẽ được lưu tự động tại `docs/charts/`:
- `exp2_storage_compression.png` (So sánh dung lượng Raw JSON vs CSV vs Parquet Snappy)
- `exp3_partition_pruning.png` (Tốc độ truy vấn SQL có và không có Partition Pruning)
- `exp4_veracity_accuracy.png` (Độ chính xác khử trùng & lọc lỗi Quarantine)
