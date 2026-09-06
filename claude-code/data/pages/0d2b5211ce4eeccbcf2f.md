---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/office-process-spawned-with-suspicious-command-line-arguments
fetched_at: 2026-09-06T11:05:49Z
source: cortex-platform
---

# Office process spawned with suspicious command-line arguments | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 Office process spawned with suspicious command-line arguments 

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

 Stealth (TA0005) 

 ATT&CK Technique 

 Process Injection: Process Hollowing (T1055.012) 

 Severity 

 Low 

 Description 

 An Office process was executed with LOLBIN-like command-line arguments. This behavior is exhibited in the VBA-RunPE tool that executes executables from the memory of Word/Excel/PowerPoint. 

 Attacker's Goals 

 Execute arbitrary code or run malicious applications undetected. 

 Investigative actions 

 Check the file that spawns the office application and search for macros, formulas, or scripts. 

 Variations 
 Masqueraded office process spawned with suspicious command-line arguments 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Stealth (TA0005) 

 ATT&CK Technique 

 Process Injection: Process Hollowing (T1055.012), Masquerading (T1036) 

 Severity 

 Medium 

 Description 

 An executable masquerading an office process was executed with LOLBIN-like command-line arguments. 

 Attacker's Goals 

 Execute arbitrary code or run malicious applications undetected. 

 Investigative actions 

 Check the file that spawns the office application and search for macros, formulas, or scripts. 

 PowerPoint process accesses a suspicious PPAM file 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Stealth (TA0005) 

 ATT&CK Technique 

 Process Injection: Process Hollowing (T1055.012) 

 Severity 

 Low 

 Description 

 A PowerPoint process opened a PPAM file which might be used to execute malicious code. 

 Attacker's Goals 

 Execute arbitrary code or run malicious applications undetected. 

 Investigative actions 

 Check the file that spawns the office application and search for macros, formulas, or scripts. 

 Previous Office process accessed an unusual .LNK file 

 Next Okta account reset password attempt 

 Was this helpful?
