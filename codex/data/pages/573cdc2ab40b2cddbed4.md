---
url: https://docs.paloaltonetworks.com/content/techdocs/en_US/enterprise-dlp/administration/monitor-enterprise-dlp/enterprise-dlp-incident-management.html
fetched_at: 2026-09-16T09:59:20Z
source: palo-alto-main
---

# Enterprise DLP Incident Management Clear

Updated on 

 Thu Sep 10 12:41:05 PDT 2026 

 Focus 

 Home 

 Enterprise DLP 

 Administration 

 Monitor Enterprise DLP 

 Enterprise DLP Incident Management 

 Download PDF 

 Enterprise DLP 

 Enterprise DLP Incident Management 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Enterprise DLP Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Reference 

 Release Notes 

 New Features by OS Version 

 New Features by Month 

 Previous 

 Monitor DLP Status with the DLP Health and Telemetry App 

 Next 

 Explore the Enterprise DLP Incident Management Dashboard 

 Enterprise DLP Incident Management 

 The Unified Incident Management and Response for Enterprise Data Loss Prevention (E-DLP) offers a
 powerful, unified solution for handling data security incidents across your organization. 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by Panorama or Strata Cloud Manager) 

 Prisma Access (Managed by Panorama or Strata Cloud Manager) 

 Prisma Browser 

 Enterprise Data Loss Prevention (E-DLP) license 

 Review the Supported
 Platforms for details on the required license
 for each enforcement point. 

 Or any of the following licenses that include the Enterprise DLP license 

 Prisma Access CASB license 

 Next-Generation
CASB for Prisma Access and NGFW (CASB-X) license 

 Data Security license 

 The Enterprise Data Loss Prevention (E-DLP) Incident Management and Response dashboard combines
 AI-powered threat detection, customizable response workflows, and real-time
 collaboration tools to dramatically reduce incident response times and minimize the
 impact of security breaches in your organization. It enhances collaboration among
 different members of your security teams, enabling faster and more coordinated responses
 to data security incidents. 

 The Incident Management and Response dashboard provides a structured approach to data
 security incident handling by consolidating incidents across Enterprise DLP , Email
 DLP, Endpoint DLP, SaaS Security Inline , Data Security , and Prisma Browser . This enables you to aggregate and correlate data security incidents
 across your various enforcement channels to efficiently apply a consistent security
 posture. The Incident Management and Response dashboard also enables you to validate
 adherence to your organization's regulatory compliance requirements by providing incident
 reports and audit trails. 

 With integrations across multiple data security channels, compliance reporting, and
 continuous improvement capabilities, the Incident Management and Response dashboard
 improves your overall security posture. It enables you to rapidly and effectively
 respond to data security incidents to protect your organization's sensitive data and
 assets. You and your SOC team can assign, escalate, and collaborate on incidents
 effectively, with support for bulk incident response and automated prioritization. The
 detailed incident triage capabilities help you significantly reduce the mean time to
 detect and respond to threats. The Incident Management and Response dashboard
 streamlines your investigation process and helps expedite response and remediation for
 Enterprise DLP incidents. 

 Enterprise DLP caches inspection results of forwarded files for up to 90 days to
 reduce latency for repeat file inspections. When an enforcement point forwards a file to
 Enterprise DLP , Enterprise DLP checks whether an identical file was
 previously inspected. If a cached report exists, Enterprise DLP returns the cached
 inspection result without performing a new scan. Enterprise DLP creates an incident
 regardless of whether the result comes from a new inspection or a cached report. Enterprise DLP returns a cached verdict when all of the following are true: 

 The file is from the same tenant. 

 The data profile hasn't changed (same profile ID and version). 

 The file content is identical (same file SHA regardless of filename). 

 Previous 

 Monitor DLP Status with the DLP Health and Telemetry App 

 Next 

 Explore the Enterprise DLP Incident Management Dashboard
