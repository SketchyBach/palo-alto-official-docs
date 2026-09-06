---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/suspicious-modification-of-the-adminsdholder-s-acl
fetched_at: 2026-09-06T11:08:16Z
source: cortex-platform
---

# Suspicious modification of the AdminSDHolder's ACL | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 Suspicious modification of the AdminSDHolder's ACL 

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

 Persistence (TA0003) 

 ATT&CK Technique 

 Account Manipulation (T1098) 

 Severity 

 Low 

 Description 

 A user modified the AdminSDHolder ACL, which may be an indication of a privilege escalation attack. 

 Attacker's Goals 

 Attackers attempt to obtain full control privileges and then move laterally. 

 Investigative actions 

 Check if a new user was added to the AdminSDHolder object. 

 Check if a suspicious user account was recently created. 

 Check if a user was added to a privileged group (e.g. Domain Admins). 

 Investigate any other potentially suspicious behavior from the compromised user. 

 Search for actions that may trigger SDProp, such as modifying the registry or executing an LDAP query. 

 Previous Suspicious ML Model Download 

 Next Suspicious module load using direct syscall 

 Was this helpful?
