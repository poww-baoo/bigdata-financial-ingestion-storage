---
experiment_id: "EXP-001"
date: 2026-11-10
author: "hungmg"
tags:
  - experiment-log
  - baseline
status: "Completed"
---

# 🧪 Thử Nghiệm Baseline #001: Đánh Giá Hiệu Năng Ban Đầu

## 1. Mục Đích Thí Nghiệm
Thiết lập ngưỡng chuẩn (baseline benchmark) để làm mốc so sánh cho tất cả các cải tiến và phương pháp mới sau này.

---

## 2. Thiết Lập Môi Trường (Setup & Environment)
- **Phần cứng:** GPU / CPU info
- **Môi trường:** Python 3.10+, PyTorch / TensorFlow
- **Random Seed:** 42 (đảm bảo tính tái lập - reproducibility)
- **Tham số (Hyperparameters):**
  - Batch size: 64
  - Learning rate: $1e-3$ (Adam)
  - Epochs: 50

---

## 3. Dữ Liệu Sử Dụng (Dataset)
- Xem thông tin chi tiết tại: [[03 - Phương pháp & Thí nghiệm (Methodology & Experiments)/Dữ liệu & Benchmarks (Datasets & Benchmarks)/Danh sách Datasets|Danh mục Datasets]]
- Tỉ lệ phân chia Train / Val / Test: 70% / 15% / 15%

---

## 4. Kết Quả Thu Được (Results)
| Metric | Giá trị Baseline | Ghi chú |
| :--- | :--- | :--- |
| **Accuracy** | 82.4% | Bão hòa ở epoch 35 |
| **F1-Score (Macro)** | 0.812 | Lớp thiểu số bị dự đoán sai nhiều |
| **Inference Time** | 12.5 ms / sample | Đo trên GPU |

---

## 5. Nhận Xét & Bước Tiếp Theo (Insights & Next Steps)
- Mô hình baseline có hiện tượng mất cân bằng giữa các lớp.
- Thử nghiệm tiếp theo (#002): Áp dụng Data Augmentation hoặc hàm Focal Loss để khắc phục.
