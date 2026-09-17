---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/intense-sso-failures
fetched_at: 2026-09-16T09:07:13Z
source: cortex-platform
---

# Intense SSO failures | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 Intense SSO failures 

 Synopsis 

 Field 

 Value 

 Activation Period 

 14 Days 

 Training Period 

 30 Days 

 Test Period 

 10 Minutes 

 Deduplication Period 

 1 Day 

 Required Data 

 Requires one of the following data sources:
AzureAD OR Azure SignIn Log OR Idira OR Duo OR Okta OR OneLogin OR PingOne 

 Detection Modules 

 Identity Analytics 

 ATT&CK Tactic 

 Credential Access (TA0006), Initial Access (TA0001) 

 ATT&CK Technique 

 Valid Accounts (T1078), Brute Force: Password Spraying (T1110.003), Brute Force: Password Guessing (T1110.001) 

 Severity 

 Informational 

 Description 

 An abnormally high amount of SSO authentication attempts were seen within a short period of time. This could be the outcome of a brute-force login attempt. 

 Attacker's Goals 

 An attacker is attempting to gain access to an account secured with MFA. 

 Investigative actions 

 Check the legitimacy of this activity and determine whether it is malicious or not. 

 Check whether a successful login was made after unsuccessful attempts. 

 Variations 
 Intense SSO failures with suspicious characteristics 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Credential Access (TA0006), Initial Access (TA0001) 

 ATT&CK Technique 

 Valid Accounts (T1078), Brute Force: Password Spraying (T1110.003), Brute Force: Password Guessing (T1110.001) 

 Severity 

 Low 

 Description 

 An abnormally high amount of SSO authentication attempts were seen within a short period of time. This could be the outcome of a brute-force login attempt. 

 Attacker's Goals 

 An attacker is attempting to gain access to an account secured with MFA. 

 Investigative actions 

 Check the legitimacy of this activity and determine whether it is malicious or not. 

 Check whether a successful login was made after unsuccessful attempts. 

 Previous Installation of a new System-V service 

 Next Interactive at.exe privilege escalation method 

 Was this helpful?
