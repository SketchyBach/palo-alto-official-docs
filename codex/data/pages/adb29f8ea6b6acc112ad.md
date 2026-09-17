---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/monitoring/appsec-azure-27
fetched_at: 2026-09-16T09:09:21Z
source: cortex-platform
---

# Azure SQL Databases with disabled Email service and co-administrators for Threat Detection misconfig | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Monitoring 

 Azure SQL Databases with disabled Email service and co-administrators for Threat Detection misconfig 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AZURE_27 

 Category - Subcategory 

 Monitoring - Alerting And Notifications 

 Provider 

 AZURE 

 Severity 

 LOW 

 Framework 

 ARM, Bicep, Terraform, Terraform Plan 

 Mapped CSPM/KSPM Rule 

 c2ce11a6-a1c2-48f9-9b24-f1384d6ced01 

 Impact 

 Enable Email Service and Co-administrators to receive security alerts from the SQL server. Providing the email address to receive alerts ensures that any detection of anomalous activities is reported as soon as possible, enabling early mitigation of any potential risk detected. 

 How to Fix 

 Resource: Microsoft.Sql/servers/databases 

 [source,go] 

 { "type": "Microsoft.Sql/servers/databases", "apiVersion": "2020-08-01-preview", "name": "[variables('dbName')]", "location": "[parameters('location')]", "sku": { "name": "[parameters('sku')]" }, "kind": "v12.0,user", "properties": { "collation": "SQL_Latin1_General_CP1_CI_AS", "maxSizeBytes": "[mul(parameters('maxSizeMB'), 1048576)]", "catalogCollation": "SQL_Latin1_General_CP1_CI_AS", "zoneRedundant": false, "readScale": "Disabled", "storageAccountType": "GRS" }, "resources": [ { "type": "Microsoft.Sql/servers/databases/securityAlertPolicies", "apiVersion": "2014-04-01", "name": "[concat(variables('dbName'), '/current')]", "location": "[parameters('location')]", "dependsOn": [ "[resourceId('Microsoft.Sql/servers/databases', parameters('serverName'), parameters('databaseName'))]" ], "properties": { "state": "Enabled", "disabledAlerts": "", "emailAddresses": "[variables('emailAddresses')[copyIndex()]]", 

 Ask Copy 

 "emailAccountAdmins": "Enabled" 
 } 
 } 

 ] } 

 Previous Azure SQL Server threat detection alerts are not enabled for all threat types misconfiguration detec 

 Next Azure Microsoft Defender for Cloud is set to Off for Servers misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?
