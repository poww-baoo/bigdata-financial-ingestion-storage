#!/usr/bin/env python3
"""
Word / OOXML Document Engineer Build Pipeline (ECMA-376) cho Báo cáo Cuối kỳ Đề tài C (05 bài báo).

Tính năng chuẩn Word chuyên nghiệp:
  1. Trang bìa Section 1 riêng, khung viền đôi màu đen phủ trọn khổ giấy A4 (lề 1.0 cm).
  2. Toàn bộ tiêu đề & văn bản màu đen tuyệt đối (#000000), Times New Roman chuẩn học thuật.
  3. Cấu hình sẵn Styles (Heading 1–3, Caption, TOC 1–3) trong word/styles.xml để khi nhấn
     F9 (Update Entire Table) trên Microsoft Word không bị nhảy font hay đổi màu xanh.
  4. MỤC LỤC TỰ ĐỘNG (Trang 3): trường Word `TOC \\o "1-2" \\h \\z \\u` kèm bookmark & hyperlink nội bộ.
  5. DANH MỤC HÌNH ẢNH TỰ ĐỘNG THEO CẤU TRÚC CÂY 3 TẦNG (Trang 4):
     - Nhúng trường ẩn `TC "..." \\f F \\l 1|2|3` tại đúng các Chương có hình (L1), Mục có hình (L2)
       và Chú thích hình ảnh (L3) để khi nhấn F9 trên Word, Danh mục hình ảnh tự động dựng lại
       đúng cấu trúc cây 3 tầng (Chương -> Mục -> Hình) mà không kéo theo chương không có hình
       và không làm nhiễu Mục lục chính.
     - Nhúng bookmark & hyperlink nội bộ click-to-jump cho cả Word và PDF.
  6. Số trang căn giữa đáy trang (chỉ hiển thị con số, ẩn trang bìa).
  7. Bảng không lặp tiêu đề khi sang trang (không gắn tblHeader).
  8. Quy trình 2-pass tự động đồng bộ 100% số trang chính xác từ PDF cho cả Mục lục & Danh mục hình ảnh.

Lưu ý: TUYỆT ĐỐI không đụng chạm đến bất kỳ file Báo cáo Giữa kỳ nào (Baocao.docx/pdf).
"""

import re
import subprocess
from pathlib import Path
import docx
from docx.shared import Cm, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.enum.section import WD_SECTION
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

VAULT = Path(__file__).resolve().parents[2]
DRAFTS = VAULT / "04 - Viết bài & Xuất bản (Writing & Publication)" / "Bản thảo (Drafts)"
ATTACH = VAULT / "99 - Đính kèm (Attachments)"

MD_PATH = DRAFTS / "BaoCao_CuoiKy_DeTaiC_Nhom4.md"
DOCX_PATH = DRAFTS / "BaoCao_CuoiKy_DeTaiC_Nhom4.docx"
PDF_PATH = DRAFTS / "BaoCao_CuoiKy_DeTaiC_Nhom4.pdf"
LOGO_PATH = ATTACH / "sgu_logo.jpeg"

COLOR_BLACK = RGBColor(0x00, 0x00, 0x00)
COLOR_PRIMARY = COLOR_BLACK
COLOR_DARK = COLOR_BLACK
COLOR_BODY = COLOR_BLACK
COLOR_MUTED = RGBColor(0x1F, 0x29, 0x37)

APPENDIX_GALLERY_ITEMS = [
    ("BtrBlocks_Hinh1_TaiTao_CayQuyetDinhNen.png", "Hình 2.1: Cây quyết định nén đệ quy BtrBlocks (Figure 3)"),
    ("BtrBlocks_Hinh2_TaiTao_S3ScanBenchmark.png", "Hình 2.2: Thông lượng quét S3 & chi phí BtrBlocks (Figure 1)"),
    ("Hinh1_TaiTao_KienTruc_Pipeline.png", "Hình 2.3: Đường ống Medallion trên Delta Lake (Figure 1)"),
    ("Hinh2_TaiTao_TPCDS_PowerTest.png", "Hình 2.4: Hiệu năng TPC-DS 1 TB Delta Lake (Figure 6)"),
    ("Hinh3_DeXuatMoi_HeSoTangToc.png", "Hình 2.5: Hệ số tăng tốc & tiết kiệm thời gian Delta Lake"),
    ("TV3_Hinh1_KienTruc_Photon.png", "Hình 2.6: Kiến trúc Databricks Runtime & Photon (Figure 1)"),
    ("TV3_Hinh2_TPCDS_Q24.png", "Hình 2.7: Tác động Adaptive Join Compaction Q24 (Figure 9)"),
    ("Hinh_TV4_1_KienTruc_FeathrPO.png", "Hình 2.8: Kiến trúc tích hợp FeathrPO (Figure 8)"),
    ("Hinh_TV4_2_HieuNang_FeathrPO.png", "Hình 2.9: Hiệu năng PIT Join của FeathrPO (Figure 12)"),
    ("TV1_Bai5_Hinh1_Autotune_Model.png", "Hình 2.10: Mô hình độ trễ AUTOTUNE tf.data (Figure 5)"),
    ("TV1_Bai5_Hinh2_MLPerf_Speedup.png", "Hình 2.11: Hệ số tăng tốc hội tụ MLPerf tf.data (Figure 8)"),
    ("TV1_Hinh_KienTruc_TichHop_5Tang.png", "Hình 3.1: Sơ đồ Kiến trúc Tích hợp Năm Tầng Đề xuất"),
    ("Hinh_TongHop_HieuNang_5Tang.png", "Hình 3.2: Tổng hợp định lượng hiệu năng năm tầng"),
    ("TV3_Hinh3_TongHop_HieuNang.png", "Hình A.1: Bản đối chiếu tổng hợp định lượng 4 tầng Lakehouse cốt lõi (Bổ sung)"),
]


class BookmarkCounter:
    def __init__(self):
        self.val = 1

    def next_id(self):
        cur = self.val
        self.val += 1
        return str(cur)


def clean_math_to_unicode(text: str) -> str:
    """Chuyển các biểu thức LaTeX inline sang ký hiệu Unicode chuẩn cho Word."""
    replacements = [
        (r"\$T_c = 86[,.]2\\text\{ Gbps\}\$", "Tc = 86,2 Gbps"),
        (r"\$T_u = 174[,.]6\\text\{ GB/s\}\$", "Tu = 174,6 GB/s"),
        (r"\$T_c\$", "Tc"),
        (r"\$T_u\$", "Tu"),
        (r"\$p_\{\\text\{empty\}\}\$", "p_empty"),
        (r"\$t_\{\\text\{feat\}\} \\le t_\{\\text\{obs\}\}\$", "t_feat ≤ t_obs"),
        (r"\$t_\{\\text\{obs\}\}\$", "t_obs"),
        (r"\$C_q = \\sum_\{s \\in S_q\} \\mathcal\{D\}_s - \\mathcal\{U\}_\{s_p\}\^q\$", "Cq = Σ(Ds) − Usp(q)"),
        (r"\$\\mathcal\{B\}\$", "B"),
        (r"\$%\s*\\text\{ Time Saved\} = \(1 - 1/\\text\{Speedup\}\) \\times 100%\$", "% Time Saved = (1 − 1/Speedup) × 100%"),
        (r"\$L\$", "L"),
        (r"\$F\$", "F"),
        (r"\$A\$", "A"),
        (r"\$x\$", "x"),
        (r"\$y\$", "y"),
        (r"\$n\$", "n"),
    ]
    out = text
    for pat, rep in replacements:
        out = re.sub(pat, rep, out)
    out = re.sub(
        r"\$([^$]+)\$",
        lambda m: (
            m.group(1)
            .replace(r"\times", "×")
            .replace(r"\le", "≤")
            .replace(r"\ge", "≥")
            .replace(r"\%", "%")
            .replace(r"\text{", "")
            .replace("}", "")
        ),
        out,
    )
    out = out.replace(r"\%", "%")
    return out


def strip_md_inline(text: str) -> str:
    t = clean_math_to_unicode(text).replace(r"\*", "\x00STAR\x00")
    t = re.sub(r"\*\*([^*]+)\*\*", r"\1", t)
    t = re.sub(r"\*([^*]+)\*", r"\1", t)
    t = re.sub(r"`([^`]+)`", r"\1", t)
    return t.replace("\x00STAR\x00", "*").strip()


def set_run_font(run, size=12.5, bold=False, italic=False, color=COLOR_BLACK, font_name="Times New Roman"):
    run.font.name = font_name
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    run.font.color.rgb = color
    rPr = run._r.get_or_add_rPr()
    rFonts = rPr.find(qn("w:rFonts"))
    if rFonts is None:
        rFonts = OxmlElement("w:rFonts")
        rPr.insert(0, rFonts)
    for attr in ("ascii", "hAnsi", "eastAsia", "cs"):
        rFonts.set(qn(f"w:{attr}"), font_name)


def configure_word_styles(doc):
    """Chuẩn hóa styles trong word/styles.xml (Times New Roman, đen tuyệt đối) để F9 không làm vỡ định dạng."""
    normal = doc.styles["Normal"]
    normal.font.name = "Times New Roman"
    normal.font.size = Pt(12.2)
    normal.font.color.rgb = COLOR_BLACK

    heading_specs = [
        ("Heading 1", 14.5, True, False, 0),
        ("Heading 2", 13.0, True, False, 1),
        ("Heading 3", 12.0, True, False, 2),
        ("Caption", 10.5, False, True, None),
    ]
    for name, sz, b, it, outline_lvl in heading_specs:
        try:
            st = doc.styles[name]
        except KeyError:
            st = doc.styles.add_style(name, docx.enum.style.WD_STYLE_TYPE.PARAGRAPH)
        st.font.name = "Times New Roman"
        st.font.size = Pt(sz)
        st.font.bold = b
        st.font.italic = it
        st.font.color.rgb = COLOR_BLACK
        rPr = st.element.get_or_add_rPr()
        rFonts = rPr.find(qn("w:rFonts"))
        if rFonts is None:
            rFonts = OxmlElement("w:rFonts")
            rPr.insert(0, rFonts)
        for attr in ("ascii", "hAnsi", "eastAsia", "cs"):
            rFonts.set(qn(f"w:{attr}"), "Times New Roman")
        if outline_lvl is not None:
            pPr = st.element.get_or_add_pPr()
            for old in pPr.findall(qn("w:outlineLvl")):
                pPr.remove(old)
            ol = OxmlElement("w:outlineLvl")
            ol.set(qn("w:val"), str(outline_lvl))
            pPr.append(ol)

    # Cấu hình sẵn TOC 1, TOC 2, TOC 3 cho Word khi người dùng bấm Update Table (F9)
    toc_specs = [
        ("TOC 1", 11.0, True, 0.0, 3, 2),
        ("TOC 2", 10.5, False, 0.55, 1, 1),
        ("TOC 3", 10.0, False, 1.15, 0.5, 0.5),
    ]
    for name, sz, b, indent_cm, sb, sa in toc_specs:
        try:
            st = doc.styles[name]
        except KeyError:
            st = doc.styles.add_style(name, docx.enum.style.WD_STYLE_TYPE.PARAGRAPH)
        st.font.name = "Times New Roman"
        st.font.size = Pt(sz)
        st.font.bold = b
        st.font.color.rgb = COLOR_BLACK
        st.paragraph_format.left_indent = Cm(indent_cm)
        st.paragraph_format.space_before = Pt(sb)
        st.paragraph_format.space_after = Pt(sa)
        st.paragraph_format.line_spacing = 1.12
        rPr = st.element.get_or_add_rPr()
        rFonts = rPr.find(qn("w:rFonts"))
        if rFonts is None:
            rFonts = OxmlElement("w:rFonts")
            rPr.insert(0, rFonts)
        for attr in ("ascii", "hAnsi", "eastAsia", "cs"):
            rFonts.set(qn(f"w:{attr}"), "Times New Roman")
        pPr = st.element.get_or_add_pPr()
        for old_tabs in pPr.findall(qn("w:tabs")):
            pPr.remove(old_tabs)
        pPr.append(parse_xml(f'<w:tabs {nsdecls("w")}><w:tab w:val="right" w:leader="dot" w:pos="9070"/></w:tabs>'))


def add_bookmark(paragraph, bm_name: str, counter: BookmarkCounter):
    """Chèn cặp w:bookmarkStart / w:bookmarkEnd bao quanh đoạn để hỗ trợ hyperlink nội bộ."""
    bm_id = counter.next_id()
    start = OxmlElement("w:bookmarkStart")
    start.set(qn("w:id"), bm_id)
    start.set(qn("w:name"), bm_name)
    end = OxmlElement("w:bookmarkEnd")
    end.set(qn("w:id"), bm_id)
    p = paragraph._p
    # Đặt bookmarkStart ngay sau pPr (nếu có)
    insert_pos = 1 if (len(p) > 0 and p[0].tag == qn("w:pPr")) else 0
    p.insert(insert_pos, start)
    p.append(end)


def add_tc_field(paragraph, label: str, table_id: str, level: int):
    """Nhúng trường ẩn TC (Table of Contents Entry) chuẩn OOXML cho Danh mục hình ảnh phân cấp."""
    safe_label = label.replace('"', "'")
    r_begin = OxmlElement("w:r")
    rPr1 = OxmlElement("w:rPr")
    rPr1.append(OxmlElement("w:vanish"))
    r_begin.append(rPr1)
    fld_begin = OxmlElement("w:fldChar")
    fld_begin.set(qn("w:fldCharType"), "begin")
    r_begin.append(fld_begin)

    r_instr = OxmlElement("w:r")
    rPr2 = OxmlElement("w:rPr")
    rPr2.append(OxmlElement("w:vanish"))
    r_instr.append(rPr2)
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = f' TC "{safe_label}" \\f {table_id} \\l "{level}" '
    r_instr.append(instr)

    r_end = OxmlElement("w:r")
    rPr3 = OxmlElement("w:rPr")
    rPr3.append(OxmlElement("w:vanish"))
    r_end.append(rPr3)
    fld_end = OxmlElement("w:fldChar")
    fld_end.set(qn("w:fldCharType"), "end")
    r_end.append(fld_end)

    paragraph._p.append(r_begin)
    paragraph._p.append(r_instr)
    paragraph._p.append(r_end)


def add_hyperlink_toc_runs(paragraph, anchor: str, text: str, page_str: str, size: float, bold: bool, italic: bool = False):
    """Tạo dòng mục lục có hyperlink nội bộ w:hyperlink bấm nhảy tới bookmark (màu đen, không gạch chân)."""
    hl = OxmlElement("w:hyperlink")
    hl.set(qn("w:anchor"), anchor)
    hl.set(qn("w:history"), "1")

    def make_run(t_val, is_tab=False):
        r = OxmlElement("w:r")
        rPr = OxmlElement("w:rPr")
        rFonts = OxmlElement("w:rFonts")
        for attr in ("ascii", "hAnsi", "eastAsia", "cs"):
            rFonts.set(qn(f"w:{attr}"), "Times New Roman")
        rPr.append(rFonts)
        if bold:
            rPr.append(OxmlElement("w:b"))
        if italic:
            rPr.append(OxmlElement("w:i"))
        col = OxmlElement("w:color")
        col.set(qn("w:val"), "000000")
        rPr.append(col)
        u = OxmlElement("w:u")
        u.set(qn("w:val"), "none")
        rPr.append(u)
        sz = OxmlElement("w:sz")
        sz.set(qn("w:val"), str(int(round(size * 2))))
        rPr.append(sz)
        szCs = OxmlElement("w:szCs")
        szCs.set(qn("w:val"), str(int(round(size * 2))))
        rPr.append(szCs)
        r.append(rPr)
        if is_tab:
            r.append(OxmlElement("w:tab"))
        else:
            t = OxmlElement("w:t")
            t.set(qn("xml:space"), "preserve")
            t.text = t_val
            r.append(t)
        return r

    hl.append(make_run(text))
    hl.append(make_run("", is_tab=True))
    hl.append(make_run(page_str))
    paragraph._p.append(hl)


def add_formatted_runs(p, text, base_size=12.5, base_color=COLOR_BLACK, base_bold=False, base_italic=False):
    """Phân tích **bold**, *italic*, `code` inline (bảo toàn \\* như CORE A*)."""
    STAR = "\x00STAR\x00"
    text = clean_math_to_unicode(text).replace(r"\*", STAR)
    token_pat = re.compile(r"(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`)")
    pos = 0
    for m in token_pat.finditer(text):
        if m.start() > pos:
            r = p.add_run(text[pos:m.start()].replace(STAR, "*"))
            set_run_font(r, size=base_size, bold=base_bold, italic=base_italic, color=base_color)
        tok = m.group(0)
        if tok.startswith("**") and tok.endswith("**"):
            inner = tok[2:-2].replace(STAR, "*")
            r = p.add_run(inner)
            set_run_font(r, size=base_size, bold=True, italic=base_italic, color=base_color)
        elif tok.startswith("*") and tok.endswith("*"):
            inner = tok[1:-1].replace(STAR, "*")
            r = p.add_run(inner)
            set_run_font(r, size=base_size, bold=base_bold, italic=True, color=base_color)
        elif tok.startswith("`") and tok.endswith("`"):
            inner = tok[1:-1].replace(STAR, "*")
            r = p.add_run(inner)
            set_run_font(r, size=max(base_size - 0.5, 9.0), bold=base_bold, italic=False, color=base_color)
        pos = m.end()
    if pos < len(text):
        r = p.add_run(text[pos:].replace(STAR, "*"))
        set_run_font(r, size=base_size, bold=base_bold, italic=base_italic, color=base_color)


def set_cell_shading(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>'))


def set_cell_margins(cell, top=80, bottom=80, left=110, right=110):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement("w:tcMar")
    for m, val in (("top", top), ("bottom", bottom), ("left", left), ("right", right)):
        node = OxmlElement(f"w:{m}")
        node.set(qn("w:w"), str(val))
        node.set(qn("w:type"), "dxa")
        tcMar.append(node)
    tcPr.append(tcMar)


def set_table_borders(table, color="666666", sz="4"):
    tblPr = table._tbl.tblPr
    tblPr.append(parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:left w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:bottom w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:right w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:insideH w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:insideV w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'</w:tblBorders>'
    ))


def add_page_number_footer(section):
    """Chỉ hiển thị số trang, căn giữa đáy trang (không tên đề tài, không chữ 'Trang')."""
    section.footer.is_linked_to_previous = False
    p = section.footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p._p.append(parse_xml(
        f'<w:fldSimple {nsdecls("w")} w:instr="PAGE">'
        f'<w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:eastAsia="Times New Roman" w:cs="Times New Roman"/>'
        f'<w:sz w:val="22"/><w:color w:val="000000"/></w:rPr><w:t>2</w:t></w:r>'
        f'</w:fldSimple>'
    ))


def enable_update_fields_on_open(doc):
    """Bật cờ updateFields=true để Word tự cập nhật Mục lục & Danh mục hình ảnh khi mở."""
    settings_el = doc.settings.element
    if settings_el.find(qn("w:updateFields")) is None:
        uf = OxmlElement("w:updateFields")
        uf.set(qn("w:val"), "true")
        settings_el.append(uf)


def build_cover_page(doc):
    """Trang 1 (Section 1 riêng): Trang bìa khung viền đen phủ trọn khổ A4."""
    sec0 = doc.sections[0]
    sec0.page_width = Cm(21.0)
    sec0.page_height = Cm(29.7)
    sec0.top_margin = Cm(1.0)
    sec0.bottom_margin = Cm(1.0)
    sec0.left_margin = Cm(1.0)
    sec0.right_margin = Cm(1.0)
    sec0.header_distance = Cm(0.5)
    sec0.footer_distance = Cm(0.5)

    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    tbl.columns[0].width = Cm(19.0)
    cell = tbl.cell(0, 0)
    cell.width = Cm(19.0)

    tcPr = cell._tc.get_or_add_tcPr()
    tcPr.append(parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'<w:top w:val="double" w:sz="18" w:space="0" w:color="000000"/>'
        f'<w:left w:val="double" w:sz="18" w:space="0" w:color="000000"/>'
        f'<w:bottom w:val="double" w:sz="18" w:space="0" w:color="000000"/>'
        f'<w:right w:val="double" w:sz="18" w:space="0" w:color="000000"/>'
        f'</w:tcBorders>'
    ))
    set_cell_margins(cell, top=520, bottom=440, left=560, right=560)

    trPr = tbl.rows[0]._tr.get_or_add_trPr()
    trH = OxmlElement("w:trHeight")
    trH.set(qn("w:val"), "15100")
    trH.set(qn("w:hRule"), "exact")
    trPr.append(trH)

    def add_cov_p(text, size=13, bold=False, italic=False, align=WD_ALIGN_PARAGRAPH.CENTER, before=0, after=4, left_indent=0):
        p = cell.add_paragraph() if len(cell.paragraphs) > 1 or cell.paragraphs[0].text else cell.paragraphs[0]
        p.alignment = align
        p.paragraph_format.space_before = Pt(before)
        p.paragraph_format.space_after = Pt(after)
        p.paragraph_format.line_spacing = 1.3
        if left_indent:
            p.paragraph_format.left_indent = Cm(left_indent)
        if text:
            set_run_font(p.add_run(text), size=size, bold=bold, italic=italic, color=COLOR_BLACK)
        return p

    add_cov_p("TRƯỜNG ĐẠI HỌC SÀI GÒN", size=15, bold=True, before=12, after=3)
    add_cov_p("KHOA CÔNG NGHỆ THÔNG TIN", size=15, bold=True, before=0, after=28)

    p_logo = cell.add_paragraph()
    p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_logo.paragraph_format.space_before = Pt(6)
    p_logo.paragraph_format.space_after = Pt(34)
    if LOGO_PATH.exists():
        p_logo.add_run().add_picture(str(LOGO_PATH), width=Cm(4.2))

    add_cov_p("BÁO CÁO BÀI TẬP CUỐI KỲ", size=22, bold=True, before=8, after=10)
    add_cov_p("MÔN: PHƯƠNG PHÁP NGHIÊN CỨU KHOA HỌC TRONG CNTT", size=14, bold=True, before=0, after=20)
    add_cov_p(
        "Đề tài: PHÂN TÍCH VÀ ĐỀ XUẤT KIẾN TRÚC TÍCH HỢP HẠ TẦNG QUẢN TRỊ DỮ LIỆU "
        "CHO HỌC MÁY QUY MÔ LỚN TRÊN NỀN TẢNG DATA LAKEHOUSE ĐÁM MÂY "
        "QUA KHẢO CỨU SO SÁNH NĂM CÔNG TRÌNH PVLDB/SIGMOD GIAI ĐOẠN 2020–2023",
        size=13.0, bold=True, before=6, after=34
    )

    add_cov_p("Lớp: DCT123C4", size=13, bold=True, align=WD_ALIGN_PARAGRAPH.LEFT, before=12, after=6, left_indent=3.0)
    add_cov_p("Nhóm sinh viên thực hiện (04 thành viên — 05 bài báo):", size=13, bold=True, align=WD_ALIGN_PARAGRAPH.LEFT, before=2, after=6, left_indent=3.0)

    for m in (
        "1. Võ Huỳnh Minh Sang – MSSV: 3123411256 (Nhóm trưởng)",
        "2. Nguyễn Đình Cường – MSSV: 3123411043",
        "3. Châu Quốc Bảo – MSSV: 3123411024",
        "4. Nguyễn Hoàng Long – MSSV: 3123411179",
    ):
        add_cov_p(m, size=12.5, bold=False, align=WD_ALIGN_PARAGRAPH.LEFT, before=0, after=4, left_indent=3.6)

    add_cov_p("Giảng viên hướng dẫn: Vũ Ngọc Thanh Sang", size=13.5, bold=True, before=56, after=44)
    add_cov_p("TP. Hồ Chí Minh, tháng 11 năm 2026", size=12.5, italic=True, before=18, after=0)

    sec1 = doc.add_section(WD_SECTION.NEW_PAGE)
    sec1.page_width = Cm(21.0)
    sec1.page_height = Cm(29.7)
    sec1.top_margin = Cm(2.2)
    sec1.bottom_margin = Cm(2.2)
    sec1.left_margin = Cm(2.8)
    sec1.right_margin = Cm(2.2)
    add_page_number_footer(sec1)


def add_dynamic_toc_block(doc, heading_text, instr_code, entries, page_map, is_tree=False):
    """
    Dựng trang Mục lục tự động chuẩn OOXML (begin -> instrText -> separate -> cached hyperlinks -> end).
    entries: list of (level, display_label, lookup_key, bookmark_name)
    """
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.page_break_before = True
    p_title.paragraph_format.space_before = Pt(4)
    p_title.paragraph_format.space_after = Pt(12)
    set_run_font(p_title.add_run(heading_text), size=15.5, bold=True, color=COLOR_BLACK)

    for idx, (level, display_label, lookup_key, bm_name) in enumerate(entries):
        style_name = f"TOC {min(level, 3)}"
        p = doc.add_paragraph(style=style_name)
        if is_tree:
            # Tinh chỉnh gọn để toàn bộ cây 3 tầng (14 hình + Chương + Mục) vừa trọn 1 trang A4
            if level == 1:
                p.paragraph_format.space_before = Pt(5 if idx > 0 else 1)
                p.paragraph_format.space_after = Pt(1.5)
                p.paragraph_format.left_indent = Cm(0.0)
                sz, is_b, is_it = 10.5, True, False
            elif level == 2:
                p.paragraph_format.space_before = Pt(2.5)
                p.paragraph_format.space_after = Pt(1)
                p.paragraph_format.left_indent = Cm(0.55)
                sz, is_b, is_it = 10.0, True, False
            else:
                p.paragraph_format.space_before = Pt(0.5)
                p.paragraph_format.space_after = Pt(1)
                p.paragraph_format.left_indent = Cm(1.15)
                sz, is_b, is_it = 9.7, False, False
            p.paragraph_format.line_spacing = 1.12
        else:
            p.paragraph_format.space_before = Pt(3 if level == 1 else 1)
            p.paragraph_format.space_after = Pt(2.5 if level == 1 else 1.2)
            p.paragraph_format.left_indent = Cm(0.0 if level == 1 else 0.6)
            p.paragraph_format.line_spacing = 1.15
            sz = 11.2 if level == 1 else 10.6
            is_b = (level == 1)
            is_it = False

        pPr = p._p.get_or_add_pPr()
        for old_tabs in pPr.findall(qn("w:tabs")):
            pPr.remove(old_tabs)
        pPr.append(parse_xml(f'<w:tabs {nsdecls("w")}><w:tab w:val="right" w:leader="dot" w:pos="9070"/></w:tabs>'))

        if idx == 0:
            r_begin = OxmlElement("w:r")
            fb = OxmlElement("w:fldChar")
            fb.set(qn("w:fldCharType"), "begin")
            r_begin.append(fb)
            p._p.append(r_begin)

            r_instr = OxmlElement("w:r")
            ins = OxmlElement("w:instrText")
            ins.set(qn("xml:space"), "preserve")
            ins.text = instr_code
            r_instr.append(ins)
            p._p.append(r_instr)

            r_sep = OxmlElement("w:r")
            fs = OxmlElement("w:fldChar")
            fs.set(qn("w:fldCharType"), "separate")
            r_sep.append(fs)
            p._p.append(r_sep)

        pg = str(page_map.get(lookup_key, "5"))
        add_hyperlink_toc_runs(p, bm_name, display_label, pg, size=sz, bold=is_b, italic=is_it)

        if idx == len(entries) - 1:
            r_end = OxmlElement("w:r")
            fe = OxmlElement("w:fldChar")
            fe.set(qn("w:fldCharType"), "end")
            r_end.append(fe)
            p._p.append(r_end)


def parse_markdown_sections(md_text):
    lines = md_text.splitlines()
    intro_lines = []
    body_lines = []
    mode = "header"
    for line in lines:
        if line.strip() == "# LỜI MỞ ĐẦU":
            mode = "intro"
            continue
        elif line.startswith("# CHƯƠNG 1:"):
            mode = "body"
            body_lines.append(line)
            continue
        if mode == "intro":
            if line.strip() == "---":
                continue
            intro_lines.append(line)
        elif mode == "body":
            body_lines.append(line)
    return intro_lines, body_lines


def analyze_document_structure(body_lines):
    """
    Quét trước toàn bộ body_lines để tạo:
      - toc_entries: (level, display_label, lookup_key, bookmark_name) cho Mục lục chính (H1, H2)
      - fig_tree_entries: (level, display_label, lookup_key, bookmark_name) cho Danh mục hình ảnh phân cấp 3 tầng
      - tc_meta: mapping heading/caption -> (tc_label, level, bookmark_name) để nhúng trường TC ẩn chính xác
    """
    toc_entries = []
    raw_fig_nodes = []  # list of (h1_title, h2_title, fig_caption, fig_bm)
    bm_by_key = {}

    cur_h1 = None
    cur_h2 = None
    h1_idx = 0
    h2_idx = 0
    fig_idx = 0

    for ln in body_lines:
        s = ln.strip()
        if s.startswith("# "):
            h1_idx += 1
            cur_h1 = strip_md_inline(s[2:])
            cur_h2 = None
            bm = f"_TocH1_{h1_idx}"
            bm_by_key[cur_h1] = bm
            toc_entries.append((1, cur_h1, cur_h1, bm))
        elif s.startswith("## "):
            h2_idx += 1
            cur_h2 = strip_md_inline(s[3:])
            bm = f"_TocH2_{h2_idx}"
            bm_by_key[cur_h2] = bm
            toc_entries.append((2, cur_h2, cur_h2, bm))
        else:
            m_img = re.match(r"^!\[([^\]]+)\]\(<([^>]+)>\)$", s) or re.match(r"^!\[([^\]]+)\]\((.+)\)$", s)
            if m_img:
                fig_idx += 1
                cap = strip_md_inline(m_img.group(1))
                bm = f"_Fig_{fig_idx}"
                bm_by_key[cap] = bm
                raw_fig_nodes.append((cur_h1, cur_h2, cap, bm))
            elif s == "<!-- APPENDIX_GALLERY -->":
                # Hình A.1 là hình bổ sung duy nhất chỉ xuất hiện ở Phụ lục A.2
                fig_idx += 1
                cap_a1 = APPENDIX_GALLERY_ITEMS[-1][1]
                bm = f"_Fig_{fig_idx}"
                bm_by_key[cap_a1] = bm
                raw_fig_nodes.append((cur_h1, cur_h2, cap_a1, bm))

    # Nhóm theo cây phân tầng: Chương (L1) -> Mục (L2) -> Các hình thuộc mục (L3)
    tree_map = {}  # h1 -> { h2 -> [ (cap, bm), ... ] }
    for h1, h2, cap, bm in raw_fig_nodes:
        tree_map.setdefault(h1, {}).setdefault(h2, []).append((cap, bm))

    fig_tree_entries = []
    tc_for_h1 = {}
    tc_for_h2 = {}
    tc_for_fig = {}

    for h1, h2_dict in tree_map.items():
        h1_bm = bm_by_key[h1]
        fig_tree_entries.append((1, h1, h1, h1_bm))
        tc_for_h1[h1] = h1
        for h2, figs in h2_dict.items():
            h2_bm = bm_by_key[h2]
            fig_tree_entries.append((2, h2, h2, h2_bm))
            tc_for_h2[h2] = h2
            for fi, (cap, fbm) in enumerate(figs):
                branch = "└─ " if fi == len(figs) - 1 else "├─ "
                short_cap = re.sub(r"\s+—\s+Tái tạo từ\s+", " — ", cap)
                display = f"{branch}{short_cap}"
                fig_tree_entries.append((3, display, cap, fbm))
                tc_for_fig[cap] = (display, fbm)

    return toc_entries, fig_tree_entries, bm_by_key, tc_for_h1, tc_for_h2, tc_for_fig


def add_table_from_md(doc, table_lines):
    rows_data = []
    for ln in table_lines:
        stripped = ln.strip().strip("|")
        cells = [c.strip() for c in stripped.split("|")]
        if all(re.fullmatch(r"[:\- ]+", c) for c in cells):
            continue
        rows_data.append(cells)
    if not rows_data:
        return

    ncols = len(rows_data[0])
    table = doc.add_table(rows=len(rows_data), cols=ncols)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = True
    set_table_borders(table, color="666666", sz="4")

    font_sz = 9.0 if ncols >= 6 else (9.5 if ncols == 5 else 10.2)

    for ri, rdata in enumerate(rows_data):
        row = table.rows[ri]
        trPr = row._tr.get_or_add_trPr()
        trPr.append(OxmlElement("w:cantSplit"))
        # KHÔNG dùng tblHeader để tiêu đề bảng chỉ xuất hiện đúng 1 lần

        for ci in range(ncols):
            val = rdata[ci] if ci < len(rdata) else ""
            cell = row.cells[ci]
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            set_cell_margins(cell, top=60, bottom=60, left=80, right=80)
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(1)
            p.paragraph_format.line_spacing = 1.12
            if ri == 0:
                set_cell_shading(cell, "E5E7EB")
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                add_formatted_runs(p, val, base_size=font_sz, base_color=COLOR_BLACK, base_bold=True)
            else:
                if ri % 2 == 0:
                    set_cell_shading(cell, "F9FAFB")
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                add_formatted_runs(p, val, base_size=font_sz, base_color=COLOR_BLACK)

    p_sp = doc.add_paragraph()
    p_sp.paragraph_format.space_before = Pt(0)
    p_sp.paragraph_format.space_after = Pt(4)


def add_appendix_image_gallery(doc, bm_counter: BookmarkCounter, tc_for_fig: dict):
    """Lưới bộ sưu tập 2 ảnh/hàng (14 ảnh) ở Phụ lục A.2, gắn bookmark + TC field cho Hình A.1."""
    rows_needed = (len(APPENDIX_GALLERY_ITEMS) + 1) // 2
    tbl = doc.add_table(rows=rows_needed, cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    set_table_borders(tbl, color="CBD5E1", sz="4")

    for r_idx in range(rows_needed):
        row = tbl.rows[r_idx]
        trPr = row._tr.get_or_add_trPr()
        trPr.append(OxmlElement("w:cantSplit"))
        for c_idx in range(2):
            item_idx = r_idx * 2 + c_idx
            cell = row.cells[c_idx]
            cell.width = Cm(7.9)
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            set_cell_margins(cell, top=90, bottom=90, left=90, right=90)
            if item_idx >= len(APPENDIX_GALLERY_ITEMS):
                continue
            fname, cap = APPENDIX_GALLERY_ITEMS[item_idx]
            img_path = ATTACH / fname
            p_img = cell.paragraphs[0]
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(2)
            p_img.paragraph_format.space_after = Pt(4)
            if img_path.exists():
                p_img.add_run().add_picture(str(img_path), width=Cm(7.3))
            p_cap = cell.add_paragraph(style="Caption")
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_before = Pt(0)
            p_cap.paragraph_format.space_after = Pt(2)
            p_cap.paragraph_format.line_spacing = 1.12
            set_run_font(p_cap.add_run(cap), size=9.2, italic=True, color=COLOR_BLACK)
            if cap in tc_for_fig:
                tc_lbl, fbm = tc_for_fig[cap]
                add_bookmark(p_cap, fbm, bm_counter)
                add_tc_field(p_cap, tc_lbl, "F", 3)


def render_lines(doc, lines, bm_counter, bm_by_key=None, tc_for_h1=None, tc_for_h2=None, tc_for_fig=None, is_intro=False):
    bm_by_key = bm_by_key or {}
    tc_for_h1 = tc_for_h1 or {}
    tc_for_h2 = tc_for_h2 or {}
    tc_for_fig = tc_for_fig or {}

    i = 0
    n = len(lines)
    first_h1_seen = False

    while i < n:
        ln = lines[i].rstrip()
        stripped = ln.strip()

        if not stripped or stripped == "---":
            i += 1
            continue

        if stripped == "<!-- APPENDIX_GALLERY -->":
            add_appendix_image_gallery(doc, bm_counter, tc_for_fig)
            i += 1
            continue

        if stripped.startswith("|"):
            tbl_lines = []
            while i < n and lines[i].strip().startswith("|"):
                tbl_lines.append(lines[i])
                i += 1
            add_table_from_md(doc, tbl_lines)
            continue

        m_img = re.match(r"^!\[([^\]]+)\]\(<([^>]+)>\)$", stripped) or re.match(r"^!\[([^\]]+)\]\((.+)\)$", stripped)
        if m_img:
            caption = strip_md_inline(m_img.group(1))
            rel_path = m_img.group(2).strip()
            img_file = (DRAFTS / rel_path).resolve()
            if not img_file.exists():
                raise FileNotFoundError(f"Missing image: {img_file}")
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(8)
            p_img.paragraph_format.space_after = Pt(3)
            p_img.paragraph_format.keep_with_next = True
            p_img.add_run().add_picture(str(img_file), width=Cm(15.0))

            p_cap = doc.add_paragraph(style="Caption")
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_before = Pt(0)
            p_cap.paragraph_format.space_after = Pt(8)
            set_run_font(p_cap.add_run(caption), size=10.5, italic=True, color=COLOR_BLACK)
            if caption in tc_for_fig:
                tc_lbl, fbm = tc_for_fig[caption]
                add_bookmark(p_cap, fbm, bm_counter)
                add_tc_field(p_cap, tc_lbl, "F", 3)
            i += 1
            continue

        if stripped.startswith("# "):
            raw_title = stripped[2:].strip()
            clean_title = strip_md_inline(raw_title)
            if first_h1_seen:
                doc.add_page_break()
            first_h1_seen = True
            p = doc.add_paragraph(style="Heading 1")
            p.paragraph_format.space_before = Pt(4)
            p.paragraph_format.space_after = Pt(10)
            p.paragraph_format.keep_with_next = True
            add_formatted_runs(p, raw_title, base_size=14.5, base_color=COLOR_BLACK, base_bold=True)
            if clean_title in bm_by_key:
                add_bookmark(p, bm_by_key[clean_title], bm_counter)
            if clean_title in tc_for_h1:
                add_tc_field(p, tc_for_h1[clean_title], "F", 1)
            i += 1
            continue

        if stripped.startswith("## "):
            raw_title = stripped[3:].strip()
            clean_title = strip_md_inline(raw_title)
            p = doc.add_paragraph(style="Heading 2")
            p.paragraph_format.space_before = Pt(10)
            p.paragraph_format.space_after = Pt(5)
            p.paragraph_format.keep_with_next = True
            add_formatted_runs(p, raw_title, base_size=13.0, base_color=COLOR_BLACK, base_bold=True)
            if clean_title in bm_by_key:
                add_bookmark(p, bm_by_key[clean_title], bm_counter)
            if clean_title in tc_for_h2:
                add_tc_field(p, tc_for_h2[clean_title], "F", 2)
            i += 1
            continue

        if stripped.startswith("### "):
            raw_title = stripped[4:].strip()
            p = doc.add_paragraph(style="Heading 3")
            p.paragraph_format.space_before = Pt(7)
            p.paragraph_format.space_after = Pt(3)
            p.paragraph_format.keep_with_next = True
            add_formatted_runs(p, raw_title, base_size=12.0, base_color=COLOR_BLACK, base_bold=True)
            i += 1
            continue

        m_ol = re.match(r"^(\d+)\.\s+(.*)$", stripped)
        m_ul = re.match(r"^[-*]\s+(.*)$", stripped)
        m_ref = re.match(r"^\[(\d+)\]\s+(.*)$", stripped)

        if m_ref:
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p.paragraph_format.left_indent = Cm(0.85)
            p.paragraph_format.first_line_indent = Cm(-0.85)
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(4)
            p.paragraph_format.line_spacing = 1.2
            set_run_font(p.add_run(f"[{m_ref.group(1)}] "), size=11.0, bold=True, color=COLOR_BLACK)
            add_formatted_runs(p, m_ref.group(2), base_size=11.0, base_color=COLOR_BLACK)
            i += 1
            continue

        if m_ol or m_ul:
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p.paragraph_format.left_indent = Cm(0.85)
            p.paragraph_format.first_line_indent = Cm(-0.45)
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(4.5)
            p.paragraph_format.line_spacing = 1.25
            prefix = f"{m_ol.group(1)}. " if m_ol else "• "
            content = m_ol.group(2) if m_ol else m_ul.group(1)
            set_run_font(p.add_run(prefix), size=12.0, bold=False, color=COLOR_BLACK)
            add_formatted_runs(p, content, base_size=12.0, base_color=COLOR_BLACK)
            i += 1
            continue

        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.first_line_indent = Cm(0.9)
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(6 if not is_intro else 8)
        p.paragraph_format.line_spacing = 1.28 if not is_intro else 1.35
        add_formatted_runs(p, stripped, base_size=12.2 if not is_intro else 12.5, base_color=COLOR_BLACK)
        i += 1


def build_docx(page_map):
    md_text = MD_PATH.read_text(encoding="utf-8")
    intro_lines, body_lines = parse_markdown_sections(md_text)
    toc_entries, fig_tree_entries, bm_by_key, tc_for_h1, tc_for_h2, tc_for_fig = analyze_document_structure(body_lines)

    doc = docx.Document()
    configure_word_styles(doc)
    enable_update_fields_on_open(doc)
    bm_counter = BookmarkCounter()

    # Trang 1: Trang bìa khung đen phủ trọn khổ A4 (Section 1 -> tự sang Section 2)
    build_cover_page(doc)

    # Trang 2: Lời mở đầu
    p_intro_h = doc.add_paragraph()
    p_intro_h.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_intro_h.paragraph_format.space_before = Pt(8)
    p_intro_h.paragraph_format.space_after = Pt(18)
    set_run_font(p_intro_h.add_run("LỜI MỞ ĐẦU"), size=16, bold=True, color=COLOR_BLACK)
    render_lines(doc, intro_lines, bm_counter, is_intro=True)

    # Trang 3: MỤC LỤC TỰ ĐỘNG (Heading 1–2)
    add_dynamic_toc_block(
        doc,
        heading_text="MỤC LỤC",
        instr_code=' TOC \\o "1-2" \\h \\z \\u ',
        entries=toc_entries,
        page_map=page_map,
        is_tree=False,
    )

    # Trang 4: DANH MỤC HÌNH ẢNH TỰ ĐỘNG THEO CẤU TRÚC CÂY 3 TẦNG (TC \f F \l 1-3)
    add_dynamic_toc_block(
        doc,
        heading_text="DANH MỤC HÌNH ẢNH",
        instr_code=' TOC \\f F \\l "1-3" \\h \\z \\u ',
        entries=fig_tree_entries,
        page_map=page_map,
        is_tree=True,
    )
    doc.add_page_break()

    # Trang 5+: Toàn bộ 5 chương + Phụ lục
    render_lines(
        doc,
        body_lines,
        bm_counter,
        bm_by_key=bm_by_key,
        tc_for_h1=tc_for_h1,
        tc_for_h2=tc_for_h2,
        tc_for_fig=tc_for_fig,
        is_intro=False,
    )

    doc.save(str(DOCX_PATH))
    return toc_entries, fig_tree_entries


def export_pdf():
    subprocess.run(
        [
            "libreoffice", "--headless", "--convert-to", "pdf",
            "--outdir", str(DRAFTS), str(DOCX_PATH),
        ],
        check=True,
    )


def detect_exact_pages(toc_entries, fig_tree_entries):
    """Đọc chính xác số trang của mọi Chương, Mục và Hình ảnh sau trang DANH MỤC HÌNH ẢNH."""
    res = subprocess.run(["pdftotext", str(PDF_PATH), "-"], check=True, capture_output=True, text=True)
    pages = res.stdout.split("\x0c")

    # Tìm trang kết thúc front-matter (ngay sau trang DANH MỤC HÌNH ẢNH)
    front_end = 3
    for idx, pg in enumerate(pages[:8]):
        if "DANH MỤC HÌNH ẢNH" in pg and "CHƯƠNG 1:" not in pg:
            front_end = idx
        elif "DANH MỤC HÌNH ẢNH" in pg:
            front_end = idx
    start_search = front_end + 1

    # Tìm chính xác từng trang cho TOC entries (tuần tự tăng dần)
    page_map = {}
    cursor = start_search
    for _, _, key, _ in toc_entries:
        norm_key = re.sub(r"\s+", " ", key).strip()
        short_key = norm_key[:38]
        found = None
        for idx in range(cursor, len(pages)):
            norm_pg = re.sub(r"\s+", " ", pages[idx])
            if short_key in norm_pg:
                found = idx + 1
                cursor = idx
                break
        if found is None:
            m_num = re.match(r"^(CHƯƠNG \d+:|PHỤ LỤC:|A\.\d+\.|[\d]+\.[\d]+\.)", norm_key)
            if m_num:
                tok = m_num.group(1)
                for idx in range(cursor, len(pages)):
                    if tok in pages[idx]:
                        found = idx + 1
                        cursor = idx
                        break
        page_map[key] = found if found is not None else (cursor + 1)

    # Tìm chính xác từng trang cho các Hình ảnh (level 3 trong fig_tree_entries)
    fig_cursor = start_search
    for lvl, _, key, _ in fig_tree_entries:
        if lvl != 3:
            continue
        norm_key = re.sub(r"\s+", " ", key).strip()
        # Khớp theo "Hình X.Y:" + đoạn đầu tên hình (tránh khớp nhầm vào bảng A.1 ở Phụ lục)
        m_fig = re.match(r"^(Hình\s+[A\d]+\.\d+:)", norm_key)
        fig_prefix = m_fig.group(1) if m_fig else norm_key[:24]
        found = None
        for idx in range(fig_cursor, len(pages)):
            norm_pg = re.sub(r"\s+", " ", pages[idx])
            if fig_prefix in norm_pg:
                found = idx + 1
                fig_cursor = idx
                break
        page_map[key] = found if found is not None else (fig_cursor + 1)

    total_pages = len([p for p in pages if p.strip()])
    return page_map, total_pages


def main():
    print("Pass 1: Building DOCX & PDF (TOC + 3-level Hierarchical List of Figures)...")
    toc_entries, fig_tree_entries = build_docx({})
    export_pdf()
    page_map, total_pages = detect_exact_pages(toc_entries, fig_tree_entries)
    print(f"Pass 1 done: {total_pages} pages.")
    print("=== DANH MỤC HÌNH ẢNH (CẤU TRÚC CÂY 3 TẦNG) ===")
    for lvl, disp, key, _ in fig_tree_entries:
        indent = "  " * (lvl - 1)
        print(f"  p.{page_map[key]:2d} | {indent}{disp[:68]}")

    print("Pass 2: Rebuilding DOCX & PDF with 100% exact page numbers & hyperlinks...")
    build_docx(page_map)
    export_pdf()
    page_map2, total_pages2 = detect_exact_pages(toc_entries, fig_tree_entries)
    assert page_map == page_map2, f"Page shift between pass 1 and pass 2: {page_map} vs {page_map2}"
    print(f"SUCCESS! Final PDF verified ({total_pages2} pages), TOC & Hierarchical List of Figures 100% exact.")


if __name__ == "__main__":
    main()
