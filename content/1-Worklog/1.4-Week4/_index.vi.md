---
title: "Worklog Tuần 4"
date: 2024-01-01
weight: 4
chapter: false
pre: " <b> 1.4. </b> "
---

### Mục tiêu tuần 4:

* Thiết lập hạ tầng Cơ sở dữ liệu NoSQL với Amazon DynamoDB.
* Phát triển mã nguồn xử lý logic Backend bằng ngôn ngữ Python.
* Triển khai kiến trúc Serverless (không máy chủ) sử dụng AWS Lambda và Amazon API Gateway.

---

### Các công việc triển khai:

| Ngày (Day) | Công việc (Task) | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| ---------- | ---------------- | ------------ | --------------- | -------------- |
| Thứ 2 | Khởi tạo cơ sở dữ liệu **DynamoDB (NoSQL)** để lưu trữ thông tin người dùng, đề thi và điểm số. | 11/05/2026 | 11/05/2026 | |
| Thứ 3 | Viết code xử lý logic **Serverless Backend** bằng ngôn ngữ Python và thư viện Boto3. | 12/05/2026 | 12/05/2026 | |
| Thứ 5 | Đưa các hàm xử lý Backend lên **AWS Lambda** để hệ thống chạy mà không cần quản lý máy chủ. | 14/05/2026 | 14/05/2026 | |
| Thứ 6 | Cấu hình **API Gateway** để định tuyến các HTTP request từ phía người dùng vào các hàm Lambda. | 15/05/2026 | 15/05/2026 | |

---

### Kết quả đạt được:

* Triển khai thành công hạ tầng **Serverless Backend** cho toàn bộ dự án Quiz App:
  * Khởi tạo và thiết lập quyền truy cập an toàn cho các bảng dữ liệu trên **Amazon DynamoDB**.
  * Viết và debug thành công các hàm xử lý logic Backend bằng **Python (Boto3)**.
  * Đóng gói và upload source code lên **AWS Lambda**, giảm thiểu chi phí duy trì máy chủ 24/7.
  * Tích hợp thành công **Amazon API Gateway** để tạo RESTful APIs kết nối an toàn với Lambda.
* Đảm bảo Backend xử lý mượt mà các thao tác CRUD (Tạo, Đọc, Sửa, Xóa) dữ liệu người dùng và đề thi.
