---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/iam/appsec2-gcp-3
fetched_at: 2026-09-06T11:12:29Z
source: cortex-platform
---

# There are not only GCP-managed service account keys for each service account misconfiguration detect | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 IAM 

 There are not only GCP-managed service account keys for each service account misconfiguration detect 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC2_GCP_3 

 Category - Subcategory 

 IAM - Credential Exposure 

 Provider 

 GCP 

 Severity 

 LOW 

 Framework 

 Terraform, Terraform Plan 

 Impact 

 Anyone who has access to the keys will be able to access resources through the service account. GCP-managed keys are used by Cloud Platform services such as App Engine and Compute Engine. These keys cannot be downloaded. 

 Google will keep the keys and automatically rotate them on an approximately weekly basis. User-managed keys are created, downloadable, and managed by users. They expire 10 years from creation. 

 For user-managed keys, the user has to take ownership of key management activities which include: 

 Key storage 

 Key distribution 

 Key revocation 

 Key rotation 

 Protecting the keys from unauthorized users 

 Key recovery Even with key owner precautions, keys can be easily leaked by common development malpractices like checking keys into the source code or leaving them in the Downloads directory, or accidentally leaving them on support blogs/channels. 

 We recommended you prevent user-managed service account keys. 

 How to Fix 

 Resource: google_service_account, google_service_account_key 

 Arguments: service_account_id [source,go] 

 { "resource "google_service_account" "account_ok" { account_id = "dev-foo-account" } 

 resource "google_service_account_key" "ok_key" { service_account_id = google_service_account.account_ok.name } 

 ", } 

 Previous GCP Kubernetes Engine Cluster Nodes have default Service account for Project access misconfiguration 

 Next A MySQL database instance allows anyone to connect with administrative privileges misconfiguration d 

 Last updated 1 month ago 

 Was this helpful?
