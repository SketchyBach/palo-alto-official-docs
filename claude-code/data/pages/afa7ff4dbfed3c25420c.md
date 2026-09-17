---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/networking/appsec-azure-123
fetched_at: 2026-09-16T09:09:30Z
source: cortex-platform
---

# Azure front door does not use WAF in Detection or Prevention modes misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Networking 

 Azure front door does not use WAF in Detection or Prevention modes misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AZURE_123 

 Category - Subcategory 

 Public Exposure - Ingress Controls 

 Provider 

 AZURE 

 Severity 

 LOW 

 Framework 

 ARM, Bicep, Terraform, Terraform Plan 

 Impact 

 WAF has two modes: Detection and Prevention. In Detection mode, WAF analyzes incoming traffic to the Azure front door and logs any requests that are determined to be malicious based on a set of rules. This can help you to identify potential security threats and take appropriate action to protect your application. In Prevention mode, WAF analyzes incoming traffic to the application gateway and blocks any requests that are determined to be malicious based on a set of rules. This can help to prevent malicious requests from reaching your application and potentially causing damage. 

 How to Fix 

 Resource: azurerm_frontdoor_firewall_policy 

 Arguments: policy_settings.enabled + policy_settings.mode [source,go] 

 resource "azurerm_frontdoor_firewall_policy" "example" { 

 ... policy_settings { 

 enabled = true 

 mode = "Prevention" request_body_check = true file_upload_limit_in_mb = 100 max_request_body_size_in_kb = 128 } ... } 

 Previous Application gateway does not use WAF in Detection or Prevention modes misconfiguration detected in c 

 Next Azure Front Door Web application firewall (WAF) policy rule for Remote Command Execution is disabled 

 Last updated 1 month ago 

 Was this helpful?
