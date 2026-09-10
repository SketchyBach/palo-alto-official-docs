---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/suspicious-runonce-exe-parent-process
fetched_at: 2026-09-06T11:08:27Z
source: cortex-platform
---

# Suspicious runonce.exe parent process | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 Suspicious runonce.exe parent process 

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

 Persistence (TA0003) 

 ATT&CK Technique 

 Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder (T1547.001) 

 Severity 

 Low 

 Description 

 Runonce.exe executes commands under the Registry key HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce, typically on computer boot and user logon events. 

 Attacker's Goals 

 Command execution and persistence on the host. 

 Investigative actions 

 Check whether the executing process is benign and if this was a desired behavior as part of its normal execution flow. 

 Previous Suspicious reconnaissance using LDAP 

 Next Suspicious RunOnce Parent Process 

 Was this helpful?
