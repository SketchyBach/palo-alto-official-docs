---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/ai-and-machine-learning/appsec-gcp-96
fetched_at: 2026-09-16T09:08:59Z
source: cortex-platform
---

# GCP Vertex AI Metadata Store does not use a Customer Manager Key (CMK) misconfiguration detected in | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 AI And Machine Learning 

 GCP Vertex AI Metadata Store does not use a Customer Manager Key (CMK) misconfiguration detected in 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_GCP_96 

 Category - Subcategory 

 Storage - Encryption 

 Provider 

 GCP 

 Severity 

 LOW 

 Framework 

 Terraform 

 Impact 

 This rule identifies Vertex AI Metadata Stores which are encrypted with default KMS keys and not with Keys managed by Customer. It is a best practice to use customer-managed KMS Keys to encrypt your Vertex AI Metadata Store data. It gives you full control over the encrypted data. 

 How to Fix 

 Resource: google_vertex_ai_metadata_store 

 Arguments: region.encryption_spec.kms_key_name [source,go] 

 resource "google_vertex_ai_metadata_store" "pass" { name = "test-store" description = "Store to test the terraform module" region = "us-central1" encryption_spec { kms_key_name=google_kms_crypto_key.example.name } } 

 Previous GCP Vertex AI datasets do not use a Customer Manager Key (CMK) misconfiguration detected in code 

 Next GCP Dataproc Clusters have public IPs misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?
