---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/aws-user-creation
fetched_at: 2026-09-06T11:01:10Z
source: cortex-platform
---

# AWS user creation | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 AWS user creation 

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

 Persistence (TA0003) 

 ATT&CK Technique 

 Create Account: Cloud Account (T1136.003) 

 Severity 

 Informational 

 Description 

 A new AWS user was created. 

 Attacker's Goals 

 Maintaining persistence by creating backdoor users or malicious resources, ensuring ongoing access even if their initial entry is detected. 

 Investigative actions 

 Check which user was created. 

 Investigate the created user role and permissions. 

 Verify the user who created the new identity is aware of this action. 

 Be aware of any suspicious activity originating from the new user. 

 Previous AWS Transfer Family server created 

 Next AWS web ACL deletion 

 Was this helpful?
