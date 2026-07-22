---
title: "Worklog Tuần 11"
date: 2024-01-01
weight: 11
chapter: false
pre: " <b> 1.11. </b> "
---

### Mục tiêu tuần 11:

* Tìm hiểu về văn hóa DevOps và phương pháp Tự động hóa luồng triển khai phần mềm.
* Xây dựng luồng CI/CD pipelines trên AWS (CodePipeline, CodeBuild).
* Hoàn thành toàn bộ kiến trúc và Đưa dự án Workshop ra công chúng (Go Live).

---

### Các công việc triển khai:

| Ngày (Day) | Công việc (Task) | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| ---------- | ---------------- | ------------ | --------------- | -------------- |
| Thứ 2 | Tìm hiểu các nguyên lý của luồng **Tích hợp liên tục và Triển khai liên tục (CI/CD)**. | 29/06/2026 | 29/06/2026 | |
| Thứ 3 | Tự động hóa quy trình triển khai bằng cách sử dụng **AWS CodePipeline** và **AWS CodeBuild**. | 30/06/2026 | 30/06/2026 | |
| Thứ 4 | Áp dụng CI/CD pipelines để đạt được tính năng cập nhật website **Zero-Downtime (không gián đoạn)**. | 01/07/2026 | 01/07/2026 | |
| Thứ 5 | Kiểm tra tự động hóa bằng cách đẩy source code mới lên **kho lưu trữ mã nguồn (repository)**. | 02/07/2026 | 02/07/2026 | |
| Thứ 6 | Hoàn thiện toàn bộ các chủ đề Workshop và **Triển khai thành công hệ thống Quiz App** ra Internet. | 03/07/2026 | 03/07/2026 | |

---

### Kết quả đạt được:

* Thiết lập thành công quy trình Tự động hóa triển khai (CI/CD) cho mã nguồn Frontend:
  * Khởi tạo **AWS CodePipeline** tự động theo dõi các thay đổi trên Github/CodeCommit.
  * Sử dụng **AWS CodeBuild** để tự động chạy lệnh `npm build` và đồng bộ file lên Amazon S3.
* Đạt được mục tiêu tự động hóa hoàn toàn:
  * Mọi thay đổi code của Developer đều được tự động đưa lên website trong vài phút mà không cần thao tác tay thủ công.
  * Đảm bảo website cập nhật tính năng mới với tỷ lệ gián đoạn bằng 0 (Zero-Downtime).
* Dự án **Quiz App** chính thức đi vào hoạt động ổn định trên Internet.
