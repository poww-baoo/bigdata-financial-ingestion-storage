# BÁO CÁO NGHIÊN CỨU KHOA HỌC CUỐI KỲ — ĐỀ TÀI C

**Cơ sở đào tạo:** Trường Đại học Sài Gòn – Khoa Công nghệ Thông tin  
**Học phần:** Phương pháp Nghiên cứu Khoa học trong Công nghệ Thông tin  
**Tên đề tài (Tiếng Việt):** *Hạ tầng quản trị dữ liệu hiện đại cho Học máy quy mô lớn: Liên kết Kiến trúc Data Lakehouse, Tối ưu hóa Lưu trữ Cột, Thực thi Vector hóa và Feature Store*  
**Tên đề tài (Tiếng Anh):** *Modern Data Management Infrastructure for Large-Scale Machine Learning: Bridging Open Columnar Storage, Data Lakehouse, Vectorized Query Execution, and Feature Stores*  
**Nhóm thực hiện (4 thành viên):**  
- TV1 — Võ Huỳnh Minh Sang *(Nhóm trưởng)*  
- TV2 — Cường  
- TV3 — Bảo  
- TV4 — Long  
**Giảng viên hướng dẫn:** Vũ Ngọc Thanh Sang  

> **Trạng thái tích hợp:** Đã hoàn thiện tích hợp toàn bộ phần đóng góp của **TV4 — Long** (Mục 2.4, Chương 4, 02 hình minh họa 300 DPI và Tài liệu tham khảo IEEE) cùng phần nền **Delta Lake** của **TV1 — Sang** (Mục 2.2). Các mục của TV1 (Chương 1, 3.1, 5), TV2 — Cường (Mục 2.1, 3.2) và TV3 — Bảo (Mục 2.3, 3.3) đang giữ khung chờ ghép bản thảo.

---

# CHƯƠNG 1: MỞ ĐẦU VÀ ĐẶT VẤN ĐỀ *(Chủ trì: TV1 — Sang)*

## 1.1. Bối cảnh và Xu hướng hội tụ Data Lakehouse – MLOps
Trong kỷ nguyên dữ liệu lớn và Học máy quy mô doanh nghiệp, dữ liệu thô ngày càng được lưu trữ tập trung trên Cloud Object Storage (AWS S3, Azure Blob Storage, GCS, MinIO) nhằm tận dụng chi phí thấp và khả năng mở rộng tách biệt giữa lưu trữ và tính toán. Tuy nhiên, để đưa dữ liệu thô từ tầng lưu trữ vật lý đi qua các lớp quản trị bảng, xử lý truy vấn và tạo đặc trưng phục vụ huấn luyện mô hình ML/AI, hệ thống thường đối mặt với chuỗi dịch chuyển điểm nghẽn hiệu năng qua bốn tầng kiến trúc: Định dạng tệp cột $\rightarrow$ Tầng bảng giao dịch ACID $\rightarrow$ Động cơ thực thi truy vấn $\rightarrow$ Đường ống đặc trưng Học máy.

## 1.2. Mục tiêu và Câu hỏi Nghiên cứu chung (RQ1 – RQ3)
- **RQ1:** Các điểm nghẽn hiệu năng dịch chuyển như thế nào qua 4 tầng của một hệ thống quản trị dữ liệu hiện đại (từ nén tệp cột $\rightarrow$ giao dịch bảng ACID $\rightarrow$ thực thi truy vấn $\rightarrow$ đường ống đặc trưng ML)?
- **RQ2:** Làm thế nào các kỹ thuật trong *BtrBlocks*, *Delta Lake*, *Photon* và *ML Feature Store (FeathrPO)* bổ trợ cho nhau để giải quyết bài toán cung cấp dữ liệu quy mô lớn cho Học máy?
- **RQ3:** Những sự đánh đổi (*trade-offs*) và khoảng trống nghiên cứu nào vẫn còn tồn tại khi tích hợp đồng thời cả 4 tầng trên hạ tầng Cloud Object Storage?

*(Phần diễn giải chi tiết Chương 1: Chờ TV1 — Sang bổ sung bản thảo cuối kỳ.)*

---

# CHƯƠNG 2: TỔNG QUAN 4 CÔNG TRÌNH NGHIÊN CỨU NỀN TẢNG

## 2.1. Tầng Định dạng Cột: BtrBlocks (ACM SIGMOD 2023) *(TV2 — Cường)*
- **Bài báo lõi:** M. Kuschewski et al., *"BtrBlocks: Efficient Columnar Compression for Data Lakes,"* ACM SIGMOD 2023, DOI: `10.1145/3589263`.
- *(Chờ TV2 — Cường bổ sung nội dung phân tích IMRAD, minh chứng Scopus/WoS và 02 hình vẽ lại.)*

## 2.2. Tầng Bảng Giao dịch ACID: Delta Lake (PVLDB 2020) *(TV1 — Sang — Bài gốc trung tâm)*
Công trình *"Delta Lake: High-Performance ACID Table Storage over Cloud Object Stores"* (M. Armbrust et al., PVLDB Vol. 13, No. 12, pp. 3411–3424, Aug. 2020, DOI: `10.14778/3415478.3415560`, Scopus Source ID `21100199855`, Q1, CORE A*) đóng vai trò trục trung tâm của đề tài. Delta Lake giải quyết vấn đề thiếu tính nguyên tử đa đối tượng, không có cô lập giao dịch và chi phí lệnh `LIST` siêu dữ liệu lớn trên Cloud Object Storage bằng cách lưu trữ nhật ký giao dịch `_delta_log` dạng JSON/Parquet ngay trên chính Object Store, kết hợp kiểm soát đồng thời lạc quan (OCC), Data Skipping (min/max stats) và sắp xếp không gian đa chiều Z-Order. Trên chuẩn TPC-DS 1 TB (cụm AWS `i3.2xlarge`), Delta Lake đạt thời gian thực thi **0,93 giờ** (tiết kiệm **75,3%** thời gian và nhanh hơn **4,04×** so với Presto 3,76 giờ).

![[Hinh1_TaiTao_KienTruc_Pipeline.png]]
![[Hinh2_TaiTao_TPCDS_PowerTest.png]]

*(Ghi chú: Toàn văn phân tích chi tiết Delta Lake đã hoàn thiện tại `Báo cáo Giữa kỳ - Delta Lake.md` và `Baocao.docx`, TV1 — Sang sẽ tinh gọn trực tiếp khi chốt bản in cuối.)*

## 2.3. Tầng Thực thi Truy vấn Vector hóa: Photon (ACM SIGMOD 2022) *(TV3 — Bảo)*
- **Bài báo lõi:** A. Behm et al., *"Photon: A Fast Query Engine for Lakehouse Systems,"* ACM SIGMOD 2022 (Best Industry Paper Award), DOI: `10.1145/3514221.3526054`.
- *(Chờ TV3 — Bảo bổ sung nội dung phân tích IMRAD, minh chứng Scopus/WoS và 02 hình vẽ lại.)*

## 2.4. Tầng Đường ống Đặc trưng Học máy: ML Feature Stores — FeathrPO (PVLDB 2023) *(TV4 — Long — ĐÃ HOÀN THÀNH)*

### 2.4.1. Thông tin và Nguồn Bài báo (Chuẩn Scopus / WoS / CORE A\*)
Bài báo được lựa chọn là *"Optimizing Data Pipelines for Machine Learning in Feature Stores"* (tạm dịch: *Tối ưu hóa Đường ống Dữ liệu cho Học máy trong các Kho Đặc trưng*), công bố bởi nhóm **10 tác giả** gồm Rui Liu (*University of Chicago*), Kwanghyun Park (*Yonsei University*), Fotis Psallidas, Xiaoyong Zhu, Rathijit Sen, Matteo Interlandi, Yuanyuan Tian, Jesús Camacho-Rodríguez (*Microsoft*), Jinghui Mo (*LinkedIn*) và Konstantinos Karanasos (*Meta*). Công trình xuất bản tại *Proceedings of the VLDB Endowment (PVLDB)*, Tập 16, Số 13, trang 4230–4239, tháng 8/2023 (trình bày tại Hội nghị VLDB lần thứ 49, Vancouver, Canada), mã **ISSN `2150-8097`** và **DOI [`10.14778/3625054.3625060`](https://doi.org/10.14778/3625054.3625060)** ([VLDB PDF](https://www.vldb.org/pvldb/vol16/p4230-liu.pdf), [ACM DL](https://dl.acm.org/doi/10.14778/3625054.3625060)).

Về minh chứng chỉ mục học thuật, ấn phẩm PVLDB được Elsevier Scopus lập chỉ mục liên tục từ năm 2008 đến nay với **Scopus Source ID `21100199855`** ([Scopus Source](https://www.scopus.com/sourceid/21100199855)), CiteScore dao động **7,5–8,2** và h-index **> 200**; trên hệ thống Clarivate Web of Science, nguồn được ghi nhận tại *Master Journal List* qua ISSN `2150-8097` (thuộc *WoS Core Collection* — CPCI-S/ESCI); xếp hạng **CORE A\*** và đạt **Q1** trên ScimagoJR ([SJR Profile](https://www.scimagojr.com/journalsearch.php?q=21100199855&tip=sid)) ở các lĩnh vực *Information Systems*, *Software* và *Hardware and Architecture*.

### 2.4.2. Phân tích Nội dung Nghiên cứu theo cấu trúc IMRAD
Trong quy trình MLOps, **Feature Store** (như Feathr, Feast, Tecton) đóng vai trò như một **“DBMS-for-ML”** giúp định nghĩa, lưu trữ và cung cấp đặc trưng đồng nhất giữa huấn luyện và suy luận. Nút thắt cốt lõi của các đường ống tạo tập huấn luyện lịch sử là phép ghép theo thời gian chính xác **Point-in-Time (PIT) Join** ($t_{\text{feat}} \le t_{\text{obs}}$) nhằm ngăn chặn tuyệt đối lỗi **rò rỉ dữ liệu (*Data Leakage*)**. Tuy nhiên, các Feature Store hiện có triển khai phép PIT Join 3 chiều một cách “ngây thơ” trên Apache Spark, gây ra lượng dữ liệu *shuffle* khổng lồ, tính toán lặp lại giữa các vòng thử nghiệm và chưa tận dụng các kỹ thuật tối ưu truy vấn kinh điển của CSDL quan hệ.

Nhóm tác giả xây dựng **FeathrPO** tích hợp vào **Feathr** để giải quyết hai câu hỏi trọng tâm về hiệu quả tái sử dụng logic và tăng tốc đầu-cuối trên đa nền tảng PIT Join. Thực nghiệm được tiến hành trên bốn bộ dữ liệu lớn gồm **TPCxAI-UC7 (SF10)** ($L$: 789.225 dòng / 27 MB; $F$: 27.987.766 dòng / 1,5 GB; $A$: 358.818 dòng / 39 MB), **TPCxAI-UC10 (SF10)** ($L$: 37.696 dòng / 725 KB; $F$: 55.975.921 dòng / 2,1 GB; $A$: 358.818 dòng / 39 MB), **Favorita (Kaggle)** ($L$: 379 dòng / 7,3 KB; $F$: 125.497.041 dòng / 3,9 GB; $A$: 55 dòng / 1,4 KB) và **eCommerce (Kaggle)** ($L$: 44.415 dòng / 941 KB; $F$: 104.335.510 dòng / 3,4 GB; $A$: 104.335.510 dòng / 4,1 GB), chạy trên cụm đám mây **Azure Synapse** (Feathr v0.7.2, Spark v3.1, 1 driver + 4 workers 8 vCores/64 GB RAM) và cụm cục bộ Ubuntu 20.04 (10 cores, 32 GB RAM, Spark v3.2).

Giải pháp kỹ thuật của FeathrPO kết hợp ba cơ chế chính: *(1)* **Mô hình chi phí nhận biết bố cục & KLL Sketches (§4)** tối thiểu hóa lượng dữ liệu quét với độ chính xác ước lượng phân vị đạt **96,84% – 99,73%** (vượt trội mức **89,61% – 92,19%** của Spark mặc định tại Table 2); *(2)* **Tái sử dụng tính toán & Rút gọn Semijoin (§5)** chỉ tính phần chênh lệch (*delta*) trên tập đã vật chất hóa kèm bộ lọc `[min_ts, max_ts]` để cắt giảm *shuffle* và phòng tránh suy thoái khi độ chọn lọc cao (80%–100%); và *(3)* **Chọn bố cục phân vùng thời gian tự động bằng Quy hoạch Nguyên Nhị phân BIP (§6)** giải bằng Google OR-Tools (*glop solver*) trong **6–7 giây** cho 10.000 truy vấn và 1.000 bảng nguồn. Kết quả cho thấy FeathrPO tăng tốc lên tới **3,00×** trên `TPCxAI-UC10` (Cloud), đạt **1,4× – 2,50×** trên các thuật toán PIT Join khác (*Early-stop Sort Merge*, *Union Merge*) và giữ mức tăng tốc **1,3× – 2,3×** trên các quy mô SF1–SF100.

### 2.4.3. Hai Hình Minh họa Tự Vẽ lại (300 DPI + Vector PDF)
![[Hinh_TV4_1_KienTruc_FeathrPO.png]]
*Hình 2.4.1: Tái tạo Figure 8 (tr. 4235) — Kiến trúc tích hợp không xâm lấn của Data Layout Selector và Reuse-based Optimizer trong Feathr trên Azure.*

![[Hinh_TV4_2_HieuNang_FeathrPO.png]]
*Hình 2.4.2: Tái tạo Figure 12 (tr. 4237) — Hệ số cải thiện hiệu năng của FeathrPO trên 4 tập dữ liệu và 3 cài đặt PIT Join.*

*(Thuyết minh đầy đủ 7 tiêu chí khoa học cho từng hình vẽ và phần phản biện bài báo được lưu đồng bộ từ `Phan_TV4_Long_Feature_Store_va_Chuong4.md`.)*

### 2.4.4. Đánh giá và Phản biện Bài báo
FeathrPO định vị chính xác bài toán PIT Join lặp đi lặp lại trong MLOps và chứng minh hiệu quả thực tế tới **3,00×** trên hệ thống mã nguồn mở Feathr cùng chuẩn công nghiệp TPCx-AI. Tuy nhiên, bài báo vẫn còn ba hạn chế: phụ thuộc vào tầng thực thi Spark (JVM) nên chưa tận dụng định dạng nén giải mã siêu nhanh (BtrBlocks) hay engine C++ vector hóa (Photon); việc chọn đặc trưng để vật chất hóa vẫn phụ thuộc chỉ định thủ công; và chưa mở rộng sang dữ liệu phi cấu trúc hoặc vector embeddings cho LLM/RAG.

---

# CHƯƠNG 3: PHÂN TÍCH LIÊN KẾT, SO SÁNH ĐỐI CHIẾU VÀ KIẾN TRÚC TÍCH HỢP

## 3.1. Kiến trúc Tích hợp 4 Tầng Đề xuất *(Chủ trì: TV1 — Sang)*
*(Chờ TV1 — Sang bổ sung sơ đồ tổng thể 4 tầng và phân tích kết nối.)*

## 3.2. Ma trận So sánh Đa chiều 4 Công trình *(Chủ trì: TV2 — Cường)*
*(Chờ TV2 — Cường bổ sung bảng ma trận đối chiếu và cầu nối BtrBlocks ↔ Delta Lake.)*

## 3.3. Tổng hợp Định lượng và Biểu đồ Phân tích Mới *(Chủ trì: TV3 — Bảo)*
*(Chờ TV3 — Bảo bổ sung biểu đồ tổng hợp xuyên tầng và cầu nối Delta Lake ↔ Photon.)*

---

# CHƯƠNG 4: PHẢN BIỆN, KHOẢNG TRỐNG NGHIÊN CỨU VÀ HƯỚNG PHÁT TRIỂN *(Chủ trì: TV4 — Long — ĐÃ HOÀN THÀNH)*

Chương 4 tổng hợp các phân tích từ cả bốn tầng (**BtrBlocks → Delta Lake → Photon → ML Feature Store**) nhằm trả lời trực tiếp cho Câu hỏi Nghiên cứu **RQ3**.

## 4.1. Phân tích các Sự Đánh Đổi (Trade-offs) Xuyên Suốt 4 Tầng

| Cặp tầng liên kết | Sự đánh đổi (Trade-off) | Phân tích kỹ thuật chuyên sâu |
| :--- | :--- | :--- |
| **Tầng 1 (BtrBlocks) ↔ Tầng 2 (Delta Lake)** | **Tỷ lệ nén tối đa vs. Tốc độ giải nén & Độ phổ cập chuẩn mở** | Delta Lake dựa vào chuẩn Parquet để bảo đảm tương thích đa công cụ nhưng Parquet giải nén chậm trên CPU hiện đại; BtrBlocks giải nén cực nhanh nhưng thay trực tiếp sẽ phá vỡ tính tương thích của hệ sinh thái Parquet. |
| **Tầng 2 (Delta Lake) ↔ Tầng 3 (Photon)** | **Tính nhất quán ACID chặt chẽ vs. Độ trễ ghi/đọc thời gian thực** | Giao thức `_delta_log` và cơ chế OCC bảo đảm ACID và Time Travel nhưng phát sinh chi phí quản lý metadata và nguy cơ xung đột ghi khi có nhiều luồng cập nhật nhỏ liên tục. |
| **Tầng 3 (Photon) ↔ Tầng 4 (Feature Store)** | **Tốc độ Vectorized C++/SIMD vs. Tính linh hoạt của UDF Python/ML** | Photon tăng tốc toán tử SQL chuẩn bằng C++/SIMD, nhưng phép biến đổi đặc trưng ML thường dùng UDF Python/PyTorch nên dễ rơi về luồng chậm hoặc tốn chi phí tuần tự hóa C++ ↔ Python. |
| **Tầng 4 (Feature Store) ↔ Object Store** | **Tính toán sẵn (Pre-computation) vs. Chi phí lưu trữ & Độ tươi dữ liệu** | Vật chất hóa sẵn giúp train/serve nhanh nhưng nhân đôi chi phí lưu trữ và dễ lỗi thời; tính động bằng PIT Join mỗi lần train lại tốn CPU nếu thiếu bộ nhớ đệm xuyên tầng. |

## 4.2. Tổng hợp Khoảng trống Nghiên cứu Chung (Synthesized Research Gaps)
1. **Thiếu bộ tối ưu hóa dựa trên chi phí xuyên tầng (*Lack of Cross-layer Cost-based Optimization*):** Tối ưu hóa hiện bị cắt khúc theo từng tầng (byte/block ở BtrBlocks, metadata/Z-Order ở Delta Lake, vector hóa ở Photon, logic Feature Pipeline ở FeathrPO), chưa có cơ chế truyền ngữ nghĩa từ Feature Store xuống tầng bố cục và giải mã bên dưới.
2. **Điểm nghẽn chuyển đổi dữ liệu giữa Engine C++ và Môi trường ML Python:** Dù Photon loại bỏ JVM overhead, quá trình trao đổi tensor sang PyTorch/TensorFlow/Scikit-learn vẫn tốn chi phí sao chép bộ nhớ nếu thiếu chuẩn Zero-copy (Arrow Flight / DLPack) xuyên suốt.
3. **Thiếu chuẩn đánh giá hiệu năng đầu-cuối thống nhất (*End-to-End Unified Benchmark*):** Các tầng hiện đo bằng benchmark rời rạc (micro-benchmark giải nén, TPC-DS SQL, TPCx-AI PIT Join), thiếu một chuẩn đo xuyên suốt từ byte nén trên Object Store đến khi nạp vào GPU huấn luyện mô hình.

## 4.3. Đề xuất Hướng Nghiên cứu Mới (Future Research Directions)
1. **Tự động Tối ưu hóa Xuyên tầng cho AI-Ready Lakehouse (*Cross-layer Semantic Optimization*):** Truyền gợi ý ngữ nghĩa (*semantic hints*) từ Feature Store (tần suất khóa thực thể, cửa sổ thời gian, TTL) xuống Delta Lake để tự chọn khóa Z-Order/Partitioning và xuống BtrBlocks để chọn chiến lược nén tối ưu theo từng kiểu đặc trưng ML.
2. **Hỗ trợ Nguyên bản Dữ liệu Đa phương thức & Vector Embeddings cho Kỷ nguyên AI/LLM:** Lưu trữ nguyên bản vector embeddings và dữ liệu phi cấu trúc ngay trong bảng ACID của Lakehouse, tích hợp chỉ mục tìm kiếm vector gần đúng (ANN Index) vào engine vector hóa nhằm phục vụ trực tiếp RAG và Fine-tuning LLM.

---

# CHƯƠNG 5: KẾT LUẬN VÀ TÀI LIỆU THAM KHẢO *(Chuẩn hóa: TV1 — Sang)*

*(Phần tổng kết câu trả lời RQ1–RQ3 chờ TV1 — Sang hoàn thiện sau khi ghép đủ Chương 1 và Chương 3.)*

## Tài liệu Tham khảo (Chuẩn IEEE)
1. M. Armbrust et al., "Delta Lake: High-Performance ACID Table Storage over Cloud Object Stores," *Proc. VLDB Endow.*, vol. 13, no. 12, pp. 3411–3424, Aug. 2020, doi: `10.14778/3415478.3415560`.
2. M. Kuschewski, D. Sauerwein, A. Alhomssi, and V. Leis, "BtrBlocks: Efficient Columnar Compression for Data Lakes," *Proc. ACM Manag. Data (SIGMOD)*, vol. 1, no. 2, pp. 1–26, Jun. 2023, doi: `10.1145/3589263`.
3. A. Behm et al., "Photon: A Fast Query Engine for Lakehouse Systems," in *Proc. ACM SIGMOD Int. Conf. Manag. Data*, Jun. 2022, pp. 2326–2339, doi: `10.1145/3514221.3526054`.
4. R. Liu et al., "Optimizing Data Pipelines for Machine Learning in Feature Stores," *Proc. VLDB Endow.*, vol. 16, no. 13, pp. 4230–4239, Aug. 2023, doi: `10.14778/3625054.3625060`.
