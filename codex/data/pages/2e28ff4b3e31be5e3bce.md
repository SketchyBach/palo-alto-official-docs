---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/autorun-inf-created-in-root-c-drive
fetched_at: 2026-09-06T11:00:49Z
source: cortex-platform
---

# Autorun.inf created in root C drive | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 Autorun.inf created in root C drive 

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

 Lateral Movement (TA0008), Execution (TA0002) 

 ATT&CK Technique 

 Hijack Execution Flow: Services File Permissions Weakness (T1574.010), Replication Through Removable Media (T1091) 

 Severity 

 Medium 

 Description 

 An autorun file installed at the root of a C:\ drive is suspicious, as autorun files are typically associated with removable drives. 

 Attacker's Goals 

 The Autorun and AutoPlay components of Microsoft Windows operating systems may use 'Autorun.inf' to automatically execute a program (without user interaction). Adversaries can manipulate this mechanism to run a malicious program. 

 Investigative actions 

 Read the content of the 'Autorun.inf' file from the root directory folder of the drive (the file may be hidden). 

 Previous Authentication method was added to Azure account 

 Next AWS Backup recovery point deletion 

 Was this helpful?
