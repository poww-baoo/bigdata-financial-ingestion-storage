# BÁO CÁO PHÂN TÍCH CÁ NHÂN (PHẦN RIÊNG — CUỐI KỲ)
**Cơ sở đào tạo:** Trường Đại học Sài Gòn – Khoa Công nghệ Thông tin  
**Học phần:** Phương pháp nghiên cứu khoa học trong Công nghệ thông tin  
**Đề tài nhóm:** *Hạ tầng quản trị dữ liệu hiện đại cho Học máy quy mô lớn: Liên kết Kiến trúc Data Lakehouse, Tối ưu hóa Lưu trữ Cột, Thực thi Vector hóa và Feature Store* *(Đề tài C)*  
**Phần cá nhân phụ trách (Tầng 1):** Phân tích và Trực quan hóa bài báo *"BtrBlocks: Efficient Columnar Compression for Data Lakes"*  
**Sinh viên thực hiện:** Nguyễn Đình Cường *(TV2)* | **MSSV:** `3123411043`  
**Giảng viên hướng dẫn:** Vũ Ngọc Thanh Sang  
**Ngày thực hiện:** 2026-11-25  

---

# PHẦN 1: THÔNG TIN VÀ NGUỒN BÀI BÁO

### 1. Tên bài báo (Paper Title)
* **Tiếng Anh:** *BtrBlocks: Efficient Columnar Compression for Data Lakes*
* **Dịch nghĩa tiếng Việt:** *BtrBlocks: Nén dữ liệu dạng cột hiệu quả cho Hồ dữ liệu (Data Lakes)*

---

### 2. Danh sách tác giả & Cơ quan công tác (Authors & Affiliations)
Bài báo được thực hiện bởi nhóm 04 nhà nghiên cứu hệ thống cơ sở dữ liệu hàng đầu tại Đức:
* **Maximilian Kuschewski** (`maximilian.kuschewski@tum.de`) — Technische Universität München (TU Munich), Đức.
* **David Sauerwein** (`david.sauerwein@fau.de`) — Friedrich-Alexander-Universität Erlangen-Nürnberg (FAU), Đức.
* **Adnan Alhomssi** (`adnan.alhomssi@fau.de`) — Friedrich-Alexander-Universität Erlangen-Nürnberg (FAU), Đức.
* **Viktor Leis** (`leis@in.tum.de`) — Technische Universität München (TU Munich), Đức *(tác giả nổi tiếng trong cộng đồng CSDL với các công trình tối ưu hóa truy vấn và kiến trúc lưu trữ đám mây)*.

---

### 3. Tên tạp chí / Kỷ yếu hội nghị (Journal / Proceedings)
* **Tên chính thức:** *Proceedings of the ACM on Management of Data (PACMMOD)* — Kỷ yếu tạp chí hóa của hội nghị **ACM SIGMOD 2023**.
* **Nhà xuất bản:** Association for Computing Machinery (ACM), New York, NY, USA.
* **Mã số tiêu chuẩn quốc tế (Online ISSN):** `2836-6573`.
* **Quy cách xuất bản:** Tập 1 (Volume 1), Số 2 (Issue 2), Bài số 118 (Article 118), Tháng 6/2023, Trang `118:1 – 118:26` (26 trang). *(Nhận bài: tháng 10/2022; chỉnh sửa: tháng 1/2023; chấp nhận đăng: tháng 2/2023).*
* **Mã nguồn mở đi kèm:** [https://github.com/maxi-k/btrblocks](https://github.com/maxi-k/btrblocks).

---

### 4. Năm công bố (Year of Publication)
* **Năm công bố chính thức:** **2023** (Tháng 6 năm 2023).

---

### 5. DOI & Đường dẫn chính thức của bài báo (DOI & Official Links)
* **Mã định danh số (DOI):** [`10.1145/3589263`](https://doi.org/10.1145/3589263)
* **Đường dẫn trên thư viện điện tử ACM Digital Library:** [https://dl.acm.org/doi/10.1145/3589263](https://dl.acm.org/doi/10.1145/3589263)
* **Bản PDF lưu trữ trong Vault:** [BtrBlocks PDF](<../01 - Tổng quan tài liệu (Literature Review)/Bài báo đã đọc (Papers)/BtrBlocks: Efficient Columnar     
  Compression for Data Lakes.pdf>)

---

### 6. Thông tin chứng minh ấn phẩm thuộc Web of Science, CORE & Scopus
Từ năm 2023, **ACM SIGMOD** chuyển đổi mô hình xuất bản kỷ yếu hội nghị sang tạp chí định kỳ *Proceedings of the ACM on Management of Data (PACMMOD)* (`ISSN: 2836-6573`):
* **Minh chứng trên Web of Science (Clarivate):**
  * Tạp chí *Proceedings of the ACM on Management of Data* (`ISSN: 2836-6573`) được lập chỉ mục chính thức trong **Web of Science Core Collection**, thuộc phân nhóm **Emerging Sources Citation Index (ESCI)** (tra cứu tại Clarivate Master Journal List: [https://mjl.clarivate.com](https://mjl.clarivate.com)).
* **Minh chứng xếp hạng CORE (Computing Research and Education Association of Australasia):**
  * Hội nghị gốc **ACM SIGMOD** đạt thứ hạng **CORE A\*** — hạng xuất sắc cao nhất toàn cầu trong ngành Khoa học Máy tính / Cơ sở dữ liệu.
  * Do *PACMMOD* mới được ACM thành lập từ năm 2023 để thay thế kỷ yếu SIGMOD truyền thống, Ủy ban Điều hành ACM SIGMOD ban hành hướng dẫn chuyển tiếp chính thức khuyến nghị các hội đồng học thuật ghi nhận các bài báo *PACMMOD* thuộc kỳ SIGMOD có giá trị học thuật tương đương tuyệt đối với **ACM SIGMOD (CORE A\*)**.
* **Minh chứng trên Scopus / ScimagoJR:**
  * Do *PACMMOD* là ấn phẩm mới khởi tạo từ năm 2023 theo mô hình *Proceedings of the ACM*, các chỉ số định lượng tích lũy nhiều năm (CiteScore của Scopus và SJR/Quartile trên ScimagoJR) được Elsevier cập nhật theo chu kỳ đánh giá đa niên sau khi đủ cửa sổ trích dẫn; thông tin nguồn được theo dõi qua mã `ISSN: 2836-6573` tại [Scopus Source List](https://www.scopus.com/sources.uri) và [ScimagoJR](https://www.scimagojr.com). Về mặt thực chất học thuật, PACMMOD kế thừa trực tiếp vị thế nhóm đầu (**Top-tier / tương đương Q1**) của kỷ yếu ACM SIGMOD.

---

### 7. Chỉ số ảnh hưởng & Mức độ trích dẫn (Impact Metrics & Citations)
Theo dữ liệu thư mục học mở **OpenAlex** (`https://openalex.org/S4387289859` cho *Proceedings of the ACM on Management of Data*, `ISSN: 2836-6573`) và **Google Scholar**:
* **Chỉ số trích dẫn trung bình 2 năm (2-year mean citedness — OpenAlex):** **8.8**
* **Chỉ số h-index của ấn phẩm (OpenAlex):** **53** (`i10-index: 495`, tổng cộng `1,202` công trình và `17,379` lượt trích dẫn tính chung cho PACMMOD).
* **Tình trạng lõi học thuật (OpenAlex):** Được gắn nhãn `is_core: true`, nằm trong các danh mục chuẩn `cwts-core`, `norway-1`, `vabb-shw`.
* **Số lượt trích dẫn của riêng bài báo *BtrBlocks*:** Đạt **89 lượt trích dẫn** theo thống kê OpenAlex và **hơn 120 lượt trích dẫn** trên Google Scholar chỉ sau hơn 3 năm công bố — cho thấy mức độ ảnh hưởng nhanh và sâu rộng đối với các hệ thống Data Lake và định dạng lưu trữ cột thế hệ mới.

---

### 8. Lĩnh vực của bài báo (Subject Area & Classification)
* **Phân loại theo ACM Computing Classification System (CCS):** *Information systems → Column based storage; Data compression.*
* **Từ khóa gốc của tác giả:** `data lake`, `query processing`, `compression`, `columnar storage`.
* **Lĩnh vực chuyên môn tương ứng trên ScimagoJR / WoS:**
  1. *Computer Science: Information Systems / Database Management*
  2. *Computer Science: Software & Data Engineering*
  3. *Computer Science: Computer Networks and Distributed Storage*

---

# PHẦN 2: PHÂN TÍCH NỘI DUNG NGHIÊN CỨU

### 1. Bối cảnh và vấn đề nghiên cứu (Context & Problem Statement)
* **Bối cảnh (Context):**
  * Các hệ thống phân tích dữ liệu (Data Warehousing & Analytics) đang dịch chuyển mạnh mẽ lên điện toán đám mây theo kiến trúc tách rời lưu trữ và tính toán (*disaggregated storage and compute*), trong đó dữ liệu được đặt trên các dịch vụ lưu trữ đối tượng giá rẻ như Amazon S3, Azure Blob hoặc Google Cloud Storage.
  * Trước đây, các kho dữ liệu đám mây (Snowflake, BigQuery, Redshift) sử dụng định dạng đóng độc quyền (*proprietary formats*), vô tình tạo ra "bẫy dữ liệu" (*proprietary data traps*): các hệ thống ML hoặc BI bên ngoài phải trích xuất và nhân bản dữ liệu ra ngoài, gây tốn kém chi phí.
  * Để đảm bảo tính tương tác mở (*interoperability*), mô hình **Data Lake** sử dụng các định dạng tệp cột mở như **Apache Parquet** và **Apache ORC**. Đồng thời, phần cứng mạng đám mây đã có bước nhảy vọt lên **100 Gbps** (ví dụ máy chủ AWS `c5n` hoặc `c6gn`), khiến băng thông mạng không còn là nút thắt cổ chai duy nhất như trước.
* **Vấn đề nghiên cứu cốt lõi (Problem Statement):**
  * **Giải nén chậm làm nghẽn CPU (CPU-bound scans):** Apache Parquet có tập lược đồ mã hóa hạn chế và luật chọn lược đồ quá đơn giản (mặc định bản C++ chỉ thử Dictionary, nếu từ điển lớn thì bỏ qua không nén). Do đó, thực tế người dùng phải bọc thêm lớp nén đa dụng nặng nề như Snappy, LZ4 hoặc Zstd. Khi đọc qua mạng 100 Gbps, CPU bị bão hòa ở khâu giải nén Zstd/Snappy trước khi khai thác hết băng thông mạng, làm tăng mạnh thời gian chạy truy vấn và chi phí thuê máy chủ ảo.
  * **Thiếu tối ưu cho dữ liệu thực tế (Real-world Data Lakes):** Các bộ dữ liệu thực tế chứa rất nhiều chuỗi dài có tiền tố chung, giá trị phân bố lệch (*skew*), nhiều giá trị NULL không đồng nhất và rất nhiều số thực dấu phẩy động (`double`, ví dụ giá tiền `3.25` hoặc `0.99`) vốn không tương thích với các thuật toán nén số nguyên truyền thống.
  * **Gắn chặt metadata vào file dữ liệu:** Parquet nhúng metadata, thống kê và chỉ mục vào phần đuôi file (*footer*), buộc client khi đọc từng cột đơn lẻ từ S3 phải thực hiện 3 HTTP GET request tuần tự phụ thuộc nhau trước khi tải được dữ liệu cột.

---

### 2. Khoảng trống nghiên cứu mà tác giả muốn giải quyết (Research Gap)
Trước *BtrBlocks*, hai nhánh tiếp cận đều tồn tại khoảng trống rõ rệt:
1. **Định dạng mở truyền thống (Parquet, ORC):** Phổ biến và tương thích rộng, nhưng bộ mã hóa ít ỏi, heuristic tĩnh kém linh hoạt và phụ thuộc vào nén đa dụng (Snappy/Zstd) nên tốc độ giải nén thấp trên mạng tốc độ cao.
2. **Nghiên cứu nén học thuật & hệ thống đóng (SQL Server, DB2 BLU, HyPer Data Blocks, Damme et al.):**
   * Phần lớn nghiên cứu chỉ tập trung vào **một kiểu dữ liệu riêng lẻ** (chủ yếu là số nguyên `int`, rất ít công trình giải quyết đồng thời cả `string` và `double`).
   * Chưa có **thiết kế đầu-cuối (end-to-end)** hoàn chỉnh cho định dạng mở trên Data Lake: vừa có tập lược đồ nhẹ bổ trợ nhau, vừa cho phép **nén đệ quy đa tầng (multi-level cascading)** trên mọi kiểu dữ liệu, vừa có thuật toán lấy mẫu tự động chọn lược đồ nhanh mà không cần xây dựng mô hình chi phí (*cost model*) phức tạp.
   * Các định dạng nghiên cứu trước (như HyPer Data Blocks hay SAP BRPFC) tối ưu cho độ trễ truy cập điểm (*point-access latency*) trong bộ nhớ (in-memory), trong khi Data Lake trên Object Storage đòi hỏi tối ưu **thông lượng quét và tốc độ giải nén hàng loạt (bulk decompression bandwidth)**.

---

### 3. Mục tiêu nghiên cứu (Research Objectives)
1. **Thiết kế một định dạng lưu trữ cột mã nguồn mở mới (BtrBlocks)** tối ưu cho Data Lake trên mạng đám mây băng thông cao, cân bằng đồng thời **tỷ lệ nén cao** và **tốc độ giải nén cực nhanh** mà không dùng nén đa dụng nặng nề (Snappy/Zstd).
2. **Xây dựng khung nén đệ quy đa tầng (Cascading Compression Framework)** kết hợp thuật toán **chọn lược đồ dựa trên lấy mẫu (Sampling-based Scheme Selection)** gọn nhẹ, mở rộng được cho cả 3 kiểu dữ liệu: số nguyên, số thực và chuỗi.
3. **Đề xuất thuật toán nén mới cho số thực (`Pseudodecimal Encoding` — PDE)** nhằm khai thác đặc trưng của các giá trị thập phân lưu dưới dạng IEEE 754 `double` trong dữ liệu thực tế và dữ liệu Học máy.
4. **Tối ưu hóa triệt để thuật toán giải nén bằng tập lệnh vector SIMD (AVX2)** và loại bỏ các chi phí phụ (như copy chuỗi không cần thiết) để giảm tổng chi phí quét trên Cloud Object Store (S3).

---

### 4. Câu hỏi nghiên cứu & Giả thuyết khoa học (Research Questions & Hypotheses)
Trong quá trình thiết kế và thực nghiệm (đặc biệt tại Mục 6.3, 6.7 và 6.8), bài báo xoay quanh các câu hỏi cốt lõi sau:
* **RQ1:** Với ngân sách kích thước mẫu cố định (`1%` của một block), chiến lược lấy mẫu nào vừa giữ được tính cục bộ không gian (*spatial locality*) vừa phản ánh đúng phân bố toàn block, và kích thước mẫu ảnh hưởng thế nào đến chất lượng nén?
* **RQ2:** Việc tắt các tối ưu hóa phần cứng cấp thấp (SIMD) có làm mất lợi thế của BtrBlocks hay không — nói cách khác, tốc độ vượt trội đến từ thiết kế kiến trúc định dạng bậc cao hay chỉ đơn thuần nhờ lập trình SIMD?
* **RQ3:** Khi xét trên hạ tầng mạng đám mây 100 Gbps (AWS `c5n.18xlarge` đọc từ S3), tốc độ giải nén nhanh hơn có thực sự giúp giảm chi phí quét đầu-cuối (tiền thuê EC2 + phí S3 GET) so với Parquet+Zstd/Snappy hay không?
* **Giả thuyết nghiên cứu (Hypothesis):** *"Bằng cách kết hợp một tập hợp chọn lọc các lược đồ mã hóa nhẹ chuyên biệt theo kiểu dữ liệu, cho phép áp dụng đệ quy tối đa 3 tầng thông qua thuật toán lấy mẫu $10 \times 64$ phần tử, đồng thời tách rời siêu dữ liệu khỏi khối dữ liệu nén, BtrBlocks có thể đạt tỷ lệ nén tiệm cận các định dạng dùng nén đa dụng (như Parquet+Snappy/Zstd) nhưng giải nén nhanh hơn nhiều lần, qua đó khai thác gần tối đa băng thông mạng 100 Gbps và cắt giảm đáng kể chi phí vận hành trên Data Lake."*

---

### 5. Đối tượng nghiên cứu (Object of Study)
* **Đối tượng nghiên cứu chính:** **Định dạng lưu trữ cột mở và kiến trúc nén/giải nén dữ liệu theo khối (Open Columnar Storage Format & Block-based Compression/Decompression Engine)** phục vụ truy vấn phân tích trên Cloud Data Lakes.
* **Cơ chế tách biệt thiết kế:** BtrBlocks chỉ chịu trách nhiệm nén và lưu các block dữ liệu cột kích thước cố định (mặc định **64.000 giá trị/block**); phần metadata, thống kê min/max và chỉ mục được tách rời hoàn toàn (*orthogonal*) để các tầng bảng phía trên (như Delta Lake / Iceberg) hoặc hệ thống quản lý bảng tự xử lý.

---

### 6. Dữ liệu và Tập dữ liệu sử dụng (Datasets & Benchmarks)
Bài báo chỉ ra hạn chế của dữ liệu tổng hợp (như TPC-H vốn chuẩn hóa quá mức, phân bố đều và phần lớn số nguyên là khóa chính/ngoại ít lặp) nên sử dụng kết hợp hai bộ chuẩn:
1. **Public BI Benchmark (Bộ dữ liệu thực tế trọng tâm):**
   * Thu thập từ các workbook thực tế lớn nhất trên Tableau Public, phản ánh đúng tính chất phức tạp của Data Lake ngoài đời thực: lệch phân bố (*data skew*), bảng phi chuẩn hóa, lạm dụng chuỗi (`71.5%` dung lượng), biểu diễn `NULL` đa dạng và lưu số thập phân dưới dạng `double` (`14.4%`).
   * **Tập con thử nghiệm chuẩn hóa:** Gồm **43 bảng** lớn nhất đại diện cho 43 bộ dữ liệu (loại bỏ `IUBLibrary`, `IGlocations`, `Hatred1` quá nhỏ và tách các cột ngày/giờ sang số nguyên), tổng dung lượng nhị phân trong RAM là **119.5 GB**, gồm **2.451 cột** (trung bình 57 cột/bảng, dao động từ 6 đến 519 cột).
   * **Tập thử nghiệm S3 End-to-End:** 5 workbook Public BI lớn nhất (loại các bảng có file CSV dưới 6 GB).
2. **TPC-H Benchmark (Bộ dữ liệu chuẩn đối chứng):**
   * Gồm `61.7%` String, `19.5%` Double, `18.7%` Integer về mặt dung lượng (theo Table 2), được dùng để đối chiếu công bằng với các nghiên cứu liên quan trước đây.

---

### 7. Các biến số, đặc trưng và thông tin đầu vào quan trọng (Variables & Parameters)
* **Kiểu dữ liệu đầu vào được hỗ trợ:** Số nguyên (`Integer`), Số thực dấu phẩy động (`Double` 64-bit IEEE 754), Chuỗi có độ dài biến thiên (`String`), và Bitmask đánh dấu giá trị `NULL`.
* **Siêu tham số cấu hình lõi của BtrBlocks:**
  * Kích thước khối (Block size): Mặc định `64.000` phần tử/cột/block.
  * Chiến lược lấy mẫu (Sampling): `10` đoạn liên tiếp × `64` phần tử = `640` phần tử (`1%` kích thước block), lấy tại các vị trí ngẫu nhiên trên các phân vùng không chồng lấn.
  * Độ sâu đệ quy tối đa (Max recursion depth): Mặc định `recur = 3` tầng.
  * Ngưỡng loại trừ heuristic (Section 3.1 & 4.2): Bỏ qua RLE nếu độ dài chuỗi lặp trung bình `< 2`; bỏ qua Frequency nếu tỷ lệ giá trị duy nhất $\ge 50\%$; tắt Pseudodecimal nếu tỷ lệ ngoại lệ (exceptions) $> 50\%$ hoặc tỷ lệ giá trị duy nhất $< 10\%$; hợp nhất giải nén RLE+Dict nếu độ dài run trung bình $> 3$.
* **Thống kê thu thập một lượt (Single-pass stats):** `min`, `max`, `unique count`, `average run length`.
* **Biến số môi trường thực nghiệm (Section 6):**
  * Máy chủ: AWS EC2 **`c5n.18xlarge`** (CPU Intel Xeon Platinum 8000 Skylake-SP, `36` nhân × `3.5 GHz` / 72 luồng, hỗ trợ AVX2 và AVX512, `192 GiB` RAM, mạng **`100 Gbps`**).
  * Phần mềm & cấu hình: Biên dịch bằng `GCC 10.3.1` trên Amazon Linux 2 (kernel `5.10`), song song hóa bằng **Intel TBB**, tắt hyperthreading, cấp phát và chạm bộ nhớ trước để tránh lỗi trang (*page faults*).
  * Đối thủ so sánh: Apache Parquet (`pyarrow 9.0.0`, rowgroup size $2^{17}$, đọc qua Arrow C++ low-level API) kết hợp không nén / `LZ4` / `Snappy` / `Zstd`; Apache ORC (`pyarrow 9.0.0` + `orc::InputStream` tùy biến trên bộ nhớ); và 4 hệ quản trị cột thương mại ẩn danh (`System A–D`).
  * Tham số tính phí đám mây S3 (Section 6.7): Giá thuê `c5n.18xlarge` = `$3.89 / giờ`; phí gọi `S3 GET` = `$0.0004 / 1,000 requests`; kích thước chunk tải từ S3 = `16 MB`.

---

### 8. Phương pháp, thuật toán, mô hình và quy trình nghiên cứu (Methodology & Architecture)
BtrBlocks áp dụng phương pháp **Thiết kế Kiến trúc Định dạng Cột (Systems Engineering) kết hợp Tối ưu hóa Thực nghiệm theo Dữ liệu thực tế (Data-Driven Empirical Selection)**:

#### A. Tập 09 lược đồ mã hóa nhẹ (Table 1)
1. **Nhóm dùng chung mọi kiểu dữ liệu:** `RLE` (Run-Length Encoding lưu cặp `(giá trị, độ dài)`), `One Value` (chuyên biệt khi cả block chỉ có 1 giá trị duy nhất), `Dictionary` (ánh xạ giá trị sang mã code ngắn hơn), `Frequency` (tối ưu cho phân bố lệch cực mạnh: chỉ lưu giá trị phổ biến nhất, bitmap đánh dấu vị trí và mảng các giá trị ngoại lệ).
2. **Nhóm số nguyên (`Integer`):** `SIMD-FastPFOR` (Patched Frame of Reference tách giá trị ngoại lệ để giữ bitwidth nhỏ) và `SIMD-FastBP128` (bit-packing tối ưu SIMD theo khối 128 phần tử).
3. **Nhóm chuỗi (`String`):** `FSST` (Fast Static Symbol Table — thay thế các chuỗi con lặp lại độ dài tối đa 8 byte bằng mã 1 byte tra cứu qua bảng ký hiệu tĩnh tối đa 255 mục). Có thể áp dụng `FSST` trực tiếp lên chuỗi thô hoặc lên từ điển (`Dict + FSST`).
4. **Nhóm Bitmap (`NULL` & Exceptions):** `Roaring Bitmap` — tự động chọn cấu trúc lưu trữ tùy theo mật độ bit cục bộ.
5. **Nhóm số thực (`Double`) — Đóng góp mới `Pseudodecimal Encoding (PDE)` (Mục 4):**
   * *Vấn đề:* Số thập phân như `0.99` khi lưu theo chuẩn IEEE 754 `double` bị biến thành `0.98999...` với phần định trị (*mantissa*) tuần hoàn dài (`0xfae147ae147ae`) và phần mũ (*exponent*) biến động mạnh giữa `3.25` và `0.99`, khiến Bit-packing và FOR thất bại.
   * *Ý tưởng cốt lõi:* Tách mỗi số `double` thành cặp số nguyên `(digits, exp)` với $digits \in \text{int32}$, $exp \in [0, 22]$ (5 bit) sao cho $\text{digits} \times 10^{-\text{exp}} \equiv \text{double}$ (khớp từng bit khi giải nén). Ví dụ: `3.25` $\rightarrow (325, 2)$; `0.98999...` $\rightarrow (99, 2)$.
   * *Đảm bảo không mất dữ liệu (Lossless):* Các trường hợp đặc biệt (`-0.0`, `±Inf`, `±NaN`) hoặc số quá nhỏ/lớn không biểu diễn được (như `5.5e-42`) được gán mã lỗi `exp = 23` và lưu nguyên gốc vào mảng `patches`. Hai mảng số nguyên `digits` và `exponents` sinh ra sau đó tiếp tục được nén đệ quy bằng các thuật toán số nguyên như `SIMD-FastPFOR` hoặc `RLE`.

#### B. Quy trình chọn lược đồ qua Lấy mẫu & Nén Đệ quy (Mục 3)
Tại mỗi tầng đệ quy (tối đa `3` tầng), thuật toán `pickScheme` thực hiện 5 bước:
1. Quét 1 lượt thu thập thống kê cơ bản (`min`, `max`, `unique count`, `avg run length`).
2. Dùng luật heuristic loại bỏ nhanh các lược đồ không khả thi (tránh chạy thử vô ích).
3. Lấy mẫu phân tầng ngẫu nhiên gồm `10` đoạn $\times$ `64` phần tử (`= 1%` block) và nén thử mẫu với từng lược đồ còn lại để ước lượng tỷ lệ nén.
4. Chọn lược đồ có tỷ lệ nén ước lượng cao nhất để nén toàn bộ block.
5. Nếu đầu ra của lược đồ là các luồng dữ liệu còn nén được (ví dụ: `codes`, `values`, `lengths`, `exceptions`), gọi đệ quy lại từ Bước 1 với `recur - 1` cho đến khi chạm đáy `recur = 0` hoặc gặp lá kết thúc.

#### C. Kỹ thuật Giải nén Vector hóa Tốc độ cao (Mục 5)
* **RLE bằng AVX2 (`decodeRLEAVX`):** Nhân bản đồng thời 8 số `int` (hoặc 4 số `double`) bằng thanh ghi 256-bit; chấp nhận ghi tràn nhẹ ra cuối bộ đệm đệm sẵn ($\ge 32$ byte) rồi đặt lại con trỏ `dst = target` để loại bỏ hoàn toàn câu lệnh rẽ nhánh (*branch misprediction*).
* **Dictionary không sao chép chuỗi (Zero-copy String Dictionary):** Thay vì copy toàn bộ chuỗi khi giải nén, BtrBlocks giải mã chuỗi mã code thành mảng các cặp `(offset, length)` 64-bit trỏ vào vùng nhớ chuỗi, dùng chung nhân AVX2 gather (`_mm256_i32gather_epi32`) với loop unroll `4×`.
* **Hợp nhất RLE + Dictionary (Kernel Fusion):** Khi mã từ điển được nén tiếp bằng RLE (với độ dài run $> 3$), tra từ điển trước rồi ghi lặp cặp `(offset, size)` trực tiếp, bỏ qua mảng trung gian.
* **FSST theo lô & Pseudodecimal SIMD:** Truyền toàn bộ khối chuỗi nối tiếp cho API giải nén của FSST thay vì gọi từng chuỗi (giảm `50` lệnh CPU/chuỗi); giải nén PDE bằng lệnh nhân vector `_mm256_cvtepi32_pd` và `_mm256_mul_pd` kèm kiểm tra Roaring Bitmap.

---

### 9. Các chỉ số dùng để đánh giá kết quả (Evaluation Metrics)
1. **Tỷ lệ nén (Compression Ratio / Factor):**
   $$\text{Compression Ratio} = \frac{\text{Dung lượng dữ liệu gốc chưa nén (Binary Size)}}{\text{Dung lượng sau khi nén (Compressed Size)}}$$
2. **Tốc độ nén (Compression Speed):** Đo bằng `MB/s` ở chế độ đơn luồng (tính từ cả file CSV lẫn dữ liệu nhị phân in-memory).
3. **Băng thông giải nén theo dữ liệu gốc ($T_u$ — Uncompressed Decompression Bandwidth):**
   $$T_u = \frac{\text{Kích thước dữ liệu sau giải nén}}{\text{Thời gian giải nén}} \quad [\text{GB/s}]$$
4. **Thông lượng giải nén theo dữ liệu nén ($T_c$ — Compressed Decompression Throughput):**
   $$T_c = \frac{\text{Kích thước dữ liệu nén}}{\text{Thời gian giải nén}} = \frac{T_u}{\text{Compression Ratio}} \quad [\text{Gbit/s}]$$
   *(Đây là chỉ số quyết định xem CPU có giải nén kịp để bão hòa đường truyền mạng S3 `100 Gbps` hay không).*
5. **Độ chính xác chọn lược đồ qua lấy mẫu:** Tỷ lệ phần trăm số block chọn được lược đồ tối ưu (hoặc chỉ kém tối ưu tối đa `2%`).
6. **Chi phí quét S3 đầu-cuối (End-to-End S3 Scan Cost):** Tổng chi phí thuê máy ảo EC2 (`$3.89/h`) cộng chi phí các lời gọi `S3 GET` (`$0.0004/1,000 requests`), đo bằng USD (`$`) hoặc chuẩn hóa thành số lượt quét trên mỗi Đô-la (*S3 Scans per Dollar*).

---

### 10. Những kết quả chính của nghiên cứu (Key Findings)
* **Tỷ lệ nén cao tương đương hệ thống thương mại (Mục 6.4, Hình 7):**
  * Trên Public BI Benchmark, BtrBlocks đạt hệ số nén tổng hợp **`7.06×`**, vượt qua **cả 4 hệ quản trị cột thương mại (System A–D)**, vượt Parquet thuần, Parquet+LZ4 và **Parquet+Snappy (`6.88×`)**, chỉ đứng sau định dạng nén nặng **Parquet+Zstd (`8.24×`)**.
  * Tốc độ nén đơn luồng từ dữ liệu nhị phân trong RAM của BtrBlocks đạt **`75.3 MB/s`**, nhanh hơn **~1.8×** so với Parquet+Snappy (`41.9 MB/s`) và Parquet+Zstd (`41.0 MB/s`).
* **Hiệu quả thuật toán lấy mẫu (Mục 6.3, Hình 5 & 6):**
  * Lấy mẫu `10 × 64` phần tử (`1%` block) chỉ tiêu tốn **`1.2%` thời gian CPU** lúc nén nhưng đạt tỷ lệ chọn đúng lược đồ **`77%`** và kích thước nén trung bình chỉ kém phương án tối ưu lý tưởng **`3.3%`**.
* **Hiệu quả Pseudodecimal Encoding trên dữ liệu số thực (Mục 6.5, Bảng 3):**
  * Kết hợp với `FastBP128`, PDE vượt trội hơn các thuật toán nén số thực kinh điển như FPC, Gorilla, Chimp và Chimp128 trên các cột dữ liệu giá cả / tài chính ít chữ số thập phân (ví dụ cột `CommonGov./26` đạt tỷ lệ nén **`75.0×`** so với `48.0×` của Gorilla và `6.9×` của Chimp128).
* **Tốc độ giải nén In-Memory vượt trội (Mục 6.6, Hình 8):**
  * Trên **Public BI**, BtrBlocks giải nén nhanh hơn **`2.6×`** so với Parquet không nén thêm, **`3.6×`** so với Parquet+Snappy và **`3.8×`** so với Parquet+Zstd. Trên **TPC-H**, mức tăng tốc tương ứng là **`2.6×`**, **`3.9×`** và **`4.2×`**.
  * Đáng chú ý, ngay cả khi **tắt toàn bộ SIMD** để chạy phiên bản tuần tự (*scalar*, Mục 6.8), tốc độ giải nén của BtrBlocks chỉ giảm **`17%`** và vẫn nhanh hơn **`2.3×`** so với biến thể Parquet nhanh nhất — chứng minh lợi thế đến từ thiết kế kiến trúc bậc cao.
* **Khai thác tối đa mạng 100 Gbps và cắt giảm chi phí S3 (Mục 6.7, Bảng 5 & Hình 1):**
  * Khi quét toàn bộ 5 tập Public BI lớn nhất từ S3 trên `c5n.18xlarge` (mạng `100 Gbps`, giới hạn thực tế S3 client đạt `~91 Gbps`), BtrBlocks đạt thông lượng dữ liệu nén **$T_c = 86.2\text{ Gbit/s}$** ($T_u = 174.6\text{ GB/s}$), gần chạm ngưỡng giới hạn phần cứng; trong khi Parquet+Snappy chỉ đạt `33.2 Gbit/s` và Parquet+Zstd chỉ đạt `24.8 Gbit/s` (nghẽn CPU).
  * Tổng chi phí quét của BtrBlocks là **`$0.97`** (`1.00×`), rẻ hơn **`2.61×`** so với Parquet thuần (`$2.47`) và rẻ hơn khoảng **`1.8×`** so với Parquet+Snappy (`$1.74`) và Parquet+Zstd (`$1.70`). Nếu quét chọn lọc từng cột đơn lẻ (*selective column reads*), BtrBlocks còn rẻ hơn **`9×`** so với Parquet nén và **`20×`** so với Parquet không nén do loại bỏ được 3 lượt GET metadata footer tuần tự của Parquet.

---

# PHẦN 3: VẼ LẠI 02 HÌNH MINH HỌA TỪ BÀI BÁO GỐC

---

## 3.1. HÌNH 1: CÂY QUYẾT ĐỊNH LƯỢC ĐỒ MÃ HÓA ĐỆ QUY (FIGURE 3 BÀI BÁO)

### Hình ảnh tái tạo:
![Hình tái tạo Figure 3: Cây quyết định lược đồ mã hóa đệ quy trong BtrBlocks](<../../99 - Đính kèm (Attachments)/BtrBlocks_Hinh1_TaiTao_CayQuyetDinhNen.png>)

*(Tệp hình ảnh chất lượng cao lưu tại: `99 - Đính kèm (Attachments)/BtrBlocks_Hinh1_TaiTao_CayQuyetDinhNen.png` (300 DPI) và bản vector `BtrBlocks_Hinh1_TaiTao_CayQuyetDinhNen.pdf`; mã nguồn dựng hình tại `03 - Phương pháp & Thí nghiệm (Methodology & Experiments)/scripts/ve_btrblocks_hinh1_cay_quyet_dinh.py`)*

---

### Thuyết minh chi tiết 7 nội dung theo yêu cầu:

#### 1. Vị trí hình gốc trong bài báo
* **Hình gốc:** **Figure 3**, xuất hiện tại **Trang 7 (`118:7`)** của bài báo (thuộc Mục 3.2: *Cascading*).
* **Tiêu đề gốc:** *"Fig. 3. Encoding scheme decision trees that we apply recursively."*

#### 2. Mục đích của hình
* Minh họa trực quan **kiến trúc nén đệ quy đa tầng (Cascading Compression Architecture)** của BtrBlocks: chỉ rõ tập lược đồ mã hóa ứng viên dành cho mỗi kiểu dữ liệu gốc (`Double`, `String`, `Integer`) và các điểm rẽ nhánh đệ quy cho phép đầu ra của một lược đồ này trở thành đầu vào để nén tiếp bằng lược đồ khác.

#### 3. Các biến số và thông tin được thể hiện
* **Ba cây quyết định theo 3 kiểu dữ liệu cột:**
  1. **Cây `Double` (Số thực):** 6 nhánh ứng viên gồm `Frequency` (tách thành `bitmap → Roaring Bitmap` và `exceptions → Double`), `One Value`, `RLE` (tách thành `length → Integer` và `value → Double`), `Dict` (tách `codes → Integer`), `Uncompressed`, và `Pseudodecimal` (tách `exceptions → Double` và `values → Integer`).
  2. **Cây `String` (Chuỗi):** 5 nhánh ứng viên gồm `FSST`, `Dict + FSST` (tách `codes → Integer` và `string pool → FSST`), `One Value`, `Dict` (tách `codes → Integer`, `lengths → Integer`, `strings → Uncompressed`), và `Uncompressed`.
  3. **Cây `Integer` (Số nguyên):** 6 nhánh ứng viên gồm `Uncompressed`, `RLE` (tách `values → Integer` và `lengths → Integer`), `SIMD-FastPFOR`, `SIMD-FastBP128`, `One Value`, và `Dict` (tách `codes → Integer`).
* **Quy ước phân loại nút:** Nút xanh lá là **Kiểu dữ liệu / Điểm gọi đệ quy**; nút xanh dương là **Lược đồ mã hóa**; nút xám nhạt là **Thành phần lá kết thúc** không gọi đệ quy tiếp (`Roaring Bitmap`, `FSST`, `Uncompressed`).

#### 4. Cách thức sinh viên tái tạo hình
* **Công cụ thực hiện:** Lập trình Python 3 sử dụng thư viện **`matplotlib`** (`matplotlib.patches.FancyBboxPatch` và `annotate`).
* **Quy trình tái tạo:**
  1. Đối soát toàn bộ các nhánh, nhãn cạnh (`bitmap`, `exceptions`, `length`, `value`, `codes`, `string pool`, `lengths`, `strings`, `values`) và hướng mũi tên từ Figure 3 trang `118:7` (đặc biệt xác minh chính xác kết nối trực tiếp của `SIMD-FastBP128` tới gốc `Integer`).
  2. Xây dựng hàm vẽ khối bo góc (`draw_box`), mũi tên có nhãn nền trắng (`draw_arrow`) và nhánh phân cấp vuông góc (`draw_ortho_branch`).
  3. Phân tách 3 nhóm kiểu dữ liệu vào 3 khung viền nét đứt rõ ràng, bổ sung hộp chú giải (*Legend*) bên dưới giải thích quy ước màu sắc và thông số mặc định (`độ sâu tối đa = 3`, `lấy mẫu 10×64`).
  4. Xuất đồng thời ảnh `PNG 300 DPI` và tệp vector `PDF`.

#### 5. Ý nghĩa của kết quả được thể hiện
* Sơ đồ cho thấy **tính mô-đun và khả năng cộng hưởng** của BtrBlocks: thay vì tìm một thuật toán "vạn năng" duy nhất (thường rất chậm như Zstd/Bzip2), BtrBlocks biến đổi các kiểu dữ liệu phức tạp (`Double`, `String`) thành các mảng số nguyên đơn giản hơn (`codes`, `lengths`, `values` của Pseudodecimal) để tiếp tục tận dụng sức mạnh của các bộ nén số nguyên siêu nhanh như `SIMD-FastPFOR`, `SIMD-FastBP128` hoặc `RLE`.
* Khi gặp dữ liệu đã bão hòa hoặc đạt giới hạn đệ quy 3 tầng, luồng dữ liệu tự động dừng an toàn tại các lá kết thúc.

#### 6. Kết luận khoa học rút ra từ hình
* Thiết kế cây quyết định đệ quy giúp không gian tổ hợp các chuỗi nén (*cascades*) vừa đủ phong phú để thích ứng với sự đa dạng của dữ liệu thực tế trong Data Lake, vừa hoàn toàn kiểm soát được độ phức tạp tính toán thông qua giới hạn độ sâu đệ quy (`recur = 3`) và bộ lọc heuristic tại từng nút.
* Giải nén đơn giản là đảo ngược thứ tự các phép biến đổi dọc theo đường đi đã lưu trong header của mỗi block.

#### 7. Những điểm giống và khác giữa hình vẽ lại và hình trong bài báo gốc
* **Điểm giống:** Bảo toàn chính xác 100% cấu trúc 3 cây quyết định (`Double`, `String`, `Integer`), đầy đủ tất cả các nút lược đồ mã hóa, các nhãn cạnh và các điểm đệ quy như Figure 3 gốc.
* **Điểm khác biệt & cải tiến của sinh viên:**
  * **Bổ sung khung phân nhóm và chú giải (Legend):** Hình gốc không có hộp chú giải phân biệt ý nghĩa 3 màu nút; hình vẽ lại bổ sung bảng chú giải tiếng Việt rõ ràng về vai trò từng loại nút cùng tham số đệ quy/lấy mẫu.
  * **Tiêu đề song ngữ và bố cục thoáng hơn:** Bổ sung khung phân vùng từng kiểu dữ liệu và căn chỉnh khoảng cách đều nhau để dễ đọc trên báo cáo học thuật.

---

## 3.2. HÌNH 2: THÔNG LƯỢNG QUÉT S3 VÀ CHI PHÍ SO VỚI PARQUET (FIGURE 1 BÀI BÁO)

### Hình ảnh tái tạo:
![Hình tái tạo Figure 1: Thông lượng quét S3 và Chi phí trên 5 tập dữ liệu Public BI lớn nhất](<../../99 - Đính kèm (Attachments)/BtrBlocks_Hinh2_TaiTao_S3ScanBenchmark.png>)

*(Tệp hình ảnh chất lượng cao lưu tại: `99 - Đính kèm (Attachments)/BtrBlocks_Hinh2_TaiTao_S3ScanBenchmark.png` (300 DPI) và bản vector `BtrBlocks_Hinh2_TaiTao_S3ScanBenchmark.pdf`; mã nguồn dựng hình tại `03 - Phương pháp & Thí nghiệm (Methodology & Experiments)/scripts/ve_btrblocks_hinh2_s3_scan_benchmark.py`)*

---

### Thuyết minh chi tiết 7 nội dung theo yêu cầu:

#### 1. Vị trí hình gốc trong bài báo
* **Hình gốc:** **Figure 1**, xuất hiện tại **Trang 2 (`118:2`)** của bài báo (thuộc Mục 1: *Introduction*), đối soát số liệu định lượng chính xác từ **Table 5 (Trang `118:20`)** và **Mục 6.7 (Trang `118:21`)**.
* **Tiêu đề gốc:** *"Fig. 1. S3 scan cost and throughput (c5n.18xlarge) on the 5 largest Public BI Benchmark datasets."*

#### 2. Mục đích của hình
* Chứng minh trực quan giá trị thực tiễn đầu-cuối (*end-to-end*) của BtrBlocks so với chuẩn công nghiệp Apache Parquet (không nén thêm, nén Snappy và nén Zstd) trên hai trục đánh giá quan trọng nhất của Data Lake đám mây: **tốc độ khai thác băng thông mạng S3** và **hiệu quả chi phí trên mỗi Đô-la**.

#### 3. Các biến số và thông tin được thể hiện
* **Trục hoành (X):** Thông lượng quét S3 tính theo dữ liệu nén $T_c$ (`S3 Scan Throughput [Gbps]`), thang đo từ `0` đến `100+ Gbps`.
* **Trục tung (Y):** Hiệu quả chi phí biểu diễn bằng số lượt quét S3 trên mỗi Đô-la (`S3 Scans per Dollar`, tính bằng $10 / \text{Scan cost (\$)}$ từ Bảng 5).
* **Đường giới hạn phần cứng:** Vạch đứng tại `~91 Gbps` biểu diễn giới hạn thông lượng thực tế khi tải dữ liệu không nén từ S3 trên máy ảo AWS `c5n.18xlarge` (`100 Gbps` network).
* **Số liệu định lượng chính xác của 4 định dạng (Bảng 5):**
  * **BtrBlocks:** $T_c = 86.2\text{ Gbps}$, $T_u = 174.6\text{ GB/s}$, chi phí `$0.97` $\rightarrow$ **`10.31` lượt/$** *(chuẩn hóa `1.00×`)*.
  * **Parquet + Zstd:** $T_c = 24.8\text{ Gbps}$, $T_u = 78.6\text{ GB/s}$, chi phí `$1.70` $\rightarrow$ **`5.88` lượt/$** *(đắt hơn `1.77×`)*.
  * **Parquet + Snappy:** $T_c = 33.2\text{ Gbps}$, $T_u = 77.6\text{ GB/s}$, chi phí `$1.74` $\rightarrow$ **`5.75` lượt/$** *(đắt hơn `1.84×`)*.
  * **Parquet (không nén thêm):** $T_c = 52.6\text{ Gbps}$, $T_u = 56.1\text{ GB/s}$, chi phí `$2.47` $\rightarrow$ **`4.05` lượt/$** *(đắt hơn `2.61×`)*.

#### 4. Cách thức sinh viên tái tạo hình
* **Công cụ thực hiện:** Viết mã nguồn Python 3 sử dụng thư viện **`matplotlib`**.
* **Quy trình tái tạo:**
  1. Trích xuất trực tiếp các giá trị đo đạc chính xác từ **Bảng 5 (Trang `118:20`)** và ngưỡng `91 Gbps` tại **Mục 6.7 (Trang `118:21`)** của bài báo gốc thay vì ước lượng cảm tính bằng mắt.
  2. Vẽ biểu đồ phân tán (*Scatter Plot*) với 4 hình dạng marker khác nhau (`o`, `D`, `^`, `s`) và bảng màu phân biệt rõ từng định dạng ngay cả khi in đen trắng.
  3. Bổ sung vùng tô xám biểu thị ngưỡng giới hạn S3 (`> 91 Gbps`) và hộp chú thích định lượng chỉ vào điểm tối ưu của BtrBlocks.
  4. Xuất đồng thời ảnh `PNG 300 DPI` và file vector `PDF`.

#### 5. Ý nghĩa của kết quả được thể hiện
* Biểu đồ phơi bày nghịch lý của Parquet trên hạ tầng mạng đám mây tốc độ cao: khi bật nén `Zstd` hoặc `Snappy`, dung lượng file giảm đi (nên rẻ hơn Parquet thuần về phí S3/thời gian tải), nhưng giải nén lại làm **nghẽn CPU**, kéo thông lượng mạng $T_c$ tụt xuống chỉ còn `24.8–33.2 Gbps` (chỉ tận dụng được khoảng 1/4–1/3 đường truyền 100 Gbps).
* Ngược lại, nếu tắt Snappy/Zstd ở Parquet để tăng $T_c$ lên `52.6 Gbps` thì kích thước file phình to khiến chi phí quét tăng vọt (`$2.47`).
* **BtrBlocks phá vỡ sự đánh đổi này**: vừa giữ kích thước nhỏ gọn, vừa giải nén siêu nhanh để đạt $T_c = 86.2\text{ Gbps}$ (tiệm cận ngưỡng giới hạn `91 Gbps` của S3) và đạt hiệu quả chi phí cao nhất (`10.31` lượt/$).

#### 6. Kết luận khoa học rút ra từ hình
* Trong môi trường Data Lake có băng thông mạng cao (`100 Gbps`), **tốc độ giải nén trên dữ liệu nén ($T_c$)** mới là thước đo quyết định chi phí và thời gian quét, thay vì chỉ nhìn vào tốc độ giải nén $T_u$ trong bộ nhớ.
* BtrBlocks đạt điểm tối ưu Pareto (vừa nhanh nhất vừa rẻ nhất): nhanh hơn **2.6×–3.5×** về thông lượng quét $T_c$ và rẻ hơn khoảng **1.8×** so với Parquet+Snappy/Zstd (và rẻ hơn **2.6×** so với Parquet thuần).

#### 7. Những điểm giống và khác giữa hình vẽ lại và hình trong bài báo gốc
* **Điểm giống:** Giữ nguyên hệ trục tọa độ, vị trí tương đối của 4 điểm dữ liệu, ký hiệu marker (tròn, thoi, tam giác, vuông), đường ranh giới giới hạn S3 trên `c5n.18xlarge` và xu hướng so sánh của Figure 1 gốc.
* **Điểm khác biệt & cải tiến của sinh viên:**
  * **Định lượng hóa trực tiếp trên nhãn dữ liệu:** Mỗi điểm dữ liệu được gắn thẻ hiển thị đầy đủ bộ 3 thông số lấy từ Bảng 5 ($T_c$, số lượt/$, và $T_u$), giúp người đọc đối chiếu ngay giá trị chính xác thay vì chỉ thấy tên định dạng như hình gốc.
  * **Bổ sung hộp chú thích kết luận (Callout Box) và vùng xám bão hòa S3:** Làm nổi bật trực quan vùng giới hạn phần cứng (`~91 Gbps`) và tóm tắt tỷ lệ tăng tốc/tiết kiệm chi phí ngay trên biểu đồ.

---

# PHẦN 4: ĐÁNH GIÁ VÀ PHẢN BIỆN BÀI BÁO (CRITICAL REVIEW)

### 1. Đánh giá những đóng góp nổi bật (Major Strengths)
* **Giải quyết đúng nút thắt của kỷ nguyên Cloud Data Lake 100 Gbps:** Nhóm tác giả nhận diện chính xác sự dịch chuyển nút thắt từ băng thông mạng sang tốc độ giải nén CPU, đồng thời chứng minh định lượng bằng thông số $T_c$ (thay vì $T_u$ truyền thống dễ gây ngộ nhận).
* **Thiết kế hướng dữ liệu thực tế thay vì chỉ chạy theo benchmark tổng hợp:** Việc dùng **Public BI Benchmark** (`43` bảng, `2.451` cột, `119.5 GB`) thay cho việc chỉ dựa vào TPC-H giúp phát hiện ra sự thống trị của chuỗi (`71.5%`) và số thực thập phân (`double`) trong thực tế — tiền đề trực tiếp tạo ra **Pseudodecimal Encoding** và sự kết hợp `Dict + FSST`.
* **Thuật toán chọn lược đồ thông minh với chi phí cực thấp:** Chiến lược lấy mẫu phân tầng $10 \times 64$ phần tử (`1%` block) giải quyết bài toán tổ hợp của nén đệ quy đa tầng mà chỉ tốn `1.2%` CPU khi nén nhưng đạt độ sát tối ưu (`chỉ kém 3.3%`).
* **Kiến trúc mở, tách rời siêu dữ liệu (Orthogonal Metadata) & tính khoa học cao:** Tách hoàn toàn block nén khỏi metadata bảng giúp dễ tích hợp vào các hệ sinh thái Lakehouse hiện đại; đồng thời thí nghiệm đối chứng scalar vs. SIMD (Mục 6.8) chứng minh thuyết phục giá trị đến từ thiết kế bậc cao của định dạng chứ không phải chỉ nhờ mẹo tối ưu phần cứng.

---

### 2. Những hạn chế và thách thức kỹ thuật (Limitations & Challenges)
* **Rào cản tương thích hệ sinh thái (Ecosystem Adoption & Migration Cost):** Apache Parquet đang là chuẩn mặc định của toàn bộ hệ sinh thái Big Data & Lakehouse (Spark, Trino, Delta Lake, Apache Iceberg, DuckDB, Snowflake). Chính các tác giả cũng thừa nhận (Mục 6.8) rằng các kỹ thuật của BtrBlocks không thể nhét vừa vào Parquet mà không phá vỡ tương thích ngược (*"Parquet v3"*). Do đó, việc thay thế hoàn toàn Parquet trong sản xuất thực tế đòi hỏi chi phí chuyển đổi dữ liệu và tích hợp driver rất lớn.
* **Tối ưu cho quét toàn khối (Bulk Scan), hạn chế truy cập điểm (Point Lookup) và xử lý trực tiếp trên dữ liệu nén:** Khác với HyPer Data Blocks hay DB2 BLU cho phép lọc điều kiện trực tiếp trên dữ liệu chưa giải nén, BtrBlocks ưu tiên giải nén toàn block (64.000 dòng) thật nhanh ra bộ nhớ rồi mới xử lý. Điều này không tối ưu cho các truy vấn chọn lọc cực hẹp (truy vấn điểm OLTP/HTAP hoặc chỉ cần đọc vài dòng trong block).
* **Giới hạn của Pseudodecimal Encoding trên dữ liệu khoa học / Học máy độ chính xác cao:** Như tác giả chỉ ra ở Bảng 3 (cột tọa độ `NYC/29`), `PDE` hoạt động xuất sắc với số thập phân ngắn (như giá tiền, số liệu tài chính/BI), nhưng kém hiệu quả với số thực có độ chính xác cao hoặc ngẫu nhiên (như tọa độ GPS, vector embedding hoặc trọng số mạng nơ-ron sâu trong ML).
* **Chưa hỗ trợ cập nhật tại chỗ (In-place Updates) và chi phí phụ thuộc vào bộ lệnh AVX2:** Block nén của BtrBlocks là bất biến (*immutable*), phù hợp ghi-một-lần đọc-nhiều-lần. Ngoài ra, hiệu năng giải nén đỉnh cao phụ thuộc đáng kể vào tập lệnh AVX2/x86; việc triển khai trên các kiến trúc CPU khác (như ARM Graviton ngày càng phổ biến trên AWS) cần được viết lại và kiểm chứng riêng.
* **Thiếu thực nghiệm đầu-cuối trong một Query Engine thực thụ:** Thử nghiệm S3 ở Mục 6.7 mới dừng ở tầng đọc và giải nén bộ nhớ (*S3 scan + decompression*) bằng C++ thuần, chưa đo trên một SQL/OLAP engine hoàn chỉnh (như DuckDB, Velox hay Spark/Photon) có tính cả chi phí giải mã truy vấn, join và tổng hợp.

---

### 3. Ý nghĩa học thuật và tiềm năng phát triển tương lai (Academic Impact & Future Directions)
* **Ý nghĩa học thuật:** *BtrBlocks* là một trong những công trình khơi mào làn sóng nghiên cứu định dạng tệp cột thế hệ hậu-Parquet (cùng thời kỳ với *Nimble* của Meta hay *Lance*, *Vortex* cho dữ liệu AI/ML). Các ý tưởng về tách rời metadata, nén đệ quy và giải nén ưu tiên băng thông mạng đã đặt lại tiêu chuẩn thiết kế cho lưu trữ Data Lake.
* **Tiềm năng mở rộng:**
  1. **Tích hợp vào tầng bảng ACID (như Delta Lake / Apache Iceberg):** Thay thế tệp Parquet bên dưới bảng Delta Lake bằng BtrBlocks để tận dụng khả năng tách rời metadata sẵn có của `_delta_log`, giúp tránh thao tác 3 lượt GET footer của Parquet và tăng tốc độ đọc S3 lên mức tối đa.
  2. **Mở rộng cho dữ liệu Vector/Tensor trong Học máy:** Nghiên cứu bổ sung các lược đồ nén chuyên biệt cho mảng số thực độ chính xác thấp (`FP16`, `BF16`, quantized vectors) vào pool của BtrBlocks để phục vụ trực tiếp bài toán AI/ML quy mô lớn.
  3. **Hỗ trợ lọc sớm (Predicate Pushdown) trên dữ liệu nén:** Kết hợp cơ chế dictionary/RLE có sẵn với đánh giá biểu thức SIMD trực tiếp trước khi giải nén hoàn toàn các cột không cần thiết.

---

# PHẦN 5: DANH MỤC TÀI LIỆU THAM KHẢO (References)

1. **M. Kuschewski, D. Sauerwein, A. Alhomssi, and V. Leis**, *"BtrBlocks: Efficient Columnar Compression for Data Lakes,"* *Proceedings of the ACM on Management of Data (PACMMOD)*, vol. 1, no. 2, Art. 118, pp. 118:1–118:26, Jun. 2023. DOI: `10.1145/3589263`.
2. **D. Abadi, P. A. Boncz, S. Harizopoulos, S. Idreos, and S. Madden**, *"The Design and Implementation of Modern Column-Oriented Database Systems,"* *Foundations and Trends in Databases*, vol. 5, no. 3, pp. 197–280, 2013.
3. **P. A. Boncz, T. Neumann, and V. Leis**, *"FSST: Fast Random Access String Compression,"* *Proceedings of the VLDB Endowment (PVLDB)*, vol. 13, no. 11, pp. 2649–2661, 2020.
4. **D. Lemire and L. Boytsov**, *"Decoding billions of integers per second through vectorization,"* *Software: Practice and Experience*, vol. 45, no. 1, pp. 1–29, 2015 *(arXiv:1209.2137)*.
5. **D. Lemire, G. Ssi Yan Kai, and O. Kaser**, *"Consistently faster and smaller compressed bitmaps with Roaring,"* *Software: Practice and Experience*, vol. 46, no. 11, pp. 1547–1569, 2016.
6. **P. Damme, A. Ungethüm, J. Hildebrandt, D. Habich, and W. Lehner**, *"From a Comprehensive Experimental Survey to a Cost-based Selection Strategy for Lightweight Integer Compression Algorithms,"* *ACM Transactions on Database Systems (TODS)*, vol. 44, no. 3, Art. 9, pp. 9:1–9:46, 2019.
7. **M. Armbrust, T. Das, L. Sun, B. Yavuz, S. Zhu, M. Murthy, et al.**, *"Delta Lake: High-Performance ACID Table Storage over Cloud Object Stores,"* *Proceedings of the VLDB Endowment (PVLDB)*, vol. 13, no. 12, pp. 3411–3424, Aug. 2020. DOI: `10.14778/3415478.3415560`.
