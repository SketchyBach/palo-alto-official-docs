---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/a-lolbin-was-copied-to-a-different-location
fetched_at: 2026-09-16T09:05:41Z
source: cortex-platform
---

# A LOLBIN was copied to a different location | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 A LOLBIN was copied to a different location 

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

 6 Hours 

 Required Data 

 XDR Agent 

 ATT&CK Tactic 

 Stealth (TA0005) 

 ATT&CK Technique 

 Masquerading: Rename Legitimate Utilities (T1036.003) 

 Severity 

 Informational 

 Description 

 To evade detection, attackers may copy a LOLBIN executable to a different location. 

 Attacker's Goals 

 Command execution via lolbins and detection avoidance via file rename. 

 Investigative actions 

 Check whether the executing process is benign and if this was a desired behavior as part of its normal execution flow. 

 Check the destination path of the lolbin and try to see if it's benign. 

 Variations 
 A LOLBIN was copied to a different location using a rare command line 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Stealth (TA0005) 

 ATT&CK Technique 

 Masquerading: Rename Legitimate Utilities (T1036.003) 

 Severity 

 High 

 Description 

 To evade detection, attackers may copy a LOLBIN executable to a different location. 

 Attacker's Goals 

 Command execution via lolbins and detection avoidance via file rename. 

 Investigative actions 

 Check whether the executing process is benign and if this was a desired behavior as part of its normal execution flow. 

 Check the destination path of the lolbin and try to see if it's benign. 

 A LOLBIN was copied to a different location using a rare command line via a commonly used method 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Stealth (TA0005) 

 ATT&CK Technique 

 Masquerading: Rename Legitimate Utilities (T1036.003) 

 Severity 

 Low 

 Description 

 To evade detection, attackers may copy a LOLBIN executable to a different location. 

 Attacker's Goals 

 Command execution via lolbins and detection avoidance via file rename. 

 Investigative actions 

 Check whether the executing process is benign and if this was a desired behavior as part of its normal execution flow. 

 Check the destination path of the lolbin and try to see if it's benign. 

 Previous A Kubernetes StatefulSet was created 

 Next A machine certificate was issued with a mismatch 

 Was this helpful?
