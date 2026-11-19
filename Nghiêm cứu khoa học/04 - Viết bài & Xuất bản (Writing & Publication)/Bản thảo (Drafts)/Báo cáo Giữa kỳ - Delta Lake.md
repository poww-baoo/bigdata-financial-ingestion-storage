# BÁO CÁO BÀI TẬP GIỮA KỲ
**Cơ sở đào tạo:** Trường Đại học Sài Gòn – Khoa Công nghệ Thông tin  
**Học phần:** Phương pháp nghiên cứu khoa học trong Công nghệ thông tin  
**Đề tài:** Phân tích và Trực quan hóa bài báo khoa học: *"Delta Lake: High-Performance ACID Table Storage over Cloud Object Stores"*  
**Sinh viên thực hiện:** Võ Huỳnh Minh Sang | **Lớp:** DCT123C4 | **MSSV:** 3123411256  
**Giảng viên hướng dẫn:** Vũ Ngọc Thanh Sang  
**Ngày thực hiện:** 2026-11-10  
---

# PHẦN 1: THÔNG TIN VÀ NGUỒN BÀI BÁO (Item 1.1)

### 1. Tên bài báo (Paper Title)
* **Tiếng Anh:** *Delta Lake: High-Performance ACID Table Storage over Cloud Object Stores*
* **Dịch nghĩa tiếng Việt:** *Delta Lake: Tầng lưu trữ bảng hỗ trợ giao dịch ACID hiệu năng cao trên hệ thống lưu trữ đối tượng đám mây*

---

### 2. Danh sách tác giả & Cơ quan công tác (Authors & Affiliations)
Đội ngũ gồm 21 tác giả đến từ doanh nghiệp tiên phong và các viện/trường đại học danh tiếng hàng đầu thế giới:
* **Nhóm tác giả chính từ Databricks:** Michael Armbrust, Tathagata Das, Liwen Sun, Burak Yavuz, Shixiong Zhu, Mukul Murthy, Joseph Torres, Herman van Hövell, Adrian Ionescu, Alicja Łuszczak, Michał Świtakowski, Michał Szafrański, Xiao Li, Takuya Ueshin, Mostafa Mokhtar, Sameer Paranjpye, Pieter Senster, Reynold Xin, Matei Zaharia.
* **Cơ quan học thuật hợp tác:**
  * **Peter Boncz:** Viện CWI Amsterdam (Centrum Wiskunde & Informatica, Hà Lan) – Viện nghiên cứu quốc gia về Toán & Khoa học máy tính, chuyên gia hàng đầu thế giới về cơ sở dữ liệu dạng cột (Columnar Databases).
  * **Ali Ghodsi:** Đại học California, Berkeley (UC Berkeley, Hoa Kỳ) – Đồng sáng lập & CEO Databricks, cựu nhà nghiên cứu tại AMPLab.
  * **Matei Zaharia:** Đại học Stanford (Stanford University, Hoa Kỳ) & Databricks – Giáo sư Khoa học Máy tính tại Stanford, người sáng lập Apache Spark.
* **Email liên hệ nhóm tác giả:** `delta-paper-authors@databricks.com`

---

### 3. Tên tạp chí / Kỷ yếu hội nghị (Journal / Proceedings)
* **Tên chính thức:** *Proceedings of the VLDB Endowment (PVLDB)*
* **Nhà xuất bản:** VLDB Endowment & ACM (Association for Computing Machinery)
* **Mã số tiêu chuẩn quốc tế (ISSN):** `2150-8097`
* **Quy cách xuất bản:** Tập 13 (Volume 13), Số 12 (Issue 12), Tháng 8/2020, Trang: 3411 – 3424.
* **Ghi chú về uy tín:** PVLDB là ấn phẩm định kỳ kết hợp giữa tạp chí học thuật và hội nghị VLDB (Very Large Data Bases) – 1 trong 3 hội nghị/tạp chí đỉnh cao nhất thế giới trong ngành Khoa học Máy tính về Cơ sở Dữ liệu & Hệ thống Dữ liệu Lớn (cùng với ACM SIGMOD và IEEE ICDE), đạt chuẩn xếp hạng **CORE A\*** (hạng cao nhất tuyệt đối).

---

### 4. Năm công bố (Year of Publication)
* **Năm công bố chính thức:** **2020** (Tháng 8 năm 2020 tại hội nghị VLDB lần thứ 46).

---

### 5. DOI & Đường dẫn chính thức của bài báo (DOI & Official Links)
* **Mã định danh số (DOI):** [`10.14778/3415478.3415560`](https://doi.org/10.14778/3415478.3415560)
* **Đường dẫn chính thức tại VLDB Endowment:** [https://www.vldb.org/pvldb/vol13/p3411-armbrust.pdf](https://www.vldb.org/pvldb/vol13/p3411-armbrust.pdf)
* **Đường dẫn trên thư viện điện tử ACM Digital Library:** [https://dl.acm.org/doi/10.14778/3415478.3415560](https://dl.acm.org/doi/10.14778/3415478.3415560)
* **Bản lưu trữ offline trong Vault:** `01 - Tổng quan tài liệu (Literature Review)/Bài báo đã đọc (Papers)/Delta-Lake-VLDB2020.pdf`

---

### 6. Thông tin chứng minh ấn phẩm thuộc Scopus & Web of Science
* **Vị trí và minh chứng danh mục Scopus (Elsevier):**
  * Tạp chí *Proceedings of the VLDB Endowment* được Elsevier Scopus lập chỉ mục liên tục từ năm **2008 đến nay** (trạng thái Active).
  * Vị trí lưu trữ nguồn trên Scopus: Định danh tại trang hồ sơ nguồn (Source Profile) với mã **Scopus Source ID: `21100199855`** gắn liền mã tiêu chuẩn quốc tế **ISSN: `2150-8097`**.
  * Cổng tra cứu chính thức của Scopus: [Scopus Source Details - ID 21100199855](https://www.scopus.com/sourceid/21100199855).
  * Bài báo *"Delta Lake: High-Performance ACID Table Storage over Cloud Object Stores"* nằm tại Tập 13 (Volume 13), Số 12 (Issue 12), năm 2020 của tập san này, với mã định danh số quốc tế DOI: [`10.14778/3415478.3415560`](https://doi.org/10.14778/3415478.3415560).
* **Vị trí và minh chứng danh mục Web of Science (Clarivate):**
  * Vị trí lưu trữ nguồn trên Web of Science: Được ghi nhận chính thức trên cổng danh mục tạp chí cốt lõi **Clarivate Master Journal List** ([https://mjl.clarivate.com](https://mjl.clarivate.com)) khi tra cứu trực tiếp qua mã định danh **ISSN: `2150-8097`**.
  * Hệ thống Clarivate chứng nhận ấn phẩm nằm trong danh mục lõi **Web of Science Core Collection**, thuộc đồng thời hai phân nhóm: Danh mục Kỷ yếu Hội nghị Khoa học (*Conference Proceedings Citation Index - Science / CPCI-S*) và Danh mục Tạp chí Mới nổi (*Emerging Sources Citation Index / ESCI*).
  * Xếp hạng học thuật CORE: Bài báo được xếp hạng **A\*** (hạng xuất sắc cao nhất toàn cầu) theo tiêu chuẩn của Hội đồng Giáo sư và Nghiên cứu Điện toán Australasian.
* **Chỉ số trích dẫn thực tế:** Bài báo đạt hơn **350+ trích dẫn học thuật** (theo thống kê OpenAlex và Google Scholar), khẳng định tính ảnh hưởng sâu rộng trong giới học thuật lẫn công nghiệp.

---

### 7. Điểm CiteScore & Điểm IF (Impact Factor)
* **Điểm Scopus CiteScore:** Dao động trong khoảng **7.5 – 8.2** (xếp trong top các ấn phẩm được trích dẫn nhiều nhất của ngành Khoa học Máy tính).
* **Chỉ số trích dẫn 2 năm (2-year mean citedness):** **8.22** (theo OpenAlex Metrics).
* **Chỉ số h-index của ấn phẩm:** **204** (Ấn phẩm có chỉ số h-index trên 200 là minh chứng cho độ uy tín và mức độ tác động học thuật khổng lồ trên quy mô toàn cầu).

---

### 8. Lĩnh vực của bài báo & Phân hạng trên ScimagoJR (Scimago Journal Rank)
* **Liên kết tra cứu ScimagoJR:** [https://www.scimagojr.com/journalsearch.php?q=21100199855&tip=sid](https://www.scimagojr.com/journalsearch.php?q=21100199855&tip=sid)
* **Xếp hạng phân vị (Quartile):** Đạt phân hạng **Q1** (nhóm 25% ấn phẩm khoa học xuất sắc nhất) ở tất cả các chuyên ngành liên quan:
  1. **Computer Science: Information Systems** – Phân hạng **Q1**
  2. **Computer Science: Software** – Phân hạng **Q1**
  3. **Computer Science: Hardware and Architecture** – Phân hạng **Q1**
  4. **Computer Science: Computer Science (miscellaneous)** – Phân hạng **Q1**
* **Chỉ số SJR (Scimago Journal Rank):** Thường niên đạt mức ~**2.1 – 2.8**, thuộc nhóm tinh hoa (top-tier) của ngành Cơ sở dữ liệu và Kỹ thuật Dữ liệu phân tán.


---

# PHẦN 2: PHÂN TÍCH NỘI DUNG NGHIÊN CỨU (Item 1.2)

### 1. Bối cảnh và vấn đề nghiên cứu (Context & Problem Statement)
* **Bối cảnh (Context):**
  * Trong kỷ nguyên điện toán đám mây, các hệ thống lưu trữ đối tượng (Cloud Object Stores) như Amazon S3, Azure Blob Storage, Google Cloud Storage đã trở thành hạ tầng lưu trữ dữ liệu lớn nhất hành tinh nhờ chi phí cực thấp, độ bền dữ liệu cao (99.999999999%) và khả năng tách biệt hoàn toàn giữa tài nguyên tính toán (Compute) và lưu trữ (Storage).
  * Các tổ chức có xu hướng di chuyển toàn bộ kho dữ liệu (Data Warehouse) và hồ dữ liệu (Data Lake) lên Object Storage, sử dụng các định dạng tệp cột mở (như Apache Parquet, ORC) kết hợp với các công cụ xử lý phân tán như Apache Spark, Presto, Hive, AWS Athena.
* **Vấn đề nghiên cứu cốt lõi (Problem Statement):**
  * Về bản chất kỹ thuật, Cloud Object Stores chỉ là các **hệ thống lưu trữ Key-Value phân tán**, không phải là hệ thống tệp tin (File System) truyền thống:
    1. **Thiếu tính nguyên tử đa đối tượng (No multi-object atomicity):** Không thể thực hiện cập nhật đồng thời nhiều tệp tin một cách an toàn. Nếu một tác vụ ghi (write job) bị sập giữa chừng, bảng dữ liệu rơi vào trạng thái lỗi/hỏng (corrupted state).
    2. **Không có tính cô lập giao dịch (No transaction isolation):** Khi một tiến trình đang cập nhật/xóa dữ liệu, các tiến trình đọc (readers) sẽ đọc phải dữ liệu dở dang (dirty reads / partial updates).
    3. **Chi phí thao tác siêu dữ liệu cực lớn (Expensive metadata operations):** Thao tác liệt kê tệp (`LIST` operations) trên S3/Azure có độ trễ rất cao (chỉ trả về tối đa 1.000 khóa mỗi lần gọi). Khi bảng dữ liệu phình to lên hàng triệu tệp và hàng ngàn phân vùng (partitions), thời gian duyệt siêu dữ liệu thậm chí còn lâu hơn thời gian thực thi câu truy vấn.
    4. **Vấn đề tệp nhỏ (Small file problem):** Các pipeline truyền dữ liệu theo luồng (streaming ingestion) thường xuyên ghi ra hàng triệu tệp Parquet kích thước nhỏ (vài KB đến vài MB), làm suy giảm nghiêm trọng thông lượng đọc của hệ thống.

---

### 2. Khoảng trống nghiên cứu mà tác giả muốn giải quyết (Research Gap)
Trước khi Delta Lake ra đời, cộng đồng dữ liệu đã thử nhiều cách nhưng đều bộc lộ hạn chế lớn:
* **Cách tiếp cận 1: Quản lý dạng "Thư mục các tệp tin" (Directories of Files):** Mô hình cổ điển của Hive/Spark. Dùng cấu trúc đường dẫn thư mục để phân vùng. Hạn chế: Không hỗ trợ giao dịch ACID, không thể sửa/xóa từng dòng (DELETE/UPDATE/MERGE), dễ xung đột dữ liệu và chi phí quét siêu dữ liệu (directory listing) quá chậm.
* **Cách tiếp cận 2: Cơ sở dữ liệu chuyên dụng đóng kín (Custom Storage Engines / Data Warehouses):** Các hệ thống như Snowflake, Google BigQuery hay Redshift. Mặc dù hỗ trợ ACID nhưng lại lưu dữ liệu theo định dạng độc quyền (proprietary format), bắt buộc phải có máy chủ chạy liên tục (always-on servers) để quản trị trạng thái, không thể tận dụng trực tiếp định dạng tệp mở (Parquet) và gây phụ thuộc nhà cung cấp (vendor lock-in).
* **Khoảng trống tri thức (The Gap):** *Chưa có một giải pháp lưu trữ mã nguồn mở nào có thể cung cấp đầy đủ bảo đảm giao dịch ACID cấp cơ sở dữ liệu trên Cloud Object Storage mà hoàn toàn không cần duy trì cụm máy chủ quản trị siêu dữ liệu tập trung (serverless/stateless metadata architecture), đồng thời vẫn tương thích 100% với định dạng Parquet mở.*

---

### 3. Mục tiêu nghiên cứu (Research Objectives)
1. **Thiết kế tầng lưu trữ bảng giao dịch (ACID Table Storage Layer):** Xây dựng một hệ thống trung gian nằm trên Cloud Object Storage, mang lại đầy đủ 4 thuộc tính ACID (Atomicity, Consistency, Isolation, Durability) cho cả tác vụ đọc/ghi theo lô (Batch) lẫn theo luồng (Streaming).
2. **Kiến trúc phi máy chủ cho Siêu dữ liệu (Serverless Metadata):** Lưu trữ toàn bộ nhật ký giao dịch (Transaction Log) trực tiếp trên chính Object Store dưới dạng tệp dữ liệu mở, giúp hệ thống mở rộng quy mô độc lập mà không cần server điều phối trung tâm.
3. **Tối ưu hóa hiệu năng truy vấn phân tích (High-Performance Querying):** Cung cấp các kỹ thuật nén nhật ký, bỏ qua dữ liệu (Data Skipping dựa trên min/max stats) và sắp xếp không gian đa chiều (Z-Order Clustering) để tăng tốc độ truy vấn lên nhiều lần.
4. **Hợp nhất kiến trúc dữ liệu (Lakehouse Architecture):** Loại bỏ nhu cầu phải duy trì đồng thời 2 hệ thống song song (Data Lake cho lưu trữ rẻ + Data Warehouse cho phân tích ACID), tạo tiền đề cho kiến trúc **Data Lakehouse**.

---

### 4. Câu hỏi nghiên cứu & Giả thuyết khoa học (Research Questions & Hypotheses)
* **Câu hỏi nghiên cứu (RQ):**
  * *RQ1:* Làm thế nào để đạt được giao dịch tuần tự hóa (serializable transactions) trên các hệ thống lưu trữ dạng Key-Value vốn chỉ hỗ trợ tính nhất quán sau cùng (eventual consistency) mà không cần máy chủ điều phối trạng thái?
  * *RQ2:* Làm sao để giải quyết nút thắt cổ chai về độ trễ liệt kê tệp (`LIST` API latency) khi truy vấn trên các bảng dữ liệu khổng lồ chứa hàng triệu đối tượng Parquet?
  * *RQ3:* Việc bổ sung tầng quản trị giao dịch có làm suy giảm thông lượng ghi/đọc so với định dạng Parquet gốc hay không?
* **Giả thuyết nghiên cứu (Hypothesis):**
  * *"Bằng cách ghi tuần tự nhật ký giao dịch dạng Write-Ahead Log (WAL) kết hợp kiểm soát đồng thời lạc quan (Optimistic Concurrency Control) và nén định kỳ nhật ký thành tệp Parquet trực tiếp trên Cloud Storage, ta có thể đạt được bảo đảm ACID với chi phí siêu dữ liệu $O(1)$ mà không làm giảm thông lượng ghi/đọc của các engine phân tán."*

---

### 5. Đối tượng nghiên cứu (Object of Study)
* Đối tượng nghiên cứu chính: **Cơ chế lưu trữ và giao dịch dữ liệu bảng (Table Storage Engine)** trên nền tảng lưu trữ đối tượng đám mây (Cloud Object Stores).
* Môi trường thử nghiệm: Nền tảng điện toán đám mây Amazon Web Services (AWS S3) kết hợp cụm tính toán phân tán Apache Spark và Databricks Runtime.

---

### 6. Dữ liệu và Tập dữ liệu sử dụng (Datasets & Benchmarks)
Bài báo sử dụng các bộ dữ liệu chuẩn công nghiệp và dữ liệu thực tế:
1. **TPC-DS Benchmark (Transaction Processing Performance Council - Decision Support):**
   * Chuẩn công nghiệp số 1 thế giới để đánh giá hiệu năng kho dữ liệu phân tích (Decision Support Systems).
   * Kích thước thử nghiệm: Quy mô **1 TB** và bảng dữ liệu giao dịch `store_sales` quy mô **400 GB** (ở định dạng CSV/Parquet thô).
   * Tập truy vấn: Chuỗi bài kiểm tra toàn diện **TPC-DS Power Test** gồm hàng chục câu truy vấn phức tạp (joins, aggregations, window functions).
2. **Tập dữ liệu dòng nhật ký mạng (Network Flow Security Log Dataset):**
   * Dữ liệu mô phỏng bài toán an ninh mạng thực tế để kiểm tra thuật toán sắp xếp không gian đa chiều (Z-Ordering).
   * Gồm 100 đối tượng Parquet với hàng triệu bản ghi lưu lượng mạng.
3. **Tập dữ liệu kiểm thử tải phân vùng (Partition Scalability Test):**
   * Tập dữ liệu bảng được phân chia nhân tạo thành từ **1.000 đến 1.000.000 phân vùng (partitions)** nhằm kiểm tra giới hạn chịu tải siêu dữ liệu của các hệ thống.

---

### 7. Các biến số, đặc trưng và thông tin đầu vào quan trọng (Variables & Parameters)
* **Thông tin đầu vào trong nhật ký giao dịch (Delta Log Schema):**
  * `add`: Ghi nhận tệp Parquet mới được tạo kèm đường dẫn URI, kích thước tệp và siêu dữ liệu thống kê min/max của từng cột dữ liệu.
  * `remove`: Ghi nhận tệp Parquet bị đánh dấu xóa (logical deletion).
  * `commitInfo`: Thông tin thời gian commit, định danh phiên làm việc, người thực thi, loại thao tác (WRITE, MERGE, DELETE).
  * `metaData`: Thông tin schema bảng (tên cột, kiểu dữ liệu, ràng buộc).
* **Các đặc trưng trong thử nghiệm Z-Order:** 4 chiều tọa độ mạng gồm: `sourceIP`, `sourcePort`, `destIP`, `destPort`.
* **Biến số môi trường thực nghiệm:**
  * Cụm tính toán: 1 nút Master + 8 nút Worker chuẩn AWS `i3.2xlarge` (mỗi nút có 8 vCPU, 61 GiB RAM, ổ cứng SSD NVMe).
  * Số lượng phân vùng: Thang đo logarit từ $10^3, 10^4, 10^5$ đến $10^6$ partitions.

---

### 8. Phương pháp, thuật toán, mô hình và quy trình nghiên cứu (Methodology & Architecture)
Phương pháp nghiên cứu của nhóm tác giả dựa trên kỹ thuật **Thiết kế Hệ thống Thực nghiệm (Systems Design & Experimental Engineering)**:

```
[Ứng dụng: Spark / Presto / Hive / Flink]
                   │
                   ▼ (Delta Lake API / ACID Layer)
 ┌─────────────────────────────────────────────────────────┐
 │ 1. Optimistic Concurrency Control (OCC)                 │
 │ 2. Log Compaction (Checkpointing sang Parquet mỗi 10 commit)
 │ 3. Data Skipping (Dựa trên Min/Max Statistics trong Log) │
 │ 4. Z-Order Multidimensional Clustering                  │
 └─────────────────────────────────────────────────────────┘
                   │
                   ▼ (Cloud Object Store: S3 / Azure / GCS)
 ┌─────────────────────────────────────────────────────────┐
 │ _delta_log/                                             │
 │   ├── 000000.json, 000001.json (Giao dịch vi mô WAL)    │
 │   └── 000010.checkpoint.parquet (Gộp trạng thái $O(1)$) │
 │ part-0000.parquet, part-0001.parquet (Dữ liệu bảng gốc) │
 └─────────────────────────────────────────────────────────┘
```

* **1. Giao thức Nhật ký ghi trước (Write-Ahead Log - WAL):**
  * Mọi thay đổi trên bảng được ghi dưới dạng các tệp commit liên tiếp: `000000.json`, `000001.json` trong thư mục `_delta_log/`.
  * Trạng thái bảng tại thời điểm bất kỳ là kết hợp (replay) các hành động `add` và `remove` trong log.
* **2. Kiểm soát đồng thời lạc quan (Optimistic Concurrency Control - OCC):**
  * Tác vụ ghi giả định không có xung đột. Khi kết thúc, tiến trình cố gắng ghi tệp commit tiếp theo (ví dụ bản ghi thứ $k+1$).
  * Nếu tệp $k+1$ đã bị tiến trình khác tạo trước, tác vụ ghi sẽ kiểm tra xem thay đổi của nó có chồng lấn dữ liệu với commit trước không: nếu không, tự động đổi tên thành $k+2$ (Mutual Exclusion); nếu có xung đột thực sự, rollback an toàn và báo lỗi cho ứng dụng.
* **3. Nén nhật ký Checkpoint định kỳ:**
  * Cứ sau mỗi **10 commits**, hệ thống tự động tổng hợp trạng thái bảng và lưu thành 1 tệp Parquet duy nhất: `000010.checkpoint.parquet`.
  * Nhờ đó, các câu truy vấn sau này chỉ cần đọc tệp checkpoint gần nhất cộng thêm các tệp JSON lẻ phía sau, đưa độ phức tạp đọc siêu dữ liệu về thời gian hằng số $O(1)$.
* **4. Kỹ thuật Data Skipping & Z-Order Clustering:**
  * Delta Lake tự động tính toán giá trị `min/max` của 32 cột đầu tiên trong mỗi tệp Parquet và lưu trực tiếp vào transaction log.
  * Áp dụng đường cong Hilbert / Morton Z-curve để ánh xạ dữ liệu đa chiều (multi-dimensional) vào không gian tuyến tính 1 chiều, giúp bỏ qua (skip) đến 90%+ số lượng tệp không liên quan khi truy vấn có mệnh đề `WHERE` trên nhiều cột khác nhau.

---

### 9. Các chỉ số dùng để đánh giá kết quả (Evaluation Metrics)
1. **Query Runtime / Test Duration (Thời gian chạy truy vấn):** Đo bằng giây (seconds) hoặc giờ (hours) khi thực thi toàn bộ chuỗi truy vấn TPC-DS Power Test.
2. **Metadata Search Latency (Độ trễ tìm kiếm siêu dữ liệu):** Thời gian cần thiết để xác định danh sách các tệp Parquet cần đọc khi số lượng phân vùng tăng từ 1.000 đến 1.000.000.
3. **Data Skipping Efficiency (Hiệu suất bỏ qua dữ liệu):** Tỷ lệ phần trăm tệp Parquet được bỏ qua (không phải tải qua mạng) khi thực hiện câu truy vấn có điều kiện lọc:
   $$\text{Skipping Rate} = \frac{\text{Số tệp bị bỏ qua}}{\text{Tổng số tệp trong bảng}} \times 100\%$$
4. **Ingestion / Write Load Time (Thời gian ghi và nạp dữ liệu):** Thời gian nạp 400 GB dữ liệu thô vào bảng, đo bằng giây.

---

### 10. Những kết quả chính của nghiên cứu (Key Findings)
* **Khả năng mở rộng siêu dữ liệu vượt trội (Figure 4):**
  * Khi kích thước bảng đạt **1.000.000 phân vùng (partitions)**, Delta Lake phản hồi câu truy vấn chỉ trong **chưa đầy 10 giây**.
  * Trong khi đó, các hệ thống truyền thống (Apache Hive và Presto trên Parquet thuần) mất **hơn 1 giờ** hoặc hoàn toàn bị tràn bộ nhớ / treo hệ thống do nghẽn hàm `LIST` của Cloud Storage.
* **Tăng tốc độ truy vấn phân tích TPC-DS (Figure 6):**
  * Trên tập TPC-DS 1 TB, Spark chạy trên **Delta Lake (bật SSD cache)** hoàn thành chuỗi Power Test chỉ trong **0.93 giờ**, nhanh hơn gấp **1.55 lần** so với Spark chạy trên Parquet thuần (1.44 giờ) và nhanh hơn gấp **4.04 lần** so với dịch vụ Presto của bên thứ ba (3.76 giờ).
* **Hiệu quả tối ưu hóa Z-Ordering (Figure 5):**
  * Với phương pháp sắp xếp tuyến tính thông thường (Global Sort Order), hệ thống chỉ bỏ qua được tệp khi lọc theo cột đầu tiên (`sourceIP`: bỏ qua 99%), nhưng hoàn toàn bất lực (bỏ qua 0%) khi lọc theo 3 cột còn lại (`destIP`, `sourcePort`, `destPort`).
  * Khi kích hoạt **Z-Ordering**, Delta Lake đạt tỷ lệ bỏ qua tệp từ **44% đến 67% đồng đều trên tất cả các cột**, giúp tiết kiệm băng thông và tăng tốc truy vấn lọc đa chiều ngoạn mục.
* **Chi phí ghi không đáng kể (Zero-overhead Ingestion - Figure 7):**
  * Quá trình nạp 400 GB dữ liệu vào Delta Lake mất ~575 giây, tương đương hoàn toàn với Parquet thuần (~560 giây), chứng minh rằng việc thu thập siêu dữ liệu min/max và ghi Write-Ahead Log không tạo ra độ trễ đáng kể.


---

# PHẦN 3: VẼ LẠI 02 HÌNH MINH HỌA TỪ BÀI BÁO GỐC (Item 1.3)

---

## 3.1. HÌNH 1: SƠ ĐỒ KIẾN TRÚC PIPELINE DỮ LIỆU (FIGURE 1 BÀI BÁO)

### Hình ảnh tái tạo:
![[Hinh1_TaiTao_KienTruc_Pipeline.png]]
*(Tệp hình ảnh chất lượng cao lưu tại: `99 - Đính kèm (Attachments)/Hinh1_TaiTao_KienTruc_Pipeline.png` và bản vector `Hinh1_TaiTao_KienTruc_Pipeline.pdf`)*

---

### Thuyết minh chi tiết 7 nội dung theo yêu cầu:

#### 1. Vị trí hình gốc trong bài báo
* **Hình gốc:** Figure 1, xuất hiện tại **Trang 2** của bài báo (thuộc Phần 1: Giới thiệu & Phần 2: Động lực nghiên cứu).
* **Tiêu đề gốc:** *"Figure 1: A data pipeline implemented using three storage systems (a message queue, object store and data warehouse), or using Delta Lake for both stream and table storage. The Delta Lake version removes the need to manage multiple copies of the data and uses only low-cost object storage."*

#### 2. Mục đích của hình
* So sánh trực quan sự khác biệt mang tính kiến trúc giữa:
  * **Kịch bản (a):** Kiến trúc truyền thống kết hợp 3 hệ sinh thái lưu trữ độc lập (Message Queue cho Streaming + Object Store cho Batch/Raw + Data Warehouse cho BI/ACID).
  * **Kịch bản (b):** Kiến trúc tinh gọn và hợp nhất trên nền tảng Delta Lake (Lakehouse Architecture), chỉ sử dụng duy nhất một tầng lưu trữ đối tượng giá rẻ cho mọi nhu cầu.

#### 3. Các biến số và thông tin được thể hiện
* **Nguồn dữ liệu đầu vào (Data Inputs):** Dữ liệu nhật ký thay đổi cơ sở dữ liệu (`MySQL Change Log`) và dữ liệu cảm biến thời gian thực (`Sensor Data`).
* **Các thành phần lưu trữ trung gian:**
  * Kịch bản (a): Hàng đợi thông điệp (`Message Queue / Kafka`), Hồ dữ liệu đối tượng (`Cloud Object Store` với các bảng Parquet thô, lọc, tổng hợp), và Kho dữ liệu độc quyền (`Data Warehouses`).
  * Kịch bản (b): Duy nhất một tầng Cloud Object Store với các bảng Delta Lake đa tầng (Bronze - Silver - Gold).
* **Các tiến trình xử lý (Processing Jobs):** `ETL Job 1` (Streaming ingestion), `ETL Job 2` (Continuous aggregation), `ETL Job 3` (Batch ETL / ACID Upsert).
* **Đối tượng tiêu thụ dữ liệu cuối (Consumers):** Ứng dụng phân tích thời gian thực (`Streaming Analytics`), Người dùng nghiệp vụ thông minh (`BI Users / Dashboards`), và Các nhà khoa học dữ liệu (`Data Scientists / Machine Learning`).

#### 4. Cách thức sinh viên tái tạo hình
* **Công cụ thực hiện:** Sử dụng công cụ thiết kế đồ họa lập trình **Graphviz (ngôn ngữ DOT)** kết hợp với thư viện xử lý ảnh **Python (Pillow)**.
* **Quy trình tái tạo:**
  1. Phân tích cấu trúc logic các khối và luồng dữ liệu của hai sơ đồ (a) và (b) trong hình gốc.
  2. Lập trình file mô tả cấu trúc `figure1.dot`, định nghĩa các nút (nodes) với hình khối chuẩn (cylinder cho database, box3d cho message queue, folder cho dữ liệu cảm biến).
  3. Áp dụng bảng màu phân tầng có ý nghĩa học thuật rõ ràng (màu ấm cho đầu vào, màu xanh dương cho Delta Lake, màu xanh lá cho đầu ra).
  4. Biên dịch đồ họa vector và ghép nối theo trục dọc (vertical layout) để đảm bảo hình ảnh cân đối, trực quan và không bị méo mó khi chèn vào báo cáo.

#### 5. Ý nghĩa của kết quả được thể hiện
* Hình vẽ chỉ ra rõ ràng "nỗi đau" (pain point) lớn nhất của các kỹ sư dữ liệu trong kiến trúc truyền thống: dữ liệu bị nhân bản (duplicated) qua quá nhiều hệ thống, gây tốn kém chi phí lưu trữ gấp 3-4 lần, đồng thời tạo ra độ trễ lớn do phải chờ các job sao chép (export/import) chạy xong.
* Delta Lake giải quyết triệt để vấn đề này bằng cách cho phép các công cụ phân tích (BI, Data Science, Streaming) truy vấn trực tiếp trên một nguồn sự thật duy nhất (Single Source of Truth) trên Object Store.

#### 6. Kết luận khoa học rút ra từ hình
* Nhờ khả năng hỗ trợ giao dịch ACID và cơ chế đọc nối đuôi log (`Log Tailing`), một bảng dữ liệu trên Cloud Storage hoàn toàn có thể vừa đóng vai trò như một Message Queue vừa đóng vai trò như một bảng Data Warehouse.
* Khẳng định tính khả thi và ưu thế vượt trội của kiến trúc **Data Lakehouse** so với kiến trúc Lambda hoặc kiến trúc hai tầng truyền thống.

#### 7. Những điểm giống và khác giữa hình vẽ lại và hình trong bài báo
* **Điểm giống:** Giữ nguyên 100% bản chất luồng dữ liệu, tất cả các tác vụ ETL, các đối tượng tham gia và hai kịch bản so sánh đối chiếu (a) và (b).
* **Điểm khác biệt & cải tiến của sinh viên:**
  * **Việt hóa chú giải:** Toàn bộ thuật ngữ được dịch nghĩa chuẩn xác kèm thuật ngữ tiếng Anh trong ngoặc đơn để dễ theo dõi.
  * **Hệ thống màu sắc ngữ nghĩa:** Sử dụng màu sắc tương phản giúp phân biệt rõ từng tầng chức năng (Input -> Processing -> Storage -> Consumer).
  * **Bổ sung chuẩn kiến trúc Medallion:** Đưa vào phân loại tầng dữ liệu hiện đại (Bronze / Silver / Gold) trên các bảng Delta Lake để tăng tính ứng dụng thực tế.

---

## 3.2. HÌNH 2: BIỂU ĐỒ HIỆU NĂNG TPC-DS POWER TEST (FIGURE 6 BÀI BÁO)

### Hình ảnh tái tạo:
![[Hinh2_TaiTao_TPCDS_PowerTest.png]]
*(Tệp hình ảnh chất lượng cao lưu tại: `99 - Đính kèm (Attachments)/Hinh2_TaiTao_TPCDS_PowerTest.png` và bản vector `Hinh2_TaiTao_TPCDS_PowerTest.pdf`)*

---

### Thuyết minh chi tiết 7 nội dung theo yêu cầu:

#### 1. Vị trí hình gốc trong bài báo
* **Hình gốc:** Figure 6, xuất hiện tại **Trang 11** của bài báo (thuộc Mục 6.2: Đánh giá hiệu năng TPC-DS).
* **Tiêu đề gốc:** *"Figure 6: TPC-DS power test duration for Spark on Databricks and Spark and Presto on a third-party cloud service."*

#### 2. Mục đích của hình
* So sánh định lượng thời gian hoàn thành (Query Execution Duration) của bài kiểm tra chuẩn công nghiệp **TPC-DS Power Test** trên tập dữ liệu quy mô **1 TB** giữa 4 cấu hình hệ thống thực thi trên đám mây AWS.

#### 3. Các biến số và thông tin được thể hiện
* **Biến độc lập (Trục hoành X):** 4 cấu hình hệ thống thử nghiệm trên phần cứng tương đương (1 master + 8 worker nodes `i3.2xlarge`):
  1. *Databricks Runtime sử dụng Delta Lake* (có SSD cache).
  2. *Databricks Runtime sử dụng định dạng Parquet thuần*.
  3. *Dịch vụ đám mây bên thứ ba chạy Apache Spark trên Parquet*.
  4. *Dịch vụ đám mây bên thứ ba chạy Presto trên Parquet*.
* **Biến phụ thuộc (Trục tung Y):** Thời gian thực thi toàn bộ chuỗi truy vấn TPC-DS Power Test, đơn vị đo bằng **giờ (hours)**.
* **Số liệu đo đạc định lượng cụ thể:**
  * Databricks Delta Lake: **0.93 giờ** (~55.8 phút)
  * Databricks Parquet: **0.99 giờ** (~59.4 phút)
  * 3rd-Party Spark Parquet: **1.44 giờ** (~86.4 phút)
  * 3rd-Party Presto Parquet: **3.76 giờ** (~225.6 phút)

#### 4. Cách thức sinh viên tái tạo hình
* **Công cụ thực hiện:** Viết mã nguồn Python sử dụng thư viện trực quan hóa dữ liệu chuyên dụng **`matplotlib`**.
* **Quy trình tái tạo:**
  1. Trích xuất chính xác số liệu định lượng từ biểu đồ gốc và thuyết minh trong bài báo gốc.
  2. Xây dựng biểu đồ cột (Bar Chart) với tỷ lệ trục Y từ 0 đến 4.3 giờ, khoảng chia lưới (gridlines) nét đứt trang nhã.
  3. Giữ nguyên hoa văn nhận diện (hatch patterns: chấm bi cho Spark bên thứ ba, sọc chéo cho Presto) để đảm bảo tính trực quan ngay cả khi in ấn trên tài liệu đen trắng.
  4. Xuất file ảnh với mật độ điểm ảnh 300 DPI và file vector PDF.

#### 5. Ý nghĩa của kết quả được thể hiện
* Kết quả chứng minh rằng việc bổ sung tầng quản trị giao dịch ACID của Delta Lake hoàn toàn không làm giảm hiệu năng truy vấn, mà ngược lại còn giúp hệ thống chạy nhanh nhất (0.93 giờ).
* Cho thấy sự kết hợp giữa kỹ thuật tối ưu hóa truy vấn của Spark và khả năng bỏ qua dữ liệu (Data Skipping) của Delta Lake đem lại hiệu năng vượt trội áp đảo so với các công cụ truy vấn phân tán khác như Presto (3.76 giờ).

#### 6. Kết luận khoa học rút ra từ hình
* Databricks chạy Delta Lake đạt tốc độ nhanh hơn gấp **4.04 lần** so với dịch vụ Presto trên cùng một tập dữ liệu và hạ tầng phần cứng.
* Khi so sánh với phiên bản Spark của bên thứ ba chạy cùng định dạng Parquet, Databricks nhanh hơn **1.55 lần**, khẳng định giá trị của việc tối ưu hóa tầng tính toán gắn liền với tầng siêu dữ liệu.

#### 7. Những điểm giống và khác giữa hình vẽ lại và hình trong bài báo
* **Điểm giống:** Tái hiện trung thực 100% 4 cột giá trị định lượng (0.93h, 0.99h, 1.44h, 3.76h), giữ nguyên hệ quy chiếu trục tọa độ và các hoa văn phân biệt.
* **Điểm khác biệt & cải tiến của sinh viên:**
  * **Nhãn dữ liệu trực tiếp (Direct Data Labels):** Hiển thị rõ giá trị số liệu trên đầu từng cột, giúp người xem nắm bắt thông tin ngay mà không cần dóng mắt vào thang đo trục Y.
  * **Hộp chú thích tính toán trực quan (Callout Annotations):** Bổ sung 2 mũi tên chỉ báo làm nổi bật kết quả so sánh định lượng then chốt ("Nhanh hơn 4.04× vs Presto", "Nhanh hơn 1.55× vs Spark khác").
  * **Tiêu đề song ngữ:** Tiêu đề và nhãn trục được diễn giải chi tiết, rõ ràng hơn biểu đồ gốc trong bài báo.


---

# PHẦN 4: ĐỀ XUẤT VÀ XÂY DỰNG 01 HÌNH MINH HỌA MỚI (Item 2.4)

### Hình ảnh đề xuất mới:
![[Hinh3_DeXuatMoi_HeSoTangToc.png]]
*(Tệp hình ảnh chất lượng cao lưu tại: `99 - Đính kèm (Attachments)/Hinh3_DeXuatMoi_HeSoTangToc.png` và bản vector `Hinh3_DeXuatMoi_HeSoTangToc.pdf`)*

---

### Thuyết minh chi tiết 5 nội dung theo yêu cầu đề bài:

#### 1. Lý do đề xuất hình mới
* Trong bài báo gốc, tác giả trình bày kết quả thực nghiệm tại **Figure 6** dưới dạng biểu đồ cột đơn giản chỉ thể hiện thời gian chạy tuyệt đối (đơn vị: giờ: 0.93h, 0.99h, 1.44h, 3.76h).
* **Hạn chế của cách trình bày gốc:** Người đọc, người làm chính sách dữ liệu hoặc kỹ sư hệ thống nhìn vào số giờ thô sẽ phải tự thực hiện các phép tính nhẩm phức tạp để biết:
  * Hệ thống mới nhanh hơn hệ thống cũ bao nhiêu lần?
  * Thời gian chờ đợi của người dùng và chi phí thuê máy chủ đám mây (Cloud Compute Cost) được cắt giảm cụ thể bao nhiêu phần trăm?
* **Mục tiêu của hình đề xuất mới:** Xây dựng một biểu đồ kép chuẩn khoa học kết hợp hai khía cạnh then chốt: **(A) Hệ số tăng tốc hiệu năng (Speedup Factor)** và **(B) Tỷ lệ phần trăm thời gian truy vấn được tiết kiệm (% Time Saved)** nhằm cung cấp góc nhìn toàn diện, sắc bén và trực quan hóa trọn vẹn giá trị thực tế của Delta Lake.

---

#### 2. Dữ liệu và thông tin được sử dụng
* **Nguồn dữ liệu:** Trích xuất từ số liệu đo đạc thực nghiệm chuẩn **TPC-DS 1 TB Power Test** (chạy trên cụm 1 master + 8 worker nodes AWS `i3.2xlarge`) công bố trong Mục 6.2 và Figure 6 của bài báo gốc:
  * $T_{\text{Presto}} = 3.76$ giờ (13.536 giây) — được chọn làm mốc đối chứng chuẩn (Baseline = 1.0×).
  * $T_{\text{Spark\_3rdParty}} = 1.44$ giờ (5.184 giây).
  * $T_{\text{Databricks\_Parquet}} = 0.99$ giờ (3.564 giây).
  * $T_{\text{Databricks\_Delta}} = 0.93$ giờ (3.348 giây).
* **Công thức toán học áp dụng:**
  * **Hệ số tăng tốc (Speedup Factor):**
    $$\text{Speedup} = \frac{T_{\text{Presto}}}{T_{\text{Hệ thống}}}$$
    * Presto: $\frac{3.76}{3.76} = 1.00\times$ (Mốc tham chiếu).
    * Spark bên thứ ba: $\frac{3.76}{1.44} = 2.61\times$.
    * Databricks Parquet: $\frac{3.76}{0.99} = 3.80\times$.
    * Databricks Delta Lake: $\frac{3.76}{0.93} = 4.04\times$.
  * **Tỷ lệ phần trăm thời gian tiết kiệm (% Time Saved):**
    $$\% \text{ Time Saved} = \frac{T_{\text{Presto}} - T_{\text{Hệ thống}}}{T_{\text{Presto}}} \times 100\%$$
    * Presto: $0.0\%$ (Mốc chuẩn).
    * Spark bên thứ ba: $\frac{3.76 - 1.44}{3.76} \times 100\% = 61.7\%$.
    * Databricks Parquet: $\frac{3.76 - 0.99}{3.76} \times 100\% = 73.7\%$.
    * Databricks Delta Lake: $\frac{3.76 - 0.93}{3.76} \times 100\% = 75.3\%$.

---

#### 3. Cách thức xây dựng hình
* **Công cụ:** Lập trình kịch bản tự động bằng ngôn ngữ **Python** với thư viện đồ họa **`matplotlib`** và xử lý số học **`numpy`**.
* **Kỹ thuật thiết kế:**
  * Chia bố cục Subplot đối xứng $1 \times 2$ (ngang $13.5$ inch, cao $6.0$ inch), căn chỉnh lề tự động (`tight_layout`).
  * Phối màu có chủ đích: Màu xám trung tính cho mốc chuẩn Presto (1.0×), màu cam cho dịch vụ đám mây bên thứ ba, màu xanh dương tươi cho Databricks Parquet, và màu xanh đậm khẳng định vị thế dẫn đầu của Databricks Delta Lake.
  * Tích hợp nhãn số liệu trực tiếp trên từng thanh cột (In-bar Data Labels) và đường kẻ tham chiếu ngang (Horizontal Reference Line tại $y=1.0\times$).
  * Thiết kế hộp chú thích nổi bật (Callout Annotation) có mũi tên định hướng làm nổi bật kết luận: *"Rút ngắn 75.3% thời gian (Nhanh hơn gấp 4 lần)"*.
  * Xuất đồng thời 2 định dạng: file ảnh siêu nét PNG (300 DPI) và file vector PDF phục vụ in ấn chất lượng cao.

---

#### 4. Giá trị thông tin mà hình mới mang lại
1. **Lượng hóa rõ ràng mức độ vượt trội về hiệu năng:** Thay vì chỉ biết các khoảng thời gian lẻ tẻ, hình mới khẳng định ngay lập tức rằng Delta Lake giúp hệ thống chạy **nhanh hơn gấp 4 lần (4.04×)** so với giải pháp Presto phổ biến và **nhanh hơn 1.55×** so với phiên bản Apache Spark tiêu chuẩn.
2. **Góc nhìn Kinh tế Điện toán Đám mây (Cloud Cost Optimization):** 
   * Trên các nền tảng đám mây như AWS, chi phí tính toán được tính chính xác theo từng giây/giờ mà cụm máy chủ ảo (`EC2 i3.2xlarge`) hoạt động.
   * Việc tiết kiệm **75.3% thời gian chạy truy vấn** đồng nghĩa với việc doanh nghiệp có thể **cắt giảm tương ứng tới ~75% hóa đơn chi phí điện toán** cho các tác vụ phân tích dữ liệu quy mô lớn hàng ngày.
3. **Phân tách rạch ròi 2 tầng tối ưu hóa:**
   * Tầng công cụ tính toán (Compute engine): Chuyển từ Presto sang Spark giúp tăng tốc $2.61\times$.
   * Tầng lưu trữ bảng giao dịch (Storage layer): Kết hợp runtime tối ưu của Databricks và tầng Delta Lake nâng hệ số tăng tốc từ $2.61\times$ lên $4.04\times$.

---

#### 5. Hình mới bổ sung điều gì so với cách trình bày của bài báo gốc
* **Chuyển đổi từ dữ liệu thô sang thông tin chiết xuất (Raw Data to Actionable Insights):** Bài báo gốc chỉ cung cấp dữ liệu đo đếm thụ động; hình đề xuất mới đã chuyển hóa thành chỉ số đánh giá hiệu năng (KPIs) rõ ràng, giúp bất kỳ ai đọc vào cũng có thể nắm bắt và phản biện ngay.
* **Tính trực quan và dễ diễn giải khi báo cáo:** Rất thuận tiện khi trình bày slide hoặc trả lời vấn đáp với giảng viên: chỉ cần nhìn vào cột tăng tốc $4.04\times$ và con số $-75.3\%$ là toàn bộ ưu thế cạnh tranh của Delta Lake đã được chứng minh trọn vẹn.


---

# PHẦN 5: ĐÁNH GIÁ VÀ PHẢN BIỆN BÀI BÁO (Critical Review)

### 1. Đánh giá những đóng góp nổi bật (Major Strengths)
* **Ý tưởng kiến trúc mang tính cách mạng (Architectural Innovation):**
  * Nhóm tác giả đã giải quyết được mâu thuẫn tồn tại nhiều năm trong ngành dữ liệu: làm sao có được tính toàn vẹn giao dịch (ACID) của hệ quản trị cơ sở dữ liệu truyền thống (RDBMS) ngay trên một hệ thống lưu trữ đối tượng dạng Key-Value giá rẻ (Cloud Object Store).
  * Khai sinh ra mô hình kiến trúc **Data Lakehouse** – xu hướng chủ đạo của toàn bộ ngành Kỹ thuật Dữ liệu (Data Engineering) hiện nay.
* **Thiết kế phi máy chủ cho siêu dữ liệu (Serverless Metadata Design):**
  * Lưu trữ toàn bộ nhật ký giao dịch (Delta Log) và siêu dữ liệu thống kê trực tiếp trên Object Store dưới dạng tệp tin mở (JSON và Parquet).
  * Loại bỏ hoàn toàn sự phụ thuộc vào các dịch vụ quản trị siêu dữ liệu trung tâm chạy liên tục 24/7 (như Hive Metastore hay MySQL catalog), giúp mở rộng không giới hạn và giảm thiểu chi phí vận hành hạ tầng.
* **Tính tương thích và tiêu chuẩn hóa cao (High Interoperability):**
  * Vì dữ liệu bảng vẫn là các tệp Parquet tiêu chuẩn, người dùng không bị "khóa cứng" (vendor lock-in) vào một công cụ duy nhất. Các công cụ tính toán phổ biến như Spark, Presto, Trino, Hive, Flink đều có thể đọc/ghi trực tiếp.
* **Độ tin cậy thực nghiệm và khả năng tái lập (Empirical Rigor):**
  * Các thử nghiệm được đo đạc kỹ lưỡng trên chuẩn công nghiệp **TPC-DS (1 TB)** và thử nghiệm khả năng mở rộng lên tới **1.000.000 phân vùng**, phản ánh chính xác các thách thức thực tế của các doanh nghiệp lớn.

---

### 2. Những hạn chế và thách thức kỹ thuật (Limitations & Challenges)
* **Giao dịch ACID chỉ giới hạn trong một bảng đơn lẻ (Single-table Atomicity):**
  * Nhật ký giao dịch Delta Log gắn liền với từng thư mục bảng riêng biệt. Hệ thống chưa hỗ trợ giao dịch nguyên tử xuyên suốt nhiều bảng (Cross-table Multi-object Transactions). Nếu một nghiệp vụ tài chính đòi hỏi cập nhật đồng thời bảng A và bảng B, nhà phát triển vẫn phải tự xử lý logic phối hợp ở tầng ứng dụng.
* **Hiện tượng xung đột khi ghi đồng thời cao (Write Contention in OCC):**
  * Do sử dụng cơ chế Kiểm soát đồng thời lạc quan (Optimistic Concurrency Control), Delta Lake hoạt động lý tưởng khi tỷ lệ đọc áp đảo tỷ lệ ghi hoặc các tác vụ ghi vào các phân vùng tách biệt. Tuy nhiên, nếu có hàng chục tác vụ đồng thời cùng cập nhật hoặc xóa (UPDATE/DELETE/MERGE) trên cùng một phân vùng dữ liệu, tỷ lệ xung đột commit sẽ tăng cao, buộc hệ thống phải tự động retry nhiều lần làm gia tăng độ trễ.
* **Độ trễ xử lý luồng thời gian thực (Streaming Latency Limit):**
  * Dù hỗ trợ Streaming I/O rất tiện lợi nhưng độ trễ xử lý luồng của Delta Lake phụ thuộc vào độ trễ thao tác I/O của Cloud Object Store (thường từ 50ms đến 200ms). Do đó, Delta Lake không thể thay thế hoàn toàn các hệ thống in-memory streaming chuyên dụng yêu cầu độ trễ mức dưới mili-giây (sub-millisecond) như Apache Flink thuần hay Apache Kafka.
* **Chi phí phình to dữ liệu lưu trữ nếu không bảo trì (Storage Bloat & Maintenance):**
  * Vì mọi giao dịch xóa/sửa đều là ghi thêm phiên bản mới (CoW - Copy-on-Write hoặc MoR - Merge-on-Read), các tệp dữ liệu cũ vẫn tồn tại để phục vụ tính năng "Du hành thời gian" (Time Travel). Nếu người quản trị không chủ động lên lịch chạy định kỳ tác vụ `VACUUM` để dọn dẹp tệp rác, chi phí lưu trữ trên S3 sẽ tăng dần theo thời gian.

---

### 3. Ý nghĩa học thuật và tiềm năng phát triển tương lai (Academic Impact & Future Directions)
* Bài báo mở ra một hướng nghiên cứu học thuật sôi động về tối ưu hóa tầng lưu trữ bảng phân tán (Table Formats), thúc đẩy sự cạnh tranh và phát triển của các công nghệ kế cận như **Apache Iceberg** (từ Netflix/Apple) và **Apache Hudi** (từ Uber).
* Hướng phát triển tiềm năng: Mở rộng giao thức điều phối giao dịch đa bảng phi tập trung (Decentralized Multi-table Coordinator), tích hợp học máy để tự động điều chỉnh ngưỡng phân vùng và tần suất dọn dẹp tệp (Autonomous Compaction & Auto-Vacuum).

---

# PHẦN 6: DANH MỤC TÀI LIỆU THAM KHẢO (References)

1. **M. Armbrust, T. Das, L. Sun, B. Yavuz, S. Zhu, M. Murthy, J. Torres, H. van Hövell, A. Ionescu, A. Łuszczak, M. Świtakowski, M. Szafrański, X. Li, T. Ueshin, M. Mokhtar, P. Boncz, A. Ghodsi, S. Paranjpye, P. Senster, R. Xin, and M. Zaharia**, *"Delta Lake: High-Performance ACID Table Storage over Cloud Object Stores,"* *Proceedings of the VLDB Endowment (PVLDB)*, vol. 13, no. 12, pp. 3411–3424, Aug. 2020. DOI: `10.14778/3415478.3415560`.
2. **M. Zaharia, R. S. Xin, P. Wendell, T. Das, M. Armbrust, A. Dave, X. Meng, J. Rosen, S. Venkataraman, M. J. Franklin, A. Ghodsi, J. Gonzalez, S. Shenker, and I. Stoica**, *"Apache Spark: A Unified Engine for Big Data Processing,"* *Communications of the ACM*, vol. 59, no. 11, pp. 56–65, 2016.
3. **M. Armbrust, R. S. Xin, C. Lian, Y. Huai, D. Liu, J. K. Bradley, X. Meng, T. Kaftan, M. J. Franklin, A. Ghodsi, and M. Zaharia**, *"Spark SQL: Relational Data Processing in Spark,"* in *Proceedings of the 2015 ACM SIGMOD International Conference on Management of Data*, 2015, pp. 1383–1394.
4. **Transaction Processing Performance Council (TPC)**, *"TPC Benchmark DS (TPC-DS) Specification,"* Standard Benchmark for Decision Support, Version 2.13.0, 2020. [Online]. Available: `http://www.tpc.org/tpcds/`.
5. **R. S. Xin, J. Rosen, M. Zaharia, M. J. Franklin, S. Shenker, and I. Stoica**, *"Shark: SQL and Rich Analytics at Scale,"* in *Proceedings of the 2013 ACM SIGMOD International Conference on Management of Data*, 2013, pp. 13–24.
