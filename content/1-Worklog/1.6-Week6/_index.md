---
title: "Week 6 Worklog"
date: 2024-01-01
weight: 6
chapter: false
pre: " <b> 1.6. </b> "
---

### Week 6 Objectives:

* Deploy the User Interface (Frontend) to the Cloud.
* Use a Content Delivery Network (CDN) to accelerate global page load speeds.
* Set up secure HTTPS connections via AWS's free SSL/TLS certificates.

---

### Tasks implemented:

| Day | Task | Start Date | Completion Date | Reference/Material |
| --- | ---- | ---------- | --------------- | ------------------ |
| Mon | Build the ReactJS source code and host the **Website interface (Frontend)** on Amazon S3. | 25/05/2026 | 25/05/2026 | |
| Tue | Set up **Amazon CloudFront** to distribute the website globally and reduce latency for users. | 26/05/2026 | 26/05/2026 | |
| Thu | Request an SSL certificate via **AWS Certificate Manager (ACM)** for secure HTTPS connections. | 28/05/2026 | 28/05/2026 | |
| Fri | Configure **Origin Access Control (OAC)** to restrict direct access to the S3 bucket. | 29/05/2026 | 29/05/2026 | |

---

### Achievements:

* Quiz App project Frontend is fully completed and ready for users:
  * Successfully built and hosted ReactJS code on **Amazon S3**.
  * Distributed static content at high speed thanks to **Amazon CloudFront's** Edge Locations network.
* Ensured absolute security for accessing users:
  * The application was issued a valid SSL certificate via **AWS ACM** and runs on HTTPS protocol.
  * Successfully configured **OAC (Origin Access Control)**, forcing all traffic to pass through the CDN (CloudFront) rather than accessing the S3 origin directly.
