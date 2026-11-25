# DÀN Ý SLIDE THUYẾT TRÌNH & BỘ CÂU HỎI VẤN ĐÁP (Q&A) — ĐỀ TÀI C
**Phụ trách biên soạn:** TV4 — Long *(Theo phân công tại Kế hoạch Cuối kỳ - Đề tài C)*  
**Đề tài:** *Hạ tầng quản trị dữ liệu hiện đại cho Học máy quy mô lớn: Liên kết Kiến trúc Data Lakehouse, Tối ưu hóa Lưu trữ Cột, Thực thi Vector hóa và Feature Store*  
**Thời lượng thuyết trình dự kiến:** 15–20 phút (4 thành viên cùng trình bày) + 10 phút Q&A.

---

## PHẦN 1: DÀN Ý CHI TIẾT 14 SLIDES THUYẾT TRÌNH

| Slide | Tiêu đề Slide | Nội dung cốt lõi hiển thị trên Slide | Người trình bày |
| :---: | :--- | :--- | :---: |
| **1** | **Trang bìa** | Tên đề tài (Việt/Anh), Tên học phần, GVHD Vũ Ngọc Thanh Sang, Danh sách 4 thành viên (Sang, Cường, Bảo, Long). | **Sang** |
| **2** | **Đặt vấn đề & Bối cảnh** | Thách thức của hạ tầng dữ liệu ML quy mô lớn trên Cloud Object Storage; Sợi dây dịch chuyển điểm nghẽn từ Lưu trữ $\rightarrow$ Bảng $\rightarrow$ CPU $\rightarrow$ Feature Engineering. | **Sang** |
| **3** | **Mục tiêu & 3 Câu hỏi Nghiên cứu** | Trình bày ngắn gọn RQ1 (Dịch chuyển nút thắt), RQ2 (Sự bổ trợ 4 tầng), RQ3 (Đánh đổi & Khoảng trống). | **Sang** |
| **4** | **Kiến trúc Tổng thể 4 Tầng (Đề tài C)** | Sơ đồ tích hợp 4 công trình Scopus Q1 / CORE A\*: *BtrBlocks $\rightarrow$ Delta Lake $\rightarrow$ Photon $\rightarrow$ ML Feature Store*. | **Sang** |
| **5** | **Tầng 1: BtrBlocks (SIGMOD 2023)** | Điểm nghẽn giải nén của Parquet; Cơ chế nén đệ quy linh hoạt & giải nén siêu nhanh; Minh họa Hình vẽ lại 1 & 2 của Cường. | **Cường** |
| **6** | **Tầng 2: Delta Lake (PVLDB 2020)** | Giao dịch ACID trên Object Store qua `_delta_log`, Time Travel, Z-Order & TPC-DS 1 TB (0.93h, nhanh hơn 4.04× Presto). | **Sang** |
| **7** | **Tầng 3: Photon (SIGMOD 2022)** | Loại bỏ nút thắt JVM/Spark bằng động cơ C++ Vectorized (SIMD); Hiệu năng vượt trội trên TPC-DS 100TB. | **Bảo** |
| **8** | **Tầng 4: ML Feature Stores — FeathrPO (PVLDB 2023)** | Vấn đề Data Leakage & Point-in-Time (PIT) Join; Kiến trúc tích hợp 2 module mới (*Reuse-based Optimizer* & *Data Layout Selector*) — Tái tạo Figure 8 (`Hinh_TV4_1_KienTruc_FeathrPO.png`). | **Long** |
| **9** | **Kết quả Tối ưu Feature Pipeline (FeathrPO)** | Tái sử dụng tính toán, Semijoin Reduction, KLL Cost Model & BIP Layout Selection; Biểu đồ tăng tốc tới **3,0×** (Feathr Cloud) và **2,5×** (Union Merge) — Tái tạo Figure 12 (`Hinh_TV4_2_HieuNang_FeathrPO.png`). | **Long** |
| **10** | **Ma trận So sánh 4 Công trình** | Bảng đối chiếu đa chiều: Bài toán, Kiến trúc cốt lõi, Benchmark, Chỉ số, Điểm mạnh/Hạn chế. | **Cường** |
| **11** | **Phân tích Định lượng Xuyên tầng** | Biểu đồ tổng hợp mới của nhóm thể hiện hiệu ứng cộng hưởng từ Storage đến ML Feature Pipeline. | **Bảo** |
| **12** | **Đánh đổi (Trade-offs) giữa 4 Tầng** | 4 cặp đánh đổi cốt lõi: Nén vs Giải nén; ACID chặt vs Độ trễ; Vectorized C++ vs UDF Python; Pre-computation vs Chi phí lưu trữ. | **Long** |
| **13** | **Khoảng trống Nghiên cứu & Hướng Phát triển** | 3 Research Gaps còn tồn tại & 2 đề xuất mới: *Cross-layer Optimization cho AI-Ready Lakehouse* & *Native Vector/Multimodal cho LLM/RAG*. | **Long** |
| **14** | **Kết luận & Lời cảm ơn** | Tóm tắt câu trả lời cho RQ1–RQ3; Danh mục 4 bài báo chuẩn IEEE; Mời Hội đồng đặt câu hỏi. | **Sang / Long** |

---

## PHẦN 2: BỘ CÂU HỎI & ĐÁP ÁN VẤN ĐÁP (Q&A PHẢN BIỆN)

### A. Câu hỏi cho phần của Long (Tầng 4 — ML Feature Stores)

**Câu 1: *Point-in-Time (PIT) Join là gì và tại sao nó lại quan trọng sống còn trong ML Feature Store?***
* **Gợi ý trả lời:** Dạ, PIT Join (hay *As-of Join*) là phép ghép dữ liệu giữa bảng nhãn quan sát và bảng lịch sử đặc trưng sao cho với mỗi sự kiện tại thời điểm $t_{obs}$, hệ thống chỉ lấy giá trị đặc trưng mới nhất được sinh ra tại $t_{feat} \le t_{obs}$. Nếu dùng phép `JOIN` thông thường không kiểm tra chặt điều kiện thời gian này, mô hình sẽ vô tình "nhìn thấy dữ liệu tương lai" lúc huấn luyện (**Data Leakage**), dẫn đến độ chính xác ảo lúc train nhưng sai lệch nghiêm trọng khi chạy thực tế.

**Câu 2: *Vì sao phép PIT Join chạy trên Spark mặc định lại chậm, và FeathrPO giải quyết bằng cách nào?***
* **Gợi ý trả lời:** Trên Spark mặc định, PIT Join phải xử lý phép ghép thời gian trên các bảng lịch sử rất lớn, gây quét toàn bảng và xáo trộn dữ liệu qua mạng (**Shuffle**) khổng lồ. **FeathrPO** giải quyết theo 3 hướng chuẩn CSDL: *(1)* **Reuse-based Rewriting** để tái sử dụng tập dữ liệu huấn luyện đã vật chất hóa (tính phần delta); *(2)* **Semijoin Reduction** lọc min/max timestamp kết hợp mô hình chi phí dùng **KLL sketches** (chính xác 96,84%–99,73% so với ~90% của Spark mặc định) để tránh suy thoái hiệu năng; *(3)* **Automatic Layout Selection** giải bài toán **BIP (Binary Integer Programming)** chọn phân vùng thời gian tối ưu cho bảng nguồn. Nhờ đó tăng tốc tới **3,0×** trên TPCxAI-UC10 (Cloud) và tới **2,5×** trên các thuật toán PIT Join khác.

**Câu 3: *Hai hình trong phần của em lấy từ đâu trong bài báo gốc? Có phải chụp lại từ PDF không?***
* **Gợi ý trả lời:** Dạ tuyệt đối không chụp lại. Toàn bộ 02 hình đều được em tự lập trình vẽ bằng Python `matplotlib` ở độ phân giải 300 DPI (kèm bản vector PDF):
  * **Hình 1** tái tạo trực tiếp **Figure 8** (trang 4235 của bài báo gốc), làm rõ 2 module mới (`Data Layout Selector` và `Reuse-based Optimizer`) trong kiến trúc Feathr trên Azure.
  * **Hình 2** tái tạo trực tiếp **Figure 12** (trang 4237 của bài báo gốc) qua 4 tập dữ liệu (`TPCxAI UC7/UC10`, `Kaggle-Favorita`, `Kaggle-eCommerce`) và 3 thuật toán PIT Join, trong đó các mốc trần **3,00×** và **2,50×** lấy từ văn bản mục §8.2 và các thanh còn lại được trích xuất trực quan từ vạch chia trục tung của Figure 12 gốc với độ chính xác 2 chữ số thập phân (`1,32×`–`2,02×`).

---

### B. Câu hỏi Tích hợp Xuyên 4 Tầng (Hội đồng thường hỏi nhất)

**Câu 4: *Điểm khác biệt lớn nhất của đề tài nhóm em so với việc ghép 4 bài tóm tắt rời rạc là gì?***
* **Gợi ý trả lời:** Dạ, 4 bài báo không đứng độc lập mà tạo thành một **chuỗi dịch chuyển nút thắt hiệu năng (Performance Bottleneck Shifting)**:
  * Khi Cloud Object Storage chậm về mặt quản lý giao dịch $\rightarrow$ **Delta Lake (2020)** giải quyết bằng Transaction Log ACID.
  * Khi đã có ACID trên Parquet, nút thắt lộ ra ở tốc độ giải nén Parquet trên CPU hiện đại $\rightarrow$ **BtrBlocks (2023)** giải quyết ở tầng định dạng cột.
  * Khi dữ liệu đọc lên nhanh rồi, nút thắt dịch chuyển lên tầng thực thi Spark/JVM $\rightarrow$ **Photon (2022)** giải quyết bằng engine C++ vector hóa.
  * Cuối cùng, khi hạ tầng SQL đã nhanh, bài toán đưa dữ liệu vào mô hình Học máy vẫn bị nghẽn bởi tính lặp và PIT Join $\rightarrow$ **FeathrPO (2023)** hoàn thiện mắt xích cuối.

**Câu 5: *Nếu thay Parquet bằng BtrBlocks trong Delta Lake và chạy bằng Photon + FeathrPO ngay hôm nay thì gặp rào cản gì?***
* **Gợi ý trả lời (Liên kết thẳng Chương 4):** Đây chính là **Khoảng trống nghiên cứu** mà nhóm em chỉ ra ở Chương 4:
  1. *Tính tương thích chuẩn mở:* Hệ sinh thái Delta Lake hiện gắn chặt với chuẩn Parquet; thay định dạng tệp đòi hỏi chuẩn hóa lại giao thức đọc/ghi metadata và Data Skipping.
  2. *Chi phí chuyển đổi giữa Engine C++ và Python ML:* Photon tối ưu rất mạnh cho toán tử SQL bằng C++, nhưng các hàm biến đổi đặc trưng phức tạp trong ML Feature Store lại viết bằng Python/PyTorch (UDF), nếu không có cơ chế truyền dữ liệu Zero-copy xuyên suốt thì vẫn phát sinh chi phí tuần tự hóa dữ liệu.
  3. *Thiếu tối ưu hóa xuyên tầng:* Hiện chưa có bộ tối ưu thống nhất biết đẩy thông tin TTL từ Feature Store xuống thẳng tầng Z-Order của Delta Lake và tầng nén của BtrBlocks.
