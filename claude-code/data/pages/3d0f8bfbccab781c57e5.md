---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/networking/appsec-gcp-25
fetched_at: 2026-09-16T09:09:30Z
source: cortex-platform
---

# GCP Kubernetes Engine private cluster has private endpoint disabled misconfiguration detected in cod | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Networking 

 GCP Kubernetes Engine private cluster has private endpoint disabled misconfiguration detected in cod 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_GCP_25 

 Category - Subcategory 

 Kubernetes - Management Services Exposure 

 Provider 

 GCP 

 Severity 

 MEDIUM 

 Framework 

 Terraform, Terraform Plan 

 Mapped CSPM/KSPM Rule 

 f698d4a8-6ee8-40b4-9cf1-211901b00ca3 

 Impact 

 Private clusters enable isolation of nodes from any inbound and outbound connectivity to the public internet. This is achieved as the nodes have internal RFC 1918 IP addresses only. In private clusters, the cluster master has private and public endpoints. You can configure which endpoint should be enabled or disabled to control access to the public internet. We recommend you enable private cluster when creating Kubernetes clusters. By creating a private cluster, the nodes will have a reserved set of IP addresses, ensuring their workloads are isolated from the public internet. 

 How to Fix 

 Add Block: private_cluster_config with attribute enable_private_nodes set to true . [source,go] 

 resource "google_container_cluster" "cluster" { ... 

 private_cluster_config { 

 enable_private_nodes=true 

 } ... } 

 Previous GCP Kubernetes Engine Clusters have Alias IP disabled misconfiguration detected in code 

 Next GCP Kubernetes cluster intra-node visibility disabled misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?
