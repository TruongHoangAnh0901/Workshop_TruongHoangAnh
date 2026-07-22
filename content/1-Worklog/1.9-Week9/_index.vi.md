---
title: "Worklog Tuần 9"
date: 2024-01-01
weight: 9
chapter: false
pre: " <b> 1.9. </b> "
---

### Mục tiêu tuần 9:

* Nghiên cứu về khả năng quan sát (Observability) và giám sát hệ thống trên AWS.
* Sử dụng Amazon CloudWatch để thu thập Logs và Metrics.
* Tự động hóa cảnh báo sự cố thông qua CloudWatch Alarms.

---

### Các công việc triển khai:

| Ngày (Day) | Công việc (Task) | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| ---------- | ---------------- | ------------ | --------------- | -------------- |
| Thứ 2 | Khám phá dịch vụ giám sát và khả năng quan sát hệ thống **Amazon CloudWatch**. | 15/06/2026 | 15/06/2026 | |
| Thứ 4 | Theo dõi các metrics hệ thống và xem **log lỗi (error logs)** của AWS Lambda và API Gateway. | 17/06/2026 | 17/06/2026 | |
| Thứ 6 | Tạo **CloudWatch Dashboards** trực quan và thiết lập Alarm để cảnh báo khi có sự cố hệ thống. | 19/06/2026 | 19/06/2026 | |

---

### Kết quả đạt được:

* Làm chủ được công cụ giám sát toàn diện **Amazon CloudWatch**:
  * Thu thập và phân tích thành công Log Groups của tất cả các hàm **AWS Lambda**.
  * Truy vết dễ dàng các lỗi (bug) khi hệ thống Backend trả về mã lỗi 500.
* Thiết lập thành công trung tâm điều khiển (Dashboard) cho dự án:
  * Vẽ biểu đồ theo dõi số lượng Request, số lỗi và thời gian phản hồi (Latency) của API Gateway.
  * Cấu hình **CloudWatch Alarms** tự động gửi email cảnh báo mỗi khi số lượng lỗi vượt ngưỡng cho phép.
