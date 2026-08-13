---
url: https://docs.paloaltonetworks.com/ai-access-security/release-notes/limitations
fetched_at: 2026-08-12T14:06:06Z
source: ai-security
---

# Limitations Clear

Limitations 

 Home 

 EN

 Location 

 Documentation Home 

 Palo Alto Networks 

 Support 

 Live Community 

 Knowledge Base 

 >

 Strata Copilot

 Limitations 

 Updated on 

 Fri May 29 13:54:12 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 AI Access Security Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Release Notes 

 New Features 

 Updated on 

 Fri May 29 13:54:12 PDT 2026 

 Focus 

 Home 

 AI Access Security 

 Release Notes 

 Limitations 

 Download PDF 

 AI Access Security 

 Limitations 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 AI Access Security Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Release Notes 

 New Features 

 Previous 

 Addressed Issues 

 Limitations 

 Review the limitations for AI Access Security . 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by Panorama or Strata Cloud Manager) 

 Prisma Access (Managed by Panorama or Strata Cloud Manager) 

 Prisma Browser 

 Strata Logging Service license 

 One of the following: 

 AI Access Security license 

 CASB-PA license 

 CASB-X license 

 Prisma Browser standalone license 

 Review the limitations in AI Access Security . 

 Feature 

 Limitation ID 

 Description 

 AI Access Security Recommendations 

 ADI-42500 

 In some cases, Security policy rules listed in the
 Review Policy Rules Blocking Sanctioned or
 Tolerated GenAI Apps recommendation might include
 Security policy rules blocking access to Sanctioned and Tolerated
 GenAI apps even though traffic for those apps was already
 allowed. 

 For example, you create Allow-Rule that
 allows traffic to Sanctioned-App1 and
 Tolerated-App2 . You order
 Allow-Rule at the top of your
 Security policy rulebase so traffic to these allowed GenAI apps is
 evaluated first. 

 You also create Deny-Rule using an application filter to
 block traffic to all other GenAI apps not explicitly allowed by your
 organization. This application filter dynamically groups all GenAI
 apps so it includes Sanctioned-App1 and
 Tolerated-App2 . You place this
 Security policy rule at the bottom of your Security policy rulebase
 so it's evaluated last. 

 In this case, the Review Policy Rules Blocking
 Sanctioned or Tolerated GenAI Apps recommendation
 lists Deny-Rule as blocking access to
 your Sanctioned and Tolerated GenAI apps even though traffic to
 these apps was already evaluated against
 Allow-Rule and allowed. 

 AI Access Security Sensitive Data Assets 

 — 

 Data Discrepancies 

 The Sensitive Data Assets count on the AI Access Security Dashboard is based on
 pre-aggregated data and may not match the count in Enterprise DLP Data Asset Explorer. 

 Enterprise DLP Data Asset Explorer reflects
 real-time on-the-fly aggregation and is the
 authoritative source for current asset counts. 

 Previous 

 Addressed Issues 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Strata Logging Service 

 Identity and Access Management 

 Next-Generation Firewalls 

 AIOps for NGFW 

 Firewalls 

 PAN-OS 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 AI-Powered ADEM 

 Prisma Access Monitoring and Visibility 

 Next-Generation CASB 

 Cloud-Delivered Security Services 

 Advanced Threat Prevention 

 Enterprise DLP 

 SaaS Security 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Release Notes 

 AI Access Security 

 Cloud-Delivered Security Services 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
