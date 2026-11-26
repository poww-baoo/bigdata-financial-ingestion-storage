---
title: "Báo cáo Cá nhân & Tích hợp — Photon (Thành viên 3)"
course: "Phương pháp nghiên cứu khoa học trong Công nghệ thông tin"
type: "Phần đóng góp thành viên 3 (Tầng 3 + Mục 3.3)"
status: "Hoàn thiện chuẩn tích hợp"
updated: 2026-11-26
---

# BÁO CÁO PHÂN TÍCH CÁ NHÂN & TÍCH HỢP NHÓM (THÀNH VIÊN 3 — CUỐI KỲ)

**Cơ sở đào tạo:** Trường Đại học Sài Gòn – Khoa Công nghệ Thông tin  
**Học phần:** Phương pháp nghiên cứu khoa học trong Công nghệ thông tin  
**Đề tài nhóm:** *Hạ tầng quản trị dữ liệu hiện đại cho Học máy quy mô lớn: Liên kết Kiến trúc Data Lakehouse, Tối ưu hóa Lưu trữ Cột, Thực thi Vector hóa và Feature Store* *(Đề tài C)*  
**Phần phụ trách:**
- **Phần cá nhân (Mục 2.3 — Tầng 3):** Phân tích và trực quan hóa bài báo *"Photon: A Fast Query Engine for Lakehouse Systems"* *(ACM SIGMOD 2022)*  
- **Phần tích hợp nhóm (Mục 2.3.5 & Mục 3.3):** Cầu nối **Delta Lake ↔ Photon**, tổng hợp định lượng 4 tầng kiến trúc và xây dựng **Biểu đồ đề xuất mới cấp nhóm**

**Sinh viên thực hiện:** Châu Quốc Bảo *(TV3)* | **Lớp:** DCT123C4| **MSSV:** 3123411024  
**Giảng viên hướng dẫn:** Vũ Ngọc Thanh Sang  
**Ngày hoàn thiện:** 2026-11-26

---

# PHẦN 1: THÔNG TIN VÀ KIỂM CHỨNG NGUỒN BÀI BÁO

### 1. Tên bài báo (Paper Title)
* **Tiếng Anh:** *Photon: A Fast Query Engine for Lakehouse Systems*
* **Dịch nghĩa tiếng Việt:** *Photon: Động cơ thực thi truy vấn tốc độ cao cho các hệ thống Lakehouse*

---

### 2. Danh sách tác giả & Cơ quan công tác (Authors & Affiliations)
Công trình được thực hiện bởi đội ngũ **24 tác giả** đến từ **Databricks Inc.** *(trong đó nhiều tác giả đồng thời gắn kết học thuật mật thiết với UC Berkeley và Stanford University)*:
* **Nhóm tác giả đầy đủ:** Alexander Behm, Shoumik Palkar, Utkarsh Agarwal, Timothy Armstrong, David Cashman, Ankur Dave, Todd Greenstein, Shant Hovsepian, Ryan Johnson, Arvind Sai Krishnan, Paul Leventis, Ala Luszczak, Prashanth Menon, Mostafa Mokhtar, Gene Pang, Sameer Paranjpye, Greg Rahn, Bart Samwel, Tom van Bussel, Herman van Hovell, Maryann Xue, Reynold Xin, và Matei Zaharia.
* **Cơ quan công tác:** Databricks Inc. *(San Francisco, Hoa Kỳ)* — Matei Zaharia đồng thời là Giáo sư Khoa học Máy tính tại Đại học Stanford / UC Berkeley, người sáng lập Apache Spark.
* **Email liên hệ nhóm tác giả:** `photon-paper-authors@databricks.com`

---

### 3. Tên hội nghị / Kỷ yếu công bố (Conference / Proceedings)
* **Tên chính thức:** *Proceedings of the 2022 International Conference on Management of Data (SIGMOD '22)*
* **Nhà xuất bản:** Association for Computing Machinery (ACM), New York, NY, USA.
* **Mã sách quốc tế (ACM ISBN):** `978-1-4503-9249-5/22/06`
* **Quy cách xuất bản:** Trang `2326 – 2339` (14 trang), tổ chức từ ngày 12–17/06/2022 tại Philadelphia, PA, USA.
* **Giải thưởng chính thức:** Đạt giải **SIGMOD 2022 Industry Best Paper Award** *(Bài báo Công nghiệp Xuất sắc nhất hội nghị)* — xác nhận tại [Trang giải thưởng SIGMOD 2022](https://2022.sigmod.org/sigmod_paper_awards.shtml).

---

### 4. Năm công bố (Year of Publication)
* **Năm công bố chính thức:** **2022** (Xuất bản chính thức ngày 10/06/2022 trên ACM Digital Library).

---

### 5. DOI & Đường dẫn chính thức của bài báo (DOI & Official Links)
* **Mã định danh số (DOI):** [`10.1145/3514221.3526054`](https://doi.org/10.1145/3514221.3526054)
* **Đường dẫn trên thư viện điện tử ACM Digital Library:** [https://dl.acm.org/doi/10.1145/3514221.3526054](https://dl.acm.org/doi/10.1145/3514221.3526054)
* **Bản toàn văn PDF từ trang tác giả (UC Berkeley):** [https://people.eecs.berkeley.edu/~matei/papers/2022/sigmod_photon.pdf](https://people.eecs.berkeley.edu/~matei/papers/2022/sigmod_photon.pdf)
* **Bản lưu trữ offline trong Vault:** `01 - Tổng quan tài liệu (Literature Review)/Bài báo đã đọc (Papers)/Photon-SIGMOD2022.pdf`

---

### 6. Minh chứng lập chỉ mục CORE, Scopus và Web of Science
* **Xếp hạng học thuật CORE:** Hội nghị **ACM SIGMOD** đạt thứ hạng **CORE A\*** — hạng xuất sắc cao nhất toàn cầu trong lĩnh vực Cơ sở dữ liệu và Hệ thống Dữ liệu lớn *(ngang hàng với VLDB và ICDE)*.
* **Vị trí trên danh mục Scopus (Elsevier):** Kỷ yếu *Proceedings of the ACM SIGMOD International Conference on Management of Data* (ACM ISBN `978-1-4503-9249-5`) thuộc nhóm **Conference Proceedings** được Elsevier Scopus lập chỉ mục thường niên. Có thể xác thực bản ghi trực tiếp bằng mã DOI `10.1145/3514221.3526054` trên cổng Scopus thông qua tài khoản thư viện trường.
* **Vị trí trên danh mục Web of Science (Clarivate):** Kỷ yếu hội nghị ACM SIGMOD thuộc phân nhóm **Conference Proceedings Citation Index – Science (CPCI-S)** trong *Web of Science Core Collection* (xác thực theo DOI `10.1145/3514221.3526054` hoặc tiêu đề bài báo trên cổng WoS).
* **Lưu ý liêm chính khoa học về phân vị Q1:** Vì bài báo công bố tại kỷ yếu hội nghị năm 2022 *(trước khi ACM SIGMOD chuyển sang mô hình tạp chí định kỳ PACMMOD từ năm 2023)*, ấn phẩm này là **kỷ yếu hội nghị (Conference Proceedings)** nên không mang chỉ số phân vị tạp chí Q1/Q2/Q3/Q4 hay Impact Factor theo nghĩa tạp chí định kỳ trên ScimagoJR. Giá trị học thuật đỉnh cao của công trình được bảo chứng bằng xếp hạng **CORE A\***, chỉ mục **Scopus / WoS CPCI-S**, và giải thưởng **SIGMOD 2022 Industry Best Paper**. *(Nếu học phần yêu cầu ảnh chụp tra cứu trực tiếp bản ghi DOI, cần xuất ảnh từ cổng Scopus/WoS bằng tài khoản trường và đính kèm phụ lục).*

---

### 7. Chỉ số ảnh hưởng & Mức độ trích dẫn (Impact Metrics & Citations)
Theo dữ liệu thư mục học mở **OpenAlex** (`https://openalex.org/W4282585030`, nguồn hội nghị `S4393915683`, truy xuất trực tiếp ngày 26/11/2026) và thư viện học thuật quốc tế:
* **Số lượt trích dẫn ghi nhận trên OpenAlex:** **92 lượt trích dẫn** *(chưa kể hàng trăm lượt trích dẫn bổ sung từ tiền ấn phẩm và tài liệu công nghiệp trên Google Scholar / Semantic Scholar)*.
* **Tác động thực tiễn công nghiệp:** Được triển khai vận hành thực tế cho hàng trăm doanh nghiệp, thực thi hàng chục triệu truy vấn và lập kỷ lục thế giới có kiểm toán của hội đồng TPC trên benchmark **TPC-DS 100 TB** (tháng 11/2021 – 02/2022).

---

### 8. Lĩnh vực chuyên môn (Subject Area & Classification)
* **Phân loại chuyên ngành Khoa học Máy tính:**
  1. *Information Systems → Data Management Systems / Query Processing & Optimization*
  2. *Computer Systems Organization → Vectorized & SIMD Execution Engines*
  3. *Software and Its Engineering → Runtime Environments & Native/JVM Interoperability*
* **Từ khóa cốt lõi:** `Lakehouse`, `Vectorized Query Execution`, `Native C++ Engine`, `Runtime Adaptivity`, `Apache Spark`, `Delta Lake`.

---

# PHẦN 2 (MỤC 2.3): PHÂN TÍCH NỘI DUNG NGHIÊN CỨU — PHOTON

### 2.3.1. Bối cảnh và vấn đề nghiên cứu (Context & Problem Statement)
* **Bối cảnh (Context):**
  * Các doanh nghiệp hiện đại lưu trữ phần lớn dữ liệu trên hệ thống lưu trữ đối tượng đám mây giá rẻ (Amazon S3, Azure ADLS, Google Cloud Storage) theo định dạng tệp cột mở như Apache Parquet hoặc bảng giao dịch Delta Lake.
  * Mô hình **hai tầng truyền thống** (Data Lake cho dữ liệu thô/ML + Data Warehouse đóng kín cho phân tích SQL hiệu năng cao) gây phức tạp vận hành, nhân bản chi phí lưu trữ và dễ sai lệch dữ liệu giữa hai hệ thống do độ trễ đường ống ETL [1, Mục 1].
  * Kiến trúc **Data Lakehouse** ra đời nhằm hợp nhất hai tầng này. Khi các tầng lưu trữ như **Delta Lake** [2] kết hợp SSD cache và data skipping đã giảm mạnh độ trễ I/O, nút thắt hiệu năng dịch chuyển sang **tầng thực thi truy vấn trong bộ nhớ (CPU-bound execution)** của động cơ JVM (Apache Spark / Databricks Runtime) [1, Mục 3.2].
* **Vấn đề nghiên cứu cốt lõi (Problem Statement):**
  1. **Thách thức 1 — Hỗ trợ dữ liệu thô, chưa chuẩn hóa (Raw, Uncurated Data):** Khác với kho dữ liệu truyền thống chỉ chạy trên bảng đã làm sạch, Lakehouse phải phục vụ đồng thời bảng sạch lẫn dữ liệu thô có nhiều tệp nhỏ, bảng rộng hàng trăm cột, nhiều giá trị `NULL` hoặc chuỗi giữ chỗ (*placeholder*), lưu số/ngày dưới dạng chuỗi, thiếu ràng buộc schema và thiếu thống kê phân bố.
  2. **Thách thức 2 — Tương thích tuyệt đối với hệ sinh thái Apache Spark hiện hữu:** Tổ chức đang vận hành đồng thời SQL, DataFrame API và hàm người dùng tự định nghĩa (UDF/ML) trên Spark. Động cơ mới phải chia sẻ tài nguyên bộ nhớ/đĩa an toàn với mã người dùng và đảm bảo **tính tương đương ngữ nghĩa** với Spark SQL, tránh làm sai lệch kết quả các ứng dụng đang chạy.

---

### 2.3.2. Khoảng trống nghiên cứu (Research Gap)
Trước khi Photon ra đời, các giải pháp thực thi truy vấn tồn tại ba khoảng trống rõ rệt:
1. **Giới hạn trần hiệu năng của động cơ dựa trên JVM (Spark SQL / DBR cũ):**
   * Thu gom rác (GC) suy giảm nghiêm trọng khi heap vượt quá **64 GB** — quá nhỏ so với máy chủ đám mây hiện đại, buộc kỹ sư phải tự quản lý bộ nhớ off-heap phức tạp.
   * Cơ chế sinh mã Java (*Whole-Stage Code Generation*) thường chạm trần giới hạn kích thước phương thức hoặc bộ nhớ đệm mã của trình biên dịch JIT trên các bảng rộng (hàng trăm cột), khiến hệ thống rơi về nhánh thông dịch kiểu Volcano chậm hơn nhiều lần (*performance cliffs*).
   * Thiếu quyền kiểm soát tường minh đối với tập lệnh SIMD và cơ chế đường ống bộ nhớ (memory pipelining) [1, Mục 3.2].
2. **Đánh đổi giữa Sinh mã (Code-Gen) và Vector hóa (Vectorization) trong môi trường Lakehouse:**
   * Các động cơ biên dịch native như HyPer hay nguyên mẫu dùng Weld đạt tốc độ tốt cho biểu thức phức tạp, nhưng rất khó gỡ lỗi (debug), khó quan sát chỉ số theo từng toán tử (observability) do các toán tử bị gộp lại, và tốn chi phí biên dịch lại khi muốn thích nghi với dữ liệu thay đổi ở runtime [1, Mục 3.3].
3. **Thiếu cầu nối triển khai từng phần (Partial Rollout) cho hệ sinh thái mở đang biến động:**
   * Các hệ thống kho dữ liệu đóng (Snowflake, Redshift) chỉ chạy trên định dạng độc quyền; các nguyên mẫu native cho Spark trước đó (như Flare) chưa giải quyết triệt để bài toán quản lý bộ nhớ thống nhất, cơ chế đổ đĩa (*spilling*) và triển khai xen kẽ với mã nguồn Spark vốn cập nhật liên tục (ví dụ tháng 7/2021 có tới 321 commit, trong đó 47% nằm ở gói SQL) [1, Mục 3.5 & Mục 7].

---

### 2.3.3. Mục tiêu nghiên cứu (Research Objectives)
1. **Xây dựng động cơ thực thi vector hóa native bằng C++ (Photon)** khai thác tối đa phần cứng hiện đại (bộ nhớ đệm, song song truy cập bộ nhớ, SIMD) để đạt hiệu năng SQL ngang tầm hoặc vượt các Data Warehouse đám mây ngay trên định dạng mở Parquet/Delta Lake.
2. **Tích hợp cơ chế thích nghi vi mô theo từng lô dữ liệu (Batch-level Runtime Adaptivity)** nhằm xử lý mượt mà dữ liệu Lakehouse thô, thiếu thống kê và nhiều ngoại lệ.
3. **Tích hợp sâu ở cấp toán tử với Databricks Runtime / Apache Spark** cho phép triển khai từng phần (*partial rollout*), chia sẻ bộ quản lý bộ nhớ thống nhất (kèm cơ chế spilling động) và đảm bảo tương thích ngữ nghĩa Spark SQL thông qua hệ thống kiểm thử tự động đa tầng.

---

### 2.3.4. Câu hỏi nghiên cứu & Giả thuyết khoa học (Research Questions & Hypotheses)
Theo phần đặt vấn đề và đánh giá thực nghiệm tại Mục 1 và Mục 6 của bài báo [1]:
* **RQ1:** Những dạng truy vấn và toán tử nào (join, aggregation, biểu thức chuỗi/thập phân, ghi Parquet) hưởng lợi nhiều nhất từ kiến trúc thực thi vector hóa native C++ so với động cơ JVM sinh mã?
* **RQ2:** Hiệu năng đầu-cuối (end-to-end) của Photon trên các chuẩn công nghiệp quy mô lớn (TPC-H SF=3000, TPC-DS 100 TB) thay đổi ra sao so với Databricks Runtime cũ, và chi phí giao tiếp JNI/chuyển đổi định dạng tại ranh giới Spark–Photon lớn đến mức nào?
* **RQ3:** Các kỹ thuật tối ưu hóa thích nghi ở runtime (như nén lô thưa trước khi join — *adaptive join compaction* — và mã hóa chuỗi UUID thích nghi khi shuffle) đóng góp bao nhiêu vào việc thu hẹp khoảng cách giữa mô hình vector hóa và mô hình sinh mã?
* **Giả thuyết nghiên cứu (Hypothesis):** *"Bằng cách chuyển tầng thực thi toán tử sang mô hình thông dịch vector hóa theo lô cột viết bằng C++ kết hợp thích nghi vi mô ở cấp batch, đồng thời cắm trực tiếp vào trình tối ưu Catalyst và bộ quản lý bộ nhớ thống nhất của Spark qua giao diện JNI không sao chép (zero-copy), hệ thống có thể vượt qua trần hiệu năng JVM, đạt tốc độ truy vấn phân tích ngang tầm kho dữ liệu chuyên dụng mà vẫn giữ trọn khả năng hỗ trợ dữ liệu thô và tính tương thích API của Spark."*

---

### 2.3.5. Đối tượng nghiên cứu (Object of Study)
* **Đối tượng nghiên cứu chính:** **Động cơ thực thi truy vấn đơn luồng trên từng phân vùng dữ liệu (In-memory Vectorized Query Execution Engine)** hoạt động như một thư viện chia sẻ C++ (`shared library`) nhúng bên trong tiến trình JVM của nút Executor thuộc Databricks Runtime (mô hình đa luồng *shared-nothing* theo phân vùng).
* **Phạm vi tích hợp:** Quá trình chuyển đổi kế hoạch vật lý từ Spark SQL Catalyst, truyền dữ liệu cột qua JNI (`OffHeapColumnVector`), quản lý bộ nhớ chung & spilling, và kiểm chứng ngữ nghĩa giữa C++ và JVM.

---

### 2.3.6. Dữ liệu và Tập chuẩn thực nghiệm (Datasets & Benchmarks)
Bài báo sử dụng 5 nhóm thử nghiệm từ vi mô đến quy mô sản xuất [1, Mục 6]:
1. **Bộ vi chuẩn (Micro-benchmarks — Mục 6.1):**
   * *Hash Join:* Hai bảng tổng hợp chứa **1 GB** dữ liệu số nguyên mỗi bảng, thực hiện inner equi-join (`SELECT count(*) FROM t1, t2 WHERE t1.id = t2.id`).
   * *Grouping Aggregation:* Hàm gom nhóm mảng `collect_list(strcol) GROUP BY intcol` với số nhóm thay đổi từ `10`, `10K` đến `10M` nhóm.
   * *Expression Evaluation:* Hàm chuyển chữ hoa `upper()` trên cột chuỗi ASCII và chuỗi tổng quát UTF-8 (thư viện ICU).
   * *Parquet Writes:* Ghi bảng **200 triệu dòng** gồm 6 cột (`int`, `long`, `date`, `timestamp`, `string`, `boolean`) xuống Amazon S3.
2. **TPC-H Benchmark (Mục 6.2):** Đầy đủ **22 truy vấn** TPC-H ở hệ số quy mô **SF=3000** (~3 TB dữ liệu thô) lưu theo định dạng **Delta Lake trên Amazon S3**.
3. **TPC-DS 100 TB chính thức (Mục 6.2):** Bộ chuẩn công nghiệp quy mô **100 TB** do Hội đồng TPC kiểm toán độc lập (gồm cả 3 pha: *Power run*, *Concurrency run*, và *Database update run*), lưu theo định dạng Delta Lake trên Amazon S3.
4. **Kiểm thử chi phí JNI & Transition (Mục 6.3):** Đọc 1 cột số nguyên từ bảng trong bộ nhớ kèm no-op UDF nhằm đo tình huống xấu nhất (*worst-case overhead*).
5. **Thử nghiệm Thích nghi Runtime (Mục 6.4):**
   * *TPC-DS Query 24:* Đánh giá tác động của *adaptive join compaction* trên lô dữ liệu thưa.
   * *Adaptive UUID Encoding:* Phân vùng lại (*repartition*) tập dữ liệu **50 triệu dòng** chứa cột chuỗi UUID 36 ký tự, nén shuffle bằng LZ4.

---

### 2.3.7. Các biến số, đặc trưng và cấu hình môi trường thực nghiệm (Variables & Experimental Setup)
* **Cấu hình phần cứng trên Amazon Web Services (AWS EC2 `i3.2xlarge` — 8 vCPU Intel Xeon E5-2686 v4, 64 GB RAM, SSD NVMe):**
  * *Micro-benchmarks (trừ Parquet write):* **1 nút** `i3.2xlarge`, đơn luồng, `11 GB` heap cho JVM và `35 GB` bộ nhớ off-heap cho Photon, đọc bảng trong bộ nhớ để cô lập chi phí I/O.
  * *Parquet Write:* **1 nút** `i3.2xlarge`, `8` luồng, `16` phân vùng, ghi trực tiếp xuống S3.
  * *TPC-H SF=3000:* **1 Driver + 8 Worker nodes** `i3.2xlarge`; chạy 1 lượt warm-up rồi lấy thời gian nhỏ nhất trong **3 lần chạy**.
  * *TPC-DS Q24 (Join Compaction):* Cụm **16 nút**.
  * *TPC-DS 100 TB chính thức:* Cụm **256 nút** `i3.2xlarge` trên AWS, dữ liệu trên Amazon S3.
* **Biến số thực nghiệm & đối chứng:**
  * *Đối thủ chính:* Databricks Runtime (DBR — Spark SQL với Whole-Stage Code Generation, Sort-Merge Join mặc định và Shuffled-Hash Join).
  * *Các biến cờ kỹ thuật:* Bật/tắt `ASCII SIMD optimization`, bật/tắt `Adaptive Join Compaction`, bật/tắt `Adaptive UUID 128-bit encoding`, số lượng nhóm aggregation (`10`, `10K`, `10M`).

---

### 2.3.8. Phương pháp, kiến trúc và kỹ thuật cốt lõi (Methodology & Architecture)

#### A. Quyết định kiến trúc nền tảng (Mục 3)
* **Native C++ thay cho JVM:** Loại bỏ trần GC > 64 GB, tránh lỗi JIT bailout trên bảng rộng, kiểm soát trực tiếp bộ nhớ và tập lệnh SIMD.
* **Thông dịch Vector hóa (Interpreted Vectorization) thay cho Sinh mã (Code-Gen):** Nhóm tác giả đã thử nghiệm nguyên mẫu cả hai nhánh (dùng *Weld* cho code-gen) và chọn vector hóa vì: (1) rút ngắn thời gian phát triển & gỡ lỗi (ví dụ xây dựng aggregation mất vài tuần thay vì 2 tháng với code-gen); (2) giữ nguyên ranh giới toán tử để thu thập số liệu quan sát trực tiếp (*live metrics*) trên Spark UI; (3) hỗ trợ thích nghi theo lô ở runtime mà không tốn chi phí tái biên dịch; và (4) vẫn có thể bù đắp khoảng cách hiệu năng bằng các toán tử gộp chuyên biệt (*fused operators*, ví dụ biểu thức `BETWEEN`).
* **Biểu diễn theo cột mặc định, xoay sang hàng có chọn lọc:** Lưu dữ liệu cột trong bộ nhớ giúp bỏ qua bước xoay cột-sang-hàng khi đọc Parquet và thân thiện với SIMD; riêng bên trong bảng băm (*hash table*), Photon lưu các bản ghi theo dạng hàng (*row*) để một con trỏ duy nhất trỏ tới khóa tổ hợp, tránh truy cập ngẫu nhiên tốn kém khi so sánh khóa.

#### B. Cấu trúc dữ liệu `Column Batch` & Nhân thực thi Vector hóa (Mục 4.1–4.5)
* **Column Vector & Column Batch (Figure 2, tr. 2331):** Mỗi cột lưu mảng giá trị liên tiếp trong bộ nhớ + mảng byte đánh dấu `NULL` + siêu dữ liệu cấp batch (ví dụ cờ mã hóa ASCII). Một `Column Batch` tập hợp các vector cột kèm **Position List** chứa chỉ số các hàng đang hoạt động (*active rows*). Chọn *Position List* thay vì *byte vector* giúp vòng lặp chỉ duyệt $O(\text{active rows})$ thay vì $O(\text{batch size})$ trên lô thưa.
* **Execution Kernels & C++ Templates (Listing 2, tr. 2332):** Mọi phép tính biểu thức, lọc, dò bảng băm và tuần tự hóa đều viết dưới dạng vòng lặp chặt trên vector với từ khóa `RESTRICT` hỗ trợ trình biên dịch tự động vector hóa (hoặc dùng SIMD intrinsics thủ công). Các tham số template compile-time như `<bool kHasNulls, bool kAllRowsActive>` giúp trình biên dịch loại bỏ hoàn toàn câu lệnh rẽ nhánh (`if`) ở runtime.
* **Vectorized Hash Table 3 bước (Mục 4.4):** (1) Băm theo lô bằng kernel băm (hưởng lợi từ SIMD); (2) Dò nạp con trỏ theo lô (các phép đọc bộ nhớ ngẫu nhiên nằm sát nhau nên CPU song song hóa được truy cập bộ nhớ — *memory-level parallelism* — quan trọng hơn cả SIMD cho workload giới hạn bởi bộ nhớ); (3) So sánh khóa theo cột với dò bậc hai (*quadratic probing*) và xuất position list cho các dòng chưa khớp.
* **Quản lý bộ nhớ cấp vector (Mục 4.5):** Dùng buffer pool nội bộ theo cơ chế *most-recently-used (MRU)* để tái sử dụng vùng nhớ nóng của các batch tạm; dữ liệu độ dài biến thiên (chuỗi) dùng append-only pool giải phóng sau mỗi batch.

#### C. Thích nghi vi mô ở thời điểm chạy (Batch-level Runtime Adaptivity — Mục 4.6)
Photon tự động phát hiện đặc trưng từng batch ở runtime để chọn đường thực thi tối ưu:
1. **Chuyên biệt hóa `NULL` & hàng không hoạt động:** Nếu batch không có `NULL` và mọi hàng đều active, bỏ kiểm tra null và bỏ tra gián tiếp qua `pos_list` để mở đường cho SIMD.
2. **Chuỗi ASCII vs. UTF-8:** Tính cờ *all-ASCII* để chạy phép trừ byte bằng SIMD thay vì gọi thư viện Unicode ICU nặng nề.
3. **Adaptive Join Compaction:** Theo dõi độ thưa của batch sau lọc/join; khi quá thưa, chủ động nén (*compact*) các hàng hợp lệ thành lô đặc trước khi dò bảng băm nhằm tối đa hóa song song truy cập bộ nhớ. *(Lưu ý: đây là nén chỉ số trong RAM, hoàn toàn khác với compaction gộp tệp nhỏ trên Delta Lake).*
4. **Adaptive Shuffle Encoding:** Nhận diện chuỗi UUID 36 byte để nén thành số nguyên 128-bit trước khi nén LZ4 và truyền shuffle.

#### D. Tích hợp với Databricks Runtime & Đảm bảo ngữ nghĩa (Mục 5)
Quá trình chuyển đổi kế hoạch vật lý từ Spark SQL sang Photon thông qua quy tắc Catalyst (duyệt từ dưới lên bắt đầu từ `FileScan`, minh họa theo **Figure 3, trang 2332**):

```text
  [Kế hoạch Spark SQL gốc (JVM)]          [Kế hoạch lai Spark–Photon sau quy tắc Catalyst]
  ┌────────────────────────────┐          ┌───────────────────────┐   ┌─────────────────────────┐
  │  ToObject (JVM)            │          │  ToObject (JVM)       │◄──┤  Transition (Col→Row)   │
  │      ▲                     │          │      (Spark fallback) │   │      ▲                  │
  │  Shuffle (JVM)             │   ═══►   │                       │   │  PhotonShuffle (C++)    │
  │      ▲                     │ Catalyst │                       │   │      ▲                  │
  │  Filter (JVM)              │   Rule   │                       │   │  PhotonFilter (C++)     │
  │      ▲                     │          │                       │   │      ▲                  │
  │  FileScan (JVM Off-heap)   │          │  FileScan (JVM)       ├──►│  Adapter (Zero-copy JNI)│
  └────────────────────────────┘          └───────────────────────┘   └─────────────────────────┘
                                               JVM Execution               Photon C++ Execution
```

* **Zero-copy Adapter & Single-pivot Transition:** Nút `Adapter` truyền con trỏ trực tiếp tới `OffHeapColumnVector` của Spark qua JNI (~`23 ns`/lần gọi mỗi batch, không sao chép dữ liệu). Khi gặp toán tử chưa hỗ trợ (như `ToObject` hoặc UDF), nút `Transition` xoay cột sang hàng trả lại cho JVM; chỉ bắt đầu chuyển từ `FileScan` để tránh nhiều lần xoay qua lại gây suy giảm hiệu năng.
* **Quản lý bộ nhớ thống nhất & Recursive Spill (Mục 5.3–5.4):** Tách biệt *đặt chỗ bộ nhớ (reservation)* với *cấp phát cục bộ (allocation)*. Photon đăng ký làm một `MemoryConsumer` trong Spark Unified Memory Manager: Spark có thể yêu cầu Photon đổ đĩa (*spill*) và ngược lại (hỗ trợ cả *recursive spill* giữa hai toán tử Photon). Ngoài ra, gắn listener dọn trạng thái on-heap (ví dụ dữ liệu broadcast) ngay khi kết thúc truy vấn vì bộ nhớ off-heap lớn khiến JVM GC ít kích hoạt.
* **Kiểm thử nhất quán ngữ nghĩa 3 tầng (Mục 5.6):** Kết hợp *Unit tests* (chạy cả bộ test biểu thức mã nguồn mở của Spark trên mọi nhánh chuyên biệt hóa), *End-to-end tests* (so khớp đầu ra truy vấn giữa Spark và Photon), và *Fuzz tests* (sinh ngẫu nhiên dữ liệu/truy vấn, đặc biệt cho phép toán `Decimal` và múi giờ IANA).

---

### 2.3.9. Các chỉ số đánh giá kết quả (Evaluation Metrics)
1. **Thời gian thực thi truy vấn (Query Runtime):** Đo bằng giây (`s`) hoặc mili-giây (`ms`); riêng TPC-H lấy giá trị nhỏ nhất trong 3 lần chạy sau warm-up.
2. **Hệ số tăng tốc (Speedup Factor):**
   $$\text{Speedup} = \frac{T_{\text{DBR (Baseline)}}}{T_{\text{Photon}}}$$
3. **Tỷ lệ chi phí giao tiếp biên (JNI & Transition Overhead %):** Phần trăm thời gian CPU tiêu tốn cho phương thức JNI nội bộ và nút Adapter/Transition trong tình huống xấu nhất.
4. **Dung lượng dữ liệu trao đổi (Shuffle Data Volume):** Đo bằng `MB` sau nén LZ4 (đánh giá khả năng giảm áp lực bộ nhớ và tránh spill).
5. **Hiệu năng chuẩn kiểm toán TPC-DS 100 TB:** Bao gồm thông lượng tổng hợp qua cả 3 pha *Power*, *Concurrency* và *Database Update*.

---

### 2.3.10. Những kết quả chính của nghiên cứu (Key Findings)
* **Vi chuẩn toán tử lõi (Mục 6.1, Figures 4–7):**
  * *Hash Join (Figure 4):* Photon chạy trong **`5,3 giây`** so với DBR Sort-Merge Join (`18,9 giây`) và DBR Shuffled-Hash Join (`19,4 giây`) → tăng tốc **`3,5×`** nhờ song song hóa nạp bộ nhớ khi dò bảng băm.
  * *Aggregation `collect_list` (Figure 5):* Tăng tốc từ **`3,5×`** (`10M` nhóm: `76 s → 22 s`), **`4,8×`** (`10` nhóm: `48 s → 10 s`) lên tới **`5,7×`** (`10K` nhóm: `63 s → 11 s`) nhờ bảng băm vector hóa và gộp cấp phát danh sách qua memory pool.
  * *Biểu thức chuỗi `upper()` (Figure 6):* Photon + SIMD ASCII (`1.384 ms`) nhanh hơn **`3,14×`** (~3×) so với DBR + ASCII (`4.343 ms`) và **`3,92×`** (~4×) so với nhánh UTF-8 ICU (`5.427 ms`).
  * *Ghi Parquet lên S3 (Figure 7):* Ghi 200M dòng nhanh hơn **`2×`** đầu-cuối, chủ yếu nhờ bộ mã hóa cột (dictionary hash table, bit-packing, tính thống kê) viết bằng native C++.
* **TPC-H SF=3000 trên cụm 8+1 nút AWS (Mục 6.2, Figure 8):**
  * Photon đạt tốc độ trung bình **`4×` theo từng truy vấn** và tối đa **`23×`** (ở truy vấn **Q1** vốn nặng phép tính `Decimal`, một số biểu thức thập phân nhanh hơn trên `80×` do dùng số nguyên native thay cho Java `BigDecimal`).
  * Trên **Q9** (nặng hash join lớn), Photon giảm mạnh chu kỳ CPU cho join đến mức pha ghi tệp shuffle chiếm tới 50% tổng thời gian.
* **TPC-DS 100 TB chính thức (Mục 6.2):** Trên cụm 256 máy `i3.2xlarge` đọc Delta Lake từ Amazon S3, DBR bật Photon thiết lập **kỷ lục thế giới có kiểm toán** tại thời điểm công bố (tháng 11/2021 – 02/2022). Ở quy mô khách hàng thực tế, tốc độ trung bình quan sát là **`3×`** và một số workload đạt trên **`10×`** [1, Mục 1].
* **Chi phí JNI & chuyển đổi định dạng gần như không đáng kể (Mục 6.3):** Mỗi lời gọi JNI theo batch chỉ tốn khoảng **`23 ns`** (tương đương một lời gọi hàm ảo C++); ngay cả ở truy vấn tình huống xấu nhất, JNI chỉ chiếm **`0,06%`** và nút Adapter chiếm **`0,2%`** tổng thời gian thực thi.
* **Hiệu quả thích nghi runtime (Mục 6.4, Figure 9 & Table 1):**
  * *Adaptive Join Compaction (TPC-DS Q24):* Rút thời gian chạy từ **`120 giây`** (không nén — chậm hơn DBR `118 giây`) xuống **`76 giây`**, đạt mức tăng tốc **`1,55×`** so với DBR và **`1,58×`** so với không nén.
  * *Adaptive UUID Encoding (Table 1):* Giảm thời gian chạy từ `31.501 ms` (DBR) và `17.324 ms` (Photon không thích nghi) xuống **`15.069 ms`** (`−15%` so với không thích nghi, `2,09×` so với DBR), đồng thời cắt giảm **hơn `2×` dung lượng shuffle** (`1.715,1 MB → 763,2 MB`).

---

# PHẦN 3: TỰ VẼ LẠI 02 HÌNH MINH HỌA TỪ BÀI BÁO GỐC

---

## 3.1. HÌNH 1: KIẾN TRÚC TẦNG THỰC THI DATABRICKS RUNTIME VÀ PHOTON (FIGURE 1 BÀI BÁO)

### Hình ảnh tái tạo:
![Hình tái tạo Figure 1: Kiến trúc tầng thực thi Databricks Runtime và Photon trên Lakehouse](../../99%20-%20Đính%20kèm%20(Attachments)/TV3_Hinh1_KienTruc_Photon.png)

*(Tệp hình ảnh chất lượng cao lưu tại: `99 - Đính kèm (Attachments)/TV3_Hinh1_KienTruc_Photon.png` (300 DPI) và bản vector `TV3_Hinh1_KienTruc_Photon.pdf`; mã nguồn dựng hình tại `03 - Phương pháp & Thí nghiệm (Methodology & Experiments)/scripts/ve_hinh_photon_tv3.py`)*

---

### Thuyết minh chi tiết 7 nội dung theo yêu cầu:

#### 1. Vị trí hình gốc trong bài báo
* **Hình gốc:** **Figure 1**, xuất hiện tại **Trang 3 (tr. 2328)** của bài báo (thuộc Mục 2.1: *Databricks' Lakehouse Architecture* và Mục 2.2: *The Databricks Runtime*).
* **Tiêu đề gốc:** *"Figure 1: Databricks' execution layer. Photon runs as part of the Databricks Runtime, which executes queries on a distributed cluster of public cloud VMs. Within these clusters, Photon executes tasks on partitions of data on a single thread."*

#### 2. Mục đích của hình
* Định vị rõ ràng vị trí của **Photon** trong kiến trúc Lakehouse phân tán của Databricks: chỉ ra cách một truy vấn SQL hoặc DataFrame từ người dùng đi qua tầng điều phối Driver, được phân rã thành các tác vụ đơn luồng trên từng lõi CPU của Executor, và được Photon xử lý trực tiếp trên dữ liệu bảng mở Delta Lake / Parquet lưu ở Cloud Object Storage.

#### 3. Các biến số và thông tin được thể hiện
* **Đầu vào truy vấn (User Queries):** Giao diện thống nhất gồm Apache Spark DataFrame API (`df.select($"col1").filter($"col2" > 0).join(df2)`) và SQL chuẩn (`SELECT * FROM t1, t2 WHERE col2 > 0 AND t1.id = t2.id`).
* **Tầng hạ tầng tính toán (Databricks Runtime Clusters):** Tập hợp các cụm máy ảo đám mây (AWS/Azure/GCP), mỗi cụm gồm:
  * **Driver (Điều phối trung tâm):** Chứa trình phân tích & tối ưu truy vấn (*Catalyst Query Optimizer*) và bộ lập lịch tác vụ (*Task Scheduler*).
  * **Executor (Tiến trình đa luồng JVM):** Quản lý nhóm lõi xử lý (`CPU0`–`CPU3`) thực thi song song các phân vùng độc lập theo mô hình *shared-nothing*.
* **Đơn vị thực thi lõi (Photon Task):** Khối phóng to từ `CPU1`, minh họa đường ống toán tử C++ đơn luồng xử lý theo lô cột (`FileScan → Filter → Join`).
* **Tầng lưu trữ đám mây (User Cloud Storage):** Hệ thống bảng **Delta Lake** gồm siêu dữ liệu (`_delta_log`) và các tệp dữ liệu cột mở **Apache Parquet**.

#### 4. Cách thức sinh viên tái tạo hình
* **Công cụ thực hiện:** Lập trình Python 3 sử dụng thư viện **`matplotlib`** (`matplotlib.patches.FancyBboxPatch`, `Circle`, `annotate`).
* **Quy trình tái tạo:**
  1. Phân tích bố cục 4 tầng thông tin và các mối quan hệ phóng to (Cluster → DBR; `CPU1` → Photon Task) từ Figure 1 trang 2328 của bài báo gốc.
  2. Xây dựng hàm vẽ khối bo góc (`draw_rounded_box`) và mũi tên định hướng (`draw_arrow`) trong hàm `build_figure_1()` thuộc script `ve_hinh_photon_tv3.py`.
  3. Phối bảng màu phân tầng theo chức năng (xanh dương cho đầu vào & lưu trữ Delta Lake, xám trung tính cho Driver/Executor JVM, cam nổi bật cho động cơ Photon C++) và bổ sung hộp chú giải (*Legend*) phía dưới.
  4. Xuất đồng thời bản ảnh raster `PNG 300 DPI` và bản vector `PDF`.

#### 5. Ý nghĩa của kết quả được thể hiện
* Sơ đồ làm rõ một điểm kiến trúc then chốt thường bị hiểu nhầm: **Photon không thay thế toàn bộ Apache Spark**, mà đóng vai trò **động cơ thực thi ở mức thấp nhất (single-threaded per-partition task engine)** bên trong khung điều phối phân tán của Databricks Runtime.
* Nhờ kế thừa nguyên vẹn Catalyst Optimizer, Task Scheduler và tầng quản lý bảng Delta Lake, các tác vụ SQL, ETL và ML có thể hưởng tốc độ native C++ một cách trong suốt mà không cần di chuyển dữ liệu sang kho dữ liệu đóng kín.

#### 6. Kết luận khoa học rút ra từ hình
* Kiến trúc tách lớp giữa **mặt phẳng điều khiển/lập lịch phân tán** (Driver & Executor đa luồng), **động cơ tính toán đơn luồng chuyên tối ưu CPU** (Photon Task C++), và **tầng bảng giao dịch mở** (Delta Lake + Parquet) cho phép mở rộng quy mô linh hoạt trên Cloud VM đồng thời tận dụng hiệu quả phần cứng cục bộ trên từng lõi CPU.

#### 7. So sánh điểm giống và khác giữa hình vẽ lại và hình trong bài báo gốc
* **Điểm giống:** Bảo toàn 100% các thành phần kiến trúc, hai câu truy vấn ví dụ nguyên bản, cấu trúc phóng to từ cụm VM vào DBR (`Driver` / `Executor` với `CPU0`–`CPU3`), chuỗi toán tử `FileScan → Filter → Join` trong `Photon Task`, và kết nối trực tiếp tới `Delta Lake (Metadata + Parquet data files)`.
* **Điểm khác biệt & cải tiến của sinh viên:**
  * **Việt hóa song ngữ chú giải:** Kèm thuật ngữ tiếng Việt chuẩn xác bên cạnh tên gốc tiếng Anh để đồng bộ ngôn ngữ toàn báo cáo.
  * **Làm rõ vai trò kỹ thuật tại từng toán tử:** Bổ sung ghi chú ngắn ngay trong các khối Photon (`Adapter Zero-copy JNI`, `Position List / Adaptive`, `Vectorized Hash Table`) và hộp chú giải phân tầng (*Legend*) ở đáy hình mà hình gốc chưa có.

---

## 3.2. HÌNH 2: TÁC ĐỘNG CỦA ADAPTIVE JOIN COMPACTION TRÊN TPC-DS Q24 (FIGURE 9 BÀI BÁO)

### Hình ảnh tái tạo:
![Hình tái tạo Figure 9: Tác động của Adaptive Join Compaction trong Photon (TPC-DS Q24)](../../99%20-%20Đính%20kèm%20(Attachments)/TV3_Hinh2_TPCDS_Q24.png)

*(Tệp hình ảnh chất lượng cao lưu tại: `99 - Đính kèm (Attachments)/TV3_Hinh2_TPCDS_Q24.png` (300 DPI) và bản vector `TV3_Hinh2_TPCDS_Q24.pdf`; mã nguồn dựng hình tại `03 - Phương pháp & Thí nghiệm (Methodology & Experiments)/scripts/ve_hinh_photon_tv3.py`)*

---

### Thuyết minh chi tiết 7 nội dung theo yêu cầu:

#### 1. Vị trí hình gốc trong bài báo
* **Hình gốc:** **Figure 9**, xuất hiện tại **Trang 12 (tr. 2337)** của bài báo (thuộc Mục 6.4: *Benefits of Runtime Adaptivity — Adapting to Sparse Batches*).
* **Tiêu đề gốc:** *"Figure 9: Impact of adaptive join compaction in Photon on TPC-DS Q24. Compaction allows vectorization to outperform code-gen and produces a 1.55× speedup over DBR."*

#### 2. Mục đích của hình
* Minh họa định lượng vai trò sống còn của kỹ thuật **thích nghi ở thời điểm chạy (Adaptive Join Compaction)** trong mô hình thực thi vector hóa: chứng minh rằng chỉ chuyển sang mã C++ là chưa đủ nếu gặp lô dữ liệu thưa (*sparse batches*), và việc chủ động nén lô thưa giúp mô hình vector hóa vượt qua mô hình sinh mã (Code-Gen) của DBR.

#### 3. Các biến số và thông tin được thể hiện
* **Biến độc lập (Trục hoành X):** 3 cấu hình thực thi truy vấn **TPC-DS Query 24** trên cụm **16 nút**:
  1. `DBR (Spark SQL Code-Gen)` — Mốc đối chứng.
  2. `Photon + No Compaction` — Chạy vector hóa C++ nhưng tắt cơ chế nén lô thưa trước khi dò bảng băm.
  3. `Photon + Join Compaction` — Chạy vector hóa C++ có theo dõi độ thưa và nén lô thích nghi.
* **Biến phụ thuộc (Trục tung Y):** Thời gian thực thi truy vấn (*Runtime*), đơn vị **giây** (giá trị càng thấp càng tốt).
* **Số liệu định lượng trích xuất trực tiếp từ nhãn cột của Figure 9 gốc:**
  * DBR: **`118 giây`**
  * Photon (không compaction): **`120 giây`** *(chậm hơn DBR `1,7%`)*
  * Photon (có adaptive join compaction): **`76 giây`** *(nhanh hơn **`1,55×`** so với DBR và **`1,58×`** so với Photon không compaction)*

#### 4. Cách thức sinh viên tái tạo hình
* **Công cụ thực hiện:** Python 3 và thư viện **`matplotlib`** (hàm `build_figure_2()` trong `ve_hinh_photon_tv3.py`).
* **Quy trình tái tạo:**
  1. Đọc chính xác 3 con số nhãn in sẵn trên đỉnh cột của Figure 9 trang 2337 (`118`, `120`, `76` giây) và hệ số `1.55×` trong chú thích hình gốc.
  2. Dựng biểu đồ cột đứng kèm hoa văn chấm (`...`) cho cột giữa để dễ phân biệt khi in đen trắng, bổ sung đường nét đứt ngang tại mốc `118 giây` của DBR.
  3. Tính và gắn hộp chú thích định lượng (*Callout Annotations*) cho cả hiện tượng thoái lui nhẹ (`+1,7%`) lẫn mức tăng tốc (`1,55× / −35,6%` và `1,58× / −36,7%`).
  4. Xuất ảnh `PNG 300 DPI` và `PDF`.

#### 5. Ý nghĩa của kết quả được thể hiện
* Kết quả phơi bày điểm yếu kinh điển của mô hình thực thi vector hóa: sau khi qua các điều kiện lọc hoặc phép join có tính chọn lọc cao, một `Column Batch` trở nên rất thưa; nếu truyền nguyên lô thưa qua các toán tử phía sau, chi phí gọi hàm diễn giải và độ trễ nạp bộ nhớ không bão hòa được băng thông sẽ khiến **Photon (`120 s`) thậm chí chậm hơn cả Spark SQL Code-Gen trên JVM (`118 s`)** vì Code-Gen xử lý từng dòng gộp nội tuyến (*inlined*) không chịu chi phí gọi theo batch.
* Khi kích hoạt **Adaptive Join Compaction**, Photon dồn các chỉ số hàng còn hợp lệ thành batch đặc trước khi dò bảng băm, khai thác tối đa song song truy cập bộ nhớ và giảm thời gian chạy xuống **`76 giây`**.

#### 6. Kết luận khoa học rút ra từ hình
* Lợi thế hiệu năng của Photon không chỉ đến từ việc viết lại bằng C++ hay dùng SIMD, mà phụ thuộc quyết định vào **kỹ thuật tối ưu hóa thích nghi ở runtime (micro-adaptivity)** nhằm khắc phục nhược điểm cố hữu của mô hình vector hóa trên dữ liệu thưa.
* Lưu ý phạm vi kết luận: đây là kết quả chuyên sâu trên một truy vấn tiêu biểu (TPC-DS Q24), minh họa cơ chế kỹ thuật chứ không thay thế cho kết quả trung bình toàn bộ chuẩn benchmark.

#### 7. So sánh điểm giống và khác giữa hình vẽ lại và hình trong bài báo gốc
* **Điểm giống:** Giữ nguyên tuyệt đối 3 giá trị thực nghiệm (`118 s`, `120 s`, `76 s`), thứ tự 3 cấu hình so sánh và kết luận định lượng `1,55×` của Figure 9 gốc.
* **Điểm khác biệt & cải tiến của sinh viên:**
  * **Đường chuẩn tham chiếu DBR (`118 s`):** Giúp mắt người đọc nhìn thấy ngay lập tức sự thoái lui của cột `120 s` vượt trên vạch chuẩn và mức cắt giảm sâu của cột `76 s`.
  * **Hai hộp chú thích phân tích định lượng:** Bổ sung phần trăm thay đổi (`+1,7%`, `−35,6%`, `−36,7%`) và so sánh trực tiếp cặp `Photon có/không compaction (1,58×)` giúp diễn giải bài học kiến trúc rõ ràng hơn hình gốc.

---

# PHẦN 4 (MỤC 2.3.4 & 2.3.5): PHẢN BIỆN BÀI BÁO VÀ CẦU NỐI DELTA LAKE ↔ PHOTON

### 2.3.4. Đánh giá và phản biện bài báo (Critical Review)

#### 1. Những đóng góp nổi bật (Major Strengths)
* **Tính thực chiến và giá trị kỹ thuật hệ thống cao:** Bài báo không dừng ở nguyên mẫu học thuật mà trình bày một động cơ đã vận hành thực tế trên hàng chục triệu truy vấn khách hàng, chia sẻ thẳng thắn các bài học xương máu về đánh đổi kỹ thuật (JVM vs. C++, Vectorization vs. Code-Gen, Position List vs. Byte Vector, On-heap GC vs. Off-heap).
* **Thiết kế triển khai từng phần (Partial Rollout) và quản lý bộ nhớ thống nhất xuất sắc:** Khả năng chạy xen kẽ toán tử Photon và Spark trong cùng một kế hoạch truy vấn với chi phí JNI cực thấp (~`23 ns`/batch) cùng cơ chế *recursive spill* là giải pháp thực tế giúp chuyển đổi mượt mà một hệ sinh thái lớn như Apache Spark mà không phá vỡ tương thích ngược.
* **Thực nghiệm đa tầng thuyết phục:** Kết hợp chặt chẽ giữa vi chuẩn cô lập từng nút thắt (Figures 4–7), kiểm chứng quy mô lớn TPC-H SF=3000 & TPC-DS 100 TB có kiểm toán độc lập, và thực nghiệm đối chứng làm rõ vai trò của tính thích nghi (Figure 9, Table 1).

#### 2. Những hạn chế và thách thức kỹ thuật (Limitations & Challenges)
* **Khả năng tái lập độc lập và tính đóng của mã nguồn:** Toàn bộ nhóm tác giả thuộc doanh nghiệp phát triển sản phẩm (Databricks) và bản thân **Photon là động cơ độc quyền (proprietary)** bên trong Databricks Runtime (không mở mã nguồn như Delta Lake hay BtrBlocks). Do đó, cộng đồng nghiên cứu khó tái lập độc lập hoặc kiểm chứng chi tiết thuật toán bên trong trên các hạ tầng ngoài Databricks.
* **Không phải mọi phép tăng tốc đều do SIMD và vẫn có nhánh yếu hơn Code-Gen:** Như chính tác giả thừa nhận, các biểu thức điều kiện lồng ghép phức tạp vẫn là thế mạnh của Code-Gen (hướng lai ghép *hybrid* để lại cho tương lai); với hash join bị giới hạn bộ nhớ, song song hóa truy cập bộ nhớ quan trọng hơn SIMD.
* **Giới hạn hỗ trợ toán tử và chi phí ranh giới Spark–Photon:** Photon không hỗ trợ *Sort-Merge Join*, và khi truy vấn chứa nhiều UDF phức tạp hoặc toán tử chưa được hỗ trợ xen kẽ ở giữa kế hoạch, quy tắc bảo thủ của Catalyst sẽ không chuyển phần kế hoạch đó sang Photon để tránh phát sinh nhiều nút xoay cột-sang-hàng (`Transition`).
* **Tính nhạy cảm với phân bổ bộ nhớ On-heap / Off-heap và chưa đánh giá xuyên tầng đầy đủ:** Việc tách tĩnh bộ nhớ off-heap làm giảm tần suất GC của JVM, tiềm ẩn lỗi `OutOfMemory` cho các cấu trúc tạm on-heap (như broadcast) nếu thiếu cơ chế dọn dẹp chặt chẽ. Ngoài ra, bài báo chưa đánh giá tổ hợp kết hợp với các định dạng cột thế hệ mới ngoài Parquet (như BtrBlocks) hay đường ống đặc trưng ML (Feature Store).

---

### 2.3.5. Cầu nối kiến trúc: Delta Lake (Tầng 2) ↔ Photon (Tầng 3)

Trong kiến trúc 4 tầng của đề tài, **Delta Lake** [2] và **Photon** [1] là cặp cộng hưởng trực tiếp giải quyết hai nút thắt kế tiếp nhau trong vòng đời một câu truy vấn Lakehouse:

| Khía cạnh | Tầng 2 — Delta Lake (PVLDB 2020) | Tầng 3 — Photon (SIGMOD 2022) | Cơ chế bổ trợ giữa hai tầng |
| :--- | :--- | :--- | :--- |
| **Nút thắt giải quyết** | Tính nhất quán ACID, độ trễ `LIST` metadata và lượng I/O quét thừa trên Cloud Object Store. | Nút thắt **CPU & JVM overhead** khi giải mã, lọc, join, tổng hợp dữ liệu trong bộ nhớ. | Delta Lake **giảm lượng dữ liệu phải đọc**; Photon **tăng tốc xử lý CPU** trên phần dữ liệu sống sót. |
| **Cơ chế kỹ thuật chính** | Transaction Log (`_delta_log`), Checkpoint Parquet, Min/Max Data Skipping, Z-Order / Hilbert Clustering. | Native C++ Columnar Batch, Execution Kernels (SIMD), Vectorized Hash Table, Batch-level Adaptivity, Zero-copy Adapter. | Khi Delta Lake bật Data Skipping & SSD Cache, I/O không còn là nút thắt → mở khóa tối đa tiềm năng tăng tốc CPU của Photon. |
| **Giao tiếp vận hành** | Cung cấp snapshot nhất quán và danh sách tệp Parquet cần đọc cho trình lập kế hoạch. | Thực thi quét tệp qua `OffHeapColumnVector` (zero-copy JNI), hỗ trợ Dynamic File Pruning và tối ưu ghi tệp Parquet mới (`2×`). | Photon vừa tăng tốc truy vấn đọc trên bảng Delta, vừa tăng tốc tác vụ ghi/ETL (`INSERT`/`MERGE`/`OPTIMIZE`) tạo tệp Parquet cho Delta Lake. |

* **Lưu ý phản biện về tính cộng hưởng:** Hai cơ chế bổ trợ rõ rệt nhưng **không đảm bảo luôn cộng dồn tuyến tính** trong mọi tình huống. Nếu câu truy vấn bị giới hạn bởi băng thông mạng S3 (tính chọn lọc kém, không bỏ qua được tệp), hoặc chứa nhiều UDF/toán tử không hỗ trợ phải fallback về JVM, lợi ích từ Photon sẽ bị thu hẹp. Đồng thời, **Photon không cung cấp giao dịch ACID, Time Travel hay kiểm soát đồng thời thay cho Delta Lake** — hai tầng đảm nhiệm trách nhiệm tách bạch và bổ sung cho nhau [1], [2].

---

# PHẦN 5 (MỤC 3.3 — PHẦN TÍCH HỢP CHUNG CỦA NHÓM): TỔNG HỢP ĐỊNH LƯỢNG 4 TẦNG VÀ HÌNH ĐỀ XUẤT MỚI

### Hình đề xuất mới cấp nhóm:
![Hình đề xuất mới: Tổng hợp định lượng hiệu quả cải thiện qua 4 tầng kiến trúc Lakehouse cho ML](../../99%20-%20Đính%20kèm%20(Attachments)/TV3_Hinh3_TongHop_HieuNang.png)

*(Tệp hình ảnh chất lượng cao lưu tại: `99 - Đính kèm (Attachments)/TV3_Hinh3_TongHop_HieuNang.png` (300 DPI) và bản vector `TV3_Hinh3_TongHop_HieuNang.pdf`; mã nguồn dựng hình tại `03 - Phương pháp & Thí nghiệm (Methodology & Experiments)/scripts/ve_hinh_photon_tv3.py`)*

---

### Thuyết minh chi tiết 5 nội dung theo yêu cầu hình đề xuất mới:

#### 1. Lý do đề xuất hình mới
* Trong 4 công trình nền tảng của đề tài (**BtrBlocks**, **Delta Lake**, **Photon**, **FeathrPO**), mỗi bài báo công bố kết quả định lượng bằng các đơn vị khác nhau (tốc độ quét `GB/s` hoặc `Gbps`, thời gian chạy theo giờ `h`, theo giây `s`, hay tỷ lệ rút gọn tương đối).
* Nếu chỉ đặt 4 chương cạnh nhau, người đọc khó hình dung bức tranh định lượng tổng thể về **mức độ cải thiện và tỷ lệ tiết kiệm thời gian tính toán** mà mỗi tầng đóng góp vào chuỗi đường ống dữ liệu cho Học máy (từ tệp cột → bảng ACID → thực thi truy vấn → đường ống đặc trưng ML).
* Hình đề xuất mới được thiết kế nhằm tổng hợp **đồng thời hai góc nhìn trực quan**: **(A) Hệ số cải thiện minh họa theo từng tầng** *(so với đối chứng `1,0×` riêng của mỗi nghiên cứu)* và **(B) Tỷ lệ cắt giảm thời gian thực thi tương ứng (`% Time Saved`)**, đồng thời tích hợp cơ chế ký hiệu trực quan (thanh gạch chéo cho cận trên *up to*, khung cảnh báo phương pháp luận) để ngăn ngừa lỗi diễn giải sai khi đối chiếu liên công trình.

---

#### 2. Dữ liệu, bảng đối chứng và công thức sử dụng
Toàn bộ số liệu được tổng hợp trực tiếp từ 4 bài báo gốc và đối khớp với báo cáo của các thành viên trong nhóm (TV1, TV2, TV3, TV4):

| Tầng kiến trúc | Công trình | Hệ số đưa vào Hình 3 | Tỷ lệ giảm thời gian tương ứng | Đối chứng, phạm vi & điều kiện đo | Nguồn |
| :--- | :--- | :---: | :---: | :--- | :--- |
| **Tầng 1:** Nén cột mở | **BtrBlocks** *(TV2)* | **`2,22×`** *(ghi chú $T_c$: `3,48×`)* | **`−55,0%`** | Băng thông giải nén dữ liệu gốc khi quét S3 ($T_u = 174,6$ vs. $78,6\text{ GB/s}$) so với **Parquet+Zstd** trên 5 tập Public BI lớn nhất, máy AWS `c5n.18xlarge` (`100 Gbps`). *(Tóm tắt bài báo nêu tổng quan `2,2×`)* | [3], Abstract, Hình 1 & Bảng 5 |
| **Tầng 2:** Bảng giao dịch ACID | **Delta Lake** *(TV1)* | **`1,55×`** *(ghi chú: `4,04×` vs. Presto)* | **`−35,4%`** *(`−75,3%` vs. Presto)* | Thời gian hoàn thành **TPC-DS 1 TB Power Test** (`0,93 giờ`) so với **3rd-Party Spark Parquet** (`1,44 giờ`) trên cụm AWS `1+8 i3.2xlarge`. *(So với 3rd-Party Presto `3,76 giờ` đạt `4,04×`)* | [2], Mục 6.2 & Hình 6 |
| **Tầng 3:** Thực thi Vector hóa | **Photon** *(TV3 — toàn chuẩn)* | **`4,00×`** *(tối đa `23×` ở Q1)* | **`−75,0%`** | Hệ số tăng tốc trung bình theo từng truy vấn trên **22 câu TPC-H SF=3000** so với **DBR**, cụm AWS `1+8 i3.2xlarge`, định dạng Delta Lake trên S3. | [1], Mục 6.2 & Hình 8 |
| **Tầng 3:** Thực thi Vector hóa | **Photon** *(TV3 — cơ chế thích nghi)* | **`1,55×`** | **`−35,6%`** | Truy vấn **TPC-DS Q24** (`118 s → 76 s`), **DBR** so với **Photon bật Adaptive Join Compaction**, cụm 16 nút. | [1], Mục 6.4 & Hình 9 |
| **Tầng 4:** ML Feature Store | **FeathrPO** *(TV4)* | **`tới 3,00×`** *(cận trên)* | **`tới −66,7%`** | Tối ưu hóa **point-in-time join** trong đường ống đặc trưng ML so với baseline trên các kịch bản TPCx-AI và bán lẻ. *(Là mức tối đa được tác giả báo cáo, không phải trung bình)* | [4], Abstract |

* **Công thức quy đổi tỷ lệ giảm thời gian thực thi (Biểu đồ B):**
  $$\% \text{ Time Saved} = \left(1 - \frac{1}{\text{Speedup}}\right) \times 100\% = \frac{T_{\text{Baseline}} - T_{\text{Đề xuất}}}{T_{\text{Baseline}}} \times 100\%$$

---

#### 3. Cách thức xây dựng hình
* **Công cụ:** Python 3 và thư viện **`matplotlib`** (hàm `build_figure_3()` trong script `ve_hinh_photon_tv3.py`).
* **Kỹ thuật thiết kế trực quan:**
  * Sử dụng bố cục 2 biểu đồ thanh ngang song song dùng chung trục tung (`sharey=True`, kích thước `14,8 × 6,4 inch`, mật độ `300 DPI`) để liệt kê rõ tên tầng, công trình và phạm vi đối chứng mà không bị chồng chữ.
  * Áp dụng thang màu phân biệt 4 tầng kiến trúc (xanh ngọc đậm cho BtrBlocks, xanh lam cho Delta Lake, xanh teal cho Photon, tím cho FeathrPO).
  * Riêng thanh **FeathrPO** được phủ hoa văn gạch chéo (`///`) kèm dấu hoa thị `*` để người xem nhận diện ngay đây là **cận trên tối đa (`up to 3,0×`)** chứ không phải trung bình.
  * Tích hợp đường tham chiếu `1,0×` ở Biểu đồ (A) và hộp lưu ý phương pháp luận rõ ràng ở chân hình.

---

#### 4. Giá trị thông tin và nguyên tắc diễn giải khoa học
1. **Nhìn toàn cảnh tiềm năng cải thiện tại từng nút thắt:** Cả 4 tầng đều ghi nhận mức tăng tốc đáng kể trong phạm vi bài toán riêng (`1,55×` đến `4,00×`, tương đương cắt giảm `35%–75%` thời gian thực thi từng pha), khẳng định rằng tối ưu hóa một tầng đơn lẻ là chưa đủ — hiệu năng hệ thống ML trên Lakehouse đòi hỏi tối ưu đồng bộ từ định dạng tệp, quản trị bảng, động cơ thực thi đến đường ống đặc trưng.
2. **Minh họa sự dịch chuyển vai trò trong cùng một tầng (Photon):** Đặt song song hai thanh của Photon (`4,00×` trung bình TPC-H và `1,55×` riêng Q24) cho thấy biên độ cải thiện phụ thuộc mạnh vào bản chất workload (phép tính thập phân/join lớn vs. truy vấn có batch thưa).
3. **Nguyên tắc liêm chính phương pháp luận (Cảnh báo bắt buộc):**
   * **Không xếp hạng tuyệt đối giữa các tầng** dựa trên chiều dài cột, vì mỗi công trình đo trên bộ dữ liệu, cụm phần cứng và mốc đối chứng `1,0×` hoàn toàn khác nhau.
   * **Tuyệt đối không cộng hoặc nhân các hệ số** (ví dụ không lấy $2,22 \times 1,55 \times 4,00 \times 3,00$) để suy diễn tốc độ đầu-cuối, do hiện tượng *Amdahl's Law* và sự chồng lấn chi phí giữa các tầng.
   * **Phân định chính xác bản chất đóng góp từng tầng:** [4] (FeathrPO) tối ưu *point-in-time join* (không được gộp nhầm thành hiệu quả thuần của tái sử dụng feature); [3] (BtrBlocks) hiện chưa là định dạng mặc định tương thích sẵn trong Delta Lake hay Photon mà đòi hỏi tích hợp lớp đọc/ghi và metadata tương ứng.

---

#### 5. Hình mới bổ sung điều gì so với từng bài báo gốc
* Không một bài báo gốc nào trong 4 công trình trực quan hóa đồng thời hiệu quả định lượng xuyên suốt chuỗi 4 tầng kiến trúc *Columnar Storage → ACID Table → Vectorized Engine → ML Feature Store*.
* Biểu đồ mới không chỉ chuyển hóa các kết quả rời rạc về cùng hệ quy chiếu trực quan (*Speedup* & *% Time Saved*), mà còn thiết lập một **khung tham chiếu khoa học trung thực** làm cầu nối trực tiếp cho Chương 4 (Phân tích đánh đổi & Khoảng trống nghiên cứu).

---

### Đề xuất quy trình kiểm chứng thực nghiệm đầu-cuối (End-to-End Evaluation Protocol)

Do 4 bài báo gốc đo trên 4 hạ tầng khác nhau, để kiểm chứng thực nghiệm kiến trúc tích hợp đề xuất một cách công bằng, nhóm đề xuất giao thức đo kiểm 4 bước tăng dần trên **cùng tập dữ liệu, cùng truy vấn và cùng cấu hình phần cứng**:
1. **Cấu hình cơ sở (Baseline):** Apache Spark + bảng Parquet/Delta Lake chưa bật tối ưu bố trí dữ liệu.
2. **Kích hoạt Tầng 2 (Delta Lake Optimization):** Bật Data Skipping kết hợp Z-Order/Hilbert Clustering với tập điều kiện lọc (*predicates*) được kiểm soát trên cùng bản chụp dữ liệu (*snapshot*).
3. **Kích hoạt Tầng 3 (Photon Execution):** Bật động cơ Photon trên cùng snapshot và cùng kế hoạch logic để tách biệt rõ đóng góp của CPU vectorization so với I/O skipping.
4. **Kích hoạt Tầng 4 (Feature Store Pipeline):** Bổ sung đường ống tạo đặc trưng và phép *point-in-time join* cho tập huấn luyện ML. *(Nhánh thay thế Parquet bằng BtrBlocks ở Tầng 1 chỉ đưa vào so sánh sau khi có trình đọc/ghi tích hợp tương thích metadata với Delta Lake).*

* **Tiêu chuẩn đo đạc:** Ghi nhận đồng thời tổng thời gian chạy, thời gian từng pha (I/O, giải nén, thực thi CPU, shuffle), số lượng tệp/byte đọc thực tế, mức sử dụng CPU/RAM và chi phí đám mây quy đổi; xác minh tính tương đương kết quả đầu ra ở mọi bước; cố định phiên bản phần mềm, tách bạch trạng thái *cold cache* và *warm cache*, lặp nhiều lần và báo cáo phân bố (trung vị, phân vị P95). *(Lưu ý: đây là **đề xuất thiết kế thực nghiệm** định hướng nghiên cứu tiếp theo, không phải kết quả đã chạy thực tế của nhóm).*

---

# PHẦN 6: DANH MỤC TÀI LIỆU THAM KHẢO (CHUẨN IEEE)

[1] A. Behm, S. Palkar, U. Agarwal, T. Armstrong, D. Cashman, A. Dave, T. Greenstein, S. Hovsepian, R. Johnson, A. S. Krishnan, P. Leventis, A. Luszczak, P. Menon, M. Mokhtar, G. Pang, S. Paranjpye, G. Rahn, B. Samwel, T. van Bussel, H. van Hovell, M. Xue, R. Xin, and M. Zaharia, "Photon: A Fast Query Engine for Lakehouse Systems," in *Proc. 2022 Int. Conf. Management of Data (SIGMOD '22)*, Philadelphia, PA, USA, Jun. 2022, pp. 2326–2339, doi: `10.1145/3514221.3526054`.

[2] M. Armbrust, T. Das, L. Sun, B. Yavuz, S. Zhu, M. Murthy, J. Torres, H. van Hövell, A. Ionescu, A. Łuszczak, M. Świtakowski, M. Szafrański, X. Li, T. Ueshin, M. Mokhtar, P. Boncz, A. Ghodsi, S. Paranjpye, P. Senster, R. Xin, and M. Zaharia, "Delta Lake: High-Performance ACID Table Storage over Cloud Object Stores," *Proc. VLDB Endow.*, vol. 13, no. 12, pp. 3411–3424, Aug. 2020, doi: `10.14778/3415478.3415560`.

[3] M. Kuschewski, D. Sauerwein, A. Alhomssi, and V. Leis, "BtrBlocks: Efficient Columnar Compression for Data Lakes," *Proc. ACM Manag. Data (PACMMOD)*, vol. 1, no. 2, Art. 118, pp. 118:1–118:26, Jun. 2023, doi: `10.1145/3589263`.

[4] R. Liu, K. Park, F. Psallidas, X. Huang, M. Interlandi, K. Karanasos, C. Curino, and J. Camacho-Rodríguez, "Optimizing Data Pipelines for Machine Learning in Feature Stores," *Proc. VLDB Endow.*, vol. 16, no. 13, pp. 4230–4239, Sep. 2023, doi: `10.14778/3625054.3625060`.

[5] M. Armbrust, R. S. Xin, C. Lian, Y. Huai, D. Liu, J. K. Bradley, X. Meng, T. Kaftan, M. J. Franklin, A. Ghodsi, and M. Zaharia, "Spark SQL: Relational Data Processing in Spark," in *Proc. 2015 ACM SIGMOD Int. Conf. Management of Data*, Melbourne, Australia, May 2015, pp. 1383–1394, doi: `10.1145/2723372.2742797`.

[6] P. A. Boncz, M. Zukowski, and N. Nes, "MonetDB/X100: Hyper-Pipelining Query Execution," in *Proc. 2nd Biennial Conf. Innovative Data Systems Research (CIDR)*, Asilomar, CA, USA, Jan. 2005, pp. 225–237.

[7] T. Kersten, V. Leis, A. Kemper, T. Neumann, A. Pavlo, and P. Boncz, "Everything You Always Wanted to Know About Compiled and Vectorized Queries But Were Afraid to Ask," *Proc. VLDB Endow.*, vol. 11, no. 13, pp. 2209–2222, Sep. 2018, doi: `10.14778/3275366.3275370`.

[8] A. Ngom, P. Menon, M. Butrovich, L. Ma, W. S. Lim, T. C. Mowry, and A. Pavlo, "Filter Representation in Vectorized Query Execution," in *Proc. 17th Int. Workshop on Data Management on New Hardware (DaMoN '21)*, Jun. 2021, Art. 6, pp. 1–7, doi: `10.1145/3465998.3466009`.

---

*Mã nguồn tái tạo đồng thời cả 03 hình ảnh (`PNG 300 DPI` và `PDF` vector): `03 - Phương pháp & Thí nghiệm (Methodology & Experiments)/scripts/ve_hinh_photon_tv3.py`.*
