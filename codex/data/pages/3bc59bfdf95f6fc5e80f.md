---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/monitoring/appsec-azure-21
fetched_at: 2026-09-16T09:09:22Z
source: cortex-platform
---

# Azure Microsoft Defender for Cloud security alert email notification is not set misconfiguration det | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Monitoring 

 Azure Microsoft Defender for Cloud security alert email notification is not set misconfiguration det 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AZURE_21 

 Category - Subcategory 

 Monitoring - Alerting And Notifications 

 Provider 

 AZURE 

 Severity 

 LOW 

 Framework 

 ARM, Bicep, Terraform, Terraform Plan 

 Impact 

 The alert notifications setting within an Azure Security Center contact configuration specifies whether email notifications for high severity alerts are sent to the security contact. Enabling this setting ensures that the designated contacts are promptly informed of high severity security alerts, allowing for a quicker response to potential security incidents. 

 How to Fix 

 Resource: Microsoft.Security/securityContacts 

 Property: properties.alertNotifications [source,go] 

 { "type": "Microsoft.Security/securityContacts", "apiVersion": "2020-01-01", "name": "default", "properties": { "email": "security_contact@example.com", 

 "alertNotifications": "On", "phone": "(555) 555-5555", "alertsToAdmins": "Off" // Or "On", depending on organizational requirements } } 

 Previous Azure Microsoft Defender for Cloud security contact phone number is not set misconfiguration detecte 

 Next Azure Microsoft Defender for Cloud email notification for subscription owner is not set misconfigura 

 Last updated 1 month ago 

 Was this helpful?
