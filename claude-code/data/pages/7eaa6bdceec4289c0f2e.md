---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/iam/appsec-k8s-117
fetched_at: 2026-09-16T09:09:13Z
source: cortex-platform
---

# The --client-cert-auth argument is not set to True misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 IAM 

 The --client-cert-auth argument is not set to True misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_K8S_117 

 Category - Subcategory 

 Kubernetes - Native Security Controls 

 Provider 

 OTHER 

 Severity 

 MEDIUM 

 Framework 

 Helm, Kubernetes, Kustomize 

 Impact 

 Enable client authentication on etcd service. etcd is a highly-available key value store used by Kubernetes deployments for persistent storage of all of its REST API objects. These objects are sensitive in nature and should not be available to unauthenticated clients. You should enable the client authentication via valid certificates to secure the access to the etcd service. 

 How to Fix 

 Kind: Pod [source,go] 

 { "apiVersion: v1 kind: Pod metadata: annotations: scheduler.alpha.kubernetes.io/critical-pod: "" creationTimestamp: null labels: component: etcd tier: control-plane name: etcd namespace: kube-system spec: containers: 

 command: 

 etcd 

 --client-cert-auth=true image: k8s.gcr.io/etcd-amd64:3.2.18", } 

 Previous The RotateKubeletServerCertificate argument for controller managers is not set to True misconfigurat 

 Next The --peer-client-cert-auth argument is not set to True misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?
