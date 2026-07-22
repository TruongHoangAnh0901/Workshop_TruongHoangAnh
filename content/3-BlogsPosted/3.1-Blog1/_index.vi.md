---
title: "Blog 1"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 3.1. </b> "
---

# KHÁM PHÁ CÁC MÔ HÌNH SERVERLESS CHO AMAZON DYNAMODB

Amazon DynamoDB là một dịch vụ cơ sở dữ liệu NoSQL được quản lý hoàn toàn, cung cấp hiệu suất nhất quán ở mức mili-giây tại bất kỳ quy mô nào. Khi kết hợp với các dịch vụ Serverless như AWS Lambda và Amazon API Gateway, DynamoDB trở thành một thành phần cốt lõi cho việc xây dựng các ứng dụng web và di động hiện đại, linh hoạt và có khả năng mở rộng tự động.

Trong bài viết chính thức này từ AWS Compute Blog, tác giả đã đi sâu vào việc phân tích các mô hình (patterns) kiến trúc Serverless phổ biến và hiệu quả nhất khi làm việc với DynamoDB:

1. **Kết nối trực tiếp API Gateway tới DynamoDB:** 
Đây là mô hình lý tưởng cho các thao tác CRUD cơ bản. Thay vì phải viết và duy trì một hàm Lambda chỉ để chuyển tiếp dữ liệu (như một proxy), bạn có thể cấu hình API Gateway để tương tác trực tiếp với DynamoDB thông qua VTL (Velocity Template Language). Điều này không chỉ giúp giảm độ trễ (latency) do loại bỏ hoàn toàn thời gian khởi động (cold start) của Lambda, mà còn tiết kiệm được chi phí điện toán đáng kể.

2. **AWS Lambda như một lớp xử lý logic nghiệp vụ (Business Logic Layer):**
Đối với các hệ thống phức tạp yêu cầu kiểm tra xác thực, tổng hợp dữ liệu từ nhiều nguồn, hoặc tính toán phức tạp trước khi lưu trữ, AWS Lambda đóng vai trò trung tâm. Lambda sẽ nhận request, thực thi các nghiệp vụ kinh doanh, sau đó mới tiến hành đọc hoặc ghi vào DynamoDB. Mô hình này mang lại sự linh hoạt tối đa cho các nhà phát triển.

3. **Xử lý bất đồng bộ với DynamoDB Streams:**
DynamoDB Streams cho phép bạn nắm bắt các sự kiện thay đổi dữ liệu (Insert, Update, Delete) theo thời gian thực. Bằng cách kích hoạt một hàm Lambda mỗi khi có sự kiện từ Stream, bạn có thể dễ dàng xây dựng các kiến trúc Event-Driven. Ví dụ: tự động gửi email xác nhận khi một bản ghi đơn hàng mới được tạo, hoặc cập nhật bộ nhớ cache phân tán một cách đồng bộ.

Việc hiểu rõ và áp dụng đúng đắn các mô hình kiến trúc này không chỉ giúp tối ưu hóa hiệu suất, mà còn là chìa khóa để giảm độ trễ và tiết kiệm chi phí vận hành cho các ứng dụng Serverless quy mô lớn.

![DynamoDB Pattern](/images/dynamodb-pattern.png)

### Link bài viết gốc
**[Đọc toàn bộ bài viết trên AWS Compute Blog](https://aws.amazon.com/blogs/compute/exploring-serverless-patterns-for-amazon-dynamodb/)**