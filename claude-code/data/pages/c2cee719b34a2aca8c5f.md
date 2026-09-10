---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/a-user-modified-the-ca-audit-policy
fetched_at: 2026-09-06T10:59:36Z
source: cortex-platform
---

# A user modified the CA audit policy | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 A user modified the CA audit policy 

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

 Requires one of the following data sources:
Windows Event Collector OR XDR Agent with eXtended Threat Hunting (XTH) 

 Detection Modules 

 Identity Analytics 

 Detector Tags 

 Active Directory Certificate Services Analytics 

 ATT&CK Tactic 

 Defense Impairment (TA0112) 

 ATT&CK Technique 

 Disable or Modify Tools: Disable or Modify Windows Event Log (T1685.001) 

 Severity 

 Low 

 Description 

 A user modified the CA audit policy. 

 This may indicate that an attacker is attempting to cover their tracks before an AD CS attack. 

 Attacker's Goals 

 An attacker is attempting to cover their tracks before an AD CS attack. 

 Investigative actions 

 Check the user account modifying the CA audit policy and verify its activity. 

 Review AD CS logs to identify any unauthorized certificate issuances, modifications, or template changes. 

 Examine recent activity from the user account, including logon patterns and privilege changes. 

 Continue monitoring the account for any subsequent actions that may indicate suspicious behavior. 

 Previous A user modified an Okta policy rule 

 Next A user observed and reported unusual activity in Okta 

 Was this helpful?
