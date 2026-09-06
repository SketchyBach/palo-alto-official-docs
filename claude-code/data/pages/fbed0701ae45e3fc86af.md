---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/compute/appsec-aws-225
fetched_at: 2026-09-06T11:11:24Z
source: cortex-platform
---

# AWS API Gateway method settings do not enable caching misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Compute 

 AWS API Gateway method settings do not enable caching misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_AWS_225 

 Category - Subcategory 

 Compute - Unsanctioned Resource Or Type 

 Provider 

 AWS 

 Severity 

 LOW 

 Framework 

 Terraform 

 Impact 

 Enabling caching for API Gateway helps improve your API's performance by allowing clients to retrieve responses from a cache instead of making a request to the backend service. This can reduce the load on your backend service and improve the overall responsiveness of your API. It can reduce the cost of using your API by reducing the number of requests your backend service needs to handle. It can also improve the reliability of your API by allowing it to continue functioning even if the backend service is unavailable or experiencing problems. 

 How to Fix 

 [source,go] 

 resource "aws_api_gateway_method_settings" "pass" { rest_api_id = aws_api_gateway_rest_api.fail.id stage_name = aws_api_gateway_stage.fail.stage_name method_path = "path1/GET" 

 settings { caching_enabled = true metrics_enabled = false logging_level = "INFO" cache_data_encrypted = true data_trace_enabled = false } } 

 Previous AWS DMS replication instance automatic version upgrade disabled misconfiguration detected in code 

 Next AWS DB instance does not get all minor upgrades automatically misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?
