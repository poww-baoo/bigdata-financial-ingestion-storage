# Danh sách chỉnh sửa và kiểm tra báo cáo

Bản gốc: `report_updated.docx`. Bản hoàn thiện để duyệt: `report_hoan_thien.docx`.

## Nội dung đã chỉnh

- [x] Đối chiếu tên/MSSV ở bìa với bảng phân công; chuẩn hóa dòng địa danh và ngày tháng.
- [x] Bổ sung mục 4.4 về lý do chọn Kafka, MinIO, Parquet, Python microbatch và DuckDB.
- [x] Bổ sung mục 4.5 về lựa chọn phân vùng, small files và hợp đồng bàn giao.
- [x] Bổ sung mục 5.3 về phân loại lỗi và giới hạn khôi phục, chỉ rõ trường hợp thiếu event_time có thể vượt validator nhưng lỗi ở bước sau.
- [x] Bổ sung mục 5.4 về điều kiện tái lập và các thông số môi trường cần lưu.
- [x] Bổ sung mục 6.6 phân tích tỷ lệ đầu ra, phạm vi phép đo và tiêu chí đã/chưa có bằng chứng.
- [x] Bổ sung mục 7.2 hướng dẫn đọc từng bộ log/JSON/CSV, phân biệt ảnh Storage với demo Kafka.
- [x] Bổ sung mục 8.3 về ưu tiên hoàn thiện schema, khôi phục và thử tải liên tục.
- [x] Viết lại kết luận gắn từng kết quả với phạm vi đã kiểm chứng.
- [x] Thêm Phụ lục B đối chiếu mục 5.1–5.8 của đề và danh mục hồ sơ bàn giao.
- [x] Thêm Phụ lục C ghi nhận phạm vi sử dụng Codex trong đợt hoàn thiện này, để nhóm duyệt.
- [x] Chuẩn hóa đơn vị MiB trong bảng và biểu đồ dung lượng.
- [x] Vẽ lại bốn biểu đồ từ đúng số liệu benchmark đã lưu để loại bỏ chồng nhãn và làm rõ phạm vi đo cục bộ/trong bộ nhớ. Lưu hình mới với tiền tố `report_` trong `docs/charts/`; giữ các hình gốc.
- [x] Gộp các đoạn diễn giải benchmark bị lặp, giữ số liệu gốc.
- [x] Tạo và chạy `scripts/check_report_schema.py`, bổ sung `docs/schema_validation_probe.json` gồm chín ca và hash mã nguồn.
- [x] Giữ đủ 12 ảnh nhúng (vẽ lại bốn biểu đồ; giữ logo, sơ đồ và sáu ảnh MinIO); cập nhật mục lục dạng trường Word đủ 51 mục và số trang theo bản dựng kiểm tra.

## Kết quả kiểm tra bản Word

- [x] DOCX mở và dựng được bằng ONLYOFFICE, khổ A4; bản dựng kiểm tra có 42 trang.
- [x] Rà hình ảnh toàn bộ trang; kiểm tra lại các trang có biểu đồ sau khi thay hình.
- [x] Đối chiếu 51 số trang mục lục với vị trí tiêu đề trong bản dựng, không phát hiện lệch.
- [x] Kiểm tra gói ZIP/XML, đủ 9 chương, tóm tắt 234 từ, không có trang trắng chỉ chứa số trang.
- [x] Đối chiếu số liệu chính với JSON/CSV đã lưu; xác nhận chín ca probe và SHA-256 khớp tệp nguồn đang có.
- [x] Chỉ tạo bản PDF/PNG tạm phục vụ kiểm tra bố cục; không đưa PDF vào bộ bàn giao.

## Giới hạn cần hiểu khi duyệt

- Không sửa hành vi pipeline hoặc bổ sung tính năng cưỡng chế schema. Báo cáo mô tả đúng hiện trạng của mã.
- Không chạy lại Kafka/MinIO, benchmark tải lớn hoặc thử nghiệm sự cố trong đợt biên tập.
- Chín ca validator khớp hành vi được mô tả không có nghĩa validator đạt hợp đồng dữ liệu đầy đủ.
- CPU/RAM của lần benchmark cũ chưa được lưu đủ; không lấy thông số máy hiện tại thay cho thông số lịch sử.
- Giữ số liệu demo 3.061 message, 2.923 hợp lệ, 61 trùng, 77 lỗi và Storage 1.000 dòng, 45 → 9 tệp.
- Không kéo dài nội dung chỉ để đạt số trang khuyến nghị; bổ sung tập trung vào lập luận và khả năng kiểm chứng.
- Bản PDF để nộp do người dùng xuất sau khi duyệt Word.

## Người dùng duyệt trước khi xuất PDF

- [ ] Xác nhận tên, MSSV, lớp, giảng viên và bảng phân công phản ánh đúng thực tế.
- [ ] Đọc Phụ lục C và xác nhận phần sử dụng AI trong đợt hoàn thiện này.
- [ ] Nếu chỉnh nội dung hoặc font trong Word/WordCraft, cập nhật toàn bộ mục lục và trường số trang trước khi xuất PDF.
- [ ] Nộp kèm mã nguồn, cấu hình, script/mẫu dữ liệu và các thư mục minh chứng được dẫn trong báo cáo.
