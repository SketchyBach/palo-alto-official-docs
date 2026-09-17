---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/potential-creation-of-persistent-cloud-credentials
fetched_at: 2026-09-16T09:07:50Z
source: cortex-platform
---

# Potential creation of persistent cloud credentials | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 Potential creation of persistent cloud credentials 

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

 Persistence (TA0003), Credential Access (TA0006), Lateral Movement (TA0008) 

 ATT&CK Technique 

 Account Manipulation: Additional Cloud Credentials (T1098.001), Forge Web Credentials (T1606), Use Alternate Authentication Material: Application Access Token (T1550.001) 

 Severity 

 Informational 

 Description 

 A cloud identity invoked a credential-related persistence operation. 

 Attacker's Goals 

 Maintain persistence in cloud environments. 

 Investigative actions 

 Check what API calls were executed by the identity. 

 Check what resources are affected by this change. 

 Look for signs that the user account is compromised (e.g. abnormal logins, unusual activity). 

 Follow further actions done by the account. 

 Previous Possible webshell file written by a web server process 

 Next Potential DCSync by an unusual user 

 Was this helpful?
