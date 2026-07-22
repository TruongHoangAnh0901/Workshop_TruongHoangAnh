---
title: "Event 2"
date: 2026-05-23
weight: 2
chapter: false
pre: " <b> 4.2. </b> "
---

# Sự kiện: AWS COMMUNITY DAY

**Thời gian:** 09:00 - 12:00, 23/05/2026  
**Địa điểm:** 26th Floor, Bitexco Tower, 02 Hai Trieu Street, Saigon Ward, Ho Chi Minh City  
**Vai trò:** Người tham dự  

Sự kiện AWS Community Day 2026 là một chuỗi các phiên chia sẻ chuyên sâu từ các chuyên gia hàng đầu, tập trung vào việc hiện đại hóa ứng dụng, quy trình phát triển và ứng dụng Generative AI vào thực tiễn. Dưới đây là bài thu hoạch và tóm tắt nội dung từ 6 diễn giả chính trong chương trình:

### 1. GenAIOps Essential DevOps for Generative Applications — Context Is Everything
**Diễn giả:** Tinh Truong (Platform Engineer tại GoTymeX)

- **Tầm quan trọng của ngữ cảnh (Context):** Mô hình AI rất mạnh mẽ nhưng kết quả thường bị hạn chế do dữ liệu đầu vào (prompt) yếu hoặc thiếu ngữ cảnh. Ngữ cảnh tốt sẽ giúp biến các yêu cầu mơ hồ thành các tác vụ có thể giải quyết chính xác.
- **Các sai lầm phổ biến khi cung cấp ngữ cảnh:**
  - Lỗi "Internet Puller": Sao chép toàn bộ bài viết, tài liệu dài vào chatbot làm nhiễu mô hình và tăng chi phí token.
  - Cung cấp thông tin thừa thãi: Nói lại những điều hiển nhiên mà AI đã biết thay vì tập trung vào yêu cầu cốt lõi tiếp theo.
  - Thiếu mục tiêu và ràng buộc: Prompt quá mơ hồ (ví dụ: "Xây dựng website portfolio") thay vì đưa ra các tiêu chí rõ ràng (React, Tailwind, giao diện Mobile-first).
- **Sự tiến hóa của hệ thống AI:** Chuyển dịch từ việc đặt câu hỏi đơn lẻ (Prompt) sang tích hợp tài liệu nền tảng (Context) và tiến tới xây dựng hệ thống ghi nhớ dài hạn (Memory) như một "Bộ não AI thứ hai" (Second AI Brain).
- **Lời khuyên nghề nghiệp:** Tương lai không phải là cuộc chiến giữa con người và AI, mà là giữa người biết cách làm việc với AI và người không biết. Khuyến khích tự xây dựng các dự án nhỏ như Trợ lý học tập AI, Ứng dụng chat với PDF, hoặc Hệ thống xem xét mã nguồn.

### 2. UTMorpho — 36 hrs with LotusHacks: Building UTMorpho from Idea to Reality
**Diễn giả:** Nhóm UTMorpho (Đội ngũ tham gia LotusHacks 2026)

- **Lý do tham gia:** Trải nghiệm áp lực của cuộc thi hackathon lớn nhất Việt Nam (36 giờ liên tục), học hỏi từ các lập trình viên khác và thử thách khả năng biến ý tưởng thành sản phẩm demo chạy được.
- **Ý tưởng sản phẩm (UTMorpho):** Xuất phát từ sự ức chế đối với các công cụ tạo UI bằng AI hiện tại (khi muốn sửa một chi tiết nhỏ phải prompt lại, làm thiết kế bị lệch và tốn token), nhóm đã tạo ra UTMorpho — một AI Agent cho phép tạo giao diện người dùng (UI) từ mô tả bằng văn bản và hỗ trợ chỉnh sửa trực tiếp trên canvas (WYSIWYG).
- **Quá trình triển khai 36 giờ:** Trải qua các giai đoạn từ lập đội, xây dựng khung backend, phát triển tính năng cốt lõi (đồng bộ trạng thái giữa editor và AI), xử lý các điểm nghẽn về giới hạn token cho đến khâu tinh chỉnh và thuyết trình.
- **Bài học kinh nghiệm:** Ý tưởng thực tế đến từ những bức xúc của chính bản thân; áp lực cao đôi khi cần những khoảng nghỉ để kích hoạt sự sáng tạo; tinh thần tin tưởng lẫn nhau trong đội ngũ quan trọng hơn kỹ năng cá nhân; và chi phí token là một ràng buộc lớn khi thiết kế trải nghiệm người dùng (UX).

### 3. Automate any business process using Amazon Quick Suite — Friendly AI Assistant w/ Amazon Quick
**Diễn giả:** Phạm Nguyễn Hải Anh (G-AsiaPacific Vietnam, AWS Community Builder)

- **Thực trạng của người dùng doanh nghiệp:** Thường xuyên phải lặp đi lặp lại các công việc hành chính nhàm chán, tốn thời gian như thu thập, phân tích thông tin từ nhiều nguồn và tổng hợp dữ liệu.
- **Giải pháp Amazon Quick Suite:** AWS giới thiệu giải pháp AI thế hệ mới cho doanh nghiệp, tích hợp dữ liệu nội bộ (Spaces, Datasets), tri thức thế giới, khả năng tìm kiếm web và hơn 40 cổng kết nối dữ liệu (Data connectors) cùng các mô hình Bedrock. Hệ thống đảm bảo tính bảo mật và tuân thủ quy định của doanh nghiệp (Governance, Guardrails, SOC 2, GDPR).
- **Ứng dụng thực tế (Trợ lý quản lý dự án - PM Assistant):** Tự động hóa hoàn toàn các quy trình như tạo Biên bản cuộc họp (MoM), gửi email cho các bên liên quan và tự động lên lịch cho cuộc họp tiếp theo.

### 4. CloudFront as Your Foundation — From Edge to Origin
**Diễn giả:** Nguyễn Tuấn Thịnh (DevOps Engineer tại First Cloud AI Journey - FCAJ)

- **Mô hình giá cố định mới (Flat-rate pricing):** AWS vừa ra mắt tính năng này (vào ngày 18/11), giúp giải quyết nhược điểm của mô hình "Pay as you go" truyền thống. Mô hình mới gộp chung các chi phí CDN, WAF, Anti-DDoS, DNS và lưu trữ S3 vào một mức giá cố định hàng tháng tùy theo các gói (Free, Pro, Business, Premium) giúp doanh nghiệp loại bỏ rủi ro tài chính.
- **Khả năng phòng thủ và tối ưu hệ thống:**
  - Phòng thủ DDoS phân tán: Chặn đứng các cuộc tấn công volumetric attack ngay tại các điểm Edge gần nguồn phát nhất thay vì đợi traffic đi sâu vào hệ thống.
  - Tối ưu hóa chi phí và hiệu năng: Lưu cache dữ liệu tại mạng lưới hơn 700 điểm PoPs toàn cầu. Bật tính năng nén HTTP giúp giảm dung lượng truyền tải lên đến 82%. Sử dụng giao thức HTTP/3 giúp tải song song nhiều tài nguyên, tăng tốc độ phản hồi.
  - Bảo mật nâng cao: Hỗ trợ mTLS (xác thực hai chiều) phục vụ cho các dịch vụ tài chính, quản lý chứng chỉ TLS miễn phí qua ACM và các giải pháp che giấu Origin (Origin cloaking) an toàn.

### 5. Enterprise-Grade Multi-Agent System — The Case of Startup Credit Scoring
**Diễn giả:** Vy Lâm (Senior Business Systems Analyst tại VPBank)

- **Sự bất tương thích dữ liệu:** Hệ thống chấm điểm tín dụng truyền thống của ngân hàng yêu cầu doanh nghiệp phải có báo cáo tài chính dài hạn. Trong khi đó, các startup thường chỉ mới hoạt động 6-18 tháng, dẫn đến việc hệ thống cũ thường từ chối các startup.
- **Kiến trúc Đa tác nhân (Multi-Agent Paradigm):** Thay vì dùng một AI Agent đơn lẻ dễ bị giới hạn ngữ cảnh, giải pháp đề xuất xây dựng một "Hội đồng tín dụng ảo" gồm nhiều Agent chuyên trách: Tác nhân phân tích tài chính, tác nhân đánh giá thị trường, tác nhân đánh giá đội ngũ sáng lập, tác nhân kiểm soát rủi ro và tác nhân tuân thủ quy định. Mô hình này giúp kiểm tra chéo, xử lý song song và cung cấp lộ trình giải trình rõ ràng.
- **Hiệu quả đầu tư (ROI):** Hệ thống giúp cắt giảm thời gian xử lý hồ sơ từ 2-3 tuần xuống còn 2-4 giờ (nhanh hơn 95%), giảm 95% số giờ làm việc của chuyên viên và tiết kiệm chi phí đưa ra quyết định đáng kể.

### 6. Non-Determinism of "Deterministic" LLM Settings
**Diễn giả:** Đức Đào (Solution Architect tại Cloud Kinetics)

- **Lầm tưởng về tính toàn định (Determinism):** Nhiều nhà phát triển tin rằng việc thiết lập nhiệt độ mô hình bằng 0 (temperature=0) sẽ đảm bảo kết quả đầu ra luôn giống nhau hoàn toàn cho cùng một câu lệnh.
- **Thực tế nghiên cứu:** Khi thử nghiệm trên 5 mô hình LLM lớn phổ biến, kết quả cho thấy không có mô hình nào đạt tính nhất quán 100%. Độ chính xác có thể lệch tới 15% giữa các lượt chạy giống hệt nhau.
- **Nguyên nhân cốt lõi:**
  - Kỹ thuật: Phép toán dấu phẩy động trên GPU không có tính kết hợp, và các luồng xử lý song song trên GPU có thứ tự thực thi ngẫu nhiên.
  - Thương mại: Các nhà cung cấp API gom chung yêu cầu của nhiều người dùng vào một lượt xử lý (Inference batching) làm thay đổi môi trường tính toán của prompt.
- **Chiến lược giảm thiểu:** Nên thiết lập temperature=0.1 (điểm ngọt) thay vì bằng 0; áp dụng phương pháp chạy nhiều lần và bỏ phiếu số đông (majority voting); thiết kế hệ thống có khả năng xử lý các kết quả mang tính xác suất.

### Trải Nghiệm (Event Experience)

Tham gia sự kiện "AWS COMMUNITY DAY 2026" là một cơ hội tuyệt vời để mình đắm chìm vào các xu hướng công nghệ đám mây và AI tiên tiến nhất hiện nay. Những giá trị thực tiễn lớn nhất mà mình nhận được bao gồm:

- **Mở rộng tư duy về Generative AI:** Hiểu sâu sắc hơn về cách cung cấp ngữ cảnh (Context) tối ưu cho LLMs, cũng như nắm bắt kiến trúc Đa tác nhân (Multi-Agent Paradigm) để giải quyết các bài toán doanh nghiệp phức tạp như chấm điểm tín dụng.
- **Nắm bắt thực tiễn bảo mật & hạ tầng:** Việc cập nhật mô hình giá mới của CloudFront và khả năng phòng thủ Edge-to-Origin giúp mình định hình được tư duy thiết kế hệ thống vừa an toàn vừa tối ưu chi phí.
- **Bài học từ những dự án thực tế:** Được truyền cảm hứng mạnh mẽ từ hành trình phát triển sản phẩm UTMorpho trong 36 giờ hackathon, cũng như thấu hiểu bản chất không toàn định (non-determinism) của các LLM để xây dựng hệ thống AI đáng tin cậy hơn.
- **Định hướng ứng dụng doanh nghiệp:** Hiểu rõ cách Amazon Quick Suite có thể tự động hóa quy trình nghiệp vụ (như PM Assistant), giúp mình có thêm góc nhìn về cách công nghệ trực tiếp giải quyết nỗi đau (pain points) của doanh nghiệp.

### Hình Ảnh Sự Kiện

![Event 2](/images/event2-img1.png)
