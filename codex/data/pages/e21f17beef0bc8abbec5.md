---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/aws-ssm-parameters-retrieval
fetched_at: 2026-09-06T11:01:05Z
source: cortex-platform
---

# AWS SSM parameters retrieval | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 AWS SSM parameters retrieval 

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

 Detector Tags 

 SSM Remote Management Analytics 

 ATT&CK Tactic 

 Credential Access (TA0006) 

 ATT&CK Technique 

 Credentials from Password Stores: Cloud Secrets Management Stores (T1555.006) 

 Severity 

 Informational 

 Description 

 An attempt was made to retrieve parameters stored in AWS SSM. 

 Attacker's Goals 

 Exfiltrate sensitive secrets stored in AWS SSM parameter store. 

 Investigative actions 

 Investigate the purpose of the encrypted parameter and assess the sensitivity of its contents. 

 Check if the access aligns with known workflows or automation, or if it indicates abnormal activity. 

 Variations 
 AWS SSM encrypted parameters retrieval 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Credential Access (TA0006) 

 ATT&CK Technique 

 Credentials from Password Stores: Cloud Secrets Management Stores (T1555.006) 

 Severity 

 Informational 

 Description 

 An attempt was made to retrieve encrypted parameters stored in AWS SSM. 

 Attacker's Goals 

 Exfiltrate sensitive secrets stored in AWS SSM parameter store. 

 Investigative actions 

 Investigate the purpose of the encrypted parameter and assess the sensitivity of its contents. 

 Check if the access aligns with known workflows or automation, or if it indicates abnormal activity. 

 Previous AWS SSM parameters discovery 

 Next AWS SSM send command attempt 

 Was this helpful?
