---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/unusual-user-agent-for-a-cloud-identity
fetched_at: 2026-09-16T09:08:53Z
source: cortex-platform
---

# Unusual user-agent for a cloud identity | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 Unusual user-agent for a cloud identity 

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

 Requires one of the following data sources:
AWS Audit Log OR Azure Audit Log OR Gcp Audit Log 

 Detection Modules 

 Cloud 

 Detector Tags 

 OCI Analytics 

 ATT&CK Tactic 

 Initial Access (TA0001), Persistence (TA0003), Privilege Escalation (TA0004), Stealth (TA0005) 

 ATT&CK Technique 

 Valid Accounts: Cloud Accounts (T1078.004) 

 Severity 

 Informational 

 Description 

 A cloud identity has executed an API call with an unusual user-agent. 

 Attacker's Goals 

 Evade detection by using non-standard tools or scripts. 

 Investigative actions 

 Examine the recent actions of the user for any abnormal or unauthorized behavior. 

 Verify if the user intentionally used a new device or tool. 

 Variations 
 Unusual user-agent for a cloud identity by a compromised AWS access key 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Initial Access (TA0001), Persistence (TA0003), Privilege Escalation (TA0004), Stealth (TA0005) 

 ATT&CK Technique 

 Valid Accounts: Cloud Accounts (T1078.004) 

 Severity 

 Medium 

 Description 

 A cloud identity has executed an API call with an unusual user-agent. 

 Attacker's Goals 

 Evade detection by using non-standard tools or scripts. 

 Investigative actions 

 Examine the recent actions of the user for any abnormal or unauthorized behavior. 

 Verify if the user intentionally used a new device or tool. 

 Previous Unusual user account unlock 

 Next Unusual weak authentication by user 

 Was this helpful?
