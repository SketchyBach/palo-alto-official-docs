---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/storage/appsec-gcp-83
fetched_at: 2026-09-06T11:14:19Z
source: cortex-platform
---

# GCP Pub/Sub Topics are not encrypted with Customer Supplied Encryption Keys (CSEK) misconfiguration | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Storage 

 GCP Pub/Sub Topics are not encrypted with Customer Supplied Encryption Keys (CSEK) misconfiguration 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_GCP_83 

 Category - Subcategory 

 Storage - Encryption 

 Provider 

 GCP 

 Severity 

 LOW 

 Framework 

 Terraform 

 Impact 

 Customer-Supplied Encryption Keys (CSEK) are a feature in Google Cloud Storage and Google Compute Engine. Google Compute Engine encrypts all data at rest by default. Compute Engine handles and manages this encryption automatically, with no additional action required. When you provide your own encryption keys Compute Engine uses your key to protect the Google-generated keys used to encrypt and decrypt your data. Only users that provide the correct key can use resources protected by a customer-supplied encryption key. Google does not store your keys on its servers and cannot access your protected data unless you provide the key. If you forget or lose your key Google is unable to recover the key or to recover any data encrypted with that key. To control and manage this encryption yourself, you must provide your own encryption keys. We recommend you supply your own encryption keys for Google to use, at a minimum to encrypt business critical Pub/Sub Topics. This helps protect the Google-generated keys used to encrypt and decrypt your data. 

 How to Fix 

 Resource: google_pubsub_topic 

 Arguments: kms_key_name [source,go] 

 resource "google_pubsub_topic" "pass" { name = "example-topic" kms_key_name = google_kms_crypto_key.crypto_key.id } 

 Previous GCP KMS keys are not protected from deletion misconfiguration detected in code 

 Next GCP Artifact Registry repositories are not encrypted with Customer Supplied Encryption Keys (CSEK) m 

 Last updated 1 month ago 

 Was this helpful?
