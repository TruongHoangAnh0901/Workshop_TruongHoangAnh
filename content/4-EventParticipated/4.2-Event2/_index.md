---
title: "Event 2"
date: 2026-05-23
weight: 2
chapter: false
pre: " <b> 4.2. </b> "
---

# Event: AWS COMMUNITY DAY

**Date & Time:** 09:00 - 12:00, May 23, 2026  
**Location:** 26th Floor, Bitexco Tower, 02 Hai Trieu Street, Saigon Ward, Ho Chi Minh City  
**Role:** Attendee  

The AWS Community Day 2026 is a series of in-depth sharing sessions from leading experts, focusing on application modernization, DevOps, and practical applications of Generative AI. Below is a summary of the insights gained from the 6 key speakers:

### 1. GenAIOps Essential DevOps for Generative Applications — Context Is Everything
**Speaker:** Tinh Truong (Platform Engineer at GoTymeX)

- **The Importance of Context:** AI models are powerful, but their output is often limited by weak inputs (prompts) or a lack of context. Good context helps transform vague requests into accurately solvable tasks.
- **Common Mistakes in Providing Context:**
  - "Internet Puller" Error: Copying entire articles or long documents into the chatbot causes noise and increases token costs.
  - Providing Redundant Information: Repeating obvious facts the AI already knows instead of focusing on the next core requirement.
  - Lack of Goals and Constraints: Vague prompts (e.g., "Build a portfolio website") instead of clear criteria (React, Tailwind, Mobile-first UI).
- **The Evolution of AI Systems:** Shifting from single prompt queries to integrating foundational context and moving towards building long-term memory systems as a "Second AI Brain".
- **Career Advice:** The future is not a battle between humans and AI, but between those who know how to work with AI and those who don't. Highly encouraged building small projects like AI Study Assistants, PDF Chat Apps, or Source Code Review Systems.

### 2. UTMorpho — 36 hrs with LotusHacks: Building UTMorpho from Idea to Reality
**Speaker:** UTMorpho Team (Participants in LotusHacks 2026)

- **Reason for Participating:** To experience the pressure of Vietnam's largest hackathon (36 continuous hours), learn from other developers, and challenge the ability to turn ideas into a working demo.
- **Product Idea (UTMorpho):** Stemming from the frustration with current AI UI generation tools (having to re-prompt for minor changes, breaking the layout and wasting tokens), the team created UTMorpho — an AI Agent that allows generating UI from text descriptions and supports direct canvas editing (WYSIWYG).
- **The 36-Hour Implementation Process:** Covered stages from team formation, building the backend framework, developing core features (state synchronization between editor and AI), handling token limit bottlenecks, to final tuning and pitching.
- **Lessons Learned:** Practical ideas come from personal frustrations; high pressure sometimes requires breaks to trigger creativity; mutual trust in the team is more important than individual skills; and token cost is a major constraint when designing User Experience (UX).

### 3. Automate any business process using Amazon Quick Suite — Friendly AI Assistant w/ Amazon Quick
**Speaker:** Pham Nguyen Hai Anh (G-AsiaPacific Vietnam, AWS Community Builder)

- **The Reality of Enterprise Users:** Frequently dealing with repetitive, boring, and time-consuming administrative tasks such as collecting and analyzing information from multiple sources and synthesizing data.
- **Amazon Quick Suite Solution:** AWS introduces a next-generation enterprise AI solution, integrating internal data (Spaces, Datasets), world knowledge, web search capabilities, and over 40 Data connectors along with Bedrock models. The system ensures enterprise security and compliance (Governance, Guardrails, SOC 2, GDPR).
- **Practical Application (PM Assistant):** Completely automates processes such as generating Minutes of Meeting (MoM), sending emails to stakeholders, and auto-scheduling the next meeting.

### 4. CloudFront as Your Foundation — From Edge to Origin
**Speaker:** Nguyen Tuan Thinh (DevOps Engineer at First Cloud AI Journey - FCAJ)

- **New Flat-rate Pricing Model:** AWS recently launched this feature (on Nov 18), solving the drawbacks of the traditional "Pay as you go" model. The new model bundles CDN, WAF, Anti-DDoS, DNS, and S3 storage costs into a fixed monthly rate across different tiers (Free, Pro, Business, Premium), helping enterprises eliminate financial risks.
- **System Defense and Optimization Capabilities:**
  - Distributed DDoS Defense: Stops volumetric attacks right at the Edge locations closest to the source instead of waiting for traffic to penetrate deep into the system.
  - Cost and Performance Optimization: Caches data across a network of over 700 global PoPs. Enabling HTTP Compression reduces payload size by up to 82%. Utilizing HTTP/3 allows parallel loading of resources, accelerating response times.
  - Advanced Security: Supports mTLS (two-way authentication) for financial services, free TLS certificate management via ACM, and secure Origin cloaking solutions.

### 5. Enterprise-Grade Multi-Agent System — The Case of Startup Credit Scoring
**Speaker:** Vy Lam (Senior Business Systems Analyst at VPBank)

- **Data Incompatibility:** Traditional bank credit scoring systems require businesses to have long-term financial reports. Meanwhile, startups usually only operate for 6-18 months, causing older systems to reject them.
- **Multi-Agent Paradigm:** Instead of using a single AI Agent that is easily context-limited, the proposed solution builds a "Virtual Credit Council" comprising specialized Agents: Financial Analyst, Market Assessor, Founding Team Evaluator, Risk Controller, and Compliance Agent. This model enables cross-checking, parallel processing, and provides a clear audit trail.
- **Return on Investment (ROI):** The system cuts application processing time from 2-3 weeks down to 2-4 hours (95% faster), reduces 95% of specialist working hours, and saves significant decision-making costs.

### 6. Non-Determinism of "Deterministic" LLM Settings
**Speaker:** Duc Dao (Solution Architect at Cloud Kinetics)

- **The Myth of Determinism:** Many developers believe that setting the model temperature to 0 (temperature=0) will ensure the output is always perfectly identical for the same prompt.
- **Research Reality:** Testing across 5 major popular LLM models running through public endpoints showed that none achieved 100% consistency. Accuracy could deviate up to 15% between identical runs.
- **Core Causes:**
  - Technical: Floating-point arithmetic on GPUs is non-associative, and parallel processing threads have random execution orders.
  - Commercial: API providers batch requests from multiple users into a single processing run (Inference batching), altering the prompt's compute environment.
- **Mitigation Strategies:** Set temperature=0.1 (the sweet spot) instead of 0; apply a multiple-run and majority voting approach; design systems capable of handling probabilistic outcomes.

### Event Experience

Participating in "AWS COMMUNITY DAY 2026" was an excellent opportunity to immerse myself in the latest cloud computing and AI trends. The most practical values I gained include:

- **Expanding Generative AI Mindset:** Gained a deep understanding of how to provide optimal context for LLMs, as well as grasping the Multi-Agent Paradigm to solve complex enterprise problems like credit scoring.
- **Grasping Security & Infrastructure Practices:** Learning about CloudFront's new pricing model and Edge-to-Origin defense capabilities helped me shape a mindset for designing secure and cost-optimized systems.
- **Lessons from Real-world Projects:** Deeply inspired by the 36-hour hackathon journey to develop UTMorpho, and gained insights into the non-deterministic nature of LLMs to build more reliable AI systems.
- **Enterprise Application Orientation:** Understood how Amazon Quick Suite can automate business processes (like a PM Assistant), giving me a clearer perspective on how technology directly solves enterprise pain points.

### Event Photos

![Event 2](/images/event2-img1.png)
