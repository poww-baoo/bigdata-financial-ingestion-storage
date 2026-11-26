---
title: "Kế Hoạch Bài Tập Cuối Kỳ - Đề Tài C (Nhóm 4 Thành Viên — 05 Bài Báo)"
course: "Phương pháp nghiên cứu khoa học trong Công nghệ thông tin"
type: "Final Group Project Plan"
status: "In Progress"
created: 2026-11-24
updated: 2026-11-26
tags:
  - final-project
  - data-lakehouse
  - mlops
  - feature-store
  - tf-data
  - team-plan
---

# KẾ HOẠCH NGHIÊN CỨU CUỐI KỲ (NHÓM 4 THÀNH VIÊN — 05 BÀI BÁO)

## 1. Thông tin Đề tài Tổng thể (Đề tài C)

- **Tên đề tài (Tiếng Việt):** *Hạ tầng quản trị dữ liệu hiện đại cho Học máy quy mô lớn: Liên kết Định dạng Lưu trữ Cột, Kiến trúc Data Lakehouse, Thực thi Vector hóa, Feature Store và Đường ống Nạp dữ liệu Huấn luyện*
- **Tên đề tài (Tiếng Anh):** *Modern Data Management Infrastructure for Large-Scale Machine Learning: Bridging Open Columnar Storage, Data Lakehouse, Vectorized Query Execution, Feature Stores, and ML Input Pipelines*
- **Mục tiêu cốt lõi:** Hệ thống hóa, phân tích đối chiếu và đề xuất kiến trúc tích hợp đầu-cuối **5 tầng** từ **05 công trình đỉnh cao (PVLDB / ACM SIGMOD — 100% Scopus Q1, WoS, CORE A\*)**, chỉ ra trọn vẹn chuỗi tối ưu hóa từ định dạng tệp thô trên Cloud Object Storage đến đường ống nạp dữ liệu huấn luyện (*Input Pipeline*) vào GPU/TPU cho bài toán AI/ML.

---

## 2. Mạch Liên Kết 5 Tầng Kiến Trúc (Research Storyline)

Bài báo giữa kỳ **Delta Lake (PVLDB 2020)** đóng vai trò **trục trung tâm (Core Anchor)**, liên kết xuống tầng lưu trữ vật lý bên dưới và mở rộng lên tầng tính toán, kho đặc trưng và nạp dữ liệu huấn luyện bên trên:

```text
┌────────────────────────────────────────────────────────────────────────────┐
│  TẦNG 5 [TV1 - Sang (BÀI BỔ SUNG)] — ML Training Input Pipeline            │
│  tf.data: A Machine Learning Data Processing Framework (PVLDB 2021, Google)│
│  ► Giải quyết: Nghẽn I/O & tiền xử lý khi nạp đặc trưng vào GPU/TPU        │
└────────────────────────────────────▲───────────────────────────────────────┘
                                     │ Nạp tập huấn luyện (AUTOTUNE, Prefetch)
┌────────────────────────────────────┴───────────────────────────────────────┐
│  TẦNG 4 [TV4 - Long] — ML Feature Store & Pipeline Optimization            │
│  Optimizing Data Pipelines for ML in Feature Stores (PVLDB 2023, Microsoft)│
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

### Sợi dây logic giữa 5 bài báo (Dùng cho phần Đặt vấn đề & Tổng quan):
1. **Nút thắt 1 (Storage → Table):** Delta Lake (2020) dựa vào tệp **Parquet** để đạt ACID trên Object Store, nhưng Parquet thiết kế từ hơn 10 năm trước nên giải nén chậm và kém tối ưu cho CPU hiện đại → **BtrBlocks (2023)** tối ưu hóa ngay tầng tệp cột bên dưới.
2. **Nút thắt 2 (Table → Compute):** Khi dữ liệu bảng đã có ACID và Data Skipping nhờ Delta Lake, nút thắt dịch chuyển sang **CPU & JVM overhead** của Spark → **Photon (2022)** giải quyết bằng engine C++ vector hóa (SIMD).
3. **Nút thắt 3 (Compute → Feature Engineering):** Dù Lakehouse phục vụ tốt BI/SQL, các đường ống chuẩn bị đặc trưng cho Học máy (ML Feature Engineering) vẫn bị tính toán trùng lặp và chậm ở phép *Point-in-Time Join* → **ML Feature Store Pipelines / FeathrPO (2023)** tối ưu hóa tái sử dụng và bố cục đặc trưng.
4. **Nút thắt 4 (Feature Store → GPU/TPU Training):** Sau khi đặc trưng được xuất thành tập huấn luyện trên Object Store, khâu đọc/giải mã/tiền xử lý dữ liệu trực tuyến có thể gây **nghẽn đường ống đầu vào (*input pipeline bottleneck*)** khiến GPU/TPU nhàn rỗi → **tf.data (2021)** khép kín mắt xích cuối bằng cơ chế song song hóa, tự động tinh chỉnh (`AUTOTUNE`), bộ nhớ đệm (*prefetch/caching*) và phân phối dữ liệu (`tf.data.service`).

---

## 3. Danh mục 05 Bài Báo Chính (100% Scopus Q1 / WoS / CORE A\*)

| STT | Thành viên | Tên bài báo | Tác giả chính & Tổ chức | Hội nghị / Tạp chí | DOI |
| :-: | :--- | :--- | :--- | :--- | :--- |
| **1** | **TV2 — Cường** *(Nguyễn Đình Cường — `3123411043`)* | *BtrBlocks: Efficient Columnar Compression for Data Lakes* | M. Kuschewski, D. Sauerwein, A. Alhomssi, V. Leis *(TU Munich / FAU)* | **ACM SIGMOD 2023** *(PACMMOD Vol. 1, Iss. 2)* | `10.1145/3589263` |
| **2** | **TV1 — Sang** *(Nhóm trưởng — Võ Huỳnh Minh Sang — `3123411256`)* | *Delta Lake: High-Performance ACID Table Storage over Cloud Object Stores* | M. Armbrust, T. Das, ..., M. Zaharia *(Databricks, UC Berkeley, Stanford, CWI)* | **PVLDB**, Vol. 13, No. 12 (2020), pp. 3411–3424 | `10.14778/3415478.3415560` |
| **3** | **TV3 — Bảo** *(Châu Quốc Bảo — `3123411024`)* | *Photon: A Fast Query Engine for Lakehouse Systems* | A. Behm, S. Palkar, ..., R. Xin, M. Zaharia *(Databricks, UC Berkeley)* | **ACM SIGMOD 2022** *(Best Industry Paper Award)* | `10.1145/3514221.3526054` |
| **4** | **TV4 — Long** *(Nguyễn Hoàng Long — `3123411179`)* | *Optimizing Data Pipelines for Machine Learning in Feature Stores* | R. Liu, K. Park, F. Psallidas, ..., J. Camacho-Rodríguez *(Microsoft Gray Systems Lab)* | **PVLDB**, Vol. 16, No. 13 (2023), pp. 4230–4239 | `10.14778/3625054.3625060` |
| **5** | **TV1 — Sang** *(Nhóm trưởng — phụ trách bài bổ sung thứ 5)* | *tf.data: A Machine Learning Data Processing Framework* | D. G. Murray, J. Šimša, A. Klimovic, I. Indyk *(Google)* | **PVLDB**, Vol. 14, No. 12 (2021), pp. 2945–2958 | `10.14778/3476311.3476374` |

---

## 4. Phân Công Công Việc Chi Tiết Cho 4 Thành Viên (05 Bài Báo)

### Nguyên tắc phân công
- **Phần cá nhân (60% khối lượng):** Mỗi thành viên chịu trách nhiệm phân tích sâu bài báo lõi theo chuẩn giữa kỳ (Minh chứng Scopus/WoS/SJR, Phân tích IMRAD, Tái tạo 02 hình minh họa, Phản biện điểm mạnh/hạn chế). Riêng **TV1 — Sang** đã hoàn thiện sẵn bài *Delta Lake* từ giữa kỳ nên nhận phụ trách thêm **Bài báo số 5 (`tf.data`, PVLDB 2021)** để hoàn thiện đủ 05 bài báo.
- **Phần liên kết & tổng hợp chung (40% khối lượng):** Mỗi thành viên phụ trách thêm **01 hạng mục tích hợp chung** để đảm bảo báo cáo là một chỉnh thể thống nhất 5 tầng, không bị ghép cơ học.

### Bảng phân công cụ thể

| Thành viên | Bài báo phụ trách (Phần riêng) | Vai trò & Nhiệm vụ chung (Phần tích hợp) | Sản phẩm bàn giao (Deliverables) |
| :--- | :--- | :--- | :--- |
| **TV1 — Sang** *(Nhóm trưởng)* | 1. **Delta Lake** *(PVLDB 2020)* — Đã hoàn thành bản giữa kỳ, tinh gọn & nâng cấp thành chương trung tâm (Mục 2.2).<br>2. **tf.data** *(PVLDB 2021 — Bài bổ sung thứ 5)* — Phân tích sâu ML Input Pipeline, `AUTOTUNE`, prefetching/caching & `tf.data.service` (Mục 2.5). | - **Kiến trúc sư nội dung & Điều phối:** Viết Phần Mở đầu, Bối cảnh chung & Câu hỏi nghiên cứu (RQ) của cả đề tài.<br>- Thiết kế **Sơ đồ Kiến trúc Tích hợp 5 Tầng** (Hình tổng hợp mới).<br>- Biên tập, chuẩn hóa trích dẫn (IEEE) và kiểm tra tính nhất quán toàn báo cáo. | - Chương Delta Lake (đã chuẩn hóa).<br>- Chương phân tích **tf.data** + minh chứng Scopus/WoS + 02 hình vẽ lại (300 DPI + PDF).<br>- Mục 1 (Giới thiệu & Đặt vấn đề chung).<br>- Sơ đồ tổng thể 5 tầng (PNG/PDF 300 DPI).<br>- Bản báo cáo tổng hợp hoàn chỉnh (Word/PDF). |
| **TV2 — Cường** | **BtrBlocks** *(SIGMOD 2023)* — Phân tích sâu định dạng tệp cột, thuật toán nén đệ quy & giải nén tốc độ cao. *(✅ Đã xong phần riêng)* | - **Phụ trách Trục Dữ liệu & Lưu trữ:** Lập **Bảng Ma trận So sánh (Comparative Matrix)** đối chiếu cả **5 bài** (Vấn đề, Kiến trúc, Benchmark, Chỉ số đánh giá, Hạn chế).<br>- Phân tích rõ cầu nối **BtrBlocks ↔ Delta Lake**. | - Chương phân tích BtrBlocks + minh chứng Scopus/WoS + 02 hình vẽ lại *(✅ Đã xong)*.<br>- Bảng Ma trận So sánh 5 bài báo. |
| **TV3 — Bảo** | **Photon** *(SIGMOD 2022)* — Phân tích sâu Vectorized Execution (C++/SIMD), tích hợp Spark & TPC-DS 100TB. *(✅ Đã xong)* | - **Phụ trách Trục Hiệu năng & Trực quan hóa:** Xây dựng **01 Biểu đồ Tổng hợp / Đề xuất Mới cấp nhóm** *(✅ Đã xong bản 4 tầng, cần bổ sung Tầng 5 khi ghép 5 bài)*.<br>- Phân tích cầu nối **Delta Lake ↔ Photon** *(✅ Đã xong)*. | - Chương phân tích Photon + minh chứng Scopus/WoS + 02 hình vẽ lại + 01 Biểu đồ tổng hợp mới *(✅ Đã hoàn thành)*. |
| **TV4 — Long** | **ML Feature Store Pipelines / FeathrPO** *(PVLDB 2023)* — Phân tích sâu Feature Store, tối ưu hóa đường ống ML & tái sử dụng tính toán. *(✅ Đã xong)* | - **Phụ trách Tổng hợp Khoảng trống & Hướng phát triển:** Viết chương **Thảo luận, Phản biện chéo & Khoảng trống nghiên cứu chung (Synthesized Research Gaps)** + **Đề xuất hướng nghiên cứu mới** (End-to-End AI-Ready Lakehouse — bổ sung thêm liên kết Tầng 4 ↔ Tầng 5). | - Chương phân tích Feature Store + minh chứng Scopus/WoS + 02 hình vẽ lại *(✅ Đã xong)*.<br>- Chương 4 (Phản biện, Đánh đổi & Hướng nghiên cứu tương lai) *(✅ Đã có bản 4 tầng, cần bổ sung nhẹ liên kết Tầng 5)*. |

---

## 5. Khung Cấu Trúc Báo Cáo Cuối Kỳ Đề Xuất (05 Bài Báo)

1. **Chương 1: Mở đầu & Đặt vấn đề** *(Sang)* — Xu hướng hội tụ Data Lakehouse và MLOps; Mục tiêu & Câu hỏi nghiên cứu chung (RQ1–RQ3).
2. **Chương 2: Tổng quan 05 Công trình Nghiên cứu Nền tảng**
   - 2.1. Tầng Định dạng Cột: *BtrBlocks (SIGMOD 2023)* *(Cường — ✅)*
   - 2.2. Tầng Bảng Giao dịch ACID: *Delta Lake (PVLDB 2020)* *(Sang — ✅ bản gốc)*
   - 2.3. Tầng Thực thi Truy vấn Vector hóa: *Photon (SIGMOD 2022)* *(Bảo — ✅)*
   - 2.4. Tầng Đường ống Đặc trưng Học máy: *ML Feature Stores / FeathrPO (PVLDB 2023)* *(Long — ✅)*
   - 2.5. Tầng Đường ống Nạp Dữ liệu Huấn luyện ML: *tf.data (PVLDB 2021)* *(Sang — 🆕)*
3. **Chương 3: Phân tích Liên kết, So sánh Đối chiếu & Kiến trúc Tích hợp**
   - 3.1. Kiến trúc tích hợp 5 tầng đề xuất *(Sang)*
   - 3.2. Ma trận so sánh đa chiều 5 công trình *(Cường)*
   - 3.3. Tổng hợp định lượng & Biểu đồ phân tích mới *(Bảo)*
4. **Chương 4: Phản biện, Khoảng trống Nghiên cứu & Hướng Phát triển** *(Long chủ trì, Sang bổ sung liên kết Tầng 5)*
   - Đánh đổi (Trade-offs) xuyên suốt 5 tầng: Nén sâu vs. Giải nén nhanh; ACID chặt vs. Độ trễ thấp; Vectorized C++ vs. UDF Python; Pre-computation Feature vs. Chi phí lưu trữ; Băng thông nạp dữ liệu CPU vs. Hiệu suất sử dụng GPU/TPU.
   - Đề xuất hướng nghiên cứu mở: *Tự động tối ưu hóa xuyên tầng (Cross-layer Optimization) cho Lakehouse phục vụ AI/LLM*.
5. **Chương 5: Kết luận & Tài liệu tham khảo** *(Sang chuẩn hóa chuẩn IEEE)*

---

## 6. Lộ Trình Thực Hiện Theo Tuần (4 Tuần)

| Giai đoạn | Mục tiêu chính | Công việc từng thành viên | Cột mốc kiểm tra (Milestone) |
| :--- | :--- | :--- | :--- |
| **Tuần 1:** Đọc sâu & Tải tài liệu | Chốt đề cương 5 bài, tải đủ 5 PDF, kiểm tra Scopus/WoS/SJR | - **Sang:** Chốt template chung, tải thêm PDF **tf.data (PVLDB 2021)**.<br>- **Cường, Bảo, Long:** Tải bài PDF, đọc theo kỹ thuật 3-pass, trích xuất thông tin Scopus/WoS & chọn 2 hình sẽ vẽ lại. | Duyệt danh sách hình vẽ & dàn ý chi tiết 5 bài. |
| **Tuần 2:** Phân tích & Vẽ hình cá nhân | Hoàn thiện bản nháp 5 mục cá nhân & toàn bộ hình vẽ lại | - **Sang:** Rút gọn chương Delta Lake + viết Chương 1 + phân tích & vẽ 2 hình **tf.data (Mục 2.5)**.<br>- **Cường, Bảo, Long:** Viết phân tích IMRAD + code vẽ 2 hình minh họa bằng Python (300 DPI + PDF). | Nộp đủ 5 phần riêng vào `Bản thảo (Drafts)/`; review chéo. |
| **Tuần 3:** Tích hợp & Tổng hợp chéo | Tạo "chất keo" liên kết 5 bài thành 1 công trình thống nhất | - **Sang:** Vẽ Sơ đồ tích hợp 5 tầng.<br>- **Cường:** Hoàn thiện Ma trận so sánh 5 bài.<br>- **Bảo:** Code biểu đồ tổng hợp đề xuất mới.<br>- **Long (+ Sang):** Hoàn thiện Chương 4 (đủ 5 tầng). | Bản ghép hoàn chỉnh (Draft v1) có đủ hình, bảng, trích dẫn. |
| **Tuần 4:** Hoàn thiện & Chuẩn bị nộp/bảo vệ | Chống đạo văn, trau chuốt định dạng, tập vấn đáp | - **Sang:** Format báo cáo cuối (Word/PDF chuẩn SGU), kiểm tra chuẩn IEEE.<br>- **Cả 4 TV (Sang, Cường, Bảo, Long):** Đọc hiểu phần của nhau, tập hỏi-đáp phản biện chéo. | Nộp báo cáo Final & sẵn sàng bảo vệ. |

---

## 7. Gợi ý Câu hỏi Nghiên cứu Chung (Cho Chương 1)
- **RQ1:** Các điểm nghẽn hiệu năng dịch chuyển như thế nào qua 5 tầng của một hệ thống quản trị dữ liệu hiện đại (từ nén tệp cột → giao dịch bảng ACID → thực thi truy vấn → đường ống đặc trưng ML → nạp dữ liệu vào GPU/TPU)?
- **RQ2:** Làm thế nào các kỹ thuật trong *BtrBlocks*, *Delta Lake*, *Photon*, *ML Feature Store (FeathrPO)* và *tf.data* bổ trợ cho nhau để giải quyết trọn vẹn bài toán cung cấp dữ liệu quy mô lớn cho Học máy?
- **RQ3:** Những sự đánh đổi (trade-offs) và khoảng trống nghiên cứu nào vẫn còn tồn tại khi tích hợp đồng thời cả 5 tầng trên hạ tầng Cloud Object Storage?
