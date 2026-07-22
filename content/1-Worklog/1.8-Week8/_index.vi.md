---
title: "Worklog Tuần 8"
date: 2024-01-01
weight: 8
chapter: false
pre: " <b> 1.8. </b> "
---

### Mục tiêu tuần 8:

* Tăng cường bảo vệ ứng dụng ở tầng Application (Lớp 7 OSI).
* Tìm hiểu và cấu hình Tường lửa ứng dụng web AWS WAF.
* Ngăn chặn các hình thức tấn công mạng phổ biến như SQL Injection, XSS.

---

### Các công việc triển khai:

| Ngày (Day) | Công việc (Task) | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| ---------- | ---------------- | ------------ | --------------- | -------------- |
| Thứ 2 | Tìm hiểu các khái niệm và cơ chế hoạt động của **Tường lửa ứng dụng web (AWS WAF)**. | 08/06/2026 | 08/06/2026 | |
| Thứ 3 | Cài đặt các luật (rules) cho AWS WAF để bảo vệ website khỏi **tấn công mạng và SQL injection**. | 09/06/2026 | 09/06/2026 | |
| Thứ 5 | Giám sát các request bị chặn và tinh chỉnh **các rule bảo mật WAF** để tối ưu hóa. | 11/06/2026 | 11/06/2026 | |
| Thứ 7 | Tham gia sự kiện First Cloud Security Journey của công ty. | 13/06/2026 | 13/06/2026 | |

---

### Kết quả đạt được:

* Dự án Quiz App đã được trang bị lớp khiên bảo vệ vững chắc với **AWS WAF**:
  * Đính kèm thành công Web ACL (WAF) vào bản phân phối **CloudFront** để bảo vệ Frontend.
  * Kích hoạt bộ quy tắc bảo mật do AWS quản lý (AWS Managed Rules).
* Ngăn chặn tự động các luồng truy cập độc hại:
  * Hệ thống tự động chặn các cú pháp SQL Injection và Cross-Site Scripting (XSS).
  * Giảm thiểu nguy cơ bị tấn công rò rỉ dữ liệu đề thi và điểm số của học sinh.
* Biết cách đọc Logs và biểu đồ request bị WAF chặn trên bảng điều khiển.
