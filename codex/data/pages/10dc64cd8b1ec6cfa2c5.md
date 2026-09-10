---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/iam/appsec-k8s-74
fetched_at: 2026-09-06T11:12:18Z
source: cortex-platform
---

# The --authorization-mode argument is set to AlwaysAllow for Kubelet misconfiguration detected in cod | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 IAM 

 The --authorization-mode argument is set to AlwaysAllow for Kubelet misconfiguration detected in cod 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_K8S_74 

 Category - Subcategory 

 Kubernetes - Access Control 

 Provider 

 OTHER 

 Severity 

 MEDIUM 

 Framework 

 Helm, Kubernetes, Kustomize 

 Impact 

 Do not always authorize all requests. The API Server, can be configured to allow all requests. This mode should not be used on any production cluster. 

 How to Fix 

 Kind: Pod [source,go] 

 { "apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: component: kube-apiserver tier: control-plane name: kube-apiserver namespace: kube-system spec: containers: 

 command: 

 kube-apiserver 

 --authorization-mode=RBAC,node image: gcr.io/google_containers/kube-apiserver-amd64:v1.6.0 ...", } 

 Previous The --kubelet-certificate-authority argument is not set appropriately misconfiguration detected in c 

 Next The --authorization-mode argument does not include node misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?
