---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/iam/appsec-oci-12
fetched_at: 2026-09-06T11:12:22Z
source: cortex-platform
---

# OCI IAM password policy for local (non-federated) users does not have a number misconfiguration dete | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 IAM 

 OCI IAM password policy for local (non-federated) users does not have a number misconfiguration dete 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_OCI_12 

 Category - Subcategory 

 IAM - Authentication Policies 

 Provider 

 ORACLE 

 Severity 

 MEDIUM 

 Framework 

 Terraform, Terraform Plan 

 Impact 

 This rule identifies Oracle Cloud Infrastructure(OCI) accounts that do not have a lowercase character in the password policy for local (non-federated) users. As a security best practice, configure a strong password policy for secure access to the OCI console. 

 How to Fix 

 Resource: oci_identity_authentication_policy 

 Arguments: password_policy.is_numeric_characters_required [source,go] 

 resource "oci_identity_authentication_policy" "pass" { ... password_policy { ... is_numeric_characters_required = true ... } } 

 Previous OCI IAM password policy for local (non-federated) users does not have a lowercase character misconfi 

 Next OCI IAM password policy for local (non-federated) users does not have a symbol misconfiguration dete 

 Last updated 1 month ago 

 Was this helpful?
