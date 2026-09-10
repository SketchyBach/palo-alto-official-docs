---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/a-user-logged-on-to-multiple-workstations-via-schannel
fetched_at: 2026-09-06T10:59:33Z
source: cortex-platform
---

# A user logged on to multiple workstations via Schannel | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 A user logged on to multiple workstations via Schannel 

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

 XDR Agent 

 Detection Modules 

 Identity Analytics 

 Detector Tags 

 Active Directory Certificate Services Analytics 

 ATT&CK Tactic 

 Persistence (TA0003), Privilege Escalation (TA0004), Credential Access (TA0006) 

 ATT&CK Technique 

 Account Manipulation (T1098), Valid Accounts (T1078), Steal or Forge Authentication Certificates (T1649) 

 Severity 

 Informational 

 Description 

 A user logged on to multiple workstations with a certificate via Schannel. This may be indicative of a compromised account. 

 Attacker's Goals 

 Elevate permissions and establish persistence. 

 Investigative actions 

 Verify the activity with the performing user. 

 Check for possible certificate authentications with the subject user. 

 Check if the user logged in to other endpoints via Schannel. 

 Variations 
 Rare user authentication with a certificate via Schannel 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Persistence (TA0003), Privilege Escalation (TA0004), Credential Access (TA0006) 

 ATT&CK Technique 

 Account Manipulation (T1098), Valid Accounts (T1078), Steal or Forge Authentication Certificates (T1649) 

 Severity 

 Low 

 Description 

 A rare user authentication with a certificate via Schannel was observed. This may be indicative of a compromised account. 

 Attacker's Goals 

 Elevate permissions and establish persistence. 

 Investigative actions 

 Verify the activity with the performing user. 

 Check for possible certificate authentications with the subject user. 

 Check if the user logged in to other endpoints via Schannel. 

 Abnormal authentication with a certificate via Schannel 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Persistence (TA0003), Privilege Escalation (TA0004), Credential Access (TA0006) 

 ATT&CK Technique 

 Account Manipulation (T1098), Valid Accounts (T1078), Steal or Forge Authentication Certificates (T1649) 

 Severity 

 Informational 

 Description 

 An abnormal authentication with a certificate via Schannel was observed. This may be indicative of a compromised account. 

 Attacker's Goals 

 Elevate permissions and establish persistence. 

 Investigative actions 

 Verify the activity with the performing user. 

 Check for possible certificate authentications with the subject user. 

 Check if the user logged in to other endpoints via Schannel. 

 Previous A user logged in to the AWS console for the first time 

 Next A user modified an Okta MFA factor 

 Was this helpful?
