# 📊 Danh Sách Bộ Dữ Liệu & Benchmark (Datasets & Benchmarks)

Bảng theo dõi các bộ dữ liệu được sử dụng trong đề tài nghiên cứu.

| Tên Dataset | Nguồn / Link | Kích thước | Phân loại / Ứng dụng | License | Đã tải về |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **Dataset Mẫu A** | Kaggle / HuggingFace | 10,000 samples | Phân loại văn bản | MIT | [x] |
| **Dataset Chuẩn B** | PapersWithCode | 50,000 images | Nhận dạng đối tượng | CC-BY 4.0 | [ ] |

---

## 🔒 Quy Chuẩn Quản Lý Dữ Liệu
1. Dữ liệu gốc (Raw Data) luôn được lưu trữ chỉ đọc (Read-only) và có bản backup.
2. Mọi bước xử lý làm sạch dữ liệu (Data Preprocessing) phải được viết thành script tự động, không chỉnh sửa thủ công trên file dữ liệu.
