"""
MÃ NGUỒN XÂY DỰNG HÌNH ĐỀ XUẤT MỚI (TỶ LỆ TĂNG TỐC & TIẾT KIỆM THỜI GIAN)
Học phần: Phương pháp Nghiên cứu Khoa học trong CNTT
Công cụ: Python 3 + Matplotlib + Numpy
"""

import matplotlib.pyplot as plt
import os

systems = [
    '3rd-Party Presto\n(Parquet) [Baseline]',
    '3rd-Party Spark\n(Parquet)',
    'Databricks Spark\n(Parquet thuần)',
    'Databricks Runtime\n(Delta Lake)'
]
durations = [3.76, 1.44, 0.99, 0.93]
presto_baseline = 3.76

speedup = [presto_baseline / d for d in durations]
time_saved = [((presto_baseline - d) / presto_baseline) * 100 for d in durations]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.5, 6.0), dpi=300)
colors = ['#94a3b8', '#f97316', '#38bdf8', '#0284c7']

# (A) Speedup
bars1 = ax1.bar(systems, speedup, color=colors, edgecolor='#1e293b', linewidth=1.2, width=0.52)
ax1.set_title('(A) Hệ số tăng tốc hiệu năng (Speedup Factor)\n[So với mốc chuẩn 3rd-Party Presto = 1.0×]', 
              fontsize=11.5, fontweight='bold', color='#0f172a', pad=12)
ax1.set_ylabel('Hệ số tăng tốc (Lần - Càng cao càng tốt)', fontsize=11, fontweight='bold')
ax1.set_ylim(0, 4.9)
ax1.grid(axis='y', linestyle='--', alpha=0.5)

for bar, val in zip(bars1, speedup):
    h = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2.0, h + 0.1, f'{val:.2f}×', 
             ha='center', va='bottom', fontsize=11.5, fontweight='bold', color='#0f172a')

ax1.axhline(1.0, color='#64748b', linestyle=':', linewidth=1.5, label='Mốc chuẩn Presto (1.0×)')
ax1.legend(loc='upper left', fontsize=10.5)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.tick_params(axis='both', which='major', labelsize=10.5)

# (B) % Time Saved
bars2 = ax2.bar(systems, time_saved, color=colors, edgecolor='#1e293b', linewidth=1.2, width=0.52)
ax2.set_title('(B) Tỷ lệ thời gian truy vấn tiết kiệm được (% Time Saved)\n[Rút ngắn thời gian chờ đợi & Chi phí điện toán đám mây]', 
              fontsize=11.5, fontweight='bold', color='#0f172a', pad=12)
ax2.set_ylabel('Tỷ lệ thời gian tiết kiệm (%)', fontsize=11, fontweight='bold')
ax2.set_ylim(0, 102)
ax2.grid(axis='y', linestyle='--', alpha=0.5)

for bar, val in zip(bars2, time_saved):
    h = bar.get_height()
    if val == 0:
        ax2.text(bar.get_x() + bar.get_width()/2.0, 2.5, '0.0%\n(Mốc chuẩn)', 
                 ha='center', va='bottom', fontsize=10, fontweight='bold', color='#475569')
    else:
        ax2.text(bar.get_x() + bar.get_width()/2.0, h + 2.0, f'-{val:.1f}%', 
                 ha='center', va='bottom', fontsize=11.5, fontweight='bold', color='#0369a1')

ax2.annotate('Rút ngắn 75.3% thời gian\n(Nhanh hơn gấp 4 lần)',
            xy=(3, 78.5), xytext=(1.45, 87),
            arrowprops=dict(facecolor='#0284c7', edgecolor='#0284c7', shrink=0.08, width=1.5, headwidth=6.5),
            fontsize=10.5, fontweight='bold', color='#0284c7',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#e0f2fe', edgecolor='#0284c7', alpha=0.95))

ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.tick_params(axis='both', which='major', labelsize=10.5)

plt.suptitle('HÌNH ĐỀ XUẤT MỚI: PHÂN TÍCH TỶ LỆ TĂNG TỐC VÀ HIỆU QUẢ TIẾT KIỆM THỜI GIAN TRUY VẤN (TPC-DS 1 TB)', 
             fontsize=12.5, fontweight='bold', color='#1e3a8a', y=0.99)

plt.tight_layout()
out_file = '../../99 - Đính kèm (Attachments)/Hinh3_DeXuatMoi_HeSoTangToc.png'
plt.savefig(out_file, dpi=300, bbox_inches='tight')
print(f"Luu thanh cong tai: {out_file}")
