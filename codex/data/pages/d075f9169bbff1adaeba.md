---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/suspicious-setspn-exe-execution
fetched_at: 2026-09-16T09:08:38Z
source: cortex-platform
---

# Suspicious setspn.exe execution | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 Suspicious setspn.exe execution 

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

 Credential Access (TA0006) 

 ATT&CK Technique 

 Steal or Forge Kerberos Tickets (T1558) 

 Severity 

 Low 

 Description 

 A Service Principal Name (SPN) is a unique identifier for a service, mapped to a specific account. Setspn.exe can be used to retrieve SPN information, which may indicate an attacker's attempt to "Kerberoast". 

 Attacker's Goals 

 Retrieving SPN information to perform related attacks like 'Kerberoast'. 

 Investigative actions 

 Investigate the user who executed setspn.exe and find out if the act was malicious. 

 Previous Suspicious sending domain with sender address randomization 

 Next Suspicious SMB connection from domain controller 

 Was this helpful?
