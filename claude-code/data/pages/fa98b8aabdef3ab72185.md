---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/local-group-enumeration
fetched_at: 2026-09-06T11:05:09Z
source: cortex-platform
---

# Local group enumeration | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 Local group enumeration 

 Synopsis 

 Field 

 Value 

 Activation Period 

 14 Days 

 Training Period 

 30 Days 

 Test Period 

 5 Minutes 

 Deduplication Period 

 1 Day 

 Required Data 

 Requires one of the following data sources:
Windows Event Collector OR XDR Agent with eXtended Threat Hunting (XTH) 

 Detection Modules 

 Identity Analytics 

 ATT&CK Tactic 

 Discovery (TA0007) 

 ATT&CK Technique 

 Permission Groups Discovery: Local Groups (T1069.001), Permission Groups Discovery (T1069) 

 Severity 

 Informational 

 Description 

 A user performed an enumeration on local groups to retrieve their details. 

 Attacker's Goals 

 An adversary may leverage local groups discovery to identify privileged groups and escalate privileges. 

 Investigative actions 

 Determine the user, hostname, and process that performed the group enumeration. 

 Inspect process, command-line arguments or scripts used. 

 Check for any privilege escalation or lateral movement attempts from the source system. 

 Check if the tool used to enumerate the local groups is a known or an approved tool. 

 Review the logs for suspicious activity from the same host or user. 

 Variations 
 Local group enumeration for the first time 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Discovery (TA0007) 

 ATT&CK Technique 

 Permission Groups Discovery: Local Groups (T1069.001), Permission Groups Discovery (T1069) 

 Severity 

 Low 

 Description 

 A user performed an enumeration on local groups to retrieve their details. 

 Attacker's Goals 

 An adversary may leverage local groups discovery to identify privileged groups and escalate privileges. 

 Investigative actions 

 Determine the user, hostname, and process that performed the group enumeration. 

 Inspect process, command-line arguments or scripts used. 

 Check for any privilege escalation or lateral movement attempts from the source system. 

 Check if the tool used to enumerate the local groups is a known or an approved tool. 

 Review the logs for suspicious activity from the same host or user. 

 Local group enumeration using a builtin Windows binary 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Discovery (TA0007) 

 ATT&CK Technique 

 Permission Groups Discovery: Local Groups (T1069.001), Permission Groups Discovery (T1069) 

 Severity 

 Informational 

 Description 

 A user performed an enumeration on local groups to retrieve their details. 

 Attacker's Goals 

 An adversary may leverage local groups discovery to identify privileged groups and escalate privileges. 

 Investigative actions 

 Determine the user, hostname, and process that performed the group enumeration. 

 Inspect process, command-line arguments or scripts used. 

 Check for any privilege escalation or lateral movement attempts from the source system. 

 Check if the tool used to enumerate the local groups is a known or an approved tool. 

 Review the logs for suspicious activity from the same host or user. 

 Previous Local group enumeration via RPC 

 Next Local user account creation by a machine account 

 Was this helpful?
