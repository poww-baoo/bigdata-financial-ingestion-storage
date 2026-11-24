---
title: "Kế Hoạch Bài Tập Cuối Kỳ - Đề Tài C (Nhóm 4 Thành Viên)"
course: "Phương pháp nghiên cứu khoa học trong Công nghệ thông tin"
type: "Final Group Project Plan"
status: "Planning"
created: 2026-11-24
tags:
  - final-project
  - data-lakehouse
  - mlops
  - feature-store
  - team-plan
---

# KẾ HOẠCH NGHIÊN CỨU CUỐI KỲ (NHÓM 4 THÀNH VIÊN)

## 1. Thông tin Đề tài Tổng thể (Đề tài C)

- **Tên đề tài (Tiếng Việt):** *Hạ tầng quản trị dữ liệu hiện đại cho Học máy quy mô lớn: Liên kết Kiến trúc Data Lakehouse, Tối ưu hóa Lưu trữ Cột, Thực thi Vector hóa và Feature Store*
- **Tên đề tài (Tiếng Anh):** *Modern Data Management Infrastructure for Large-Scale Machine Learning: Bridging Open Columnar Storage, Data Lakehouse, Vectorized Query Execution, and Feature Stores*
- **Mục tiêu cốt lõi:** Hệ thống hóa, phân tích đối chiếu và đề xuất kiến trúc tích hợp 4 tầng từ 4 công trình đỉnh cao (**PVLDB / ACM SIGMOD — Scopus Q1, CORE A\***), chỉ ra chuỗi tối ưu hóa từ định dạng tệp thô trên Cloud Object Storage lên đến đường ống đặc trưng (Feature Pipeline) cho bài toán AI/ML.

---

## 2. Mạch Liên Kết 4 Tầng Kiến Trúc (Research Storyline)

Bài báo giữa kỳ **Delta Lake (PVLDB 2020)** đóng vai trò **trục trung tâm (Core Anchor)**, liên kết xuyên suốt xuống tầng lưu trữ vật lý bên dưới và mở rộng lên tầng tính toán & học máy bên trên:

```text
┌────────────────────────────────────────────────────────────────────────────┐
│  TẦNG 4 [TV4 - Long] — ML Feature Store & Pipeline Optimization            │
│  Optimizing Data Pipelines for ML in Feature Stores (PVLDB 2023, MS)       │
│  ► Giải quyết: Tái sử dụng feature, tránh tính toán lặp khi train/serve ML │
└────────────────────────────────────▲───────────────────────────────────────┘
                                     │ Truy vấn & biến đổi dữ liệu tốc độ cao
┌────────────────────────────────────┴───────────────────────────────────────┐
│  TẦNG 3 [TV3 - Bảo] — Vectorized Query Execution Engine                    │
│  Photon: A Fast Query Engine for Lakehouse Systems (SIGMOD 2022, DBX)      │
│  ► Giải quyết: Nút thắt CPU/JVM khi chạy SQL & ETL phức tạp trên Lakehouse │
└────────────────────────────────────▲───────────────────────────────────────┘
                                     │ Đọc/Ghi bảng ACID, Time Travel, Skipping
┌────────────────────────────────────┴───────────────────────────────────────┐
│  TẦNG 2 [TV1 - Sang (BÀI GỐC)] — ACID Table Storage Layer (Trung tâm)      │
│  Delta Lake: High-Performance ACID Table Storage (PVLDB 2020, DBX)         │
│  ► Giải quyết: ACID, Serverless Metadata, Z-Order trên Cloud Object Store  │
└────────────────────────────────────▲───────────────────────────────────────┘
                                     │ Lưu trữ & giải nén tệp cột tốc độ cao
┌────────────────────────────────────┴───────────────────────────────────────┐
│  TẦNG 1 [TV2 - Cường] — Open Columnar File Format & Compression            │
│  BtrBlocks: Efficient Columnar Compression for Data Lakes (SIGMOD 2023)    │
│  ► Giải quyết: Điểm nghẽn tốc độ giải nén & tỷ lệ nén của Parquet truyền   │
│    thống trong môi trường Data Lake băng thông mạng cao                    │
└────────────────────────────────────▲───────────────────────────────────────┘
                                     │
                 [Cloud Object Storage: AWS S3 / Azure Blob / GCS / MinIO]
```

### Sợi dây logic giữa 4 bài báo (Dùng cho phần Đặt vấn đề & Tổng quan):
1. **Nút thắt 1 (Storage → Table):** Delta Lake (2020) dựa vào tệp **Parquet** để đạt ACID trên Object Store, nhưng Parquet thiết kế từ hơn 10 năm trước nên giải nén chậm và kém tối ưu cho CPU hiện đại → **BtrBlocks (2023)** tối ưu hóa ngay tầng tệp cột bên dưới.
2. **Nút thắt 2 (Table → Compute):** Khi dữ liệu bảng đã có ACID và Data Skipping nhờ Delta Lake, nút thắt dịch chuyển sang **CPU & JVM overhead** của Spark → **Photon (2022)** giải quyết bằng engine C++ vector hóa (SIMD).
3. **Nút thắt 3 (Compute → AI/ML):** Dù Lakehouse đã phục vụ tốt BI/SQL, các đường ống chuẩn bị đặc trưng cho Học máy (ML Feature Engineering) vẫn bị tính toán trùng lặp và khó đồng bộ giữa training/serving → **ML Feature Store Pipelines (2023)** hoàn thiện mắt xích cuối đưa dữ liệu Lakehouse vào AI/ML.

---

## 3. Danh mục 04 Bài Báo Chính (100% Scopus Q1 / WoS / CORE A*)

| STT | Thành viên | Tên bài báo | Tác giả chính & Tổ chức | Hội nghị / Tạp chí | DOI |
| :-: | :--- | :--- | :--- | :--- | :--- |
| **1** | **TV1 — Sang** *(Nhóm trưởng — Võ Huỳnh Minh Sang)* | *Delta Lake: High-Performance ACID Table Storage over Cloud Object Stores* | M. Armbrust, T. Das, ..., M. Zaharia *(Databricks, UC Berkeley, Stanford, CWI)* | **PVLDB**, Vol. 13, No. 12 (2020) | `10.14778/3415478.3415560` |
| **2** | **TV2 — Cường** | *BtrBlocks: Efficient Columnar Compression for Data Lakes* | M. Kuschewski, D. Sauerwein, A. Alhomssi, V. Leis *(TU Munich / FAU)* | **ACM SIGMOD 2023** *(PACMMOD Vol. 1, Iss. 2)* | `10.1145/3589263` |
| **3** | **TV3 — Bảo** | *Photon: A Fast Query Engine for Lakehouse Systems* | A. Behm, S. Palkar, ..., R. Xin, M. Zaharia *(Databricks, UC Berkeley)* | **ACM SIGMOD 2022** *(Best Industry Paper Award)* | `10.1145/3514221.3526054` |
| **4** | **TV4 — Long** | *Optimizing Data Pipelines for Machine Learning in Feature Stores* | R. Liu, K. Park, F. Psallidas, ..., J. Camacho-Rodríguez *(Microsoft Gray Systems Lab)* | **PVLDB**, Vol. 16, No. 13 (2023) | `10.14778/3625054.3625060` |

---

## 4. Phân Công Công Việc Chi Tiết Cho 4 Thành Viên

### Nguyên tắc phân công
- **Phần cá nhân (60% khối lượng):** Mỗi thành viên chịu trách nhiệm phân tích sâu **01 bài báo lõi** theo chuẩn giữa kỳ (Minh chứng Scopus/WoS/SJR, Phân tích IMRAD, Tái tạo hình minh họa, Phản biện điểm mạnh/hạn chế).
- **Phần liên kết & tổng hợp chung (40% khối lượng):** Mỗi thành viên phụ trách thêm **01 hạng mục tích hợp chung** để đảm bảo báo cáo là một chỉnh thể thống nhất, không bị ghép cơ học.

### Bảng phân công cụ thể

| Thành viên | Bài báo phụ trách (Phần riêng) | Vai trò & Nhiệm vụ chung (Phần tích hợp) | Sản phẩm bàn giao (Deliverables) |
| :--- | :--- | :--- | :--- |
| **TV1 — Sang** *(Nhóm trưởng)* | **Delta Lake** *(PVLDB 2020)* — Đã hoàn thành bản giữa kỳ, tinh gọn & nâng cấp thành chương trung tâm. | - **Kiến trúc sư nội dung & Điều phối:** Viết Phần Mở đầu, Bối cảnh chung & Câu hỏi nghiên cứu (RQ) của cả đề tài.<br>- Thiết kế **Sơ đồ Kiến trúc Tích hợp 4 Tầng** (Hình tổng hợp mới).<br>- Biên tập, chuẩn hóa trích dẫn (IEEE/APA) và kiểm tra tính nhất quán toàn báo cáo. | - Chương Delta Lake (đã chuẩn hóa).<br>- Mục 1 (Giới thiệu & Đặt vấn đề chung).<br>- Sơ đồ tổng thể 4 tầng (PNG/PDF 300 DPI).<br>- Bản báo cáo tổng hợp hoàn chỉnh (Word/PDF). |
| **TV2 — Cường** | **BtrBlocks** *(SIGMOD 2023)* — Phân tích sâu định dạng tệp cột, thuật toán nén đệ quy & giải nén tốc độ cao. | - **Phụ trách Trục Dữ liệu & Lưu trữ:** Lập **Bảng Ma trận So sánh (Comparative Matrix)** đối chiếu cả 4 bài (Vấn đề, Kiến trúc, Benchmark, Chỉ số đánh giá, Hạn chế).<br>- Phân tích rõ cầu nối **BtrBlocks ↔ Delta Lake** (nếu thay Parquet bằng BtrBlocks trong Delta Lake thì cải thiện gì?). | - Chương phân tích BtrBlocks + minh chứng Scopus/WoS.<br>- 02 hình vẽ lại (kiến trúc nén & benchmark tốc độ giải nén vs Parquet).<br>- Bảng Ma trận So sánh 4 bài báo. |
| **TV3 — Bảo** | **Photon** *(SIGMOD 2022)* — Phân tích sâu Vectorized Execution (C++/SIMD), tích hợp Spark & TPC-DS 100TB. | - **Phụ trách Trục Hiệu năng & Trực quan hóa:** Xây dựng **01 Biểu đồ Tổng hợp / Đề xuất Mới cấp nhóm** (so sánh hệ số tăng tốc/hiệu quả xuyên suốt các tầng: Compression → Table Skipping → Vectorized Compute → Feature Reuse).<br>- Phân tích cầu nối **Delta Lake ↔ Photon**. | - Chương phân tích Photon + minh chứng Scopus/WoS.<br>- 02 hình vẽ lại (kiến trúc Photon & hiệu năng TPC-DS).<br>- 01 Biểu đồ tổng hợp mới của cả nhóm (Python `matplotlib`). |
| **TV4 — Long** | **ML Feature Store Pipelines** *(PVLDB 2023)* — Phân tích sâu Feature Store, tối ưu hóa đường ống ML & tái sử dụng tính toán. | - **Phụ trách Tổng hợp Khoảng trống & Hướng phát triển:** Viết chương **Thảo luận, Phản biện chéo & Khoảng trống nghiên cứu chung (Synthesized Research Gaps)** + **Đề xuất hướng nghiên cứu mới** (End-to-End AI-Ready Lakehouse).<br>- Chuẩn bị **Slide thuyết trình & Bộ câu hỏi Q&A vấn đáp** cho nhóm. | - Chương phân tích Feature Store + minh chứng Scopus/WoS.<br>- 02 hình vẽ lại (kiến trúc tối ưu pipeline & kết quả tiết kiệm thời gian/chi phí ML).<br>- Chương Kết luận & Hướng nghiên cứu tương lai + Slide thuyết trình. |

---

## 5. Khung Cấu Trúc Báo Cáo Cuối Kỳ Đề Xuất

1. **Chương 1: Mở đầu & Đặt vấn đề** *(Sang)* — Xu hướng hội tụ Data Lakehouse và MLOps; Mục tiêu & Câu hỏi nghiên cứu chung (RQ1–RQ3).
2. **Chương 2: Tổng quan 4 Công trình Nghiên cứu Nền tảng**
   - 2.1. Tầng Định dạng Cột: *BtrBlocks (SIGMOD 2023)* *(Cường)*
   - 2.2. Tầng Bảng Giao dịch ACID: *Delta Lake (PVLDB 2020)* *(Sang)*
   - 2.3. Tầng Thực thi Truy vấn Vector hóa: *Photon (SIGMOD 2022)* *(Bảo)*
   - 2.4. Tầng Đường ống Đặc trưng Học máy: *ML Feature Stores (PVLDB 2023)* *(Long)*
3. **Chương 3: Phân tích Liên kết, So sánh Đối chiếu & Kiến trúc Tích hợp**
   - 3.1. Kiến trúc tích hợp 4 tầng đề xuất *(Sang)*
   - 3.2. Ma trận so sánh đa chiều 4 công trình *(Cường)*
   - 3.3. Tổng hợp định lượng & Biểu đồ phân tích mới *(Bảo)*
4. **Chương 4: Phản biện, Khoảng trống Nghiên cứu & Hướng Phát triển** *(Long chủ trì, cả nhóm góp ý)*
   - Đánh đổi (Trade-offs) giữa các tầng: Nén sâu vs. Giải nén nhanh; ACID chặt vs. Độ trễ thấp; Tính toán trước Feature vs. Chi phí lưu trữ.
   - Đề xuất hướng nghiên cứu mở: *Tự động tối ưu hóa xuyên tầng (Cross-layer Optimization) cho Lakehouse phục vụ AI/LLM*.
5. **Chương 5: Kết luận & Tài liệu tham khảo** *(Sang chuẩn hóa chuẩn IEEE)*

---

## 6. Lộ Trình Thực Hiện Theo Tuần (4 Tuần)

| Giai đoạn | Mục tiêu chính | Công việc từng thành viên | Cột mốc kiểm tra (Milestone) |
| :--- | :--- | :--- | :--- |
| **Tuần 1:** Đọc sâu & Tải tài liệu | Chốt đề cương, tải PDF 3 bài mới, kiểm tra Scopus/WoS/SJR | - **Sang:** Chốt template chung, gửi mẫu báo cáo Delta Lake làm chuẩn.<br>- **Cường, Bảo, Long:** Tải bài PDF, đọc theo kỹ thuật 3-pass, trích xuất thông tin Scopus/WoS & chọn 2 hình sẽ vẽ lại. | Họp nhóm cuối tuần 1: Duyệt danh sách hình vẽ & dàn ý chi tiết. |
| **Tuần 2:** Phân tích & Vẽ hình cá nhân | Hoàn thiện bản nháp 4 chương cá nhân & toàn bộ hình vẽ lại | - **Sang:** Rút gọn & chuẩn hóa chương Delta Lake + viết Chương 1.<br>- **Cường, Bảo, Long:** Viết phân tích IMRAD + code vẽ 2 hình minh họa bằng Python/Graphviz (xuất 300 DPI). | Nộp bản nháp phần riêng vào thư mục chung; review chéo lẫn nhau. |
| **Tuần 3:** Tích hợp & Tổng hợp chéo | Tạo "chất keo" liên kết 4 bài thành 1 công trình thống nhất | - **Sang:** Vẽ Sơ đồ tích hợp 4 tầng.<br>- **Cường:** Hoàn thiện Ma trận so sánh 4 bài.<br>- **Bảo:** Code biểu đồ tổng hợp đề xuất mới.<br>- **Long:** Viết Chương 4 (Phản biện & Research Gaps). | Bản ghép hoàn chỉnh (Draft v1) có đủ hình, bảng, trích dẫn. |
| **Tuần 4:** Hoàn thiện, Slide & Tập vấn đáp | Chống đạo văn, trau chuốt định dạng, tập thuyết trình | - **Sang:** Format báo cáo cuối (Word/PDF), kiểm tra chuẩn IEEE.<br>- **Long:** Hoàn thiện Slide.<br>- **Cả 4 TV (Sang, Cường, Bảo, Long):** Đọc hiểu phần của nhau, tập hỏi-đáp phản biện chéo. | Nộp báo cáo Final & sẵn sàng bảo vệ. |

---

## 7. Gợi ý Câu hỏi Nghiên cứu Chung (Cho Chương 1)
- **RQ1:** Các điểm nghẽn hiệu năng dịch chuyển như thế nào qua 4 tầng của một hệ thống quản trị dữ liệu hiện đại (từ nén tệp cột → giao dịch bảng ACID → thực thi truy vấn → đường ống đặc trưng ML)?
- **RQ2:** Làm thế nào các kỹ thuật trong *BtrBlocks*, *Delta Lake*, *Photon* và *ML Feature Store* bổ trợ cho nhau để giải quyết bài toán cung cấp dữ liệu quy mô lớn cho Học máy?
- **RQ3:** Những sự đánh đổi (trade-offs) và khoảng trống nghiên cứu nào vẫn còn tồn tại khi tích hợp đồng thời cả 4 tầng trên hạ tầng Cloud Object Storage?
