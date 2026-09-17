---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/a-user-was-added-to-a-windows-security-group
fetched_at: 2026-09-16T09:06:05Z
source: cortex-platform
---

# A user was added to a Windows security group | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 A user was added to a Windows security group 

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

 Requires one of the following data sources:
Windows Event Collector OR XDR Agent with eXtended Threat Hunting (XTH) 

 Detection Modules 

 Identity Analytics 

 ATT&CK Tactic 

 Persistence (TA0003), Privilege Escalation (TA0004) 

 ATT&CK Technique 

 Account Manipulation (T1098), Valid Accounts (T1078) 

 Severity 

 Informational 

 Description 

 A user was added to a Windows security group. 

 Attacker's Goals 

 Privilege escalation using a valid account. 

 Investigative actions 

 Check the user who added the account to the group and verify its activity. 

 Variations 
 User added a member to a Windows privileged group for the first time 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Persistence (TA0003), Privilege Escalation (TA0004) 

 ATT&CK Technique 

 Account Manipulation (T1098), Valid Accounts (T1078) 

 Severity 

 Medium 

 Description 

 A user was added to a Windows security privileged group. 

 Attacker's Goals 

 Privilege escalation using a valid account. 

 Investigative actions 

 Check the user who added the account to the group and verify its activity. 

 User added to a Windows privileged group 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Persistence (TA0003), Privilege Escalation (TA0004) 

 ATT&CK Technique 

 Account Manipulation (T1098), Valid Accounts (T1078) 

 Severity 

 Low 

 Description 

 A user was added to a Windows security privileged group. 

 Attacker's Goals 

 Privilege escalation using a valid account. 

 Investigative actions 

 Check the user who added the account to the group and verify its activity. 

 User removed from a Windows privileged group 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Persistence (TA0003), Privilege Escalation (TA0004) 

 ATT&CK Technique 

 Account Manipulation (T1098), Valid Accounts (T1078) 

 Severity 

 Informational 

 Description 

 A user was removed from a Windows security privileged group. 

 Attacker's Goals 

 Privilege escalation using a valid account. 

 Investigative actions 

 Check the user who removed the account from the group and verify its activity. 

 A user was removed from a Windows security group 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Persistence (TA0003), Privilege Escalation (TA0004) 

 ATT&CK Technique 

 Account Manipulation (T1098), Valid Accounts (T1078) 

 Severity 

 Informational 

 Description 

 A user was removed from a Windows security group. 

 Attacker's Goals 

 Privilege escalation using a valid account. 

 Investigative actions 

 Check the user who removed the account from the group and verify its activity. 

 Previous A user uploaded malware to SharePoint or OneDrive 

 Next A WMI subscriber was created 

 Was this helpful?
