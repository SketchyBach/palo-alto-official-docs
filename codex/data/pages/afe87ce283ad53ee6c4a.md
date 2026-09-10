---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/globally-uncommon-root-domain-from-a-signed-process
fetched_at: 2026-09-06T11:03:54Z
source: cortex-platform
---

# Globally uncommon root domain from a signed process | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 Globally uncommon root domain from a signed process 

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

 Global Anomaly Analytics 

 ATT&CK Tactic 

 Stealth (TA0005), Command and Control (TA0011) 

 ATT&CK Technique 

 System Binary Proxy Execution (T1218), Application Layer Protocol (T1071) 

 Severity 

 Low 

 Description 

 A signed process connected to an external domain that, on a global level, it usually doesn't connect to. 

 Attacker's Goals 

 Attackers may use various methods to execute code in the context of a signed process to avoid detection. 

 Investigative actions 

 Check the destination domain reputation. 

 Check if the actor process loaded a suspicious dll before the alert. 

 Check if the actor process was injected before the alert. 

 Check if the process execution and connections are legitimate. 

 Variations 
 Globally uncommon root domain from an injected thread in a signed process 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Stealth (TA0005), Command and Control (TA0011) 

 ATT&CK Technique 

 System Binary Proxy Execution (T1218), Application Layer Protocol (T1071), Process Injection (T1055) 

 Severity 

 High 

 Description 

 An injected thread in a signed process connected to an external domain that, on a global level, it usually doesn't connect to. 

 Attacker's Goals 

 Attackers may use various methods to execute code in the context of a signed process to avoid detection. 

 Investigative actions 

 Check the destination domain reputation. 

 Check if the actor process loaded a suspicious dll before the alert. 

 Check if the actor process was injected before the alert. 

 Check if the process execution and connections are legitimate. 

 Globally uncommon root domain from a signed process 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Stealth (TA0005), Command and Control (TA0011) 

 ATT&CK Technique 

 System Binary Proxy Execution (T1218), Application Layer Protocol (T1071) 

 Severity 

 High 

 Description 

 A signed process connected to an external domain that, on a global level, it usually doesn't connect to. 

 Attacker's Goals 

 Attackers may use various methods to execute code in the context of a signed process to avoid detection. 

 Investigative actions 

 Check the destination domain reputation. 

 Check if the actor process loaded a suspicious dll before the alert. 

 Check if the actor process was injected before the alert. 

 Check if the process execution and connections are legitimate. 

 Globally uncommon root domain from a signed process 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Stealth (TA0005), Command and Control (TA0011) 

 ATT&CK Technique 

 System Binary Proxy Execution (T1218), Application Layer Protocol (T1071) 

 Severity 

 High 

 Description 

 A signed process connected to an external domain that, on a global level, it usually doesn't connect to. 

 Attacker's Goals 

 Attackers may use various methods to execute code in the context of a signed process to avoid detection. 

 Investigative actions 

 Check the destination domain reputation. 

 Check if the actor process loaded a suspicious dll before the alert. 

 Check if the actor process was injected before the alert. 

 Check if the process execution and connections are legitimate. 

 Globally uncommon root domain from a signed process 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Stealth (TA0005), Command and Control (TA0011) 

 ATT&CK Technique 

 System Binary Proxy Execution (T1218), Application Layer Protocol (T1071) 

 Severity 

 Medium 

 Description 

 A signed process connected to an external domain that, on a global level, it usually doesn't connect to. 

 Attacker's Goals 

 Attackers may use various methods to execute code in the context of a signed process to avoid detection. 

 Investigative actions 

 Check the destination domain reputation. 

 Check if the actor process loaded a suspicious dll before the alert. 

 Check if the actor process was injected before the alert. 

 Check if the process execution and connections are legitimate. 

 Previous Globally uncommon process execution from a signed process 

 Next Globally uncommon root-domain port combination by a common process (sha256) 

 Was this helpful?
