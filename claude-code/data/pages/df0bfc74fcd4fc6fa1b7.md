---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/suspicious-ntlm-authentication-with-machine-account
fetched_at: 2026-09-16T09:08:32Z
source: cortex-platform
---

# Suspicious NTLM authentication with machine account | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 Suspicious NTLM authentication with machine account 

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
Palo Alto Networks Firewall EAL Logs OR XDR Agent 

 Detection Modules 

 Identity Analytics 

 ATT&CK Tactic 

 Credential Access (TA0006) 

 ATT&CK Technique 

 Forced Authentication (T1187) 

 Severity 

 Informational 

 Description 

 A suspicious NTLM authentication attempt was made by a machine account. 

 Attacker's Goals 

 An attacker aims to exploit authentication protocols to steal credentials and enable lateral movement within the network. 

 Investigative actions 

 Identify the source and target users and hosts involved in the NTLM authentication attempt. 

 Monitor the users associated with the authentication for any further suspicious activities or unauthorized actions. 

 Look for earlier connections to the source which may cause it to initiate the session. 

 Investigate the root cause of the behavior and determine if it can be mitigated or blocked in the future. 

 Variations 
 Rare and sensitive NTLM authentication with machine account 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Credential Access (TA0006) 

 ATT&CK Technique 

 Forced Authentication (T1187) 

 Severity 

 Low 

 Description 

 A rare and sensitive NTLM authentication attempt was made by a machine account. 

 Attacker's Goals 

 An attacker aims to exploit authentication protocols to steal credentials and enable lateral movement within the network. 

 Investigative actions 

 Check for signs of data exfiltration from any internet-facing destination server. 

 Identify the source and target users and hosts involved in the NTLM authentication attempt. 

 Monitor the users associated with the authentication for any further suspicious activities or unauthorized actions. 

 Look for earlier connections to the source which may cause it to initiate the session. 

 Investigate the root cause of the behavior and determine if it can be mitigated or blocked in the future. 

 Previous Suspicious Network Connection Originating from AWS SSM Agent 

 Next Suspicious objects encryption in an AWS bucket 

 Was this helpful?
