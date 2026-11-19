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
