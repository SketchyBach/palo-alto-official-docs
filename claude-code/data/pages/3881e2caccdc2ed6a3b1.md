---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/aws-backup-recovery-point-deletion
fetched_at: 2026-09-16T09:06:28Z
source: cortex-platform
---

# AWS Backup recovery point deletion | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 AWS Backup recovery point deletion 

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

 Impact (TA0040) 

 ATT&CK Technique 

 Inhibit System Recovery (T1490) 

 Severity 

 Informational 

 Description 

 An attempt was made to delete an AWS Backup recovery point. 

 Attacker's Goals 

 Adversaries may delete backup recovery points to prevent system recovery after compromise. 

 Investigative actions 

 Identify the deleted recovery point and its associated resource. 

 Investigate the identity that performed the deletion and review recent related activity. 

 Previous Autorun.inf created in root C drive 

 Next AWS Backup vault was deleted 

 Was this helpful?
