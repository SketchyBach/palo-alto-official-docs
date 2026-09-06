---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/iam/appsec-ali-13
fetched_at: 2026-09-06T11:11:57Z
source: cortex-platform
---

# Alibaba Cloud RAM password policy does not have a minimum of 14 characters misconfiguration detected | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 IAM 

 Alibaba Cloud RAM password policy does not have a minimum of 14 characters misconfiguration detected 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_ALI_13 

 Category - Subcategory 

 IAM - Authentication Policies 

 Provider 

 ALIBABA_CLOUD 

 Severity 

 LOW 

 Framework 

 Terraform 

 Impact 

 This rule identifies Alibaba Cloud accounts that do not have a minimum of 14 characters in the password policy. As a security best practice, configure a strong password policy for secure access to the Alibaba Cloud console. 

 How to Fix 

 Resource: alicloud_ram_account_password_policy 

 Arguments: minimum_password_length 

 To mitigate this issue, ensure the minimum_password_length attribute in the alicloud_ram_account_password_policy resource is set to 14 or higher. 

 Example: [source,go] 

 resource "alicloud_ram_account_password_policy" "example" { ... 

 minimum_password_length = 15 } 

 Previous IAM 

 Next Alibaba Cloud RAM password policy does not have a number misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?
