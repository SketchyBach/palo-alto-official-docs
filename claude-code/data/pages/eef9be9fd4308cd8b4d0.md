---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/uncommon-dotnet-module-load-relationship
fetched_at: 2026-09-16T09:08:41Z
source: cortex-platform
---

# Uncommon DotNet module load relationship | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 Uncommon DotNet module load relationship 

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

 Reflective Code Loading (T1620) 

 Severity 

 Informational 

 Description 

 A signed process that usually doesn't use DotNet loaded a common DotNet module. 

 Attacker's Goals 

 Adversaries may reflectively load DotNet code into a process to conceal execution of malicious payloads. 

 Investigative actions 

 Investigate the actor process for potential malicious activity. 

 Check for recently installed services that may load DotNet modules. 

 Previous Uncommon DLL-sideloading from a logical CD-ROM (ISO) device 

 Next Uncommon driver loaded 

 Was this helpful?
