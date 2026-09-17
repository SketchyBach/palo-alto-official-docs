---
url: https://docs.prismacloud.io/release-notes/prisma-cloud-release-information/classic-releases/prisma-cloud-code-security-release-information/features-introduced-in-code-security-march-2023
fetched_at: 2026-09-16T13:36:09Z
source: prisma-cloud
---

# Features Introduced in March 2023 | Prisma Cloud arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Enterprise Edition 

 Release Notes 

 Prisma Cloud Release Information 

 Classic Releases 

 Prisma Cloud Code Security Release Information 

 Features Introduced in March 2023 

 Learn about the new Code Security capabilities on Prisma® Cloud Enterprise Edition (SaaS) in March 2023. 

 The following new features or enhancements are available for Prisma Cloud Code Security. These capabilities help agile teams add security checks to their existing IaC (Infrastructure-as-Code) model and enforce security throughout the build lifecycle. 

 New Features 

 Policy Updates 

 New Features 

 FEATURE 

 DESCRIPTION 

 Custom Prisma Cloud Permission group for Code Security capabilities 

 As a part of custom Prisma Cloud roles for Code Security, administrators can now define explicit permissions for Code Security workflows from Permission Group (Settings > Access Control > Add > Permission Group) . In addition to the existing System Admin permission you can define roles for: 

 View access Permissions: Provide view access for Code Security Configuration, Projects, Supply Chain and Development Pipelines pages. 

 Repository permissions: Provide integrate, view, update and delete access to Repositories. 

 Enhancements to Audit Logs 

 In addition to the existing Audit Logs (Settings > Audit Logs) , you can now see a list of all actions initiated by Prisma Cloud administrators on Code Security. The actions on the Audit Logs help you identify any configuration changes and activities initiated on the repositories behalf of the administrator. Here are the kind of actions you can track. 

 Suppression Management : Creating or deleting a suppression rule for the default branch on Projects (Code Security > Projects) 

 Enforcement : Adding a new Enforcement rule or reconfiguring an existing Enforcement rule by editing or deleting the rule. This also includes modifying the default thresholds of Enforcement parameters. 

 Repository : Addition, deletion and updating integrated repositories. 

 Secrets Scanning on Git History 

 In addition to the current scans run on your repositories, Prisma Cloud now scans Git history to find exposed secrets that are deleted from code. You can view the scan results in the resource block on Projects (Code Security > Projects) , Secrets code category view. On Resource Explorer, you can also see the commit history on when the secret was added or removed. 

 Policy Updates 

 POLICY UPDATES 

 DESCRIPTION 

 AWS EBS volume region with encryption is disabled 

 Changes- The Build remediation instructions are being updated. 

 Impact- No impact on Code Security findings. 

 Basic Auth Credentials 

 Changes- The policy name is being updated. 

 Current Policy Name- Basic Authentication Credentials 

 Impact- No impact on Code Security findings. 

 Policy Deletions 

 AWS EC2 instance is not configured with VPC 

 Changes- This policy is deleted because resources are configured in VPC by default. 

 Impact- Code Security findings for this policy will no longer be surfaced in scans. 

 My SQL server enables public network access (duplication of CKV_AZURE_53) 

 Changes- This policy is a duplication of an existing policy, therefore will be deleted. 

 Impact- Code Security findings for this policy will no longer be surfaced in scans. 

 Previous Features Introduced in April 2023 

 Next Features Introduced in February 2023 

 Last updated 2 months ago 

 Was this helpful?
