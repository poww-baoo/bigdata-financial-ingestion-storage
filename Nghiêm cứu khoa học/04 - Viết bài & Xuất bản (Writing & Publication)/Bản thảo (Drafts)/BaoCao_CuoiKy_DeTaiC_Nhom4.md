# BÁO CÁO BÀI TẬP CUỐI KỲ

**Cơ sở đào tạo:** Trường Đại học Sài Gòn – Khoa Công nghệ Thông tin  
**Học phần:** Phương pháp Nghiên cứu Khoa học trong Công nghệ Thông tin  
**Tên đề tài:** *Phân tích và đề xuất kiến trúc tích hợp hạ tầng quản trị dữ liệu cho học máy quy mô lớn trên nền tảng Data Lakehouse đám mây qua khảo cứu so sánh năm công trình PVLDB/SIGMOD giai đoạn 2020–2023*  
**Lớp:** `DCT123C4`  
**Nhóm sinh viên thực hiện:**
1. Võ Huỳnh Minh Sang — MSSV: `3123411256` (Nhóm trưởng)
2. Nguyễn Đình Cường — MSSV: `3123411043`
3. Châu Quốc Bảo — MSSV: `3123411024`
4. Nguyễn Hoàng Long — MSSV: `3123411179`

**Giảng viên hướng dẫn:** Vũ Ngọc Thanh Sang  
**Thời gian hoàn thiện:** Tháng 11 năm 2026  

---

# LỜI MỞ ĐẦU

Trong kỷ nguyên học máy quy mô lớn và điện toán đám mây, hiệu năng cùng độ tin cậy của một hệ thống trí tuệ nhân tạo không chỉ phụ thuộc vào kiến trúc mô hình mà được quyết định trực tiếp bởi toàn bộ chuỗi hạ tầng quản trị dữ liệu phía sau — từ định dạng tệp cột trên lưu trữ đối tượng đám mây (*Cloud Object Storage*), tầng bảng giao dịch ACID, động cơ thực thi truy vấn, kho đặc trưng (*Feature Store*) cho đến đường ống nạp dữ liệu trực tuyến vào bộ tăng tốc GPU/TPU. Thực tiễn triển khai cho thấy việc chỉ tối ưu cục bộ một thành phần đơn lẻ thường khiến điểm nghẽn dịch chuyển sang tầng kế cận thay vì mang lại cải thiện đầu-cuối bền vững.

Xuất phát từ bài toán đó, báo cáo cuối kỳ này tập trung phân tích, đối chiếu và đề xuất kiến trúc tích hợp năm tầng trên nền tảng Data Lakehouse đám mây thông qua khảo cứu năm công trình khoa học tiêu biểu công bố trong giai đoạn 2020–2023 tại hai diễn đàn hàng đầu thế giới về hệ quản trị cơ sở dữ liệu là PVLDB và ACM SIGMOD (đều đạt xếp hạng CORE A\* và lập chỉ mục trong Scopus / Web of Science), gồm *BtrBlocks* (SIGMOD 2023), *Delta Lake* (PVLDB 2020 — bài báo trục trung tâm từ giai đoạn giữa kỳ), *Photon* (SIGMOD 2022), *FeathrPO* (PVLDB 2023) và *tf.data* (PVLDB 2021). Bên cạnh việc thẩm định nguồn học thuật và phân tích chuyên sâu từng công trình, báo cáo tự lập trình tái tạo đầy đủ hệ thống hình minh họa định lượng bằng Python, xây dựng ma trận so sánh đa chiều, phản biện các sự đánh đổi liên tầng và đề xuất hướng nghiên cứu mở cho thế hệ hạ tầng *AI-Ready Lakehouse*.

---

# CHƯƠNG 1: MỞ ĐẦU VÀ ĐẶT VẤN ĐỀ NGHIÊN CỨU

## 1.1. Bối cảnh hội tụ giữa Data Lakehouse và Học máy quy mô lớn

Sự bùng nổ của dữ liệu đa phương thức cùng chi phí lưu trữ đối tượng đám mây cực thấp (Amazon S3, Azure ADLS, Google Cloud Storage) đã thúc đẩy các tổ chức dịch chuyển mạnh mẽ từ kiến trúc hai tầng rời rạc (Data Lake cho dữ liệu thô và Data Warehouse đóng kín cho phân tích BI) sang mô hình hợp nhất Data Lakehouse. Kiến trúc này cho phép lưu trữ tập trung dữ liệu trên định dạng cột mở như Apache Parquet kết hợp lớp quản trị giao dịch ACID để phục vụ đồng thời truy vấn phân tích SQL lẫn huấn luyện học máy. Tuy nhiên, khi băng thông mạng đám mây đạt ngưỡng 100 Gbps và các bộ tăng tốc phần cứng (GPU, TPU) tăng tốc độ tính toán đại số tuyến tính theo cấp số nhân, bài toán cung cấp dữ liệu liên tục, nhất quán và đủ nhanh cho toàn bộ vòng đời MLOps vẫn đối mặt với nhiều nút thắt nghiêm trọng trải dài qua từng tầng kiến trúc.

## 1.2. Chuỗi bốn nút thắt hiệu năng từ lưu trữ đối tượng đến GPU/TPU

Phân tích xuyên suốt năm công trình nền tảng trong giai đoạn 2020–2023 cho thấy hiệu năng của hạ tầng dữ liệu cho học máy bị chi phối bởi sự dịch chuyển tuần tự của bốn nút thắt kỹ thuật cốt lõi:

1. Nút thắt thứ nhất nằm ở cầu nối giữa tệp lưu trữ vật lý và tầng bảng giao dịch ACID. *Delta Lake* (2020) cung cấp giao dịch ACID và quản trị bảng trên Cloud Object Storage dựa trên định dạng tệp cột Apache Parquet. Tuy nhiên, Parquet được thiết kế từ hơn một thập kỷ trước, phụ thuộc vào nén đa dụng nặng (Snappy, Zstd) và nhúng siêu dữ liệu ở phần đuôi tệp (*footer*), dẫn tới hiện tượng bão hòa CPU khi giải nén trên mạng đám mây 100 Gbps. *BtrBlocks* (2023) giải quyết trực diện nút thắt này bằng khung nén đệ quy nhẹ đa tầng tối ưu SIMD và tách rời siêu dữ liệu.
2. Nút thắt thứ hai xuất hiện giữa tầng bảng ACID và động cơ tính toán. Khi *Delta Lake* đã loại bỏ phần lớn thao tác I/O dư thừa nhờ nhật ký giao dịch `_delta_log`, *Data Skipping* và phân cụm *Z-Order*, điểm nghẽn dịch chuyển mạnh sang chi phí CPU và bộ thu gom rác (GC) của máy ảo JVM trên Apache Spark. *Photon* (2022) giải quyết nút thắt này bằng động cơ thực thi vector hóa viết thuần bằng C++ (SIMD) tích hợp trong suốt vào Databricks Runtime qua giao diện JNI không sao chép.
3. Nút thắt thứ ba nằm giữa động cơ tính toán và kho đặc trưng học máy. Ngay cả khi truy vấn SQL và ETL chạy nhanh trên Lakehouse, quy trình tạo tập huấn luyện học máy vẫn phải thực hiện lặp đi lặp lại các phép ghép theo mốc thời gian (*Point-in-Time Join*) để phòng tránh rò rỉ dữ liệu (*Data Leakage*), gây xáo trộn mạng (*shuffle*) khổng lồ và lãng phí tài nguyên tính toán. *FeathrPO* (2023) đưa tư duy tối ưu hóa truy vấn cơ sở dữ liệu vào lớp Feature Store thông qua ước lượng phân vị KLL, viết lại truy vấn tái sử dụng, rút gọn *Semijoin* và chọn bố cục phân vùng tự động.
4. Nút thắt thứ tư nằm ở chặng cuối giữa kho đặc trưng và bộ tăng tốc GPU/TPU. Sau khi tập đặc trưng sạch được xuất ra lưu trữ, khâu đọc dữ liệu, giải mã, tăng cường dữ liệu (*data augmentation*), xáo trộn và gom lô trực tuyến trên CPU thường không theo kịp tốc độ tiêu thụ của GPU/TPU, chiếm tới 30% tổng thời gian tính toán trên cụm sản xuất. *tf.data* (2021) khép kín mắt xích cuối cùng bằng giao diện lập trình khai báo, tối ưu hóa đồ thị tĩnh (Grappler) và cơ chế tự động tinh chỉnh động `AUTOTUNE` dựa trên mô hình hàng đợi M/M/1/k.

## 1.3. Mục tiêu và câu hỏi nghiên cứu chung

Báo cáo hướng tới mục tiêu hệ thống hóa, thẩm định uy tín học thuật, tái lập trực quan hóa và phản biện chéo năm công trình giai đoạn 2020–2023 nhằm đề xuất kiến trúc tích hợp năm tầng và giải đáp ba câu hỏi nghiên cứu xuyên suốt:
- Câu hỏi nghiên cứu 1 (RQ1): Các điểm nghẽn hiệu năng dịch chuyển như thế nào qua năm tầng của một hạ tầng quản trị dữ liệu hiện đại trên nền tảng đám mây, từ nén tệp cột, giao dịch bảng ACID, thực thi truy vấn vector hóa, đường ống đặc trưng học máy cho đến đường ống nạp dữ liệu vào GPU/TPU?
- Câu hỏi nghiên cứu 2 (RQ2): Các cơ chế kỹ thuật trong *BtrBlocks*, *Delta Lake*, *Photon*, *FeathrPO* và *tf.data* bổ trợ cho nhau ra sao để giải quyết trọn vẹn bài toán cung cấp dữ liệu quy mô lớn cho học máy?
- Câu hỏi nghiên cứu 3 (RQ3): Những sự đánh đổi (*trade-offs*) và khoảng trống nghiên cứu liên tầng nào vẫn còn tồn tại khi tích hợp đồng thời cả năm tầng trên hạ tầng Cloud Object Storage, và đâu là hướng mở rộng tiềm năng cho kỷ nguyên AI/LLM?

## 1.4. Danh mục năm công trình nền tảng và bảng phân công nhóm

Toàn bộ công việc nghiên cứu, phân tích bài báo lõi, tái lập trực quan hóa và tích hợp tổng thể được phân công minh bạch cho bốn thành viên lớp `DCT123C4` như trình bày trong bảng dưới đây.

| STT | Tầng kiến trúc | Công trình & Ấn phẩm (2020–2023) | Chỉ mục & DOI | Thành viên phụ trách & Nhiệm vụ tích hợp chung |
| :-: | :--- | :--- | :--- | :--- |
| 1 | Tầng 1: Định dạng tệp cột mở | *BtrBlocks: Efficient Columnar Compression for Data Lakes* — Kuschewski et al., ACM SIGMOD 2023 (*PACMMOD* Vol. 1, No. 2) | CORE A\*, WoS ESCI; DOI: `10.1145/3589263` | Nguyễn Đình Cường (`3123411043` — TV2): Phân tích Mục 2.1, tái tạo 02 hình, cầu nối BtrBlocks ↔ Delta Lake và Ma trận so sánh 05 công trình (Mục 3.2). |
| 2 | Tầng 2 (Trục lõi): Bảng giao dịch ACID | *Delta Lake: High-Performance ACID Table Storage over Cloud Object Stores* — Armbrust et al., PVLDB 2020 (Vol. 13, No. 12) | CORE A\*, Scopus Q1 (`21100199855`), WoS; DOI: `10.14778/3415478.3415560` | Võ Huỳnh Minh Sang (`3123411256` — TV1, Nhóm trưởng): Chuẩn hóa Mục 2.2, viết Chương 1, Sơ đồ tích hợp 5 tầng (Mục 3.1), Chương 5 và biên tập tổng thể. |
| 3 | Tầng 3: Thực thi truy vấn vector hóa | *Photon: A Fast Query Engine for Lakehouse Systems* — Behm et al., ACM SIGMOD 2022 (*Industry Best Paper Award*) | CORE A\*, Scopus, WoS CPCI-S; DOI: `10.1145/3514221.3526054` | Châu Quốc Bảo (`3123411024` — TV3): Phân tích Mục 2.3, tái tạo 02 hình, cầu nối Delta Lake ↔ Photon, Biểu đồ tổng hợp hiệu năng và giao thức kiểm chứng (Mục 3.3). |
| 4 | Tầng 4: Kho đặc trưng học máy | *Optimizing Data Pipelines for Machine Learning in Feature Stores* — Liu et al., PVLDB 2023 (Vol. 16, No. 13) | CORE A\*, Scopus Q1 (`21100199855`), WoS; DOI: `10.14778/3625054.3625060` | Nguyễn Hoàng Long (`3123411179` — TV4): Phân tích Mục 2.4, tái tạo 02 hình và chủ trì Chương 4 (Phản biện chéo, đánh đổi liên tầng, khoảng trống nghiên cứu và hướng mở rộng). |
| 5 | Tầng 5: Đường ống nạp dữ liệu ML | *tf.data: A Machine Learning Data Processing Framework* — Murray et al., PVLDB 2021 (Vol. 14, No. 12) | CORE A\*, Scopus Q1 (`21100199855`), WoS; DOI: `10.14778/3476311.3476374` | Võ Huỳnh Minh Sang (`3123411256` — TV1, Nhóm trưởng): Phụ trách bài bổ sung thứ 5 (Mục 2.5), tái tạo 02 hình, cầu nối FeathrPO ↔ tf.data và mở rộng liên kết tầng 5 vào Chương 3–4. |

---

# CHƯƠNG 2: TỔNG QUAN VÀ PHÂN TÍCH SÂU NĂM CÔNG TRÌNH NỀN TẢNG

## 2.1. Tầng 1 — Định dạng tệp cột mở và nén nhẹ: BtrBlocks (SIGMOD 2023)

### 2.1.1. Thông tin ấn phẩm và minh chứng chỉ mục
Công trình *"BtrBlocks: Efficient Columnar Compression for Data Lakes"* do bốn tác giả Maximilian Kuschewski, David Sauerwein, Adnan Alhomssi và Viktor Leis (TU Munich và FAU, Đức) thực hiện, công bố tháng 6/2023 trên *Proceedings of the ACM on Management of Data (PACMMOD)* — kỷ yếu tạp chí hóa của hội nghị ACM SIGMOD 2023, Tập 1, Số 2, Bài 118, trang `118:1–118:26` (`Online ISSN: 2836-6573`, DOI: `10.1145/3589263`). Tạp chí *PACMMOD* được lập chỉ mục chính thức trong Web of Science Core Collection (ESCI) và kế thừa trực tiếp hạng CORE A\* của ACM SIGMOD; dữ liệu thư mục mở OpenAlex ghi nhận h-index ấn phẩm đạt 53, 2-year mean citedness đạt 8,8, riêng bài báo đạt 89 lượt trích dẫn trên OpenAlex và hơn 120 lượt trên Google Scholar.

### 2.1.2. Phân tích nội dung nghiên cứu cốt lõi
Trong môi trường Data Lake trên đám mây có băng thông mạng đạt 100 Gbps (như AWS `c5n.18xlarge`), định dạng chuẩn công nghiệp Apache Parquet bộc lộ hai điểm yếu nghiêm trọng là tập lược đồ mã hóa nghèo nàn buộc phải bọc thêm nén đa dụng nặng (Snappy, Zstd) khiến CPU bị bão hòa ở khâu giải nén trước khi lấp đầy đường truyền mạng, đồng thời việc nhúng siêu dữ liệu vào phần đuôi tệp (*footer*) buộc trình đọc tốn tới 3 lượt HTTP GET tuần tự cho mỗi cột. Dựa trên khảo sát Public BI Benchmark (43 bảng thực tế, 2.451 cột, 119,5 GB) — nơi kiểu chuỗi chiếm tới 71,5% và có rất nhiều số thực thập phân `double` — nhóm tác giả thiết kế định dạng cột mã nguồn mở BtrBlocks xoay quanh bốn trụ cột kỹ thuật chính:

1. Khung nén đệ quy đa tầng (*Cascading Compression*) cho phép xếp chồng tối đa 3 tầng các lược đồ mã hóa nhẹ chuyên biệt theo kiểu dữ liệu (`Integer`, `Double`, `String`), chuyển đổi dữ liệu phức tạp thành các mảng số nguyên đơn giản để tận dụng `SIMD-FastPFOR`, `SIMD-FastBP128` và `RLE`.
2. Thuật toán chọn lược đồ bằng lấy mẫu phân tầng (`10 × 64` phần tử) chỉ lấy mẫu 1% mỗi khối 64.000 dòng để thử nghiệm nhanh chuỗi nén tối ưu; chi phí chọn lược đồ chỉ tốn 1,2% CPU nhưng đạt tỷ lệ nén sát mức tối ưu lý thuyết (chỉ kém 3,3%).
3. Kỹ thuật nén số thực `Pseudodecimal Encoding (PDE)` và chuỗi `Dict + FSST` biến đổi số thực thập phân IEEE 754 (như giá tiền, số liệu tài chính) thành cặp số nguyên hệ số và số mũ, kết hợp FSST cho chuỗi dài truy cập ngẫu nhiên nhanh.
4. Nguyên tắc tách rời siêu dữ liệu (*Orthogonal Metadata*) và tối ưu SIMD AVX2 loại bỏ hoàn toàn footer metadata khỏi khối nén, đồng thời giải nén hàng loạt bằng tập lệnh vector AVX2 không sao chép chuỗi dư thừa.

Kết quả thực nghiệm trên 5 tập dữ liệu Public BI lớn nhất đọc từ Amazon S3 trên máy ảo AWS `c5n.18xlarge` (Bảng 5, tr. `118:20`) khẳng định tính vượt trội toàn diện của BtrBlocks. Cụ thể, thông lượng quét trên dữ liệu nén $T_c$ đạt 86,2 Gbps (tiệm cận ngưỡng giới hạn phần cứng 91 Gbps của S3) với băng thông giải nén gốc $T_u = 174,6\text{ GB/s}$ và chi phí `$0,97` cho 10 lượt quét (10,31 lượt/$). Con số này nhanh hơn 3,48× về $T_c$ (và 2,22× về $T_u$) so với Parquet + Zstd (24,8 Gbps, `$1,70`), nhanh hơn 2,60× so với Parquet + Snappy (33,2 Gbps, `$1,74`), đồng thời giảm chi phí quét đám mây khoảng 1,8× so với Parquet có nén và 2,6× so với Parquet không nén (`$2,47`).

### 2.1.3. Hai hình minh họa tái tạo từ bài báo gốc

![Hình 2.1: Cây quyết định nén đệ quy đa tầng của BtrBlocks — Tái tạo từ Figure 3 (SIGMOD 2023)](<../../99 - Đính kèm (Attachments)/BtrBlocks_Hinh1_TaiTao_CayQuyetDinhNen.png>)

Hình 2.1 tái tạo đầy đủ ba cây quyết định nén đệ quy từ Figure 3 gốc (tr. `118:10`) theo ba kiểu dữ liệu (`Double`, `String`, `Integer`) bằng Python (`matplotlib`) ở độ phân giải 300 DPI kèm hộp chú giải màu sắc và tham số mặc định (`recur = 3`, lấy mẫu `10 × 64`). Sơ đồ chứng minh tính mô-đun của BtrBlocks: thay vì tìm một thuật toán nén đa dụng chậm chạp, hệ thống phân rã kiểu `Double` (qua `Pseudodecimal`, `Dict`, `Freq`, `RLE`) và `String` (qua `Dict`, `FSST`, `Freq`) thành các mảng số nguyên để tiếp tục nén siêu nhanh bằng `FastBP128` hoặc `PFOR`, đảm bảo dừng an toàn ở độ sâu tối đa 3 tầng.

![Hình 2.2: Thông lượng quét S3 và chi phí quét so với Apache Parquet — Tái tạo từ Figure 1 & Table 5 (SIGMOD 2023)](<../../99 - Đính kèm (Attachments)/BtrBlocks_Hinh2_TaiTao_S3ScanBenchmark.png>)

Hình 2.2 tái tạo Figure 1 gốc (tr. `118:2`) với số liệu đối soát trực tiếp từ Table 5 (tr. `118:20`), đối chiếu thông lượng nén $T_c$ (`Gbps`) trên trục hoành và hiệu quả chi phí (`S3 Scans per Dollar`) trên trục tung, bổ sung đường giới hạn phần cứng ~91 Gbps và gắn nhãn định lượng đầy đủ bộ ba thông số ($T_c$, lượt/$, $T_u$) cho cả bốn định dạng. Kết quả làm rõ điểm tối ưu Pareto của BtrBlocks khi phá vỡ sự đánh đổi giữa kích thước tệp nhỏ (Parquet+Zstd/Snappy bị nghẽn CPU ở 24,8–33,2 Gbps) và tốc độ giải nén cao (Parquet thuần phình dung lượng nên tốn `$2,47`).

### 2.1.4. Đánh giá và phản biện
BtrBlocks định vị chính xác sự dịch chuyển nút thắt sang tốc độ giải nén $T_c$ trong kỷ nguyên mạng 100 Gbps và chứng minh thuyết phục bằng thí nghiệm đối chứng scalar với SIMD rằng lợi thế cốt lõi đến từ thiết kế kiến trúc bậc cao. Tuy nhiên, công trình còn tồn tại bốn hạn chế đáng lưu ý: rào cản tương thích hệ sinh thái cực lớn do Apache Parquet đang thống trị toàn bộ công cụ Lakehouse; thiết kế ưu tiên giải nén toàn khối 64.000 dòng nên kém tối ưu cho truy vấn điểm (*point lookup*) hay lọc sớm trực tiếp trên dữ liệu nén; thuật toán *Pseudodecimal* kém hiệu quả với số thực độ chính xác cao mang tính ngẫu nhiên (như tọa độ GPS hay vector embedding trong học máy); và thực nghiệm S3 mới dừng ở lớp đọc C++ thuần, chưa kiểm chứng đầu-cuối trong một SQL Query Engine hoàn chỉnh.

---

## 2.2. Tầng 2 (Trung tâm) — Tầng bảng giao dịch ACID: Delta Lake (PVLDB 2020)

### 2.2.1. Thông tin ấn phẩm và minh chứng chỉ mục
Bài báo *"Delta Lake: High-Performance ACID Table Storage over Cloud Object Stores"* do nhóm 21 tác giả từ Databricks, UC Berkeley, Stanford và CWI Amsterdam (Michael Armbrust, Tathagata Das, Reynold Xin, Peter Boncz, Ali Ghodsi, Matei Zaharia và cộng sự) công bố tháng 8/2020 trên *Proceedings of the VLDB Endowment (PVLDB)*, Tập 13, Số 12, trang `3411–3424` (`ISSN: 2150-8097`, DOI: `10.14778/3415478.3415560`). Ấn phẩm được lập chỉ mục chính thức trên Scopus tại Source ID `21100199855` (phân hạng Q1 trên ScimagoJR, CiteScore 8,2, h-index trên 200), định vị trên Clarivate Master Journal List thuộc Web of Science Core Collection (CPCI-S và ESCI) và đạt xếp hạng học thuật cao nhất CORE A\*.

### 2.2.2. Phân tích nội dung nghiên cứu cốt lõi
Các hệ thống hồ dữ liệu truyền thống lưu trực tiếp tệp Parquet trên Amazon S3 hay Azure Blob vốn thiếu tính chất giao dịch ACID: khi tác vụ ghi bị lỗi giữa chừng, các tệp dở dang làm hỏng toàn bộ bảng; đọc/ghi đồng thời gây sai lệch kết quả; thao tác liệt kê tệp (`LIST`) chậm nghiêm trọng khi bảng có hàng triệu tệp nhỏ, và doanh nghiệp phải duy trì song song hai đường ống tách biệt cho xử lý theo lô (*Batch*) và xử lý luồng (*Streaming*). Delta Lake giải quyết triệt để các hạn chế này bằng kiến trúc tầng bảng giao dịch mở đặt trực tiếp trên Cloud Object Store mà không cần dịch vụ quản trị siêu dữ liệu tập trung đắt đỏ thông qua ba cơ chế nền tảng:

1. Cơ chế nhật ký giao dịch phi máy chủ (`_delta_log`) lưu mọi biến đổi bảng (thêm/xóa tệp, cập nhật schema) thành các bản ghi JSON tăng dần tuần tự (`000000.json`, `000001.json`, ...) kèm nén định kỳ sang tệp Checkpoint Parquet mỗi 10 giao dịch để tăng tốc khôi phục trạng thái bảng.
2. Cơ chế kiểm soát đồng thời lạc quan (*Optimistic Concurrency Control — OCC*) dựa vào thao tác ghi nguyên tử (*put-if-absent* hoặc dịch vụ điều phối nhẹ trên S3) giúp đảm bảo tính cô lập *Snapshot Isolation* và *Serializable* giữa nhiều tiến trình đọc và ghi đồng thời.
3. Nhóm kỹ thuật tối ưu truy vấn và quản trị vòng đời dữ liệu tự động lưu thống kê `min/max` của từng cột ngay trong log giao dịch để bỏ qua tệp (*Data Skipping*), hỗ trợ gom tệp nhỏ (`OPTIMIZE`), sắp xếp đa chiều (*Z-Order Clustering*), thực thi ràng buộc schema (*Schema Enforcement/Evolution*), du hành thời gian (*Time Travel*) phục vụ kiểm toán hoặc tái lập huấn luyện học máy, và hợp nhất mô hình Batch cùng Streaming theo kiến trúc *Medallion* (Bronze → Silver → Gold).

Trên bài đo chuẩn công nghiệp TPC-DS 1 TB Power Test (cụm AWS `1 Driver + 8 Worker i3.2xlarge`), Delta Lake hoàn thành toàn bộ bộ truy vấn chỉ trong 0,93 giờ, nhanh hơn 1,55× (tiết kiệm 35,4% thời gian) so với 3rd-Party Spark Parquet (1,44 giờ) và nhanh hơn 4,04× (tiết kiệm 75,3% thời gian) so với 3rd-Party Presto (3,76 giờ).

### 2.2.3. Hình minh họa tái tạo và biểu đồ đề xuất từ giai đoạn giữa kỳ

![Hình 2.3: Kiến trúc đường ống tích hợp dữ liệu Medallion trên Delta Lake — Tái tạo từ Figure 1 (PVLDB 2020)](<../../99 - Đính kèm (Attachments)/Hinh1_TaiTao_KienTruc_Pipeline.png>)

![Hình 2.4: So sánh thời gian thực thi TPC-DS 1 TB Power Test — Tái tạo từ Figure 6 (PVLDB 2020)](<../../99 - Đính kèm (Attachments)/Hinh2_TaiTao_TPCDS_PowerTest.png>)

![Hình 2.5: Biểu đồ đề xuất mới — Hệ số tăng tốc (Speedup) và tỷ lệ thời gian tiết kiệm của Delta Lake](<../../99 - Đính kèm (Attachments)/Hinh3_DeXuatMoi_HeSoTangToc.png>)

Hình 2.3 tái tạo Figure 1 gốc minh họa cách Delta Lake hợp nhất luồng dữ liệu thời gian thực và dữ liệu theo lô qua ba tầng Bronze–Silver–Gold mà không cần sao chép sang kho dữ liệu thứ hai. Hình 2.4 tái tạo trực quan kết quả TPC-DS 1 TB Power Test từ Figure 6 (0,93 giờ so với 1,44 giờ và 3,76 giờ), còn Hình 2.5 chuyển hóa định lượng thành hai chỉ số hỗ trợ ra quyết định trực tiếp là hệ số tăng tốc (1,55× đến 4,04×) và tỷ lệ phần trăm thời gian tính toán tiết kiệm được (35,4% đến 75,3%).

### 2.2.4. Đánh giá và phản biện
Delta Lake đã đặt nền móng chuẩn mực cho kỷ nguyên Data Lakehouse nhờ thiết kế nhật ký giao dịch đơn giản, khả năng mở rộng gần như không giới hạn theo Cloud Object Store và tính mã nguồn mở mạnh mẽ. Tuy vậy, công trình vẫn có ba giới hạn chính: độ trễ ghi thời gian thực bị giới hạn bởi chu kỳ tạo tệp JSON và nguy cơ xung đột OCC khi có nhiều luồng ghi đồng thời tốc độ rất cao; sự phụ thuộc vào định dạng tệp vật lý Apache Parquet truyền thống nên chưa tối ưu tốc độ giải nén trên mạng 100 Gbps; và hiệu năng tính toán các truy vấn SQL phức tạp sau khi đọc tệp vẫn bị giới hạn bởi động cơ thực thi JVM của Apache Spark.

---

## 2.3. Tầng 3 — Động cơ thực thi truy vấn vector hóa: Photon (SIGMOD 2022)

### 2.3.1. Thông tin ấn phẩm và minh chứng chỉ mục
Bài báo *"Photon: A Fast Query Engine for Lakehouse Systems"* do 24 tác giả thuộc Databricks Inc. (Alexander Behm, Shoumik Palkar, Reynold Xin, Matei Zaharia và cộng sự) trình bày tại hội nghị *ACM SIGMOD '22* (Philadelphia, PA, USA, tháng 6/2022, trang `2326–2339`, ISBN `978-1-4503-9249-5/22/06`, DOI: `10.1145/3514221.3526054`). Công trình xuất sắc giành giải SIGMOD 2022 Industry Best Paper Award. Hội nghị ACM SIGMOD đạt hạng CORE A\*, kỷ yếu được lập chỉ mục chính thức trong Scopus và Web of Science Core Collection (CPCI-S). Về mặt liêm chính khoa học, do đây là kỷ yếu hội nghị năm 2022 trước khi chuyển sang tạp chí PACMMOD nên ấn phẩm không mang phân vị tạp chí Q1–Q4 mà được bảo chứng bằng xếp hạng CORE A\*, chỉ mục Scopus/WoS CPCI-S và giải thưởng Best Industry Paper; dữ liệu OpenAlex ghi nhận 92 lượt trích dẫn.

### 2.3.2. Phân tích nội dung nghiên cứu cốt lõi
Khi Delta Lake kết hợp SSD cache và Data Skipping giúp giảm mạnh độ trễ I/O, nút thắt hiệu năng của hệ thống Lakehouse dịch chuyển hoàn toàn sang tầng thực thi trong bộ nhớ (*CPU-bound*) của máy ảo JVM trên Spark SQL: bộ thu gom rác (GC) suy thoái nặng khi heap vượt quá 64 GB, cơ chế sinh mã Java (*Whole-Stage CodeGen*) thường xuyên bị rơi về nhánh thông dịch chậm trên bảng rộng hàng trăm cột, và Java không cho phép kiểm soát tường minh tập lệnh vector SIMD. Nhóm tác giả xây dựng Photon như một động cơ thực thi vector hóa đơn luồng viết bằng C++ native nhúng trong Executor JVM của Databricks Runtime, nổi bật với bốn đột phá kiến trúc:

1. Mô hình thông dịch vector hóa theo lô cột (`Column Batch` kết hợp `Position List`) được ưu tiên thay vì sinh mã (*Code-Gen* vốn khó gỡ lỗi và tốn chi phí biên dịch lại), giúp xử lý từng lô cột liên tiếp trong bộ nhớ đệm CPU kèm mảng chỉ số hàng hoạt động, đồng thời sử dụng C++ template compile-time `<bool kHasNulls, bool kAllRowsActive>` để triệt tiêu rẽ nhánh và kích hoạt tự động vector hóa SIMD.
2. Cấu trúc bảng băm vector hóa ba bước tách biệt pha băm theo lô (SIMD), pha dò nạp con trỏ theo lô để tối đa hóa song song hóa truy cập bộ nhớ (*memory-level parallelism*), và pha so sánh khóa trên bản ghi xoay dạng hàng trong bảng băm.
3. Cơ chế thích nghi vi mô cấp batch ở thời điểm chạy (*Batch-level Runtime Adaptivity*) tự động bỏ kiểm tra `NULL` trên lô đầy đủ, phát hiện cờ chuỗi *all-ASCII* để chạy SIMD thay vì thư viện Unicode ICU, nén lô thưa trước khi dò bảng băm (*Adaptive Join Compaction*) và nén chuỗi UUID 36 byte thành số nguyên 128-bit trước khi shuffle (*Adaptive Shuffle Encoding*).
4. Cơ chế tích hợp triển khai từng phần (*Partial Rollout*) với Spark truyền con trỏ `OffHeapColumnVector` qua giao diện Zero-copy JNI chỉ tốn khoảng 23 ns mỗi lần gọi (0,06% tổng thời gian), đăng ký dùng chung bộ quản lý bộ nhớ thống nhất với cơ chế *recursive spill*, và đảm bảo tương đương ngữ nghĩa Spark SQL bằng bộ kiểm thử ba tầng (Unit, End-to-End, Fuzz).

Thực nghiệm trên cụm AWS `i3.2xlarge` chứng minh hiệu năng vượt trội của Photon. Ở mức vi chuẩn, Photon nhanh hơn DBR 3,5× với Hash Join (5,3 giây so với 18,9 giây), 3,5×–5,7× với `collect_list`, 3,14×–3,92× với `upper()` SIMD ASCII, và ghi Parquet xuống S3 nhanh hơn 2×. Trên TPC-H SF=3000 (cụm 1+8 nút, dữ liệu Delta Lake trên S3), Photon đạt tăng tốc trung bình 4,0× theo từng truy vấn và đỉnh 23× ở truy vấn Q1 (nặng phép tính `Decimal`). Trên TPC-DS 100 TB (cụm 256 nút), Databricks Runtime bật Photon thiết lập kỷ lục thế giới có kiểm toán của hội đồng TPC. Đặc biệt trên truy vấn TPC-DS Q24, cơ chế *Adaptive Join Compaction* rút thời gian từ 120 giây (không nén) xuống 76 giây, đạt tăng tốc 1,55× so với DBR (118 giây) và 1,58× so với Photon không nén.

### 2.3.3. Hai hình minh họa tái tạo từ bài báo gốc

![Hình 2.6: Kiến trúc tầng thực thi Databricks Runtime và động cơ Photon — Tái tạo từ Figure 1 (SIGMOD 2022)](<../../99 - Đính kèm (Attachments)/TV3_Hinh1_KienTruc_Photon.png>)

Hình 2.6 tái tạo Figure 1 gốc (tr. 2328) làm rõ vai trò thực sự của Photon: động cơ này không thay thế toàn bộ Apache Spark mà vận hành như nhân thực thi C++ đơn luồng trên từng phân vùng (`FileScan → Filter → Join`) bên trong Executor của Databricks Runtime, kế thừa nguyên vẹn trình tối ưu Catalyst, bộ lập lịch tác vụ của Driver và tầng lưu trữ bảng mở Delta Lake trên đám mây.

![Hình 2.7: Tác động của Adaptive Join Compaction trên truy vấn TPC-DS Q24 — Tái tạo từ Figure 9 (SIGMOD 2022)](<../../99 - Đính kèm (Attachments)/TV3_Hinh2_TPCDS_Q24.png>)

Hình 2.7 tái tạo Figure 9 gốc (tr. 2337) đối chứng ba cấu hình trên cụm 16 nút (DBR 118 giây, Photon không compaction 120 giây và Photon có adaptive join compaction 76 giây), chứng minh trực quan rằng nếu không nén lô thưa, mô hình vector hóa C++ thậm chí chậm hơn Spark Code-Gen 1,7%; việc kích hoạt nén lô thích nghi giúp đảo ngược tình thế và cắt giảm 35,6% thời gian thực thi (1,55× so với DBR).

### 2.3.4. Đánh giá và phản biện
Photon là hình mẫu xuất sắc về kỹ thuật hệ thống công nghiệp nhờ cơ chế tích hợp không gián đoạn (*partial rollout*), chi phí ranh giới JNI cực nhỏ (0,06%) và kiểm chứng thực nghiệm nghiêm ngặt ở quy mô 100 TB. Hạn chế lớn nhất của công trình là mã nguồn đóng độc quyền trong sản phẩm thương mại Databricks nên cộng đồng học thuật khó tái lập độc lập; đồng thời động cơ chưa hỗ trợ *Sort-Merge Join* và vẫn buộc phải chuyển về luồng JVM chậm khi gặp các hàm người dùng tự định nghĩa (UDF Python/ML) xen kẽ trong kế hoạch truy vấn.

---

## 2.4. Tầng 4 — Đường ống đặc trưng học máy: FeathrPO (PVLDB 2023)

### 2.4.1. Thông tin ấn phẩm và minh chứng chỉ mục
Công trình *"Optimizing Data Pipelines for Machine Learning in Feature Stores"* do nhóm 10 tác giả đến từ Microsoft Gray Systems Lab cùng các trường đại học và tập đoàn công nghệ (Rui Liu, Kwanghyun Park, Fotis Psallidas, Jesús Camacho-Rodríguez và cộng sự) công bố tháng 8/2023 trên *Proceedings of the VLDB Endowment (PVLDB)*, Tập 16, Số 13, trang `4230–4239` (`ISSN: 2150-8097`, DOI: `10.14778/3625054.3625060`). Ấn phẩm nằm trên Scopus tại Source ID `21100199855` (phân hạng Q1, CiteScore 7,5–8,2), lập chỉ mục trong Web of Science Core Collection (CPCI-S/ESCI) và đạt xếp hạng CORE A\*.

### 2.4.2. Phân tích nội dung nghiên cứu cốt lõi
Trong quy trình MLOps, các Feature Store (như Feathr, Feast, Tecton) đóng vai trò hệ quản trị cơ sở dữ liệu chuyên biệt cho học máy nhằm quản trị và đồng bộ đặc trưng giữa huấn luyện ngoại tuyến và suy luận trực tuyến. Phép toán đắt đỏ và nhạy cảm nhất khi tạo tập dữ liệu huấn luyện chuỗi thời gian là *Point-in-Time (PIT) Join* (*As-of Join*), yêu cầu mỗi bản ghi nhãn ở thời điểm $t_{\text{obs}}$ chỉ được ghép với bản ghi đặc trưng mới nhất tại $t_{\text{feat}} \le t_{\text{obs}}$ nhằm tuyệt đối tránh lỗi rò rỉ dữ liệu (*Data Leakage*). Thực thi PIT Join đa bảng (bảng nhãn $L$, bảng đặc trưng $F$ và bảng phụ trợ $A$) một cách trực tiếp trên Spark gây lượng *network shuffle* khổng lồ và tính toán lặp đi lặp lại giữa các vòng thử nghiệm mô hình.

Nhóm tác giả thiết kế lớp tối ưu hóa không xâm lấn FeathrPO tích hợp vào Feature Store mã nguồn mở Feathr gồm ba trụ cột phối hợp chặt chẽ:
1. Mô hình chi phí nhận biết bố cục dựa trên KLL Sketches (§4) ước lượng phân vị phân bố thời gian để tính chính xác lượng dữ liệu cần quét $C_q = \sum_{s \in S_q} \mathcal{D}_s - \mathcal{U}_{s_p}^q$. Thực nghiệm (Bảng 2, tr. 4236) cho thấy KLL sketches đạt độ chính xác 96,84%–99,73%, vượt trội bộ ước lượng mặc định của Spark (89,61%–92,19%), giúp nhận diện ngưỡng độ chọn lọc cao (80%–100%) để tự động quay về kế hoạch mặc định nhằm ngăn ngừa suy thoái hiệu năng.
2. Cơ chế tái sử dụng tính toán và rút gọn Semijoin (§5) sử dụng bộ *Matcher* phát hiện tập huấn luyện đã vật chất hóa có khả năng bao hàm, chuyển sang bộ *Rewriter* chỉ tính phần chênh lệch (*delta*) trên cửa sổ thời gian mới, đồng thời chèn bộ lọc `[min_ts, max_ts]` (*Semijoin Reduction*) để cắt giảm *shuffle* dư thừa.
3. Bộ chọn bố cục phân vùng vật lý tự động bằng Quy hoạch Nguyên Nhị phân — BIP (§6) mô hình hóa bài toán chọn độ mịn phân vùng thời gian (năm, tháng, ngày hoặc giờ) dưới ngân sách ghi lại $\mathcal{B}$ và giải bằng Google OR-Tools (*glop solver*) chỉ trong 6–7 giây cho quy mô 10.000 truy vấn và 1.000 bảng nguồn.

Đánh giá trên bốn tập dữ liệu quy mô công nghiệp (`TPCxAI-UC7 SF10`, `TPCxAI-UC10 SF10`, `Kaggle-Favorita`, `Kaggle-eCommerce` với bảng đặc trưng tới 125,5 triệu dòng / 3,9 GB) trên cụm đám mây Azure Synapse (Spark v3.1) và cụm cục bộ cho thấy FeathrPO đạt mức tăng tốc lên tới 3,00× ở bài toán phát hiện gian lận tài chính `TPCxAI-UC10` (nơi bảng đặc trưng gấp gần 1.500 lần bảng nhãn), duy trì tăng tốc 1,4×–2,50× khi cắm ghép lên các thuật toán PIT Join tiên tiến (*Early-stop Sort Merge*, *Union Merge*) và giữ vững mức cải thiện 1,3×–2,3× khi mở rộng quy mô từ SF1 đến SF100.

### 2.4.3. Hai hình minh họa tái tạo từ bài báo gốc

![Hình 2.8: Kiến trúc tích hợp các module tối ưu mới của FeathrPO vào Feathr — Tái tạo từ Figure 8 (PVLDB 2023)](<../../99 - Đính kèm (Attachments)/Hinh_TV4_1_KienTruc_FeathrPO.png>)

Hình 2.8 tái tạo Figure 8 gốc (tr. 4235) phân biệt trực quan hai module tối ưu mới của FeathrPO (*Data Layout Selector* và *Reuse-based Optimizer*, tô màu xanh lá) bên cạnh các thành phần sẵn có của Feathr (màu xám) trên Azure, khẳng định thiết kế không xâm lấn (*non-intrusive*) khi không yêu cầu chỉnh sửa mã nguồn lõi của Apache Spark hay kho lưu trữ bên dưới.

![Hình 2.9: Hệ số cải thiện hiệu năng của FeathrPO trên 4 tập dữ liệu và 3 thuật toán PIT Join — Tái tạo từ Figure 12 (PVLDB 2023)](<../../99 - Đính kèm (Attachments)/Hinh_TV4_2_HieuNang_FeathrPO.png>)

Hình 2.9 tái tạo Figure 12 gốc (tr. 4237) biểu diễn 12 tổ hợp dữ liệu–thuật toán đều vượt xa mốc cơ sở 1,0×, nổi bật với đỉnh 3,00× (Feathr ZipPartition Cloud) và 2,50× (Union Merge Local) trên `TPCx-AI UC10` (hai giá trị đỉnh lấy trực tiếp từ văn bản §8.2; 10 cột còn lại trích xuất trực quan từ trục tung Figure 12 gốc với độ chính xác hai chữ số thập phân từ 1,32× đến 2,02×). Kết quả khẳng định bản chất cắm ghép đa nền tảng (*pluggable*) của FeathrPO.

### 2.4.4. Đánh giá và phản biện
FeathrPO thành công trong việc đưa tối ưu hóa truy vấn cơ sở dữ liệu vào lớp Feature Store mã nguồn mở mà không phá vỡ lõi Spark. Tuy nhiên, hệ thống vẫn tồn tại ba hạn chế: mới can thiệp ở tầng kế hoạch logic trên Spark JVM nên chưa khai thác trực tiếp định dạng nén siêu nhanh (BtrBlocks) hay động cơ C++ (Photon); quyết định vật chất hóa đặc trưng nào vẫn do kỹ sư dữ liệu chỉ định thủ công qua API thay vì khuyến nghị tự động theo chi phí; và phạm vi mới giới hạn ở dữ liệu bảng có cấu trúc, chưa xử lý dữ liệu phi cấu trúc hay vector embeddings cho LLM.

---

## 2.5. Tầng 5 — Đường ống nạp dữ liệu huấn luyện ML: tf.data (PVLDB 2021)

### 2.5.1. Thông tin ấn phẩm và minh chứng chỉ mục
Bài báo *"tf.data: A Machine Learning Data Processing Framework"* do bốn tác giả Derek G. Murray, Jiří Šimša, Ana Klimovic và Ihor Indyk thực hiện tại Google, công bố tháng 8/2021 trên *Proceedings of the VLDB Endowment (PVLDB)*, Tập 14, Số 12, trang `2945–2958` (`ISSN: 2150-8097`, DOI: `10.14778/3476311.3476374`, bản preprint `arXiv:2101.12127v2`). Ấn phẩm thuộc Scopus Source ID `21100199855` (phân hạng Q1, CiteScore 7,5–8,2, h-index trên 200), lập chỉ mục trong Web of Science Core Collection (CPCI-S/ESCI) và đạt hạng CORE A\*.

### 2.5.2. Phân tích nội dung nghiên cứu cốt lõi
Phân tích đo đạc trên hàng triệu tác vụ huấn luyện học máy chạy thực tế trong một tháng tại trung tâm dữ liệu Google chỉ ra thực trạng đáng chú ý: 30% tổng thời gian tính toán bị tiêu tốn cho đường ống dữ liệu đầu vào (*input pipeline*), 20% số tác vụ dành hơn một phần ba tài nguyên chỉ để nạp dữ liệu, và 13% số tác vụ đọc trên 1 TB dữ liệu nhưng tiêu thụ tới hơn 96% tổng tài nguyên tính toán toàn cụm (Figures 1–2, §1–§2). Do GPU và TPU chuyên biệt cho đại số tuyến tính nhưng kém phù hợp với tiền xử lý trực tuyến (giải mã ảnh, tăng cường dữ liệu, xáo trộn, gom lô), CPU máy chủ dễ trở thành nút thắt khiến bộ tăng tốc bị nhàn rỗi (*input pipeline stalls*).

Hệ thống tf.data (tích hợp trong TensorFlow với hơn 15.000 dòng Python và 40.000 dòng C++) giải quyết bài toán này bằng hai trừu tượng tách biệt là `Dataset` (phi trạng thái, mô tả cây biểu thức ETL) và `Iterator` (có trạng thái), kết hợp ba lớp tối ưu hóa:
1. Lớp song song hóa và Software Pipelining (§3.2) sử dụng toán tử `interleave` để song song hóa I/O đọc tệp, `map(num_parallel_calls)` để song song hóa tiền xử lý CPU, `prefetch` để gối đầu truyền nạp dữ liệu với tính toán trên GPU/TPU, cùng tùy chọn thứ tự phi tất định giúp loại bỏ tắc nghẽn đầu hàng (*head-of-line blocking*, tăng tới khoảng 40% thông lượng trên ImageNet).
2. Lớp tối ưu hóa tĩnh bằng viết lại đồ thị (§3.3.1) biểu diễn cây biểu thức sang `GraphDef` để Grappler tự động gộp toán tử (`map + batch`, `map + map`, `shuffle + repeat`, `map + filter`) giảm chi phí gọi ảo, kết hợp kỹ thuật *Map Vectorization* chuyển `d.map(f).batch(b)` sang `d.batch(b).map(pfor(f))`.
3. Lớp tối ưu hóa động `AUTOTUNE` (§3.3.2) duy trì một luồng nền nhẹ theo dõi cây iterator và xây dựng mô hình giải tích ước lượng độ trễ đầu ra; các toán tử bất đồng bộ được mô hình hóa bằng hàng đợi M/M/1/k để tính xác suất bộ đệm rỗng $p_{\text{empty}}$, sau đó dùng thuật toán Gradient Descent định kỳ dưới ngân sách CPU/RAM để chọn cấu hình song song và bộ đệm tối ưu toàn cục trong micro giây đến mili giây.

Thực nghiệm trên bộ chuẩn MLPerf (năm mô hình gồm ResNet-50/ImageNet 140 GB, SSD và Mask-RCNN/COCO 19 GB, GNMT/WMT16 1,3 GB, Transformer/WMT17 720 MB) mang lại ba kết quả định lượng nổi bật. Trên máy chủ 56 nhân, tốc độ xử lý mỗi epoch tăng từ 2,7× (Mask-RCNN) đến 43,3× (ResNet-50) và 63,1× (SSD). Trên cụm 8×TPUv3, thời gian huấn luyện hội tụ đầu-cuối giảm trung bình 7,0× chỉ nhờ song song hóa và đạt đỉnh 21,0× (ResNet-50) cùng 22,0× (SSD) khi bật đủ tối ưu tf.data, trong đó `AUTOTUNE` sát cấu hình chuyên gia chỉnh tay trong phạm vi dưới 1% ở 4/5 bài chuẩn (và dưới 4% ở GNMT), triệt tiêu hoàn toàn nút thắt đầu vào. Trên máy Google Cloud `n2-standard-64` (ImageNet-ResNet50), tf.data thuần CPU đạt 110 giây/epoch — nhanh hơn 1,9× so với PyTorch DataLoader (213 giây), vượt xa NVIDIA DALI CPU (777 giây) và DALI + 1 GPU (172 giây), đồng thời tiệm cận DALI + 2 GPUs (107 giây) mà không chiếm dụng lõi GPU huấn luyện.

### 2.5.3. Hai hình minh họa tái tạo từ bài báo gốc

![Hình 2.10: Mô hình ước lượng độ trễ đầu ra của cơ chế AUTOTUNE trên cây Iterator — Tái tạo từ Figure 5 (PVLDB 2021)](<../../99 - Đính kèm (Attachments)/TV1_Bai5_Hinh1_Autotune_Model.png>)

Hình 2.10 tái tạo Figure 5 gốc (tr. 2951) minh họa cơ chế duyệt cây hai chiều của `AUTOTUNE`: lượt duyệt xuống tính tốc độ tiêu thụ $y$ (100 → 100 → 1000 → 1000 → 500 calls/s), lượt duyệt lên tính độ trễ đầu ra bằng hàm tuyến tính cho toán tử đồng bộ (`batch`: 36,5 ms) và công thức hàng đợi M/M/1/k $p_{\text{empty}}$ cho toán tử bất đồng bộ (`interleave`: 4,15 ms, `map`: 3,55 ms, `prefetch`: 27,0 ms), giúp tìm cấu hình tối ưu toàn cục mà không làm gián đoạn đường ống thật.

![Hình 2.11: Hệ số tăng tốc thời gian hội tụ huấn luyện đầu-cuối trên bộ chuẩn MLPerf — Tái tạo từ Figure 8 (PVLDB 2021)](<../../99 - Đính kèm (Attachments)/TV1_Bai5_Hinh2_MLPerf_Speedup.png>)

Hình 2.11 tái tạo Figure 8 gốc (tr. 2953) đối chiếu 15 giá trị số chính xác cho năm bài chuẩn MLPerf trên cụm 8×TPUv3, phân tách rõ nhóm bài toán thị giác máy tính (hưởng lợi gấp đôi từ tối ưu tĩnh và caching với ResNet-50 tăng từ 10,4× lên 21,0×, SSD tăng từ 17,9× lên 22,0×) và nhóm xử lý ngôn ngữ tự nhiên (GNMT 1,5×, Transformer 2,0×), khẳng định khả năng tự động hóa tiệm cận chuyên gia (sai khác dưới 1%) của `AUTOTUNE`.

### 2.5.4. Đánh giá và phản biện
Công trình của Google kết hợp xuất sắc giữa mô hình giải tích hàng đợi và thực chứng sản xuất ở quy mô hàng triệu tác vụ. Tuy vậy, chính phân tích toàn cụm (§5.1) phơi bày ba giới hạn lớn cho nghiên cứu kế tiếp: tf.data mới tối ưu cục bộ từng tác vụ nên chưa tự động chia sẻ dữ liệu đã tiền xử lý giữa nhiều tác vụ chạy lặp lại cùng một đường ống (ví dụ khi dò siêu tham số); có tới 75% số tác vụ có dung lượng đầu ra nhỏ hơn dữ liệu thô đọc từ lưu trữ, cho thấy vẫn còn lãng phí băng thông mạng do chưa đẩy được phép chiếu/lọc (*projection/filter pushdown*) xuống tầng lưu trữ; và tối ưu `map + batch fusion` chưa hỗ trợ chuỗi toán tử gom nhóm theo độ dài (`groupby`) đặc trưng của bài toán NLP/LLM.

---

# CHƯƠNG 3: PHÂN TÍCH LIÊN KẾT, SO SÁNH ĐỐI CHIẾU VÀ KIẾN TRÚC TÍCH HỢP NĂM TẦNG

## 3.1. Kiến trúc tích hợp năm tầng đề xuất và phân tích bốn cầu nối liên tầng

Trên cơ sở phân tích sâu năm công trình lõi giai đoạn 2020–2023, nghiên cứu đề xuất Kiến trúc Tích hợp Năm Tầng Đầu-Cuối (Hình 3.1) kết nối liền mạch từ hạ tầng lưu trữ đối tượng đám mây băng thông 100 Gbps đến cụm huấn luyện GPU/TPU, trong đó mỗi cặp tầng kế cận liên kết chặt chẽ qua một cầu nối kỹ thuật cụ thể.

![Hình 3.1: Sơ đồ Kiến trúc Tích hợp Năm Tầng Hạ tầng Quản trị Dữ liệu cho Học máy Quy mô lớn](<../../99 - Đính kèm (Attachments)/TV1_Hinh_KienTruc_TichHop_5Tang.png>)

1. Cầu nối giữa Tầng 1 (BtrBlocks) và Tầng 2 (Delta Lake) khai thác sự cộng hưởng trực tiếp từ thiết kế tách rời siêu dữ liệu (*orthogonal metadata*) của BtrBlocks với nhật ký `_delta_log` của Delta Lake, giúp loại bỏ 3 lượt HTTP GET đọc footer tuần tự của Parquet trên S3. Việc thay Parquet+Zstd/Snappy bằng BtrBlocks bên dưới các bảng Delta Lake giải phóng thông lượng mạng lên 86,2 Gbps (nhanh hơn 2,6×–3,5× và rẻ hơn 1,8×), tuy nhiên cần cơ chế định dạng lai vì thuật toán *Pseudodecimal* chưa tối ưu cho các cột vector embedding độ chính xác cao.
2. Cầu nối giữa Tầng 2 (Delta Lake) và Tầng 3 (Photon) thể hiện sự chuyển tiếp tự nhiên từ tối ưu I/O sang tối ưu CPU. Delta Lake cung cấp snapshot nhất quán ACID và cắt giảm mạnh lượng tệp đọc nhờ Data Skipping cùng Z-Order, tạo đúng điều kiện để động cơ C++ vector hóa Photon phát huy sức mạnh qua `OffHeapColumnVector` (Zero-copy JNI khoảng 23 ns). Ở chiều ngược lại, Photon tăng tốc 2× quá trình ghi tệp Parquet mới cho các lệnh `INSERT`, `MERGE` và `OPTIMIZE` của Delta Lake.
3. Cầu nối giữa Tầng 3 (Photon) và Tầng 4 (FeathrPO) kết hợp tối ưu kế hoạch logic ở lớp đặc trưng với tốc độ thực thi vật lý cấp thấp. FeathrPO tối ưu kế hoạch và bố cục phân vùng cho phép ghép *Point-in-Time Join* đa bảng bằng KLL sketches, *Semijoin Reduction* và BIP, trong khi Photon tăng tốc trực tiếp các toán tử hash join, lọc và tổng hợp cột sinh ra từ kế hoạch đã viết lại, qua đó khắc phục nút thắt CPU/JVM vốn còn tồn đọng khi FeathrPO chạy trên Spark mặc định.
4. Cầu nối giữa Tầng 4 (FeathrPO) và Tầng 5 (tf.data) khép kín đường ống dữ liệu từ kho đặc trưng đến bộ tăng tốc huấn luyện. FeathrPO đảm bảo tính đúng đắn thời gian và loại bỏ rò rỉ dữ liệu cho tập đặc trưng ngoại tuyến xuất ra kho lưu trữ, còn tf.data tiếp nhận trực tiếp tập dữ liệu này để thực hiện tiền xử lý trực tuyến (*shuffling, augmentation, batching, prefetching*) và tự động tinh chỉnh bằng `AUTOTUNE`, đảm bảo GPU/TPU luôn vận hành ở mức bão hòa mà không bị nghẽn đầu vào.

## 3.2. Ma trận so sánh đa chiều năm công trình nền tảng

Bảng dưới đây đối chiếu toàn diện cả năm công trình nền tảng theo tám tiêu chí học thuật và kỹ thuật xuyên suốt từ tầng lưu trữ vật lý đến tầng nạp dữ liệu huấn luyện học máy.

| Tiêu chí so sánh | Tầng 1: BtrBlocks (SIGMOD 2023) | Tầng 2: Delta Lake (PVLDB 2020) | Tầng 3: Photon (SIGMOD 2022) | Tầng 4: FeathrPO (PVLDB 2023) | Tầng 5: tf.data (PVLDB 2021) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Tác giả & Tổ chức | Kuschewski et al. (TU Munich, FAU) | Armbrust et al. (Databricks, UCB, Stanford, CWI) | Behm et al. (Databricks, UCB) | Liu et al. (Microsoft Gray Systems Lab) | Murray et al. (Google) |
| Ấn phẩm & Xếp hạng | ACM SIGMOD 2023 (*PACMMOD*), WoS ESCI, CORE A\* | PVLDB 2020 (Vol. 13, No. 12), Scopus Q1, WoS, CORE A\* | ACM SIGMOD 2022 (*Best Industry Paper*), Scopus, WoS CPCI-S, CORE A\* | PVLDB 2023 (Vol. 16, No. 13), Scopus Q1, WoS, CORE A\* | PVLDB 2021 (Vol. 14, No. 12), Scopus Q1, WoS, CORE A\* |
| Nút thắt giải quyết | Parquet giải nén chậm, nghẽn CPU khi quét Data Lake trên mạng 100 Gbps | Cloud Object Store thiếu ACID, hỏng dữ liệu khi ghi lỗi, tệp nhỏ và LIST chậm | Overhead JVM/GC (>64 GB heap) và JIT bailout của Spark trên SQL/ETL | Point-in-Time Join chậm, shuffle lớn và tính toán lặp trong Feature Store | Nghẽn I/O và tiền xử lý CPU làm GPU/TPU bị nhàn rỗi khi huấn luyện |
| Kiến trúc & Kỹ thuật cốt lõi | Nén đệ quy ≤ 3 tầng, lấy mẫu `10×64` (1%), *Pseudodecimal*, *FSST*, SIMD AVX2, tách rời metadata | Nhật ký `_delta_log` (JSON + Parquet checkpoint), OCC, *Data Skipping*, *Z-Order*, *Time Travel*, Batch+Stream | Engine C++ vector hóa thuần túy (SIMD), *Column Batch + Position List*, *Adaptive Join Compaction*, Zero-copy JNI | Mô hình chi phí *KLL sketches*, viết lại tái sử dụng (*Matcher/Rewriter*), *Semijoin*, chọn bố cục BIP (OR-Tools) | API khai báo `Dataset`/`Iterator`, tối ưu tĩnh Grappler (*fusion/vectorization*), động `AUTOTUNE` (M/M/1/k + GD) |
| Dữ liệu & Benchmark | Public BI Benchmark (43 bảng, 2.451 cột, 119,5 GB) trên AWS `c5n.18xlarge` + S3 | TPC-DS 1 TB Power Test (AWS 1+8 `i3.2xlarge`) và workload exabyte sản xuất | Vi chuẩn, TPC-H SF=3000 (1+8 nút), TPC-DS 100 TB kiểm toán (256 nút AWS) | TPCx-AI UC7 & UC10 (SF1–SF100), Kaggle Favorita & eCommerce (Azure Synapse) | 5 mô hình MLPerf trên 8×TPUv3, đối chứng PyTorch/DALI và hàng triệu job Google |
| Chỉ số đánh giá chính | Thông lượng nén $T_c$ (Gbps), $T_u$ (GB/s), số lượt quét S3 / USD | Thời gian chạy TPC-DS (giờ), tỷ lệ bỏ qua tệp, thông lượng | Thời gian chạy (s/ms), Speedup vs DBR, JNI overhead (%), dung lượng shuffle | Hệ số cải thiện (*Factor of Improvement*), độ chính xác KLL (%), thời gian giải BIP | Hệ số tăng tốc epoch và hội tụ đầu-cuối (×), thời gian/epoch (s) vs DataLoader/DALI |
| Kết quả định lượng nổi bật | $T_c = 86,2\text{ Gbps}$ (2,6×–3,5× Parquet+Snappy/Zstd), rẻ hơn 1,8× (`$0,97` vs `$1,70–$1,74`) | Nhanh hơn 1,55× Spark Parquet (0,93 h vs 1,44 h) và 4,04× Presto (3,76 h) | Trung bình 4,0× TPC-H (đỉnh 23× Q1); kỷ lục TPC-DS 100 TB; 1,55× Q24; JNI chỉ 0,06% | Tăng tốc 1,4×–3,00× (đỉnh 3,00× UC10 Cloud); KLL chính xác 96,84%–99,73%; giải BIP 6–7 s | Tăng tốc đầu-cuối 7,0× TB, đỉnh 21,0× (ResNet-50) và 22,0× (SSD); `AUTOTUNE` sát chuyên gia ≤ 1%; nhanh 1,9× DataLoader |
| Hạn chế chính | Rào cản hệ sinh thái Parquet; hạn chế *point lookup*; phụ thuộc AVX2; chưa đo trong SQL engine | Độ trễ ghi bị giới hạn bởi chu kỳ commit JSON và xung đột OCC; phụ thuộc tệp Parquet cũ | Mã nguồn đóng Databricks; chưa hỗ trợ Sort-Merge Join; fallback về JVM với UDF Python | Can thiệp ở tầng logic Spark JVM; vật chất hóa thủ công; mới hỗ trợ dữ liệu bảng | Chưa tự động chia sẻ cache liên tác vụ mặc định; chưa đẩy lọc/chiếu xuống tầng lưu trữ; hạn chế fusion với `groupby` |

## 3.3. Tổng hợp định lượng hiệu năng năm tầng và giao thức kiểm chứng đầu-cuối

Để đặt kết quả định lượng của năm công trình rời rạc trên cùng một hệ quy chiếu trực quan, báo cáo xây dựng Biểu đồ Tổng hợp Định lượng Năm Tầng (Hình 3.2), đối chiếu đồng thời hệ số cải thiện (*Speedup*, trục logarit) và tỷ lệ cắt giảm thời gian thực thi tương ứng $\% \text{ Time Saved} = (1 - 1/\text{Speedup}) \times 100\%$.

![Hình 3.2: Tổng hợp định lượng hiệu quả cải thiện xuyên suốt năm tầng kiến trúc Lakehouse cho học máy](<../../99 - Đính kèm (Attachments)/Hinh_TongHop_HieuNang_5Tang.png>)

| Tầng kiến trúc | Công trình & Phạm vi đo | Hệ số cải thiện | Tỷ lệ giảm thời gian | Đối chứng (1,0×) & Môi trường thực nghiệm |
| :--- | :--- | :---: | :---: | :--- |
| Tầng 1 | BtrBlocks (Public BI — Quét S3) | 2,22× ($T_c$: 3,48×) | −55,0% | Băng thông giải nén $T_u$ (174,6 vs 78,6 GB/s) so với Parquet+Zstd trên AWS `c5n.18xlarge` (100 Gbps) |
| Tầng 2 | Delta Lake (TPC-DS 1 TB Power) | 1,55× (4,04× vs Presto) | −35,5% | Thời gian chạy (0,93 h) so với 3rd-Party Spark Parquet (1,44 h), cụm AWS `1+8 i3.2xlarge` |
| Tầng 3 | Photon (TPC-DS Q24 — Adaptive) | 1,55× | −35,5% | Truy vấn Q24 (76 s vs 118 s) so với DBR Spark Code-Gen, cụm 16 nút |
| Tầng 3 | Photon (TPC-H SF=3000 — 22 câu) | 4,00× (đỉnh 23× Q1) | −75,0% | Trung bình theo từng truy vấn trên 22 câu TPC-H SF=3000 so với DBR trên Delta Lake/S3 |
| Tầng 4 | FeathrPO (TPCx-AI UC10 — Cận trên\*) | tới 3,00× | tới −66,7% | Tối ưu PIT Join so với Feathr mặc định trên Azure Synapse Spark (2,50× với Union Merge) |
| Tầng 5 | tf.data (MLPerf — TB 5 mô hình) | 7,00× | −85,7% | Thời gian hội tụ đầu-cuối khi bật song song hóa và pipelining so với đọc tuần tự trên `8×TPUv3` |
| Tầng 5 | tf.data (MLPerf — ResNet-50 / SSD\*) | 21,00× (SSD 22,0×) | −95,2% | Tổng tăng tốc hội tụ đầu-cuối khi bật đầy đủ tối ưu và `AUTOTUNE` so với đường ống tuần tự |

Về nguyên tắc liêm chính phương pháp luận, cần nhấn mạnh rằng tuyệt đối không được xếp hạng tuyệt đối hay cộng, nhân các hệ số tăng tốc giữa năm tầng để suy diễn tốc độ đầu-cuối, bởi mỗi công trình đo trên bộ chuẩn, cụm phần cứng và mốc đối chứng 1,0× khác nhau, đồng thời bị chi phối chặt chẽ bởi Định luật Amdahl và sự chồng lấn chi phí giữa các tầng. Để kiểm chứng thực nghiệm công bằng trong nghiên cứu tiếp theo, báo cáo đề xuất Giao thức Kiểm chứng Năm Bước Tăng dần trên cùng tập dữ liệu, cùng truy vấn và cùng cụm phần cứng (tách bạch *cold cache* và *warm cache*, báo cáo trung vị và phân vị P95): bắt đầu từ cấu hình cơ sở Spark + Parquet tuần tự; lần lượt kích hoạt Tầng 2 (Delta Lake Data Skipping + Z-Order), Tầng 3 (Photon C++), Tầng 4 (FeathrPO cho PIT Join tạo tập huấn luyện) và Tầng 5 (tf.data `AUTOTUNE` nạp trực tiếp vào GPU/TPU); riêng nhánh thay Parquet bằng BtrBlocks ở Tầng 1 được kiểm thử độc lập sau khi tích hợp lớp đọc/ghi tương thích siêu dữ liệu `_delta_log`.

---

# CHƯƠNG 4: PHẢN BIỆN CHÉO, KHOẢNG TRỐNG NGHIÊN CỨU VÀ HƯỚNG PHÁT TRIỂN

Chương 4 tổng hợp phản biện liên tầng xuyên suốt cả năm công trình nền tảng nhằm giải đáp trực tiếp câu hỏi nghiên cứu RQ3.

## 4.1. Phân tích các sự đánh đổi xuyên suốt năm tầng kiến trúc

Khi tích hợp đồng thời năm công trình nền tảng vào một hạ tầng quản trị dữ liệu duy nhất trên Cloud Object Storage, kiến trúc tổng thể buộc phải cân bằng năm cặp đánh đổi kỹ thuật cốt lõi được hệ thống hóa trong bảng sau.

| Cặp tầng liên kết | Sự đánh đổi (Trade-off) | Phân tích kỹ thuật chuyên sâu |
| :--- | :--- | :--- |
| Tầng 1 (BtrBlocks) ↔ Tầng 2 (Delta Lake) | Tốc độ giải nén tối đa vs. Độ phổ cập chuẩn mở | Delta Lake dựa vào Parquet để đảm bảo tương thích đa công cụ nhưng Parquet giải nén chậm trên mạng 100 Gbps; BtrBlocks giải nén vượt trội nhờ nén đệ quy SIMD nhưng thay thế trực tiếp sẽ phá vỡ tính tương thích hệ sinh thái hiện hữu. |
| Tầng 2 (Delta Lake) ↔ Tầng 3 (Photon) | Tính nhất quán ACID chặt vs. Độ trễ ghi thời gian thực | Nhật ký `_delta_log` và kiểm soát OCC đảm bảo ACID cùng Time Travel nhưng tạo chi phí kiểm tra/gộp metadata và nguy cơ xung đột ghi khi có nhiều luồng cập nhật nhỏ liên tục. |
| Tầng 3 (Photon) ↔ Tầng 4 (FeathrPO) | Tốc độ Vectorized C++/SIMD vs. Tính linh hoạt UDF Python/ML | Photon tăng tốc mạnh các toán tử SQL chuẩn bằng mã máy C++, nhưng các phép biến đổi đặc trưng trong Feature Store thường chứa UDF Python/PyTorch, dễ buộc động cơ rơi về luồng JVM chậm và gánh chi phí tuần tự hóa bộ nhớ. |
| Tầng 4 (FeathrPO) ↔ Hạ tầng Object Store | Tính toán sẵn (Pre-computation) vs. Chi phí lưu trữ & Độ tươi dữ liệu | Vật chất hóa sẵn bảng đặc trưng giúp rút ngắn thời gian tạo tập huấn luyện nhưng phình to dung lượng lưu trữ và dễ lỗi thời; ngược lại tính động bằng PIT Join mỗi lần huấn luyện lại tốn chu kỳ CPU nếu thiếu tái sử dụng. |
| Tầng 4 (FeathrPO) ↔ Tầng 5 (tf.data) & GPU/TPU | Tiền xử lý trực tuyến linh hoạt vs. Băng thông mạng & Tính lặp lại liên tác vụ | Tiền xử lý trực tuyến (*augmentation, shuffling*) trong tf.data tránh phình dung lượng đĩa và giữ GPU/TPU luôn bận nhờ `AUTOTUNE`, nhưng buộc phải đọc lại toàn bộ dữ liệu thô qua mạng (75% job giảm dung lượng sau xử lý) và lặp lại tính toán giữa các lần chạy dò siêu tham số. |

## 4.2. Tổng hợp khoảng trống nghiên cứu liên tầng

Từ năm cặp đánh đổi nêu trên, nghiên cứu đúc kết bốn khoảng trống khoa học liên tầng còn bỏ ngỏ trong bức tranh tổng thể hiện nay:

1. Thiếu bộ tối ưu hóa dựa trên chi phí xuyên tầng (*Lack of Cross-layer Cost-based Optimization*), bởi cả năm công trình hiện mới tối ưu cục bộ trong ranh giới tầng riêng — BtrBlocks ở mức khối nén, Delta Lake ở mức metadata tệp, Photon ở toán tử SQL C++, FeathrPO ở kế hoạch logic PIT Join và tf.data ở cây iterator đơn máy. Toàn hệ thống vẫn thiếu một lớp tối ưu thống nhất có thể truyền ngữ nghĩa (như độ chọn lọc thực thể, vòng đời TTL và danh sách cột thực dùng) từ tầng học máy xuống thẳng tầng bố cục bảng và tầng giải mã tệp.
2. Tồn tại điểm nghẽn sao chép bộ nhớ giữa động cơ thực thi C++ và môi trường học máy Python. Dù Photon loại bỏ thành công chi phí JVM cho tầng truy vấn SQL, việc luân chuyển dữ liệu đặc trưng từ Lakehouse vào các framework học sâu (TensorFlow, PyTorch) vẫn gặp nút thắt tuần tự hóa và sao chép bộ nhớ qua lại giữa C++ và Python do thiếu chuẩn trao đổi *Zero-copy* (như Apache Arrow Flight hay DLPack) xuyên suốt toàn đường ống.
3. Phát sinh lãng phí băng thông mạng và tái thực thi tính toán giữa nhiều tác vụ học máy. Phát hiện thực nghiệm của tf.data trên hàng triệu tác vụ tại Google cho thấy 75% tác vụ làm giảm dung lượng dữ liệu sau tiền xử lý và các đường ống giống hệt nhau bị chạy lại rất nhiều lần, nhưng hạ tầng hiện tại vẫn thiếu cơ chế đẩy phép chiếu/lọc (*projection/filter pushdown*) xuống gần tầng lưu trữ và thiếu dịch vụ bộ nhớ đệm vật chất hóa chia sẻ liên tác vụ (*cross-job caching*).
4. Thiếu chuẩn đánh giá hiệu năng đầu-cuối thống nhất (*Lack of End-to-End Unified Benchmark*). Năm công trình hiện đang đo trên các hệ quy chiếu rời rạc (Public BI, TPC-DS, TPC-H, TPCx-AI, MLPerf); cộng đồng vẫn chưa có một bộ chuẩn thống nhất đo thông lượng trọn vẹn từ khi đọc khối nén trên Object Storage tới thời điểm nạp tensor vào GPU/TPU hội tụ mô hình.

## 4.3. Đề xuất hướng nghiên cứu mới

Trên cơ sở các khoảng trống đã nhận diện, nghiên cứu đề xuất hai hướng mở rộng trọng tâm có giá trị học thuật và tính ứng dụng cao:

1. Hướng thứ nhất là tự động tối ưu hóa ngữ nghĩa xuyên năm tầng cho hạ tầng *AI-Ready Lakehouse* (*Cross-layer Semantic Optimization*). Nghiên cứu này thiết kế giao thức truyền gợi ý ngữ nghĩa từ tf.data và FeathrPO (tập cột cần thiết, khóa thực thể, cửa sổ thời gian, tần suất tái sử dụng) xuống thẳng Delta Lake để tự động cấu hình Z-Order/Partitioning và xuống BtrBlocks để chọn lược đồ nén phù hợp từng loại đặc trưng, kết hợp đẩy phép chiếu dữ liệu xuống sát tầng lưu trữ và xây dựng dịch vụ bộ nhớ đệm chia sẻ liên tác vụ (*disaggregated caching service*).
2. Hướng thứ hai là hỗ trợ nguyên bản dữ liệu đa phương thức và vector embeddings cho kỷ nguyên AI/LLM. Kiến trúc năm tầng cần được mở rộng để lưu trữ nguyên bản dữ liệu phi cấu trúc (ảnh, văn bản, âm thanh) cùng vector nhúng độ chính xác thấp (`FP16`, `BF16`, quantized vectors) trong bảng giao dịch ACID của Lakehouse, tích hợp chỉ mục tìm kiếm vector gần đúng (ANN) vào động cơ vector hóa C++ và bổ sung toán tử `map + groupby + batch fusion` cho đường ống nạp chuỗi văn bản phục vụ truy xuất tăng cường (RAG) và tinh chỉnh mô hình ngôn ngữ lớn.

---

# CHƯƠNG 5: KẾT LUẬN VÀ TÀI LIỆU THAM KHẢO

## 5.1. Kết luận tổng quát

Thông qua việc thẩm định uy tín học thuật, phân tích chuyên sâu, tự lập trình tái lập 10 hình minh họa gốc cùng 03 hình tổng hợp/đề xuất mới và phản biện liên tầng năm công trình hàng đầu thế giới giai đoạn 2020–2023 (*BtrBlocks*, *Delta Lake*, *Photon*, *FeathrPO*, *tf.data*), báo cáo đã hoàn thành mục tiêu đặt ra và giải đáp trọn vẹn ba câu hỏi nghiên cứu:
- Đối với câu hỏi nghiên cứu RQ1 về sự dịch chuyển điểm nghẽn, khi hạ tầng đám mây nâng cấp lên mạng 100 Gbps và bộ tăng tốc GPU/TPU, nút thắt hiệu năng dịch chuyển liên hoàn từ khâu giải nén tệp cột (Parquet) sang tính nhất quán giao dịch và I/O bảng, tiếp đến là chi phí CPU/JVM, phép ghép chuỗi thời gian PIT Join và cuối cùng là nghẽn đường ống nạp dữ liệu đầu vào.
- Đối với câu hỏi nghiên cứu RQ2 về cơ chế bổ trợ năm tầng, năm công trình tạo thành một chỉnh thể kiến trúc khép kín: *BtrBlocks* tối ưu giải nén SIMD tách rời metadata; *Delta Lake* thiết lập trục ACID và Data Skipping; *Photon* giải phóng tốc độ thực thi C++ trên bảng mở; *FeathrPO* ngăn rò rỉ dữ liệu và tái sử dụng đặc trưng; và *tf.data* tự động hóa song song hóa nạp dữ liệu vào GPU/TPU sát ngưỡng phần cứng.
- Đối với câu hỏi nghiên cứu RQ3 về đánh đổi và hướng phát triển, việc tích hợp đồng thời năm tầng đòi hỏi cân bằng năm cặp đánh đổi kỹ thuật cốt lõi và mở ra hai hướng nghiên cứu giàu tiềm năng gồm tối ưu hóa ngữ nghĩa xuyên tầng kèm chia sẻ bộ nhớ đệm liên tác vụ, cùng khả năng hỗ trợ nguyên bản dữ liệu đa phương thức và vector embeddings cho kỷ nguyên AI/LLM.

## 5.2. Danh mục tài liệu tham khảo (Chuẩn IEEE)

[1] M. Kuschewski, D. Sauerwein, A. Alhomssi, and V. Leis, "BtrBlocks: Efficient Columnar Compression for Data Lakes," *Proc. ACM Manag. Data (PACMMOD)*, vol. 1, no. 2, Art. 118, pp. 118:1–118:26, Jun. 2023, doi: `10.1145/3589263`.

[2] M. Armbrust, T. Das, L. Sun, B. Yavuz, S. Zhu, M. Murthy, J. Torres, H. van Hövell, A. Ionescu, A. Łuszczak, M. Świtakowski, M. Szafrański, X. Li, T. Ueshin, M. Mokhtar, P. Boncz, A. Ghodsi, S. Paranjpye, P. Senster, R. Xin, and M. Zaharia, "Delta Lake: High-Performance ACID Table Storage over Cloud Object Stores," *Proc. VLDB Endow.*, vol. 13, no. 12, pp. 3411–3424, Aug. 2020, doi: `10.14778/3415478.3415560`.

[3] A. Behm, S. Palkar, U. Agarwal, T. Armstrong, D. Cashman, A. Dave, T. Greenstein, S. Hovsepian, R. Johnson, A. S. Krishnan, P. Leventis, A. Luszczak, P. Menon, M. Mokhtar, G. Pang, S. Paranjpye, G. Rahn, B. Samwel, T. van Bussel, H. van Hovell, M. Xue, R. Xin, and M. Zaharia, "Photon: A Fast Query Engine for Lakehouse Systems," in *Proc. 2022 ACM SIGMOD Int. Conf. Management of Data (SIGMOD '22)*, Philadelphia, PA, USA, Jun. 2022, pp. 2326–2339, doi: `10.1145/3514221.3526054`.

[4] R. Liu, K. Park, F. Psallidas, X. Zhu, R. Sen, M. Interlandi, Y. Tian, J. Camacho-Rodríguez, J. Mo, and K. Karanasos, "Optimizing Data Pipelines for Machine Learning in Feature Stores," *Proc. VLDB Endow.*, vol. 16, no. 13, pp. 4230–4239, Aug. 2023, doi: `10.14778/3625054.3625060`.

[5] D. G. Murray, J. Šimša, A. Klimovic, and I. Indyk, "tf.data: A Machine Learning Data Processing Framework," *Proc. VLDB Endow.*, vol. 14, no. 12, pp. 2945–2958, Aug. 2021, doi: `10.14778/3476311.3476374`.

[6] M. Armbrust, R. S. Xin, C. Lian, Y. Huai, D. Liu, J. K. Bradley, X. Meng, T. Kaftan, M. J. Franklin, A. Ghodsi, and M. Zaharia, "Spark SQL: Relational Data Processing in Spark," in *Proc. 2015 ACM SIGMOD Int. Conf. Management of Data*, Melbourne, Australia, May 2015, pp. 1383–1394, doi: `10.1145/2723372.2742797`.

[7] P. A. Boncz, T. Neumann, and V. Leis, "FSST: Fast Random Access String Compression," *Proc. VLDB Endow.*, vol. 13, no. 11, pp. 2649–2661, Jul. 2020.

[8] D. Abadi, P. A. Boncz, S. Harizopoulos, S. Idreos, and S. Madden, "The Design and Implementation of Modern Column-Oriented Database Systems," *Foundations and Trends in Databases*, vol. 5, no. 3, pp. 197–280, 2013.

[9] P. A. Boncz, M. Zukowski, and N. Nes, "MonetDB/X100: Hyper-Pipelining Query Execution," in *Proc. 2nd Biennial Conf. Innovative Data Systems Research (CIDR)*, Asilomar, CA, USA, Jan. 2005, pp. 225–237.

[10] T. Kersten, V. Leis, A. Kemper, T. Neumann, A. Pavlo, and P. Boncz, "Everything You Always Wanted to Know About Compiled and Vectorized Queries But Were Afraid to Ask," *Proc. VLDB Endow.*, vol. 11, no. 13, pp. 2209–2222, Sep. 2018, doi: `10.14778/3275366.3275370`.

[11] D. Lemire and L. Boytsov, "Decoding billions of integers per second through vectorization," *Software: Practice and Experience*, vol. 45, no. 1, pp. 1–29, 2015.

[12] P. Mattson, C. Cheng, G. Diamos, C. Coleman, P. Micikevicius, D. Patterson, et al., "MLPerf Training Benchmark," in *Proc. Machine Learning and Systems (MLSys)*, vol. 2, pp. 336–349, 2020.

[13] M. Abadi, P. Barham, J. Chen, Z. Chen, A. Davis, J. Dean, et al., "TensorFlow: A System for Large-Scale Machine Learning," in *Proc. 12th USENIX Symp. Operating Systems Design and Implementation (OSDI)*, 2016, pp. 265–283.

[14] M. Armbrust, A. Ghodsi, R. Xin, and M. Zaharia, "Lakehouse: A New Generation of Open Platforms that Unify Data Warehousing and Advanced Analytics," in *Proc. 11th Conf. Innovative Data Systems Research (CIDR)*, Jan. 2021.

---

# PHỤ LỤC: DANH MỤC VÀ BỘ SƯU TẬP HÌNH ẢNH

Phụ lục tổng hợp đầy đủ danh mục và bộ sưu tập trực quan hóa toàn bộ 14 hình ảnh khoa học được tự lập trình bằng Python (`matplotlib`, độ phân giải 300 DPI kèm bản vector PDF) phục vụ báo cáo cuối kỳ.

## A.1. Danh mục tổng hợp toàn bộ hình ảnh trong báo cáo

| STT | Ký hiệu | Tên hình ảnh | Công trình / Phạm vi | Tệp ảnh & Mã nguồn |
| :-: | :--- | :--- | :--- | :--- |
| 1 | Hình 2.1 | Cây quyết định nén đệ quy đa tầng của BtrBlocks (Figure 3) | BtrBlocks (SIGMOD 2023) | `BtrBlocks_Hinh1_TaiTao_CayQuyetDinhNen.png` |
| 2 | Hình 2.2 | Thông lượng quét S3 và chi phí quét so với Apache Parquet (Figure 1) | BtrBlocks (SIGMOD 2023) | `BtrBlocks_Hinh2_TaiTao_S3ScanBenchmark.png` |
| 3 | Hình 2.3 | Kiến trúc đường ống tích hợp dữ liệu Medallion trên Delta Lake (Figure 1) | Delta Lake (PVLDB 2020) | `Hinh1_TaiTao_KienTruc_Pipeline.png` |
| 4 | Hình 2.4 | So sánh thời gian thực thi TPC-DS 1 TB Power Test (Figure 6) | Delta Lake (PVLDB 2020) | `Hinh2_TaiTao_TPCDS_PowerTest.png` |
| 5 | Hình 2.5 | Biểu đồ đề xuất hệ số tăng tốc và tỷ lệ thời gian tiết kiệm của Delta Lake | Delta Lake (Đề xuất mới) | `Hinh3_DeXuatMoi_HeSoTangToc.png` |
| 6 | Hình 2.6 | Kiến trúc tầng thực thi Databricks Runtime và động cơ Photon (Figure 1) | Photon (SIGMOD 2022) | `TV3_Hinh1_KienTruc_Photon.png` |
| 7 | Hình 2.7 | Tác động của Adaptive Join Compaction trên TPC-DS Q24 (Figure 9) | Photon (SIGMOD 2022) | `TV3_Hinh2_TPCDS_Q24.png` |
| 8 | Hình 2.8 | Kiến trúc tích hợp các module tối ưu mới của FeathrPO (Figure 8) | FeathrPO (PVLDB 2023) | `Hinh_TV4_1_KienTruc_FeathrPO.png` |
| 9 | Hình 2.9 | Hệ số cải thiện hiệu năng FeathrPO trên 4 tập dữ liệu (Figure 12) | FeathrPO (PVLDB 2023) | `Hinh_TV4_2_HieuNang_FeathrPO.png` |
| 10 | Hình 2.10 | Mô hình ước lượng độ trễ đầu ra của AUTOTUNE trên cây Iterator (Figure 5) | tf.data (PVLDB 2021) | `TV1_Bai5_Hinh1_Autotune_Model.png` |
| 11 | Hình 2.11 | Hệ số tăng tốc thời gian hội tụ huấn luyện trên MLPerf (Figure 8) | tf.data (PVLDB 2021) | `TV1_Bai5_Hinh2_MLPerf_Speedup.png` |
| 12 | Hình 3.1 | Sơ đồ Kiến trúc Tích hợp Năm Tầng Hạ tầng Quản trị Dữ liệu cho Học máy | Tích hợp 5 tầng (Đề xuất) | `TV1_Hinh_KienTruc_TichHop_5Tang.png` |
| 13 | Hình 3.2 | Tổng hợp định lượng hiệu quả cải thiện xuyên suốt năm tầng kiến trúc | Tích hợp 5 tầng (Đề xuất) | `Hinh_TongHop_HieuNang_5Tang.png` |
| 14 | Hình A.1 | Bản đối chiếu tổng hợp định lượng 4 tầng Lakehouse cốt lõi (Bổ sung) | Tổng hợp 4 tầng cốt lõi | `TV3_Hinh3_TongHop_HieuNang.png` |

## A.2. Bộ sưu tập đối chiếu hình ảnh trực quan hóa (300 DPI)

<!-- APPENDIX_GALLERY -->

