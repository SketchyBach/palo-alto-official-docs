---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/compute/appsec-k8s-44
fetched_at: 2026-09-16T09:09:05Z
source: cortex-platform
---

# Tiller (Helm v2) service is not deleted misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Compute 

 Tiller (Helm v2) service is not deleted misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_K8S_44 

 Category - Subcategory 

 Kubernetes - Management Services Exposure 

 Provider 

 OTHER 

 Severity 

 LOW 

 Framework 

 Helm, Kubernetes, Kustomize, Terraform, Terraform Plan 

 Impact 

 Tiller (Helm v2) is the in-cluster component of Helm. It interacts directly with the Kubernetes API server to install, upgrade, query, and remove Kubernetes resources. It also stores the objects that represent releases. Its permissive configuration could grant the users a broad range of permissions. Helm v3 removes Tiller, and it is recommended that you upgrade: see link:doc:bc_k8s_32[Ensure Tiller (Helm V2) Is Not Deployed]. However, this is not always feasible. Restricting access to Tiller from within the cluster limits the abilities of a compromised pod or anonymous user in the cluster. After link:doc:bc_k8s_40[restricting connectivity to the Tiller deployment], the Tiller service can be deleted. 

 How to Fix 

 Resource: Service 

 [source,go] 

 { "-- apiVersion: v1 

 kind: Service 

 metadata: 

 labels: 

 app: helm 

 name: tiller 

 name: tiller-deploy 

 namespace: kube-system 

 spec: 

 ports: 

 name: tiller 

 port: 44134 

 protocol: TCP 

 targetPort: tiller 

 selector: 

 app: helm 

 name: tiller 

 type: ClusterIP", } 

 Previous Images are not selected using a digest misconfiguration detected in code 

 Next The admission control plugin EventRateLimit is not set misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?
