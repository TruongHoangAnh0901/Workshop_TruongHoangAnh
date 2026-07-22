import os
from datetime import date, timedelta

start_date = date(2026, 4, 20) # Monday

weeks_data = [
    {
        'goal_vi': [
            'Nắm vững các khái niệm cơ bản về hệ sinh thái Điện toán đám mây của AWS.',
            'Tìm hiểu về giao diện quản lý AWS Management Console và các Region/Availability Zone.',
            'Thực hành thiết lập AWS Free Tier, quản lý Billing và cảnh báo vượt ngân sách (Cost Management).',
            'Nắm bắt khái quát về Mạng (VPC), Bảo mật (IAM), Máy chủ ảo (EC2) và Cơ sở dữ liệu (RDS/DynamoDB).'
        ],
        'goal_en': [
            'Master the basic concepts of the AWS Cloud Computing ecosystem.',
            'Learn about the AWS Management Console interface and Regions/Availability Zones.',
            'Practice setting up AWS Free Tier, managing Billing, and configuring budget alerts (Cost Management).',
            'Grasp core concepts of Networking (VPC), Security (IAM), Virtual Servers (EC2), and Databases (RDS/DynamoDB).'
        ],
        'tasks_vi': [
            'Làm quen với **hệ sinh thái điện toán đám mây AWS**, giao diện quản lý (Console) và các Region.',
            'Tìm hiểu về **Billing and Cost Management**, thiết lập AWS Free Tier và cảnh báo vượt ngân sách.',
            'Nắm bắt các khái niệm cơ bản về **Mạng (VPC)** và **Bảo mật (IAM)** trên Cloud.',
            'Khám phá **Máy chủ ảo (EC2)**, các loại instance và dịch vụ lưu trữ khối (EBS).',
            'Tìm hiểu các loại **Cơ sở dữ liệu trên Cloud**, so sánh giữa RDS (có cấu trúc) và NoSQL.'
        ],
        'tasks_en': [
            'Get familiar with the **AWS cloud ecosystem**, understand the Management Console and Regions.',
            'Learn about **Billing and Cost Management**, set up AWS Free Tier and budget alerts.',
            'Grasp basic concepts of **Network (VPC)** and **Security (IAM)** on the Cloud.',
            'Explore **Virtual Servers (EC2)**, instance types, and block storage (EBS).',
            'Understand **Databases on Cloud**, compare RDS (relational) vs NoSQL.'
        ],
        'days_offset': [(0, 'Thứ 2', 'Mon'), (1, 'Thứ 3', 'Tue'), (2, 'Thứ 4', 'Wed'), (3, 'Thứ 5', 'Thu'), (4, 'Thứ 6', 'Fri')],
        'result_vi': [
            'Đã hiểu rõ hệ sinh thái AWS và sự khác biệt giữa các mô hình Cloud computing (IaaS, PaaS, SaaS).',
            'Cấu hình thành công cảnh báo ngân sách (Budget Alerts) để kiểm soát chi phí thực hành.',
            'Nắm vững kiến thức nền tảng của các dịch vụ cốt lõi:',
            '  * **Compute:** Nắm được khái niệm EC2, các loại instance family và use-case.',
            '  * **Storage:** Phân biệt được đặc tính của Block storage (EBS) và Object storage (S3).',
            '  * **Database:** Nắm được ưu/nhược điểm của RDS (SQL) so với DynamoDB (NoSQL).',
            'Bước đầu biết cách tra cứu tài liệu kỹ thuật AWS và sử dụng giao diện console.'
        ],
        'result_en': [
            'Fully understood the AWS ecosystem and differences between Cloud computing models (IaaS, PaaS, SaaS).',
            'Successfully configured Budget Alerts to control practice costs.',
            'Mastered foundational knowledge of core services:',
            '  * **Compute:** Understood EC2 concepts, instance families, and use-cases.',
            '  * **Storage:** Differentiated characteristics of Block storage (EBS) and Object storage (S3).',
            '  * **Database:** Grasped the pros/cons of RDS (SQL) versus DynamoDB (NoSQL).',
            'Learned how to navigate AWS technical documentation and use the console interface.'
        ]
    },
    {
        'goal_vi': [
            'Hiểu và thực hành triển khai máy chủ ảo Amazon EC2 (Linux & Windows).',
            'Nắm bắt các khái niệm cơ bản về mạng ảo (Amazon VPC) và các thành phần cấu thành.',
            'Thực hành cấu hình Security Groups (tường lửa cấp độ instance) để bảo mật máy chủ.'
        ],
        'goal_en': [
            'Understand and practice deploying Amazon EC2 virtual servers (Linux & Windows).',
            'Grasp the basic concepts of virtual networking (Amazon VPC) and its components.',
            'Practice configuring Security Groups (instance-level firewalls) to secure servers.'
        ],
        'tasks_vi': [
            'Đi sâu vào **Amazon EC2**, học cách cấp phát máy chủ và chọn AMI phù hợp.',
            'Thực hành **khởi tạo máy chủ Linux và Windows**, cài đặt web server cơ bản (Apache).',
            'Tìm hiểu về **Virtual Private Cloud (VPC)**, mạng con (subnets), bảng định tuyến và Internet Gateways.',
            'Đọc tài liệu mạng và cấu hình **Security Groups** để kiểm soát truy cập vào/ra (inbound/outbound).'
        ],
        'tasks_en': [
            'Deep dive into **Amazon EC2**, learn how to provision instances and select the right AMIs.',
            'Practice **initializing Linux and Windows servers**, install a basic web server (Apache).',
            'Learn about **Virtual Private Cloud (VPC)**, subnets, route tables, and Internet Gateways.',
            'Review networking documents and configure **Security Groups** to control inbound/outbound traffic.'
        ],
        'days_offset': [(0, 'Thứ 2', 'Mon'), (1, 'Thứ 3', 'Tue'), (3, 'Thứ 5', 'Thu'), (4, 'Thứ 6', 'Fri')],
        'result_vi': [
            'Triển khai thành công máy chủ ảo Amazon EC2 thực tế:',
            '  * Khởi tạo thành công các máy chủ từ nhiều loại AMI (Linux, Windows).',
            '  * Cài đặt và cấu hình thành công web server Apache chạy trên EC2.',
            'Đã hiểu rõ cơ chế hoạt động cơ bản của Amazon VPC, Subnets, Route Tables.',
            'Cấu hình thành thạo **Security Groups**, áp dụng nguyên tắc đặc quyền tối thiểu (Principle of Least Privilege) để giới hạn port HTTP/SSH.',
            'Làm quen với việc thao tác EC2 thông qua SSH (Linux) và RDP (Windows).'
        ],
        'result_en': [
            'Successfully deployed actual Amazon EC2 virtual servers:',
            '  * Launched instances using various AMIs (Linux, Windows).',
            '  * Installed and configured an Apache web server running on EC2.',
            'Clearly understood the basic mechanisms of Amazon VPC, Subnets, and Route Tables.',
            'Proficiently configured **Security Groups**, applying the Principle of Least Privilege to restrict HTTP/SSH ports.',
            'Got accustomed to operating EC2 via SSH (Linux) and RDP (Windows).'
        ]
    },
    {
        'goal_vi': [
            'Thực hành chuyên sâu về thiết kế mạng bảo mật trên AWS thông qua Custom VPC.',
            'Cấu hình NAT Gateway để bảo mật luồng truy cập Internet cho Private Subnet.',
            'Nghiên cứu sâu về các loại cơ sở dữ liệu trên AWS để chuẩn bị kiến trúc cho dự án Quiz App.',
            'Nâng cao nhận thức về bảo mật Cloud thông qua sự kiện nội bộ của công ty.'
        ],
        'goal_en': [
            'In-depth practice on secure network design on AWS using Custom VPC.',
            'Configure NAT Gateway to secure Internet access for Private Subnets.',
            'Deeply research AWS databases to prepare the architecture for the Quiz App project.',
            'Enhance Cloud security awareness through the company\'s internal event.'
        ],
        'tasks_vi': [
            'Thực hành tạo **Custom VPC** với public và private subnets để cách ly hệ thống an toàn.',
            'Cấu hình **NAT Gateway** để các tài nguyên trong private subnet có thể truy cập Internet an toàn.',
            'Tìm hiểu các loại cơ sở dữ liệu trên AWS (**RDS, DynamoDB**) để chuẩn bị cho dự án Quiz App.',
            'So sánh dữ liệu có cấu trúc và không cấu trúc, tiến hành thiết kế **database schema**.',
            'Tham gia sự kiện First Cloud Security Journey của công ty.'
        ],
        'tasks_en': [
            'Hands-on practice creating a **Custom VPC** with public and private subnets to isolate resources securely.',
            'Set up a **NAT Gateway** to allow private subnets to access the internet securely.',
            'Explore database types on AWS (**RDS, DynamoDB**) in preparation for the Quiz App project.',
            'Compare structured vs unstructured data and design the **database schema**.',
            'Attend the company\'s First Cloud Security Journey event.'
        ],
        'days_offset': [(0, 'Thứ 2', 'Mon'), (1, 'Thứ 3', 'Tue'), (2, 'Thứ 4', 'Wed'), (3, 'Thứ 5', 'Thu'), (5, 'Thứ 7', 'Sat')],
        'result_vi': [
            'Thiết kế và xây dựng thành công kiến trúc mạng **Custom VPC** đạt chuẩn bảo mật:',
            '  * Phân tách rõ ràng giữa Public Subnet (chứa tài nguyên có thể truy cập từ internet) và Private Subnet.',
            '  * Định tuyến thành công **NAT Gateway** cho các máy chủ ở Private Subnet cập nhật phần mềm an toàn.',
            'Hoàn thiện bước khảo sát và thiết kế dữ liệu:',
            '  * Phân tích rõ sự khác biệt hiệu năng và chi phí giữa RDS và DynamoDB.',
            '  * Hoàn thành phác thảo thiết kế cấu trúc bảng (schema) tối ưu nhất cho dự án Quiz App.',
            'Tiếp thu và ghi chú được nhiều best practices về Cloud Security từ sự kiện nội bộ.'
        ],
        'result_en': [
            'Designed and built a **Custom VPC** network architecture meeting security standards:',
            '  * Clear segregation between Public Subnets (internet-facing resources) and Private Subnets.',
            '  * Successfully routed **NAT Gateway** for servers in Private Subnets to update software securely.',
            'Completed database research and design phase:',
            '  * Analyzed performance and cost differences between RDS and DynamoDB.',
            '  * Finished sketching the optimal table structure (schema) for the Quiz App project.',
            'Absorbed and noted many Cloud Security best practices from the internal event.'
        ]
    },
    {
        'goal_vi': [
            'Thiết lập hạ tầng Cơ sở dữ liệu NoSQL với Amazon DynamoDB.',
            'Phát triển mã nguồn xử lý logic Backend bằng ngôn ngữ Python.',
            'Triển khai kiến trúc Serverless (không máy chủ) sử dụng AWS Lambda và Amazon API Gateway.'
        ],
        'goal_en': [
            'Set up NoSQL Database infrastructure with Amazon DynamoDB.',
            'Develop Backend logic source code using Python.',
            'Deploy a Serverless architecture using AWS Lambda and Amazon API Gateway.'
        ],
        'tasks_vi': [
            'Khởi tạo cơ sở dữ liệu **DynamoDB (NoSQL)** để lưu trữ thông tin người dùng, đề thi và điểm số.',
            'Viết code xử lý logic **Serverless Backend** bằng ngôn ngữ Python và thư viện Boto3.',
            'Đưa các hàm xử lý Backend lên **AWS Lambda** để hệ thống chạy mà không cần quản lý máy chủ.',
            'Cấu hình **API Gateway** để định tuyến các HTTP request từ phía người dùng vào các hàm Lambda.'
        ],
        'tasks_en': [
            'Initialize **DynamoDB (NoSQL)** database to store users, quizzes, and scores efficiently.',
            'Write the **Serverless Backend** logic using Python and Boto3 library to interact with DynamoDB.',
            'Deploy the project\'s backend functions to **AWS Lambda** for execution without managing servers.',
            'Configure **API Gateway** to route HTTP requests from users to the Lambda functions.'
        ],
        'days_offset': [(0, 'Thứ 2', 'Mon'), (1, 'Thứ 3', 'Tue'), (3, 'Thứ 5', 'Thu'), (4, 'Thứ 6', 'Fri')],
        'result_vi': [
            'Triển khai thành công hạ tầng **Serverless Backend** cho toàn bộ dự án Quiz App:',
            '  * Khởi tạo và thiết lập quyền truy cập an toàn cho các bảng dữ liệu trên **Amazon DynamoDB**.',
            '  * Viết và debug thành công các hàm xử lý logic Backend bằng **Python (Boto3)**.',
            '  * Đóng gói và upload source code lên **AWS Lambda**, giảm thiểu chi phí duy trì máy chủ 24/7.',
            '  * Tích hợp thành công **Amazon API Gateway** để tạo RESTful APIs kết nối an toàn với Lambda.',
            'Đảm bảo Backend xử lý mượt mà các thao tác CRUD (Tạo, Đọc, Sửa, Xóa) dữ liệu người dùng và đề thi.'
        ],
        'result_en': [
            'Successfully deployed the **Serverless Backend** infrastructure for the entire Quiz App project:',
            '  * Initialized and set up secure access permissions for data tables on **Amazon DynamoDB**.',
            '  * Successfully wrote and debugged Backend logic functions using **Python (Boto3)**.',
            '  * Packaged and uploaded source code to **AWS Lambda**, minimizing 24/7 server maintenance costs.',
            '  * Successfully integrated **Amazon API Gateway** to create RESTful APIs securely connecting to Lambda.',
            'Ensured the Backend smoothly handles CRUD operations (Create, Read, Update, Delete) for user and quiz data.'
        ]
    },
    {
        'goal_vi': [
            'Nghiên cứu dịch vụ phân giải tên miền (DNS) Amazon Route 53.',
            'Tìm hiểu chuyên sâu về dịch vụ lưu trữ Object Storage vô hạn (Amazon S3).',
            'Tiếp tục tham gia chuỗi sự kiện bảo mật để nâng cao nhận thức về mã hóa.'
        ],
        'goal_en': [
            'Research the Amazon Route 53 Domain Name System (DNS) service.',
            'Gain in-depth understanding of the limitless Object Storage service (Amazon S3).',
            'Continue attending the security event series to raise encryption awareness.'
        ],
        'tasks_vi': [
            'Tìm hiểu tổng quan về **Amazon Route 53**, nắm bắt public/private DNS zones và phân giải tên miền.',
            'Nghiên cứu dịch vụ lưu trữ **Amazon S3**, tìm hiểu về buckets, objects và host website tĩnh.',
            'Tham gia sự kiện First Cloud Security Journey của công ty.'
        ],
        'tasks_en': [
            'Get an overview of **Amazon Route 53**, understand public/private DNS zones and domain resolution.',
            'Dive into **Amazon S3** storage service, learn about buckets, objects, and static website hosting.',
            'Attend the company\'s First Cloud Security Journey event.'
        ],
        'days_offset': [(0, 'Thứ 2', 'Mon'), (2, 'Thứ 4', 'Wed'), (5, 'Thứ 7', 'Sat')],
        'result_vi': [
            'Đã hiểu rõ cơ chế hoạt động của **Amazon Route 53**:',
            '  * Khả năng quản lý và định tuyến lưu lượng DNS toàn cầu.',
            '  * Biết cách tạo Hosted Zones và cấu hình các loại Record (A, CNAME, ALIAS).',
            'Thành thạo các thao tác cơ bản với **Amazon S3**:',
            '  * Tạo S3 Buckets, quản lý quyền truy cập (Bucket Policies) an toàn.',
            '  * Nắm được tính năng Static Website Hosting để chuẩn bị triển khai Frontend.',
            'Hiểu thêm về các cơ chế mã hóa dữ liệu at-rest và in-transit từ sự kiện bảo mật.'
        ],
        'result_en': [
            'Clearly understood the operating mechanism of **Amazon Route 53**:',
            '  * Global DNS traffic management and routing capabilities.',
            '  * Knowing how to create Hosted Zones and configure Record types (A, CNAME, ALIAS).',
            'Mastered basic operations with **Amazon S3**:',
            '  * Creating S3 Buckets and securely managing access permissions (Bucket Policies).',
            '  * Grasped the Static Website Hosting feature to prepare for Frontend deployment.',
            'Gained more understanding of data encryption at-rest and in-transit from the security event.'
        ]
    },
    {
        'goal_vi': [
            'Triển khai giao diện người dùng (Frontend) lên Cloud.',
            'Sử dụng Content Delivery Network (CDN) để tăng tốc độ tải trang toàn cầu.',
            'Thiết lập kết nối HTTPS an toàn thông qua chứng chỉ SSL/TLS miễn phí của AWS.'
        ],
        'goal_en': [
            'Deploy the User Interface (Frontend) to the Cloud.',
            'Use a Content Delivery Network (CDN) to accelerate global page load speeds.',
            'Set up secure HTTPS connections via AWS\'s free SSL/TLS certificates.'
        ],
        'tasks_vi': [
            'Build source code ReactJS và đưa **giao diện Website (Frontend)** lên lưu trữ trực tiếp trên Amazon S3.',
            'Cài đặt **Amazon CloudFront** để phân phối website trên toàn cầu và giảm độ trễ cho người dùng.',
            'Yêu cầu chứng chỉ SSL thông qua **AWS Certificate Manager (ACM)** để thiết lập kết nối HTTPS an toàn.',
            'Cấu hình **Origin Access Control (OAC)** để ngăn chặn truy cập trực tiếp vào S3 bucket.'
        ],
        'tasks_en': [
            'Build the ReactJS source code and host the **Website interface (Frontend)** on Amazon S3.',
            'Set up **Amazon CloudFront** to distribute the website globally and reduce latency for users.',
            'Request an SSL certificate via **AWS Certificate Manager (ACM)** for secure HTTPS connections.',
            'Configure **Origin Access Control (OAC)** to restrict direct access to the S3 bucket.'
        ],
        'days_offset': [(0, 'Thứ 2', 'Mon'), (1, 'Thứ 3', 'Tue'), (3, 'Thứ 5', 'Thu'), (4, 'Thứ 6', 'Fri')],
        'result_vi': [
            'Dự án Quiz App đã hoàn thiện phần Giao diện Frontend và sẵn sàng tiếp cận người dùng:',
            '  * Build và host thành công code ReactJS lên **Amazon S3**.',
            '  * Phân phối nội dung tĩnh siêu tốc nhờ mạng lưới Edge Locations của **Amazon CloudFront**.',
            'Đảm bảo tuyệt đối an toàn bảo mật cho người dùng truy cập:',
            '  * Ứng dụng đã được cấp chứng chỉ SSL hợp lệ qua **AWS ACM** và chạy trên giao thức HTTPS.',
            '  * Cấu hình **OAC (Origin Access Control)** thành công, ép buộc mọi truy cập phải đi qua CDN (CloudFront) thay vì truy cập trực tiếp vào nguồn S3.'
        ],
        'result_en': [
            'Quiz App project Frontend is fully completed and ready for users:',
            '  * Successfully built and hosted ReactJS code on **Amazon S3**.',
            '  * Distributed static content at high speed thanks to **Amazon CloudFront\'s** Edge Locations network.',
            'Ensured absolute security for accessing users:',
            '  * The application was issued a valid SSL certificate via **AWS ACM** and runs on HTTPS protocol.',
            '  * Successfully configured **OAC (Origin Access Control)**, forcing all traffic to pass through the CDN (CloudFront) rather than accessing the S3 origin directly.'
        ]
    },
    {
        'goal_vi': [
            'Tìm hiểu mô hình kiến trúc bất đồng bộ (Asynchronous Architecture).',
            'Nghiên cứu dịch vụ hàng đợi tin nhắn Amazon SQS.',
            'Thực hành kết nối SQS với Lambda để xử lý khối lượng lớn công việc ngầm.'
        ],
        'goal_en': [
            'Learn about Asynchronous Architecture models.',
            'Research the Amazon SQS message queueing service.',
            'Practice connecting SQS with Lambda to process heavy background workloads.'
        ],
        'tasks_vi': [
            'Tìm hiểu cách xử lý **các công việc chạy ngầm** để website không bị đơ khi có lượng lớn người truy cập.',
            'Nắm bắt khái niệm message queueing và thiết lập hàng đợi **Amazon SQS**.',
            'Thực hành tích hợp **SQS với Lambda** để xử lý các tin nhắn một cách bất đồng bộ.',
            'Nghiên cứu sâu hơn về **Lambda triggers** và kiến trúc hướng sự kiện (event-driven) trong AWS.',
            'Triển khai tính năng xử lý ngầm cho **hệ thống chấm điểm** của dự án Quiz App.'
        ],
        'tasks_en': [
            'Learn how to process **background jobs** to prevent the website from lagging during high traffic.',
            'Understand message queueing concepts and set up **Amazon SQS** queues.',
            'Practice integrating **SQS with Lambda** to process messages asynchronously.',
            'Research **Lambda triggers** and event-driven architecture within AWS.',
            'Implement background processing for the Quiz App\'s **score calculation system**.'
        ],
        'days_offset': [(0, 'Thứ 2', 'Mon'), (1, 'Thứ 3', 'Tue'), (2, 'Thứ 4', 'Wed'), (3, 'Thứ 5', 'Thu'), (4, 'Thứ 6', 'Fri')],
        'result_vi': [
            'Nâng cấp hệ thống Quiz App lên kiến trúc Event-Driven tiên tiến:',
            '  * Tích hợp thành công **Amazon SQS** làm bộ đệm (buffer) cho các yêu cầu gửi về từ người dùng.',
            '  * Sử dụng SQS làm Trigger kích hoạt **AWS Lambda** xử lý chấm điểm ngầm một cách mượt mà.',
            'Hệ thống hiện tại đã có thể chịu tải tốt hơn (Decoupled architecture):',
            '  * Website không còn bị treo hoặc timeout khi có hàng ngàn học sinh nộp bài thi cùng một lúc.',
            '  * Nắm vững các khái niệm Visibility Timeout và Dead Letter Queue trong xử lý lỗi.'
        ],
        'result_en': [
            'Upgraded the Quiz App system to an advanced Event-Driven architecture:',
            '  * Successfully integrated **Amazon SQS** as a buffer for incoming user requests.',
            '  * Used SQS as a Trigger to activate **AWS Lambda** for smooth background score calculation.',
            'The system can now handle heavy traffic much better (Decoupled architecture):',
            '  * The website no longer freezes or times out when thousands of students submit exams simultaneously.',
            '  * Mastered concepts of Visibility Timeout and Dead Letter Queue in error handling.'
        ]
    },
    {
        'goal_vi': [
            'Tăng cường bảo vệ ứng dụng ở tầng Application (Lớp 7 OSI).',
            'Tìm hiểu và cấu hình Tường lửa ứng dụng web AWS WAF.',
            'Ngăn chặn các hình thức tấn công mạng phổ biến như SQL Injection, XSS.'
        ],
        'goal_en': [
            'Enhance application protection at the Application layer (OSI Layer 7).',
            'Learn and configure the AWS Web Application Firewall (AWS WAF).',
            'Prevent common cyber attacks such as SQL Injection and XSS.'
        ],
        'tasks_vi': [
            'Tìm hiểu các khái niệm và cơ chế hoạt động của **Tường lửa ứng dụng web (AWS WAF)**.',
            'Cài đặt các luật (rules) cho AWS WAF để bảo vệ website khỏi **tấn công mạng và SQL injection**.',
            'Giám sát các request bị chặn và tinh chỉnh **các rule bảo mật WAF** để tối ưu hóa.',
            'Tham gia sự kiện First Cloud Security Journey của công ty.'
        ],
        'tasks_en': [
            'Learn the concepts and workings of **Web Application Firewall (AWS WAF)**.',
            'Set up AWS WAF rules to protect the website from common **cyber attacks and SQL injections**.',
            'Monitor blocked requests and fine-tune the **WAF security rules**.',
            'Attend the company\'s First Cloud Security Journey event.'
        ],
        'days_offset': [(0, 'Thứ 2', 'Mon'), (1, 'Thứ 3', 'Tue'), (3, 'Thứ 5', 'Thu'), (5, 'Thứ 7', 'Sat')],
        'result_vi': [
            'Dự án Quiz App đã được trang bị lớp khiên bảo vệ vững chắc với **AWS WAF**:',
            '  * Đính kèm thành công Web ACL (WAF) vào bản phân phối **CloudFront** để bảo vệ Frontend.',
            '  * Kích hoạt bộ quy tắc bảo mật do AWS quản lý (AWS Managed Rules).',
            'Ngăn chặn tự động các luồng truy cập độc hại:',
            '  * Hệ thống tự động chặn các cú pháp SQL Injection và Cross-Site Scripting (XSS).',
            '  * Giảm thiểu nguy cơ bị tấn công rò rỉ dữ liệu đề thi và điểm số của học sinh.',
            'Biết cách đọc Logs và biểu đồ request bị WAF chặn trên bảng điều khiển.'
        ],
        'result_en': [
            'The Quiz App project was equipped with a robust protective shield using **AWS WAF**:',
            '  * Successfully attached a Web ACL (WAF) to the **CloudFront** distribution to protect the Frontend.',
            '  * Activated AWS Managed Rules for security.',
            'Automatically blocked malicious traffic streams:',
            '  * The system automatically blocks SQL Injection and Cross-Site Scripting (XSS) syntaxes.',
            '  * Minimized the risk of attacks leaking exam data and student scores.',
            'Learned how to read Logs and charts of requests blocked by WAF on the dashboard.'
        ]
    },
    {
        'goal_vi': [
            'Nghiên cứu về khả năng quan sát (Observability) và giám sát hệ thống trên AWS.',
            'Sử dụng Amazon CloudWatch để thu thập Logs và Metrics.',
            'Tự động hóa cảnh báo sự cố thông qua CloudWatch Alarms.'
        ],
        'goal_en': [
            'Research Observability and system monitoring on AWS.',
            'Use Amazon CloudWatch to collect Logs and Metrics.',
            'Automate incident alerts via CloudWatch Alarms.'
        ],
        'tasks_vi': [
            'Khám phá dịch vụ giám sát và khả năng quan sát hệ thống **Amazon CloudWatch**.',
            'Theo dõi các metrics hệ thống và xem **log lỗi (error logs)** của AWS Lambda và API Gateway.',
            'Tạo **CloudWatch Dashboards** trực quan và thiết lập Alarm để cảnh báo khi có sự cố hệ thống.'
        ],
        'tasks_en': [
            'Explore the **Amazon CloudWatch** monitoring and observability service.',
            'Monitor system metrics and view **error logs** for AWS Lambda and API Gateway.',
            'Create visual **CloudWatch Dashboards** and set up Alarms to trigger alerts on system issues.'
        ],
        'days_offset': [(0, 'Thứ 2', 'Mon'), (2, 'Thứ 4', 'Wed'), (4, 'Thứ 6', 'Fri')],
        'result_vi': [
            'Làm chủ được công cụ giám sát toàn diện **Amazon CloudWatch**:',
            '  * Thu thập và phân tích thành công Log Groups của tất cả các hàm **AWS Lambda**.',
            '  * Truy vết dễ dàng các lỗi (bug) khi hệ thống Backend trả về mã lỗi 500.',
            'Thiết lập thành công trung tâm điều khiển (Dashboard) cho dự án:',
            '  * Vẽ biểu đồ theo dõi số lượng Request, số lỗi và thời gian phản hồi (Latency) của API Gateway.',
            '  * Cấu hình **CloudWatch Alarms** tự động gửi email cảnh báo mỗi khi số lượng lỗi vượt ngưỡng cho phép.'
        ],
        'result_en': [
            'Mastered the comprehensive monitoring tool **Amazon CloudWatch**:',
            '  * Successfully collected and analyzed Log Groups of all **AWS Lambda** functions.',
            '  * Easily traced bugs when the Backend system returned 500 error codes.',
            'Successfully set up a control center (Dashboard) for the project:',
            '  * Drew charts to monitor Request count, Error count, and Latency of the API Gateway.',
            '  * Configured **CloudWatch Alarms** to automatically send warning emails whenever the error rate exceeds the threshold.'
        ]
    },
    {
        'goal_vi': [
            'Quản trị tập trung tình trạng bảo mật của toàn bộ tài khoản AWS.',
            'Nghiên cứu AWS Security Hub và các dịch vụ đánh giá tuân thủ tự động.',
            'Phân tích, ước tính và tối ưu hóa chi phí vận hành kiến trúc Serverless.'
        ],
        'goal_en': [
            'Centrally manage the security posture of the entire AWS account.',
            'Research AWS Security Hub and automated compliance assessment services.',
            'Analyze, estimate, and optimize the operating costs of the Serverless architecture.'
        ],
        'tasks_vi': [
            'Tìm hiểu về **AWS Security Hub** để quản lý trạng thái bảo mật một cách tập trung.',
            'Tích hợp kết quả từ **GuardDuty, Inspector và Macie** vào bảng điều khiển chung của Security Hub.',
            'Theo dõi và đánh giá mức độ **tuân thủ bảo mật tổng thể** cho tài khoản AWS.',
            'Phân tích chi phí đang chạy bằng **AWS Pricing Calculator** và Cost Explorer để tối ưu hệ thống.'
        ],
        'tasks_en': [
            'Learn about **AWS Security Hub** for centralized security posture management.',
            'Integrate findings from **GuardDuty, Inspector, and Macie** into the Security Hub dashboard.',
            'Monitor and evaluate the overall **security compliance** for the AWS account.',
            'Analyze running costs using **AWS Pricing Calculator** and Cost Explorer to optimize the Serverless system.'
        ],
        'days_offset': [(0, 'Thứ 2', 'Mon'), (1, 'Thứ 3', 'Tue'), (3, 'Thứ 5', 'Thu'), (4, 'Thứ 6', 'Fri')],
        'result_vi': [
            'Nắm bắt được bức tranh tổng thể về bảo mật của tài khoản AWS thông qua **Security Hub**:',
            '  * Hiểu cách tổng hợp các phát hiện đe dọa (findings) từ nhiều dịch vụ về một màn hình duy nhất.',
            '  * Đánh giá kiến trúc dự án Quiz App dựa trên các tiêu chuẩn bảo mật thực tế (CIS Foundations Benchmark).',
            'Hoàn thành bài toán tối ưu hóa chi phí (Cost Optimization):',
            '  * Sử dụng **AWS Pricing Calculator** để ước tính chuẩn xác ngân sách hàng tháng cho Quiz App.',
            '  * Sử dụng **Cost Explorer** để tìm ra các tài nguyên dư thừa, tài nguyên chạy ngầm không cần thiết và tiến hành cắt giảm.'
        ],
        'result_en': [
            'Grasped the overall security posture of the AWS account via **Security Hub**:',
            '  * Understood how to aggregate threat findings from multiple services into a single dashboard.',
            '  * Evaluated the Quiz App project architecture based on practical security standards (CIS Foundations Benchmark).',
            'Completed the Cost Optimization challenge:',
            '  * Used **AWS Pricing Calculator** to accurately estimate the monthly budget for the Quiz App.',
            '  * Used **Cost Explorer** to find redundant resources and unnecessary background processes, and proceeded to cut them.'
        ]
    },
    {
        'goal_vi': [
            'Tìm hiểu về văn hóa DevOps và phương pháp Tự động hóa luồng triển khai phần mềm.',
            'Xây dựng luồng CI/CD pipelines trên AWS (CodePipeline, CodeBuild).',
            'Hoàn thành toàn bộ kiến trúc và Đưa dự án Workshop ra công chúng (Go Live).'
        ],
        'goal_en': [
            'Learn about DevOps culture and methodologies for Automating software deployment flows.',
            'Build CI/CD pipelines on AWS (CodePipeline, CodeBuild).',
            'Complete the entire architecture and launch the Workshop project to the public (Go Live).'
        ],
        'tasks_vi': [
            'Tìm hiểu các nguyên lý của luồng **Tích hợp liên tục và Triển khai liên tục (CI/CD)**.',
            'Tự động hóa quy trình triển khai bằng cách sử dụng **AWS CodePipeline** và **AWS CodeBuild**.',
            'Áp dụng CI/CD pipelines để đạt được tính năng cập nhật website **Zero-Downtime (không gián đoạn)**.',
            'Kiểm tra tự động hóa bằng cách đẩy source code mới lên **kho lưu trữ mã nguồn (repository)**.',
            'Hoàn thiện toàn bộ các chủ đề Workshop và **Triển khai thành công hệ thống Quiz App** ra Internet.'
        ],
        'tasks_en': [
            'Understand the principles of **Continuous Integration and Continuous Deployment (CI/CD)**.',
            'Automate the deployment process using **AWS CodePipeline** and **AWS CodeBuild**.',
            'Apply CI/CD pipelines to achieve **Zero-Downtime** website updates.',
            'Test the automated deployment by pushing new changes to the **source code repository**.',
            'Finalize all Workshop topics and successfully **Deploy the Quiz App system** to the Internet.'
        ],
        'days_offset': [(0, 'Thứ 2', 'Mon'), (1, 'Thứ 3', 'Tue'), (2, 'Thứ 4', 'Wed'), (3, 'Thứ 5', 'Thu'), (4, 'Thứ 6', 'Fri')],
        'result_vi': [
            'Thiết lập thành công quy trình Tự động hóa triển khai (CI/CD) cho mã nguồn Frontend:',
            '  * Khởi tạo **AWS CodePipeline** tự động theo dõi các thay đổi trên Github/CodeCommit.',
            '  * Sử dụng **AWS CodeBuild** để tự động chạy lệnh `npm build` và đồng bộ file lên Amazon S3.',
            'Đạt được mục tiêu tự động hóa hoàn toàn:',
            '  * Mọi thay đổi code của Developer đều được tự động đưa lên website trong vài phút mà không cần thao tác tay thủ công.',
            '  * Đảm bảo website cập nhật tính năng mới với tỷ lệ gián đoạn bằng 0 (Zero-Downtime).',
            'Dự án **Quiz App** chính thức đi vào hoạt động ổn định trên Internet.'
        ],
        'result_en': [
            'Successfully set up an Automated Deployment (CI/CD) pipeline for the Frontend source code:',
            '  * Initialized **AWS CodePipeline** to automatically track changes on Github/CodeCommit.',
            '  * Used **AWS CodeBuild** to automatically run `npm build` and sync files to Amazon S3.',
            'Achieved full automation goals:',
            '  * Any Developer code changes are automatically pushed to the website within minutes without manual intervention.',
            '  * Ensured the website updates with new features with zero downtime.',
            'The **Quiz App** project officially goes live and operates stably on the Internet.'
        ]
    },
    {
        'goal_vi': [
            'Tiến hành rà soát (Review) lại toàn bộ hệ thống từ Frontend đến Backend.',
            'Tiến hành kiểm thử (Testing) và khắc phục các lỗi (Bugs) còn tồn đọng.',
            'Chuẩn bị hồ sơ, tài liệu báo cáo thực tập và thiết kế các Slide thuyết trình.'
        ],
        'goal_en': [
            'Conduct a thorough review of the entire system from Frontend to Backend.',
            'Conduct Testing and fix outstanding Bugs.',
            'Prepare files, internship report documentation, and design presentation slides.'
        ],
        'tasks_vi': [
            'Tiến hành **rà soát và chỉnh sửa** toàn bộ dự án, kiểm tra kỹ lưỡng tất cả các luồng người dùng.',
            '**Khắc phục lỗi (Fix bugs)** và tối ưu hóa hiệu suất của các thành phần Serverless trong hệ thống.',
            'Tổng hợp kết quả đạt được và các cột mốc quan trọng trong **toàn bộ quá trình thực tập**.',
            'Hoàn thành báo cáo.'
        ],
        'tasks_en': [
            'Conduct a thorough **review and revision** of the project, testing all user flows carefully.',
            '**Fix bugs** and optimize the performance of various Serverless components in the system.',
            'Summarize the execution results and milestones achieved during the **entire internship period**.',
            'Complete the report.'
        ],
        'days_offset': [(0, 'Thứ 2', 'Mon'), (1, 'Thứ 3', 'Tue'), (3, 'Thứ 5', 'Thu'), (4, 'Thứ 6', 'Fri')],
        'result_vi': [
            'Dự án Quiz App đã được kiểm thử toàn diện (End-to-End Testing):',
            '  * Xác nhận không còn xuất hiện lỗi liên quan đến quyền truy cập IAM, lỗi Lambda timeout hay lỗi phân giải DNS.',
            '  * Hệ thống đáp ứng tốt các tiêu chí về tốc độ tải, bảo mật, và khả năng tự động mở rộng (Scalability).',
            'Hoàn thành xuất sắc nhiệm vụ báo cáo:',
            '  * Tổng hợp toàn bộ Worklog và tài liệu Workshop chi tiết vào báo cáo chính thức.',
            '  * Hoàn thiện thiết kế Slide thuyết trình bảo vệ với nội dung súc tích, trực quan.',
            'Sẵn sàng cho buổi thuyết trình tổng kết quá trình thực tập tại công ty.'
        ],
        'result_en': [
            'The Quiz App project underwent comprehensive End-to-End Testing:',
            '  * Confirmed no remaining errors related to IAM access rights, Lambda timeouts, or DNS resolution issues.',
            '  * The system meets all criteria for load speed, security, and Auto-Scalability.',
            'Successfully accomplished the reporting task:',
            '  * Aggregated all Worklogs and detailed Workshop documents into the official report.',
            '  * Finalized the presentation Slide design with concise, visual content.',
            'Ready for the final internship summary presentation at the company.'
        ]
    }
]

for i, w in enumerate(weeks_data):
    week_num = i + 1
    current_week_start = start_date + timedelta(days=7 * i)
    
    # Vietnamese
    vi_content = f"""---
title: "Worklog Tuần {week_num}"
date: 2024-01-01
weight: {week_num}
chapter: false
pre: " <b> 1.{week_num}. </b> "
---

### Mục tiêu tuần {week_num}:

"""
    for g in w['goal_vi']:
        vi_content += f"* {g}\n"

    vi_content += """
---

### Các công việc triển khai:

| Ngày (Day) | Công việc (Task) | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| ---------- | ---------------- | ------------ | --------------- | -------------- |
"""
    for j, (offset, vi_day, en_day) in enumerate(w['days_offset']):
        task_date = current_week_start + timedelta(days=offset)
        date_str = task_date.strftime("%d/%m/%Y")
        vi_content += f"| {vi_day} | {w['tasks_vi'][j]} | {date_str} | {date_str} | |\n"

    vi_content += """
---

### Kết quả đạt được:

"""
    for r in w['result_vi']:
        if r.startswith(' '):
            vi_content += f"{r}\n"
        else:
            vi_content += f"* {r}\n"

    # English
    en_content = f"""---
title: "Week {week_num} Worklog"
date: 2024-01-01
weight: {week_num}
chapter: false
pre: " <b> 1.{week_num}. </b> "
---

### Week {week_num} Objectives:

"""
    for g in w['goal_en']:
        en_content += f"* {g}\n"

    en_content += """
---

### Tasks implemented:

| Day | Task | Start Date | Completion Date | Reference/Material |
| --- | ---- | ---------- | --------------- | ------------------ |
"""
    for j, (offset, vi_day, en_day) in enumerate(w['days_offset']):
        task_date = current_week_start + timedelta(days=offset)
        date_str = task_date.strftime("%d/%m/%Y")
        en_content += f"| {en_day} | {w['tasks_en'][j]} | {date_str} | {date_str} | |\n"

    en_content += """
---

### Achievements:

"""
    for r in w['result_en']:
        if r.startswith(' '):
            en_content += f"{r}\n"
        else:
            en_content += f"* {r}\n"
    
    with open(f"e:/fcj-workshop-template-main/content/1-Worklog/1.{week_num}-week{week_num}/_index.vi.md", "w", encoding="utf-8") as f:
        f.write(vi_content)
    with open(f"e:/fcj-workshop-template-main/content/1-Worklog/1.{week_num}-week{week_num}/_index.md", "w", encoding="utf-8") as f:
        f.write(en_content)

print("SUCCESS")
