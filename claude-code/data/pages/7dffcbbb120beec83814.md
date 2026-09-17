---
url: https://docs.prismacloud.io/use-cases/secure-the-infrastructure/risk-prioritization
fetched_at: 2026-09-16T13:35:54Z
source: prisma-cloud
---

# Prioritize Risks | Prisma Cloud arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Enterprise Edition 

 Use Cases 

 Secure the Infrastructure 

 Prioritize Risks 

 In the public cloud, an organization's most vital assets are its Applications and Data . Their confidentiality, integrity, and availability are critical to business operations, competitive edge, and regulatory compliance. However, the enormous scale and intricate nature of cloud infrastructures introduce specialized security challenges, including an expanded attack surface that threatens these key assets. 

 Risk prioritization & Remediation serves as a cornerstone in cloud security strategy. It enables organizations to allocate resources efficiently, focusing on mitigating the most significant security issues first for robust protection. 

 A comprehensive risk assessment involves correlating a wide array of security signals, such as: 

 Internet exposure 

 Overly permissive or risky identities 

 Direct or Indirect access to sensitive data 

 Nature of the vulnerabilities present 

 Cloud misconfigurations 

 For example, an application with a specific vulnerability that is network exploitable may pose a critical or high risk if it is internet exposed and also has overly permissive IAM access to sensitive datastore. Conversely, the same vulnerability may present a lower risk if the asset is not internet exposed. 

 Prisma Cloud Risk prioritization capabilities are: 

 Incident Analysis : Refers to the automated process of examining and interpreting data such as events and logs to understand the nature, impact, and origin of a potential security incident. 

 Attack Path Analysis : Refers to the automated process of Identifying vulnerable assets/applications by correlating multiple security indicators, providing actionable security context to defend against high-risk threats. 

 Prisma Cloud Risk Remediation capabilities are: 

 Fix in Cloud - Automated remediation to help fix the problem at Runtime - by fixing the misconfig, apply virtual patch to a vulnerability. 

 Fix in Code - Automated remediation to prevent the problem from happening again by tracing to the source of the problem (code) and eliminating the root cause. 

 1. Review the most urgent issues 

 On the Prisma Cloud Home page, begin with the view into the urgent incidents and risks detected in the last 24 hours. 

 Alerts are split into Incidents, Attack Paths and Risks. 

 Incidents encompass all the alerts that are generated as a result of policy violations of type anomaly, Network, and Audit Event. These policy types deal with things that occur and represent a clear and present danger that they must urgently look at because it means that something bad has already occurred in their cloud environment. 

 Attack Path identifies exposed or vulnerable infrastructure assets, applications, or data by correlating multiple security signals. It indicates the likelihood of a breach that often requires immediate action. 

 Risks represent all the misconfigurations that currently exist in the customers cloud environment but they haven’t been exploited by a bad actor yet. 

 To help you prioritize, the urgency is shown to you on the Home Page itself. At a fundamental level, you should look to resolve Incidents first, then Attack Paths, before you look to resolve the Risks. In a lot of cases the Incidents and Attack Paths are sent over to the SOC team to investigate and resolve while the Risks are sent to the DevOps/DevSecOps team to resolve. 

 2. Review the alert details 

 Let's take the example of an Attack Path alert. 

 You can get more details when you View Attack Paths on the Home page.

 And that opens the Attack Path Visualization graph 

 In the above example, There is an EC2 role attached to a specific S3 bucket and clicking on the S3 bucket to gather additional information. 

 Review the findings to review all the findings with the S3 bucket and notice a Storage asset has sensitive data finding. 

 Then clicks on the object level information, to view the sensitive objects in the storage bucket. 

 With Data Security bringing in the data risk context in conjunction with the attack path alert, It’s now clear that the alert is not just a critical alert, but a high risk critical alert and needs to be addressed as soon as possible. 

 3. Fix the issue 

 Identifying critical risks is just the beginning. Prisma Cloud assists with eliminating the root cause through its unique code to cloud remediation capability. This approach not only helps security teams to act quickly but also addresses the issue at its source. 

 Code to cloud remediation helps allows you to: 

 Fix in Cloud : Fix risks immediately in the cloud which (OR) even better option 

 Fix in Code : Pinpoint at-risk assets/applications, and route remediations (e.g., via pull requests) back to their source so that issues are fixed permanently in code such as IaC templates, Terraform, AWS CloudFormation. 

 Previous Identify Identity Risks 

 Next Prioritize and Fix Vulnerabilities 

 Last updated 1 month ago 

 Was this helpful?
