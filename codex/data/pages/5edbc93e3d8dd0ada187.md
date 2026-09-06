---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/azure-device-code-authentication-flow-used
fetched_at: 2026-09-06T11:01:25Z
source: cortex-platform
---

# Azure device code authentication flow used | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 Azure device code authentication flow used 

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

 Azure Audit Log 

 Detection Modules 

 Identity Analytics 

 ATT&CK Tactic 

 Persistence (TA0003), Lateral Movement (TA0008) 

 ATT&CK Technique 

 Account Manipulation (T1098), Use Alternate Authentication Material (T1550) 

 Severity 

 Informational 

 Description 

 An Azure AD login was performed with device code flow. 

 Attacker's Goals 

 An attacker may use a device to access resources in the tenant using an access token from device code authentication flows. 

 Investigative actions 

 Check what devices are listed with the logged-in user. 

 Check if the account is authorized to use such devices to access resources. 

 Check for possible logins from the device. 

 Follow further actions done by the account and device. 

 Variations 
 Suspicious Azure device code authentication flow used by an Azure AD privileged user 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Persistence (TA0003), Lateral Movement (TA0008) 

 ATT&CK Technique 

 Account Manipulation (T1098), Use Alternate Authentication Material (T1550) 

 Severity 

 Medium 

 Description 

 An Azure AD login was performed with device code flow. 

 Attacker's Goals 

 An attacker may use a device to access resources in the tenant using an access token from device code authentication flows. 

 Investigative actions 

 Check what devices are listed with the logged-in user. 

 Check if the account is authorized to use such devices to access resources. 

 Check for possible logins from the device. 

 Follow further actions done by the account and device. 

 Suspicious Azure device code authentication flow used 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Persistence (TA0003), Lateral Movement (TA0008) 

 ATT&CK Technique 

 Account Manipulation (T1098), Use Alternate Authentication Material (T1550) 

 Severity 

 Low 

 Description 

 An Azure AD login was performed with device code flow. 

 Attacker's Goals 

 An attacker may use a device to access resources in the tenant using an access token from device code authentication flows. 

 Investigative actions 

 Check what devices are listed with the logged-in user. 

 Check if the account is authorized to use such devices to access resources. 

 Check for possible logins from the device. 

 Follow further actions done by the account and device. 

 Azure device code authentication flow used by an Azure AD privileged user 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Persistence (TA0003), Lateral Movement (TA0008) 

 ATT&CK Technique 

 Account Manipulation (T1098), Use Alternate Authentication Material (T1550) 

 Severity 

 Low 

 Description 

 An Azure AD login was performed with device code flow. 

 Attacker's Goals 

 An attacker may use a device to access resources in the tenant using an access token from device code authentication flows. 

 Investigative actions 

 Check what devices are listed with the logged-in user. 

 Check if the account is authorized to use such devices to access resources. 

 Check for possible logins from the device. 

 Follow further actions done by the account and device. 

 Previous Azure conditional access policy creation or modification 

 Next Azure diagnostic configuration deletion 

 Was this helpful?
