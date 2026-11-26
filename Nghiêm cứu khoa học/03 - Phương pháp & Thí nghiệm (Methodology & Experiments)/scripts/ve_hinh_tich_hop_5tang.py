#!/usr/bin/env python3
"""
Tạo 02 hình tích hợp cấp nhóm cho Báo cáo Cuối kỳ — Đề tài C (05 bài báo):
1. TV1_Hinh_KienTruc_TichHop_5Tang.{png,pdf} — Mục 3.1: Sơ đồ Kiến trúc Tích hợp 5 Tầng
2. Hinh_TongHop_HieuNang_5Tang.{png,pdf} — Mục 3.3: Biểu đồ Tổng hợp Định lượng 5 Tầng (mở rộng từ TV3)

Nhóm thực hiện (Lớp DCT123C4 — SGU):
TV1 Võ Huỳnh Minh Sang | TV2 Nguyễn Đình Cường | TV3 Châu Quốc Bảo | TV4 Nguyễn Hoàng Long
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["axes.unicode_minus"] = False

OUT_DIR = Path(__file__).resolve().parents[2] / "99 - Đính kèm (Attachments)"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def draw_integrated_5layer_arch():
    """Mục 3.1: Sơ đồ Kiến trúc Tích hợp 5 Tầng (Cloud Object Store -> GPU/TPU Training)."""
    fig, ax = plt.subplots(figsize=(13.2, 10.0), dpi=300)
    ax.set_xlim(0, 13.2)
    ax.set_ylim(0, 10.6)
    ax.axis("off")

    # Tiêu đề
    ax.text(
        6.6, 10.22,
        "KIẾN TRÚC TÍCH HỢP 5 TẦNG HẠ TẦNG QUẢN TRỊ DỮ LIỆU CHO HỌC MÁY QUY MÔ LỚN",
        ha="center", va="center", fontsize=13.2, fontweight="bold", color="#0F172A"
    )
    ax.text(
        6.6, 9.85,
        "Liên kết 05 công trình PVLDB / ACM SIGMOD (Scopus Q1, WoS, CORE A*) — Từ lưu trữ đối tượng đám mây đến GPU/TPU",
        ha="center", va="center", fontsize=9.6, style="italic", color="#475569"
    )

    # Đầu ra đỉnh: GPU/TPU Training Cluster
    top_box = patches.FancyBboxPatch(
        (3.4, 8.95), 6.4, 0.56,
        boxstyle="round,pad=0.04,rounding_size=0.10",
        facecolor="#1E293B", edgecolor="#0F172A", linewidth=1.6
    )
    ax.add_patch(top_box)
    ax.text(
        6.6, 9.23,
        "TẦNG ỨNG DỤNG AI/ML: Huấn luyện & Suy luận Mô hình (GPU / TPU Cluster)",
        ha="center", va="center", fontsize=10.2, fontweight="bold", color="white"
    )

    # 5 tầng chính từ trên xuống dưới (không ghi tên thành viên trong sơ đồ học thuật)
    layers = [
        {
            "y": 7.55, "h": 1.02,
            "tag": "TẦNG 5\nML Input",
            "title": "Đường ống Nạp Dữ liệu Huấn luyện — tf.data (Google, PVLDB 2021)",
            "tech": "API khai báo (Dataset/Iterator) • Tối ưu tĩnh Grappler (map+batch fusion) • AUTOTUNE (M/M/1/k + Gradient Descent)",
            "solve": "Giải quyết: Nghẽn I/O & tiền xử lý CPU (tăng tốc hội tụ 21×–22× trên MLPerf; sát chuyên gia ≤ 1%)",
            "bg": "#ECFDF5", "edge": "#059669", "tag_bg": "#059669",
            "bridge_up": "Nạp tensor song song (Prefetch, Zero-stall GPU/TPU)",
        },
        {
            "y": 6.08, "h": 1.02,
            "tag": "TẦNG 4\nFeature Store",
            "title": "Kho Đặc trưng & Tối ưu Đường ống ML — FeathrPO (Microsoft, PVLDB 2023)",
            "tech": "Mô hình chi phí KLL sketches (96.8–99.7%) • Viết lại tái sử dụng & Semijoin • Chọn phân vùng bằng BIP (OR-Tools)",
            "solve": "Giải quyết: PIT Join chậm, shuffle lớn, tính toán lặp & rò rỉ dữ liệu (tăng tốc tới 3.00× trên TPCx-AI)",
            "bg": "#F5F3FF", "edge": "#7C3AED", "tag_bg": "#7C3AED",
            "bridge_up": "Xuất tập huấn luyện chuẩn thời gian (PIT-consistent Dataset)",
        },
        {
            "y": 4.61, "h": 1.02,
            "tag": "TẦNG 3\nQuery Engine",
            "title": "Động cơ Thực thi Truy vấn Vector hóa — Photon (Databricks, SIGMOD 2022)",
            "tech": "Native C++ Column Batch • SIMD Kernels • Vectorized Hash Table • Adaptive Join Compaction • Zero-copy JNI (~23 ns)",
            "solve": "Giải quyết: Trần hiệu năng JVM/GC & JIT bailout trên Spark (nhanh hơn 4.0× TB TPC-H; kỷ lục TPC-DS 100 TB)",
            "bg": "#FFF7ED", "edge": "#EA580C", "tag_bg": "#EA580C",
            "bridge_up": "Truy vấn SQL/ETL tốc độ C++ cho Feature Engineering",
        },
        {
            "y": 3.14, "h": 1.02,
            "tag": "TẦNG 2 (LÕI)\nACID Table",
            "title": "Tầng Bảng Giao dịch ACID — Delta Lake (Databricks/UCB, PVLDB 2020)",
            "tech": "Nhật ký _delta_log (JSON + Parquet Checkpoint) • Kiểm soát OCC • Data Skipping • Z-Order • Time Travel • Batch+Stream",
            "solve": "Giải quyết: Thiếu ACID, tệp nhỏ & LIST chậm trên Object Store (nhanh hơn 1.55× Spark Parquet / 4.04× Presto)",
            "bg": "#EFF6FF", "edge": "#1D4ED8", "tag_bg": "#1D4ED8",
            "bridge_up": "Cung cấp Snapshot ACID, Data Skipping & OffHeapColumnVector",
        },
        {
            "y": 1.67, "h": 1.02,
            "tag": "TẦNG 1\nFile Format",
            "title": "Định dạng Tệp Cột Mở & Nén Nhẹ — BtrBlocks (TU Munich/FAU, SIGMOD 2023)",
            "tech": "Nén đệ quy ≤ 3 tầng • Lấy mẫu 10×64 (1%) • Pseudodecimal (Double) & FSST (String) • SIMD AVX2 • Tách rời Metadata",
            "solve": "Giải quyết: Nghẽn giải nén Parquet trên mạng 100 Gbps (Tc = 86.2 Gbps; nhanh 2.6×–3.5×, rẻ 1.8× trên S3)",
            "bg": "#F0FDFA", "edge": "#0D9488", "tag_bg": "#0D9488",
            "bridge_up": "Khối cột nén tách rời Metadata (tương thích kiến trúc _delta_log)",
        },
    ]

    # Nền đáy: Cloud Object Storage
    bot_box = patches.FancyBboxPatch(
        (1.0, 0.42), 9.4, 0.62,
        boxstyle="round,pad=0.04,rounding_size=0.10",
        facecolor="#334155", edgecolor="#0F172A", linewidth=1.6
    )
    ax.add_patch(bot_box)
    ax.text(
        5.7, 0.73,
        "HẠ TẦNG LƯU TRỮ ĐÁM MÂY: Cloud Object Storage (AWS S3 / Azure ADLS / GCS / MinIO — Mạng 100 Gbps)",
        ha="center", va="center", fontsize=9.8, fontweight="bold", color="white"
    )

    for idx, ly in enumerate(layers):
        y0 = ly["y"]
        h = ly["h"]
        # Khung tầng chính
        box = patches.FancyBboxPatch(
            (1.0, y0), 9.4, h,
            boxstyle="round,pad=0.04,rounding_size=0.10",
            facecolor=ly["bg"], edgecolor=ly["edge"], linewidth=1.8
        )
        ax.add_patch(box)

        # Nhãn tầng bên trái
        tag_box = patches.FancyBboxPatch(
            (1.08, y0 + 0.12), 1.48, h - 0.24,
            boxstyle="round,pad=0.02,rounding_size=0.08",
            facecolor=ly["tag_bg"], edgecolor="none"
        )
        ax.add_patch(tag_box)
        ax.text(
            1.82, y0 + h / 2, ly["tag"],
            ha="center", va="center", fontsize=8.8, fontweight="bold", color="white"
        )

        # Nội dung tầng
        ax.text(2.74, y0 + 0.78, ly["title"], ha="left", va="center", fontsize=9.7, fontweight="bold", color="#0F172A")
        ax.text(2.74, y0 + 0.49, ly["tech"], ha="left", va="center", fontsize=8.3, color="#334155")
        ax.text(2.74, y0 + 0.20, ly["solve"], ha="left", va="center", fontsize=8.3, fontweight="bold", color=ly["edge"])

        # Mũi tên đi lên tới tầng tiếp theo
        y_from = y0 + h + 0.04
        y_to = (layers[idx - 1]["y"] - 0.04) if idx > 0 else 8.91
        ax.annotate(
            "", xy=(5.7, y_to), xytext=(5.7, y_from),
            arrowprops=dict(arrowstyle="-|>", color="#1E293B", lw=1.9)
        )
        ax.text(
            5.86, (y_from + y_to) / 2, ly["bridge_up"],
            ha="left", va="center", fontsize=8.2, style="italic", color="#334155"
        )

    # Mũi tên từ Cloud Object Storage lên Tầng 1
    ax.annotate(
        "", xy=(5.7, 1.63), xytext=(5.7, 1.08),
        arrowprops=dict(arrowstyle="-|>", color="#1E293B", lw=1.9)
    )
    ax.text(5.86, 1.35, "Đọc/Ghi tệp đối tượng băng thông cao (HTTP GET/PUT)", ha="left", va="center", fontsize=8.2, style="italic", color="#334155")

    # Cột bên phải: Trục Phản hồi Ngữ nghĩa Xuyên tầng (Hướng nghiên cứu mở — Chương 4)
    side_box = patches.FancyBboxPatch(
        (10.75, 1.67), 2.2, 6.90,
        boxstyle="round,pad=0.05,rounding_size=0.12",
        facecolor="#FEFCE8", edgecolor="#CA8A04", linewidth=1.6, linestyle="--"
    )
    ax.add_patch(side_box)
    ax.text(
        11.85, 8.20,
        "HƯỚNG MỞ RỘNG\nXUYÊN TẦNG\n(Chương 4)",
        ha="center", va="center", fontsize=9.4, fontweight="bold", color="#854D0E"
    )
    side_notes = [
        (7.15, "• Đẩy phép chiếu &\n  lọc (Projection\n  Pushdown) xuống\n  lưu trữ"),
        (5.75, "• Chia sẻ cache\n  đặc trưng liên\n  tác vụ (Cross-job\n  Reuse)"),
        (4.35, "• Truyền gợi ý\n  TTL & khóa thực\n  thể xuống Z-Order\n  của Delta Lake"),
        (2.85, "• Bộ nhớ trao đổi\n  Zero-copy (Arrow\n  Flight / DLPack)\n  C++ ↔ Python"),
    ]
    for ny, ntxt in side_notes:
        ax.text(10.92, ny, ntxt, ha="left", va="center", fontsize=8.0, color="#713F12")

    # Mũi tên phản hồi từ Tầng 5 xuống Tầng 1 ở cột phải
    ax.annotate(
        "", xy=(10.55, 2.1), xytext=(10.55, 8.0),
        arrowprops=dict(arrowstyle="-|>", color="#CA8A04", lw=2.2, ls="--")
    )

    plt.tight_layout()
    for ext in ("png", "pdf"):
        out = OUT_DIR / f"TV1_Hinh_KienTruc_TichHop_5Tang.{ext}"
        fig.savefig(out, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print("Saved TV1_Hinh_KienTruc_TichHop_5Tang.{png,pdf}")


def draw_5layer_speedup_synthesis():
    """Mục 3.3 (Mở rộng 5 tầng): Tổng hợp định lượng Speedup & % Time Saved qua 5 tầng."""
    labels = [
        "Tầng 5: tf.data (MLPerf — SSD / ResNet-50)*\n(vs. Đường ống tuần tự, 8×TPUv3, đỉnh 22.0×)",
        "Tầng 5: tf.data (MLPerf — TB 5 mô hình)\n(Song song hóa & Pipelining vs. Tuần tự)",
        "Tầng 4: FeathrPO (TPCx-AI UC10)*\n(Cận trên PIT Join vs. Feathr mặc định)",
        "Tầng 3: Photon (TPC-H SF=3000)\n(Trung bình 22 câu vs. DBR, đỉnh 23× ở Q1)",
        "Tầng 3: Photon (TPC-DS Q24 — Adaptive)\n(Có vs. Không Join Compaction / DBR)",
        "Tầng 2: Delta Lake (TPC-DS 1 TB)\n(vs. 3rd-Party Spark Parquet; 4.04× vs. Presto)",
        "Tầng 1: BtrBlocks (Public BI — Quét S3)\n(Giải nén Tu vs. Parquet+Zstd; Tc đạt 3.48×)",
    ]
    # Đảo ngược để Tầng 1 ở dưới, Tầng 5 ở trên (hoặc Tầng 1 trên -> Tầng 5 dưới cho dễ đọc luồng từ dưới lên)
    speedups = np.array([21.0, 7.0, 3.00, 4.00, 1.55, 1.55, 2.22])
    time_saved = (1.0 - 1.0 / speedups) * 100.0
    is_upper = [True, False, True, False, False, False, False]
    colors = ["#047857", "#10B981", "#7C3AED", "#EA580C", "#F59E0B", "#2563EB", "#0D9488"]

    # Sắp xếp từ Tầng 1 ở trên cùng xuống Tầng 5 ở dưới cùng (luồng lưu trữ -> huấn luyện)
    labels = labels[::-1]
    speedups = speedups[::-1]
    time_saved = time_saved[::-1]
    is_upper = is_upper[::-1]
    colors = colors[::-1]

    y = np.arange(len(labels))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15.0, 6.8), sharey=True, dpi=300, gridspec_kw={"width_ratios": [1.12, 1.0]})

    # Panel A: Speedup (thang log hoặc tuyến tính với chú thích rõ vì 21.0x lớn hơn 1.55x nhiều -> dùng log scale sạch sẽ!)
    for i in range(len(labels)):
        hatch = "///" if is_upper[i] else None
        ax1.barh(y[i], speedups[i], height=0.60, color=colors[i], edgecolor="#0F172A", linewidth=1.0, hatch=hatch)
        suffix = " (cận trên*)" if is_upper[i] else ""
        ax1.text(
            speedups[i] * 1.07, y[i], f"{speedups[i]:.2f}×{suffix}",
            va="center", ha="left", fontsize=8.8, fontweight="bold", color="#0F172A"
        )

    ax1.axvline(1.0, color="#DC2626", linestyle="--", linewidth=1.3)
    ax1.text(1.04, -0.58, "Mốc 1.0×", color="#DC2626", fontsize=8.2, fontweight="bold", ha="left")
    ax1.set_xscale("log")
    ax1.set_xlim(0.85, 58.0)
    ax1.set_xticks([1, 2, 4, 10, 20, 40])
    ax1.get_xaxis().set_major_formatter(plt.ScalarFormatter())
    ax1.set_xlabel("Hệ số tăng tốc — Speedup (×, thang logarit)", fontsize=10.2, fontweight="bold", color="#0F172A")
    ax1.set_title("(A) Hệ số cải thiện theo từng tầng (so với đối chứng 1.0× riêng)", fontsize=10.6, fontweight="bold", color="#0F172A", pad=10)
    ax1.set_yticks(y)
    ax1.set_yticklabels(labels, fontsize=8.7, fontweight="bold", color="#1E293B")
    ax1.invert_yaxis()
    ax1.grid(axis="x", linestyle="--", alpha=0.4, color="#94A3B8")
    ax1.set_axisbelow(True)
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)

    # Panel B: % Time Saved
    for i in range(len(labels)):
        hatch = "///" if is_upper[i] else None
        ax2.barh(y[i], time_saved[i], height=0.60, color=colors[i], edgecolor="#0F172A", linewidth=1.0, hatch=hatch, alpha=0.9)
        ax2.text(
            time_saved[i] + 1.4, y[i], f"−{time_saved[i]:.1f}%",
            va="center", ha="left", fontsize=8.8, fontweight="bold", color="#0F172A"
        )

    ax2.set_xlim(0, 112)
    ax2.set_xlabel("Tỷ lệ cắt giảm thời gian thực thi tương ứng (%)", fontsize=10.2, fontweight="bold", color="#0F172A")
    ax2.set_title("(B) Thời gian thực thi tiết kiệm được = (1 − 1/Speedup) × 100%", fontsize=10.6, fontweight="bold", color="#0F172A", pad=10)
    ax2.grid(axis="x", linestyle="--", alpha=0.4, color="#94A3B8")
    ax2.set_axisbelow(True)
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)

    fig.suptitle(
        "Tổng hợp Định lượng Hiệu quả Cải thiện Xuyên suốt 5 Tầng Kiến trúc Lakehouse cho Học máy",
        fontsize=13.0, fontweight="bold", color="#0F172A", y=0.98
    )

    fig.text(
        0.5, 0.01,
        "Lưu ý phương pháp luận (Liêm chính học thuật): Mỗi công trình đo trên bộ chuẩn, cụm phần cứng và mốc đối chứng 1.0× khác nhau.\n"
        "Thanh gạch chéo (*) biểu thị giá trị cận trên (ResNet-50 21.0× / SSD 22.0× ở tf.data; tối đa 3.00× ở FeathrPO). Tuyệt đối KHÔNG cộng hay nhân các hệ số giữa các tầng (Định luật Amdahl).",
        ha="center", va="bottom", fontsize=8.3, style="italic", color="#475569",
        bbox=dict(boxstyle="round,pad=0.35", facecolor="#FFFBEB", edgecolor="#FCD34D", lw=1.0)
    )

    plt.tight_layout(rect=[0, 0.075, 1, 0.94])
    for ext in ("png", "pdf"):
        out = OUT_DIR / f"Hinh_TongHop_HieuNang_5Tang.{ext}"
        fig.savefig(out, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print("Saved Hinh_TongHop_HieuNang_5Tang.{png,pdf}")


if __name__ == "__main__":
    draw_integrated_5layer_arch()
    draw_5layer_speedup_synthesis()
