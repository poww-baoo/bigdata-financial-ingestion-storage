# Phần thực hiện của thành viên 3 — Storage & Data Lake

## 1. Vai trò trong hệ thống

Luồng tổng thể: **Người 1 phát giao dịch → Kafka → Người 2 kiểm tra/lọc trùng → Người 3 quản lý dữ liệu lưu trên MinIO → Người 4 đo hiệu năng**.

Hình dung MinIO là kho hàng. Bucket là kho, partition là các ngăn theo ngày và loại giao dịch, Parquet là cách đóng gói dữ liệu tiết kiệm dung lượng. Người 3 tổ chức kho, gom các gói nhỏ và kiểm kê xem dữ liệu đã lưu có đúng không.

Người 3 không quyết định giao dịch nào gian lận. Trường `is_fraud_label` là nhãn có sẵn; lọc lỗi và khử trùng trên luồng do người 2 thực hiện. Truy vấn người 3 giúp phát hiện lại sai lệch ở đầu ra.

## 2. Các sản phẩm đã hoàn thiện

| File | Làm gì | Vì sao cần |
| --- | --- | --- |
| `src/storage_management/init_minio_buckets.py` | Tạo bucket nếu chưa có, gỡ policy truy cập ẩn danh, thống kê số file/dung lượng theo partition và vùng lỗi | Chuẩn bị và kiểm kê nơi lưu giao dịch |
| `docker-compose.yml` — `minio-init` | Khởi tạo bucket riêng tư, nhận cấu hình từ biến môi trường, dừng khi lệnh khởi tạo lỗi | Đồng bộ cấu hình khởi động với script Python |
| `src/storage_management/compact_small_files.py` | Xem kế hoạch hoặc gộp file nhỏ cùng partition, ghi Snappy, kiểm tra số dòng/schema sau upload rồi mới xóa nguồn | Giảm số lần mở file khi truy vấn |
| `src/storage_management/query_verification.py` | Đọc Parquet từ MinIO bằng DuckDB, thống kê và xuất CSV/JSON; hỗ trợ dữ liệu local để kiểm thử | Đối soát và bàn giao dữ liệu cho nhóm Processing |
| `tests/test_storage_management.py` | Kiểm tra gộp không đổi dữ liệu, chạy lại, lỗi giữa chừng và đối soát SQL | Phát hiện mất/trùng dữ liệu do thao tác lưu trữ |

## 3. Cơ sở lý thuyết cho báo cáo

**Data Lake** lưu các file dữ liệu trong object storage. MinIO cung cấp API tương thích S3 để các công cụ dùng chung một nơi lưu. Bản triển khai này dùng Parquet thuần; chưa tích hợp Delta Lake hay giao dịch ACID. Một container MinIO trong Compose phục vụ demo, chưa chứng minh khả năng chịu lỗi của cụm lưu trữ nhiều node.

**Parquet** tổ chức dữ liệu theo cột. Ví dụ truy vấn chỉ cần `amount` và `currency` thì công cụ có thể đọc các cột đó thay vì toàn bộ bản ghi. Nén Snappy giảm dung lượng; mức giảm thực tế phải đo, không mặc định khẳng định một tỷ lệ cụ thể.

**Partitioning** chia dữ liệu vào thư mục `tx_date/tx_type`. Khi lọc một ngày và loại giao dịch, DuckDB/Spark có thể bỏ qua những thư mục khác (partition pruning). Không partition theo `transaction_id` vì quá nhiều giá trị sẽ tạo rất nhiều thư mục/file nhỏ.

**Small files** xuất hiện khi mỗi micro-batch ghi vài file. Ví dụ 100 file chứa mỗi file 100 giao dịch khiến hệ thống phải mở 100 file; gộp thành ít file hơn vẫn giữ nguyên 10.000 giao dịch nhưng giảm chi phí liệt kê/mở file. Compaction không khử trùng và không lọc dữ liệu.

## 4. Data contract đầu ra và thiết kế lưu trữ

```text
financial-datalake/
├── bronze/transactions/
│   └── tx_date=2026-11-09/tx_type=TRANSFER/part-....snappy.parquet
├── quarantine/bad_transactions/
│   └── rejected_date=2026-11-09/part-....snappy.parquet
├── checkpoints/transactions_stream_chk/
└── maintenance/compaction/       # Journal phục hồi khi gộp file lỗi
```

Các prefix chỉ xuất hiện khi có object; S3 không cần tạo thư mục rỗng. Người 2 đã ghi theo `tx_date/tx_type` và bỏ hai cột partition ra khỏi nội dung file. Người 3 sử dụng đúng thiết kế này; DuckDB khôi phục các cột từ đường dẫn bằng `hive_partitioning=true`.

| Nhóm trường | Trường | Ý nghĩa / kiểu logic |
| --- | --- | --- |
| Định danh | `transaction_id`, `sender_id`, `receiver_id` | Chuỗi, truy vết giao dịch và tài khoản |
| Thời gian | `event_time`, `step` | Thời điểm giao dịch và bước mô phỏng |
| Nội dung | `amount`, `currency`, `tx_type`, `payment_channel` | Số tiền, đơn vị tiền, loại giao dịch, kênh |
| Số dư | `sender_old_balance`, `sender_new_balance` | Số thực, số dư trước/sau |
| Nhãn | `is_fraud_label` | Số nguyên 0/1 từ dữ liệu nguồn |
| Partition | `tx_date`, `tx_type` | Ngày ISO YYYY-MM-DD và loại giao dịch từ đường dẫn |
| Kiểm toán | `ingested_at`, `kafka_partition`, `kafka_offset` | Thời điểm tiếp nhận và vị trí message gốc |

Lưu ý tích hợp: engine microbatch hiện lưu thời gian dưới dạng chuỗi ISO và kiểu số suy ra từ pandas; engine PySpark có thể lưu timestamp và integer khác độ rộng. File `schema.csv` cho biết kiểu đọc thực tế. Không trộn hai engine vào cùng dataset nếu chưa chuẩn hóa schema. Compaction từ chối schema khác nhau để tránh âm thầm đổi kiểu.

`amount` hiện là số thực theo contract dự án; `ROUND(SUM(amount), 2)` phục vụ đối soát demo, không thay thế mô hình tiền tệ decimal cho hệ thống kế toán. Luôn nhóm tổng tiền theo `currency`; không cộng VND và USD thành một tổng rồi gắn nhãn VND.

Nhóm Processing đọc `s3://financial-datalake/bronze/transactions/*/*/*.parquet` bằng DuckDB hoặc prefix tương ứng `s3a://` bằng Spark với quyền S3. Không đọc checkpoints hoặc maintenance như dữ liệu nghiệp vụ.

## 5. Cách chạy và bàn giao

Từ thư mục gốc dự án, sau khi cài dependencies và khởi động MinIO:

```bash
python -m src.storage_management.init_minio_buckets
python -m src.storage_management.query_verification --output-dir docs/storage_verification
python -m src.storage_management.compact_small_files
```

Lệnh thứ ba mặc định chỉ in kế hoạch, không sửa dữ liệu. Trước khi áp dụng, dừng job ingestion của người 2 và các reader, bảo đảm không còn tiến trình đang ghi/đọc Bronze:

```bash
python -m src.storage_management.compact_small_files --apply --writers-stopped --target-mb 128
python -m src.storage_management.query_verification --output-dir docs/storage_verification_after
```

`--writers-stopped` là xác nhận của người vận hành, không phải khóa tự động. Parquet thuần không có commit nguyên tử cho nhiều object; reader đang chạy có thể thấy dữ liệu lặp trong lúc đổi file. Nếu dùng Spark file sink có thư mục `_spark_metadata`, cần thiết kế lại metadata/compaction với người 2 trước khi dùng Spark streaming reader; script này hỗ trợ đọc lại bằng glob Parquet/DuckDB.

`128 MB` là ngưỡng tổng kích thước file nguồn đã nén trong một nhóm, không bảo đảm file đầu ra đúng 128 MB. Chỉ gộp nhóm có ít nhất hai file nhỏ. Script đọc từng file nguồn và ghi từng batch, không tải cả partition vào RAM; một file nguồn đã giải nén vẫn có thể lớn. Chọn ngưỡng phù hợp máy chạy.

Kết quả truy vấn:

- `schema.csv`: kiểu các cột thực tế.
- `totals.csv`: số dòng, số ID duy nhất, số dòng trùng, số dòng thiếu ID hoặc số tiền không hợp lệ.
- `by_partition.csv`: số lượng/tổng tiền theo ngày, loại giao dịch, tiền tệ.
- `by_channel.csv`: số lượng/tổng tiền theo ngày, kênh, tiền tệ.
- `sample.csv`: tối đa 20 dòng với đầy đủ các cột cho nhóm sau.
- `quarantine.csv`: số dòng cách ly theo ngày/lý do, khi có dữ liệu lỗi.
- `summary.json`: kết quả đạt/không đạt của đối soát Bronze.

Có thể thêm `--expected-records 98000` khi đã biết số lượng đầu ra đúng. Sai số lượng, ID trùng hoặc số tiền lỗi khiến lệnh thoát thất bại. Đây là kiểm tra đầu ra, không tự chứng minh exactly-once của toàn pipeline hay đối soát offset Kafka.

## 6. Xử lý khi compaction bị ngắt

Script ghi journal `maintenance/compaction/<id>.json` trước khi upload đầu ra; nếu bị ngắt, lần chạy tiếp theo dừng để tránh gộp cả nguồn lẫn đích gây trùng.

Giữ writer/reader dừng, đọc journal để biết `sources`, `destination`, `rows`:

1. Nếu tất cả nguồn vẫn tồn tại, có thể rollback: xóa destination nếu có, rồi xóa journal; chạy lại.
2. Nếu một số nguồn đã bị xóa, không xóa destination. Đọc destination, xác minh schema/số dòng bằng journal và kiểm tra dữ liệu đối soát, rồi xóa các nguồn còn lại trong danh sách journal; cuối cùng mới xóa journal.
3. Nếu destination hỏng và nguồn đã bị xóa, cần khôi phục từ backup. Journal không thay thế backup/versioning.

Không xóa journal tùy tiện. Script không tự khôi phục lỗi giữa chừng và không khóa nhiều tiến trình; chỉ chạy một tác vụ maintenance tại một thời điểm.

## 7. Kiểm chứng và ảnh minh chứng

Chạy kiểm thử độc lập:

```bash
python -m unittest discover -s tests -v
```

Đã kiểm tra với PyArrow/DuckDB thật và S3 giả lập: 3 file thành 1, giữ đủ 3 ID và tổng tiền 6; dry-run không đổi object; chạy lại không gộp thêm; lỗi lúc xóa giữ journal và chặn chạy lại; SQL phát hiện sai số lượng và ID trùng. Log nằm ở `docs/screenshots/tv3_verification_log.txt`.

Đã hoàn tất kiểm chứng trên **MinIO thật** ngày 10/11/2026. Máy không có Docker nên server MinIO được chạy trực tiếp trên Linux bằng binary lấy từ image `elestio/minio`, cùng nguồn image của Compose. Server phiên bản `RELEASE.2025-09-07T16-13-09Z`, API `http://localhost:9000`, Console `http://localhost:9001`. Dữ liệu runtime nằm ở `.local/tv3/minio-data/` (không đưa lên Git).

Dữ liệu kiểm chứng là 1.000 giao dịch tổng hợp từ CSV mẫu của dự án, ghi qua hàm Parquet của người 2 thành 5 micro-batch, cộng 6 bản ghi lỗi trong quarantine. Không cần Kafka cho kiểm chứng riêng Storage; đây không phải thí nghiệm throughput/toàn pipeline của người 4.

| Chỉ tiêu | Trước gộp | Sau gộp |
| --- | ---: | ---: |
| Giao dịch hợp lệ | 1.000 | 1.000 |
| ID giao dịch duy nhất | 1.000 | 1.000 |
| ID trùng / số tiền lỗi | 0 / 0 | 0 / 0 |
| Phân vùng ngày/loại | 9 | 9 |
| File Bronze | 45 | 9 |
| Bản ghi cách ly | 6 | 6 |
| Nén | Snappy | Snappy |

SHA-256 của toàn bộ dòng dữ liệu sắp xếp theo ID giữ nguyên; CSV tổng tiền theo ngày/loại và theo ngày/kênh/tiền tệ khớp trước/sau. Quarantine giữ nguyên cả object và nội dung. Dry-run không sửa dữ liệu; chạy apply lần hai không gộp thêm. GET không đăng nhập bị trả HTTP 403.

Kết quả máy đọc được: [`tv3_evidence/result.json`](tv3_evidence/result.json). Schema, số lượng, tổng tiền và mẫu bàn giao có trong [`tv3_evidence/after/`](tv3_evidence/after/). Chi tiết môi trường trong `tv3_evidence/environment.json`; log thật là `screenshots/tv3_minio_prepare_log.txt` và `screenshots/tv3_minio_finish_log.txt`.

Ảnh Console thật, không phải hình dựng:

- [`tv3_minio_buckets.png`](screenshots/tv3_minio_buckets.png): bucket riêng tư và cấu trúc Bronze/Quarantine.
- [`tv3_minio_partitions.png`](screenshots/tv3_minio_partitions.png): phân vùng ngày.
- [`tv3_minio_types_after.png`](screenshots/tv3_minio_types_after.png): phân vùng loại giao dịch.
- [`tv3_minio_before_compaction.png`](screenshots/tv3_minio_before_compaction.png): 5 file nhỏ trong một partition.
- [`tv3_minio_after_compaction.png`](screenshots/tv3_minio_after_compaction.png): còn một file gộp trong cùng partition.
- [`tv3_minio_quarantine_after.png`](screenshots/tv3_minio_quarantine_after.png): file vùng cách ly.

Tái lập với MinIO đang chạy và **bucket trống dành riêng kiểm chứng** (script từ chối seed nếu bucket có dữ liệu):

```bash
python -m src.storage_management.verify_minio_integration --prepare
# Chụp trước khi gộp; Chrome và playwright chỉ cần cho phần chụp ảnh.
PYTHONPATH=. python scripts/capture_tv3_minio.py --phase before
# Không chạy writer/reader khác trong lúc gộp.
python -m src.storage_management.verify_minio_integration --finish --writers-stopped
PYTHONPATH=. python scripts/capture_tv3_minio.py --phase after
```

Có thể đổi `MINIO_BUCKET_NAME` sang một bucket kiểm chứng khác bằng biến môi trường nếu kho chính đang có dữ liệu. Kết quả/ảnh được ghi lại theo lần chạy mới. Để chụp ảnh tự động: `pip install playwright`; script dùng Chrome có sẵn hoặc đường dẫn `--chrome`. Không cần chụp lại để dùng bộ minh chứng đã bàn giao.

## 8. Cách trình bày khi bảo vệ

“Em phụ trách tầng Storage. Dữ liệu sạch từ Spark được lưu vào MinIO dưới định dạng Parquet nén Snappy, chia theo ngày và loại giao dịch để giảm phần dữ liệu cần quét. Vì streaming tạo nhiều file nhỏ, em xây dựng compaction để gom chúng và kiểm tra file mới trước khi xóa nguồn. Cuối cùng em dùng DuckDB truy vấn trực tiếp dữ liệu đã lưu, đối soát số lượng, ID trùng và tổng tiền theo ngày/kênh/tiền tệ, đồng thời xuất schema và dữ liệu mẫu cho nhóm xử lý tiếp theo.”
