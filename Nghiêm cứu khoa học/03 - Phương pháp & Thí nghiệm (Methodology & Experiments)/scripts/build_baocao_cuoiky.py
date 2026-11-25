"""
KỊCH BẢN TẠO BÁO CÁO CUỐI KỲ TỔNG HỢP (.DOCX) — ĐỀ TÀI C (NHÓM 4 THÀNH VIÊN)
Tích hợp đầy đủ đóng góp của TV4 — Long (Mục 2.4, Chương 4, 2 hình 300 DPI, Tài liệu tham khảo IEEE)
và khung tổng hợp 5 chương chuẩn Đại học Sài Gòn (giữ nguyên khung chờ TV1, TV2, TV3).
"""

import io
import zipfile
from pathlib import Path

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
from docx.shared import Cm, Inches, Pt, RGBColor

BASE_DIR = Path(__file__).resolve().parents[2]
DRAFTS_DIR = BASE_DIR / "04 - Viết bài & Xuất bản (Writing & Publication)" / "Bản thảo (Drafts)"
ATTACH_DIR = BASE_DIR / "99 - Đính kèm (Attachments)"
MIDTERM_DOCX = DRAFTS_DIR / "Baocao.docx"
OUT_DOCX = DRAFTS_DIR / "BaoCao_CuoiKy_DeTaiC_Nhom4.docx"


def set_cell_shading(cell, fill_hex: str) -> None:
    shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading)


def set_table_borders(table, color="94A3B8", sz="4") -> None:
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:bottom w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:left w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:right w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:insideH w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:insideV w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f"</w:tblBorders>"
    )
    tblPr.append(borders)


def enable_update_fields(doc: Document) -> None:
    settings = doc.settings.element
    update_fields = OxmlElement("w:updateFields")
    update_fields.set(qn("w:val"), "true")
    settings.append(update_fields)


def add_toc(doc: Document) -> None:
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("MỤC LỤC")
    r.bold = True
    r.font.size = Pt(14)
    r.font.name = "Times New Roman"

    p_toc = doc.add_paragraph()
    run = p_toc.add_run()
    fldChar1 = OxmlElement("w:fldChar")
    fldChar1.set(qn("w:fldCharType"), "begin")
    instrText = OxmlElement("w:instrText")
    instrText.set(qn("xml:space"), "preserve")
    instrText.text = 'TOC \\o "1-3" \\h \\z \\u'
    fldChar2 = OxmlElement("w:fldChar")
    fldChar2.set(qn("w:fldCharType"), "separate")
    fldChar3 = OxmlElement("w:fldChar")
    fldChar3.set(qn("w:fldCharType"), "end")
    run._r.append(fldChar1)
    run._r.append(instrText)
    run._r.append(fldChar2)
    run._r.append(fldChar3)


def add_page_number_footer(doc: Document) -> None:
    section = doc.sections[1]
    footer = section.footer
    p = footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = p.add_run("Trang ")
    run.font.name = "Times New Roman"
    run.font.size = Pt(10)
    fld = OxmlElement("w:fldSimple")
    fld.set(qn("w:instr"), "PAGE")
    p._p.append(fld)


def configure_styles(doc: Document) -> None:
    normal = doc.styles["Normal"]
    normal.font.name = "Times New Roman"
    normal.font.size = Pt(13)
    normal.paragraph_format.line_spacing = 1.3
    normal.paragraph_format.space_after = Pt(6)

    for level, size, color in [
        ("Heading 1", 15, RGBColor(0x0F, 0x17, 0x2A)),
        ("Heading 2", 13.5, RGBColor(0x1E, 0x3A, 0x8A)),
        ("Heading 3", 13, RGBColor(0x1E, 0x29, 0x3B)),
    ]:
        st = doc.styles[level]
        st.font.name = "Times New Roman"
        st.font.size = Pt(size)
        st.font.bold = True
        st.font.color.rgb = color
        st.paragraph_format.space_before = Pt(10)
        st.paragraph_format.space_after = Pt(4)
        st.paragraph_format.keep_with_next = True


def add_prose(doc: Document, lead: str, body: str) -> None:
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if lead:
        r_lead = p.add_run(lead)
        r_lead.bold = True
    p.add_run(body)


def add_placeholder(doc: Document, text: str) -> None:
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.italic = True
    r.font.color.rgb = RGBColor(0x64, 0x74, 0x8B)


def add_figure(doc: Document, img_path: Path, caption: str, width_in: float = 6.1) -> None:
    if not img_path.exists():
        add_placeholder(doc, f"[Thiếu tệp hình ảnh: {img_path.name}]")
        return
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.keep_with_next = True
    p_img.add_run().add_picture(str(img_path), width=Inches(width_in))

    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p_cap.add_run(caption)
    r.italic = True
    r.font.size = Pt(11.5)
    r.font.color.rgb = RGBColor(0x33, 0x41, 0x55)


def add_styled_table(doc: Document, headers: list[str], rows: list[list[str]], col_widths_cm: list[float]) -> None:
    tbl = doc.add_table(rows=len(rows) + 1, cols=len(headers))
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl)

    for j, h in enumerate(headers):
        cell = tbl.rows[0].cells[j]
        cell.width = Cm(col_widths_cm[j])
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        set_cell_shading(cell, "1E3A8A")
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(2)
        r = p.add_run(h)
        r.bold = True
        r.font.size = Pt(11.5)
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    for i, row_data in enumerate(rows):
        for j, val in enumerate(row_data):
            cell = tbl.rows[i + 1].cells[j]
            cell.width = Cm(col_widths_cm[j])
            cell.vertical_alignment = WD_ALIGN_VERTICAL.TOP
            if i % 2 == 1:
                set_cell_shading(cell, "F8FAFC")
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(2)
            r = p.add_run(val)
            r.font.size = Pt(11)
            if j == 0:
                r.bold = True


def build_cover_page(doc: Document) -> None:
    sec0 = doc.sections[0]
    sec0.top_margin = Cm(2.0)
    sec0.bottom_margin = Cm(2.0)
    sec0.left_margin = Cm(2.5)
    sec0.right_margin = Cm(2.0)

    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl, color="1E3A8A", sz="12")
    cell = tbl.rows[0].cells[0]
    cell.width = Cm(16.5)

    def c_para(text="", size=13, bold=False, italic=False, space_after=6, color=RGBColor(0x0F, 0x17, 0x2A)):
        p = cell.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(space_after)
        if text:
            r = p.add_run(text)
            r.font.name = "Times New Roman"
            r.font.size = Pt(size)
            r.bold = bold
            r.italic = italic
            r.font.color.rgb = color
        return p

    p0 = cell.paragraphs[0]
    p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p0.paragraph_format.space_after = Pt(2)
    r0 = p0.add_run("TRƯỜNG ĐẠI HỌC SÀI GÒN")
    r0.font.name = "Times New Roman"
    r0.font.size = Pt(14)
    r0.bold = True

    c_para("KHOA CÔNG NGHỆ THÔNG TIN", size=14, bold=True, space_after=14)

    # Reuse SGU logo from midterm Baocao.docx if available
    if MIDTERM_DOCX.exists():
        with zipfile.ZipFile(MIDTERM_DOCX) as z:
            if "word/media/image4.jpeg" in z.namelist():
                logo_bytes = io.BytesIO(z.read("word/media/image4.jpeg"))
                p_logo = cell.add_paragraph()
                p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p_logo.paragraph_format.space_after = Pt(14)
                p_logo.add_run().add_picture(logo_bytes, width=Cm(3.2))

    c_para("BÁO CÁO NGHIÊN CỨU KHOA HỌC CUỐI KỲ", size=18, bold=True, space_after=6, color=RGBColor(0x1E, 0x3A, 0x8A))
    c_para("MÔN: PHƯƠNG PHÁP NGHIÊN CỨU KHOA HỌC TRONG CNTT", size=13, bold=True, space_after=14)
    c_para("ĐỀ TÀI C (NHÓM 4 THÀNH VIÊN):", size=13, bold=True, space_after=4)
    c_para(
        "HẠ TẦNG QUẢN TRỊ DỮ LIỆU HIỆN ĐẠI CHO HỌC MÁY QUY MÔ LỚN:\n"
        "LIÊN KẾT KIẾN TRÚC DATA LAKEHOUSE, TỐI ƯU HÓA LƯU TRỮ CỘT,\n"
        "THỰC THI VECTOR HÓA VÀ FEATURE STORE",
        size=13.5,
        bold=True,
        space_after=18,
    )

    info_lines = [
        "Nhóm thực hiện:",
        "TV1: Võ Huỳnh Minh Sang (Nhóm trưởng) — Tầng ACID Table Storage (Delta Lake)",
        "TV2: Cường — Tầng Open Columnar Storage (BtrBlocks)",
        "TV3: Bảo — Tầng Vectorized Execution (Photon)",
        "TV4: Long — Tầng ML Feature Store (FeathrPO) & Chương 4 (Phản biện, Hướng phát triển)",
    ]
    for idx, line in enumerate(info_lines):
        p_info = cell.add_paragraph()
        p_info.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p_info.paragraph_format.left_indent = Cm(1.2)
        p_info.paragraph_format.space_after = Pt(4 if idx < len(info_lines) - 1 else 28)
        r = p_info.add_run(line)
        r.font.name = "Times New Roman"
        r.font.size = Pt(12.5)
        r.bold = idx == 0

    c_para("GVHD: Vũ Ngọc Thanh Sang", size=13, bold=True, space_after=6)
    c_para("TP. Hồ Chí Minh, tháng 11/2026", size=12, italic=True, space_after=8)

    doc.add_section()
    sec1 = doc.sections[1]
    sec1.top_margin = Cm(2.0)
    sec1.bottom_margin = Cm(2.0)
    sec1.left_margin = Cm(2.5)
    sec1.right_margin = Cm(2.0)


def main() -> None:
    doc = Document()
    configure_styles(doc)
    enable_update_fields(doc)

    build_cover_page(doc)
    add_toc(doc)
    doc.add_page_break()
    add_page_number_footer(doc)

    # CHƯƠNG 1
    doc.add_heading("CHƯƠNG 1: MỞ ĐẦU VÀ ĐẶT VẤN ĐỀ", level=1)
    add_prose(
        doc,
        "Bối cảnh và động lực nghiên cứu: ",
        "Sự bùng nổ của các hệ thống Học máy quy mô doanh nghiệp đòi hỏi hạ tầng quản trị dữ liệu vừa có chi phí lưu trữ thấp trên Cloud Object Storage, vừa đáp ứng hiệu năng cao qua bốn tầng công nghệ liên hoàn: Định dạng tệp cột (BtrBlocks) → Tầng bảng giao dịch ACID (Delta Lake) → Động cơ thực thi vector hóa (Photon) → Đường ống đặc trưng Học máy (ML Feature Store). Đề tài trả lời ba câu hỏi nghiên cứu chung gồm RQ1 (sự dịch chuyển điểm nghẽn hiệu năng qua 4 tầng), RQ2 (cơ chế bổ trợ lẫn nhau giữa 4 công trình đỉnh cao PVLDB/SIGMOD) và RQ3 (các đánh đổi kỹ thuật và khoảng trống nghiên cứu khi tích hợp đồng thời).",
    )
    add_placeholder(doc, "[Ghi chú tích hợp: Phần diễn giải chi tiết Chương 1 chờ TV1 — Võ Huỳnh Minh Sang bổ sung bản thảo cuối kỳ.]")

    # CHƯƠNG 2
    doc.add_heading("CHƯƠNG 2: TỔNG QUAN 4 CÔNG TRÌNH NGHIÊN CỨU NỀN TẢNG", level=1)

    doc.add_heading("2.1. Tầng Định dạng Cột: BtrBlocks (ACM SIGMOD 2023)", level=2)
    add_placeholder(doc, "[Chờ TV2 — Cường bổ sung phân tích bài báo BtrBlocks (DOI: 10.1145/3589263), minh chứng Scopus/WoS và 02 hình vẽ lại.]")

    doc.add_heading("2.2. Tầng Bảng Giao dịch ACID: Delta Lake (PVLDB 2020)", level=2)
    add_prose(
        doc,
        "Vai trò trục trung tâm (TV1 — Sang): ",
        "Công trình \"Delta Lake: High-Performance ACID Table Storage over Cloud Object Stores\" (M. Armbrust et al., PVLDB Vol. 13, No. 12, pp. 3411–3424, Aug. 2020, DOI: 10.14778/3415478.3415560, Scopus Source ID 21100199855, Q1, CORE A*) đặt nền móng cho kiến trúc Data Lakehouse bằng nhật ký giao dịch _delta_log lưu trực tiếp trên Object Store, cơ chế kiểm soát đồng thời lạc quan (OCC), Data Skipping và Z-Order Clustering. Trên chuẩn TPC-DS 1 TB, Delta Lake đạt 0,93 giờ thực thi, tiết kiệm 75,3% thời gian (nhanh hơn 4,04×) so với Presto.",
    )
    add_figure(doc, ATTACH_DIR / "Hinh1_TaiTao_KienTruc_Pipeline.png", "Hình 2.2.1: Sơ đồ kiến trúc pipeline dữ liệu của Delta Lake (tái tạo từ Figure 1, PVLDB 2020).")
    add_figure(doc, ATTACH_DIR / "Hinh2_TaiTao_TPCDS_PowerTest.png", "Hình 2.2.2: Hiệu năng TPC-DS 1 TB Power Test của Delta Lake (tái tạo từ Figure 6, PVLDB 2020).")

    doc.add_heading("2.3. Tầng Thực thi Truy vấn Vector hóa: Photon (ACM SIGMOD 2022)", level=2)
    add_placeholder(doc, "[Chờ TV3 — Bảo bổ sung phân tích bài báo Photon (DOI: 10.1145/3514221.3526054), minh chứng Scopus/WoS và 02 hình vẽ lại.]")

    # MỤC 2.4 — TV4 LONG (HOÀN CHỈNH)
    doc.add_heading("2.4. Tầng Đường ống Đặc trưng Học máy: ML Feature Stores — FeathrPO (PVLDB 2023)", level=2)

    doc.add_heading("2.4.1. Thông tin và nguồn bài báo (Chuẩn Scopus / WoS / CORE A*)", level=3)
    add_prose(
        doc,
        "Thông tin xuất bản: ",
        "Bài báo mang tên \"Optimizing Data Pipelines for Machine Learning in Feature Stores\" (tạm dịch: Tối ưu hóa Đường ống Dữ liệu cho Học máy trong các Kho Đặc trưng), do nhóm 10 tác giả gồm Rui Liu (University of Chicago), Kwanghyun Park (Yonsei University), Fotis Psallidas, Xiaoyong Zhu, Rathijit Sen, Matteo Interlandi, Yuanyuan Tian, Jesús Camacho-Rodríguez (Microsoft), Jinghui Mo (LinkedIn) và Konstantinos Karanasos (Meta) thực hiện. Công trình công bố trên tạp chí Proceedings of the VLDB Endowment (PVLDB), Tập 16, Số 13, trang 4230–4239, tháng 8/2023 (Hội nghị VLDB lần thứ 49, Vancouver, Canada), mã ISSN 2150-8097 và DOI: 10.14778/3625054.3625060.",
    )
    add_prose(
        doc,
        "Minh chứng chỉ mục quốc tế: ",
        "Ấn phẩm PVLDB được Elsevier Scopus lập chỉ mục liên tục từ năm 2008 đến nay với Scopus Source ID: 21100199855 (https://www.scopus.com/sourceid/21100199855), đạt CiteScore trong khoảng 7,5–8,2 và chỉ số h-index vượt mốc 200. Trên hệ thống Clarivate Web of Science, ấn phẩm được xác thực tại Master Journal List qua ISSN 2150-8097 (thuộc WoS Core Collection: CPCI-S và ESCI), đạt xếp hạng CORE A* và phân hạng Q1 trên ScimagoJR (https://www.scimagojr.com/journalsearch.php?q=21100199855&tip=sid) ở các lĩnh vực Information Systems, Software và Hardware and Architecture.",
    )

    doc.add_heading("2.4.2. Phân tích nội dung nghiên cứu theo cấu trúc IMRAD", level=3)
    add_prose(
        doc,
        "Bối cảnh và khoảng trống nghiên cứu: ",
        "Trong quy trình MLOps quy mô lớn, Feature Store đóng vai trò như một hệ quản trị cơ sở dữ liệu chuyên biệt cho Học máy (DBMS-for-ML). Khi tạo tập dữ liệu huấn luyện từ lịch sử chuỗi thời gian, phép ghép Point-in-Time (PIT) Join bảo đảm với mỗi nhãn tại thời điểm t_obs chỉ ghép các đặc trưng phát sinh tại t_feat <= t_obs nhằm ngăn chặn rò rỉ dữ liệu (Data Leakage). Tuy nhiên, các Feature Store hiện hành thực thi PIT Join 3 chiều theo cách thức ngây thơ trên Apache Spark, phát sinh xáo trộn dữ liệu qua mạng (Shuffle) khổng lồ, tính toán lặp lại qua nhiều vòng thử nghiệm mô hình và thiếu các kỹ thuật tối ưu truy vấn kinh điển của CSDL quan hệ.",
    )
    add_prose(
        doc,
        "Mục tiêu, đối tượng và thiết kế thực nghiệm: ",
        "Nhóm tác giả phát triển lớp tối ưu FeathrPO tích hợp vào Feathr để trả lời hai câu hỏi nghiên cứu: liệu viết lại truy vấn dựa trên tái sử dụng kết hợp rút gọn semijoin và mô hình chi phí có ngăn ngừa suy thoái hiệu năng hay không (RQ1), và khi kết hợp chọn bố cục tự động thì hệ thống đạt mức tăng tốc bao nhiêu lần trên nhiều cài đặt PIT Join (RQ2). Thực nghiệm được triển khai trên cụm đám mây Azure Synapse (Feathr v0.7.2, Spark v3.1 trên YARN với 1 driver + 4 workers, mỗi node 8 vCores, 64 GB RAM) cùng cụm cục bộ (Ubuntu 20.04, 10 cores, 32 GB DRAM, Spark v3.2) qua bốn tập dữ liệu chuẩn được tổng hợp ở Bảng 2.4.1.",
    )

    add_styled_table(
        doc,
        ["Tập dữ liệu", "Bài toán ML", "Bảng Nhãn (L)", "Bảng Đặc trưng (F)", "Bảng Phụ trợ (A)"],
        [
            ["TPCxAI-UC7 (SF10)", "Gợi ý sản phẩm", "789.225 / 27 MB", "27.987.766 / 1,5 GB", "358.818 / 39 MB"],
            ["TPCxAI-UC10 (SF10)", "Phát hiện gian lận", "37.696 / 725 KB", "55.975.921 / 2,1 GB", "358.818 / 39 MB"],
            ["Favorita (Kaggle)", "Dự báo doanh số", "379 / 7,3 KB", "125.497.041 / 3,9 GB", "55 / 1,4 KB"],
            ["eCommerce (Kaggle)", "Dự đoán hành vi mua", "44.415 / 941 KB", "104.335.510 / 3,4 GB", "104.335.510 / 4,1 GB"],
        ],
        [3.3, 3.2, 3.2, 3.4, 3.4],
    )
    p_tbl_cap = doc.add_paragraph()
    p_tbl_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_tbl_cap = p_tbl_cap.add_run("Bảng 2.4.1: Thống kê 4 bộ dữ liệu đánh giá FeathrPO (nguồn: Table 1, Liu et al., PVLDB 2023, tr. 4236).")
    r_tbl_cap.italic = True
    r_tbl_cap.font.size = Pt(11)

    add_prose(
        doc,
        "Phương pháp tối ưu hóa và kết quả chính: ",
        "FeathrPO tích hợp ba kỹ thuật trụ cột: (1) Mô hình chi phí nhận biết bố cục dựa trên KLL Sketches (§4) giúp ước lượng phân vị thời gian đạt độ chính xác 96,84% – 99,73%, vượt trội mức 89,61% – 92,19% của Spark mặc định; (2) Tái sử dụng tính toán và Rút gọn Semijoin (§5) thông qua bộ Matcher và Rewriter để chỉ tính phần delta trên cửa sổ thời gian mới kèm lọc [min_ts, max_ts]; và (3) Chọn bố cục phân vùng thời gian tự động bằng Quy hoạch Nguyên Nhị phân BIP (§6) giải qua Google OR-Tools (glop solver) trong 6–7 giây cho 10.000 truy vấn và 1.000 bảng nguồn. Kết quả thực nghiệm chứng minh FeathrPO đạt mức tăng tốc tới 3,00× trên TPCxAI-UC10 (Cloud), tăng tốc 1,4× – 2,50× trên các thuật toán PIT Join khác (Early-stop Sort Merge, Union Merge), giữ mức cải thiện ổn định 1,3× – 2,3× khi mở rộng từ SF1 đến SF100 và tránh hoàn toàn suy thoái hiệu năng ở ngưỡng độ chọn lọc cao (80%–100%).",
    )

    doc.add_heading("2.4.3. Hai hình minh họa tự vẽ lại (300 DPI + Vector PDF)", level=3)
    add_figure(doc, ATTACH_DIR / "Hinh_TV4_1_KienTruc_FeathrPO.png", "Hình 2.4.1: Tái tạo Figure 8 (tr. 4235) — Kiến trúc tích hợp Data Layout Selector và Reuse-based Optimizer trong Feathr.")
    add_prose(
        doc,
        "Thuyết minh 7 tiêu chí cho Hình 2.4.1: ",
        "(1) Hình gốc là Figure 8 tại trang 4235 của bài báo; (2) Mục đích trực quan hóa vị trí tích hợp của 2 module mới (Data Layout Selector và Reuse-based Optimizer) vào kiến trúc Feathr trên Azure; (3) Thể hiện đầy đủ Python Client, cụm Feathr Client/Data Layout Selector, Feature Registry (Purview, Azure SQL), Apache Spark Runtime, Offline Stores và Online Stores; (4) Tái tạo bằng Python matplotlib (FancyBboxPatch và annotate) xuất 300 DPI kèm vector PDF; (5) Chứng minh thiết kế mở rộng không xâm lấn (non-intrusive), không cần chỉnh sửa lõi Spark; (6) Kết luận khoa học: đặt bộ tối ưu ở lớp Feature Store giúp tận dụng ngữ nghĩa đặc trưng độc lập backend; (7) So với bản gốc: giữ nguyên 100% thành phần và chiều mũi tên, Việt hóa chú giải và đồng nhất màu xanh lá cho hai module mới.",
    )

    add_figure(doc, ATTACH_DIR / "Hinh_TV4_2_HieuNang_FeathrPO.png", "Hình 2.4.2: Tái tạo Figure 12 (tr. 4237) — Hệ số cải thiện hiệu năng của FeathrPO qua 4 tập dữ liệu và 3 cài đặt PIT Join.")
    add_prose(
        doc,
        "Thuyết minh 7 tiêu chí cho Hình 2.4.2: ",
        "(1) Hình gốc là Figure 12 tại trang 4237 của bài báo; (2) Mục đích đánh giá mức tăng tốc đầu-cuối của FeathrPO; (3) Trục hoành gồm 3 thuật toán PIT Join (Feathr ZipPartition, Early-stop Sort Merge, Union Merge), 4 chuỗi cột ứng với 4 tập dữ liệu và trục tung là Hệ số cải thiện (0–4); (4) Dựng bằng Python numpy/matplotlib với họa tiết phân biệt, trong đó hai mốc đỉnh 3,00× và 2,50× lấy trực tiếp từ văn bản mục §8.2 và các cột còn lại trích xuất trực quan theo vạch chia trục tung ở độ chính xác 2 chữ số thập phân (1,32× đến 2,02×); (5) Toàn bộ 12 tổ hợp đều vượt mốc 1,00×, cao nhất tại TPCxAI-UC10; (6) Kết luận khoa học: cơ chế tối ưu mang tính cắm ghép đa nền tảng (pluggable); (7) So với bản gốc: giữ nguyên 3 nhóm thuật toán và 4 tập dữ liệu, bổ sung đường chuẩn 1.0×, nhãn số liệu 2 chữ số thập phân và hộp chú thích đỉnh 3,00×.",
    )

    doc.add_heading("2.4.4. Đánh giá và phản biện bài báo", level=3)
    add_prose(
        doc,
        "Điểm mạnh và hạn chế: ",
        "Công trình định vị chính xác nút thắt Point-in-Time Join trong MLOps, hiện thực hóa trực tiếp trên hệ thống mã nguồn mở Feathr và kiểm chứng trên chuẩn TPCx-AI với mức tăng tốc tới 3,00×. Dù vậy, bài báo còn ba hạn chế chính: phụ thuộc vào động cơ Spark (JVM) nên chưa tận dụng được định dạng giải mã nhanh thế hệ mới (BtrBlocks) hay thực thi vector hóa C++ (Photon); việc chọn đặc trưng vật chất hóa vẫn phụ thuộc cấu hình thủ công; và chưa mở rộng sang đường ống đặc trưng phi cấu trúc hay vector embeddings cho LLM/RAG.",
    )

    # CHƯƠNG 3
    doc.add_heading("CHƯƠNG 3: PHÂN TÍCH LIÊN KẾT, SO SÁNH ĐỐI CHIẾU VÀ KIẾN TRÚC TÍCH HỢP", level=1)
    add_placeholder(doc, "[Mục 3.1 (Sơ đồ tổng thể 4 tầng): Chờ TV1 — Sang bổ sung.]")
    add_placeholder(doc, "[Mục 3.2 (Ma trận so sánh 4 công trình): Chờ TV2 — Cường bổ sung.]")
    add_placeholder(doc, "[Mục 3.3 (Biểu đồ phân tích định lượng xuyên tầng): Chờ TV3 — Bảo bổ sung.]")

    # CHƯƠNG 4 — TV4 LONG (HOÀN CHỈNH)
    doc.add_heading("CHƯƠNG 4: PHẢN BIỆN, KHOẢNG TRỐNG NGHIÊN CỨU VÀ HƯỚNG PHÁT TRIỂN", level=1)
    add_prose(
        doc,
        "Mục tiêu chương (Chủ trì: TV4 — Long): ",
        "Chương 4 tổng hợp phân tích xuyên suốt bốn tầng kiến trúc (BtrBlocks → Delta Lake → Photon → ML Feature Store) nhằm giải đáp trực tiếp Câu hỏi Nghiên cứu RQ3 của toàn đề tài.",
    )

    doc.add_heading("4.1. Phân tích các sự đánh đổi (Trade-offs) xuyên suốt 4 tầng", level=2)
    add_styled_table(
        doc,
        ["Cặp tầng liên kết", "Sự đánh đổi (Trade-off)", "Phân tích kỹ thuật chuyên sâu"],
        [
            [
                "Tầng 1 (BtrBlocks) ↔ Tầng 2 (Delta Lake)",
                "Tỷ lệ nén tối đa vs. Tốc độ giải nén & Độ phổ cập chuẩn mở",
                "Parquet giúp Delta Lake tương thích đa công cụ nhưng giải nén chậm trên CPU đa nhân; BtrBlocks giải nén rất nhanh nhờ nén đệ quy thân thiện SIMD nhưng thay trực tiếp sẽ phá vỡ tương thích hệ sinh thái Parquet.",
            ],
            [
                "Tầng 2 (Delta Lake) ↔ Tầng 3 (Photon)",
                "Tính nhất quán ACID chặt chẽ vs. Độ trễ ghi/đọc thời gian thực",
                "Giao thức _delta_log và OCC bảo đảm ACID và Time Travel nhưng phát sinh chi phí quản lý metadata và nguy cơ xung đột ghi khi nhiều luồng cập nhật nhỏ liên tục.",
            ],
            [
                "Tầng 3 (Photon) ↔ Tầng 4 (Feature Store)",
                "Tốc độ Vectorized C++/SIMD vs. Tính linh hoạt UDF Python/ML",
                "Photon tăng tốc toán tử SQL bằng C++/SIMD, song phép biến đổi ML trong Feature Store thường chứa UDF Python/PyTorch nên dễ rơi về luồng xử lý chậm hoặc tốn chi phí tuần tự hóa C++ ↔ Python.",
            ],
            [
                "Tầng 4 (Feature Store) ↔ Object Store",
                "Tính toán sẵn (Pre-computation) vs. Chi phí lưu trữ & Độ tươi dữ liệu",
                "Vật chất hóa sẵn giúp train/serve nhanh nhưng nhân đôi chi phí lưu trữ và dễ lỗi thời; tính động bằng PIT Join mỗi lần train lại tốn CPU nếu thiếu bộ nhớ đệm xuyên tầng.",
            ],
        ],
        [3.8, 4.5, 8.2],
    )

    doc.add_heading("4.2. Tổng hợp khoảng trống nghiên cứu chung (Synthesized Research Gaps)", level=2)
    add_prose(
        doc,
        "Khoảng trống 1 — Thiếu bộ tối ưu hóa dựa trên chi phí xuyên tầng: ",
        "Tối ưu hóa hiện nay vẫn bị cắt khúc cục bộ ở từng lớp (byte/block trong BtrBlocks, metadata/Z-Order trong Delta Lake, vector hóa trong Photon và logic Feature Pipeline trong FeathrPO), chưa có trình tối ưu thống nhất biết đẩy thông tin ngữ nghĩa từ Feature Store xuống tầng bố cục và giải mã bên dưới.",
    )
    add_prose(
        doc,
        "Khoảng trống 2 — Điểm nghẽn chuyển đổi dữ liệu giữa Engine C++ và môi trường ML Python: ",
        "Dù Photon loại bỏ được JVM overhead, quá trình nạp dữ liệu từ Lakehouse vào PyTorch hay TensorFlow vẫn gánh chi phí sao chép bộ nhớ qua lại giữa C++ và Python do chưa chuẩn hóa hoàn toàn giao thức Zero-copy (Arrow Flight / DLPack) xuyên suốt toàn đường ống.",
    )
    add_prose(
        doc,
        "Khoảng trống 3 — Thiếu chuẩn đánh giá hiệu năng đầu-cuối thống nhất: ",
        "Các công trình hiện đo trên hệ quy chiếu rời rạc (micro-benchmark giải nén, TPC-DS SQL BI, TPCx-AI PIT Join), thiếu một bộ benchmark chung đo thông lượng trọn vẹn từ byte nén trên Object Store tới lúc nạp tensor vào GPU huấn luyện mô hình.",
    )

    doc.add_heading("4.3. Đề xuất hướng nghiên cứu mới (Future Research Directions)", level=2)
    add_prose(
        doc,
        "Hướng 1 — Tự động tối ưu hóa xuyên tầng cho AI-Ready Lakehouse: ",
        "Thiết kế cơ chế truyền gợi ý ngữ nghĩa (semantic hints) từ định nghĩa đặc trưng trong Feature Store (tần suất truy xuất khóa thực thể, cửa sổ thời gian, chính sách TTL) xuống thẳng Delta Lake để tự chọn khóa Z-Order/Partitioning và xuống BtrBlocks để chọn chiến lược nén phù hợp cho từng kiểu đặc trưng Học máy.",
    )
    add_prose(
        doc,
        "Hướng 2 — Hỗ trợ nguyên bản dữ liệu đa phương thức & Vector Embeddings cho AI/LLM: ",
        "Mở rộng kiến trúc bốn tầng để lưu trữ nguyên bản vector embeddings và dữ liệu phi cấu trúc ngay trong bảng ACID của Lakehouse, kết hợp tích hợp chỉ mục tìm kiếm vector (ANN Index) vào engine vector hóa nhằm phục vụ trực tiếp cho các đường ống RAG và Fine-tuning LLM.",
    )

    # CHƯƠNG 5
    doc.add_heading("CHƯƠNG 5: KẾT LUẬN VÀ TÀI LIỆU THAM KHẢO", level=1)
    add_placeholder(doc, "[Phần tổng kết câu trả lời RQ1–RQ3: Chờ TV1 — Sang chuẩn hóa sau khi ghép đủ Chương 1 và Chương 3.]")

    doc.add_heading("5.1. Danh mục tài liệu tham khảo (Chuẩn IEEE)", level=2)
    refs = [
        '[1] M. Armbrust et al., "Delta Lake: High-Performance ACID Table Storage over Cloud Object Stores," Proc. VLDB Endow., vol. 13, no. 12, pp. 3411–3424, Aug. 2020, doi: 10.14778/3415478.3415560.',
        '[2] M. Kuschewski, D. Sauerwein, A. Alhomssi, and V. Leis, "BtrBlocks: Efficient Columnar Compression for Data Lakes," Proc. ACM Manag. Data (SIGMOD), vol. 1, no. 2, pp. 1–26, Jun. 2023, doi: 10.1145/3589263.',
        '[3] A. Behm et al., "Photon: A Fast Query Engine for Lakehouse Systems," in Proc. ACM SIGMOD Int. Conf. Manag. Data, Jun. 2022, pp. 2326–2339, doi: 10.1145/3514221.3526054.',
        '[4] R. Liu et al., "Optimizing Data Pipelines for Machine Learning in Feature Stores," Proc. VLDB Endow., vol. 16, no. 13, pp. 4230–4239, Aug. 2023, doi: 10.14778/3625054.3625060.',
    ]
    for ref in refs:
        p = doc.add_paragraph(ref)
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.left_indent = Cm(0.8)
        p.paragraph_format.first_line_indent = Cm(-0.8)
        p.paragraph_format.space_after = Pt(4)

    doc.save(OUT_DOCX)
    print(f"Đã tạo báo cáo tổng hợp tại: {OUT_DOCX}")


if __name__ == "__main__":
    main()
