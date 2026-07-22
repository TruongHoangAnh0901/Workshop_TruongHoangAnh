---
title: "Worklog Tuần 6"
date: 2024-01-01
weight: 6
chapter: false
pre: " <b> 1.6. </b> "
---

### Mục tiêu tuần 6:

* Triển khai giao diện người dùng (Frontend) lên Cloud.
* Sử dụng Content Delivery Network (CDN) để tăng tốc độ tải trang toàn cầu.
* Thiết lập kết nối HTTPS an toàn thông qua chứng chỉ SSL/TLS miễn phí của AWS.

---

### Các công việc triển khai:

| Ngày (Day) | Công việc (Task) | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| ---------- | ---------------- | ------------ | --------------- | -------------- |
| Thứ 2 | Build source code ReactJS và đưa **giao diện Website (Frontend)** lên lưu trữ trực tiếp trên Amazon S3. | 25/05/2026 | 25/05/2026 | |
| Thứ 3 | Cài đặt **Amazon CloudFront** để phân phối website trên toàn cầu và giảm độ trễ cho người dùng. | 26/05/2026 | 26/05/2026 | |
| Thứ 5 | Yêu cầu chứng chỉ SSL thông qua **AWS Certificate Manager (ACM)** để thiết lập kết nối HTTPS an toàn. | 28/05/2026 | 28/05/2026 | |
| Thứ 6 | Cấu hình **Origin Access Control (OAC)** để ngăn chặn truy cập trực tiếp vào S3 bucket. | 29/05/2026 | 29/05/2026 | |

---

### Kết quả đạt được:

* Dự án Quiz App đã hoàn thiện phần Giao diện Frontend và sẵn sàng tiếp cận người dùng:
  * Build và host thành công code ReactJS lên **Amazon S3**.
  * Phân phối nội dung tĩnh siêu tốc nhờ mạng lưới Edge Locations của **Amazon CloudFront**.
* Đảm bảo tuyệt đối an toàn bảo mật cho người dùng truy cập:
  * Ứng dụng đã được cấp chứng chỉ SSL hợp lệ qua **AWS ACM** và chạy trên giao thức HTTPS.
  * Cấu hình **OAC (Origin Access Control)** thành công, ép buộc mọi truy cập phải đi qua CDN (CloudFront) thay vì truy cập trực tiếp vào nguồn S3.
