---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/internal-login-password-spray
fetched_at: 2026-09-16T09:07:17Z
source: cortex-platform
---

# Internal Login Password Spray | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 Internal Login Password Spray 

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

 ATT&CK Tactic 

 Credential Access (TA0006) 

 ATT&CK Technique 

 Brute Force: Password Spraying (T1110.003) 

 Severity 

 Informational 

 Description 

 An abnormally high amount of user account login attempts were seen from a host within a short period of time. This may have resulted from a login password spray attack. 

 Attacker's Goals 

 An attacker may be attempting to gain unauthorized access to user accounts. 

 Investigative actions 

 Check the amount of time in between each authentication attempt. 

 Investigate the reason behind the login failures and if any accounts were locked out. 

 Look for any successful authentication attempts and the ratio of login success versus login failures. 

 Monitor for potential abuse of MFA on users who have successfully logged in. 

 Variations 
 Suspicious intensive and short internal Login Password Spray 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Credential Access (TA0006) 

 ATT&CK Technique 

 Brute Force: Password Spraying (T1110.003) 

 Severity 

 Medium 

 Description 

 An abnormally high number of login attempts within a very short period of time and suspicious automated behavior. 

 Attacker's Goals 

 An attacker may be attempting to gain unauthorized access to user accounts. 

 Investigative actions 

 Check the amount of time in between each authentication attempt. 

 Investigate the reason behind the login failures and if any accounts were locked out. 

 Look for any successful authentication attempts and the ratio of login success versus login failures. 

 Monitor for potential abuse of MFA on users who have successfully logged in. 

 High-Volume Internal Password Spray Attack 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Credential Access (TA0006) 

 ATT&CK Technique 

 Brute Force: Password Spraying (T1110.003) 

 Severity 

 Medium 

 Description 

 Over 500 user accounts failed to login within a short period of time. 

 Attacker's Goals 

 An attacker may be attempting to gain unauthorized access to user accounts. 

 Investigative actions 

 Check the amount of time in between each authentication attempt. 

 Investigate the reason behind the login failures and if any accounts were locked out. 

 Look for any successful authentication attempts and the ratio of login success versus login failures. 

 Monitor for potential abuse of MFA on users who have successfully logged in. 

 Internal Login Password Spray with many wrong password attempts 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Credential Access (TA0006) 

 ATT&CK Technique 

 Brute Force: Password Spraying (T1110.003) 

 Severity 

 Low 

 Description 

 An abnormally high amount of user account login attempts with wrong password were seen with a wrong password within a short period of time. 

 Attacker's Goals 

 An attacker may be attempting to gain unauthorized access to user accounts. 

 Investigative actions 

 Check the amount of time in between each authentication attempt. 

 Investigate the reason behind the login failures and if any accounts were locked out. 

 Look for any successful authentication attempts and the ratio of login success versus login failures. 

 Monitor for potential abuse of MFA on users who have successfully logged in. 

 Internal Login Password Spray attempt on local user 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Credential Access (TA0006) 

 ATT&CK Technique 

 Brute Force: Password Spraying (T1110.003) 

 Severity 

 Low 

 Description 

 An abnormally high number of login attempts with the same username to different domains or local machines within a short period of time. 

 Attacker's Goals 

 An attacker may be attempting to gain unauthorized access to user accounts. 

 Investigative actions 

 Check the amount of time in between each authentication attempt. 

 Investigate the reason behind the login failures and if any accounts were locked out. 

 Look for any successful authentication attempts and the ratio of login success versus login failures. 

 Monitor for potential abuse of MFA on users who have successfully logged in. 

 Internal Login Password Spray on many users 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Credential Access (TA0006) 

 ATT&CK Technique 

 Brute Force: Password Spraying (T1110.003) 

 Severity 

 Low 

 Description 

 An abnormally high amount of user account login attempts were seen from a host within a short period of time. This may have resulted from a login password spray attack. 

 Attacker's Goals 

 An attacker may be attempting to gain unauthorized access to user accounts. 

 Investigative actions 

 Check the amount of time in between each authentication attempt. 

 Investigate the reason behind the login failures and if any accounts were locked out. 

 Look for any successful authentication attempts and the ratio of login success versus login failures. 

 Monitor for potential abuse of MFA on users who have successfully logged in. 

 Previous Interactive login from a shared user account 

 Next Invalid SAML Detected 

 Was this helpful?
