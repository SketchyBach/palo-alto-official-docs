---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/public-exposure/appsec-ali-42
fetched_at: 2026-09-06T11:13:11Z
source: cortex-platform
---

# Alibaba Cloud Mongodb instance does not use SSL misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Public Exposure 

 Alibaba Cloud Mongodb instance does not use SSL misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_ALI_42 

 Category - Subcategory 

 Public Exposure - Encryption And Protocols 

 Provider 

 ALIBABA_CLOUD 

 Severity 

 LOW 

 Framework 

 Terraform 

 Impact 

 This rule ensures that MongoDB instances in Alibaba Cloud are configured to use SSL (Secure Sockets Layer). Enforcing SSL helps in securing communication between the clients and the database server by encrypting the data transmitted over the network. This ensures data privacy and security, protecting sensitive information from being intercepted during transmission. 

 Failing to enable SSL can result in unencrypted data transmission, making it vulnerable to eavesdropping and potential data breaches. 

 How to Fix 

 Resource: alicloud_mongodb_instance 

 Attribute: ssl_action 

 To mitigate this issue, ensure that the ssl_action attribute in the alicloud_mongodb_instance resource is set to Open or Update . 

 Example: [source,go] 

 resource "alicloud_mongodb_instance" "example" { ... 

 ssl_action = "Open" } 

 Previous Alibaba cloud ALB ACL does not restrict public access misconfiguration detected in code 

 Next Alibaba Cloud MongoDB instance is public misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?
