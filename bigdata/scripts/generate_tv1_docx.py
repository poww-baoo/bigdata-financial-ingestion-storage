import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from pathlib import Path

doc = docx.Document()

# Page setup
sections = doc.sections
for s in sections:
    s.top_margin = Inches(0.8)
    s.bottom_margin = Inches(0.8)
    s.left_margin = Inches(0.8)
    s.right_margin = Inches(0.8)

# Title
p_title = doc.add_paragraph()
r_title = p_title.add_run("KỊCH BẢN THUYẾT TRÌNH & HƯỚNG DẪN VẤN ĐÁP — THÀNH VIÊN 1")
r_title.bold = True
r_title.font.size = Pt(18)
r_title.font.color.rgb = RGBColor(24, 76, 120)
p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER

p_sub = doc.add_paragraph()
r_sub = p_sub.add_run("Học phần: Nhập môn Dữ liệu lớn (Big Data) | Giai đoạn: Ingestion → Storage\nVai trò: Kỹ sư Hạ tầng & Kafka Ingestion (Nhóm trưởng)")
r_sub.font.size = Pt(11)
r_sub.font.italic = True
r_sub.font.color.rgb = RGBColor(100, 100, 100)
p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER

doc.add_paragraph().paragraph_format.space_after = Pt(10)

def add_heading_1(text):
    h = doc.add_heading(level=1)
    r = h.add_run(text)
    r.font.size = Pt(14)
    r.bold = True
    r.font.color.rgb = RGBColor(24, 76, 120)
    h.paragraph_format.space_before = Pt(12)
    h.paragraph_format.space_after = Pt(6)
    return h

def add_heading_2(text):
    h = doc.add_heading(level=2)
    r = h.add_run(text)
    r.font.size = Pt(12)
    r.bold = True
    r.font.color.rgb = RGBColor(40, 116, 166)
    h.paragraph_format.space_before = Pt(10)
    h.paragraph_format.space_after = Pt(4)
    return h

# Section 1
add_heading_1("1. THÔNG TIN TỔNG QUAN & ĐÓNG GÓP CỦA THÀNH VIÊN 1")
p = doc.add_paragraph()
p.add_run("• Vị trí trong Pipeline: ").bold = True
p.add_run("Là CỬA NGÕ (ĐẦU VÀO) của toàn bộ hệ thống. Xây dựng hạ tầng nền tảng, thiết kế cơ chế hàng đợi tiếp nhận thông lượng cao và phát sinh dữ liệu thử thách cho các thành viên sau.\n")
p.add_run("• Các file mã nguồn & tài nguyên trực tiếp phụ trách:\n").bold = True
p.add_run("  1. docker-compose.yml: Đóng gói 5 container dịch vụ (Kafka KRaft, Kafka-Init, Kafka-UI, MinIO, MinIO-Init).\n")
p.add_run("  2. src/config.py & .env: Cấu hình hệ thống tập trung và định nghĩa Data Contract (12 trường dữ liệu chuẩn ngân hàng).\n")
p.add_run("  3. src/producer/transaction_producer.py: Module phát luồng giao dịch tốc độ cao từ tập PaySim hoặc tự sinh dữ liệu ngẫu nhiên, tích hợp cơ chế bơm lỗi giả lập (Fault Injection 2%) và gửi trùng lặp (Duplicate Injection 1%).\n")
p.add_run("  4. data/sample_transactions.csv: Bộ dữ liệu mẫu 10 dòng đạt chuẩn để nộp lên GitHub theo quy định.")

# Section 2
add_heading_1("2. TRẢ LỜI ĐẦY ĐỦ 8 TIÊU CHÍ CHẤM ĐIỂM (MỤC 5.1 - 5.8)")

add_heading_2("5.1. Quy trình được lựa chọn")
p = doc.add_paragraph()
p.add_run("• Giai đoạn: Ingestion → Storage (Tiếp nhận dữ liệu thời gian thực và lưu trữ phân tán vào Data Lake).\n")
p.add_run("• Ranh giới bắt đầu (Input boundary): Bắt đầu từ khi luồng sự kiện giao dịch tài chính (JSON stream) được đẩy vào cụm đệm phân tán Apache Kafka.\n")
p.add_run("• Ranh giới kết thúc (Output boundary): Kết thúc khi dữ liệu sạch được chuẩn hóa schema và khử trùng lặp được lưu trữ phân vùng (tx_date, tx_type) dưới định dạng cột nén Apache Parquet (Snappy) trên MinIO S3 Data Lake (đồng thời các bản ghi lỗi được cách ly vào vùng quarantine/).\n")
p.add_run("• Mối liên hệ: Cung cấp kho dữ liệu sạch cho giai đoạn tiếp theo là Storage → Processing → Analytics (phát hiện gian lận và đối soát tài chính).")

add_heading_2("5.2. Bài toán cụ thể và tính chất Dữ liệu lớn (Big Data)")
p = doc.add_paragraph()
p.add_run("• Bài toán thực tế: Tiếp nhận và lưu trữ luồng giao dịch thanh toán trực tuyến đa kênh (ATM, POS, Web, Mobile App) với tần suất cao.\n")
p.add_run("• Giải quyết 3 đặc trưng 5V:\n")
p.add_run("  1. Velocity (Tốc độ cao): Hàng chục nghìn giao dịch phát sinh đồng thời trong 1 giây vào giờ cao điểm. Cơ sở dữ liệu RDBMS truyền thống sẽ bị nghẽn đĩa và sập. Cần Apache Kafka làm bộ đệm phân tán chia tải đa làn (Partitions) để hấp thụ xung lực tải.\n")
p.add_run("  2. Veracity (Tính toàn vẹn dữ liệu): Dữ liệu tài chính không được phép mất mát, không được nhân đôi số tiền khi mạng lỗi, và phải lọc tách giao dịch rác (tiền âm, thiếu ID) vào vùng cách ly (Quarantine / DLQ).\n")
p.add_run("  3. Volume (Khối lượng lớn): Dữ liệu tích lũy hàng triệu giao dịch mỗi ngày (tập PaySim thực tế lên tới 6,36 triệu dòng, ~500MB). Cần định dạng cột nén Parquet kết hợp Phân vùng (Partitioning) để tiết kiệm 75% dung lượng lưu trữ so với JSON.")

add_heading_2("5.3. Input (Đầu vào của hệ thống)")
p = doc.add_paragraph()
p.add_run("• Nguồn dữ liệu: Bộ dữ liệu thực tế PaySim từ Kaggle (6,36 triệu bản ghi) kết hợp bộ sinh dữ liệu ngẫu nhiên chuẩn phân phối ngân hàng.\n")
p.add_run("• Cách thu thập & Tốc độ: Phát qua giao thức mạng TCP vào Kafka với tốc độ từ 1.000 đến 10.000 tin nhắn/giây.\n")
p.add_run("• Định dạng: Chuỗi văn bản JSON (UTF-8).\n")
p.add_run("• Cấu trúc 12 trường dữ liệu chuẩn:\n")
p.add_run("  - Định danh: transaction_id, sender_id, receiver_id.\n")
p.add_run("  - Thời gian: event_time (ISO-8601), step (bước thời gian mô phỏng).\n")
p.add_run("  - Nội dung: amount (số tiền > 0), currency (VND/USD), tx_type (PAYMENT, TRANSFER, CASH_OUT, CASH_IN, DEBIT), payment_channel (MOBILE_APP, WEB, POS, ATM).\n")
p.add_run("  - Số dư: sender_old_balance, sender_new_balance.\n")
p.add_run("  - Phục vụ AI: is_fraud_label (0: hợp lệ, 1: gian lận).\n")
p.add_run("• Dữ liệu thử thách do TV1 cài cắm: 2% bản ghi lỗi (tiền âm, thiếu ID) và 1% bản ghi trùng lặp mã giao dịch.")

add_heading_2("5.4. Output (Đầu ra của hệ thống)")
p = doc.add_paragraph()
p.add_run("• Tầng dữ liệu sạch (Bronze Data Lake): Lưu tại financial-datalake/bronze/transactions/ dưới định dạng Apache Parquet (Snappy), phân vùng 2 cấp: tx_date=YYYY-MM-DD/tx_type=.../part-*.snappy.parquet.\n")
p.add_run("• Tầng dữ liệu cách ly (Quarantine): Lưu tại financial-datalake/quarantine/bad_transactions/ chứa các bản ghi lỗi kèm cột error_reason phục vụ kiểm toán ngân hàng.\n")
p.add_run("• Bảng đối soát doanh thu: Cho phép truy vấn SQL tức thì qua DuckDB để tính tổng doanh thu theo ngày, theo kênh và chứng minh không mất mát một đồng nào.")

add_heading_2("5.5. Công nghệ sử dụng và vai trò")
table = doc.add_table(rows=1, cols=3)
table.alignment = WD_TABLE_ALIGNMENT.CENTER
hdr_cells = table.rows[0].cells
hdr_cells[0].text = "Công nghệ"
hdr_cells[1].text = "Vai trò trong hệ thống"
hdr_cells[2].text = "Lý do bắt buộc phải chọn"
for cell in hdr_cells:
    for par in cell.paragraphs:
        for run in par.runs:
            run.bold = True

tech_data = [
    ("Docker Compose", "Quản lý hạ tầng", "Đóng gói toàn bộ cụm dịch vụ, đảm bảo tính tái lập 100% chỉ với 1 câu lệnh."),
    ("Apache Kafka (KRaft)", "Bộ đệm Ingestion phân tán", "Chế độ KRaft mới nhất loại bỏ ZooKeeper, tối ưu tài nguyên, chia 3 Partitions để chia tải tốc độ cao."),
    ("Kafka UI (Provectus)", "Bảng điều khiển giám sát", "Công cụ mã nguồn mở giúp trực quan hóa lưu lượng tin nhắn và trạng thái phân vùng Partitions."),
    ("MinIO Object Storage", "Tầng Data Lake", "Hệ thống lưu trữ đối tượng tương thích chuẩn AWS S3, triển khai cục bộ hiệu năng cao và bảo mật riêng tư."),
    ("Apache Parquet (Snappy)", "Định dạng lưu trữ cột", "Nén dung lượng tới 75%, hỗ trợ cắt tỉa phân vùng (Partition Pruning) khi truy vấn dữ liệu."),
    ("PySpark / Micro-batch", "Cầu nối Streaming", "Đọc stream từ Kafka, lọc lỗi, khử trùng lặp và ghi dữ liệu có phân vùng xuống MinIO."),
    ("DuckDB SQL", "Kiểm chứng & Đối soát", "Đọc trực tiếp các file Parquet từ MinIO qua giao thức S3 để đối soát dữ liệu với tốc độ cao.")
]

for item in tech_data:
    row_cells = table.add_row().cells
    row_cells[0].text = item[0]
    row_cells[1].text = item[1]
    row_cells[2].text = item[2]

doc.add_paragraph().paragraph_format.space_after = Pt(8)

add_heading_2("5.7. Kết quả Demo & Thực nghiệm")
p = doc.add_paragraph()
p.add_run("• Thực nghiệm demo trực tiếp: Phát 1.011 giao dịch mẫu vào Kafka -> Hệ thống lọc chính xác 982 bản ghi sạch vào Data Lake, loại bỏ 11 bản ghi trùng lặp, và nhốt đúng 18 bản ghi lỗi vào thư mục quarantine/.\n")
p.add_run("• Thông lượng tiếp nhận duy trì ổn định ở mức 5.000 – 10.000 msg/s với độ trễ ghi chỉ từ 30 – 50 ms.\n")
p.add_run("• Định dạng Parquet Snappy giúp tiết kiệm 75% dung lượng so với JSON Lines.")

add_heading_2("5.8. Khả năng tái lập (Reproducibility)")
p = doc.add_paragraph()
p.add_run("• Khởi động toàn bộ hạ tầng chỉ với: docker compose up -d.\n")
p.add_run("• Cài đặt thư viện Python: pip install -r requirements.txt.\n")
p.add_run("• Tự sinh dữ liệu lớn tức thì bằng transaction_producer.py, không bắt buộc nộp file CSV 500MB lên GitHub.")

# Section 3
add_heading_1("3. KỊCH BẢN THUYẾT TRÌNH NÓI MẪU (STEP-BY-STEP)")
p_quote = doc.add_paragraph()
p_quote.paragraph_format.left_indent = Inches(0.4)
p_quote.paragraph_format.right_indent = Inches(0.4)
r = p_quote.add_run(
    '"Kính thưa quý thầy/cô trong hội đồng và các bạn, em tên là [Tên bạn], đảm nhận vai trò Thành viên 1: Kỹ sư Hạ tầng và Ingestion (Nhóm trưởng) trong đồ án.\n\n'
    'Đề tài của nhóm em là Quy trình Ingestion → Storage cho luồng dữ liệu giao dịch tài chính thời gian thực. Quy trình bắt đầu từ khi các giao dịch phát sinh từ ứng dụng được bơm vào Apache Kafka và kết thúc khi dữ liệu sạch được nén chuẩn Parquet lưu trên MinIO Data Lake để sẵn sàng bàn giao cho các giai đoạn Analytics phía sau.\n\n'
    'Hệ thống này bắt buộc phải giải quyết bài toán Big Data vì 3 tính chất:\n'
    '- Thứ nhất là Velocity: Các giao dịch ngân hàng phát sinh hàng nghìn bản ghi/giây. Em sử dụng Apache Kafka chế độ KRaft với 3 Partitions để phân tán tải, không làm nghẽn hệ thống.\n'
    '- Thứ hai là Veracity: Tiền bạc không được mất và không được trùng. Em xây dựng bộ phát Producer có tích hợp cơ chế bơm lỗi giả lập để nhóm kiểm chứng việc lọc dữ liệu sạch và nhốt dữ liệu lỗi vào vùng cách ly Quarantine.\n'
    '- Thứ ba là Volume: Hàng triệu giao dịch được nén và tổ chức phân vùng theo ngày để tối ưu lưu trữ.\n\n'
    'Về phần việc của em:\n'
    '1. Em đã thiết lập file docker-compose.yml để tự động hóa 100% việc khởi tạo cụm Kafka KRaft mang tên financial-cluster, kho lưu trữ MinIO và bảng điều khiển giám sát.\n'
    '2. Em thiết kế topic chính financial_tx chia thành 3 Partitions để chia tải song song, cùng một topic ngách financial_tx_dlq có 1 Partition để gom các tin nhắn lỗi.\n'
    '3. Em xây dựng module transaction_producer.py phát dữ liệu lớn theo thời gian thực và cài cắm 2% dữ liệu lỗi cùng 1% dữ liệu trùng lặp để thử thách hệ thống."'
)
r.font.italic = True

# Section 4
add_heading_1("4. HƯỚNG DẪN THAO TÁC DEMO TRÊN 2 GIAO DIỆN WEB")
p = doc.add_paragraph()
p.add_run("Tab 1: Kafka UI (http://localhost:8080)\n").bold = True
p.add_run("1. Bấm vào menu Topics ở cột bên trái: Chỉ vào cụm financial-cluster và 2 topics: financial_tx và financial_tx_dlq.\n")
p.add_run("   -> Nói: 'Dạ đây là 2 topic do tiến trình tự động khởi tạo theo đúng Data Contract của nhóm.'\n")
p.add_run("2. Bấm vào topic financial_tx: Chỉ vào bảng Partitions: 0, 1, 2.\n")
p.add_run("   -> Nói: 'Thầy thấy dữ liệu được phân bổ đồng đều qua cả 3 Partitions để tận dụng tối đa khả năng xử lý song song.'\n")
p.add_run("3. Bấm sang tab Messages: Chỉ vào nội dung tin nhắn JSON.\n")
p.add_run("   -> Nói: 'Đây là cấu trúc gói tin giao dịch JSON chuẩn gồm đầy đủ 12 trường dữ liệu như số tiền, tài khoản gửi/nhận, thời gian.'\n\n")

p.add_run("Tab 2: MinIO Console (http://localhost:9001)\n").bold = True
p.add_run("1. Bấm vào Buckets -> chọn financial-datalake:\n")
p.add_run("   -> Nói: 'Thùng chứa này được tự động tạo sẵn khi khởi động Docker.'\n")
p.add_run("2. Bấm vào thư mục bronze/transactions/: Đi vào bên trong các thư mục tx_date=... và tx_type=...:\n")
p.add_run("   -> Nói: 'Dữ liệu hợp lệ được tự động tổ chức phân vùng theo ngày và loại giao dịch dưới dạng các file nén Parquet Snappy.'\n")
p.add_run("3. Bấm vào thư mục quarantine/bad_transactions/:\n")
p.add_run("   -> Nói: 'Còn đây là thư mục cách ly. Đúng các bản ghi lỗi do em cố tình chèn vào Producer đã bị hệ thống phát hiện và nhốt riêng ra đây kèm lý do lỗi để phục vụ kiểm toán ngân hàng.'\n")
p.add_run("4. Kết thúc phần 1:\n")
p.add_run("   -> Nói: 'Sau đây, em xin phép chuyển lời lại cho Thành viên 2 để trình bày chi tiết về luồng Streaming xử lý và khử trùng dữ liệu. Em xin cảm ơn thầy cô!'")

# Section 5
add_heading_1("5. CẨM NANG CÂU HỎI VẤN ĐÁP CỦA GIẢNG VIÊN & ĐÁP ÁN CHUẨN")

qa = [
    ("Câu 1: Trang web Kafka UI này là em tự viết bằng code hay lấy ở đâu?",
     "Dạ thưa thầy, Kafka UI là công cụ mã nguồn mở tiêu chuẩn công nghiệp của Provectus (provectuslabs/kafka-ui). Trong đồ án Big Data, vai trò của em là kỹ sư tích hợp hạ tầng: Em đã cấu hình trong docker-compose.yml để liên kết nó vào mạng nội bộ của cụm Kafka KRaft qua cổng 29092 và thiết lập cơ chế Healthcheck để hệ thống khởi chạy đồng bộ, đóng vai trò là tầng giám sát (Observability) cho toàn bộ pipeline ạ."),
    ("Câu 2: Partition là gì? Tại sao topic chính chia 3 mà DLQ chỉ chia 1?",
     "Dạ thưa thầy, Partition là đơn vị song song hóa cơ bản của Kafka, tương tự như việc mở thêm các làn đường xe chạy: Topic chính financial_tx em chia 3 Partitions để cho phép tối đa 3 tiến trình đọc song song cùng lúc, giúp tăng gấp 3 lần tốc độ tiếp nhận (Velocity) mà không lo bị nghẽn. Còn financial_tx_dlq là Dead Letter Queue (ngách gom lỗi), vì tỉ lệ lỗi thực tế chỉ chiếm 1 - 2% nên lưu lượng rất thấp, chỉ cần 1 Partition là đủ, vừa tối ưu tài nguyên vừa gom toàn bộ lỗi vào một chỗ để dễ kiểm tra ạ."),
    ("Câu 3: Mấy cái thư mục bronze/ hay tx_date=... trên MinIO là do em tạo bằng tay trong Docker à?",
     "Dạ không ạ. Docker chỉ tạo cái thùng rỗng financial-datalake. Còn các cây thư mục bên trong là hoàn toàn tự động: Khi tiến trình streaming Python nhận dữ liệu từ Kafka, nó phân loại dữ liệu sạch thì tự động đẩy vào thư mục bronze/ chia theo ngày, còn dữ liệu lỗi thì tự động gom vào thư mục quarantine/ ạ."),
    ("Câu 4: Fault & Duplicate Injection trong script của em có ý nghĩa gì đối với bài toán Big Data?",
     "Dạ, trong giao dịch tài chính thực tế luôn có rủi ro về tính toàn vẹn (Veracity) do lỗi mạng hoặc ứng dụng người dùng. Em tích hợp Fault Injection để cố tình tạo ra các giao dịch tiền âm, thiếu mã tài khoản và trùng lặp mã giao dịch. Điều này giúp nhóm kiểm chứng được rằng hệ thống không nhận dữ liệu một cách mù quáng mà có tầng kiểm soát chất lượng nghiêm ngặt trước khi lưu vào Data Lake ạ.")
]

for q, a in qa:
    p_q = doc.add_paragraph()
    r_q = p_q.add_run(f"❓ {q}")
    r_q.bold = True
    r_q.font.color.rgb = RGBColor(180, 40, 40)
    p_a = doc.add_paragraph()
    r_a = p_a.add_run(f"👉 Trả lời: \"{a}\"")
    r_a.italic = True
    p_a.paragraph_format.space_after = Pt(6)

output_path = Path("/home/hungmg/Documents/Big Data/bigdata-financial-ingestion-storage/docs/tv1_kich_ban_thuyet_trinh.docx")
doc.save(str(output_path))
print(f"Exported DOCX successfully to: {output_path}")
