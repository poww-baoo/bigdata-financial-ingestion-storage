"""
MÃ NGUỒN TÁI TẠO FIGURE 12 TỪ BÀI BÁO FEATHRPO (PVLDB 2023, TRANG 4237)
Tên hình gốc: Figure 12: Factor of improvement with FeathrPO on Spark for different
datasets and PIT join implementations.
Thành viên thực hiện: TV4 - Long
Ghi chú phương pháp dữ liệu: Mốc trần 3.0x (Feathr) và 2.5x (các thuật toán PIT join khác)
được công bố trực tiếp trong văn bản mục 8.2 (trang 4237); giá trị từng cột còn lại được
trích xuất trực quan từ thang chia trục tung của Figure 12 gốc.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

OUT_DIR = Path(__file__).resolve().parents[2] / "99 - Đính kèm (Attachments)"
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_PNG = OUT_DIR / "Hinh_TV4_2_HieuNang_FeathrPO.png"
OUT_PDF = OUT_DIR / "Hinh_TV4_2_HieuNang_FeathrPO.pdf"


def main():
    implementations = [
        "Feathr (ZipPartition)\n[Cloud Setup]",
        "Early-stop Sort Merge\n[Local Setup]",
        "Union Merge\n[Local Setup]",
    ]

    # Hệ số cải thiện (Factor of Improvement) đọc từ Figure 12, trang 4237:
    uc7 = [1.80, 1.32, 1.58]        # TPCx-AI UC7 (SF10)
    uc10 = [3.00, 2.02, 2.50]       # TPCx-AI UC10 (SF10) - đạt 3.0x và 2.5x theo bài báo
    favorita = [1.56, 1.40, 1.90]   # Kaggle-Favorita
    ecommerce = [1.96, 1.54, 1.98]  # Kaggle-eCommerce

    x = np.arange(len(implementations))
    width = 0.19

    fig, ax = plt.subplots(figsize=(11.5, 6.0), dpi=300)

    b1 = ax.bar(x - 1.5 * width, uc7, width, label="TPCx-AI UC7 (SF10)", color="#f97316", edgecolor="#1e293b", hatch="///", zorder=3)
    b2 = ax.bar(x - 0.5 * width, uc10, width, label="TPCx-AI UC10 (SF10)", color="#15803d", edgecolor="#1e293b", zorder=3)
    b3 = ax.bar(x + 0.5 * width, favorita, width, label="Kaggle-Favorita", color="#38bdf8", edgecolor="#1e293b", hatch="...", zorder=3)
    b4 = ax.bar(x + 1.5 * width, ecommerce, width, label="Kaggle-eCommerce", color="#dc2626", edgecolor="#1e293b", hatch="---", zorder=3)

    for bars in (b1, b2, b3, b4):
        for bar in bars:
            h = bar.get_height()
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                h + 0.06,
                f"{h:.2f}×",
                ha="center",
                va="bottom",
                fontsize=7.6,
                fontweight="bold",
                color="#0f172a",
            )

    ax.axhline(1.0, color="#475569", linestyle="--", linewidth=1.2, label="Mốc chuẩn Baseline (1.0×)", zorder=2)
    ax.set_xticks(x)
    ax.set_xticklabels(implementations, fontsize=10.5, fontweight="bold")
    ax.set_ylabel("Hệ số cải thiện (Factor of Improvement)", fontsize=11, fontweight="bold")
    ax.set_xlabel("Cài đặt thuật toán Point-in-Time Join", fontsize=11, fontweight="bold", labelpad=8)
    ax.set_ylim(0, 3.85)
    ax.set_yticks([0, 1, 2, 3, 4])
    ax.grid(axis="y", linestyle="--", alpha=0.55, zorder=0)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.set_title(
        "Hình tái tạo Figure 12: Hệ số cải thiện hiệu năng với FeathrPO trên Spark\n"
        "qua các tập dữ liệu và thuật toán Point-in-Time Join khác nhau (Liu et al., PVLDB 2023, tr. 4237)",
        fontsize=11.5,
        fontweight="bold",
        pad=14,
        color="#0f172a",
    )
    ax.legend(loc="upper right", ncol=2, fontsize=9.2, frameon=True)

    ax.annotate(
        "Đạt mức tăng tốc tối đa 3.0×\ntrên Feathr Cloud (UC10)",
        xy=(0 - 0.5 * width, 3.0),
        xytext=(0.35, 3.35),
        arrowprops=dict(arrowstyle="->", lw=1.4, color="#15803d"),
        fontsize=9.2,
        fontweight="bold",
        color="#14532d",
        bbox=dict(boxstyle="round,pad=0.35", fc="#dcfce7", ec="#16a34a"),
    )

    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=300, bbox_inches="tight")
    plt.savefig(OUT_PDF, bbox_inches="tight")
    print(f"Đã lưu hình tại: {OUT_PNG} và {OUT_PDF}")


if __name__ == "__main__":
    main()
