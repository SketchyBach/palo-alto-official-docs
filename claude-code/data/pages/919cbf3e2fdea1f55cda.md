---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/monitoring/appsec-k8s-9
fetched_at: 2026-09-16T09:09:28Z
source: cortex-platform
---

# Readiness probe is not configured misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Monitoring 

 Readiness probe is not configured misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_K8S_9 

 Category - Subcategory 

 Kubernetes - Logging And Monitoring 

 Provider 

 OTHER 

 Severity 

 LOW 

 Framework 

 Helm, Kubernetes, Kustomize, Terraform, Terraform Plan 

 Impact 

 Readiness Probe is a Kubernetes capability that enables teams to make their applications more reliable and robust. This probe regulates under what circumstances the pod should be taken out of the list of service endpoints so that it no longer responds to requests. In defined circumstances the probe can remove the pod from the list of available service endpoints. Using the Readiness Probe ensures teams define what actions need to be taken to prevent failure and ensure recovery in case of unexpected errors. https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/[Kubernetes.io Documentation] 

 How to Fix 

 Resource : Container Field: readinessProbe (Optional) 

 The probe describes a health check to be performed against a container to determine whether it is ready for traffic or not. Its configurations may include: exec, failureThreshold, httpGet, initialDelaySeconds, periodSeconds, successThreshold, tcpSocket and timeoutSeconds. [source,go] 

 apiVersion: v1 kind: Pod metadata: name: spec: containers: 

 name: image: 

 readinessProbe: 

 Previous Liveness probe is not configured misconfiguration detected in code 

 Next The --profiling argument is not set to false for API server misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?
