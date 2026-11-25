# ĐÓNG GÓP BÁO CÁO CUỐI KỲ — ĐỀ TÀI C (THÀNH VIÊN 4: LONG)

**Học phần:** Phương pháp Nghiên cứu Khoa học trong Công nghệ Thông tin  
**Đề tài nhóm:** *Hạ tầng quản trị dữ liệu hiện đại cho Học máy quy mô lớn: Liên kết Kiến trúc Data Lakehouse, Tối ưu hóa Lưu trữ Cột, Thực thi Vector hóa và Feature Store*  
**Thành viên thực hiện:** TV4 — Long  
**Phạm vi phụ trách:**
1. **Phần riêng (Mục 2.4):** Phân tích bài báo *Optimizing Data Pipelines for Machine Learning in Feature Stores* (PVLDB 2023), minh chứng chỉ mục Scopus/WoS, 02 hình tự vẽ lại ở độ phân giải 300 DPI + vector PDF và phản biện khoa học.
2. **Phần chung (Chương 4):** Phản biện chéo, Phân tích Đánh đổi 4 tầng, Tổng hợp Khoảng trống Nghiên cứu chung và Đề xuất Hướng phát triển.

---

# PHẦN A: MỤC 2.4 — TẦNG ĐƯỜNG ỐNG ĐẶC TRƯNG HỌC MÁY (ML FEATURE STORES)

## 1. Thông tin và Nguồn Bài báo (Chuẩn Scopus / WoS / CORE A\*)

1. **Tên bài báo (Title):**
   - *Tiếng Anh:* **Optimizing Data Pipelines for Machine Learning in Feature Stores**
   - *Dịch nghĩa tiếng Việt:* **Tối ưu hóa Đường ống Dữ liệu cho Học máy trong các Kho Đặc trưng (Feature Stores)**
2. **Danh sách tác giả & Cơ quan công tác:**
   - Công trình là kết quả hợp tác của **10 tác giả** đến từ Microsoft, các trường đại học và tập đoàn công nghệ lớn: Rui Liu (*University of Chicago*), Kwanghyun Park (*Yonsei University*), Fotis Psallidas, Xiaoyong Zhu, Rathijit Sen, Matteo Interlandi, Yuanyuan Tian, Jesús Camacho-Rodríguez (*Microsoft*), Jinghui Mo (*LinkedIn*) và Konstantinos Karanasos (*Meta*). Theo ghi chú trên bản in chính thức, phần lớn nghiên cứu được thực hiện trong thời gian Rui Liu, Kwanghyun Park và Konstantinos Karanasos công tác tại Microsoft.
3. **Tên tạp chí / Kỷ yếu hội nghị (Journal / Proceedings):**
   - *Tên chính thức:* **Proceedings of the VLDB Endowment (PVLDB)**
   - *Nhà xuất bản:* VLDB Endowment & ACM (Association for Computing Machinery)
   - *Mã số chuẩn quốc tế (ISSN):* `2150-8097`
   - *Quy cách xuất bản:* Tập 16 (Volume 16), Số 13 (Issue 13), Trang 4230–4239 (trình bày tại Hội nghị Quốc tế VLDB lần thứ 49 tại Vancouver, Canada).
4. **Năm công bố:** **2023** (Tháng 8/2023).
5. **DOI & Liên kết chính thức:**
   - **DOI:** [`10.14778/3625054.3625060`](https://doi.org/10.14778/3625054.3625060)
   - **Đường dẫn chính thức tại VLDB Endowment:** [https://www.vldb.org/pvldb/vol16/p4230-liu.pdf](https://www.vldb.org/pvldb/vol16/p4230-liu.pdf)
   - **Đường dẫn tại ACM Digital Library:** [https://dl.acm.org/doi/10.14778/3625054.3625060](https://dl.acm.org/doi/10.14778/3625054.3625060)
   - **Bản lưu trữ offline trong Vault:** `01 - Tổng quan tài liệu (Literature Review)/Bài báo đã đọc (Papers)/Feature-Store-FeathrPO-VLDB2023.pdf`
6. **Bằng chứng thuộc danh mục Scopus & Web of Science (WoS):**
   - **Scopus (Elsevier):** Ấn phẩm *Proceedings of the VLDB Endowment* được Elsevier Scopus lập chỉ mục liên tục từ năm **2008 đến nay** tại hồ sơ nguồn **Scopus Source ID: `21100199855`** gắn mã **ISSN `2150-8097`** ([Scopus Source Details - ID 21100199855](https://www.scopus.com/sourceid/21100199855)).
   - **Web of Science (Clarivate):** Nguồn được ghi nhận trên cổng **Clarivate Master Journal List** ([https://mjl.clarivate.com](https://mjl.clarivate.com)) khi tra cứu qua mã **ISSN `2150-8097`**, thuộc bộ chỉ mục lõi *Web of Science Core Collection* (CPCI-S và ESCI).
   - **Xếp hạng học thuật CORE:** Đạt hạng **A\*** — cấp cao nhất trong ngành Khoa học Máy tính về Cơ sở dữ liệu và Hệ thống dữ liệu lớn.
7. **Chỉ số ảnh hưởng (CiteScore / Impact):**
   - Scopus CiteScore nằm trong khoảng **7,5 – 8,2**; chỉ số h-index của ấn phẩm PVLDB đạt **> 200**.
8. **Lĩnh vực & Phân hạng trên ScimagoJR (SJR):**
   - Liên kết tra cứu ScimagoJR: [https://www.scimagojr.com/journalsearch.php?q=21100199855&tip=sid](https://www.scimagojr.com/journalsearch.php?q=21100199855&tip=sid)
   - Đạt phân hạng **Q1** ở tất cả các chuyên ngành liên quan gồm *Computer Science: Information Systems (Q1)*, *Computer Science: Software (Q1)* và *Computer Science: Hardware and Architecture (Q1)*.

---

## 2. Phân tích Nội dung Nghiên cứu (Theo cấu trúc IMRAD)

### 2.1. Bối cảnh và Vấn đề nghiên cứu (Introduction & Problem Statement)

Trong các hệ thống Học máy quy mô doanh nghiệp (MLOps), việc chuẩn bị dữ liệu và trích xuất đặc trưng (*Feature Engineering*) thường tiêu tốn phần lớn thời gian phát triển và tài nguyên điện toán so với bản thân quá trình huấn luyện mô hình. Để khắc phục tình trạng đường ống xử lý manh mún (*pipeline jungles*), **Feature Store** (như Feathr, Feast, Tecton hay Hopsworks) đã nổi lên như một mô hình **“DBMS-for-ML”** — hệ quản trị cơ sở dữ liệu chuyên biệt cho Học máy nhằm định nghĩa, lưu trữ, tái sử dụng và phục vụ đặc trưng đồng bộ giữa hai giai đoạn huấn luyện (*offline training*) và suy luận (*online serving*).

Thách thức kỹ thuật trung tâm khi xây dựng tập huấn luyện từ dữ liệu chuỗi thời gian lịch sử là phép ghép theo mốc thời gian chính xác, gọi là **Point-in-Time (PIT) Join** (hay *As-of Join*). Đối với mỗi bản ghi nhãn quan sát (*label record*) tại thời điểm $t_{\text{obs}}$, hệ thống chỉ được phép kết hợp với giá trị đặc trưng mới nhất được sinh ra tại hoặc trước mốc thời điểm đó ($t_{\text{feat}} \le t_{\text{obs}}$). Nếu phép ghép vô tình sử dụng các bản ghi đặc trưng phát sinh ở tương lai, mô hình sẽ mắc phải lỗi **rò rỉ dữ liệu (*Data Leakage*)**, dẫn đến độ chính xác ảo trong giai đoạn kiểm thử nhưng suy giảm nghiêm trọng khi triển khai thực tế.

### 2.2. Khoảng trống Nghiên cứu (Research Gap)

Mặc dù các Feature Store hiện hành giải quyết tốt khía cạnh quản trị ngữ nghĩa và tính đúng đắn thời gian thông qua SDK, nhóm tác giả chỉ ra hai khoảng trống lớn về hiệu năng từ góc nhìn hệ quản trị cơ sở dữ liệu. Thứ nhất, các đường ống tạo tập huấn luyện thường thực hiện phép **PIT Join** ba chiều hoặc đa bảng theo cách thức “ngây thơ” trực tiếp trên các engine phân tán như Apache Spark, dẫn đến lượng dữ liệu xáo trộn qua mạng (*network shuffle*) khổng lồ, mất cân bằng tải và tính toán lặp đi lặp lại giữa các vòng lặp thử nghiệm mô hình. Thứ hai, các kỹ thuật tối ưu hóa câu truy vấn kinh điển của CSDL quan hệ — bao gồm viết lại truy vấn dựa trên tái sử dụng (*reuse-based rewriting*), rút gọn bán ghép (*semijoin reduction*), ước lượng chọn lọc bằng tóm tắt dòng (*sketch-based cost modeling*) và lựa chọn bố cục phân vùng vật lý tối ưu — vẫn chưa được khai thác bài bản ngay tại tầng Feature Store.

### 2.3. Mục tiêu và Câu hỏi Nghiên cứu (Objectives & RQs)

Mục tiêu trọng tâm của công trình là thiết kế và hiện thực hóa một lớp tối ưu hóa mang phong cách CSDL mang tên **FeathrPO** tích hợp trực tiếp vào Feature Store mã nguồn mở **Feathr**, nhằm tăng tốc quá trình tạo tập huấn luyện Học máy mà vẫn bảo toàn tuyệt đối tính đúng đắn Point-in-Time và không yêu cầu thay đổi lõi của engine tính toán bên dưới. Từ thiết kế thực nghiệm của tác giả, có thể khái quát hai câu hỏi nghiên cứu cốt lõi: *(RQ1)* Việc áp dụng các phép viết lại logic dựa trên tái sử dụng kết hợp rút gọn *semijoin* và mô hình chi phí nhận biết bố cục có giúp cắt giảm lượng dữ liệu quét dư thừa và ngăn ngừa suy thoái hiệu năng hay không; và *(RQ2)* Khi kết hợp tối ưu bố cục dữ liệu tự động, hệ thống đạt mức tăng tốc đầu-cuối bao nhiêu lần trên nhiều tập dữ liệu ML và nhiều cài đặt thuật toán PIT Join khác nhau?

### 2.4. Đối tượng, Dữ liệu và Phương pháp Nghiên cứu (Methodology)

Đối tượng nghiên cứu của bài báo là các đường ống tạo tập dữ liệu huấn luyện trong **Feathr** (vận hành trên nền tảng Apache Spark và lưu trữ đám mây), tập trung vào các truy vấn ghép PIT Join ba bảng gồm nguồn nhãn ($L$), nguồn đặc trưng ($F$) và nguồn thông tin phụ trợ ($A$). Nhóm tác giả đánh giá hệ thống trên bốn bộ dữ liệu quy mô công nghiệp được tổng hợp tại Bảng 1 (tr. 4236 của bài báo gốc):

| Tập dữ liệu (Use Case) | Bài toán ứng dụng | Bảng Nhãn ($L$) | Bảng Đặc trưng ($F$) | Bảng Phụ trợ ($A$) |
| :--- | :--- | :--- | :--- | :--- |
| **TPCxAI-UC7 (SF10)** | Gợi ý sản phẩm theo lịch sử mua | 789.225 dòng / 27 MB | 27.987.766 dòng / 1,5 GB | 358.818 dòng / 39 MB |
| **TPCxAI-UC10 (SF10)** | Phát hiện giao dịch tài chính gian lận | 37.696 dòng / 725 KB | 55.975.921 dòng / 2,1 GB | 358.818 dòng / 39 MB |
| **Favorita (Kaggle)** | Dự đoán doanh số cửa hàng theo ngày lễ | 379 dòng / 7,3 KB | 125.497.041 dòng / 3,9 GB | 55 dòng / 1,4 KB |
| **eCommerce (Kaggle)** | Dự đoán hành vi mua từ lịch sử xem | 44.415 dòng / 941 KB | 104.335.510 dòng / 3,4 GB | 104.335.510 dòng / 4,1 GB |

Về môi trường thực nghiệm, các thí nghiệm đám mây sử dụng **Azure Synapse** với Feathr v0.7.2, Azure Blob Storage làm Offline Store và cụm Spark v3.1 trên YARN (1 driver + 4 worker nodes, mỗi node 8 vCores và 64 GB RAM). Song song đó, một cụm cục bộ (Ubuntu 20.04, 10 nhân CPU, 32 GB DRAM, 500 GB SSD, Spark v3.2) được dùng để kiểm chứng tính tổng quát của FeathrPO trên hai thuật toán PIT Join đối chứng là *Early-stop Sort Merge* và *Union Merge*.

Phương pháp kỹ thuật của **FeathrPO** xoay quanh ba trụ cột phối hợp chặt chẽ. Trước hết, nhóm tác giả xây dựng **Mô hình chi phí nhận biết bố cục** (§4) với hàm mục tiêu tối thiểu hóa lượng dữ liệu phải quét $C_q = \sum_{s \in S_q} \mathcal{D}_s - \mathcal{U}_{s_p}^q$ và sử dụng cấu trúc **KLL sketches** để ước lượng phân vị thời gian; thực nghiệm tại Bảng 2 (tr. 4236) cho thấy KLL đạt độ chính xác **96,84% – 99,73%**, vượt trội rõ rệt so với bộ ước lượng mặc định của Spark (**89,61% – 92,19%**). Tiếp theo, cơ chế **Tái sử dụng tính toán và Rút gọn Semijoin** (§5) sử dụng bộ *Matcher* để phát hiện tập huấn luyện đã vật chất hóa có khả năng bao hàm, chuyển sang bộ *Rewriter* chỉ tính phần chênh lệch (*delta*) trên cửa sổ thời gian mới, đồng thời chèn bộ lọc `[min_ts, max_ts]` (*Semijoin Reduction*) nhằm cắt giảm *Shuffle* dư thừa và tránh suy thoái hiệu năng khi độ chọn lọc cao. Cuối cùng, bộ **Chọn bố cục dữ liệu tự động** (§6) mô hình hóa bài toán chọn chiến lược phân vùng thời gian (theo năm, tháng, ngày hoặc giờ) thành **Quy hoạch Nguyên Nhị phân (BIP)** dưới ràng buộc dung lượng dữ liệu được phép ghi lại $\mathcal{B}$, và giải bằng thư viện **Google OR-Tools** (*glop solver*) chỉ trong **6–7 giây** cho kịch bản 10.000 truy vấn và 1.000 bảng nguồn.

### 2.5. Chỉ số Đánh giá và Kết quả Chính (Evaluation & Key Findings)

Để đảm bảo tính ổn định thống kê, mọi phép đo hiệu năng đều báo cáo giá trị trung bình thời gian thực thi đầu-cuối sau khi thực hiện 3 lần chạy và loại bỏ lần nhanh nhất lẫn chậm nhất, đồng thời tính **Hệ số cải thiện (*Factor of Improvement*)** so với hệ thống nền không bật FeathrPO. Kết quả thực nghiệm (§8, tr. 4236–4237) chứng minh ba phát hiện quan trọng. Thứ nhất, FeathrPO tăng tốc vượt trội so với Feathr mặc định trên đám mây lên tới **3,00×** ở bài toán phát hiện gian lận tài chính `TPCxAI-UC10`, đồng thời đạt mức tăng tốc **1,4× – 2,50×** khi cắm ghép vào các thuật toán PIT Join tiên tiến khác như *Early-stop Sort Merge* và *Union Merge*. Thứ hai, khi tăng quy mô dữ liệu qua các hệ số SF1, SF10 và SF100 của `TPCxAI-UC7`, FeathrPO duy trì ổn định mức cải thiện **1,3× – 2,3×** (Figure 11). Thứ ba, nhờ mô hình chi phí dùng KLL sketches, FeathrPO tự động nhận diện ngưỡng độ chọn lọc cao (80%–100% ở Figure 10) để quay về kế hoạch thực thi mặc định, triệt tiêu hoàn toàn nguy cơ suy thoái hiệu năng (*regression prevention*).

---

## 3. Hai Hình Minh họa Tự Vẽ lại (Đáp ứng đủ 7 Tiêu chí)

> **Cam kết liêm chính học thuật:** Toàn bộ hai hình minh họa dưới đây được tự lập trình tái tạo bằng ngôn ngữ **Python (`matplotlib`)** ở độ phân giải **300 DPI** (kèm bản vector **PDF**) dựa trực tiếp trên tài liệu gốc *Feature-Store-FeathrPO-VLDB2023.pdf*, tuyệt đối không cắt ghép hay chụp ảnh màn hình từ bài báo.

### 3.1. Hình 1 (TV4): Tái tạo Figure 8 — Các module mới của FeathrPO và tích hợp với Feathr

![[Hinh_TV4_1_KienTruc_FeathrPO.png]]
*(Tệp hình ảnh chất lượng cao lưu tại: `99 - Đính kèm (Attachments)/Hinh_TV4_1_KienTruc_FeathrPO.png` và bản vector `Hinh_TV4_1_KienTruc_FeathrPO.pdf`; mã nguồn tại: `03 - Phương pháp & Thí nghiệm (Methodology & Experiments)/scripts/ve_hinh_tv4_feathr_arch.py`.)*

1. **Vị trí hình gốc trong bài báo:** **Figure 8**, trang **4235** (trang 6 của file PDF gốc), với tiêu đề gốc *"FeathrPO new modules and their integration with other Feathr components (colored in gray)."*
2. **Mục đích của hình:** Trực quan hóa kiến trúc tích hợp tổng thể và ranh giới giao tiếp giữa hai module tối ưu mới của FeathrPO (**Data Layout Selector** và **Reuse-based Optimizer**) với các thành phần nguyên thủy của Feathr trên đám mây Azure.
3. **Các thành phần thể hiện:** Hình vẽ bao quát 5 nhóm khối chính gồm `Feature Registry` (gắn `Microsoft Purview` và `Azure SQL`), `Python Client (User SDK)`, cụm `Feathr Client` kèm `Data Layout Selector`, cụm `Apache Spark Runtime` (`Reuse-based Optimizer`, `Logical Optimizer`, `Execution Plan Generation`), và hai tầng lưu trữ `Offline Stores` (`Azure Blob Storage`, `Azure Data Lake Storage`) cùng `Online Stores` (`Azure Redis Cache`, `Cosmos DB`).
4. **Cách thức tái tạo:** Sinh viên viết kịch bản Python sử dụng `matplotlib.patches.FancyBboxPatch` và hệ thống mũi tên định hướng `annotate` để dựng lại chính xác sơ đồ khối và luồng tương tác của Figure 8, xuất đồng thời tệp PNG 300 DPI và PDF vector.
5. **Ý nghĩa của kết quả thể hiện:** Sơ đồ làm nổi bật thiết kế mở rộng **không xâm lấn (*non-intrusive extension*)** — toàn bộ quá trình viết lại kế hoạch truy vấn và tái bố cục phân vùng được xử lý gọn gàng ở lớp client, catalog và logical optimizer mà không phải sửa đổi mã nguồn lõi của Apache Spark hay hạ tầng lưu trữ.
6. **Kết luận khoa học rút ra:** Việc đặt tầng tối ưu hóa ngay tại lớp Feature Store giúp khai thác trọn vẹn ngữ nghĩa đặc trưng (cửa sổ thời gian, định nghĩa vật chất hóa) và đảm bảo tính độc lập với nhiều backend lưu trữ khác nhau.
7. **So sánh với bài báo gốc:** *Điểm giống:* Bảo toàn đầy đủ tên thành phần, phân tầng kiến trúc và hướng mũi tên hai chiều/một chiều như Figure 8 (tr. 4235). *Điểm khác biệt & cải tiến:* Việt hóa phần chú giải và thống nhất gam màu xanh lá cho cả hai module mới của FeathrPO nhằm phân biệt tức thời với nền xám của Feathr gốc (đồng thời chuẩn hóa nhãn `Reuse-based Optimizer` thay cho lỗi chính tả *"Reused-based"* trong hình gốc).

### 3.2. Hình 2 (TV4): Tái tạo Figure 12 — Hệ số cải thiện hiệu năng với FeathrPO trên Spark

![[Hinh_TV4_2_HieuNang_FeathrPO.png]]
*(Tệp hình ảnh chất lượng cao lưu tại: `99 - Đính kèm (Attachments)/Hinh_TV4_2_HieuNang_FeathrPO.png` và bản vector `Hinh_TV4_2_HieuNang_FeathrPO.pdf`; mã nguồn tại: `03 - Phương pháp & Thí nghiệm (Methodology & Experiments)/scripts/ve_hinh_tv4_pit_speedup.py`.)*

1. **Vị trí hình gốc trong bài báo:** **Figure 12**, trang **4237** (trang 8 của file PDF gốc), với tiêu đề gốc *"Factor of improvement with FeathrPO on Spark for different datasets and PIT join implementations."*
2. **Mục đích của hình:** Đánh giá định lượng mức độ tăng tốc đầu-cuối của FeathrPO so với đường cơ sở (không tối ưu) trên **4 bộ dữ liệu thực tế/benchmark** và **3 cài đặt thuật toán Point-in-Time Join** khác nhau.
3. **Các biến số và thông tin thể hiện:** Trục hoành biểu diễn 3 cài đặt PIT Join (*Feathr ZipPartition [Cloud Setup]*, *Early-stop Sort Merge [Local Setup]* và *Union Merge [Local Setup]*); 4 chuỗi cột phân biệt theo màu và họa tiết tương ứng với 4 tập dữ liệu (*TPCx-AI UC7 SF10*, *TPCx-AI UC10 SF10*, *Kaggle-Favorita*, *Kaggle-eCommerce*); trục tung biểu diễn Hệ số cải thiện (*Factor of Improvement*, thang đo `0–4`).
4. **Cách thức tái tạo:** Sinh viên lập trình biểu đồ cột ghép bằng `numpy` và `matplotlib` với các họa tiết in ấn phân biệt (`///`, `...`, `---`). **Phương pháp dữ liệu & giới hạn:** Hai mốc trần **`3,00×`** (Feathr Cloud — `TPCx-AI UC10`) và **`2,50×`** (Union Merge — `TPCx-AI UC10`) được lấy trực tiếp từ văn bản công bố tại mục §8.2 (tr. 4237); giá trị của 10 cột còn lại được trích xuất trực quan theo vạch chia trục tung của Figure 12 gốc với độ chính xác 2 chữ số thập phân (`1,32×` đến `2,02×`).
5. **Ý nghĩa của kết quả thể hiện:** Cả 12 tổ hợp dữ liệu–thuật toán đều đạt hệ số cải thiện vượt xa ngưỡng `1,00×`, trong đó `TPCx-AI UC10` đạt mức tăng tốc cao nhất (**`3,00×`** trên Cloud) do bảng đặc trưng có số dòng lớn gấp gần 1.500 lần bảng nhãn nên hưởng lợi tối đa từ phân vùng thời gian và rút gọn *semijoin*.
6. **Kết luận khoa học rút ra:** Bộ tối ưu hóa của FeathrPO mang tính **cắm ghép đa nền tảng (*pluggable*)** — hiệu quả tăng tốc được duy trì nhất quán bất kể thuật toán thực thi PIT Join cụ thể bên dưới.
7. **So sánh với bài báo gốc:** *Điểm giống:* Giữ nguyên 3 nhóm thuật toán, 4 tập dữ liệu, cấu trúc cột ghép và các giá trị đỉnh `3,00×` / `2,50×`. *Điểm khác biệt & cải tiến:* Bổ sung đường tham chiếu ngang `Baseline = 1.0×`, gắn nhãn giá trị 2 chữ số thập phân trên đỉnh mỗi cột (giúp phân biệt rõ các cột sát mốc `2,0` như `1,96×`, `1,98×` và `2,02×`), bổ sung hộp chú thích đỉnh tăng tốc và Việt hóa nhãn trục.

---

## 4. Đánh giá và Phản biện Bài báo (Critical Review)

Về mặt đóng góp nổi bật, bài báo định vị chính xác một nút thắt thực tế rất nghiêm trọng của quy trình MLOps là bài toán **Point-in-Time Join** lặp đi lặp lại, đồng thời chứng minh thuyết phục rằng việc đưa tư duy tối ưu hóa truy vấn CSDL vào lớp Feature Store giúp tăng tốc tới **3,00×** mà không cần sửa đổi lõi Apache Spark. Giá trị thực tiễn của công trình còn được củng cố nhờ việc triển khai trực tiếp trên hệ thống mã nguồn mở **Feathr** và kiểm chứng trên chuẩn công nghiệp **TPCx-AI** lẫn dữ liệu thương mại điện tử thực tế.

Tuy vậy, công trình vẫn tồn tại ba hạn chế kỹ thuật rõ rệt. Thứ nhất, FeathrPO chỉ mới can thiệp ở tầng kế hoạch logic trên **Apache Spark (JVM)** nên vẫn chịu chi phí tuần tự hóa và quản lý bộ nhớ của JVM, chưa tận dụng trực tiếp các định dạng nén giải mã siêu nhanh thế hệ mới (như BtrBlocks) hay động cơ thực thi vector hóa C++ (như Photon). Thứ hai, việc quyết định đặc trưng nào cần được tính toán trước (*materialization*) vẫn phụ thuộc hoàn toàn vào chỉ định thủ công của kỹ sư dữ liệu thông qua API thay vì tự động khuyến nghị dựa trên chi phí. Thứ ba, phạm vi của bài báo mới giới hạn ở dữ liệu bảng có cấu trúc và phép ghép khóa-thời gian truyền thống, chưa xử lý các đường ống đặc trưng phi cấu trúc hoặc vector nhúng (*vector embeddings*) phục vụ các mô hình đa phương thức và LLM.

---

# PHẦN B: CHƯƠNG 4 — PHẢN BIỆN, KHOẢNG TRỐNG NGHIÊN CỨU & HƯỚNG PHÁT TRIỂN (CHỦ TRÌ: TV4 — LONG)

Chương 4 tổng hợp các phân tích xuyên suốt cả bốn tầng kiến trúc (**BtrBlocks → Delta Lake → Photon → ML Feature Store**) nhằm giải đáp trực tiếp Câu hỏi Nghiên cứu **RQ3** của đề tài nhóm.

## 4.1. Phân tích các Sự Đánh Đổi (Trade-offs) Xuyên Suốt 4 Tầng

Khi kết hợp đồng thời bốn công trình nền tảng vào chung một hạ tầng quản trị dữ liệu phục vụ Học máy quy mô lớn trên Cloud Object Storage, kiến trúc tổng thể luôn phải cân bằng **bốn cặp đánh đổi kỹ thuật cốt lõi** được hệ thống hóa trong bảng dưới đây:

| Cặp tầng liên kết | Sự đánh đổi (Trade-off) | Phân tích kỹ thuật chuyên sâu |
| :--- | :--- | :--- |
| **Tầng 1 (BtrBlocks) ↔ Tầng 2 (Delta Lake)** | **Tỷ lệ nén tối đa vs. Tốc độ giải nén & Độ phổ cập chuẩn mở** | Delta Lake dựa vào chuẩn Parquet để bảo đảm khả năng đọc/ghi đa công cụ, song Parquet giải nén chậm trên CPU đa nhân băng thông cao; BtrBlocks giải nén vượt trội nhờ nén đệ quy thân thiện SIMD nhưng việc thay thế trực tiếp sẽ phá vỡ tính tương thích với hệ sinh thái công cụ Parquet hiện hữu. |
| **Tầng 2 (Delta Lake) ↔ Tầng 3 (Photon)** | **Tính nhất quán ACID chặt chẽ vs. Độ trễ ghi/đọc thời gian thực** | Giao thức nhật ký giao dịch (`_delta_log`) cùng cơ chế kiểm soát đồng thời lạc quan (OCC) bảo đảm ACID và Time Travel, nhưng tạo ra chi phí kiểm tra/gộp metadata và nguy cơ xung đột ghi khi có nhiều luồng cập nhật nhỏ liên tục. |
| **Tầng 3 (Photon) ↔ Tầng 4 (Feature Store)** | **Tốc độ Vectorized C++/SIMD vs. Tính linh hoạt của UDF Python/ML** | Photon tăng tốc mạnh mẽ các toán tử SQL/ETL chuẩn bằng mã máy C++ và SIMD, nhưng các phép biến đổi đặc trưng trong Feature Store thường chứa hàm Python/PyTorch tùy biến (UDF), dễ buộc engine rơi về luồng xử lý chậm hoặc gánh chi phí tuần tự hóa giữa không gian bộ nhớ C++ và Python. |
| **Tầng 4 (Feature Store) ↔ Hạ tầng Object Store** | **Tính toán sẵn (Pre-computation) vs. Chi phí lưu trữ & Độ tươi dữ liệu** | Vật chất hóa sẵn toàn bộ bảng đặc trưng giúp rút ngắn thời gian huấn luyện/suy luận nhưng làm phình to chi phí lưu trữ và dễ lỗi thời; ngược lại, tính động bằng PIT Join mỗi lần huấn luyện lại tiêu tốn chu kỳ CPU nếu thiếu cơ chế tái sử dụng và bộ nhớ đệm xuyên tầng. |

## 4.2. Tổng hợp Khoảng trống Nghiên cứu Chung (Synthesized Research Gaps)

Từ bốn cặp đánh đổi nêu trên, nhóm nghiên cứu đúc kết **ba khoảng trống nghiên cứu liên tầng** còn bỏ ngỏ trong bức tranh tổng thể hiện nay:

1. **Thiếu bộ tối ưu hóa dựa trên chi phí xuyên tầng (*Lack of Cross-layer Cost-based Optimization*):** Hiện tại, mỗi công trình mới dừng ở tối ưu cục bộ trong phạm vi tầng của mình — *BtrBlocks* tối ưu ở tầng mã hóa byte/block, *Delta Lake* tối ưu ở mức metadata tập tin (Z-Order, Data Skipping), *Photon* tối ưu tại động cơ thực thi vector hóa, còn *FeathrPO* tối ưu ở tầng logic Feature Pipeline. Hệ thống vẫn thiếu một trình tối ưu thống nhất có khả năng truyền ngữ nghĩa từ Feature Store (như độ chọn lọc theo thực thể hay vòng đời TTL của đặc trưng) xuống trực tiếp cho tầng bố cục bảng và tầng giải mã tệp cột bên dưới.
2. **Điểm nghẽn chuyển đổi dữ liệu giữa Engine C++ và Môi trường ML Python:** Dù Photon loại bỏ thành công chi phí JVM cho tầng truy vấn SQL, quá trình đưa dữ liệu đặc trưng từ Lakehouse vào các framework Học máy (PyTorch, TensorFlow, Scikit-learn) vẫn gặp nút thắt sao chép và chuyển đổi định dạng bộ nhớ qua lại giữa C++ và Python do chưa chuẩn hóa hoàn toàn cơ chế trao đổi bộ nhớ *Zero-copy* (như Apache Arrow Flight hay DLPack) xuyên suốt toàn đường ống.
3. **Thiếu chuẩn đánh giá hiệu năng đầu-cuối thống nhất (*Lack of End-to-End Unified Benchmark*):** Bốn công trình đang được đánh giá trên những hệ quy chiếu rời rạc — *BtrBlocks* đo vi mô tốc độ giải nén cột, *Delta Lake* và *Photon* đo theo truy vấn phân tích SQL (TPC-DS), còn *FeathrPO* đo hiệu năng PIT Join trên TPCx-AI. Cộng đồng vẫn chưa có một bộ benchmark chuẩn đo thông lượng trọn vẹn từ lúc đọc dữ liệu nén trên Object Store cho tới thời điểm nạp tensor vào GPU huấn luyện mô hình.

## 4.3. Đề xuất Hướng Nghiên cứu Mới (Future Research Directions)

Trên cơ sở các khoảng trống đã nhận diện, nhóm đề xuất **hai hướng nghiên cứu tiếp theo** có tính ứng dụng và khả năng mở rộng cao:

1. **Tự động Tối ưu hóa Xuyên tầng cho Hạ tầng AI-Ready Lakehouse (*Cross-layer Semantic Optimization*):** Hướng nghiên cứu này tập trung thiết kế giao thức truyền gợi ý ngữ nghĩa (*semantic hints*) từ định nghĩa đặc trưng trong Feature Store — bao gồm tần suất truy xuất khóa thực thể, phân phối độ dài cửa sổ thời gian và chính sách TTL — xuống thẳng tầng Delta Lake để tự động điều chỉnh khóa phân cụm Z-Order/Partitioning, đồng thời truyền xuống tầng định dạng tệp như BtrBlocks nhằm lựa chọn thuật toán nén tối ưu cho từng kiểu đặc trưng Học máy (vector thưa, chuỗi thời gian, giá trị phân loại).
2. **Hỗ trợ Nguyên bản Dữ liệu Đa phương thức & Vector Embeddings cho Kỷ nguyên AI/LLM:** Mở rộng kiến trúc bốn tầng để lưu trữ nguyên bản (*native storage*) các vector nhúng (*vector embeddings*) cùng dữ liệu phi cấu trúc (văn bản, hình ảnh) trực tiếp bên trong bảng giao dịch ACID của Lakehouse, kết hợp tích hợp chỉ mục tìm kiếm vector gần đúng (ANN Index) vào động cơ thực thi vector hóa như Photon nhằm phục vụ trực tiếp các đường ống truy xuất tăng cường (RAG) và tinh chỉnh mô hình ngôn ngữ lớn (LLM Fine-tuning).

---

# TÀI LIỆU THAM KHẢO (CHUẨN IEEE CHO BÀI CỦA TV4 & NHÓM)

1. M. Armbrust et al., "Delta Lake: High-Performance ACID Table Storage over Cloud Object Stores," *Proc. VLDB Endow.*, vol. 13, no. 12, pp. 3411–3424, Aug. 2020, doi: `10.14778/3415478.3415560`.
2. M. Kuschewski, D. Sauerwein, A. Alhomssi, and V. Leis, "BtrBlocks: Efficient Columnar Compression for Data Lakes," *Proc. ACM Manag. Data (SIGMOD)*, vol. 1, no. 2, pp. 1–26, Jun. 2023, doi: `10.1145/3589263`.
3. A. Behm et al., "Photon: A Fast Query Engine for Lakehouse Systems," in *Proc. ACM SIGMOD Int. Conf. Manag. Data*, Jun. 2022, pp. 2326–2339, doi: `10.1145/3514221.3526054`.
4. R. Liu et al., "Optimizing Data Pipelines for Machine Learning in Feature Stores," *Proc. VLDB Endow.*, vol. 16, no. 13, pp. 4230–4239, Aug. 2023, doi: `10.14778/3625054.3625060`.
