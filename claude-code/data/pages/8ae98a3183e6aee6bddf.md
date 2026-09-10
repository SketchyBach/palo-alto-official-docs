---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/aws-support-case-creation
fetched_at: 2026-09-06T11:01:07Z
source: cortex-platform
---

# AWS support case creation | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 AWS support case creation 

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

 5 Days 

 Required Data 

 AWS Audit Log 

 Detection Modules 

 Cloud 

 ATT&CK Tactic 

 Discovery (TA0007), Privilege Escalation (TA0004) 

 ATT&CK Technique 

 Cloud Infrastructure Discovery (T1580), Account Manipulation (T1098) 

 Severity 

 Informational 

 Description 

 A cloud identity has created a new case in AWS support. 

 Attacker's Goals 

 Obtaining a list of resources that could be targeted for lateral movement or convincing AWS's support to perform actions on their behalf. 

 Investigative actions 

 Investigate any unusual activity originating from the suspected identity. View the contents of the newly created case {case_id} . 

 Previous AWS STS temporary credentials were generated 

 Next AWS Systems Manager hosts enumeration 

 Was this helpful?
