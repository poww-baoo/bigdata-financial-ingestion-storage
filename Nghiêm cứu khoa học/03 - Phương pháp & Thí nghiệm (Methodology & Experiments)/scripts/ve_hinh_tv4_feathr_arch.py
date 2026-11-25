"""
MÃ NGUỒN TÁI TẠO FIGURE 8 TỪ BÀI BÁO FEATHRPO (PVLDB 2023, TRANG 4235)
Tên hình gốc: Figure 8: FeathrPO new modules and their integration with other Feathr components
Thành viên thực hiện: TV4 - Long
Công cụ: Python 3 + Matplotlib
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as patches

OUT_DIR = Path(__file__).resolve().parents[2] / "99 - Đính kèm (Attachments)"
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_PNG = OUT_DIR / "Hinh_TV4_1_KienTruc_FeathrPO.png"
OUT_PDF = OUT_DIR / "Hinh_TV4_1_KienTruc_FeathrPO.pdf"


def draw_box(ax, x, y, w, h, title, fc, ec, fontsize=9.0, bold=True, tc="#0f172a", ls="-", lw=1.5):
    box = patches.FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.005,rounding_size=0.015",
        facecolor=fc,
        edgecolor=ec,
        linewidth=lw,
        linestyle=ls,
        zorder=3,
    )
    ax.add_patch(box)
    ax.text(
        x + w / 2,
        y + h / 2,
        title,
        ha="center",
        va="center",
        fontsize=fontsize,
        fontweight="bold" if bold else "normal",
        color=tc,
        zorder=4,
    )


def draw_arrow(ax, x1, y1, x2, y2, bidir=False):
    style = "<|-|>,head_width=0.28,head_length=0.45" if bidir else "-|>,head_width=0.28,head_length=0.45"
    ax.annotate(
        "",
        xy=(x2, y2),
        xytext=(x1, y1),
        arrowprops=dict(arrowstyle=style, lw=1.4, color="#334155"),
        zorder=5,
    )


def main():
    fig, ax = plt.subplots(figsize=(13.0, 6.2), dpi=300)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # Title
    ax.text(
        0.5,
        0.945,
        "Hình tái tạo Figure 8: Các module mới của FeathrPO và tích hợp với Feathr trên Azure",
        ha="center",
        va="center",
        fontsize=12.5,
        fontweight="bold",
        color="#0f172a",
    )
    ax.text(
        0.5,
        0.895,
        "Nguồn gốc: Liu et al., PVLDB 2023, Vol. 16, No. 13, p. 4235 (Màu xanh: Module mới của FeathrPO | Màu xám: Thành phần gốc của Feathr)",
        ha="center",
        va="center",
        fontsize=9.2,
        style="italic",
        color="#475569",
    )

    # Top: Feature Registry
    reg_bg = patches.FancyBboxPatch((0.04, 0.67), 0.92, 0.16, boxstyle="round,pad=0.015,rounding_size=0.02", fc="#f1f5f9", ec="#64748b", lw=1.5, zorder=1)
    ax.add_patch(reg_bg)
    ax.text(0.35, 0.75, "Feature Registry (Kho đăng ký đặc trưng mở rộng)", ha="center", va="center", fontsize=11, fontweight="bold", color="#334155")
    draw_box(ax, 0.63, 0.695, 0.14, 0.11, "Microsoft\nPurview", "#e2e8f0", "#64748b", fontsize=9.2)
    draw_box(ax, 0.80, 0.695, 0.13, 0.11, "Azure\nSQL", "#e2e8f0", "#64748b", fontsize=9.2)

    # Middle Left: Python Client + Feathr Client + Data Layout Selector
    draw_box(ax, 0.04, 0.36, 0.14, 0.22, "Python\nClient\n(User SDK)", "#e2e8f0", "#64748b", fontsize=9.5)

    client_bg = patches.FancyBboxPatch((0.23, 0.36), 0.19, 0.22, boxstyle="round,pad=0.008,rounding_size=0.018", fc="#f8fafc", ec="#64748b", lw=1.4, zorder=2)
    ax.add_patch(client_bg)
    draw_box(ax, 0.242, 0.482, 0.166, 0.085, "Data Layout Selector\n(Mới - BIP / KLL)", "#dcfce7", "#16a34a", fontsize=8.6, tc="#14532d", lw=1.8)
    draw_box(ax, 0.242, 0.372, 0.166, 0.085, "Feathr Client", "#e2e8f0", "#64748b", fontsize=9.3)

    # Middle Center: Apache Spark Runtime
    spark_bg = patches.FancyBboxPatch((0.23, 0.08), 0.47, 0.23, boxstyle="round,pad=0.01,rounding_size=0.02", fc="#f1f5f9", ec="#475569", lw=1.6, zorder=1)
    ax.add_patch(spark_bg)
    ax.text(0.465, 0.115, "Apache Spark Runtime", ha="center", va="center", fontsize=10.8, fontweight="bold", color="#1e293b")

    draw_box(ax, 0.245, 0.165, 0.13, 0.12, "Reuse-based\nOptimizer\n(Mới)", "#dcfce7", "#16a34a", fontsize=8.8, tc="#14532d", lw=1.8)
    draw_box(ax, 0.40, 0.165, 0.13, 0.12, "Logical\nOptimizer", "#e2e8f0", "#64748b", fontsize=9.0)
    draw_box(ax, 0.555, 0.165, 0.13, 0.12, "Execution Plan\nGeneration", "#e2e8f0", "#64748b", fontsize=8.8)

    # Right: Offline Stores & Online Stores
    off_bg = patches.FancyBboxPatch((0.73, 0.35), 0.23, 0.23, boxstyle="round,pad=0.008,rounding_size=0.018", fc="#f8fafc", ec="#64748b", lw=1.4, zorder=1)
    ax.add_patch(off_bg)
    ax.text(0.845, 0.38, "Offline Stores", ha="center", va="center", fontsize=10, fontweight="bold", color="#334155")
    draw_box(ax, 0.742, 0.43, 0.095, 0.12, "Azure Blob\nStorage", "#e2e8f0", "#64748b", fontsize=8.2)
    draw_box(ax, 0.853, 0.43, 0.095, 0.12, "Azure Data\nLake Storage", "#e2e8f0", "#64748b", fontsize=8.2)

    on_bg = patches.FancyBboxPatch((0.73, 0.08), 0.23, 0.23, boxstyle="round,pad=0.008,rounding_size=0.018", fc="#f8fafc", ec="#64748b", lw=1.4, zorder=1)
    ax.add_patch(on_bg)
    ax.text(0.845, 0.11, "Online Stores", ha="center", va="center", fontsize=10, fontweight="bold", color="#334155")
    draw_box(ax, 0.742, 0.16, 0.095, 0.12, "Azure Redis\nCache", "#e2e8f0", "#64748b", fontsize=8.2)
    draw_box(ax, 0.853, 0.16, 0.095, 0.12, "Cosmos\nDB", "#e2e8f0", "#64748b", fontsize=8.2)

    # Arrows matching Figure 8
    draw_arrow(ax, 0.185, 0.415, 0.237, 0.415)
    draw_arrow(ax, 0.325, 0.575, 0.325, 0.658, bidir=True)
    draw_arrow(ax, 0.38, 0.225, 0.395, 0.225)
    draw_arrow(ax, 0.535, 0.225, 0.55, 0.225)
    draw_arrow(ax, 0.31, 0.292, 0.31, 0.367, bidir=True)
    draw_arrow(ax, 0.69, 0.25, 0.722, 0.44)
    draw_arrow(ax, 0.69, 0.20, 0.722, 0.20)
    draw_arrow(ax, 0.425, 0.465, 0.722, 0.465, bidir=True)

    # Legend (fit cleanly under Python Client without touching Spark box)
    leg_new = patches.Patch(facecolor="#dcfce7", edgecolor="#16a34a", linewidth=1.6, label="Module mới\n(FeathrPO)")
    leg_old = patches.Patch(facecolor="#e2e8f0", edgecolor="#64748b", linewidth=1.4, label="Thành phần gốc\n(Feathr)")
    ax.legend(handles=[leg_new, leg_old], loc="lower left", bbox_to_anchor=(0.03, 0.08), fontsize=8.8, frameon=True)

    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=300, bbox_inches="tight")
    plt.savefig(OUT_PDF, bbox_inches="tight")
    print(f"Đã lưu hình tại: {OUT_PNG} và {OUT_PDF}")


if __name__ == "__main__":
    main()
