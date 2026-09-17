---
url: https://cortex-docs.paloaltonetworks.com/application-security/application-security-posture-management-aspm/backlog-baseline/using-backlog
fetched_at: 2026-09-16T08:49:10Z
source: cortex-platform
---

# Using Backlog | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center shield-alt

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Application Security 

 Application Security Posture Management (ASPM) 

 Backlog baseline 

 Using Backlog 

 You can leverage the Backlog and New issue classifications across the platform as follows. 

 Role-Based Access Control (RBAC) / Standard-Based Access Control (SBAC) : Access and permissions will be managed systematically: 

 By default, only AppSec Admins have permission to configure the issues on existing SBOM are considered new setting 

 The Are SBOM issues considered new setting controls how SBOM-originated findings are classified against the Backlog/New baseline. This setting is disabled by default, meaning that SBOM findings that existed before the initial baseline scan are classified as Backlog, while only SBOM findings detected after the baseline are classified as New. When enabled, all SBOM findings are treated as New regardless of when they were first detected. Only users with the AppSec Admin role can view and modify this setting. To configure, navigate to Settings → Configuration → Application Security → AppSec Issues Configurations and enable Are SBOM issues considered new 

 Permissions for all other capabilities, such as viewing issues or applying policies, are defined by the existing RBAC/SBAC policies and the user's specific issue management capabilities 

 Policies/Scope : The system supports Backlog and New attributes for policies, allowing for differentiated enforcement. Refer to Create a policy for more information 

 Multi-Branch Support : The Backlog/New classification is consistent across development workflows: 

 The Backlog/New classification is maintained independently for every branch 

 The system allows policies to be defined and applied for specific branches, enabling you to tailor security rules (for example, enforcing stricter policies for New critical issues on main branches, or allowing Backlog issues on development branches) based on their classification 

 You can filter the Cortex Cloud Application Security dashboard to display information according to the Backlog/New classification 

 Issues and Findings : The Backlog/New classification is standardized across data for both findings and issues under the Backlog Status field, which is found under the Overview tab of both findings and issues side cards. For example, refer to Navigate to secrets issues 

 Previous Issue/Finding classification by scanner 

 Next Service Lead Agreements (SLA) 

 Last updated 1 month ago 

 Was this helpful?
