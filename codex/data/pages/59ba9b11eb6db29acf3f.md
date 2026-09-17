---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/iam/appsec-ali-28
fetched_at: 2026-09-16T09:09:07Z
source: cortex-platform
---

# Alibaba Cloud KMS Key is disabled misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 IAM 

 Alibaba Cloud KMS Key is disabled misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_ALI_28 

 Category - Subcategory 

 IAM - Expired Key Controls 

 Provider 

 ALIBABA_CLOUD 

 Severity 

 LOW 

 Framework 

 Terraform 

 Impact 

 This rule ensures that Alibaba Cloud KMS (Key Management Service) keys are enabled. Enabling KMS keys ensures they are active and can be used for cryptographic operations such as data encryption and decryption. Disabled keys cannot perform these operations, which may cause disruptions in applications relying on the keys. 

 Keeping KMS keys enabled ensures they remain operational and available for secure data handling processes. 

 How to Fix 

 Resource: alicloud_kms_key 

 Arguments: status 

 To mitigate this issue, ensure the status attribute in the alicloud_kms_key resource is set to Enabled . 

 Example: [source,go] 

 resource "alicloud_kms_key" "example" { ... 

 status = "Enabled" } 

 Previous Alibaba Cloud KMS Key Rotation is disabled misconfiguration detected in code 

 Next AWS IAM policies that allow full administrative privileges are created misconfiguration detected in 

 Last updated 1 month ago 

 Was this helpful?
