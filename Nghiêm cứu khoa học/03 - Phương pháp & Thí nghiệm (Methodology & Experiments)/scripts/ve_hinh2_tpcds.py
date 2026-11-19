"""
MÃ NGUỒN TÁI TẠO FIGURE 6 TỪ BÀI BÁO DELTA LAKE (VLDB 2020)
Học phần: Phương pháp Nghiên cứu Khoa học trong CNTT
Công cụ: Python 3 + Matplotlib
"""

import matplotlib.pyplot as plt
import os

systems = [
    'Databricks\nDelta Lake',
    'Databricks\nParquet',
    '3rd-Party Spark\nParquet',
    '3rd-Party Presto\nParquet'
]
durations = [0.93, 0.99, 1.44, 3.76]  # Thoi gian chay (gio)
colors = ['#1f77b4', '#4ba3e3', '#ff7f0e', '#d62728']
hatches = ['', '', '..', '//']

fig, ax = plt.subplots(figsize=(9, 5.8), dpi=300)

bars = ax.bar(systems, durations, color=colors, edgecolor='black', linewidth=1.2, width=0.52, hatch=hatches, zorder=3)

for bar, val in zip(bars, durations):
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2.0, yval + 0.08, f'{val:.2f} h', 
            ha='center', va='bottom', fontsize=11, fontweight='bold', color='#111111')

ax.set_ylabel('Thời gian hoàn thành TPC-DS Power Test (giờ)\n[TPC-DS Power Test Duration (hours)]', 
              fontsize=11.5, fontweight='bold', labelpad=12)
ax.set_title('Hình tái tạo Figure 6: Thời gian thực thi TPC-DS Power Test (Quy mô 1 TB)\nSo sánh giữa Databricks Runtime (Delta Lake/Parquet) và dịch vụ Cloud bên thứ ba', 
             fontsize=12, fontweight='bold', pad=16)

ax.set_ylim(0, 4.3)
ax.grid(axis='y', linestyle='--', alpha=0.6, zorder=0)

ax.annotate('Nhanh hơn 4.04×\n(so với Presto)',
            xy=(0, 0.93), xytext=(0.35, 2.5),
            arrowprops=dict(facecolor='#1f77b4', edgecolor='#1f77b4', shrink=0.08, width=1.5, headwidth=7),
            fontsize=10.5, fontweight='bold', color='#0f4c81',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#eaf2fa', edgecolor='#1f77b4', alpha=0.95))

ax.annotate('Nhanh hơn 1.55×\n(so với Spark khác)',
            xy=(0, 0.93), xytext=(1.25, 2.0),
            arrowprops=dict(facecolor='#ff7f0e', edgecolor='#ff7f0e', shrink=0.08, width=1.5, headwidth=7),
            fontsize=10.5, fontweight='bold', color='#b35400',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#fff4eb', edgecolor='#ff7f0e', alpha=0.95))

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(1.1)
ax.spines['bottom'].set_linewidth(1.1)
ax.tick_params(axis='both', which='major', labelsize=11)

plt.tight_layout()
out_file = '../../99 - Đính kèm (Attachments)/Hinh2_TaiTao_TPCDS_PowerTest.png'
plt.savefig(out_file, dpi=300)
print(f"Luu thanh cong tai: {out_file}")
