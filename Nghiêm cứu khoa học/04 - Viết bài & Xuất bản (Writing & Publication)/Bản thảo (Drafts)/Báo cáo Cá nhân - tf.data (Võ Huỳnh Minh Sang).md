# BÁO CÁO PHÂN TÍCH CÁ NHÂN — BÀI BÁO THỨ 5 (MỤC 2.5 — CUỐI KỲ)

**Cơ sở đào tạo:** Trường Đại học Sài Gòn – Khoa Công nghệ Thông tin  
**Học phần:** Phương pháp Nghiên cứu Khoa học trong Công nghệ Thông tin  
**Đề tài nhóm:** *Hạ tầng quản trị dữ liệu hiện đại cho Học máy quy mô lớn: Liên kết Định dạng Lưu trữ Cột, Kiến trúc Data Lakehouse, Thực thi Vector hóa, Feature Store và Đường ống Nạp dữ liệu Huấn luyện* *(Đề tài C — 05 Bài báo)*  
**Phần phụ trách (Tầng 5 — Bài báo số 5):** Phân tích và Trực quan hóa bài báo *"tf.data: A Machine Learning Data Processing Framework"*  
**Sinh viên thực hiện:** Võ Huỳnh Minh Sang *(TV1 — Nhóm trưởng)* | **Lớp:** `DCT123C4` | **MSSV:** `3123411256`  
**Giảng viên hướng dẫn:** Vũ Ngọc Thanh Sang  
**Ngày hoàn thiện:** 2026-11-26  

---

# PHẦN 1: THÔNG TIN VÀ MINH CHỨNG NGUỒN BÀI BÁO

### 1. Tên bài báo (Paper Title)
- **Tiếng Anh:** *tf.data: A Machine Learning Data Processing Framework*
- **Dịch nghĩa tiếng Việt:** *tf.data: Một khung xử lý dữ liệu đầu vào cho Học máy*

### 2. Danh sách tác giả & Cơ quan công tác (Authors & Affiliations)
Công trình được thực hiện bởi nhóm 04 nhà nghiên cứu hệ thống dữ liệu và học máy tại **Google** (ghi chú trong bản in gốc: toàn bộ nghiên cứu được thực hiện trong thời gian công tác tại Google):
- **Derek G. Murray** — Microsoft *(thực hiện nghiên cứu tại Google)*.
- **Jiří Šimša** — Google.
- **Ana Klimovic** — ETH Zurich *(thực hiện nghiên cứu tại Google)*.
- **Ihor Indyk** — Google.

### 3. Tên tạp chí / Kỷ yếu hội nghị (Journal / Proceedings)
- **Tên chính thức:** *Proceedings of the VLDB Endowment (PVLDB)*
- **Nhà xuất bản:** VLDB Endowment & Association for Computing Machinery (ACM)
- **Mã số tiêu chuẩn quốc tế (ISSN):** `2150-8097`
- **Quy cách xuất bản:** Tập 14 (Volume 14), Số 12 (Issue 12), Tháng 8/2021, Trang `2945 – 2958` (trình bày tại Hội nghị Quốc tế VLDB lần thứ 47).

### 4. Năm công bố (Year of Publication)
- **Năm công bố chính thức:** **2021** (bản preprint `arXiv:2101.12127v2` ngày 23/02/2021; xuất bản chính thức trên PVLDB Vol. 14, No. 12 tháng 8/2021).

### 5. DOI & Đường dẫn chính thức
- **Mã định danh số (DOI):** [`10.14778/3476311.3476374`](https://doi.org/10.14778/3476311.3476374)
- **Đường dẫn chính thức trên VLDB Endowment:** [https://www.vldb.org/pvldb/vol14/p2945-murray.pdf](https://www.vldb.org/pvldb/vol14/p2945-murray.pdf)
- **Đường dẫn arXiv:** [https://arxiv.org/abs/2101.12127](https://arxiv.org/abs/2101.12127)
- **Bản PDF lưu trữ trong Vault:** [tfdata-PVLDB2021.pdf](<../../01 - Tổng quan tài liệu (Literature Review)/Bài báo đã đọc (Papers)/tfdata-PVLDB2021.pdf>)

### 6. Minh chứng thuộc danh mục Scopus, Web of Science (WoS) & CORE
- **Scopus (Elsevier):** Ấn phẩm *Proceedings of the VLDB Endowment* được lập chỉ mục liên tục từ năm 2008 đến nay tại hồ sơ nguồn **Scopus Source ID: `21100199855`**, gắn mã **ISSN `2150-8097`** ([Scopus Source Details](https://www.scopus.com/sourceid/21100199855)).
- **Web of Science (Clarivate):** Nguồn được xác thực trên cổng *Clarivate Master Journal List* ([https://mjl.clarivate.com](https://mjl.clarivate.com)) qua mã `ISSN 2150-8097`, thuộc *Web of Science Core Collection* (nhóm CPCI-S và ESCI).
- **Xếp hạng học thuật CORE & SJR:** Đạt hạng **CORE A\*** (cấp cao nhất ngành Cơ sở dữ liệu & Hệ thống dữ liệu lớn) và phân hạng **Q1** trên [ScimagoJR](https://www.scimagojr.com/journalsearch.php?q=21100199855&tip=sid) ở cả ba chuyên ngành *Information Systems*, *Software* và *Hardware and Architecture* (CiteScore khoảng `7.5 – 8.2`, h-index ấn phẩm `> 200`).

---

# PHẦN 2 (MỤC 2.5): PHÂN TÍCH NỘI DUNG NGHIÊN CỨU — TF.DATA

### 2.5.1. Bối cảnh và Vấn đề nghiên cứu (Context & Problem Statement)
Trong quy trình huấn luyện Học máy hiện đại, các bộ tăng tốc phần cứng chuyên dụng như **GPU** và **TPU** phát triển vượt bậc về tốc độ tính toán đại số tuyến tính nhưng lại hỗ trợ hạn chế các tác vụ tiền xử lý dữ liệu trực tuyến (*online preprocessing*) như đọc tệp, giải mã ảnh/văn bản, tăng cường dữ liệu (*data augmentation*), xáo trộn (*shuffling*) và gom lô (*batching*). Do đó, các bước ETL đầu vào này chủ yếu chạy trên CPU máy chủ. Thống kê trên hàng triệu tác vụ huấn luyện thực tế tại các trung tâm dữ liệu của Google trong một tháng cho thấy **30% tổng thời gian tính toán** bị tiêu tốn cho khâu nạp dữ liệu, và **20% số tác vụ** dành hơn một phần ba tài nguyên tính toán chỉ cho đường ống đầu vào (Figure 1, §1). Đáng chú ý hơn, **13% số tác vụ** đọc trên **1 TB** dữ liệu từ lưu trữ nhưng lại chiếm tới **hơn 96% tổng tài nguyên tính toán** toàn cụm (Figure 2, §2), khiến dữ liệu không thể nạp trọn vào bộ nhớ RAM. Nếu đường ống đầu vào không đủ nhanh, GPU/TPU đắt đỏ sẽ bị rơi vào trạng thái chờ (*input pipeline stalls*), kéo dài thời gian hội tụ mô hình và gây lãng phí nghiêm trọng hạ tầng phần cứng.

### 2.5.2. Khoảng trống Nghiên cứu (Research Gap)
Trước *tf.data*, các hệ thống xử lý dữ liệu lớn ngoại tuyến (*offline batch frameworks*) như Apache Spark, Beam hay Flume chỉ phù hợp để chuẩn bị dữ liệu tĩnh sang các định dạng nhị phân (Avro, Parquet, TFRecord), không thể thực thi hiệu quả các phép biến đổi ngẫu nhiên trực tuyến vốn làm phình to dung lượng lưu trữ nếu vật chất hóa trước. Trong khi đó, các thư viện nạp dữ liệu ML truyền thống thường đòi hỏi lập trình viên phải tự viết mã đa luồng phức tạp và tinh chỉnh thủ công hàng loạt tham số hiệu năng như mức độ song song (*parallelism*) hay kích thước bộ đệm đọc trước (*prefetch buffer size*) — vốn thay đổi nhạy cảm theo kích thước từng ảnh/mẫu dữ liệu và cấu hình CPU/RAM/băng thông mạng của từng cụm máy chủ.

### 2.5.3. Mục tiêu và Câu hỏi Nghiên cứu (Objectives & Research Questions)
Công trình đặt mục tiêu thiết kế và hiện thực hóa **tf.data** — một hệ thống gồm API khai báo cấp cao và runtime tối ưu hóa tự động tích hợp trong TensorFlow — giúp lập trình viên chỉ cần tập trung vào logic tiền xử lý dữ liệu trong khi runtime đảm bảo hiệu năng nạp dữ liệu sát ngưỡng phần cứng mà không cần tinh chỉnh thủ công. Trong phần đánh giá thực nghiệm (§4), nhóm tác giả tập trung trả lời ba câu hỏi nghiên cứu cốt lõi:
- **RQ1:** Các tính năng tối ưu hiệu năng của `tf.data` (song song hóa, pipelining, caching, tối ưu tĩnh và thực thi phi tất định) tác động như thế nào đến thông lượng của đường ống đầu vào?
- **RQ2:** Các tối ưu hóa đường ống đầu vào chuyển hóa thành mức cải thiện thời gian hội tụ đầu-cuối (*end-to-end time to target accuracy*) ra sao khi huấn luyện các mô hình Học máy tiên tiến?
- **RQ3:** Hiệu năng của `tf.data` so sánh với các khung nạp dữ liệu phổ biến khác (như PyTorch DataLoader và NVIDIA DALI) như thế nào trên cùng bài toán chuẩn?

### 2.5.4. Đối tượng, Dữ liệu và Môi trường Thực nghiệm (Methodology & Setup)
Đối tượng nghiên cứu là các đường ống nạp dữ liệu huấn luyện ML quy mô lớn chạy trên TensorFlow. Nhóm tác giả thực hiện ba lớp thực nghiệm chặt chẽ:
1. **Bộ chuẩn MLPerf (§4, Table 4):** Đánh giá 5 mô hình đại diện cho cả thị giác máy tính lẫn xử lý ngôn ngữ tự nhiên: **ResNet-50** (*ImageNet* — 1,3 triệu ảnh, `140 GB`), **SSD** và **Mask-RCNN** (*COCO* — 330 nghìn ảnh, `19 GB`), **GNMT** (*WMT16* — 4 triệu cặp câu, `1,3 GB`) và **Transformer** (*WMT17* — 4,5 triệu cặp câu, `720 MB`).
2. **Hạ tầng đo lường:** Thí nghiệm đo riêng thông lượng đường ống đầu vào (§4.1) chạy trên máy chủ 56 nhân Intel Xeon 2.60 GHz, 128 GB RAM và SSD 1 TB Samsung SM961; thí nghiệm huấn luyện đầu-cuối (§4.2) chạy trên cụm 8 máy chủ (112 nhân CPU, 100 GB RAM — riêng Mask-RCNN dùng 400 GB RAM — và 8 bộ tăng tốc **TPUv3** mỗi máy); thí nghiệm đối chứng với PyTorch DataLoader và NVIDIA DALI (§4.3) chạy trên máy ảo Google Cloud `n2-standard-64` (64 nhân CPU, 256 GB RAM, 500 GB SSD, NVIDIA Tesla T4 GPU).
3. **Phân tích toàn cụm sản xuất (§5.1):** Thu thập số liệu đo đạc (*telemetry*) từ hàng triệu tác vụ `tf.data` chạy thực tế tại trung tâm dữ liệu Google trong một tháng năm 2020 (bằng cách băm đồ thị luồng dữ liệu để theo dõi tần suất tái thực thi).

### 2.5.5. Kiến trúc và Kỹ thuật Cốt lõi (Core Architecture & Optimizations)
Kiến trúc của `tf.data` (hơn 15.000 dòng Python và 40.000 dòng C++) xây dựng trên hai trừu tượng tách biệt lấy cảm hứng từ CSDL quan hệ: **`Dataset`** phi trạng thái (mô tả cây biểu thức các toán tử như `from_file`, `interleave`, `map`, `filter`, `batch`, `cache`, `prefetch`) và **`Iterator`** có trạng thái (duyệt và sinh từng phần tử). Trên nền mô hình hàm này, runtime triển khai ba lớp kỹ thuật tối ưu:
1. **Song song hóa và Software Pipelining (§3.2):** Sử dụng `interleave` để song song hóa I/O đọc nhiều tệp, `map(num_parallel_calls)` để song song hóa tiền xử lý CPU, `prefetch` để gối đầu tính toán giữa CPU host, truyền dữ liệu và GPU/TPU, cùng tùy chọn thứ tự phi tất định (*non-deterministic ordering*) giúp triệt tiêu hiện tượng tắc nghẽn đầu hàng (*head-of-line blocking*) — mang lại tới ~40% cải thiện thông lượng trên ImageNet.
2. **Tối ưu hóa Tĩnh bằng Viết lại Đồ thị (§3.3.1):** Chuyển cây biểu thức `Dataset` sang `GraphDef` và áp dụng các luật viết lại trên nền **Grappler** (gộp toán tử `map + batch`, `map + map`, `shuffle + repeat`, `map + filter`) nhằm giảm chi phí gọi ảo `get_next`, cùng kỹ thuật **Map Vectorization** chuyển `d.map(f).batch(b)` thành `d.batch(b).map(pfor(f))` để tận dụng toán tử ma trận theo lô.
3. **Tối ưu hóa Động `AUTOTUNE` (§3.3.2):** Một luồng nền nhẹ duy trì cây iterator đang chạy, đo thời gian xử lý tại từng nút và xây dựng mô hình giải tích ước lượng độ trễ đầu ra (*output latency*). Các toán tử bất đồng bộ (`prefetch`, `parallel map`, `interleave`) được mô hình hóa bằng hệ thống hàng đợi **M/M/1/k** để tính xác suất bộ đệm rỗng $p_{\text{empty}}$ theo tốc độ sản xuất $x$, tốc độ tiêu thụ $y$ và kích thước bộ đệm $n$; sau đó áp dụng thuật toán **Gradient Descent** định kỳ dưới ràng buộc ngân sách CPU/RAM để tự động chọn độ song song và kích thước bộ đệm tối ưu toàn cục trong vòng micro giây đến mili giây.

### 2.5.6. Kết quả Thực nghiệm Nổi bật (Key Findings)
- **Tăng tốc thông lượng đường ống đầu vào (§4.1, Figure 7):** Trên máy chủ 56 nhân, `tf.data` tăng tốc độ xử lý mỗi epoch từ **2,7×** (Mask-RCNN) đến **63,1×** (SSD) và **43,3×** (ResNet-50) so với đường ống tuần tự; chế độ `AUTOTUNE` đạt hiệu năng tương đương chuyên gia tinh chỉnh tay (`62,9×` vs `63,1×` ở SSD; `42,6×` vs `43,3×` ở ResNet-50).
- **Tăng tốc thời gian hội tụ huấn luyện đầu-cuối (§4.2, Figure 8):** Song song hóa và pipelining giúp giảm thời gian huấn luyện trung bình **7×** trên 5 bài chuẩn MLPerf; riêng các bài toán ảnh được hưởng lợi thêm **1,2×–2,0×** nhờ caching và tối ưu tĩnh, đưa tổng mức tăng tốc đầu-cuối lên **21,0×** (ResNet-50) và **22,0×** (SSD). Đáng chú ý, thời gian hội tụ với `AUTOTUNE` chỉ chênh lệch **trong phạm vi 1%** so với cấu hình chuyên gia tinh chỉnh tay trên 4/5 bài chuẩn (và trong 4% ở GNMT), đồng thời xóa bỏ hoàn toàn nút thắt đầu vào (tiệm cận cận trên đường ống lý tưởng).
- **So sánh với PyTorch DataLoader & NVIDIA DALI (§4.3, Table 6–7):** Trên bài toán ImageNet-ResNet50 (máy 64 nhân), `tf.data` chạy thuần CPU mất **110 giây/epoch** — nhanh hơn **1,9×** so với **PyTorch DataLoader** (`213 giây`), vượt xa **NVIDIA DALI thuần CPU** (`777 giây`) lẫn **DALI + 1 GPU** (`172 giây`), và tiệm cận **DALI + 2 GPUs** (`107 giây`) mà không tiêu tốn tài nguyên GPU huấn luyện. Trên bảng xếp hạng MLPerf v0.7, `tf.data` là khung nạp dữ liệu duy nhất được dùng xuyên suốt cả bài toán ảnh lẫn văn bản.
- **Phát hiện từ hàng triệu job sản xuất (§5.1):** Trong **75% số tác vụ**, dung lượng dữ liệu sau tiền xử lý nhỏ hơn dữ liệu thô đọc từ lưu trữ; đồng thời các đường ống giống hệt nhau bị thực thi lặp lại rất nhiều lần giữa các job — mở ra hướng nghiên cứu lớn về đẩy phép chiếu/lọc dữ liệu xuống gần tầng lưu trữ và chia sẻ bộ nhớ đệm vật chất hóa liên tác vụ.

---

# PHẦN 3: TỰ VẼ LẠI 02 HÌNH MINH HỌA TỪ BÀI BÁO GỐC

> **Cam kết liêm chính học thuật:** Cả hai hình minh họa dưới đây được sinh viên tự lập trình tái tạo hoàn toàn bằng **Python (`matplotlib`)** ở độ phân giải **300 DPI** (kèm bản vector **PDF**) dựa trực tiếp trên số liệu và sơ đồ gốc trong `tfdata-PVLDB2021.pdf`, tuyệt đối không cắt ghép hay chụp ảnh màn hình.

## 3.1. HÌNH 1 (BÀI 5): MÔ HÌNH ƯỚC LƯỢNG ĐỘ TRỄ ĐẦU RA CỦA AUTOTUNE (TÁI TẠO FIGURE 5)

![Hình tái tạo Figure 5: Mô hình ước lượng độ trễ đầu ra của cơ chế AUTOTUNE trên cây Iterator](<../../99 - Đính kèm (Attachments)/TV1_Bai5_Hinh1_Autotune_Model.png>)

*(Tệp hình ảnh lưu tại: `99 - Đính kèm (Attachments)/TV1_Bai5_Hinh1_Autotune_Model.png` và bản vector `TV1_Bai5_Hinh1_Autotune_Model.pdf`; mã nguồn tại: `03 - Phương pháp & Thí nghiệm (Methodology & Experiments)/scripts/ve_hinh_tfdata_bai5.py`.)*

1. **Vị trí hình gốc trong bài báo:** **Figure 5**, Mục 3.3.2 (*Dynamic Optimizations*), trang 7 của bản PDF gốc (`p. 2951` bản PVLDB).
2. **Mục đích của hình:** Minh họa trực quan cơ chế duyệt cây hai chiều (*downward* và *upward traversal*) mà mô hình giải tích `AUTOTUNE` của `tf.data` sử dụng để ước lượng độ trễ đầu ra đầu-cuối của một đường ống nạp dữ liệu mà không cần chạy thử nghiệm gây ảnh hưởng đến tác vụ huấn luyện thật.
3. **Các biến số và thành phần thể hiện:** Gồm 3 cột song song: cột trái biểu diễn **tốc độ tiêu thụ $y$** (`consumer rate`, đơn vị `get_next calls/sec`) lan truyền từ trên xuống (`100 → 100 → 1000 → 1000 → 500`); cột giữa là **cây toán tử đường ống** (`data consumer → prefetch (n=2) → batch (b=10) → map (p=5, n=5) → interleave (p=1, n=1, cycle=2) → from_file`); cột phải biểu diễn **độ trễ đầu ra** (`output latency`, ms) lan truyền ngược từ dưới lên thông qua công thức hàng đợi M/M/1/k $p_{\text{empty}}$ (`5 ms → 4.15 ms → 3.55 ms → 36.5 ms → 27 ms`).
4. **Cách thức sinh viên tái tạo hình:** Viết script Python sử dụng `matplotlib.patches.FancyBboxPatch` và `annotate` để dựng lại chính xác 6 tầng nút, các mũi tên hai chiều màu xanh dương (duyệt xuống) và cam đỏ (duyệt lên) cùng đầy đủ công thức định lượng của Figure 5 gốc, xuất đồng thời PNG 300 DPI và PDF vector.
5. **Ý nghĩa của kết quả thể hiện:** Sơ đồ cho thấy cách `tf.data` tách bạch tính toán cho toán tử đồng bộ (`batch`: hàm tuyến tính $10 \times 3.55 + 1 = 36.5\text{ ms}$) và toán tử bất đồng bộ (`interleave`, `map`, `prefetch`: nhân với xác suất rỗng bộ đệm $p_{\text{empty}}$), giúp giảm độ trễ hiệu dụng cuối cùng từ `36.5 ms` xuống `27 ms` nhờ bộ đệm `prefetch`.
6. **Kết luận khoa học rút ra:** Nhờ mô hình giải tích gọn nhẹ này, luồng nền `AUTOTUNE` có thể tính đạo hàm và tối ưu đồng thời toàn bộ tham số (parallelism & buffer size) bằng Gradient Descent chỉ trong micro giây–mili giây, tránh tối ưu cục bộ gây quá tải CPU/RAM.
7. **So sánh với bài báo gốc:** *Điểm giống:* Bảo toàn 100% cấu trúc 6 nút, toàn bộ giá trị thông số ($x, y, n$, cycle length, độ trễ từng tầng) và chiều duyệt của Figure 5 gốc. *Điểm khác biệt & cải tiến:* Mã hóa màu rõ ràng phân biệt toán tử bất đồng bộ (nền xanh nhạt), toán tử đồng bộ (nền vàng nhạt), nguồn/đích và bổ sung hộp chú giải trực quan bằng tiếng Việt giúp người đọc nắm ngay nguyên lý duyệt hai chiều.

---

## 3.2. HÌNH 2 (BÀI 5): HỆ SỐ TĂNG TỐC THỜI GIAN HỘI TỤ HUẤN LUYỆN MLPERF (TÁI TẠO FIGURE 8)

![Hình tái tạo Figure 8: Hệ số tăng tốc thời gian hội tụ huấn luyện đầu-cuối trên 5 bài chuẩn MLPerf](<../../99 - Đính kèm (Attachments)/TV1_Bai5_Hinh2_MLPerf_Speedup.png>)

*(Tệp hình ảnh lưu tại: `99 - Đính kèm (Attachments)/TV1_Bai5_Hinh2_MLPerf_Speedup.png` và bản vector `TV1_Bai5_Hinh2_MLPerf_Speedup.pdf`; mã nguồn tại: `03 - Phương pháp & Thí nghiệm (Methodology & Experiments)/scripts/ve_hinh_tfdata_bai5.py`.)*

1. **Vị trí hình gốc trong bài báo:** **Figure 8**, Mục 4.2 (*End-to-End Experiments*), trang 9 của bản PDF gốc (`p. 2953` bản PVLDB).
2. **Mục đích của hình:** Chứng minh định lượng rằng việc tối ưu hóa đường ống đầu vào bằng `tf.data` không chỉ tăng tốc riêng khâu đọc dữ liệu mà chuyển hóa trực tiếp thành mức rút ngắn đột biến **thời gian huấn luyện đầu-cuối đến độ chính xác mục tiêu** trên cụm TPUv3, đồng thời chứng minh `AUTOTUNE` ngang tầm chuyên gia tinh chỉnh thủ công.
3. **Các biến số và thông tin thể hiện:** Trục hoành gồm **5 bài chuẩn MLPerf** (`ResNet-50`, `SSD`, `Mask-RCNN`, `GNMT`, `Transformer`); mỗi bài chuẩn so sánh **3 cấu hình** (chuẩn hóa so với baseline đọc tuần tự = `1.0×`): *Expert-tuned Parallelism* (`10.4×`, `17.9×`, `3.1×`, `1.4×`, `2.0×`), *Expert-tuned Parallelism + Optimizations* (`20.8×`, `21.9×`, `4.3×`, `1.6×`, `2.0×`) và *Autotune Parallelism + Optimizations* (`21.0×`, `22.0×`, `4.4×`, `1.5×`, `2.0×`). Trục tung biểu diễn Hệ số tăng tốc (*End-to-end Training Time Speedup*, thang đo `0–25×`).
4. **Cách thức sinh viên tái tạo hình:** Viết script Python bằng `numpy` và `matplotlib` với toàn bộ 15 giá trị số trích xuất chính xác 100% từ nhãn số in trên Figure 8 gốc, kết hợp bảng màu học thuật có họa tiết gạch chéo/chấm phân biệt khi in đen trắng, bổ sung đường tham chiếu `Baseline = 1.0×` và hộp chú thích phân nhóm tải Ảnh vs. Văn bản.
5. **Ý nghĩa của kết quả thể hiện:** Các bài toán thị giác máy tính (ResNet-50, SSD, Mask-RCNN) chịu gánh nặng giải mã và tăng cường ảnh cực lớn nên hưởng lợi gấp đôi khi bật đầy đủ tính năng `tf.data` (ResNet-50 tăng từ `10.4×` lên `21.0×`, SSD lên `22.0×`). Ngược lại, ở các bài toán văn bản (GNMT, Transformer), chỉ riêng song song hóa và pipelining đã đủ để không còn bị nghẽn đầu vào.
6. **Kết luận khoa học rút ra:** Tối ưu hóa đường ống nạp dữ liệu là yếu tố sống còn quyết định hiệu suất khai thác GPU/TPU, và cơ chế `AUTOTUNE` hoàn toàn có thể thay thế việc tinh chỉnh tham số thủ công (sai khác `≤ 1%` ở 4/5 bài chuẩn và `≤ 4%` ở GNMT).
7. **So sánh với bài báo gốc:** *Điểm giống:* Giữ nguyên 100% 5 mô hình MLPerf, 3 nhóm cấu hình và toàn bộ 15 giá trị định lượng chính xác của Figure 8 gốc. *Điểm khác biệt & cải tiến:* Bổ sung đường chuẩn `Baseline = 1.0×`, đường phân tách trực quan giữa nhóm tải **Thị giác máy tính** và **Xử lý ngôn ngữ tự nhiên**, họa tiết thân thiện in ấn và hộp chú thích nêu bật khoảng cách `< 1%` giữa `AUTOTUNE` và chuyên gia.

---

# PHẦN 4: ĐÁNH GIÁ, PHẢN BIỆN & CẦU NỐI FEATHRPO ↔ TF.DATA

### 4.1. Đánh giá điểm mạnh và hạn chế (Critical Review)
- **Điểm mạnh nổi bật:** Công trình kết hợp xuất sắc giữa lý thuyết hệ thống (mô hình hàng đợi M/M/1/k, tối ưu hóa đồ thị tĩnh, lập trình hàm) với thực chứng công nghiệp quy mô khổng lồ (hàng triệu tác vụ sản xuất tại Google và chuẩn MLPerf v0.7). Kết quả `AUTOTUNE` đạt hiệu năng trong phạm vi 1% so với chuyên gia tinh chỉnh tay và vượt PyTorch DataLoader `1.9×` thuần CPU có giá trị ứng dụng cực kỳ cao.
- **Hạn chế kỹ thuật:** Thứ nhất, theo chính phát hiện của tác giả ở §5.1, `tf.data` hiện mới tối ưu cục bộ trong từng job đơn lẻ nên chưa tự động chia sẻ dữ liệu đã tiền xử lý giữa nhiều job chạy lặp lại cùng một đường ống (dẫn tới lãng phí CPU khi tinh chỉnh siêu tham số). Thứ hai, việc tách biệt hoàn toàn giữa tầng lưu trữ đám mây và máy chủ huấn luyện khiến `tf.data` vẫn phải kéo toàn bộ byte thô qua mạng trước khi lọc/chiếu (dù 75% số job làm giảm kích thước dữ liệu). Thứ ba, tối ưu hóa `map + batch fusion` chưa hỗ trợ tốt các toán tử gom nhóm theo độ dài chuỗi (`groupby`) trong bài toán NLP/LLM.

### 4.2. Cầu nối Kiến trúc: FeathrPO (Tầng 4) ↔ tf.data (Tầng 5)
Trong mạch 5 tầng của Đề tài C, **FeathrPO (PVLDB 2023)** giải quyết bài toán tạo tập huấn luyện ngoại tuyến chính xác thời gian (*Point-in-Time Join*) và tái sử dụng đặc trưng từ Data Lakehouse, còn **tf.data (PVLDB 2021)** tiếp nhận trực tiếp đầu ra đó để thực hiện tiền xử lý trực tuyến (*shuffling, batching, augmentation, prefetching*) nạp vào GPU/TPU ở tốc độ tối đa. Hai tầng này bổ trợ chặt chẽ nhưng cũng phơi bày rõ khoảng trống liên tầng: nếu có cơ chế truyền ngữ nghĩa từ `tf.data` xuống `FeathrPO`/`Delta Lake`/`BtrBlocks` (như đẩy phép chiếu cột *projection pushdown* và chia sẻ bộ nhớ đệm vật chất hóa liên tác vụ), toàn bộ chuỗi 5 tầng sẽ cắt giảm mạnh cả băng thông mạng lẫn chu kỳ CPU dư thừa.

---

# PHẦN 5: DANH MỤC TÀI LIỆU THAM KHẢO (CHUẨN IEEE)

1. **D. G. Murray, J. Šimša, A. Klimovic, and I. Indyk**, *"tf.data: A Machine Learning Data Processing Framework,"* *Proceedings of the VLDB Endowment (PVLDB)*, vol. 14, no. 12, pp. 2945–2958, Aug. 2021. DOI: `10.14778/3476311.3476374`.
2. **M. Abadi, P. Barham, J. Chen, Z. Chen, A. Davis, J. Dean, et al.**, *"TensorFlow: A System for Large-Scale Machine Learning,"* in *Proc. 12th USENIX Symp. Operating Systems Design and Implementation (OSDI)*, 2016, pp. 265–283.
3. **P. Mattson, C. Cheng, G. Diamos, C. Coleman, P. Micikevicius, D. Patterson, et al.**, *"MLPerf Training Benchmark,"* in *Proc. Machine Learning and Systems (MLSys)*, vol. 2, pp. 336–349, 2020.
4. **R. Liu, K. Park, F. Psallidas, X. Zhu, R. Sen, M. Interlandi, et al.**, *"Optimizing Data Pipelines for Machine Learning in Feature Stores,"* *Proceedings of the VLDB Endowment (PVLDB)*, vol. 16, no. 13, pp. 4230–4239, Aug. 2023. DOI: `10.14778/3625054.3625060`.
5. **M. Armbrust, T. Das, L. Sun, B. Yavuz, S. Zhu, M. Murthy, et al.**, *"Delta Lake: High-Performance ACID Table Storage over Cloud Object Stores,"* *Proceedings of the VLDB Endowment (PVLDB)*, vol. 13, no. 12, pp. 3411–3424, Aug. 2020. DOI: `10.14778/3415478.3415560`.
