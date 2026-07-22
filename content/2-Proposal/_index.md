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

## 1. Project Overview
**Galaxy Brain** is an online quiz application developed as an academic capstone project. The application focuses on core business logic, ensuring stable operation for a limited user base (grading instructors and a test group). The system is designed with a "Minimalist" approach, deployed entirely using a **Serverless** architecture on AWS with a priority on ease of management and absolute cost optimization.

### Technology Stack
| Category | Technology | Purpose |
| :--- | :--- | :--- |
| **Frontend** | React, Vite, S3, CloudFront | High-speed user interface, global static hosting. |
| **Compute** | AWS Lambda, API Gateway | Run Backend application (FastAPI) automatically without virtual servers. |
| **Database** | Amazon DynamoDB | Serverless NoSQL database with auto-scaling. |
| **Security** | IAM Role, Secrets Manager, OAC | Strict least-privilege permissions, S3 & Token security. |
| **CI/CD** | GitHub Actions | Automated build and deployment. |

---

## 2. Objectives
### General Objective
Successfully complete a full-stack academic project from Frontend/Backend coding to Cloud (AWS) deployment. Ensure the product runs smoothly during the live demo for the evaluation committee.

### Specific Objectives
- Successfully deploy the application on AWS using a modern **Serverless** architecture.
- Maximize the use of AWS Free Tier services (like Lambda, DynamoDB) to bring operational costs close to $0.
- Complete a comprehensive and easy-to-follow Deployment Walkthrough documentation.

---

## 3. Problem Statement & Target Audience
### Problem Statement
In academic projects, students often waste too much time configuring complex AWS infrastructure (like VPCs, NAT Gateways, Load Balancers), resulting in insufficient time to perfect features or losing points due to system errors during demos. Galaxy Brain solves this by using a **Cloud-Native Serverless Architecture**, bypassing traditional server management to focus 100% on "Making it work correctly."

### Target Audience
- Grading instructors and the academic evaluation committee.
- Students in the application testing group.

---

## 4. System Architecture
The architecture diagram below describes the Serverless Data Flow of Galaxy Brain.

![System Architecture](/images/architecture.png)

---

## 5. Timeline
| Phase | Duration | Tasks |
| :---: | :---: | :--- |
| **Phase 1** | Week 1 - 3 | Requirements analysis, UI design, DynamoDB Table provisioning. |
| **Phase 2** | Week 4 - 6 | Backend (FastAPI) and Frontend (React) coding. |
| **Phase 3** | Week 7 - 9 | Backend deployment to AWS Lambda via API Gateway. |
| **Phase 4** | Week 10 - 12| Frontend deployment to S3/CloudFront, finalizing capstone documentation. |

---

## 6. Budget
Estimated AWS Monthly Cost - Student Optimized:

| AWS Service | Configuration | Estimated Cost/Month |
| :--- | :--- | :---: |
| **AWS Lambda & API Gateway** | Free Tier (Millions of free requests) | $0.00 |
| **Amazon DynamoDB** | Free Tier (25GB free storage) | $0.00 |
| **Amazon S3 & CloudFront**| Static hosting & Low bandwidth | ~$1.00 |
| **VPC & Network** | Serverless architecture (No NAT Gateway) | $0.00 |
| **Summary** | | **~$1.00** |

---

## 7. Risk Assessment
| Risk | Probability | Mitigation Plan |
| :--- | :---: | :--- |
| **Cold Start Latency** | Medium | FastAPI on Lambda might be slow on the first request. Mitigated by using appropriate RAM configuration (1024MB) to boost speed. |
| **Overload during high user traffic** | Low | AWS Lambda and DynamoDB scale infinitely, zero risk of server crash. |
| **Billing Shock from repeated API calls**| Low | Setup AWS Budgets to alert via Email if costs exceed $5. |
