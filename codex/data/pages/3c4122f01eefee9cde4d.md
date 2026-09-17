---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/ai-and-machine-learning/appsec-gcp-92
fetched_at: 2026-09-16T09:08:59Z
source: cortex-platform
---

# GCP Vertex AI datasets do not use a Customer Manager Key (CMK) misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 AI And Machine Learning 

 GCP Vertex AI datasets do not use a Customer Manager Key (CMK) misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_GCP_92 

 Category - Subcategory 

 Storage - Encryption 

 Provider 

 GCP 

 Severity 

 LOW 

 Framework 

 Terraform 

 Impact 

 This rule identifies Vertex AI datasets which are encrypted with default KMS keys and not with Keys managed by Customer. It is a best practice to use customer managed KMS Keys to encrypt your Vertex AI datasets data. It gives you full control over the encrypted data. 

 How to Fix 

 Resource: google_vertex_ai_dataset 

 Arguments: region.encryption_spec.kms_key_name [source,go] 

 resource "google_vertex_ai_dataset" "pass" { display_name = "terraform" metadata_schema_uri = "gs://google-cloud-aiplatform/schema/dataset/metadata/image_1.0.0.yaml" region = "us-central1" encryption_spec { kms_key_name=google_kms_crypto_key.example.name } 

 } 

 Previous Azure Cognitive Services account hosted with OpenAI is not configured with data loss prevention misc 

 Next GCP Vertex AI Metadata Store does not use a Customer Manager Key (CMK) misconfiguration detected in 

 Last updated 1 month ago 

 Was this helpful?
