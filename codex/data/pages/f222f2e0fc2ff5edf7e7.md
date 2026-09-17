---
url: https://cortex-docs.paloaltonetworks.com/application-security/application-security-posture-management-aspm/application-security-posture-management-aspm
fetched_at: 2026-09-16T08:49:04Z
source: cortex-platform
---

# What is Application Security Posture Management (ASPM) | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center shield-alt

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Application Security 

 Application Security Posture Management (ASPM) 

 What is Application Security Posture Management (ASPM) 

 ASPM centralizes AppSec monitoring across the SDLC. It aggregates findings from tools such as IaC and SCA to provide a holistic view and prioritize risks. 

 Application Security Posture Management (ASPM) centralizes and automates the continuous monitoring, evaluation, and enhancement of application security across the entire software lifecycle, from initial code development through deployment and ongoing operations in cloud and on-premises environments. 

 ASPM functions as a unified governance layer. It aggregates, correlates, and assesses security signals and findings from application security testing tools (such as SAST and SCA) and other data sources, providing a holistic, real-time, and actionable view of an organization's application security landscape, addressing fragmented visibility, siloed teams, inefficient resource allocation, and delayed remediation. 

 ASPM enables you to create logical groupings of related components and SDLC assets, for example, source repositories, services, and their runtime workloads, into applications . An application is the unit you scope monitoring, prioritization, and remediation around, focused on the assets that carry the greatest business risk. Refer to Applications for more information. 

 Note 

 ASPM does not execute scans. Detection and finding generation belong to Code Security scanners (native scanners) and the Supply Chain Security pillar (VCS repository and CI/CD pipeline analysis). ASPM evaluates the findings against unified policies and orchestrates the resulting issues through to remediation. 

 Use cases 

 The primary use cases for the ASPM platform include: 

 Comprehensive visibility : Gain a holistic, unified view of your application security posture across all stages of your software development lifecycle (SDLC): 

 Applications : insights into the SDLC of your critical business applications 

 Code to cloud : Visualize and understand the relationship between your source code and deployed cloud resources, enabling you to identify and prioritize risks associated with your deployments 

 Third-party ingestion : Integrate security findings from third-party scanners and security tools to gain a centralized view of your security posture and correlate findings across your development lifecycle 

 Coverage and prevention metrics : Scanner coverage across assets, prevention rates at policy gates, and posture changes over time 

 Contextual risk prioritization and proactive detection : Prioritize remediation efforts ranked by Urgency based on a data-driven risk assessment that combines code-level vulnerabilities, runtime behaviors, and infrastructure configurations to determine actual exploitability 

 Effective prevention : Block risks at PR, CI, and periodic scan from a single unified policy definition, stopping issues before they reach production 

 Actionable remediation : Improve your security posture with actionable remediation guidance for identified security risks. Cortex Cloud offers automated remediation for IaC misconfigurations and CVE vulnerabilities, in addition to clear steps for manual fixes for all categories of detected risks 

 How ASPM works 

 Findings, from native scanners or third-party ingestion, are evaluated against unified policies. When policy conditions are met, they become issues, which the Urgency engine then classifies using code to cloud deployment context, and business context where applications are defined. You can then remediate issues individually or through a case. 

 aspm-workflow3.png 

 Key features 

 The Cortex Cloud ASPM solution provides the following key features to help you gain comprehensive control over your application security posture: 

 Command center : A central dashboard providing a real-time overview of your organization's Application Security program, including security coverage, issue distribution (total, prevented, prioritized), and identification of riskiest applications 

 Code to cloud context : Provides end-to-end visibility by mapping code-level issues (such as IaC misconfigurations and CVEs) to deployed assets and runtime issues, enabling full lifecycle insight from development through CI/CD to production 

 Coverage : Provides detailed visibility into the security monitoring status of Application Security assets (such as VCS repositories and CI/CD pipelines) by security scanners, highlighting coverage percentages, gaps, and scanner success/failure rates 

 Application builder : Facilitates the definition and management of applications, automatically discovering and associating all relevant assets across the SDLC (from code to cloud) to provide a centralized and holistic view of application risk 

 Unified Application Security policies : Single policy framework that governs findings from every detection scanner and applies consistently across PR, CI, and periodic scan trigger 

 Application side card : Offers a unified, high-level summary of risks across the full application lifecycle, aggregating insights from multiple security domains, displaying key risk metrics, and showing application topology 

 Urgency : Context-aware prioritization framework that classifies issues into Top Urgent, Urgent, Not Urgent, and Not Applicable tiers using exploit intelligence (EPSS, CISA KEV), code to cloud context, business criticality, scanner-specific signals, and runtime protection status 

 Third-party ingestion : Ingest findings from third-party scanners directly into the platform under the same policies and Urgency 

 Workflows 

 You can manage and automate the ASPM across the following interfaces. 

 Surface 

 Use for 

 Primary persona 

 Tenant (UI) 

 Posture review, policy management, issue triage, Command Center, and application creation 

 AppSec manager, practitioner 

 API 

 Bulk policy operations, issue retrieval, third-party ingestion, and automated integrations 

 AppSec practitioner, DevSecOps 

 CLI 

 Scan-time policy consumption, local finding evaluation, and CI/CD guardrail enforcement 

 DevSecOps, AppSec practitioner 

 Terraform 

 Codification of policies, rules, criteria, and integrations 

 DevSecOps, platform engineer 

 Roles and permissions 

 The AppSec Admin role is the dedicated user role for ASPM, granting full permissions for all application security-related activities. They can create and modify detection rules within the Code/Build domain, track progress, and adjust enforcements as needed. Additionally, they can triage and investigate findings, issues, and cases spanning from code to cloud. The role also includes complete visibility into all cloud assets. 

 Permissions assigned to the AppSec Admin role cannot be modified. However, you can save this role as a new custom role which can then be edited to meet specific organizational needs, offering a balance between standardized roles and customizable access control. 

 You can view AppSec Admin permissions in the tenant by navigating to Settings → Configurations → Roles → AppSec Admin . 

 Previous Page Reference F: Call-to-action routing by asset type1 

 Next ASPM Command Center 

 Last updated 1 month ago 

 Was this helpful?
