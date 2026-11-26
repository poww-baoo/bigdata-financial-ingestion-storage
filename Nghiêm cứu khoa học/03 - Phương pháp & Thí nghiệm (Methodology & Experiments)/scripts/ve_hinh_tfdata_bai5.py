#!/usr/bin/env python3
"""
Tái tạo 02 hình minh họa chuẩn học thuật (300 DPI PNG + Vector PDF) cho Bài báo số 5:
"tf.data: A Machine Learning Data Processing Framework" (Murray et al., PVLDB 2021).

Sinh viên thực hiện: Võ Huỳnh Minh Sang (TV1) - MSSV: 3123411256 - Lớp: DCT123C4
- Hình 1: Tái tạo Figure 5 (tr. 2951) — Mô hình ước lượng độ trễ đầu ra của AUTOTUNE
- Hình 2: Tái tạo Figure 8 (tr. 2953) — Hệ số tăng tốc thời gian hội tụ huấn luyện MLPerf
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Cấu hình font hỗ trợ đầy đủ tiếng Việt
plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["axes.unicode_minus"] = False

OUT_DIR = Path(__file__).resolve().parents[2] / "99 - Đính kèm (Attachments)"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def draw_hinh1_autotune_model():
    """Tái tạo Figure 5: Mô hình ước lượng độ trễ đầu ra của AUTOTUNE trên cây Iterator."""
    fig, ax = plt.subplots(figsize=(12.2, 8.6), dpi=300)
    ax.set_xlim(0, 12.2)
    ax.set_ylim(0, 9.2)
    ax.axis("off")

    # Tiêu đề chính
    ax.text(
        6.1, 8.85,
        "Mô hình ước lượng độ trễ đầu ra (Output Latency Estimation) của cơ chế AUTOTUNE",
        ha="center", va="center", fontsize=13.5, fontweight="bold", color="#0F172A"
    )
    ax.text(
        6.1, 8.48,
        "Tái tạo từ Figure 5 — Murray et al., tf.data (PVLDB 2021, tr. 2951) | Duyệt hai chiều kết hợp hàng đợi M/M/1/k",
        ha="center", va="center", fontsize=9.8, style="italic", color="#475569"
    )

    # Tiêu đề 3 cột
    col_headers = [
        (2.0, "Tốc độ tiêu thụ (y)\n[get_next calls / giây]", "#1D4ED8"),
        (6.1, "Cây toán tử đường ống\n(tf.data Pipeline)", "#0F172A"),
        (10.15, "Độ trễ đầu ra\n[Output Latency, ms]", "#B91C1C"),
    ]
    for cx, title, color in col_headers:
        ax.text(cx, 7.88, title, ha="center", va="center", fontsize=10.5, fontweight="bold", color=color)

    # 6 tầng nút từ trên xuống dưới
    nodes = [
        {
            "y": 6.85, "h": 0.68,
            "name": "data consumer", "sub": "(Vòng lặp huấn luyện — yêu cầu mỗi 10 ms)",
            "bg": "#E2E8F0", "edge": "#334155",
            "left": r"$y = \frac{1}{0.01} = 100$",
            "right": "Đầu ra cuối gửi tới GPU/TPU",
            "right_bold": False,
        },
        {
            "y": 5.65, "h": 0.78,
            "name": "prefetch  (bất đồng bộ)", "sub": "buffer size n = 2",
            "bg": "#DBEAFE", "edge": "#1D4ED8",
            "left": r"$y = 100$",
            "right": r"$x = \frac{1000}{36.5} = 27.4,\ y = 100,\ n = 2$" + "\n" + r"$\mathbf{36.5 \times p_{empty} = 27.0\ ms}$",
            "right_bold": True,
        },
        {
            "y": 4.45, "h": 0.74,
            "name": "batch  (đồng bộ)", "sub": "batch size = 10, self time = 1 ms",
            "bg": "#FEF3C7", "edge": "#B45309",
            "left": r"$100 \times \mathrm{batch\_size} = 1000$",
            "right": r"Hàm tuyến tính:" + "\n" + r"$\mathbf{10 \times 3.55 + 1 = 36.5\ ms}$",
            "right_bold": True,
        },
        {
            "y": 3.18, "h": 0.88,
            "name": "map  (bất đồng bộ)", "sub": "parallelism p = 5, buffer size n = 5",
            "bg": "#DBEAFE", "edge": "#1D4ED8",
            "left": r"$y = 1000$",
            "right": r"$\mathrm{producer\ time} = 4.15 + \frac{2}{5} = 4.55\ ms$" + "\n" + r"$x = \frac{1000}{4.55} = 220,\ y = 1000,\ n = 5$" + "\n" + r"$\mathbf{4.55 \times p_{empty} = 3.55\ ms}$",
            "right_bold": True,
        },
        {
            "y": 1.88, "h": 0.84,
            "name": "interleave  (bất đồng bộ)", "sub": "parallelism p = 1, buffer n = 1, cycle = 2",
            "bg": "#DBEAFE", "edge": "#1D4ED8",
            "left": r"$\frac{1000}{\mathrm{cycle\_length}} = 500$",
            "right": r"$x = \frac{1000}{5} = 200,\ y = 1000,\ n = 1$" + "\n" + r"$\mathbf{5 \times p_{empty} = 4.15\ ms}$",
            "right_bold": True,
        },
        {
            "y": 0.78, "h": 0.62,
            "name": "from_file  (nguồn dữ liệu)", "sub": "Thời gian đọc tệp gốc = 5 ms / phần tử",
            "bg": "#DCFCE7", "edge": "#15803D",
            "left": "(Nguồn đọc đĩa / Object Store)",
            "right": r"$\mathbf{5.0\ ms}$",
            "right_bold": True,
        },
    ]

    box_w = 3.7
    box_x = 6.1 - box_w / 2

    for nd in nodes:
        cy = nd["y"]
        bh = nd["h"]
        rect = patches.FancyBboxPatch(
            (box_x, cy - bh / 2), box_w, bh,
            boxstyle="round,pad=0.04,rounding_size=0.10",
            facecolor=nd["bg"], edgecolor=nd["edge"], linewidth=1.6
        )
        ax.add_patch(rect)
        ax.text(6.1, cy + 0.12, nd["name"], ha="center", va="center", fontsize=10.2, fontweight="bold", color="#0F172A")
        ax.text(6.1, cy - 0.14, nd["sub"], ha="center", va="center", fontsize=8.6, color="#334155")

        # Cột trái (consumer rate)
        ax.text(
            2.15, cy, nd["left"], ha="center", va="center",
            fontsize=9.3, color="#1E3A8A" if nd["y"] > 1.0 else "#475569",
            bbox=dict(boxstyle="round,pad=0.25", facecolor="#EFF6FF", edgecolor="#93C5FD", lw=0.9)
            if nd["y"] > 1.0 else None
        )

        # Cột phải (output latency)
        ax.text(
            10.15, cy, nd["right"], ha="center", va="center",
            fontsize=8.9, color="#7F1D1D" if nd["right_bold"] else "#475569",
            bbox=dict(boxstyle="round,pad=0.28", facecolor="#FEF2F2", edgecolor="#FCA5A5", lw=0.9)
            if nd["right_bold"] else None
        )

    # Mũi tên nối giữa các khối ở cột giữa (từ dưới lên thể hiện dòng dữ liệu)
    for i in range(len(nodes) - 1):
        y_top = nodes[i]["y"] - nodes[i]["h"] / 2 - 0.04
        y_bot = nodes[i + 1]["y"] + nodes[i + 1]["h"] / 2 + 0.04
        ax.annotate(
            "", xy=(6.1, y_top), xytext=(6.1, y_bot),
            arrowprops=dict(arrowstyle="-|>", color="#334155", lw=1.6)
        )

    # Mũi tên lớn bên trái: Duyệt xuống (Downward Traversal)
    ax.annotate(
        "", xy=(0.48, 1.55), xytext=(0.48, 7.15),
        arrowprops=dict(arrowstyle="-|>", color="#1D4ED8", lw=2.8)
    )
    ax.text(
        0.24, 4.35, "Duyệt xuống (Downward)\nTính tốc độ tiêu thụ y",
        rotation=90, ha="center", va="center", fontsize=9.8, fontweight="bold", color="#1D4ED8"
    )

    # Mũi tên lớn bên phải: Duyệt lên (Upward Traversal)
    ax.annotate(
        "", xy=(11.92, 6.20), xytext=(11.92, 0.70),
        arrowprops=dict(arrowstyle="-|>", color="#B91C1C", lw=2.8)
    )
    ax.text(
        11.68, 3.45, "Duyệt lên (Upward)\nƯớc lượng độ trễ đầu ra",
        rotation=90, ha="center", va="center", fontsize=9.8, fontweight="bold", color="#B91C1C"
    )

    # Chú giải dưới đáy
    legend_items = [
        patches.Patch(facecolor="#DBEAFE", edgecolor="#1D4ED8", label="Toán tử bất đồng bộ (dùng công thức M/M/1/k: p_empty)"),
        patches.Patch(facecolor="#FEF3C7", edgecolor="#B45309", label="Toán tử đồng bộ (hàm tuyến tính)"),
        patches.Patch(facecolor="#DCFCE7", edgecolor="#15803D", label="Nguồn đọc dữ liệu gốc"),
    ]
    ax.legend(
        handles=legend_items, loc="lower center", bbox_to_anchor=(0.5, -0.02),
        ncol=3, frameon=True, facecolor="#F8FAFC", edgecolor="#CBD5E1", fontsize=8.8
    )

    plt.tight_layout()
    for ext in ("png", "pdf"):
        out = OUT_DIR / f"TV1_Bai5_Hinh1_Autotune_Model.{ext}"
        fig.savefig(out, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print("Saved TV1_Bai5_Hinh1_Autotune_Model.{png,pdf}")


def draw_hinh2_mlperf_speedup():
    """Tái tạo Figure 8: Hệ số tăng tốc thời gian hội tụ huấn luyện MLPerf (End-to-End)."""
    benchmarks = [
        "ResNet-50\n(ImageNet)",
        "SSD\n(COCO)",
        "Mask-RCNN\n(COCO)",
        "GNMT\n(WMT16)",
        "Transformer\n(WMT17)",
    ]
    # Số liệu chính xác 100% từ Figure 8 (tr. 2953 — tfdata-PVLDB2021.pdf)
    exp_par = np.array([10.4, 17.9, 3.1, 1.4, 2.0])
    exp_opt = np.array([20.8, 21.9, 4.3, 1.6, 2.0])
    auto_opt = np.array([21.0, 22.0, 4.4, 1.5, 2.0])

    x = np.arange(len(benchmarks))
    width = 0.255

    fig, ax = plt.subplots(figsize=(11.2, 6.2), dpi=300)

    bars1 = ax.bar(
        x - width, exp_par, width,
        label="Expert-tuned Parallelism (Song song hóa thủ công)",
        color="#93C5FD", edgecolor="#1E3A8A", linewidth=1.1, hatch="///"
    )
    bars2 = ax.bar(
        x, exp_opt, width,
        label="Expert-tuned Parallelism + Optimizations (Đủ tính năng, chỉnh tay)",
        color="#2563EB", edgecolor="#0F172A", linewidth=1.1
    )
    bars3 = ax.bar(
        x + width, auto_opt, width,
        label="Autotune Parallelism + Optimizations (Tự động AUTOTUNE)",
        color="#059669", edgecolor="#064E3B", linewidth=1.1, hatch="..."
    )

    # Đường tham chiếu Baseline = 1.0x
    ax.axhline(1.0, color="#DC2626", linestyle="--", linewidth=1.4, zorder=3,
               label="Baseline đường ống tuần tự (1.0×)")

    # Vạch phân tách nhóm Ảnh vs Văn bản
    ax.axvline(2.5, color="#64748B", linestyle=":", linewidth=1.3)
    ax.text(1.0, 24.6, "Nhóm bài toán Thị giác máy tính (Ảnh)", ha="center", va="center",
            fontsize=9.8, fontweight="bold", color="#1E3A8A",
            bbox=dict(boxstyle="round,pad=0.28", facecolor="#EFF6FF", edgecolor="#BFDBFE"))
    ax.text(3.5, 24.6, "Nhóm Xử lý ngôn ngữ (Văn bản)", ha="center", va="center",
            fontsize=9.8, fontweight="bold", color="#475569",
            bbox=dict(boxstyle="round,pad=0.28", facecolor="#F1F5F9", edgecolor="#CBD5E1"))

    # Nhãn giá trị trên đầu cột
    for bars in (bars1, bars2, bars3):
        for bar in bars:
            h = bar.get_height()
            ax.text(
                bar.get_x() + bar.get_width() / 2, h + 0.38,
                f"{h:.1f}×", ha="center", va="bottom",
                fontsize=8.6, fontweight="bold", color="#0F172A"
            )

    # Hộp chú thích kết luận
    ax.text(
        3.52, 16.5,
        "Điểm nổi bật (MLPerf trên 8×TPUv3):\n"
        "• Đỉnh tăng tốc: 22.0× (SSD) & 21.0× (ResNet-50)\n"
        "• AUTOTUNE sát chuyên gia trong ≤ 1% (4/5 bài)\n"
        "• Xóa bỏ hoàn toàn nút thắt đường ống đầu vào",
        ha="center", va="center", fontsize=8.9, color="#064E3B",
        bbox=dict(boxstyle="round,pad=0.45", facecolor="#ECFDF5", edgecolor="#34D399", lw=1.2)
    )

    ax.set_ylabel("Hệ số tăng tốc thời gian hội tụ đầu-cuối (×)", fontsize=10.8, fontweight="bold", color="#0F172A")
    ax.set_xlabel("Tổ hợp Mô hình & Tập dữ liệu chuẩn MLPerf", fontsize=10.8, fontweight="bold", color="#0F172A")
    ax.set_title(
        "Hệ số tăng tốc thời gian huấn luyện đầu-cuối với tf.data trên bộ chuẩn MLPerf\n"
        "(Tái tạo từ Figure 8 — Murray et al., PVLDB 2021, tr. 2953 | Chuẩn hóa so với đường ống tuần tự = 1.0×)",
        fontsize=11.6, fontweight="bold", color="#0F172A", pad=14
    )
    ax.set_xticks(x)
    ax.set_xticklabels(benchmarks, fontsize=9.8, fontweight="bold")
    ax.set_ylim(0, 26.5)
    ax.grid(axis="y", linestyle="--", alpha=0.45, color="#94A3B8")
    ax.set_axisbelow(True)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.legend(
        loc="upper center", bbox_to_anchor=(0.5, -0.15), ncol=2,
        frameon=True, facecolor="#F8FAFC", edgecolor="#CBD5E1", fontsize=8.8
    )

    plt.tight_layout()
    for ext in ("png", "pdf"):
        out = OUT_DIR / f"TV1_Bai5_Hinh2_MLPerf_Speedup.{ext}"
        fig.savefig(out, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print("Saved TV1_Bai5_Hinh2_MLPerf_Speedup.{png,pdf}")


if __name__ == "__main__":
    draw_hinh1_autotune_model()
    draw_hinh2_mlperf_speedup()
