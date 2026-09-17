---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/iam/appsec-k8s-5
fetched_at: 2026-09-16T09:09:42Z
source: cortex-platform
---

# Containers run with AllowPrivilegeEscalation based on Pod Security Policy setting misconfiguration d | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 IAM 

 Containers run with AllowPrivilegeEscalation based on Pod Security Policy setting misconfiguration d 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_K8S_5 

 Category - Subcategory 

 Kubernetes - Access Control 

 Provider 

 OTHER 

 Severity 

 MEDIUM 

 Framework 

 Helm, Kubernetes, Kustomize, Terraform, Terraform Plan 

 Impact 

 The AllowPrivilegeEscalation Pod Security Policy controls whether or not a user is allowed to set the security context of a container to True . Setting it to False ensures that no child process of a container can gain more privileges than its parent. We recommend you to set AllowPrivilegeEscalation to False , to ensure RunAsUser commands cannot bypass their existing sets of permissions. 

 How to Fix 

 Resource: Container 

 Arguments: allowPrivilegeEscalation (Optional) If false, the pod can not request to allow privilege escalation. Default to true. [source,go] 

 apiVersion: v1 kind: Pod metadata: name: spec: containers: 

 name: image: securityContext: 

 allowPrivilegeEscalation: false 

 Previous Gitlab project defined in Terraform does not require signed commits misconfiguration detected in cod 

 Next Secrets used as environment variables misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?
