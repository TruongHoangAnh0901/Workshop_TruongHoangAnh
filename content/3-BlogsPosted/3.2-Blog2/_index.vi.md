---
title: "Blog 2"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 3.2. </b> "
---

# AMAZON CLOUDFRONT GIỚI THIỆU TÍNH NĂNG ORIGIN ACCESS CONTROL (OAC)

Việc bảo mật các nguồn lưu trữ (origins) của Amazon CloudFront, đặc biệt là Amazon S3 buckets, luôn là một yêu cầu bảo mật ưu tiên hàng đầu đối với mọi hệ thống trên AWS. Trước đây, AWS cung cấp một giải pháp mang tên Origin Access Identity (OAI) nhằm giới hạn quyền truy cập S3 chỉ cho phép thông qua CloudFront, ngăn chặn việc truy cập trực tiếp từ Internet. Tuy nhiên, theo thời gian, OAI đã bộc lộ một số hạn chế nhất định về mặt bảo mật nâng cao và khả năng hỗ trợ tính năng mới.

Để khắc phục triệt để những hạn chế này, AWS đã chính thức ra mắt **Origin Access Control (OAC)**. Bài blog này cung cấp một cái nhìn chuyên sâu và giải thích chi tiết tại sao OAC lại trở thành tiêu chuẩn bảo mật mới, cũng như những cải tiến vượt trội mà nó mang lại:

1.  **Bảo mật nâng cao và chống lại lỗ hổng Confused Deputy:** 
OAC sử dụng cơ chế xác thực IAM mạnh mẽ với các thông tin đăng nhập ngắn hạn (short-term credentials). Hơn thế nữa, nó yêu cầu chỉ định rõ ràng Amazon Resource Name (ARN) của CloudFront distribution cụ thể được phép truy cập. Điều này giúp ngăn chặn hoàn toàn các cuộc tấn công leo thang đặc quyền như "confused deputy", đảm bảo S3 bucket của bạn không bị truy cập trái phép bởi một CloudFront distribution thuộc tài khoản AWS khác.

2.  **Hỗ trợ Mã hóa SSE-KMS:** 
Một trong những điểm yếu lớn nhất của OAI là không hỗ trợ tải lên/tải xuống các tệp được mã hóa bằng AWS KMS. OAC đã giải quyết vấn đề này, cho phép mã hóa payload một cách an toàn và tuân thủ các tiêu chuẩn bảo mật khắt khe nhất của doanh nghiệp.

3.  **Hỗ trợ toàn diện HTTP Methods:** 
Khác với OAI vốn chỉ tối ưu cho việc đọc tĩnh, OAC hỗ trợ tất cả các phương thức HTTP bao gồm GET, PUT, POST, PATCH, DELETE, OPTIONS, và HEAD. Điều này mở ra khả năng xây dựng các ứng dụng tương tác hai chiều thông qua CloudFront một cách dễ dàng.

4.  **Mở rộng khả năng hỗ trợ (Beyond S3):** 
Không chỉ dừng lại ở Amazon S3, cơ chế OAC đã được AWS thiết kế mở rộng để hỗ trợ bảo mật cho cả Lambda Function URLs và các dịch vụ khác trong tương lai.

Việc chuyển đổi từ OAI sang OAC hiện nay là một best practice (thực hành tốt nhất) bắt buộc phải biết nếu bạn đang kiến trúc và triển khai các ứng dụng web nhằm đảm bảo an toàn tuyệt đối cho dữ liệu mã nguồn tĩnh.

![CloudFront OAC](/images/cloudfront-oac.png)

### Link bài viết gốc
**[Đọc toàn bộ bài viết trên AWS Networking Blog](https://aws.amazon.com/blogs/networking-and-content-delivery/amazon-cloudfront-introduces-origin-access-control-oac/)**