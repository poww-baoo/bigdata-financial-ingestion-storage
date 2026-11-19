---
title: "Gradient Descent (Hạ Gradient)"
tags:
  - optimization
  - machine-learning
  - mathematics
created: 2026-11-10
---

# Khái Niệm: Thuật Toán Hạ Gradient (Gradient Descent)

## 1. Định Nghĩa Cốt Lõi (Core Definition)
Hạ gradient là thuật toán tối ưu hóa bậc nhất lặp (first-order iterative optimization algorithm) dùng để tìm cực tiểu địa phương của hàm mất mát khả vi (differentiable loss function).

Công thức cập nhật tham số cơ bản:
$$\\theta_{t+1} = \\theta_t - \\eta \\cdot \\nabla L(\\theta_t)$$

Trong đó:
- $\\theta$: Vector trọng số (parameters/weights).
- $\\eta$: Tốc độ học (learning rate).
- $\\nabla L(\\theta)$: Gradient của hàm mất mát theo tham số.

---

## 2. Các Biến Thể Chính (Variants)
1. **Batch Gradient Descent (BGD):** Tính đạo hàm trên toàn bộ tập dữ liệu huấn luyện. Chính xác nhưng rất chậm với dữ liệu lớn.
2. **Stochastic Gradient Descent (SGD):** Cập nhật trọng số trên từng mẫu dữ liệu đơn lẻ. Nhanh, có tính ngẫu nhiên giúp thoát khỏi cực tiểu địa phương nhưng dao động mạnh.
3. **Mini-batch Gradient Descent:** Cân bằng giữa BGD và SGD bằng cách tính trên từng batch nhỏ (ví dụ 32, 64, 128 mẫu).
4. **Adaptive Optimizers (Adam, RMSprop, AdamW):** Tự điều chỉnh tốc độ học theo từng tham số dựa trên moment bậc một và bậc hai của gradient.

---

## 3. Liên Kết Liên Quan (Related Links)
- Ứng dụng trong việc huấn luyện mô hình sâu: [[01 - Tổng quan tài liệu (Literature Review)/Bài báo đã đọc (Papers)/Paper Mẫu - Deep Residual Learning for Image Recognition|Paper ResNet]]
- Nhật ký thực nghiệm kiểm tra learning rate: [[03 - Phương pháp & Thí nghiệm (Methodology & Experiments)/Nhật ký thực nghiệm (Lab Logbook)/Logbook - Thử nghiệm Baseline #001|Thử nghiệm Baseline #001]]
