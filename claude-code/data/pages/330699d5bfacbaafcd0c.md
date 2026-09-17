---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/public-exposure/appsec-k8s-100
fetched_at: 2026-09-16T09:10:01Z
source: cortex-platform
---

# The --tls-cert-file and --tls-private-key-file arguments for API server are not set appropriately mi | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Public Exposure 

 The --tls-cert-file and --tls-private-key-file arguments for API server are not set appropriately mi 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_K8S_100 

 Category - Subcategory 

 Kubernetes - Native Security Controls 

 Provider 

 OTHER 

 Severity 

 HIGH 

 Framework 

 Helm, Kubernetes, Kustomize 

 Impact 

 API server communication contains sensitive parameters that should remain encrypted in transit. Configure the API server to serve only HTTPS traffic by setup TLS connection on the API server. By default, --tls-cert-file and --tls-private-key-file arguments are not set. 

 How to Fix 

 Kind: Pod [source,go] 

 { " apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: component: kube-apiserver tier: control-plane name: kube-apiserver namespace: kube-system spec: containers: 

 command: 

 kube-apiserver 

 --tls-cert-file=/path/to/cert 

 --tls-private-key-file=/path/to/key image: gcr.io/google_containers/kube-apiserver-amd64:v1.6.0 livenessProbe: failureThreshold: 8 httpGet: host: 127.0.0.1 path: /healthz port: 6443 scheme: HTTPS initialDelaySeconds: 15 timeoutSeconds: 15 name: kube-apiserver resources: requests: cpu: 250m volumeMounts: 

 mountPath: /etc/kubernetes/ name: k8s readOnly: true 

 mountPath: /etc/ssl/certs name: certs 

 mountPath: /etc/pki name: pki hostNetwork: true volumes: 

 hostPath: path: /etc/kubernetes name: k8s 

 hostPath: path: /etc/ssl/certs name: certs 

 hostPath: path: /etc/pki name: pki ", } 

 Previous The --secure-port argument is set to 0 misconfiguration detected in code 

 Next The --read-only-port argument is not set to 0 misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?
