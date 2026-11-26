"""
MÃ NGUỒN TÁI TẠO 02 HÌNH GỐC (FIGURE 1 & FIGURE 9 — PHOTON, ACM SIGMOD 2022)
VÀ XÂY DỰNG 01 HÌNH ĐỀ XUẤT MỚI CẤP NHÓM (TỔNG HỢP ĐỊNH LƯỢNG 4 TẦNG KIẾN TRÚC)

Sinh viên thực hiện: Châu Quốc Bảo (TV3) - Lớp: DCT123C4 - MSSV: 3123411024
Học phần: Phương pháp Nghiên cứu Khoa học trong Công nghệ Thông tin
Công cụ: Python 3 + Matplotlib
Đầu ra: PNG (300 DPI) + PDF (Vector) lưu tại 99 - Đính kèm (Attachments)/
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch

OUT_DIR = Path(__file__).resolve().parents[2] / "99 - Đính kèm (Attachments)"
OUT_DIR.mkdir(parents=True, exist_ok=True)

plt.rcParams.update(
    {
        "font.sans-serif": ["DejaVu Sans", "Liberation Sans", "Arial"],
        "axes.unicode_minus": False,
        "font.size": 10,
    }
)


def save_figure(fig, name: str) -> None:
    for ext in ("png", "pdf"):
        out_path = OUT_DIR / f"{name}.{ext}"
        fig.savefig(out_path, dpi=300, bbox_inches="tight", facecolor="white")
        print(f"Saved: {out_path}")
    plt.close(fig)


def draw_rounded_box(
    ax,
    x: float,
    y: float,
    w: float,
    h: float,
    text: str,
    fc: str,
    ec: str,
    lw: float = 1.4,
    fontsize: float = 9.0,
    fw: str = "normal",
    tc: str = "#0f172a",
    zorder: int = 3,
    ls: str = "-",
    pad: float = 0.04,
    rounding: float = 0.14,
):
    box = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle=f"round,pad={pad},rounding_size={rounding}",
        facecolor=fc,
        edgecolor=ec,
        linewidth=lw,
        linestyle=ls,
        zorder=zorder,
    )
    ax.add_patch(box)
    if text:
        ax.text(
            x + w / 2,
            y + h / 2,
            text,
            ha="center",
            va="center",
            fontsize=fontsize,
            fontweight=fw,
            color=tc,
            zorder=zorder + 1,
        )
    return box


def draw_arrow(
    ax,
    start,
    end,
    color="#334155",
    lw=1.5,
    ls="-",
    style="-|>,head_width=0.24,head_length=0.38",
    zorder=4,
    rad=0.0,
):
    props = dict(arrowstyle=style, color=color, lw=lw, linestyle=ls)
    if rad != 0:
        props["connectionstyle"] = f"arc3,rad={rad}"
    ax.annotate("", xy=end, xytext=start, arrowprops=props, zorder=zorder)


# ==============================================================================
# HÌNH 1: TÁI TẠO FIGURE 1 — TẦNG THỰC THI DATABRICKS RUNTIME & PHOTON (TR. 2328)
# ==============================================================================
def build_figure_1():
    fig, ax = plt.subplots(figsize=(14.6, 7.6), dpi=300)
    ax.set_xlim(0, 20.4)
    ax.set_ylim(0, 10.7)
    ax.axis("off")

    # Tiêu đề chính & phụ
    ax.text(
        10.2,
        10.28,
        "Hình tái tạo Figure 1: Kiến trúc tầng thực thi Databricks Runtime và Photon trên Lakehouse",
        ha="center",
        va="center",
        fontsize=13.2,
        fontweight="bold",
        color="#0f172a",
    )
    ax.text(
        10.2,
        9.82,
        "[Databricks' Execution Layer — Nguồn: Behm et al., ACM SIGMOD 2022, Figure 1, trang 2328 (Trang 3)]",
        ha="center",
        va="center",
        fontsize=9.4,
        color="#475569",
    )

    # Khung bao chính: Databricks Runtime (nét đứt cam như bản gốc)
    ax.add_patch(
        FancyBboxPatch(
            (4.85, 4.78),
            15.00,
            4.58,
            boxstyle="round,pad=0.06,rounding_size=0.18",
            facecolor="#fffdf9",
            edgecolor="#ea580c",
            linewidth=1.5,
            linestyle="--",
            zorder=0,
        )
    )
    ax.text(
        12.35,
        9.10,
        "Databricks Runtime (DBR — Nền tảng thực thi phân tán dựa trên Apache Spark)",
        ha="center",
        va="center",
        fontsize=10.1,
        fontweight="bold",
        color="#c2410c",
    )

    # 1. Các cụm máy ảo bên trái (Databricks Runtime Clusters)
    ax.text(
        2.35,
        7.85,
        "Các cụm Databricks Runtime\n(Cloud VMs: AWS / Azure / GCP)",
        ha="center",
        va="center",
        fontsize=9.0,
        fontweight="bold",
        color="#334155",
    )
    for cx_left, highlight in [(0.45, False), (2.55, True)]:
        ec = "#0284c7" if highlight else "#94a3b8"
        fc = "#e0f2fe" if highlight else "#e2e8f0"
        draw_rounded_box(ax, cx_left, 5.78, 1.72, 1.35, "", fc=fc, ec=ec, lw=1.4, zorder=1)
        pts = [(cx_left + 0.86, 6.74), (cx_left + 0.44, 6.14), (cx_left + 1.28, 6.14)]
        for a, b in [(pts[0], pts[1]), (pts[0], pts[2]), (pts[1], pts[2])]:
            ax.plot([a[0], b[0]], [a[1], b[1]], color="#475569", lw=1.2, zorder=2)
        for px, py in pts:
            ax.add_patch(patches.Circle((px, py), 0.15, facecolor="white", edgecolor="#334155", lw=1.2, zorder=3))

    # Đường nối phóng to từ cụm thứ 2 vào khung Cluster chi tiết
    ax.plot([4.30, 5.15], [7.13, 8.70], color="#64748b", lw=1.1, ls=":", zorder=1)
    ax.plot([4.30, 5.15], [5.78, 5.14], color="#64748b", lw=1.1, ls=":", zorder=1)

    # 2. Khung Cluster chi tiết bên trong DBR (Driver + Executor)
    draw_rounded_box(
        ax, 5.18, 5.10, 8.55, 3.65, "", fc="#f1f5f9", ec="#475569", lw=1.4, zorder=1, rounding=0.22
    )

    # 2a. Driver
    draw_rounded_box(
        ax, 5.42, 5.32, 3.92, 3.20, "", fc="#e2e8f0", ec="#64748b", lw=1.2, zorder=2, rounding=0.16
    )
    ax.text(
        7.38, 8.26, "Driver (Điều phối trung tâm)",
        ha="center", va="center", fontsize=8.8, fontweight="bold", color="#0f172a", zorder=4
    )
    draw_rounded_box(
        ax, 5.64, 6.96, 3.48, 0.92,
        "Bộ lập lịch tác vụ\n(Task Scheduler)",
        fc="#ffffff", ec="#475569", lw=1.2, fontsize=8.5, fw="bold", zorder=3
    )
    draw_rounded_box(
        ax, 5.64, 5.54, 3.48, 1.04,
        "Trình phân tích & tối ưu\n(Catalyst Query Optimizer)",
        fc="#ffffff", ec="#475569", lw=1.2, fontsize=8.1, fw="bold", zorder=3
    )
    draw_arrow(ax, (7.38, 6.62), (7.38, 6.93), color="#334155", lw=1.3, zorder=5)

    # 2b. Executor (JVM Process đa luồng)
    draw_rounded_box(
        ax, 9.72, 5.32, 3.78, 3.20, "", fc="#e2e8f0", ec="#64748b", lw=1.2, zorder=2, rounding=0.16
    )
    ax.text(
        11.61, 8.26, "Executor (Tiến trình đa luồng)",
        ha="center", va="center", fontsize=8.7, fontweight="bold", color="#0f172a", zorder=4
    )

    cpu_specs = [
        (9.96, 6.90, "CPU 0", "#ffffff", "#64748b", False),
        (11.86, 6.90, "CPU 1\n(Photon)", "#ffedd5", "#c2410c", True),
        (9.96, 5.56, "CPU 2", "#ffffff", "#64748b", False),
        (11.86, 5.56, "CPU 3", "#ffffff", "#64748b", False),
    ]
    for cx, cy, label, fc, ec, is_hot in cpu_specs:
        draw_rounded_box(
            ax, cx, cy, 1.38, 0.86, label, fc=fc, ec=ec,
            lw=1.8 if is_hot else 1.1, fontsize=8.4, fw="bold" if is_hot else "normal",
            tc="#9a3412" if is_hot else "#334155", zorder=4
        )

    # Mũi tên nét đứt từ Task Scheduler gửi task tới 4 CPU (đường cong né không cắt chữ CPU 0 / CPU 2)
    draw_arrow(ax, (9.14, 7.38), (9.94, 7.34), color="#475569", lw=1.1, ls=":", zorder=3)
    draw_arrow(ax, (9.14, 7.62), (12.45, 7.80), color="#c2410c", lw=1.25, ls=":", zorder=3, rad=-0.22)
    draw_arrow(ax, (9.14, 7.22), (9.94, 6.02), color="#475569", lw=1.1, ls=":", zorder=3)
    draw_arrow(ax, (9.14, 7.12), (11.84, 6.18), color="#475569", lw=1.1, ls=":", zorder=3, rad=0.14)

    # 3. Khối phóng to Photon Task (Đơn luồng C++ Vectorized trên mỗi phân vùng)
    draw_rounded_box(
        ax, 14.32, 5.10, 5.25, 3.65, "", fc="#fff7ed", ec="#c2410c", lw=1.7, zorder=2, rounding=0.20
    )
    draw_rounded_box(
        ax, 17.28, 8.08, 2.08, 0.54, "Photon Task\n(C++ đơn luồng)",
        fc="#fed7aa", ec="#c2410c", lw=1.3, fontsize=8.1, fw="bold", tc="#7c2d12", zorder=4
    )
    ax.text(
        15.72, 8.35, "Thực thi theo\nlô cột (Batch)",
        ha="center", va="center", fontsize=8.4, fontweight="bold", color="#9a3412", zorder=4
    )

    # Chuỗi toán tử trong Photon Task: FileScan -> Filter -> Join
    draw_rounded_box(ax, 14.66, 7.18, 4.56, 0.58, "Join (Vectorized Hash Table)", fc="#ffffff", ec="#9a3412", lw=1.25, fontsize=8.4, fw="bold", zorder=4)
    draw_rounded_box(ax, 14.66, 6.26, 4.56, 0.58, "Filter (Position List / Adaptive)", fc="#ffffff", ec="#9a3412", lw=1.25, fontsize=8.4, fw="bold", zorder=4)
    draw_rounded_box(ax, 14.66, 5.34, 4.56, 0.58, "FileScan (Adapter Zero-copy JNI)", fc="#ffffff", ec="#9a3412", lw=1.25, fontsize=8.4, fw="bold", zorder=4)
    draw_arrow(ax, (16.94, 5.95), (16.94, 6.24), color="#c2410c", lw=1.5, zorder=5)
    draw_arrow(ax, (16.94, 6.87), (16.94, 7.16), color="#c2410c", lw=1.5, zorder=5)

    # Đường phóng to từ CPU 1 sang Photon Task
    ax.plot([13.26, 14.32], [7.76, 8.68], color="#c2410c", lw=1.3, ls="-", zorder=2)
    ax.plot([13.26, 14.32], [6.90, 5.15], color="#c2410c", lw=1.3, ls="-", zorder=2)

    # 4. Tầng dưới trái: Truy vấn người dùng (User Queries)
    draw_rounded_box(
        ax, 0.45, 2.30, 11.75, 1.54, "", fc="#f8fafc", ec="#0284c7", lw=1.4, zorder=2, rounding=0.14
    )
    ax.text(
        6.32, 3.52,
        "Truy vấn người dùng (User Queries — Apache Spark DataFrame API & SQL)",
        ha="center", va="center", fontsize=9.4, fontweight="bold", color="#0369a1", zorder=4
    )
    ax.text(
        6.32, 3.02,
        'DataFrame API:  df.select($"col1").filter($"col2" > 0).join(df2)',
        ha="center", va="center", fontsize=8.7, family="monospace", color="#1e293b", zorder=4, parse_math=False
    )
    ax.text(
        6.32, 2.60,
        "SQL Query:      SELECT * FROM t1, t2 WHERE col2 > 0 AND t1.id = t2.id",
        ha="center", va="center", fontsize=8.7, family="monospace", color="#1e293b", zorder=4
    )
    draw_arrow(ax, (3.41, 3.88), (3.41, 5.72), color="#0284c7", lw=2.2, zorder=4)
    draw_arrow(ax, (7.38, 3.88), (7.38, 5.50), color="#0284c7", lw=2.2, zorder=4)
    ax.text(
        7.62, 4.30, "Gửi kế hoạch SQL / DataFrame",
        ha="left", va="center", fontsize=8.2, color="#0369a1", style="italic",
        bbox=dict(boxstyle="round,pad=0.14", facecolor="white", edgecolor="none", alpha=0.92),
        zorder=5,
    )

    # 5. Tầng dưới phải: User Cloud Storage + Delta Lake
    draw_rounded_box(
        ax, 13.45, 2.02, 6.40, 2.34, "", fc="#eef2ff", ec="#1d4ed8", lw=1.5, zorder=2, rounding=0.18
    )
    ax.text(
        16.65, 4.06,
        "DELTA LAKE (Tầng bảng giao dịch ACID)",
        ha="center", va="center", fontsize=9.8, fontweight="bold", color="#1e3a8a", zorder=4
    )
    draw_rounded_box(
        ax, 13.75, 3.10, 5.80, 0.68,
        "Siêu dữ liệu (_delta_log)\nTransaction Log & Min/Max Stats",
        fc="#ffffff", ec="#3b82f6", lw=1.1, fontsize=7.9, fw="bold", tc="#1e3a8a", zorder=4
    )
    draw_rounded_box(
        ax, 13.75, 2.24, 5.80, 0.64,
        "Tệp dữ liệu cột mở Apache Parquet (Data Files)",
        fc="#ffffff", ec="#3b82f6", lw=1.1, fontsize=7.9, fw="bold", tc="#1e3a8a", zorder=4
    )
    ax.text(
        16.65, 1.65,
        "Lưu trữ đối tượng đám mây (User Cloud Storage: S3 / ADLS / GCS)",
        ha="center", va="center", fontsize=8.7, fontweight="bold", color="#334155",
    )

    # Mũi tên dữ liệu từ Delta Lake lên FileScan của Photon Task
    draw_arrow(ax, (16.94, 4.38), (16.94, 5.32), color="#1d4ed8", lw=2.2, zorder=5)
    ax.text(
        17.16, 4.62, "Đọc cột & Data Skipping",
        ha="left", va="center", fontsize=8.0, color="#1d4ed8", style="italic",
        bbox=dict(boxstyle="round,pad=0.12", facecolor="white", edgecolor="none", alpha=0.92),
        zorder=6,
    )

    # 6. Chú giải màu sắc (Legend) ở đáy
    draw_rounded_box(ax, 0.45, 0.28, 19.40, 0.96, "", fc="#ffffff", ec="#94a3b8", lw=1.0, zorder=1, rounding=0.12)
    legend_items = [
        (0.80, "#e0f2fe", "#0284c7", "Đầu vào & Cụm máy ảo\n(SQL / DataFrame API)"),
        (5.25, "#e2e8f0", "#475569", "Điều phối Databricks Runtime\n(Driver & Executor JVM)"),
        (10.15, "#fed7aa", "#c2410c", "Động cơ thực thi Photon\n(C++ Vectorized đơn luồng/phân vùng)"),
        (15.45, "#eef2ff", "#1d4ed8", "Tầng lưu trữ mở\n(Delta Lake + Parquet / Cloud)"),
    ]
    for lx, fc, ec, lbl in legend_items:
        draw_rounded_box(ax, lx, 0.57, 0.46, 0.38, "", fc=fc, ec=ec, lw=1.3, zorder=3, pad=0.02, rounding=0.06)
        ax.text(lx + 0.62, 0.76, lbl, ha="left", va="center", fontsize=8.0, color="#1e293b", zorder=3)

    save_figure(fig, "TV3_Hinh1_KienTruc_Photon")


# ==============================================================================
# HÌNH 2: TÁI TẠO FIGURE 9 — TPC-DS Q24 & ADAPTIVE JOIN COMPACTION (TR. 2337)
# ==============================================================================
def build_figure_2():
    fig, ax = plt.subplots(figsize=(9.8, 6.0), dpi=300)

    labels = [
        "DBR\n(Spark SQL Code-Gen\n— Mốc đối chứng)",
        "Photon\n(Không bật\nJoin Compaction)",
        "Photon\n(Có bật Adaptive\nJoin Compaction)",
    ]
    vals = [118, 120, 76]
    colors = ["#94a3b8", "#60a5fa", "#0f766e"]
    hatches = ["", "...", ""]

    x = range(len(labels))
    bars = ax.bar(x, vals, width=0.50, color=colors, edgecolor="#1e293b", linewidth=1.25, zorder=3)
    for bar, h in zip(bars, hatches):
        if h:
            bar.set_hatch(h)

    # Đường tham chiếu mốc DBR = 118 giây
    ax.axhline(118, color="#475569", linestyle="--", linewidth=1.25, alpha=0.85, zorder=2, label="Mốc đối chứng DBR (118 giây)")

    # Nhãn giá trị trực tiếp trên cột
    for i, (bar, v) in enumerate(zip(bars, vals)):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            v + 2.8,
            f"{v} giây",
            ha="center",
            va="bottom",
            fontsize=11.5,
            fontweight="bold",
            color="#0f766e" if i == 2 else "#0f172a",
        )

    # Chú thích phân tích cho cột 2 (đặt lệch phải trên đỉnh cột 2, không chạm legend bên trái)
    ax.annotate(
        "Chậm hơn +1,7% so với DBR\n(chi phí diễn giải trên batch thưa)",
        xy=(1.0, 130.5),
        xytext=(1.22, 151),
        ha="center",
        fontsize=8.9,
        color="#1d4ed8",
        fontweight="bold",
        bbox=dict(boxstyle="round,pad=0.38", facecolor="#eff6ff", edgecolor="#60a5fa", lw=1.15),
        arrowprops=dict(arrowstyle="-|>", color="#2563eb", lw=1.35),
    )

    # Chú thích phân tích cho cột 3 (căn gọn trên cột 3, không chạm cột 2)
    ax.annotate(
        "Nhanh hơn 1,55× so với DBR (−35,6%)\nNhanh hơn 1,58× so với không nén (−36,7%)",
        xy=(2.0, 88),
        xytext=(1.96, 114),
        ha="center",
        fontsize=8.9,
        color="#065f46",
        fontweight="bold",
        bbox=dict(boxstyle="round,pad=0.38", facecolor="#ecfdf5", edgecolor="#0f766e", lw=1.3),
        arrowprops=dict(arrowstyle="-|>", color="#0f766e", lw=1.5),
    )

    ax.set_xticks(list(x))
    ax.set_xticklabels(labels, fontsize=9.8, fontweight="bold", color="#1e293b")
    ax.set_ylabel("Thời gian thực thi truy vấn (giây — thấp hơn tốt hơn)", fontsize=10.5, fontweight="bold", color="#0f172a")
    ax.set_xlim(-0.52, 2.58)
    ax.set_ylim(0, 170)
    ax.grid(axis="y", linestyle="--", alpha=0.35, zorder=0)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.legend(loc="upper left", fontsize=9.2, frameon=True)

    ax.set_title(
        "Hình tái tạo Figure 9: Tác động của Adaptive Join Compaction trong Photon (TPC-DS Q24)\n"
        "[Cụm 16 nút AWS — Thời gian chạy của DBR so với Photon có/không nén batch thưa]",
        fontsize=11.5,
        fontweight="bold",
        color="#0f172a",
        pad=14,
    )
    fig.text(
        0.5,
        -0.02,
        "Nguồn: Behm et al., ACM SIGMOD 2022, Figure 9, trang 2337 (Trang 12). Giá trị nhãn cột trích xuất trực tiếp từ biểu đồ gốc (118 s, 120 s, 76 s).",
        ha="center",
        fontsize=8.3,
        color="#475569",
    )

    plt.tight_layout()
    save_figure(fig, "TV3_Hinh2_TPCDS_Q24")


# ==============================================================================
# HÌNH 3: HÌNH ĐỀ XUẤT MỚI CẤP NHÓM — TỔNG HỢP ĐỊNH LƯỢNG 4 TẦNG KIẾN TRÚC
# ==============================================================================
def build_figure_3():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15.0, 6.5), dpi=300, sharey=True)

    rows = [
        "Tầng 1 — BtrBlocks (SIGMOD '23)\nQuét S3 Tu vs. Parquet+Zstd (Public BI)",
        "Tầng 2 — Delta Lake (PVLDB '20)\nTPC-DS 1 TB vs. 3rd-Party Spark",
        "Tầng 3 — Photon (SIGMOD '22)\nTB 22 câu TPC-H SF=3000 vs. DBR",
        "Tầng 3 — Photon (SIGMOD '22)\nTPC-DS Q24 (Adaptive Comp.) vs. DBR",
        "Tầng 4 — FeathrPO (PVLDB '23)\nPoint-in-Time Join ML vs. Baseline*",
    ]

    speedups = [
        174.6 / 78.6,  # 2.22x (BtrBlocks Table 5: Tu = 174.6 vs 78.6 GB/s; Abstract: 2.2x)
        1.44 / 0.93,   # 1.55x (Delta Lake Fig. 6: 0.93h vs 1.44h Spark; 4.04x vs Presto)
        4.00,          # 4.00x (Photon Fig. 8: trung bình 4x theo từng truy vấn TPC-H SF=3000)
        118.0 / 76.0,  # 1.55x (Photon Fig. 9: 76s vs 118s trên TPC-DS Q24)
        3.00,          # tới 3.00x (FeathrPO Abstract: mức tối đa trên TPCx-AI & bán lẻ)
    ]
    time_saved_pct = [(1.0 - 1.0 / s) * 100.0 for s in speedups]

    colors = ["#0e7490", "#0284c7", "#0f766e", "#14b8a6", "#7c3aed"]
    hatches = ["", "", "", "", "///"]
    ypos = list(range(len(rows)))

    # --- Panel (A): Hệ số cải thiện so với mốc đối chứng riêng ---
    bars1 = ax1.barh(ypos, speedups, height=0.56, color=colors, edgecolor="#1e293b", linewidth=1.15, zorder=3)
    for bar, h in zip(bars1, hatches):
        if h:
            bar.set_hatch(h)

    ax1.axvline(1.0, color="#64748b", linestyle="--", linewidth=1.4, zorder=2, label="Mốc đối chứng riêng mỗi bài (1,0×)")

    notes_left = [
        "2,22×  (Tc: 3,48×)",
        "1,55×  (4,04× vs. Presto)",
        "4,00×  (tối đa 23× ở Q1)",
        "1,55×  (118 s → 76 s)",
        "tới 3,00×  (cận trên*)",
    ]
    for i, (s, note) in enumerate(zip(speedups, notes_left)):
        ax1.text(s + 0.08, i, note, va="center", ha="left", fontsize=9.1, fontweight="bold", color="#0f172a")

    ax1.set_yticks(ypos)
    ax1.set_yticklabels(rows, fontsize=9.3, fontweight="bold", color="#1e293b")
    ax1.invert_yaxis()
    ax1.set_xlim(0, 6.2)
    ax1.set_xlabel("Hệ số cải thiện so với đối chứng riêng (Lần — cao hơn tốt hơn)", fontsize=9.8, fontweight="bold", color="#0f172a")
    ax1.set_title("(A) Hệ số tăng tốc minh họa theo từng tầng\n[Mỗi tầng so với mốc 1,0× của riêng bài báo gốc]", fontsize=10.8, fontweight="bold", color="#0f172a", pad=10)
    ax1.grid(axis="x", linestyle="--", alpha=0.35, zorder=0)
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)
    # Đặt legend ở góc trên phải (vùng trống hoàn toàn phía trên thanh Photon)
    ax1.legend(loc="upper right", fontsize=8.4, frameon=True, facecolor="white", framealpha=0.95)

    # --- Panel (B): Tỷ lệ giảm thời gian thực thi tương ứng (%) ---
    bars2 = ax2.barh(ypos, time_saved_pct, height=0.56, color=colors, edgecolor="#1e293b", linewidth=1.15, alpha=0.90, zorder=3)
    for bar, h in zip(bars2, hatches):
        if h:
            bar.set_hatch(h)

    notes_right = [
        "−55,0% thời gian quét",
        "−35,4%  (−75,3% vs. Presto)",
        "−75,0% thời gian TB",
        "−35,6% thời gian Q24",
        "tới −66,7%  (cận trên*)",
    ]
    for i, (pct, note) in enumerate(zip(time_saved_pct, notes_right)):
        ax2.text(pct + 1.5, i, note, va="center", ha="left", fontsize=9.1, fontweight="bold", color="#0f172a")

    ax2.set_xlim(0, 118)
    ax2.set_xlabel("Tỷ lệ giảm thời gian thực thi tương ứng: (1 − 1/Speedup) × 100%", fontsize=9.8, fontweight="bold", color="#0f172a")
    ax2.set_title("(B) Mức tiết kiệm thời gian & chi phí điện toán tương ứng\n[Quy đổi trực tiếp từ hệ số cải thiện từng nghiên cứu]", fontsize=10.8, fontweight="bold", color="#0f172a", pad=10)
    ax2.grid(axis="x", linestyle="--", alpha=0.35, zorder=0)
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)

    fig.suptitle(
        "HÌNH ĐỀ XUẤT MỚI (NHÓM): TỔNG HỢP ĐỊNH LƯỢNG HIỆU QUẢ CẢI THIỆN QUA 4 TẦNG KIẾN TRÚC LAKEHOUSE CHO ML",
        fontsize=12.0,
        fontweight="bold",
        color="#1e3a8a",
        y=0.985,
    )
    fig.text(
        0.5,
        -0.015,
        "LƯU Ý PHƯƠNG PHÁP LUẬN: (*) Thanh gạch chéo biểu thị mức tối đa (up to) được tác giả báo cáo, không phải trung bình.\n"
        "Mỗi tầng sử dụng bộ dữ liệu, hạ tầng và mốc đối chứng (1,0×) riêng biệt — KHÔNG so sánh xếp hạng trực tiếp giữa các tầng và KHÔNG cộng/nhân thành hệ số đầu-cuối.",
        ha="center",
        va="top",
        fontsize=8.6,
        color="#334155",
        bbox=dict(boxstyle="round,pad=0.45", facecolor="#f8fafc", edgecolor="#94a3b8", lw=1.0),
    )

    plt.tight_layout(rect=[0, 0.05, 1, 0.935])
    save_figure(fig, "TV3_Hinh3_TongHop_HieuNang")


if __name__ == "__main__":
    build_figure_1()
    build_figure_2()
    build_figure_3()
