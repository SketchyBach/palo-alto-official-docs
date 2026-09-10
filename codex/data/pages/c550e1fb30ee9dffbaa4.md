---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/public-exposure/appsec-azure-212
fetched_at: 2026-09-06T11:13:27Z
source: cortex-platform
---

# Azure App Service Instance Lacks Redundancy misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Public Exposure 

 Azure App Service Instance Lacks Redundancy misconfiguration detected in code 

 Azure App Service Instance Lacks Redundancy misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AZURE_212 

 Category - Subcategory 

 Public Exposure - Resource Health 

 Provider 

 AZURE 

 Severity 

 LOW 

 Framework 

 ARM, Bicep, Terraform, Terraform Plan 

 Impact 

 Azure App Services Plans provide a configurable mechanism to determine how many instances will run your apps. The number of instances directly affects the availability and failover capabilities of your application. For apps running on a single instance, there's an inherent risk: during unplanned interruptions or outages, your app might experience downtime. 

 Although Azure usually self-heals and addresses faulty app service instances, there can be an intermittent interruption during this period, potentially impacting user experience or critical workflows. 

 To enhance the availability and resilience of your application, this rule ensures that there are more than one instances running your app. By doing so, even if one instance faces issues, another instance can seamlessly take over, ensuring continuous operation of the app. 

 How to Fix 

 Resource: 

 azurerm_service_plan 

 Arguments: 

 worker_count [source,go] 

 resource "azurerm_service_plan" "example" { name = "example-service-plan" 

 ... other configurations ... 

 worker_count = 2 # Ensure you're using a minimum of two instances for better availability. 

 ... other configurations ... 

 } 

 Previous Azure Cognitive Search With Global IP Allowance misconfiguration detected in code 

 Next Backend of the API management system does not utilize HTTPS misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?
