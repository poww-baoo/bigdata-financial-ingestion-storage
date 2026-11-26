# 📓 Nhật Ký Tiến Độ (Research Journal)

Ghi chép nhanh các hoạt động nghiên cứu mỗi ngày.

---

### 2026-11-10
- **Khởi tạo vault:** Thiết lập cấu trúc thư mục nghiên cứu khoa học trên Obsidian.
- **Hoạt động:** Chuẩn bị môi trường làm việc, tích hợp công cụ hỗ trợ nghiên cứu.
- **Dự định tiếp theo:** Bắt đầu khảo cứu các bài báo liên quan đến đề tài trọng tâm.

### 2026-11-10 (Cập nhật buổi tối - Tổng kết phiên làm việc)
- **Hoàn thành toàn diện báo cáo giữa kỳ môn Phương pháp NCKH trong CNTT:**
  - **Bài báo nghiên cứu:** *"Delta Lake: High-Performance ACID Table Storage over Cloud Object Stores"* (PVLDB 2020, Scopus Q1, WoS CPCI-S/ESCI, CORE A*).
  - **Cấu trúc báo cáo 6 phần hoàn chỉnh:**
    - Phần 1: Thông tin & minh chứng Scopus/WoS chi tiết.
    - Phần 2: Phân tích 10 nội dung nghiên cứu theo tiêu chuẩn học thuật.
    - Phần 3: Tái tạo 02 hình vẽ gốc (Figure 1 kiến trúc pipeline & Figure 6 đo TPC-DS) kèm thuyết minh 7 tiêu chuẩn khoa học.
    - Phần 4: Đề xuất 01 biểu đồ mới (Hệ số tăng tốc Speedup & Tỷ lệ % thời gian truy vấn tiết kiệm được) kèm thuyết minh 5 tiêu chuẩn hỗ trợ ra quyết định.
    - Phần 5: Đánh giá, phản biện bài báo và tiềm năng mở rộng.
    - Phần 6: Danh mục tài liệu tham khảo chuẩn IEEE (5 trích dẫn).
  - **Trang bìa Trường Đại học Sài Gòn (SGU):**
    - Chèn và căn giữa Logo trường SGU chính xác.
    - Sửa lỗi định dạng thụt lề âm (`hanging indent`), đưa thông tin sinh viên (`SVTH: Võ Huỳnh Minh Sang`, `Lớp: DCT123C4`, `MSSV: 3123411256`) vào vị trí ngay ngắn, thẳng hàng và cân đối hoàn hảo trong khung bìa.
    - Cập nhật chính xác giảng viên hướng dẫn: `GVHD: Vũ Ngọc Thanh Sang`.
  - **Mục lục tự động (Dynamic TOC):**
    - Thiết lập trường mã Word (`TOC \o "1-3" \h \z \u` kèm `updateFields=true`) tại Trang 2.
    - Tự động liên kết Heading 1, Heading 2 với đối soát số trang chính xác 100%.
  - **Văn phong học thuật:** Chuyển thể toàn bộ văn bản sang phong cách học thuật liên tục, mạch lạc (cohesive prose), hạn chế tối đa dấu chấm câu vụn vặt và gạch đầu dòng cộc lốc theo đúng yêu cầu.
  - **Tài liệu bàn giao:**
    - File Word: `04 - Viết bài & Xuất bản (Writing & Publication)/Bản thảo (Drafts)/Baocao.docx`
    - File PDF: `04 - Viết bài & Xuất bản (Writing & Publication)/Bản thảo (Drafts)/Baocao.pdf` (14 trang chuẩn in ấn).
    - File Markdown: `04 - Viết bài & Xuất bản (Writing & Publication)/Bản thảo (Drafts)/Báo cáo Giữa kỳ - Delta Lake.md`.
    - Script vẽ đồ thị & xuất báo cáo: `03 - Phương pháp & Thí nghiệm (Methodology & Experiments)/scripts/`.

- **Kế hoạch & Định hướng buổi tiếp theo:**
  - Rà soát lại lần cuối trước khi nộp theo yêu cầu giảng viên.
  - Chuẩn bị slide thuyết trình PowerPoint/Keynote nếu môn học có buổi bảo vệ báo cáo.
  - Đào sâu thêm các hướng nghiên cứu tiếp theo về kiến trúc Data Lakehouse, tối ưu hóa truy vấn hoặc thực nghiệm thực tế với mã nguồn mở Delta Lake.

### 2026-11-11
- **Hiệu chỉnh thông tin & định vị minh chứng Scopus / Web of Science (WoS):**
  - Khắc phục lỗi nhầm lẫn mã định danh: Cập nhật Scopus Source ID chuẩn xác của *Proceedings of the VLDB Endowment (PVLDB)* thành `21100199855` (thay thế mã cũ `19700190323` của ACM TIST).
  - Làm rõ vị trí nguồn trên 2 cơ sở dữ liệu:
    - Trên Scopus: Xác thực vị trí nguồn tại hồ sơ tạp chí (Source Profile) ID `21100199855` với mã ISSN `2150-8097`, phân hạng Q1, CiteScore 8.2 (đối soát mở qua ScimagoJR).
    - Trên Web of Science: Định vị nguồn trên *Clarivate Master Journal List* qua mã ISSN `2150-8097`, thuộc *Web of Science Core Collection* (nhóm CPCI-S và ESCI), phân loại CORE A*.
    - Bài báo nghiên cứu được công bố tại Vol. 13, No. 12 (2020), đối soát định danh số qua DOI `10.14778/3415478.3415560`.
  - Cập nhật đồng bộ các tài liệu bàn giao:
    - File Word: `04 - Viết bài & Xuất bản (Writing & Publication)/Bản thảo (Drafts)/Baocao.docx`.
    - File PDF: `04 - Viết bài & Xuất bản (Writing & Publication)/Bản thảo (Drafts)/Baocao.pdf`.
    - File Markdown: `04 - Viết bài & Xuất bản (Writing & Publication)/Bản thảo (Drafts)/Báo cáo Giữa kỳ - Delta Lake.md`.
    - Sao lưu an toàn: `Baocao_backup_20261111.docx`.

### 2026-11-26
- **Hoàn thiện phần nghiên cứu khoa học của TV4 — Long (Đề tài C — Nhóm 4 thành viên):**
  - **Hợp nhất bản thảo thành 01 file Markdown duy nhất:** Toàn bộ phần riêng (Mục 2.4 — FeathrPO, PVLDB 2023), phần chung (Chương 4 — Phản biện, Đánh đổi 4 tầng, Khoảng trống nghiên cứu & Hướng phát triển) và Tài liệu tham khảo IEEE được chuẩn hóa trong duy nhất file `04 - Viết bài & Xuất bản (Writing & Publication)/Bản thảo (Drafts)/Phan_TV4_Long_Feature_Store_va_Chuong4.md` (không làm slide riêng).
  - **Đối soát & chuẩn hóa văn phong:** Kiểm tra chéo toàn bộ số liệu (Table 1, Table 2, KLL sketches, BIP, kết quả tăng tốc `3,00×` / `2,50×`) với PDF gốc `Feature-Store-FeathrPO-VLDB2023.pdf`, bổ sung link Scopus/WoS/VLDB/ACM và diễn đạt bằng văn xuôi học thuật mạch lạc.
  - **Cập nhật 02 hình vẽ lại 300 DPI + Vector PDF:** Hiển thị độ chính xác 2 chữ số thập phân trên `Hinh_TV4_2_HieuNang_FeathrPO` (`1.96×`, `1.98×`, `2.02×`, `3.00×`, `2.50×`) và xuất bản vector `.pdf` cho cả 2 hình của TV4 (`Hinh_TV4_1_KienTruc_FeathrPO.pdf`, `Hinh_TV4_2_HieuNang_FeathrPO.pdf`).

### 2026-11-26 (Cập nhật tổng kết — Hoàn thiện Bài 5, Tích hợp Nhóm & Báo cáo Cuối kỳ Final 35 trang)
- **Đồng bộ kho lưu trữ GitHub & kiểm tra tiến độ nhóm:**
  - Pull đầy đủ bài đóng góp của TV2 (Cường — *BtrBlocks*), TV3 (Bảo — *Photon*, commit `3357a96`) và TV4 (Long — *FeathrPO* & Chương 4).
- **Hoàn thiện bổ sung cho Báo cáo Giữa kỳ (`Baocao.docx` / `Baocao.pdf` — 15 trang):**
  - Cập nhật trang bìa đầy đủ 04 thành viên lớp `DCT123C4` (Võ Huỳnh Minh Sang, Nguyễn Đình Cường, Châu Quốc Bảo, Nguyễn Hoàng Long) và bổ sung Trang 2 **Lời mở đầu** ngắn gọn (lý do chọn bài báo & nội dung bài báo), đồng bộ số trang Mục lục và bản Markdown.
- **Mở rộng Đề tài C lên 05 bài báo chuẩn PVLDB / ACM SIGMOD & cập nhật ngữ cảnh dự án:**
  - Cập nhật `agent.md` và `Kế hoạch Cuối kỳ - Đề tài C (Nhóm 4 thành viên).md` lên kiến trúc 5 tầng (bổ sung Bài số 5 giao TV1 — Sang: *tf.data: A Machine Learning Data Processing Framework*, Google, PVLDB 2021, DOI `10.14778/3476311.3476374`).
  - Hoàn thiện phần tích hợp còn thiếu của TV2 trong `Báo cáo Cá nhân - BtrBlocks (Nguyễn Đình Cường).md`: sửa liên kết PDF gốc, bổ sung cầu nối *BtrBlocks ↔ Delta Lake*, Ma trận so sánh đa chiều 05 công trình (Mục 3.2) và trích dẫn IEEE đầy đủ.
- **Hoàn thành trọn bộ Bài báo số 5 (`tf.data` — PVLDB 2021):**
  - Tải PDF gốc `tfdata-PVLDB2021.pdf`, viết bản thảo đầy đủ `Báo cáo Cá nhân - tf.data (Võ Huỳnh Minh Sang).md` và lập trình `scripts/ve_hinh_tfdata_bai5.py` tái tạo 02 hình 300 DPI + PDF vector (`TV1_Bai5_Hinh1_Autotune_Model`, `TV1_Bai5_Hinh2_MLPerf_Speedup`).
- **Biên soạn & xuất bản Báo cáo Cuối kỳ Final (35 trang chuẩn in ấn SGU & OOXML):**
  - Lập trình `scripts/ve_hinh_tich_hop_5tang.py` tạo 02 hình tích hợp cấp nhóm (`TV1_Hinh_KienTruc_TichHop_5Tang`, `Hinh_TongHop_HieuNang_5Tang`).
  - Lập trình pipeline OOXML `scripts/build_baocao_cuoiky_5bai.py` xuất bộ báo cáo cuối kỳ hoàn chỉnh: `BaoCao_CuoiKy_DeTaiC_Nhom4.md`, `BaoCao_CuoiKy_DeTaiC_Nhom4.docx` và `BaoCao_CuoiKy_DeTaiC_Nhom4.pdf` (35 trang).
  - Chuẩn hóa tên đề tài theo 5 thành phần khoa học, bỏ in đậm đầu ý, gỡ tên thành viên khỏi tiêu đề mục/sơ đồ (chỉ giữ trên trang bìa và Bảng phân công Mục 1.4), khung bìa đen phủ trọn khổ A4, toàn bộ tiêu đề chữ đen in đậm, đánh số trang đơn thuần căn giữa đáy trang, bảng không lặp tiêu đề khi sang trang, Mục lục tự động (`TOC \o "1-2"`), **Danh mục hình ảnh tự động phân cấp cây 3 tầng** (`TOC \f F \l "1-3"` + 25 trường `TC` + 39 bookmark/hyperlink nội bộ) và Phụ lục danh mục + bộ sưu tập 14 hình ảnh 300 DPI.

