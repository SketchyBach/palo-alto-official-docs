---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/a-tcp-stream-was-created-directly-in-a-shell
fetched_at: 2026-09-16T09:06:12Z
source: cortex-platform
---

# A TCP stream was created directly in a shell | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 A TCP stream was created directly in a shell 

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

 Execution (TA0002) 

 ATT&CK Technique 

 Command and Scripting Interpreter (T1059) 

 Severity 

 Medium 

 Description 

 Attackers may create a TCP stream using the shell command line to generate a reverse shell, enabling remote access to the endpoint. 

 Attacker's Goals 

 Attackers may use this device file to create sockets though shell commands as part of a reverse shell. 

 Investigative actions 

 Review the command line used. 

 Search for the corresponding network event. 

 Check the prevalence of the target IP/domain. 

 Previous A suspicious process queried AD CS objects via LDAP 

 Next A third-party application's access to the Google Workspace domain's resources was revoked 

 Was this helpful?
