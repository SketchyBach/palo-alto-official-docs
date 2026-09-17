---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/unusual-access-to-the-ad-sync-credential-files
fetched_at: 2026-09-16T09:08:47Z
source: cortex-platform
---

# Unusual access to the AD Sync credential files | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 Unusual access to the AD Sync credential files 

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

 XDR Agent with eXtended Threat Hunting (XTH) 

 Detection Modules 

 Cloud 

 ATT&CK Tactic 

 Credential Access (TA0006) 

 ATT&CK Technique 

 Credentials from Password Stores (T1555) 

 Severity 

 Informational 

 Description 

 The AD Sync credential files were accessed in an unusual way. 

 Attacker's Goals 

 Extracting and decrypting stored Azure AD and Active Directory credentials from Azure AD Connect servers. 

 Investigative actions 

 See whether this was a legitimate action. 

 Follow the causality chain/user/host activities. 

 Follow unusual actions of the AD Sync user. 

 Check for remote SMB connections to the agent. 

 Check for unusual Azure AD authentications. 

 Check if this happened on other endpoints. 

 Check for unusual logins. 

 Variations 
 Suspicious process access to the AD Sync credential files 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Credential Access (TA0006) 

 ATT&CK Technique 

 Credentials from Password Stores (T1555) 

 Severity 

 Medium 

 Description 

 The AD Sync credential files were accessed in an unusual way. 

 Attacker's Goals 

 Extracting and decrypting stored Azure AD and Active Directory credentials from Azure AD Connect servers. 

 Investigative actions 

 See whether this was a legitimate action. 

 Follow the causality chain/user/host activities. 

 Follow unusual actions of the AD Sync user. 

 Check for remote SMB connections to the agent. 

 Check for unusual Azure AD authentications. 

 Check if this happened on other endpoints. 

 Check for unusual logins. 

 An abnormal process accessed the AD Sync credential files 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Credential Access (TA0006) 

 ATT&CK Technique 

 Credentials from Password Stores (T1555) 

 Severity 

 Low 

 Description 

 The AD Sync credential files were accessed in an unusual way. 

 Attacker's Goals 

 Extracting and decrypting stored Azure AD and Active Directory credentials from Azure AD Connect servers. 

 Investigative actions 

 See whether this was a legitimate action. 

 Follow the causality chain/user/host activities. 

 Follow unusual actions of the AD Sync user. 

 Check for remote SMB connections to the agent. 

 Check for unusual Azure AD authentications. 

 Check if this happened on other endpoints. 

 Check for unusual logins. 

 Previous Unusual access to Microsoft 365 storage services 

 Next Unusual access to the Windows Internal Database on an ADFS server 

 Was this helpful?
