---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/single-ip-accessed-mail-items-of-multiple-users
fetched_at: 2026-09-06T11:20:24Z
source: cortex-platform
---

# Single IP accessed mail items of multiple users | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 Single IP accessed mail items of multiple users 

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

 Office 365 Audit 

 Detection Modules 

 Identity Threat Module, Email 

 Detector Tags 

 Extortion 

 ATT&CK Tactic 

 Collection (TA0009) 

 ATT&CK Technique 

 Email Collection: Remote Email Collection (T1114.002) 

 Severity 

 Informational 

 Description 

 A single caller IP accessed Exchange mail items belonging to multiple distinct users within a short time window. This pattern indicates mailbox harvesting from a shared attacker vantage point (VPS or AiTM box). 

 Attacker's Goals 

 An adversary may use a single IP address to access mail items across multiple user accounts, which can aid in the centralized collection and bulk exfiltration of organizational email data. 

 Investigative actions 

 Pivot on the caller IP across all SaaS audit logs and review every session originated from it. 

 For each impacted user, look for fresh OAuth grants, new inbox rules, MFA enrolment changes and anomalous logins. 

 Check the IP reputation in SPUR/threat-intel and revoke active sessions for the affected users. 

 Variations 
 Single IP accessed mail items of multiple users with suspicious characteristics 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Collection (TA0009) 

 ATT&CK Technique 

 Email Collection: Remote Email Collection (T1114.002) 

 Severity 

 Low 

 Description 

 A single caller IP accessed Exchange mail items belonging to multiple distinct users within a short window, and the IP address contributed additional suspicious characteristics (e.g., unmanaged or risky caller IP, anomalous country or ASN for these users). 

 Attacker's Goals 

 An adversary may use a single IP address to access mail items across multiple user accounts, which can aid in the centralized collection and bulk exfiltration of organizational email data. 

 Investigative actions 

 Pivot on the caller IP across all SaaS audit logs and review every session originated from it. 

 For each impacted user, look for fresh OAuth grants, new inbox rules, MFA enrolment changes and anomalous logins. 

 Check the IP reputation in SPUR/threat-intel and revoke active sessions for the affected users. 

 Previous Single account excessively locked out 

 Next SMB Traffic from Non-Standard Process 

 Was this helpful?
