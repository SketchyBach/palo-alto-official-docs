---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/compute/appsec-k8s-79
fetched_at: 2026-09-16T09:09:04Z
source: cortex-platform
---

# The admission control plugin AlwaysAdmit is set misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Compute 

 The admission control plugin AlwaysAdmit is set misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_K8S_79 

 Category - Subcategory 

 Kubernetes - Native Security Controls 

 Provider 

 OTHER 

 Severity 

 MEDIUM 

 Framework 

 Helm, Kubernetes, Kustomize 

 Impact 

 Do not allow all requests. Setting admission control plugin AlwaysAdmit allows all requests and does not filter any requests. The AlwaysAdmit admission controller was deprecated in Kubernetes v1.13. Its behavior was equivalent to turning off all admission controllers. 

 How to Fix 

 Kind: Pod [source,go] 

 { "apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: component: kube-apiserver tier: control-plane name: kube-apiserver-passed namespace: kube-system spec: containers: 

 command: 

 kube-apiserver 

 --enable-admission-plugins=other image: gcr.io/google_containers/kube-apiserver-amd64:v1.6.0 livenessProbe: failureThreshold: 8 httpGet: host: 127.0.0.1 path: /healthz port: 6443 scheme: HTTPS initialDelaySeconds: 15 timeoutSeconds: 15 name: kube-apiserver resources: requests: cpu: 250m volumeMounts: 

 mountPath: /etc/kubernetes/ name: k8s readOnly: true 

 mountPath: /etc/ssl/certs name: certs 

 mountPath: /etc/pki name: pki hostNetwork: true volumes: 

 hostPath: path: /etc/kubernetes name: k8s 

 hostPath: path: /etc/ssl/certs name: certs 

 hostPath: path: /etc/pki name: pki", } 

 Previous The admission control plugin EventRateLimit is not set misconfiguration detected in code 

 Next The admission control plugin AlwaysPullImages is not set misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?
