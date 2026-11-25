"""
MÃ NGUỒN TÁI TẠO FIGURE 1 TỪ BÀI BÁO BTRBLOCKS (ACM SIGMOD 2023)
Tên hình: Hiệu năng thông lượng quét S3 và chi phí quét (S3 scan cost and throughput)
Dữ liệu đối soát từ Figure 1 (Trang 118:2) & Table 5 (Trang 118:20) của bài báo gốc
Sinh viên thực hiện: Nguyễn Đình Cường - MSSV: 3123411043
Học phần: Phương pháp Nghiên cứu Khoa học trong CNTT
Công cụ: Python 3 + Matplotlib
"""

import os
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["DejaVu Sans", "Liberation Sans", "Arial"]
plt.rcParams["axes.unicode_minus"] = False


def main():
    # Dữ liệu chính xác từ Table 5 (Trang 118:20) & Mục 6.7 (Trang 118:21) của bài báo gốc
    # S3 Scans per Dollar = 10 / Scan_cost($) (tương ứng thang đo chuẩn hóa trên Figure 1)
    formats = [
        {
            "name": "BtrBlocks",
            "tc_gbps": 86.2,
            "scan_cost": 0.97,
            "scans_per_dollar": 10.0 / 0.97,
            "tu_gbs": 174.6,
            "color": "#5f8d41",
            "marker": "o",
            "label_xy": (82.5, 10.85),
            "ha": "right",
            "va": "center",
        },
        {
            "name": "Parquet + Zstd",
            "tc_gbps": 24.8,
            "scan_cost": 1.70,
            "scans_per_dollar": 10.0 / 1.70,
            "tu_gbs": 78.6,
            "color": "#3d8b86",
            "marker": "D",
            "label_xy": (4.0, 7.25),
            "ha": "left",
            "va": "center",
        },
        {
            "name": "Parquet + Snappy",
            "tc_gbps": 33.2,
            "scan_cost": 1.74,
            "scans_per_dollar": 10.0 / 1.74,
            "tu_gbs": 77.6,
            "color": "#1d4ed8",
            "marker": "^",
            "label_xy": (24.0, 4.30),
            "ha": "center",
            "va": "center",
        },
        {
            "name": "Parquet (không nén thêm)",
            "tc_gbps": 52.6,
            "scan_cost": 2.47,
            "scans_per_dollar": 10.0 / 2.47,
            "tu_gbs": 56.1,
            "color": "#8b5a83",
            "marker": "s",
            "label_xy": (55.0, 2.55),
            "ha": "center",
            "va": "center",
        },
    ]

    fig, ax = plt.subplots(figsize=(10.5, 6.2), dpi=300)

    # Đường giới hạn băng thông mạng S3 trên máy c5n.18xlarge (~91 Gbps khi tải dữ liệu thô, Mục 6.7)
    s3_limit = 91.0
    ax.axvline(s3_limit, color="#94a3b8", linestyle="-", linewidth=1.8, zorder=2)
    ax.axvspan(s3_limit, 106, color="#f1f5f9", alpha=0.85, zorder=1)
    ax.text(
        s3_limit + 2.5,
        3.1,
        "Giới hạn băng thông S3\ntrên c5n.18xlarge (~91 Gbps)",
        rotation=90,
        va="center",
        ha="left",
        fontsize=9.3,
        color="#475569",
        fontweight="bold",
        zorder=3,
    )

    for item in formats:
        x, y = item["tc_gbps"], item["scans_per_dollar"]
        ax.scatter(
            x,
            y,
            color=item["color"],
            marker=item["marker"],
            s=115,
            edgecolors="#1e293b",
            linewidths=0.9,
            zorder=5,
        )
        lx, ly = item["label_xy"]
        label = (
            f"{item['name']}\n"
            f"Tc={x:.1f} Gbps | {y:.2f} lượt/$ | Tu={item['tu_gbs']:.1f} GB/s"
        )
        ax.annotate(
            label,
            xy=(x, y),
            xytext=(lx, ly),
            ha=item["ha"],
            va=item["va"],
            fontsize=8.8,
            fontweight="bold",
            color=item["color"],
            arrowprops=dict(arrowstyle="-", color=item["color"], lw=1.0, alpha=0.7),
            bbox=dict(boxstyle="round,pad=0.30", facecolor="white", edgecolor="#cbd5e1", alpha=0.96),
            zorder=6,
        )

    # Hộp chú thích nhấn mạnh vùng tối ưu
    ax.annotate(
        "Vùng tối ưu (Nhanh & Rẻ nhất):\n"
        "BtrBlocks đạt Tc = 86.2 Gbps (gần chạm ngưỡng 91 Gbps),\n"
        "nhanh hơn 2.6×–3.5× so với Parquet+Snappy/Zstd ở thông lượng nén\n"
        "và tiết kiệm chi phí hơn 1.8×–2.6× mỗi lượt quét S3.",
        xy=(85.5, 10.05),
        xytext=(41.0, 7.7),
        arrowprops=dict(arrowstyle="->", color="#4d7c0f", lw=1.6, connectionstyle="arc3,rad=0.18"),
        fontsize=8.9,
        fontweight="bold",
        color="#365314",
        bbox=dict(boxstyle="round,pad=0.45", facecolor="#f7fee7", edgecolor="#84cc16", lw=1.2),
        zorder=7,
    )

    ax.set_xlim(0, 106)
    ax.set_ylim(0, 11.8)
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.set_yticks([0, 2, 4, 6, 8, 10])
    ax.grid(True, linestyle="--", alpha=0.5, zorder=0)

    ax.set_xlabel(
        "Thông lượng quét S3 trên dữ liệu nén Tc [Gbit/s]\n[S3 Scan Throughput (Gbps) — Càng cao càng khai thác tốt mạng 100 Gbps]",
        fontsize=10.3,
        fontweight="bold",
        labelpad=10,
    )
    ax.set_ylabel(
        "Số lượt quét S3 trên mỗi Đô-la [S3 Scans per Dollar]\n(Càng cao càng tiết kiệm chi phí điện toán + GET S3)",
        fontsize=10.3,
        fontweight="bold",
        labelpad=10,
    )
    ax.set_title(
        "Hình tái tạo Figure 1: Thông lượng quét S3 và Chi phí trên 5 tập dữ liệu Public BI lớn nhất\n"
        "(Thử nghiệm trên AWS EC2 c5n.18xlarge — Nguồn: Kuschewski et al., ACM SIGMOD 2023)",
        fontsize=11.3,
        fontweight="bold",
        pad=14,
        color="#0f172a",
    )

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_linewidth(1.1)
    ax.spines["bottom"].set_linewidth(1.1)

    plt.tight_layout()

    base_dir = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.path.abspath(os.path.join(base_dir, "../../99 - Đính kèm (Attachments)"))
    os.makedirs(out_dir, exist_ok=True)
    png_path = os.path.join(out_dir, "BtrBlocks_Hinh2_TaiTao_S3ScanBenchmark.png")
    pdf_path = os.path.join(out_dir, "BtrBlocks_Hinh2_TaiTao_S3ScanBenchmark.pdf")
    plt.savefig(png_path, dpi=300, bbox_inches="tight")
    plt.savefig(pdf_path, bbox_inches="tight")
    print("Saved:", png_path)
    print("Saved:", pdf_path)


if __name__ == "__main__":
    main()
