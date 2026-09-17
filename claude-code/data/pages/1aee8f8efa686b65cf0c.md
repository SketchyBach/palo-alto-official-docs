---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/cloud-email-sending-was-enabled
fetched_at: 2026-09-16T09:06:41Z
source: cortex-platform
---

# Cloud email sending was enabled | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 Cloud email sending was enabled 

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

 Resource Development (TA0042) 

 ATT&CK Technique 

 Compromise Accounts: Email Accounts (T1586.002) 

 Severity 

 Informational 

 Description 

 Cloud email sending was enabled for the cloud account. 

 Attacker's Goals 

 Use the existing account to send phishing or spread malware. 

 Investigative actions 

 Check if the identity has performed any email-related operations in the past. 

 Check if this account should be used for email sending. 

 Variations 
 Cloud email sending was enabled by an unusual identity 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Resource Development (TA0042) 

 ATT&CK Technique 

 Compromise Accounts: Email Accounts (T1586.002) 

 Severity 

 Low 

 Description 

 Cloud email sending was enabled for the cloud account. The identity was not seen performing any operations in SES in the last 30 days. 

 Attacker's Goals 

 Use the existing account to send phishing or spread malware. 

 Investigative actions 

 Check if the identity has performed any email-related operations in the past. 

 Check if this account should be used for email sending. 

 Previous Cloud email infrastructure enumeration activity 

 Next Cloud email service activity 

 Was this helpful?
