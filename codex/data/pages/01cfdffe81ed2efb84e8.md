---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/compute/appsec-k8s-40
fetched_at: 2026-09-06T11:11:46Z
source: cortex-platform
---

# Containers do not run with a high UID misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Compute 

 Containers do not run with a high UID misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_K8S_40 

 Category - Subcategory 

 Kubernetes - Access Control 

 Provider 

 OTHER 

 Severity 

 LOW 

 Framework 

 Helm, Kubernetes, Kustomize 

 Impact 

 Linux namespaces provide isolation for running processes and limits access to system resources. To prevent privilege-escalation attacks from within a container, we recommend that you configure your container's applications to run as unprivileged users. The mapped user is assigned a range of UIDs which function within the namespace as normal UIDs from 0 to 65536, but have no privileges on the host machine itself. If a process attempts to escalate privilege outside of the namespace, the process is running as an unprivileged high-number UID on the host, not mapped to a real user. This means the process has no privileges on the host system and cannot be attacked by this method. This check will trigger below UID 10,000 as common linux distributions will assign UID 1000 to the first non-root, non system user and 1000 users should provide a reasonable buffer. 

 How to Fix 

 Resource: Pod / Deployment / DaemonSet / StatefulSet / ReplicaSet / ReplicationController / Job / CronJob 

 Arguments: runAsUser (Optional) Specifies the User ID that processes within the container and/or pod run with. [source,go] 

 apiVersion: v1 kind: Pod metadata: name: spec: containers: 

 name: image: securityContext: 

 runAsUser: <UID higher then 10000> 

 apiVersion: batch/v1beta1 kind: CronJob metadata: name: spec: schedule: <> jobTemplate: spec: template: spec: containers: 

 name: image: securityContext: 

 runAsUser: <UID higher then 10000> 

 apiVersion: <> kind: metadata: name: spec: template: spec: containers: 

 name: image: securityContext: runAsUser: <UID higher then 10000> 

 Previous CAP_SYS_ADMIN Linux capability is used misconfiguration detected in code 

 Next Images are not selected using a digest misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?
