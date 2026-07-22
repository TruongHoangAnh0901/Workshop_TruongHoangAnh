---
title: "Blog 2"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 3.2. </b> "
---

# AMAZON CLOUDFRONT INTRODUCES ORIGIN ACCESS CONTROL (OAC)

Securing Amazon CloudFront origins, particularly Amazon S3 buckets, is a top-priority security requirement for any workload running on AWS. Previously, AWS provided a feature called Origin Access Identity (OAI) to restrict S3 access so that users could only retrieve files through CloudFront, effectively blocking direct Internet access. However, over time, OAI revealed certain limitations regarding advanced security capabilities and feature support.

To comprehensively address these constraints, AWS officially launched **Origin Access Control (OAC)**. This technical blog post provides an in-depth look and explains in detail why OAC has become the new security standard, highlighting its outstanding improvements:

1.  **Enhanced Security & Confused Deputy Prevention:** 
OAC utilizes robust IAM authentication mechanisms with short-term credentials. Furthermore, it requires explicitly specifying the Amazon Resource Name (ARN) of the permitted CloudFront distribution. This completely prevents privilege escalation attacks such as the "confused deputy" problem, ensuring your S3 bucket cannot be accessed by a CloudFront distribution belonging to a malicious AWS account.

2.  **SSE-KMS Encryption Support:** 
One of the most significant weaknesses of OAI was its lack of support for downloading or uploading objects encrypted with AWS Key Management Service (KMS). OAC resolves this issue, allowing payload encryption to safely comply with the strictest enterprise security standards.

3.  **Comprehensive HTTP Method Support:** 
Unlike OAI, which was primarily optimized for static reads, OAC supports all standard HTTP methods including GET, PUT, POST, PATCH, DELETE, OPTIONS, and HEAD. This opens up possibilities for building bidirectional, interactive applications seamlessly through CloudFront.

4.  **Expanded Support Capabilities (Beyond S3):** 
Moving beyond just Amazon S3, the OAC mechanism has been architected by AWS to expand security support to other origins, such as Lambda Function URLs and potentially more services in the future.

Migrating from OAI to OAC is currently an essential best practice that cloud engineers must adopt when architecting and deploying web applications to guarantee the absolute security of static source code and assets.

![CloudFront OAC](/images/cloudfront-oac.png)

### Original Article Link
**[Read the full article on AWS Networking Blog](https://aws.amazon.com/blogs/networking-and-content-delivery/amazon-cloudfront-introduces-origin-access-control-oac/)**