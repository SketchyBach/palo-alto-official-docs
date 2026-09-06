---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/possible-dll-search-order-hijacking
fetched_at: 2026-09-06T11:06:12Z
source: cortex-platform
---

# Possible DLL Search Order Hijacking | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 Possible DLL Search Order Hijacking 

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

 Detector Tags 

 DLL Hijacking Analytics 

 ATT&CK Tactic 

 Stealth (TA0005) 

 ATT&CK Technique 

 Hijack Execution Flow: DLL (T1574.001), Hijack Execution Flow: Path Interception by PATH Environment Variable (T1574.007), Hijack Execution Flow: Path Interception by Unquoted Path (T1574.009), Hijack Execution Flow: Path Interception by Search Order Hijacking (T1574.008) 

 Severity 

 Low 

 Description 

 An attacker might abuse the Windows DLL search order to trigger known, signed processes to load the attacker's malicious module. 

 Attacker's Goals 

 An attacker is attempting to load an untrusted module into a trusted context to avoid detection, gain persistence or to perform privilege escalation. 

 Investigative actions 

 Investigate the loaded module to verify if it is malicious. 

 Investigate if the loading process and the loaded module reside in legitimate locations. 

 Variations 
 Possible DLL Search Order Hijacking by DLL Substitution 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Stealth (TA0005) 

 ATT&CK Technique 

 Hijack Execution Flow: DLL (T1574.001), Hijack Execution Flow: Path Interception by PATH Environment Variable (T1574.007), Hijack Execution Flow: Path Interception by Unquoted Path (T1574.009), Hijack Execution Flow: Path Interception by Search Order Hijacking (T1574.008), Masquerading (T1036), Masquerading: Match Legitimate Resource Name or Location (T1036.005) 

 Severity 

 Low 

 Description 

 An attacker might abuse the Windows DLL search order to trigger known, signed processes to load the attacker's malicious module. 

 Attacker's Goals 

 An attacker is attempting to load an untrusted module into a trusted context to avoid detection, gain persistence or to perform privilege escalation. 

 Investigative actions 

 Investigate the loaded module to verify if it is malicious. 

 Investigate if the loading process and the loaded module reside in legitimate locations. 

 Possible DLL Search Order Hijacking - DLL extracted from an internet-downloaded archive 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Stealth (TA0005) 

 ATT&CK Technique 

 Hijack Execution Flow: DLL (T1574.001), Hijack Execution Flow: Path Interception by PATH Environment Variable (T1574.007), Hijack Execution Flow: Path Interception by Unquoted Path (T1574.009), Hijack Execution Flow: Path Interception by Search Order Hijacking (T1574.008) 

 Severity 

 Low 

 Description 

 An attacker might abuse the Windows DLL search order to trigger known, signed processes to load the attacker's malicious module. 

 Attacker's Goals 

 An attacker is attempting to load an untrusted module into a trusted context to avoid detection, gain persistence or to perform privilege escalation. 

 Investigative actions 

 Investigate the loaded module to verify if it is malicious. 

 Investigate if the loading process and the loaded module reside in legitimate locations. 

 Possible DLL Search Order Hijacking - DLL downloaded from an uncommon source 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Stealth (TA0005) 

 ATT&CK Technique 

 Hijack Execution Flow: DLL (T1574.001), Hijack Execution Flow: Path Interception by PATH Environment Variable (T1574.007), Hijack Execution Flow: Path Interception by Unquoted Path (T1574.009), Hijack Execution Flow: Path Interception by Search Order Hijacking (T1574.008) 

 Severity 

 Low 

 Description 

 An attacker might abuse the Windows DLL search order to trigger known, signed processes to load the attacker's malicious module. 

 Attacker's Goals 

 An attacker is attempting to load an untrusted module into a trusted context to avoid detection, gain persistence or to perform privilege escalation. 

 Investigative actions 

 Investigate the loaded module to verify if it is malicious. 

 Investigate if the loading process and the loaded module reside in legitimate locations. 

 Previous Possible DLL Hijack into a Microsoft process 

 Next Possible Email collection using Outlook RPC 

 Was this helpful?
