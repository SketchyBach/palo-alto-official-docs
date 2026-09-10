---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/unusual-aws-credentials-creation
fetched_at: 2026-09-06T11:09:44Z
source: cortex-platform
---

# Unusual AWS credentials creation | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 Unusual AWS credentials creation 

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

 XDR Agent 

 ATT&CK Tactic 

 Persistence (TA0003) 

 ATT&CK Technique 

 Account Manipulation: Additional Cloud Credentials (T1098.001) 

 Severity 

 Low 

 Description 

 AWS utility was used to create an access key and a secret key. 

 Attacker's Goals 

 Maintain access to an AWS provider. 

 Investigative actions 

 Check the machine timeline and look for abnormal activity. 

 Investigate what other calls were made to the AWS account. 

 Previous Unusual AWS CLI/SDK activity 

 Next Unusual AWS S3 objects deletion 

 Was this helpful?
