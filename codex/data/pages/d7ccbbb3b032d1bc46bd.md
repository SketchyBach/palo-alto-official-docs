---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/compute/appsec-k8s-25
fetched_at: 2026-09-06T11:11:42Z
source: cortex-platform
---

# Admission of containers with added capability is not minimized misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Compute 

 Admission of containers with added capability is not minimized misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_K8S_25 

 Category - Subcategory 

 Kubernetes - Access Control 

 Provider 

 OTHER 

 Severity 

 LOW 

 Framework 

 Helm, Kubernetes, Kustomize, Terraform, Terraform Plan 

 Impact 

 Containers run with a default set of capabilities as assigned by the Container Runtime. By default this can include potentially dangerous capabilities. With Docker as the container runtime the NET_RAW capability is enabled which may be misused by malicious containers. Ideally, all containers should drop this capability. 

 How to Fix 

 [source,go] 

 resource "kubernetes_pod" "pass2" { metadata { name = "terraform-example" } 

 spec { container { image = "nginx:1.7.9" name = "example22" 

 security_context { capabilities { add = [] } } 

 env { name = "environment" value = "test" } 

 port { container_port = 8080 } 

 liveness_probe { http_get { path = "/nginx_status" port = 80 

 http_header { name = "X-Custom-Header" value = "Awesome" } } 

 initial_delay_seconds = 3 period_seconds = 3 } } 

 dns_config { nameservers = ["1.1.1.1", "8.8.8.8", "9.9.9.9"] searches = ["example.com"] 

 option { name = "ndots" value = 1 } 

 option { name = "use-vc" } } 

 dns_policy = "None" } } 

 Previous Containers with added capability are allowed misconfiguration detected in code 

 Next Mounting Docker socket daemon in a container is not limited misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?
