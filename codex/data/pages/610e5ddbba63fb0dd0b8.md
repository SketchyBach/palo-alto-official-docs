---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/networking/appsec-azure-121
fetched_at: 2026-09-16T09:09:29Z
source: cortex-platform
---

# Azure Front Door does not have the Azure Web application firewall (WAF) enabled misconfiguration det | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Networking 

 Azure Front Door does not have the Azure Web application firewall (WAF) enabled misconfiguration det 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AZURE_121 

 Category - Subcategory 

 Public Exposure - Ingress Controls 

 Provider 

 AZURE 

 Severity 

 LOW 

 Framework 

 ARM, Bicep, Terraform, Terraform Plan 

 Mapped CSPM/KSPM Rule 

 79734546-c8e7-45f3-a350-f14ad01fdda6 

 Impact 

 WAF is a security feature that provides protection for web applications by inspecting incoming traffic and blocking malicious requests before they reach the application. When WAF is enabled on an Azure Front Door, it analyzes incoming traffic to the front door and blocks requests that are determined to be malicious based on a set of rules. This can help to protect your application from a variety of threats, such as SQL injection attacks, cross-site scripting (XSS) attacks, and other types of attacks. 

 How to Fix 

 Resource: azurerm_frontdoor 

 Arguments: web_application_firewall_policy_link_id [source,go] 

 resource "azurerm_frontdoor" "example" { ... 

 web_application_firewall_policy_link_id = "this_is_id" ... } 

 Previous Azure application gateway does not have WAF enabled misconfiguration detected in code 

 Next Application gateway does not use WAF in Detection or Prevention modes misconfiguration detected in c 

 Last updated 1 month ago 

 Was this helpful?
