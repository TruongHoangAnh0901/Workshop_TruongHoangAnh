---
title: "Week 7 Worklog"
date: 2024-01-01
weight: 7
chapter: false
pre: " <b> 1.7. </b> "
---

### Week 7 Objectives:

* Learn about Asynchronous Architecture models.
* Research the Amazon SQS message queueing service.
* Practice connecting SQS with Lambda to process heavy background workloads.

---

### Tasks implemented:

| Day | Task | Start Date | Completion Date | Reference/Material |
| --- | ---- | ---------- | --------------- | ------------------ |
| Mon | Learn how to process **background jobs** to prevent the website from lagging during high traffic. | 01/06/2026 | 01/06/2026 | |
| Tue | Understand message queueing concepts and set up **Amazon SQS** queues. | 02/06/2026 | 02/06/2026 | |
| Wed | Practice integrating **SQS with Lambda** to process messages asynchronously. | 03/06/2026 | 03/06/2026 | |
| Thu | Research **Lambda triggers** and event-driven architecture within AWS. | 04/06/2026 | 04/06/2026 | |
| Fri | Implement background processing for the Quiz App's **score calculation system**. | 05/06/2026 | 05/06/2026 | |

---

### Achievements:

* Upgraded the Quiz App system to an advanced Event-Driven architecture:
  * Successfully integrated **Amazon SQS** as a buffer for incoming user requests.
  * Used SQS as a Trigger to activate **AWS Lambda** for smooth background score calculation.
* The system can now handle heavy traffic much better (Decoupled architecture):
  * The website no longer freezes or times out when thousands of students submit exams simultaneously.
  * Mastered concepts of Visibility Timeout and Dead Letter Queue in error handling.
