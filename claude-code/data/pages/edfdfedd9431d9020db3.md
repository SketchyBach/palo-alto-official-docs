---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/public-exposure/appsec-aws-232
fetched_at: 2026-09-16T09:09:41Z
source: cortex-platform
---

# AWS NACL allows ingress from 0.0.0.0/0 to port 22 misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Public Exposure 

 AWS NACL allows ingress from 0.0.0.0/0 to port 22 misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AWS_232 

 Category - Subcategory 

 Public Exposure - Sensitive Ports 

 Provider 

 AWS 

 Severity 

 LOW 

 Framework 

 Terraform 

 Impact 

 Network Access Control List (NACL) is stateless and provides filtering of ingress/egress network traffic to AWS resources. We recommend that NACLs do not allow unrestricted ingress access to port 22. Removing unfettered connectivity to remote console services, such as SSH, reduces a server's exposure to risk. 

 How to Fix 

 [source,go] 

 resource "aws_network_acl_rule" "example" { network_acl_id = aws_network_acl.example.id rule_number = 200 egress = false protocol = "tcp" rule_action = "allow" 

 cidr_block = "0.0.0.0/0" 

 cidr_block = "10.0.0.0/32" from_port = 22 to_port = 22 } 

 Previous AWS NACL allows ingress from 0.0.0.0/0 to port 3389 misconfiguration detected in code 

 Next AWS DAX cluster endpoint does not use TLS (Transport Layer Security) misconfiguration detected in co 

 Last updated 1 month ago 

 Was this helpful?
