---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/azure-domain-federation-settings-modification-attempt
fetched_at: 2026-09-06T11:01:28Z
source: cortex-platform
---

# Azure domain federation settings modification attempt | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 Azure domain federation settings modification attempt 

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

 AzureAD Audit Log 

 Detection Modules 

 Identity Threat Module, SaaS Threat Detection 

 ATT&CK Tactic 

 Persistence (TA0003), Privilege Escalation (TA0004) 

 ATT&CK Technique 

 Account Manipulation: Additional Cloud Credentials (T1098.001), Domain or Tenant Policy Modification (T1484) 

 Severity 

 Low 

 Description 

 A user or application attempted to modify the federation settings of the domain. 

 Attacker's Goals 

 An attacker attempts to change Active Directory configuration for persistence or defense evasion. 

 Investigative actions 

 Check what configuration has been changed. 

 Check whether the user changing the configuration is permitted. 

 Variations 
 A successful Azure domain federation settings modification 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Persistence (TA0003), Privilege Escalation (TA0004) 

 ATT&CK Technique 

 Account Manipulation: Additional Cloud Credentials (T1098.001), Domain or Tenant Policy Modification (T1484) 

 Severity 

 Medium 

 Description 

 A user or application successfully modified the federation settings of the domain. 

 Attacker's Goals 

 An attacker attempts to change Active Directory configuration for persistence or defense evasion. 

 Investigative actions 

 Check what configuration has been changed. 

 Check whether the user changing the configuration is permitted. 

 Previous Azure diagnostic configuration deletion 

 Next Azure enumeration activity using Microsoft Graph API 

 Was this helpful?
