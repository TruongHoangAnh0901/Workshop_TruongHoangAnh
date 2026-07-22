---
title: "Worklog Tuần 7"
date: 2024-01-01
weight: 7
chapter: false
pre: " <b> 1.7. </b> "
---

### Mục tiêu tuần 7:

* Tìm hiểu mô hình kiến trúc bất đồng bộ (Asynchronous Architecture).
* Nghiên cứu dịch vụ hàng đợi tin nhắn Amazon SQS.
* Thực hành kết nối SQS với Lambda để xử lý khối lượng lớn công việc ngầm.

---

### Các công việc triển khai:

| Ngày (Day) | Công việc (Task) | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| ---------- | ---------------- | ------------ | --------------- | -------------- |
| Thứ 2 | Tìm hiểu cách xử lý **các công việc chạy ngầm** để website không bị đơ khi có lượng lớn người truy cập. | 01/06/2026 | 01/06/2026 | |
| Thứ 3 | Nắm bắt khái niệm message queueing và thiết lập hàng đợi **Amazon SQS**. | 02/06/2026 | 02/06/2026 | |
| Thứ 4 | Thực hành tích hợp **SQS với Lambda** để xử lý các tin nhắn một cách bất đồng bộ. | 03/06/2026 | 03/06/2026 | |
| Thứ 5 | Nghiên cứu sâu hơn về **Lambda triggers** và kiến trúc hướng sự kiện (event-driven) trong AWS. | 04/06/2026 | 04/06/2026 | |
| Thứ 6 | Triển khai tính năng xử lý ngầm cho **hệ thống chấm điểm** của dự án Quiz App. | 05/06/2026 | 05/06/2026 | |

---

### Kết quả đạt được:

* Nâng cấp hệ thống Quiz App lên kiến trúc Event-Driven tiên tiến:
  * Tích hợp thành công **Amazon SQS** làm bộ đệm (buffer) cho các yêu cầu gửi về từ người dùng.
  * Sử dụng SQS làm Trigger kích hoạt **AWS Lambda** xử lý chấm điểm ngầm một cách mượt mà.
* Hệ thống hiện tại đã có thể chịu tải tốt hơn (Decoupled architecture):
  * Website không còn bị treo hoặc timeout khi có hàng ngàn học sinh nộp bài thi cùng một lúc.
  * Nắm vững các khái niệm Visibility Timeout và Dead Letter Queue trong xử lý lỗi.
