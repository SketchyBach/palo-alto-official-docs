---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/networking/appsec-aws-150
fetched_at: 2026-09-06T11:12:59Z
source: cortex-platform
---

# AWS Elastic Load Balancer v2 with deletion protection feature disabled misconfiguration detected in | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Networking 

 AWS Elastic Load Balancer v2 with deletion protection feature disabled misconfiguration detected in 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AWS_150 

 Category - Subcategory 

 Public Exposure - Load Balancing 

 Provider 

 AWS 

 Severity 

 LOW 

 Framework 

 Terraform, Terraform Plan 

 Impact 

 This rule is checking to ensure that the Load Balancer on an AWS cloud network has enabled deletion protection. The absence of this protection can be harmful because it puts the system at the risk of accidental or unintended deletion, leading to disruption of network services and possibly loss of data. 

 How to Fix 

 To fix the issue highlighted by the mentioned rule, you should enable the deletion protection for your load balancer in AWS. 

 With the given secure code, the enable_deletion_protection = true ensures that the deletion protection is enabled for the load balancer. Thus, AWS prevents the load balancer from being deleted accidentally, which makes the infrastructure secure. [source,go] 

 resource "aws_elb" "example" { name = "example" availability_zones = ["us-west-2a", "us-west-2b", "us-west-2c"] 

 listener { instance_port = 80 instance_protocol = "http" lb_port = 80 lb_protocol = "http" } 

 enable_deletion_protection = true } 

 Previous Default VPC is planned to be provisioned misconfiguration detected in code 

 Next AWS Elastic Load Balancer v2 (ELBv2) with cross-zone load balancing disabled misconfiguration detect 

 Last updated 1 month ago 

 Was this helpful?
