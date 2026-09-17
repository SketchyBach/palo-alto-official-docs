---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/logging/appsec-aws-353
fetched_at: 2026-09-16T09:09:16Z
source: cortex-platform
---

# RDS instances have performance insights disabled misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Logging 

 RDS instances have performance insights disabled misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AWS_353 

 Category - Subcategory 

 Logging - Disabled or missing 

 Provider 

 AWS 

 Severity 

 LOW 

 Framework 

 Terraform, Terraform Plan 

 Impact 

 This rule is checking to verify if RDS instances have performance insights enabled. Performance insights allow for an advanced database monitoring feature that makes it easy to diagnose and solve performance issues on Amazon RDS databases. If this feature is not enabled, the user may struggle to identify the cause of issues impacting the performance of their RDS instances. Inadequate monitoring could lead to extended downtime, inefficient use of resources and potential loss of data, all of which may have significant impacts on a business's operations and profitability. Therefore, it's a bad practice not to enable performance insights on RDS instances. 

 How to Fix 

 Resource: 'aws_rds_cluster_instance', 'aws_db_instance' 

 Arguments: performance_insights_enabled 

 To fix the issue, you should enable Performance Insights for your RDS instance in your terraform file. Here is how you can do it: [source,go] 

 resource "aws_db_instance" "default" { allocated_storage = 10 engine = "mysql" engine_version = "5.7" instance_class = "db.t2.micro" name = "mydb" username = "foo" password = "foobarbaz" parameter_group_name = "default.mysql5.7" 

 performance_insights_enabled = true } 

 Previous AWS CloudWatch log groups retention set to less than 365 days misconfiguration detected in code 

 Next Azure Network Watcher Network Security Group (NSG) flow logs retention is less than 90 days misconfi 

 Last updated 1 month ago 

 Was this helpful?
