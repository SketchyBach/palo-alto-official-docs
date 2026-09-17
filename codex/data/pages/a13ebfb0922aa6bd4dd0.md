---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/iam/appsec2-gcp-1
fetched_at: 2026-09-16T09:09:14Z
source: cortex-platform
---

# GCP Kubernetes Engine Cluster Nodes have default Service account for Project access misconfiguration | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 IAM 

 GCP Kubernetes Engine Cluster Nodes have default Service account for Project access misconfiguration 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC2_GCP_1 

 Category - Subcategory 

 Kubernetes - Access Control 

 Provider 

 GCP 

 Severity 

 LOW 

 Framework 

 Terraform, Terraform Plan 

 Mapped CSPM/KSPM Rule 

 cc010769-cdf3-46f0-8c76-d5c7ae355015 

 Impact 

 Create and use minimally privileged Service accounts to run GKE cluster nodes instead of using the Compute Engine default Service account. Unnecessary permissions could be abused in the case of a node compromise. A GCP service account (as distinct from a Kubernetes ServiceAccount) is an identity that an instance or an application can use to run GCP API requests on your behalf. This identity is used to identify virtual machine instances to other Google Cloud Platform services. By default, Kubernetes Engine nodes use the Compute Engine default service account. This account has broad access by default, as defined by access scopes, making it useful to a wide variety of applications on the VM, but it has more permissions than are required to run your Kubernetes Engine cluster. You should create and use a minimally privileged service account to run your Kubernetes Engine cluster instead of using the Compute Engine default service account, and create separate service accounts for each Kubernetes Workload (See Recommendation 6.2.2). Kubernetes Engine requires, at a minimum, the node service account to have the monitoring.viewer, monitoring.metricWriter, and logging.logWriter roles. Additional roles may need to be added for the nodes to pull images from GCR. 

 How to Fix 

 Resource: google_container_node_pool / google_container_cluster 

 Arguments: google_project_default_service_accounts [source,go] 

 { "resource "google_project_default_service_accounts" "not_ok" { project = "my-project-id" action = "DELETE" id="1234" } 

 resource "google_container_node_pool" "primary_A_not_ok" { name = "my-node-pool" ... 

 service_account = google_project_default_service_accounts.not_ok.id oauth_scopes = [ "https://www.googleapis.com/auth/cloud-platform" ] } 

 } 

 resource "google_container_cluster" "primary_B_not_ok" { 

 ... node_config { 

 service_account = google_project_default_service_accounts.not_ok.id oauth_scopes = [ "https://www.googleapis.com/auth/cloud-platform" ] } 

 } 

 ", } 

 Previous 'chpasswd' is used to set or remove passwords misconfiguration detected in code 

 Next There are not only GCP-managed service account keys for each service account misconfiguration detect 

 Last updated 1 month ago 

 Was this helpful?
