---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/iam/appsec-k8s-155
fetched_at: 2026-09-06T11:12:21Z
source: cortex-platform
---

# Kubernetes ClusterRoles that grant control over validating or mutating admission webhook configurati | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 IAM 

 Kubernetes ClusterRoles that grant control over validating or mutating admission webhook configurati 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_K8S_155 

 Category - Subcategory 

 Kubernetes - Access Control 

 Provider 

 OTHER 

 Severity 

 HIGH 

 Framework 

 Helm, Kubernetes, Kustomize 

 Impact 

 ClusterRoles that grant write permissions over admission webhook should be minimized to reduce powerful identities in the cluster. Validating admission webhooks can read every object admitted to the cluster, while mutating admission webhooks can read and mutate every object admitted to the cluster. As such, ClusterRoles that grant control over admission webhooks are granting near cluster admin privileges. Minimize such ClusterRoles to limit the number of powerful credentials that if compromised could take over the entire cluster. 

 How to Fix 

 Kind : ClusterRole 

 Arguments: rules ClusterRoles that grant the "create", "update" or "patch" verbs over the "mutatingwebhookconfigurations" or "validatingwebhookconfigurations" resources in the "admissionregistration.k8s.io" API group are granting control over admission webhooks. [source,go] 

 kind: ClusterRole apiVersion: rbac.authorization.k8s.io/v1 metadata: name: rules: 

 apiGroups: [""] resources: ["pods"] verbs: ["get"] 

 apiGroups: ["admissionregistration.k8s.io"] resources: ["mutatingwebhookconfigurations"] verbs: 

 list 

 Previous The --rotate-certificates argument is set to false misconfiguration detected in code 

 Next Kubernetes ClusterRoles that grant permissions to approve CertificateSigningRequests are not minimiz 

 Last updated 1 month ago 

 Was this helpful?
