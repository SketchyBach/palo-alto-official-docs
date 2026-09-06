---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/monitoring/appsec-azure-61
fetched_at: 2026-09-06T11:12:51Z
source: cortex-platform
---

# Azure Microsoft Defender for Cloud is set to Off for App Service misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Monitoring 

 Azure Microsoft Defender for Cloud is set to Off for App Service misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AZURE_61 

 Category - Subcategory 

 Monitoring - Alerting And Notifications 

 Provider 

 AZURE 

 Severity 

 LOW 

 Framework 

 Terraform, Terraform Plan 

 Mapped CSPM/KSPM Rule 

 11e46b7a-6a7d-4500-aef5-f21b0ee608ad 

 Impact 

 Azure Defender is a cloud workload protection service that utilizes and agent-based deployment to analyze signals from Azure network fabric and the service control plane, to detect threats across all Azure resources. It can also analyze non-Azure resources, utilizing Azure Arc, including those on-premises and in both AWS and GCP (once they've been onboarded). Azure Defender for App Service detects attacks targeting applications running over App Service. 

 How to Fix 

 Resource: azurerm_security_center_subscription_pricing 

 Arguments: resource_type - (Required) The resource type this setting affects. 

 Ensure that AppServices is declared to pass this check. [source,go] 

 resource "azurerm_security_center_subscription_pricing" "example" { tier = "Standard" resource_type = "AppServices,ContainerRegistry,KeyVaults,KubernetesService,SqlServers,SqlServerVirtualMachines,StorageAccounts,VirtualMachines,ARM,DNS" } 

 Previous Azure Microsoft Defender for Cloud is set to Off for Servers misconfiguration detected in code 

 Next Azure Microsoft Defender for Cloud is set to Off for Azure SQL Databases misconfiguration detected i 

 Last updated 1 month ago 

 Was this helpful?
