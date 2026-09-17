---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/iam/appsec-ali-18
fetched_at: 2026-09-16T09:09:07Z
source: cortex-platform
---

# Alibaba Cloud RAM password policy does not prevent password reuse misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 IAM 

 Alibaba Cloud RAM password policy does not prevent password reuse misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_ALI_18 

 Category - Subcategory 

 IAM - Authentication Policies 

 Provider 

 ALIBABA_CLOUD 

 Severity 

 MEDIUM 

 Framework 

 Terraform 

 Impact 

 This rule ensures that RAM (Resource Access Management) password policies prevent password reuse by specifying a value for password_reuse_prevention . Restricting password reuse forces users to create unique passwords for each password change, reducing the likelihood of credential compromise through previously used or weak passwords. 

 Failing to set a password reuse prevention policy can increase the risk of unauthorized access due to predictable or previously compromised passwords being reused. 

 How to Fix 

 Resource: alicloud_ram_account_password_policy 

 Arguments: password_reuse_prevention 

 To mitigate this issue, ensure the password_reuse_prevention attribute in the alicloud_ram_account_password_policy resource is set to a value of 24. 

 Example: [source,go] 

 resource "alicloud_ram_account_password_policy" "example" { ... 

 password_reuse_prevention = 5 

 password_reuse_prevention = 24 } 

 Previous Alibaba Cloud RAM password policy does not have a lowercase character misconfiguration detected in c 

 Next Alibaba Cloud RAM password policy does not have an uppercase character misconfiguration detected in 

 Last updated 1 month ago 

 Was this helpful?
