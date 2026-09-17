---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/public-exposure/appsec-azure-217
fetched_at: 2026-09-16T09:09:54Z
source: cortex-platform
---

# Azure Application gateways listener that allow connection requests over HTTP misconfiguration detect | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Public Exposure 

 Azure Application gateways listener that allow connection requests over HTTP misconfiguration detect 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AZURE_217 

 Category - Subcategory 

 Public Exposure - Ingress Controls 

 Provider 

 AZURE 

 Severity 

 MEDIUM 

 Framework 

 Terraform, Terraform Plan 

 Mapped CSPM/KSPM Rule 

 864d0191-9e8f-46d0-9b3d-f76680579ff6 

 Impact 

 This rule is checking to ensure that Azure Application Gateways do not allow connection requests over HTTP. HTTP is inherently insecure as it does not encrypt the data being transmitted between clients and servers. This means that data like user credentials, payment details, and other sensitive information can be intercepted and exploited by attackers. Therefore, it's important to only allow connections over HTTPS, which is a secure version of HTTP. HTTPS encrypts all data in transit, protecting it from being viewed by third parties. 

 How to Fix 

 Resource: azurerm_application_gateway 

 Arguments: http_listener.protocol 

 To fix this issue, you need to enforce HTTPS-only listener on your Azure Application Gateway. This can be achieved by changing the protocol field from Http to Https in your azurerm_application_gateway terraform configuration. [source,go] 

 resource "azurerm_application_gateway" "example" { ... frontend_port { name = "example" port = 443 } 

 http_listener { name = "example" frontend_ip_configuration_name = azurerm_public_ip.example.name frontend_port_name = azurerm_application_gateway.example.frontend_port.name 

 protocol = "Https" } ... } 

 Previous DenyIntelMode for Azure Firewalls is not set to Deny misconfiguration detected in code 

 Next Azure Application Gateway is configured with SSL policy having TLS version 1.1 or lower misconfigura 

 Last updated 1 month ago 

 Was this helpful?
