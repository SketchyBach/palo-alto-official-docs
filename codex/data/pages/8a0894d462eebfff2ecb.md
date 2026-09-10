---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/failed-login-for-locked-out-account
fetched_at: 2026-09-06T11:03:07Z
source: cortex-platform
---

# Failed Login For Locked-Out Account | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 Failed Login For Locked-Out Account 

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
Palo Alto Networks Firewall traffic Logs OR XDR Agent 

 ATT&CK Tactic 

 Stealth (TA0005) 

 ATT&CK Technique 

 Valid Accounts (T1078) 

 Severity 

 Informational 

 Description 

 A locked-out user account (event ID 4725 or 4740) was used in a Kerberos TGT pre-authentication attempt. 

 Attacker's Goals 

 Authenticate using the principal in the TGT, not knowing that it has been revoked. 

 Investigative actions 

 Check whether you have issues with your Cloud Identity Engine failing to sync data from Active Directory. 

 Check whether the attempt to use the principals (user accounts) specified in the alert are legitimate. For example, a user or a script that was not updated that the account has been revoked. 

 The lockout can be temporary, for example, in the case of too many login attempts, and may not be visible after the account was released. 

 Search for Windows Event Log 4740 to ascertain whether the account was locked out during the time of the alert. 

 Previous Failed Login For a Long Username With Special Characters 

 Next File transfer from unusual IP using known tools 

 Was this helpful?
