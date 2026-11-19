---
title: "Deep Residual Learning for Image Recognition"
authors: "Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun"
year: 2016
conference: "CVPR"
doi: "10.1109/CVPR.2016.90"
tags:
  - deep-learning
  - computer-vision
  - residual-networks
  - paper-summary
rating: ⭐⭐⭐⭐⭐
---

# Deep Residual Learning for Image Recognition (ResNet)

## 1. Tóm Tắt Trong 1 Câu (One-Sentence Takeaway)
Đề xuất kiến trúc kết nối tắt (residual shortcut / skip connection) giúp giải quyết hiện tượng suy giảm độ chính xác (degradation problem), cho phép huấn luyện mạng nơ-ron cực sâu (lên đến 152 lớp) đạt giải nhất ImageNet 2015.

---

## 2. Vấn Đề Nghiên Cứu (Research Problem)
- Khi tăng độ sâu của mạng nơ-ron, độ chính xác bị bão hòa rồi giảm sút nhanh chóng (**degradation problem**).
- Hiện tượng này không phải do overfitting (vì training error cũng tăng theo độ sâu), mà do khó khăn trong việc tối ưu hóa (gradient vanishing / exploding).

---

## 3. Đóng Góp Cốt Lõi (Key Contribution / Solution)
- Thay vì để các lớp học trực tiếp hàm ánh xạ mục tiêu $H(x)$, tác giả cho các lớp học ánh xạ phần dư $F(x) := H(x) - x$.
- Hàm mục tiêu trở thành $H(x) = F(x) + x$, thực hiện bằng cách thêm **identity shortcut connection**.
- Nếu ánh xạ đồng nhất (identity mapping) là tối ưu, bộ tối ưu chỉ cần đưa trọng số $F(x)$ về 0, dễ dàng hơn nhiều so với việc học ánh xạ đồng nhất từ đầu.

```
      x
      │ ╲
      │  [Weight Layer]
      │        │
      │      [ReLU]
      │        │
      │  [Weight Layer]
      │        │
      │ ╱    F(x)
      + ◀──────┘
      │
    [ReLU]
      │
     F(x) + x
```

---

## 4. Kết Quả Thực Nghiệm (Key Results)
- ResNet-152 sâu gấp 8 lần VGG nhưng vẫn có độ phức tạp tính toán thấp hơn.
- Đạt top-5 error **3.57%** trên tập dữ liệu ImageNet, đoạt giải nhất cuộc thi ILSVRC 2015.
- Khả năng tổng quát hóa xuất sắc trên các tác vụ COCO object detection và segmentation.

---

## 5. Điểm Mạnh & Hạn Chế (Strengths & Limitations)
- **Điểm mạnh:**
  - Ý tưởng thanh lịch, đơn giản, dễ cài đặt.
  - Giải quyết triệt để rào cản về độ sâu của mạng nơ-ron.
- **Hạn chế:**
  - Tiêu tốn bộ nhớ VRAM khi lưu activation map cho các kết nối tắt.

---

## 6. Liên Kết & Ứng Dụng Vào Đề Tài Của Mình
- Có thể áp dụng tư tưởng skip-connection vào kiến trúc mô hình của mình trong bài toán [[Trang chủ Nghiên cứu]].
- Xem thêm: [[02 - Ý tưởng & Khái niệm (Concepts & Notes)/Ghi chú khái niệm (Permanent Notes)/Khái niệm - Gradient Descent|Khái niệm Gradient Descent & Vấn đề suy hao gradient]].
