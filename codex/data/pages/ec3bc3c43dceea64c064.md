---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/public-exposure/appsec2-gcp-9
fetched_at: 2026-09-06T11:13:44Z
source: cortex-platform
---

# GCP Container Registry repositories are anonymously or publicly accessible misconfiguration detected | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Public Exposure 

 GCP Container Registry repositories are anonymously or publicly accessible misconfiguration detected 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC2_GCP_9 

 Category - Subcategory 

 Public Exposure - Storage Buckets 

 Provider 

 GCP 

 Severity 

 HIGH 

 Framework 

 Terraform 

 Impact 

 Ensure that Container Registry repositories are not anonymously or publicly accessible 

 How to Fix 

 Resource: google_storage_bucket_iam_binding 

 Field: members 

 Resource: google_storage_bucket_iam_member 

 Field: member Google Container Registry (GCR) does not have IAM-specific resources in Terraform. Instead, GCR IAM is handled via GCS IAM resources as seen in the below examples. [source,go] 

 resource "google_storage_bucket_iam_binding" "gcr_public_binding" { bucket = google_storage_bucket.default.name role = "roles/storage.viewer" 

 members = [ 

 "allUsers", 

 "allAuthenticatedUsers", ] } 

 resource "google_artifact_registry_repository_iam_member" "public_member" { provider = google-beta location = google_artifact_registry_repository.my-repo.location repository = google_artifact_registry_repository.my-repo.name role = "roles/artifactregistry.writer" 

 member = "allUsers" 

 member = "allAuthenticatedUsers" } 

 resource "google_storage_bucket_iam_member" "gcr_public_member" { bucket = google_storage_bucket.default.name role = "roles/storage.viewer" 

 member = "allUsers" 

 member = "allAuthenticatedUsers" } 

 Previous GCP Cloud KMS Key Rings are anonymously or publicly accessible misconfiguration detected in code 

 Next GCP Cloud Function HTTP trigger is not secured misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?
