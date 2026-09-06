---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/execution-of-an-uncommon-process-with-a-local-domain-user-sid-at-early-startup-by-a-system-binary
fetched_at: 2026-09-06T11:20:22Z
source: cortex-platform
---

# Execution of an uncommon process with a local/domain user SID at early startup by a system binary | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 Execution of an uncommon process with a local/domain user SID at early startup by a system binary 

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

 Generic Persistence Analytics 

 ATT&CK Tactic 

 Persistence (TA0003) 

 ATT&CK Technique 

 Boot or Logon Autostart Execution (T1547) 

 Severity 

 Low 

 Description 

 Execution of an uncommon process with a local/domain user SID at early startup by a system binary may be an indication of a persistent mechanism on boot that is being actively abused. 

 Attacker's Goals 

 Attackers aim to get persistence to continue operating even after a reboot. 

 Investigative actions 

 Check if the Causality Group Owner (CGO) has a related persistence mechanism that may have been abused by an attacker. 

 Variations 
 Execution of an uncommon process with a local/domain user SID at early startup by a system binary - Explorer CGO 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Persistence (TA0003) 

 ATT&CK Technique 

 Boot or Logon Autostart Execution (T1547) 

 Severity 

 Informational 

 Description 

 Execution of an uncommon process with a local/domain user SID at early startup by a system binary may be an indication of a persistent mechanism on boot that is being actively abused. 

 Attacker's Goals 

 Attackers aim to get persistence to continue operating even after a reboot. 

 Investigative actions 

 Check if the user is responsible for the action process creation; otherwise, examine the Run//RunOnce (Autoruns) registry keys for possible persistence. 

 Execution of an uncommon process with a local/domain user SID at early startup with suspicious characteristics 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Persistence (TA0003) 

 ATT&CK Technique 

 Boot or Logon Autostart Execution (T1547) 

 Severity 

 Low 

 Description 

 Execution of an uncommon process with a local/domain user SID at early startup by a system binary may be an indication of a persistent mechanism on boot that is being actively abused. 

 Attacker's Goals 

 Attackers aim to get persistence to continue operating even after a reboot. 

 Investigative actions 

 Check if the Causality Group Owner (CGO) has a related persistence mechanism that may have been abused by an attacker. 

 Execution of an uncommon process with a local/domain user SID at early startup with uncommon characteristics 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Persistence (TA0003) 

 ATT&CK Technique 

 Boot or Logon Autostart Execution (T1547) 

 Severity 

 Low 

 Description 

 Execution of an uncommon process with a local/domain user SID at early startup by a system binary may be an indication of a persistent mechanism on boot that is being actively abused. 

 Attacker's Goals 

 Attackers aim to get persistence to continue operating even after a reboot. 

 Investigative actions 

 Check if the Causality Group Owner (CGO) has a related persistence mechanism that may have been abused by an attacker. 

 Previous Execution of an uncommon process with a local/domain user SID at an early startup stage 

 Next Execution of command from within a Kubernetes pod using kubelet credentials 

 Was this helpful?
