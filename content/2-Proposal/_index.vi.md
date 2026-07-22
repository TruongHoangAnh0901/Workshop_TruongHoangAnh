---
title: "Proposal"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 2. </b> "
---

<center>
    <h1>GALAXY BRAIN</h1>
</center>

---

## 1. Tổng quan dự án (Project Overview)
**Galaxy Brain** là một ứng dụng thi trắc nghiệm trực tuyến được phát triển phục vụ cho đồ án môn học. Ứng dụng tập trung vào tính năng nghiệp vụ cốt lõi, đảm bảo hoạt động ổn định cho một quy mô người dùng giới hạn (giảng viên chấm thi và nhóm thử nghiệm). Hệ thống được thiết kế theo hướng "Tối giản" (Minimalist), triển khai hoàn toàn bằng kiến trúc **Serverless** trên AWS với tiêu chí dễ quản lý và tối ưu chi phí tuyệt đối.

### Technology Stack
| Phân loại | Công nghệ sử dụng | Mục đích |
| :--- | :--- | :--- |
| **Frontend** | React, Vite, S3, CloudFront | Giao diện người dùng tốc độ cao, lưu trữ tĩnh toàn cầu. |
| **Compute** | AWS Lambda, API Gateway | Chạy ứng dụng Backend (FastAPI) tự động không cần máy chủ ảo. |
| **Database** | Amazon DynamoDB | Cơ sở dữ liệu NoSQL Serverless tự động mở rộng. |
| **Security** | IAM Role, Secrets Manager, OAC | Cấp quyền chặt chẽ theo đặc quyền tối thiểu, bảo mật S3 và Token. |
| **CI/CD** | GitHub Actions | Tự động hóa quá trình build và deploy. |

---

## 2. Mục tiêu (Objectives)
### Mục tiêu chung (General Objective)
Hoàn thành một đồ án học thuật trọn vẹn từ khâu code Frontend/Backend đến việc đưa sản phẩm lên môi trường Cloud (AWS). Đảm bảo sản phẩm có thể chạy demo mượt mà trước ban giám khảo.

### Mục tiêu cụ thể (Specific Objectives)
- Triển khai thành công ứng dụng trên AWS với kiến trúc **Serverless** hiện đại.
- Tận dụng tối đa các dịch vụ Free Tier của AWS (như Lambda, DynamoDB) để đưa chi phí vận hành về gần mức $0.
- Hoàn thành đầy đủ bộ tài liệu hướng dẫn triển khai (Walkthrough) mạch lạc và dễ thực hành lại.

---

## 3. Bài toán & Đối tượng (Problem Statement)
### Problem Statement
Đối với các dự án đồ án học thuật, sinh viên thường mất quá nhiều thời gian vào việc cấu hình hạ tầng AWS phức tạp (như VPC, NAT Gateway, Load Balancer) dẫn đến thiếu thời gian hoàn thiện tính năng, hoặc bị trừ điểm do hệ thống lỗi khi demo. Galaxy Brain giải quyết vấn đề này bằng một **Kiến trúc Serverless Cloud-Native**, loại bỏ hoàn toàn việc quản trị máy chủ truyền thống để tập trung 100% vào việc "Chạy được và chạy đúng".

### Target Audience
- Giảng viên chấm thi, hội đồng đánh giá đồ án.
- Sinh viên trong nhóm thử nghiệm ứng dụng.

---

## 4. Kiến trúc hệ thống (System Architecture)
Kiến trúc bên dưới mô tả luồng dữ liệu (Data Flow) Serverless của Galaxy Brain.

![System Architecture](/images/architecture.png)

---

## 5. Tiến độ triển khai (Timeline)
| Giai đoạn | Thời gian | Nội dung công việc |
| :---: | :---: | :--- |
| **Phase 1** | Tuần 1 - 3 | Phân tích yêu cầu, thiết kế giao diện, khởi tạo DynamoDB Table. |
| **Phase 2** | Tuần 4 - 6 | Viết code Backend (FastAPI) và Frontend (React). |
| **Phase 3** | Tuần 7 - 9 | Triển khai Backend lên AWS Lambda qua API Gateway. |
| **Phase 4** | Tuần 10 - 12| Đưa Frontend lên S3/CloudFront, viết báo cáo tổng kết đồ án. |

---

## 6. Ngân sách (Budget)
Bảng ước tính chi phí hạ tầng AWS hàng tháng (AWS Monthly Cost Estimated) - Tối ưu hóa cho Sinh viên:

| Dịch vụ AWS | Loại cấu hình | Chi phí ước tính/Tháng |
| :--- | :--- | :---: |
| **AWS Lambda & API Gateway** | Free Tier (Hàng triệu request miễn phí) | $0.00 |
| **Amazon DynamoDB** | Free Tier (25GB lưu trữ miễn phí) | $0.00 |
| **Amazon S3 & CloudFront**| Lưu trữ tĩnh & Băng thông ít | ~$1.00 |
| **VPC & Mạng** | Kiến trúc Serverless không dùng NAT Gateway | $0.00 |
| **Tổng cộng (Summary)** | | **~$1.00** |

---

## 7. Đánh giá rủi ro (Risk Assessment)
| Rủi ro (Risk) | Mức độ | Kế hoạch giảm thiểu (Mitigation Plan) |
| :--- | :---: | :--- |
| **Độ trễ khởi động lạnh (Cold Start)** | Trung bình | FastAPI chạy trên Lambda có thể chậm ở request đầu tiên. Khắc phục bằng cách dùng cấu hình RAM phù hợp (1024MB) để tăng tốc độ. |
| **Quá tải khi có nhiều người dùng** | Thấp | AWS Lambda và DynamoDB tự động scale vô hạn, hoàn toàn không sợ sập Server. |
| **Phát sinh chi phí do gọi API lặp lại**| Thấp | Cài đặt cấu hình AWS Budgets cảnh báo qua Email nếu chi phí vượt quá $5. |
