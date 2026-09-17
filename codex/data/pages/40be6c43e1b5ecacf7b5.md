---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/compute/appsec-ali-30
fetched_at: 2026-09-16T09:09:00Z
source: cortex-platform
---

# Alibaba Cloud RDS instance is not set to perform auto upgrades for minor versions misconfiguration d | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Compute 

 Alibaba Cloud RDS instance is not set to perform auto upgrades for minor versions misconfiguration d 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_ALI_30 

 Category - Subcategory 

 Compute - Unsanctioned Resource Or Type 

 Provider 

 ALIBABA_CLOUD 

 Severity 

 LOW 

 Framework 

 Terraform 

 Impact 

 Auto upgrades for minor versions help ensure that your RDS instance is running the latest version, which can include security updates and patches. By enabling auto upgrades, you can help protect your RDS instance and the data it contains from vulnerabilities and threats. 

 How to Fix 

 Resource: alicloud_db_instance 

 Arguments: auto_upgrade_minor_version 

 To mitigate this issue, ensure the auto_upgrade_minor_version attribute is set to Auto in the alicloud_db_instance resource. 

 Example: [source,go] 

 resource "alicloud_db_instance" "example" { ... 

 auto_upgrade_minor_version = "Auto" } 

 Previous Compute 

 Next Disabled Ansible URI certificate validation misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?
