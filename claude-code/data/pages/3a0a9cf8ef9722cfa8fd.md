---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/abnormal-rpc-traffic-to-multiple-hosts
fetched_at: 2026-09-06T10:59:45Z
source: cortex-platform
---

# Abnormal RPC traffic to multiple hosts | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 Abnormal RPC traffic to multiple hosts 

 Synopsis 

 Field 

 Value 

 Activation Period 

 14 Days 

 Training Period 

 30 Days 

 Test Period 

 1 Hour 

 Deduplication Period 

 1 Day 

 Required Data 

 Requires one of the following data sources:
Palo Alto Networks Firewall EAL Logs OR XDR Agent with eXtended Threat Hunting (XTH) 

 ATT&CK Tactic 

 Reconnaissance (TA0043) 

 ATT&CK Technique 

 Active Scanning (T1595), Active Scanning: Vulnerability Scanning (T1595.002) 

 Severity 

 Low 

 Description 

 The endpoint performed unfamiliar RPC activity to multiple hosts. 

 Attacker's Goals 

 An adversary may enumerate different protocols to gain information and plan its lateral movement over the network. 

 Investigative actions 

 Check if the host is a newly deployed server that provides RPC based services to multiple hosts. 

 Verify the legitimacy of the actor process (and its causality) that initiated this RPC traffic. 

 Variations 
 Abnormal RPC traffic to multiple IPs 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Reconnaissance (TA0043) 

 ATT&CK Technique 

 Active Scanning (T1595), Active Scanning: Vulnerability Scanning (T1595.002) 

 Severity 

 Informational 

 Description 

 The endpoint performed unfamiliar RPC activity to multiple hosts. 

 Attacker's Goals 

 An adversary may enumerate different protocols to gain information and plan its lateral movement over the network. 

 Investigative actions 

 Check if the host is a newly deployed server that provides RPC based services to multiple hosts. 

 Verify the legitimacy of the actor process (and its causality) that initiated this RPC traffic. 

 Previous Abnormal Recurring Communications to a Rare Domain 

 Next Abnormal sensitive RPC traffic to multiple hosts from a rarely seen host 

 Was this helpful?
