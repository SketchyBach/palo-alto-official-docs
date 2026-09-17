---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/suspicious-secrets-dump-activity
fetched_at: 2026-09-16T09:08:37Z
source: cortex-platform
---

# Suspicious secrets dump activity | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 Suspicious secrets dump activity 

 Synopsis 

 Field 

 Value 

 Activation Period 

 14 Days 

 Training Period 

 30 Days 

 Test Period 

 1 Hour 

 Deduplication Period 

 5 Days 

 Required Data 

 Requires one of the following data sources:
AWS Audit Log OR Azure Audit Log OR Gcp Audit Log 

 Detection Modules 

 Cloud 

 ATT&CK Tactic 

 Credential Access (TA0006), Collection (TA0009) 

 ATT&CK Technique 

 Unsecured Credentials (T1552), Data from Cloud Storage (T1530), Credentials from Password Stores: Cloud Secrets Management Stores (T1555.006) 

 Severity 

 Informational 

 Description 

 An identity dumped multiple secrets from the project, considerably more than usual. This may indicate an attacker's attempt to dump sensitive information from the cloud environment. 

 Attacker's Goals 

 Collect secrets from the cloud environment. 

 Investigative actions 

 Check the accessed secrets' designation. 

 Verify that the identity did not dump any sensitive information that it shouldn't. 

 Variations 
 An identity extracted every secret within the organization across multiple regions 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Credential Access (TA0006), Collection (TA0009) 

 ATT&CK Technique 

 Unsecured Credentials (T1552), Data from Cloud Storage (T1530), Credentials from Password Stores: Cloud Secrets Management Stores (T1555.006) 

 Severity 

 Medium 

 Description 

 An identity dumped multiple secrets from the project, considerably more than usual. This may indicate an attacker's attempt to dump sensitive information from the cloud environment. 

 Attacker's Goals 

 Collect secrets from the cloud environment. 

 Investigative actions 

 Check the accessed secrets' designation. 

 Verify that the identity did not dump any sensitive information that it shouldn't. 

 An identity extracted multiple secrets within the organization across multiple regions 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Credential Access (TA0006), Collection (TA0009) 

 ATT&CK Technique 

 Unsecured Credentials (T1552), Data from Cloud Storage (T1530), Credentials from Password Stores: Cloud Secrets Management Stores (T1555.006) 

 Severity 

 Low 

 Description 

 An identity dumped multiple secrets from the project, considerably more than usual. This may indicate an attacker's attempt to dump sensitive information from the cloud environment. 

 Attacker's Goals 

 Collect secrets from the cloud environment. 

 Investigative actions 

 Check the accessed secrets' designation. 

 Verify that the identity did not dump any sensitive information that it shouldn't. 

 Previous Suspicious SearchProtocolHost.exe parent process 

 Next Suspicious sender exhibiting automated sending patterns 

 Was this helpful?
