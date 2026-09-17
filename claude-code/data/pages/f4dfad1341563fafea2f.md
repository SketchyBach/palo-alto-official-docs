---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-5.x/reference-and-developer-docs/role-based-access-control/configuration-permissions/access-management-permissions
fetched_at: 2026-09-16T08:43:10Z
source: cortex-platform
---

# Access management permissions | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR 

 Cortex XDR 5.x Documentation 

 Reference and developer docs 

 Role-Based Access Control 

 Configuration permissions 

 Cortex XDR 5.x 

 Access management permissions 

 Configure permissions for user access and role management. 

 Set permissions for Users, Roles, User Groups, and Authentication Settings under Access Management ( Settings → Configurations → Access Management ). 

 Caution 

 SSO Configuration Risk: Granting View/Edit access allows users to modify the tenant's Single Sign-On (SSO) and authentication settings. Misconfigurations can cause tenant-wide lockouts. Ensure only authorized identity or infrastructure administrators hold this permission. 

 Auditing is Mandatory: It is highly recommended that any user managing access also has visibility into the Auditing module to track changes. 

 IT Admin: Unlike other modules, IT Admins require full View/Edit access here for user provisioning and SSO duties. 

 Permission 

 Description 

 Roles Example 

 None 

 No access to Access Management. 

 SOC Tier-1 and 2 Analysts and Threat Hunter: No need to manage users or roles. 

 View 

 Read-only access to users, roles, and groups. 

 SOC Tier-3 Analyst: May need to understand team structure. 

 Security Engineer: Should understand role structure but not manage users 

 View/Edit 

 Full access to create, modify, and delete users, roles, and groups, including configuring SSO settings. 

 Note 
Users with this permission are restricted from granting, modifying, or removing the Instance Administrator role for any user, user group, or API key, and cannot delete API keys that have this role. 

 Required and recommended permissions 

 Consider adding the following permissions: 

 Permission 

 Permission Level 

 Reason 

 Auditing 

 View 

 Track user and role changes for compliance; critical for access control audit trails. Strongly recommended. 

 Cases & Issues 

 View 

 Understand case workflows when configuring role permissions for case management. Recommended. 

 General Configuration 

 View 

 System settings context when managing platform access. Recommended. 

 Dashboards 

 Enabled 

 View user activity dashboards and access patterns. Recommended. 

 Query Center 

 View 

 Query user activity data for access reviews. Recommended. 

 Previous Cortex XDR Analytics permissions 

 Next Data Broker permissions 

 Last updated 15 days ago 

 Was this helpful?
