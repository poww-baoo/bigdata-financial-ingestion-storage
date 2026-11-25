"""
MÃ NGUỒN TÁI TẠO FIGURE 3 TỪ BÀI BÁO BTRBLOCKS (ACM SIGMOD 2023)
Tên hình: Cây quyết định các lược đồ mã hóa áp dụng đệ quy (Encoding scheme decision trees)
Sinh viên thực hiện: Nguyễn Đình Cường - MSSV: 3123411043
Học phần: Phương pháp Nghiên cứu Khoa học trong CNTT
Công cụ: Python 3 + Matplotlib
"""

import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Cấu hình font hỗ trợ tiếng Việt
plt.rcParams["font.sans-serif"] = ["DejaVu Sans", "Liberation Sans", "Arial"]
plt.rcParams["axes.unicode_minus"] = False

COLOR_TYPE = "#93b476"       # Xanh lá: Kiểu dữ liệu / Điểm đệ quy (Data Type / Recursion point)
COLOR_TYPE_EDGE = "#587242"
COLOR_SCHEME = "#6da4b8"     # Xanh dương: Lược đồ mã hóa (Encoding scheme)
COLOR_SCHEME_EDGE = "#3b697a"
COLOR_LEAF = "#d9dee3"       # Xám nhạt: Lá kết thúc không đệ quy tiếp (Terminal component)
COLOR_LEAF_EDGE = "#6c757d"


def draw_box(ax, cx, cy, w, h, text, kind="scheme", fontsize=8.8):
    if kind == "type":
        fc, ec, tc, fw = COLOR_TYPE, COLOR_TYPE_EDGE, "#111111", "bold"
    elif kind == "leaf":
        fc, ec, tc, fw = COLOR_LEAF, COLOR_LEAF_EDGE, "#222222", "normal"
    else:
        fc, ec, tc, fw = COLOR_SCHEME, COLOR_SCHEME_EDGE, "#0f172a", "bold"

    box = patches.FancyBboxPatch(
        (cx - w / 2, cy - h / 2),
        w,
        h,
        boxstyle="round,pad=0.04,rounding_size=0.06",
        facecolor=fc,
        edgecolor=ec,
        linewidth=1.25,
        zorder=3,
    )
    ax.add_patch(box)
    ax.text(cx, cy, text, ha="center", va="center", fontsize=fontsize, fontweight=fw, color=tc, zorder=4)


def draw_arrow(ax, x1, y1, x2, y2, label=None, label_offset=(0, 0), fontsize=7.6):
    ax.annotate(
        "",
        xy=(x2, y2),
        xytext=(x1, y1),
        arrowprops=dict(arrowstyle="-|>,head_width=0.22,head_length=0.35", color="#334155", lw=1.2),
        zorder=2,
    )
    if label:
        mx = (x1 + x2) / 2 + label_offset[0]
        my = (y1 + y2) / 2 + label_offset[1]
        ax.text(
            mx,
            my,
            label,
            ha="center",
            va="center",
            fontsize=fontsize,
            style="italic",
            color="#1e293b",
            bbox=dict(boxstyle="round,pad=0.12", facecolor="white", edgecolor="none", alpha=0.88),
            zorder=5,
        )


def draw_ortho_branch(ax, parent_x, parent_bottom_y, bar_y, child_xs, child_top_ys):
    ax.plot([parent_x, parent_x], [parent_bottom_y, bar_y], color="#334155", lw=1.2, zorder=2)
    ax.plot([min(child_xs), max(child_xs)], [bar_y, bar_y], color="#334155", lw=1.2, zorder=2)
    for cx, cty in zip(child_xs, child_top_ys):
        draw_arrow(ax, cx, bar_y, cx, cty)


def main():
    fig, ax = plt.subplots(figsize=(14.5, 9.2), dpi=300)
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 12.6)
    ax.axis("off")

    # Tiêu đề tổng thể
    ax.text(
        10.0,
        12.2,
        "Hình tái tạo Figure 3: Cây quyết định lược đồ mã hóa đệ quy trong BtrBlocks",
        ha="center",
        va="center",
        fontsize=13.5,
        fontweight="bold",
        color="#0f172a",
    )
    ax.text(
        10.0,
        11.78,
        "[Encoding scheme decision trees applied recursively — Nguồn: Kuschewski et al., ACM SIGMOD 2023, Trang 118:7]",
        ha="center",
        va="center",
        fontsize=9.5,
        color="#475569",
    )

    # ==========================================================
    # 1. CÂY DOUBLE (Phần trên)
    # ==========================================================
    d_root_x, d_root_y = 10.0, 10.95
    draw_box(ax, d_root_x, d_root_y, 1.9, 0.52, "Double", kind="type", fontsize=9.8)

    d_children_x = [5.1, 7.05, 8.75, 10.45, 12.25, 14.35]
    d_scheme_y = 9.75
    d_scheme_h = 0.56
    draw_ortho_branch(ax, d_root_x, d_root_y - 0.30, 10.42, d_children_x, [d_scheme_y + 0.32] * 6)

    draw_box(ax, d_children_x[0], d_scheme_y, 1.65, d_scheme_h, "Frequency", kind="scheme")
    draw_box(ax, d_children_x[1], d_scheme_y, 1.25, d_scheme_h, "One\nValue", kind="scheme")
    draw_box(ax, d_children_x[2], d_scheme_y, 1.15, d_scheme_h, "RLE", kind="scheme")
    draw_box(ax, d_children_x[3], d_scheme_y, 1.15, d_scheme_h, "Dict", kind="scheme")
    draw_box(ax, d_children_x[4], d_scheme_y, 1.65, d_scheme_h, "Uncom-\npressed", kind="scheme")
    draw_box(ax, d_children_x[5], d_scheme_y, 1.75, d_scheme_h, "Pseudo-\ndecimal", kind="scheme")

    # Tầng lá / đệ quy của Double
    d_leaf_y = 8.15
    d_leaf_h = 0.52

    # Frequency -> Roaring Bitmap, Double
    draw_box(ax, 4.4, d_leaf_y, 1.25, d_leaf_h, "Roaring\nBitmap", kind="leaf", fontsize=8.1)
    draw_box(ax, 5.8, d_leaf_y, 1.15, d_leaf_h, "Double", kind="type", fontsize=8.5)
    draw_arrow(ax, d_children_x[0] - 0.45, d_scheme_y - 0.32, 4.4, d_leaf_y + 0.30, "bitmap", (-0.15, 0.05))
    draw_arrow(ax, d_children_x[0] + 0.45, d_scheme_y - 0.32, 5.8, d_leaf_y + 0.30, "exceptions", (0.20, 0.05))

    # RLE -> Integer, Double
    draw_box(ax, 7.65, d_leaf_y, 1.15, d_leaf_h, "Integer", kind="type", fontsize=8.5)
    draw_box(ax, 9.0, d_leaf_y, 1.15, d_leaf_h, "Double", kind="type", fontsize=8.5)
    draw_arrow(ax, d_children_x[2] - 0.35, d_scheme_y - 0.32, 7.65, d_leaf_y + 0.30, "length", (-0.25, 0.05))
    draw_arrow(ax, d_children_x[2] + 0.25, d_scheme_y - 0.32, 9.0, d_leaf_y + 0.30, "value", (0.15, 0.05))

    # Dict -> Integer
    draw_box(ax, 10.45, d_leaf_y, 1.15, d_leaf_h, "Integer", kind="type", fontsize=8.5)
    draw_arrow(ax, d_children_x[3], d_scheme_y - 0.32, 10.45, d_leaf_y + 0.30, "codes", (0.0, 0.0))

    # Pseudodecimal -> Double, Integer
    draw_box(ax, 13.55, d_leaf_y, 1.15, d_leaf_h, "Double", kind="type", fontsize=8.5)
    draw_box(ax, 15.05, d_leaf_y, 1.15, d_leaf_h, "Integer", kind="type", fontsize=8.5)
    draw_arrow(ax, d_children_x[5] - 0.40, d_scheme_y - 0.32, 13.55, d_leaf_y + 0.30, "exceptions", (-0.28, 0.05))
    draw_arrow(ax, d_children_x[5] + 0.40, d_scheme_y - 0.32, 15.05, d_leaf_y + 0.30, "values", (0.20, 0.05))

    # Khung bao nhẹ phân nhóm Double
    rect_double = patches.FancyBboxPatch(
        (3.4, 7.55), 12.6, 3.85,
        boxstyle="round,pad=0.05,rounding_size=0.15",
        facecolor="#f8fafc", edgecolor="#cbd5e1", linestyle="--", linewidth=1.0, zorder=0
    )
    ax.add_patch(rect_double)
    ax.text(3.65, 11.15, "Nhóm kiểu Số thực (Double)", fontsize=8.8, fontweight="bold", color="#475569", ha="left")

    # ==========================================================
    # 2. CÂY STRING (Phần dưới - Bên trái)
    # ==========================================================
    s_root_x, s_root_y = 5.05, 6.45
    draw_box(ax, s_root_x, s_root_y, 1.9, 0.52, "String", kind="type", fontsize=9.8)

    s_children_x = [1.5, 3.25, 4.95, 6.65, 8.5]
    s_scheme_y = 5.15
    s_scheme_h = 0.56
    draw_ortho_branch(ax, s_root_x, s_root_y - 0.30, 5.88, s_children_x, [s_scheme_y + 0.32] * 5)

    draw_box(ax, s_children_x[0], s_scheme_y, 1.15, s_scheme_h, "FSST", kind="scheme")
    draw_box(ax, s_children_x[1], s_scheme_y, 1.35, s_scheme_h, "Dict +\nFSST", kind="scheme")
    draw_box(ax, s_children_x[2], s_scheme_y, 1.25, s_scheme_h, "One\nValue", kind="scheme")
    draw_box(ax, s_children_x[3], s_scheme_y, 1.15, s_scheme_h, "Dict", kind="scheme")
    draw_box(ax, s_children_x[4], s_scheme_y, 1.65, s_scheme_h, "Uncom-\npressed", kind="scheme")

    # Tầng lá / đệ quy của String
    s_leaf_y = 3.45
    s_leaf_h = 0.52

    # Dict + FSST -> Integer, FSST
    draw_box(ax, 2.35, s_leaf_y, 1.15, s_leaf_h, "Integer", kind="type", fontsize=8.5)
    draw_box(ax, 3.80, s_leaf_y, 1.05, s_leaf_h, "FSST", kind="leaf", fontsize=8.3)
    draw_arrow(ax, s_children_x[1] - 0.35, s_scheme_y - 0.32, 2.35, s_leaf_y + 0.30, "codes", (-0.22, 0.05))
    draw_arrow(ax, s_children_x[1] + 0.35, s_scheme_y - 0.32, 3.80, s_leaf_y + 0.30, "string pool", (0.28, 0.05))

    # Dict -> Integer, Integer, Uncompressed
    draw_box(ax, 5.35, s_leaf_y, 1.15, s_leaf_h, "Integer", kind="type", fontsize=8.5)
    draw_box(ax, 6.75, s_leaf_y, 1.15, s_leaf_h, "Integer", kind="type", fontsize=8.5)
    draw_box(ax, 8.35, s_leaf_y, 1.45, s_leaf_h, "Uncom-\npressed", kind="leaf", fontsize=8.0)
    draw_arrow(ax, s_children_x[3] - 0.40, s_scheme_y - 0.32, 5.35, s_leaf_y + 0.30, "codes", (-0.28, 0.05))
    draw_arrow(ax, s_children_x[3], s_scheme_y - 0.32, 6.75, s_leaf_y + 0.30, "lengths", (0.0, 0.0))
    draw_arrow(ax, s_children_x[3] + 0.40, s_scheme_y - 0.32, 8.35, s_leaf_y + 0.30, "strings", (0.30, 0.05))

    rect_string = patches.FancyBboxPatch(
        (0.55, 2.75), 9.15, 4.25,
        boxstyle="round,pad=0.05,rounding_size=0.15",
        facecolor="#f8fafc", edgecolor="#cbd5e1", linestyle="--", linewidth=1.0, zorder=0
    )
    ax.add_patch(rect_string)
    ax.text(0.80, 6.72, "Nhóm kiểu Chuỗi (String)", fontsize=8.8, fontweight="bold", color="#475569", ha="left")

    # ==========================================================
    # 3. CÂY INTEGER (Phần dưới - Bên phải)
    # ==========================================================
    i_root_x, i_root_y = 14.8, 6.45
    draw_box(ax, i_root_x, i_root_y, 1.9, 0.52, "Integer", kind="type", fontsize=9.8)

    # 6 nhánh của Integer (SIMD-FastBP128 nối thẳng từ thanh ngang xuống tầng giữa để tránh đè chữ)
    i_children_x = [11.0, 12.6, 14.2, 15.65, 17.0, 18.55]
    i_scheme_y = 5.15
    i_scheme_h = 0.56
    i_child_top_ys = [
        i_scheme_y + 0.32,
        i_scheme_y + 0.32,
        i_scheme_y + 0.32,
        4.15 + 0.32,       # SIMD-FastBP128 đặt thấp hơn tránh chồng lấn ngang
        i_scheme_y + 0.32,
        i_scheme_y + 0.32,
    ]
    draw_ortho_branch(ax, i_root_x, i_root_y - 0.30, 5.88, i_children_x, i_child_top_ys)

    draw_box(ax, i_children_x[0], i_scheme_y, 1.55, i_scheme_h, "Uncom-\npressed", kind="scheme")
    draw_box(ax, i_children_x[1], i_scheme_y, 1.15, i_scheme_h, "RLE", kind="scheme")
    draw_box(ax, i_children_x[2], i_scheme_y, 1.55, i_scheme_h, "SIMD-\nFastPFOR", kind="scheme")
    draw_box(ax, i_children_x[3], 4.15, 1.75, i_scheme_h, "SIMD-\nFastBP128", kind="scheme")
    draw_box(ax, i_children_x[4], i_scheme_y, 1.15, i_scheme_h, "One\nValue", kind="scheme")
    draw_box(ax, i_children_x[5], i_scheme_y, 1.15, i_scheme_h, "Dict", kind="scheme")

    # Tầng lá / đệ quy của Integer
    i_leaf_y = 3.45
    i_leaf_h = 0.52

    # RLE -> Integer, Integer
    draw_box(ax, 11.75, i_leaf_y, 1.15, i_leaf_h, "Integer", kind="type", fontsize=8.5)
    draw_box(ax, 13.25, i_leaf_y, 1.15, i_leaf_h, "Integer", kind="type", fontsize=8.5)
    draw_arrow(ax, i_children_x[1] - 0.30, i_scheme_y - 0.32, 11.75, i_leaf_y + 0.30, "values", (-0.25, 0.05))
    draw_arrow(ax, i_children_x[1] + 0.30, i_scheme_y - 0.32, 13.25, i_leaf_y + 0.30, "lengths", (0.25, 0.05))

    # Dict -> Integer
    draw_box(ax, 18.55, i_leaf_y, 1.15, i_leaf_h, "Integer", kind="type", fontsize=8.5)
    draw_arrow(ax, i_children_x[5], i_scheme_y - 0.32, 18.55, i_leaf_y + 0.30, "codes", (0.0, 0.0))

    rect_int = patches.FancyBboxPatch(
        (10.0, 2.75), 9.45, 4.25,
        boxstyle="round,pad=0.05,rounding_size=0.15",
        facecolor="#f8fafc", edgecolor="#cbd5e1", linestyle="--", linewidth=1.0, zorder=0
    )
    ax.add_patch(rect_int)
    ax.text(10.25, 6.72, "Nhóm kiểu Số nguyên (Integer)", fontsize=8.8, fontweight="bold", color="#475569", ha="left")

    # ==========================================================
    # 4. CHÚ THÍCH (LEGEND) DƯỚI ĐÁY
    # ==========================================================
    legend_y = 1.65
    ax.add_patch(
        patches.FancyBboxPatch(
            (2.2, 0.95), 15.6, 1.25,
            boxstyle="round,pad=0.05,rounding_size=0.12",
            facecolor="#ffffff", edgecolor="#94a3b8", linewidth=1.0, zorder=1
        )
    )
    draw_box(ax, 3.6, legend_y, 1.5, 0.45, "Kiểu dữ liệu", kind="type", fontsize=8.3)
    ax.text(4.55, legend_y, "Kiểu dữ liệu đầu vào / Điểm gọi đệ quy\n(tối đa độ sâu mặc định = 3 tầng)", va="center", ha="left", fontsize=8.4, color="#1e293b")

    draw_box(ax, 9.2, legend_y, 1.5, 0.45, "Lược đồ nén", kind="scheme", fontsize=8.3)
    ax.text(10.15, legend_y, "Lược đồ mã hóa ứng viên\n(chọn qua lấy mẫu 10×64 phần tử)", va="center", ha="left", fontsize=8.4, color="#1e293b")

    draw_box(ax, 14.5, legend_y, 1.4, 0.45, "Lá kết thúc", kind="leaf", fontsize=8.3)
    ax.text(15.40, legend_y, "Đầu ra đặc thù không\nđệ quy tiếp", va="center", ha="left", fontsize=8.4, color="#1e293b")

    plt.tight_layout()

    base_dir = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.path.abspath(os.path.join(base_dir, "../../99 - Đính kèm (Attachments)"))
    os.makedirs(out_dir, exist_ok=True)
    png_path = os.path.join(out_dir, "BtrBlocks_Hinh1_TaiTao_CayQuyetDinhNen.png")
    pdf_path = os.path.join(out_dir, "BtrBlocks_Hinh1_TaiTao_CayQuyetDinhNen.pdf")
    plt.savefig(png_path, dpi=300, bbox_inches="tight")
    plt.savefig(pdf_path, bbox_inches="tight")
    print("Saved:", png_path)
    print("Saved:", pdf_path)


if __name__ == "__main__":
    main()
