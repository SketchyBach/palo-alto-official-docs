---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/lolbas-executable-injects-into-another-process
fetched_at: 2026-09-16T09:07:23Z
source: cortex-platform
---

# LOLBAS executable injects into another process | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 LOLBAS executable injects into another process 

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

 Injection Analytics 

 ATT&CK Tactic 

 Stealth (TA0005) 

 ATT&CK Technique 

 Process Injection (T1055) 

 Severity 

 Informational 

 Description 

 A signed binary, which can be abused to run code, injected code to another process. 

 Attacker's Goals 

 Gain code execution on the host and evade security controls. 

 Investigative actions 

 Check whether the injecting process is benign, and if this was a desired behavior as part of its normal execution flow. 

 Variations 
 LOLBAS executable injects into another process under an uncommon CGO 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Stealth (TA0005) 

 ATT&CK Technique 

 Process Injection (T1055) 

 Severity 

 Low 

 Description 

 A signed binary, which can be abused to run code, injected code to another process. 

 Attacker's Goals 

 Gain code execution on the host and evade security controls. 

 Investigative actions 

 Check whether the injecting process is benign, and if this was a desired behavior as part of its normal execution flow. 

 Previous Logs were not collected from a data source for an abnormally long time 

 Next LOLBIN created a PSScriptPolicyTest PowerShell script file 

 Was this helpful?
