---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/compute/appsec-k8s-27
fetched_at: 2026-09-16T09:09:02Z
source: cortex-platform
---

# Mounting Docker socket daemon in a container is not limited misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Compute 

 Mounting Docker socket daemon in a container is not limited misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_K8S_27 

 Category - Subcategory 

 Kubernetes - Access Control 

 Provider 

 OTHER 

 Severity 

 MEDIUM 

 Framework 

 Helm, Kubernetes, Kustomize, Terraform, Terraform Plan 

 Impact 

 Docker runs through a non-networked UNIX socket. In daemon mode it only allows connections from clients authenticated by a certificate signed by that CA. This socket can be mounted by other containers unless correct permissions are in place. Once mounted, the socket can be used to spin up any container, create new images, or shut down existing containers. To protect the docker socket daemon running in a container, set appropriate SELinux/AppArmor profiles to limit containers mounting this socket. 

 How to Fix 

 Resource : Pod / Deployment / DaemonSet / StatefulSet / ReplicaSet / ReplicationController / Job / CronJob 

 Argument : volumes:hostPath (Optional) 

 Mounts a file or directory from the host node's filesystem into your Pod. 

 If the path is set to /var/lib/docker, the container has access to Docker internals. [source,go] 

 apiVersion: v1 kind: Pod metadata: name: spec: volumes: -name: hostPath: 

 path: /var/run/docker.sock 

 apiVersion: batch/v1beta1 kind: CronJob metadata: name: spec: schedule: <> jobTemplate: spec: template: spec: volumes: -name: hostPath: 

 path: /var/run/docker.sock 

 apiVersion: <> kind: metadata: name: spec: template: spec: volumes: -name: hostPath: 

 path: /var/run/docker.sock 

 Previous Admission of containers with added capability is not minimized misconfiguration detected in code 

 Next Admission of containers with NET_RAW capability is not minimized misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?
