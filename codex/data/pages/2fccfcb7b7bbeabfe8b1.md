---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/storage/appsec-aws-346
fetched_at: 2026-09-06T11:14:07Z
source: cortex-platform
---

# Network Firewall Policy does not define an encryption configuration that uses a CMK misconfiguration | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Storage 

 Network Firewall Policy does not define an encryption configuration that uses a CMK misconfiguration 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AWS_346 

 Category - Subcategory 

 Storage - Encryption 

 Provider 

 AWS 

 Severity 

 HIGH 

 Framework 

 Terraform, Terraform Plan 

 Impact 

 This rule is aimed at ensuring that a Network Firewall Policy includes an encryption configuration that employs a Customer Master Key (CMK). The absence or improper configuration of a CMK in a network firewall policy could lead to sub-optimal encryption of data, making it more vulnerable to unauthorized access, breaches, or leakage. This could compromise the security and integrity of the data, violating best practices for data protection and potentially non-compliance with regulations. Therefore, to maintain high security and data protection standards, it's essential to have an encryption configuration that utilizes a Customer Master Key. 

 How to Fix 

 Resource: aws_networkfirewall_firewall_policy 

 Arguments: encryption_configuration.key_id 

 To fix this issue, you need to specify an encryption configuration that uses a Customer Managed Key (CMK) while defining your AWS Network Firewall Policy. Here's how you can do it: [source,go] 

 resource "aws_networkfirewall_firewall_policy" "example" { name = "example_policy" ... encryption_configuration { key_id = aws_kms_key.example.arn } } 

 Previous Network firewall encryption does not use a CMK misconfiguration detected in code 

 Next Neptune is not encrypted with KMS using a customer managed Key (CMK) misconfiguration detected in co 

 Last updated 1 month ago 

 Was this helpful?
