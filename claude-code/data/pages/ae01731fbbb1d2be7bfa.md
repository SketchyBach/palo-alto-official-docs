---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/suspicious-active-setup-registered
fetched_at: 2026-09-06T11:07:50Z
source: cortex-platform
---

# Suspicious active setup registered | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 Suspicious active setup registered 

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

 XDR Agent with eXtended Threat Hunting (XTH) 

 ATT&CK Tactic 

 Persistence (TA0003) 

 ATT&CK Technique 

 Boot or Logon Autostart Execution: Active Setup (T1547.014) 

 Severity 

 Informational 

 Description 

 The endpoint registered a new active setup, which may be used to gain persistence on the host by loading libraries into the time management service. 

 Attacker's Goals 

 Gain persistence using the legitimate windows active setup mechanism, which executes binary on system startup. 

 Investigative actions 

 Verify if the registered binary is malicious. 

 Check if the installing software is a malicious binary. 

 Previous Suspicious account attribute modification that matches that of another account 

 Next Suspicious activity indicating a potential abuse of a cloud-native email service 

 Was this helpful?
