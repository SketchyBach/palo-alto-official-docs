---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/networking/appsec-aws-113
fetched_at: 2026-09-16T09:09:27Z
source: cortex-platform
---

# Deletion protection disabled for load balancer misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Networking 

 Deletion protection disabled for load balancer misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AWS_113 

 Category - Subcategory 

 Public Exposure - Load Balancing 

 Provider 

 AWS 

 Severity 

 MEDIUM 

 Framework 

 Terraform, Terraform Plan 

 Impact 

 This rule identifies Elastic Load Balancers v2 (ELBv2) which are configured with deletion protection feature disabled. Enabling delete protection for these ELBs prevents irreversible data loss resulting from accidental or malicious operations. For more details refer: https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancers.html#deletion-protection 

 How to Fix 

 Resource: aws_lb 

 Arguments: enable_deletion_protection [source,go] 

 resource "aws_lb" "test_success" { ... 

 enable_deletion_protection = true } 

 Previous AWS EKS node group have implicit SSH access from 0.0.0.0/0 misconfiguration detected in code 

 Next VPC endpoint service is not configured for manual acceptance misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?
