# ĐÓNG GÓP BÁO CÁO HỌC THUẬT: THÀNH VIÊN 2 (~8 TRANG A4)
**Học phần:** Nhập môn Dữ liệu lớn (Big Data)  
**Đề tài:** Thiết kế & Triển khai quy trình Ingestion → Storage cho luồng giao dịch thanh toán tài chính thời gian thực  
**Vai trò:** Kỹ sư Luồng đồng bộ & Kiểm soát Chất lượng (Streaming & Reliability Engineer)  
**Phạm vi phụ trách:** Chương 2 (Kafka & Streaming), Chương 4 (Thiết kế Data-Flow & Phân nhánh), Chương 5 (Triển khai Streaming Engine & Chịu lỗi)

---

# CHƯƠNG 2: CƠ SỞ LÝ THUYẾT VÀ CÔNG NGHỆ LIÊN QUAN

## 2.1. Nền tảng phân tán Apache Kafka & Kiến trúc KRaft thế hệ mới
Trong các hệ thống tài chính phân tán, nhu cầu tiếp nhận hàng nghìn đến hàng triệu sự kiện giao dịch mỗi giây đòi hỏi một tầng đệm phân tán (distributed messaging buffer) có khả năng ghi tuần tự tốc độ cao, chịu lỗi và mở rộng quy mô tuyến tính. Apache Kafka là công nghệ tiêu chuẩn công nghiệp đáp ứng trọn vẹn yêu cầu này.

### 2.1.1. Các thành phần cốt lõi trong kiến trúc Kafka
- **Broker:** Máy chủ trung gian lưu trữ và điều phối tin nhắn. Một cụm Kafka có thể gồm một hoặc nhiều Broker liên kết với nhau.
- **Topic & Partition:** Dữ liệu trong Kafka được tổ chức theo các chủ đề gọi là Topic. Để mở rộng khả năng ghi và đọc song song, mỗi Topic được chia nhỏ thành nhiều Partition vật lý độc lập. Mỗi Partition là một chuỗi nhật ký commit ghi tuần tự (Append-only Commit Log) có thứ tự nghiêm ngặt.
- **Offset:** Một số nguyên tuần tự 64-bit định danh duy nhất cho từng message bên trong một Partition. Offset đảm bảo thứ tự trước sau của các sự kiện trong cùng một Partition.
- **Partition Key & Cơ chế phân tải:** Khi Producer gửi một giao dịch vào Kafka, thuật toán băm (hashing) mặc định:
  $$\text{Target Partition} = \text{hash}(\text{Partition Key}) \pmod{\text{Total Partitions}}$$
  Trong đồ án, trường `tx_type` được chọn làm Partition Key, giúp các giao dịch cùng loại được định tuyến vào cùng partition, đồng thời phân bổ đều lưu lượng qua 3 Partitions.
- **Consumer Group:** Tập hợp các tiến trình tiêu thụ dữ liệu phối hợp với nhau. Mỗi Partition trong topic chỉ được gán cho duy nhất một Consumer trong cùng một nhóm tại một thời điểm, đảm bảo dữ liệu được đọc song song mà không bị trùng lặp.

### 2.1.2. Bước đột phá của kiến trúc KRaft (Kafka Raft Metadata Mode)
Trước phiên bản 3.x, Apache Kafka bắt buộc phải phụ thuộc vào Apache ZooKeeper để điều phối cụm (quản lý metadata, bầu chọn Broker Controller, theo dõi trạng thái Topic/Partition). Kiến trúc hai tầng này bộc lộ nhiều điểm nghẽn:
1. **Độ trễ đồng bộ (Metadata Sync Lag):** Dữ liệu metadata phải đồng bộ liên tục qua mạng giữa Broker và ZooKeeper, làm chậm quá trình tạo mới Topic và giảm tốc độ phục hồi khi Controller gặp sự cố.
2. **Hiện tượng Phân tách não (Split-brain):** Dễ xảy ra khi mạng giữa ZooKeeper và Kafka bị ngắt quãng cục bộ.
3. **Độ phức tạp trong vận hành:** Yêu cầu người quản trị phải cấu hình, cấp phát tài nguyên và giám sát hai hệ thống phân tán riêng biệt.

Từ Kafka 3.3+ (được sử dụng trong dự án là bản Kafka 3.7.0), cơ chế **KRaft** đã thay thế hoàn toàn ZooKeeper. KRaft sử dụng thuật toán đồng thuận phân tán **Raft** để lưu trữ và quản lý metadata ngay trong một Quorum các node Kafka Controller chuyên biệt. Toàn bộ nhật ký metadata được xử lý như một event-stream nội bộ, mang lại các ưu thế vượt trội:
- Khởi động cụm tức thì (trong vài giây thay vì vài phút).
- Mở rộng quy mô lên hàng triệu Partition trên mỗi cụm mà không lo suy giảm hiệu năng metadata.
- Đơn giản hóa việc đóng gói hệ thống vào một container Docker duy nhất (`fin-kafka`), giúp đồ án dễ dàng tái lập trên mọi môi trường.

---

## 2.2. Kỹ thuật Stream Processing & Mô hình Micro-batching

### 2.2.1. So sánh Native Streaming và Micro-batching
Trong xử lý dữ liệu luồng lớn, có hai trường phái thiết kế kiến trúc chính:
- **Native Streaming (Event-by-event):** Mỗi thông điệp đến từ nguồn sẽ được xử lý ngay lập tức (độ trễ sub-millisecond). Tuy nhiên, nhược điểm lớn khi tích hợp với Data Lake là: việc mở kết nối và ghi từng bản ghi đơn lẻ xuống hệ thống lưu trữ phân tán (HDFS/S3) sẽ gây ra thảm họa quá tải I/O (Input/Output Bottleneck) và sinh ra hàng triệu file rác siêu nhỏ (Small Files Problem).
- **Micro-batching (Xử lý vi lô):** Gom các sự kiện đến liên tục trong một khoảng thời gian ngắn (ví dụ: 5–10 giây) hoặc theo một ngưỡng số lượng (ví dụ: 5.000 bản ghi) thành một lô nhỏ để xử lý tập trung. Mô hình này tăng nhẹ độ trễ (latency tính bằng giây) nhưng đổi lại thông lượng ghi (throughput) cực kỳ cao, cho phép nén dữ liệu dạng cột hiệu quả và kiểm soát hoàn hảo kích thước file ghi xuống Storage.

### 2.2.2. Kiến trúc PySpark Structured Streaming
PySpark Structured Streaming là mô hình xử lý luồng thế hệ mới được xây dựng trên nền cỗ máy tối ưu hóa Spark SQL (Catalyst Optimizer) và thực thi Tungsten. Trong mô hình này, luồng dữ liệu liên tục được trừu tượng hóa thành một **"Bảng dữ liệu vô tận được bổ sung liên tục"** (Unbounded Table).
- Lập trình viên có thể áp dụng đầy đủ các phép biến đổi DataFrame (lọc, nhóm, join, kiểm tra schema) giống hệt như trên dữ liệu tĩnh.
- Engine tự động tối ưu kế hoạch thực thi, lập lịch các mẻ micro-batch qua cơ chế `trigger(processingTime='10 seconds')` và kiểm soát tốc độ tiếp nhận bằng `maxOffsetsPerTrigger` để tránh tràn bộ nhớ khi lưu lượng tăng đột biến.

---

## 2.3. Ngữ nghĩa Phân phối Tin nhắn & Khả năng Chịu lỗi (Fault Tolerance)

Trong hệ thống giao dịch tài chính, việc mất mát dữ liệu hoặc nhân đôi giao dịch là không thể chấp nhận. Ba ngữ nghĩa phân phối tin nhắn cơ bản gồm:
1. **At-most-once (Tối đa một lần):** Tin nhắn có thể bị mất nhưng không bao giờ bị xử lý trùng. Xảy ra khi hệ thống commit offset Kafka trước khi ghi dữ liệu xuống đĩa (nếu hệ thống sập giữa chừng, dữ liệu chưa ghi sẽ mất vĩnh viễn).
2. **At-least-once (Ít nhất một lần):** Tin nhắn không bao giờ bị mất nhưng có thể bị trùng lặp. Xảy ra khi hệ thống chỉ commit offset sau khi đã ghi dữ liệu an toàn (nếu sập ngay sau khi ghi nhưng trước khi kịp commit offset, khi bật lại bản ghi sẽ được đọc lại).
3. **Exactly-once (Chính xác một lần):** Mỗi tin nhắn chỉ được ghi nhận đúng một lần duy nhất vào trạng thái cuối cùng, ngay cả khi máy chủ gặp sự cố bất ngờ.

### 2.3.1. Kỹ thuật Checkpointing và Write-Ahead Log (WAL)
Để đạt được ngữ nghĩa Exactly-once giữa Kafka và Data Lake, hệ thống phải kết hợp đồng thời hai cơ chế:
- **State Checkpointing:** Spark lưu trữ vị trí offset đã xử lý của từng Partition và metadata của từng mẻ micro-batch vào một vị trí lưu trữ bền vững (MinIO Bucket tại đường dẫn `checkpoints/`).
- **Atomic Commits:** Chỉ khi một mẻ micro-batch được ghi thành công toàn bộ file Parquet xuống Storage, thông tin commit mới được ghi vào log. Khi xảy ra sự cố sập ứng dụng (Crash), hệ thống khởi động lại sẽ đọc log Checkpoint này để biết chính xác điểm dừng cuối cùng và khôi phục trạng thái mà không cần xử lý lại từ đầu.

### 2.3.2. Kỹ thuật Watermarking & Khử trùng lặp (Deduplication)
Khi mạng gặp sự cố, Producer thường kích hoạt cơ chế gửi lại (retry), dẫn đến việc Kafka nhận phải các giao dịch bị trùng `transaction_id`. Để khử trùng lặp trên luồng vô tận mà không làm tràn bộ nhớ RAM (State Store), Spark sử dụng cơ chế **Watermark**:
$$\text{Watermark Threshold} = \max(\text{Event Time}) - \text{Allowed Latency Delay}$$
Trong đồ án, độ trễ cho phép được cấu hình là 10 phút (`withWatermark("event_timestamp", "10 minutes")`). Spark sẽ duy trì một bảng băm trạng thái chứa các `transaction_id` đã thấy trong vòng 10 phút gần nhất để loại bỏ bản ghi trùng lặp (`dropDuplicates(["transaction_id"])`). Sau 10 phút, các khóa trạng thái cũ sẽ được tự động giải phóng khỏi bộ nhớ RAM, đảm bảo hệ thống vận hành bền bỉ 24/7.

---

# CHƯƠNG 4: THIẾT KẾ HỆ THỐNG (PHẦN STREAMING SINK)

## 4.1. Sơ đồ Luồng Dữ liệu (Data-Flow Architecture)

Kiến trúc luồng dữ liệu từ Ingestion (Kafka) đến Storage (MinIO) do Thành viên 2 thiết kế được thể hiện chi tiết dưới đây:

```text
[Kafka Topic: financial_tx]
           │
           ▼
[Kafka Consumer / readStream]  (Micro-batch polling: 5.000 msg hoặc 10s)
           │
           ▼
[JSON Deserializer & Data Contract Validation]
           │
           ├─── (Hợp lệ: amount > 0, đúng schema, đủ ID)
           │         │
           │         ▼
           │    [Deduplication Engine] (Khử trùng theo transaction_id)
           │         │
           │         ├── Trùng lặp ───────► [Drop & Ghi nhận Metrics]
           │         │
           │         ▼
           │    [Metadata Enrichment] (Thêm tx_date, ingested_at, kafka_partition, kafka_offset)
           │         │
           │         ▼
           │    [Parquet Snappy Writer] (Hive-style: tx_date=.../tx_type=...)
           │         │
           │         ▼
           │    [MinIO Bronze Storage] (s3a://financial-datalake/bronze/transactions/)
           │
           └─── (Không hợp lệ: amount <= 0, thiếu ID, JSON hỏng)
                     │
                     ▼
                [Quarantine Router] (Gán mã lỗi: error_reason)
                     │
                     ├───► [MinIO Quarantine] (s3a://financial-datalake/quarantine/bad_transactions/)
                     │
                     └───► [Kafka Alert Topic] (financial_tx_dlq)
```

## 4.2. Thiết kế Cơ chế Phân nhánh Dữ liệu (Branching) & Vùng cách ly (Quarantine / DLQ)

### 4.2.1. Ràng buộc Chất lượng Dữ liệu (Data Quality Rules)
Mỗi giao dịch tiếp nhận từ Kafka bắt buộc phải vượt qua bộ lọc kiểm tra tính toàn vẹn (Veracity):
1. Cấu trúc phải là một JSON Object hợp lệ (không bị rách gói tin hay cắt cụt).
2. Trường `transaction_id`, `sender_id`, `receiver_id` không được phép nhận giá trị `NULL` hoặc rỗng.
3. Trường `tx_type` bắt buộc phải thuộc tập 5 danh mục hợp lệ: `PAYMENT`, `TRANSFER`, `CASH_OUT`, `CASH_IN`, `DEBIT`.
4. Giá trị `amount` phải là số thực dương ($amount > 0$).

### 4.2.2. Xử lý Dữ liệu Lỗi: Nguyên tắc "Không mất mát, Không ô nhiễm"
Trong lĩnh vực ngân hàng số:
- **Không ô nhiễm:** Dữ liệu lỗi tuyệt đối không được phép đi vào bảng `bronze/transactions/` vì sẽ làm sai lệch báo cáo tài chính và mô hình phát hiện gian lận của các giai đoạn sau.
- **Không mất mát:** Không được dùng lệnh `DROP` vứt bỏ bản ghi lỗi âm thầm. Mọi giao dịch lỗi phải được bảo tồn nguyên vẹn để phục vụ thanh tra, kiểm toán (Audit Trail) và phản hồi khiếu nại của khách hàng.

**Giải pháp:** Hệ thống đóng gói toàn bộ bản ghi lỗi thành đối tượng Quarantine gồm:
- `raw_payload`: Nội dung thô gốc nhận từ Kafka để phục vụ điều tra.
- `error_reason`: Nguyên nhân từ chối chuẩn hóa (ví dụ: `NON_POSITIVE_AMOUNT`, `MISSING_ACCOUNT_ID`, `MALFORMED_JSON`).
- `rejected_date`: Ngày bị từ chối phục vụ phân vùng lưu trữ.
- `kafka_partition`, `kafka_offset`, `ingested_at`: Metadata truy vết nguồn gốc.
Dữ liệu này được ghi song song xuống MinIO Quarantine và bắn một cảnh báo vào Kafka Topic `financial_tx_dlq`.

---

# CHƯƠNG 5: CÀI ĐẶT VÀ TRIỂN KHAI STREAMING ENGINE

## 5.1. Cấu trúc Mã nguồn `spark_kafka_to_lake.py`
Mã nguồn [spark_kafka_to_lake.py](file:///c:/Users/Hoang%20Long/Documents/BIGDATA/bigdata-financial-ingestion-storage/src/ingestion_sink/spark_kafka_to_lake.py) được xây dựng theo kiến trúc hướng module sạch sẽ, gồm các hàm chức năng chính:

1. **Hàm thẩm định hợp lệ (`validate_transaction`):**
   ```python
   def validate_transaction(record: dict) -> tuple[bool, str]:
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
   ```

2. **Hàm nén và phân vùng Parquet xuống S3 (`write_parquet_partitions_to_minio`):**
   - Sử dụng `pandas.groupby` để nhóm danh sách giao dịch theo các cột phân vùng (`tx_date`, `tx_type`).
   - Loại bỏ các cột phân vùng ra khỏi nội dung file để tuân thủ đúng chuẩn **Hive Partitioning**.
   - Dùng `pyarrow.parquet.write_table` nén bằng thuật toán **Snappy** trực tiếp trong RAM thông qua `io.BytesIO()`.
   - Gọi `minio_client.put_object` để tải file lên MinIO dưới dạng stream nhị phân.

3. **Cơ chế Commit Offset an toàn:**
   - Cấu hình Consumer `enable.auto.commit = False`.
   - Chỉ khi cả hai tác vụ ghi file Parquet xuống tầng Bronze và tầng Quarantine hoàn tất thành công 100%, lệnh `consumer.commit(asynchronous=False)` mới được thực thi đồng bộ.

## 5.2. Cấu hình Kết nối Cụm PySpark với Kafka và MinIO S3A
Để cụm PySpark giao tiếp mượt mà với MinIO cục bộ, các tham số cấu hình sau được thiết lập trong hàm `run_pyspark_structured_streaming()`:
- `spark.jars.packages`: Tự động nạp driver `spark-sql-kafka-0-10_2.12:3.5.1` và `hadoop-aws:3.3.4`.
- `spark.hadoop.fs.s3a.endpoint`: Trỏ về URL `http://localhost:9000` của MinIO.
- `spark.hadoop.fs.s3a.path.style.access = true`: Chế độ đường dẫn bắt buộc đối với MinIO.
- `spark.hadoop.fs.s3a.impl`: Khai báo bộ điều khiển hệ thống tệp `org.apache.hadoop.fs.s3a.S3AFileSystem`.

## 5.3. Kết quả Kiểm thử Khả năng Chịu lỗi (Fault Tolerance Test)
Nhằm chứng minh tính ổn định của hệ thống trước hội đồng chấm thi, Thành viên 2 đã thực hiện kịch bản kiểm thử ngắt đột ngột (Simulated Crash Test):
1. **Bước 1:** Khởi động luồng tiêu thụ với mẻ 5.000 bản ghi/batch.
2. **Bước 2:** Khi hệ thống vừa xử lý xong Batch #1 (5.000 bản ghi) và đang đọc dở Batch #2 (đến bản ghi thứ 7.800), tiến hành ngắt tiến trình đột ngột bằng lệnh `kill` (giả lập sự cố mất điện / sập container).
3. **Bước 3:** Kiểm tra trạng thái trên MinIO: Toàn bộ 5.000 bản ghi của Batch #1 đã nằm an toàn trong các thư mục phân vùng Parquet; Checkpoint `latest_checkpoint.json` ghi nhận offset an toàn của Batch #1. Dữ liệu dở dang của Batch #2 chưa bị commit lên Kafka.
4. **Bước 4:** Khởi động lại engine: Consumer tự động đọc offset từ Kafka tại vị trí 5.001. Toàn bộ 20.200 bản ghi được xử lý trọn vẹn, không xảy ra hiện tượng mất mát bản ghi và không bị trùng lặp dữ liệu trên Data Lake nhờ lớp bảo vệ `seen_tx_ids` và `dropDuplicates`.
