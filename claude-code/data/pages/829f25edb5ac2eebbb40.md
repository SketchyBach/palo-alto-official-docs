---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/iam-user-added-to-an-iam-group
fetched_at: 2026-09-16T09:07:45Z
source: cortex-platform
---

# IAM User added to an IAM group | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 IAM User added to an IAM group 

 Synopsis 

 Field 

 Value 

 Activation Period 

 14 Days 

 Training Period 

 30 Days 

 Test Period 

 N/A (single event) 

 Deduplication Period 

 1 Day 

 Required Data 

 AWS Audit Log 

 Detection Modules 

 Cloud 

 ATT&CK Tactic 

 Privilege Escalation (TA0004), Persistence (TA0003) 

 ATT&CK Technique 

 Valid Accounts: Cloud Accounts (T1078.004), Account Manipulation: Additional Cloud Roles (T1098.003) 

 Severity 

 Informational 

 Description 

 An IAM user was added to an IAM group. 

 Attacker's Goals 

 Add a user to a group to establish persistence or escalate privileges within a cloud account. 

 Investigative actions 

 Identify the identity that executed the API call. 

 Determine which IAM user was added to the group. 

 Evaluate the group's permissions to determine their applicability to the IAM user. 

 Previous IAM role was created 

 Next Identity assigned an Azure AD Administrator Role 

 Was this helpful?
