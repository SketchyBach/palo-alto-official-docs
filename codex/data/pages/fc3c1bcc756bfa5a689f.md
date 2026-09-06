---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/iam/appsec-gcp-113
fetched_at: 2026-09-06T11:12:14Z
source: cortex-platform
---

# IAM policy defines public access misconfiguration detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 IAM 

 IAM policy defines public access misconfiguration detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_GCP_113 

 Category - Subcategory 

 IAM - Overly Permissive 

 Provider 

 GCP 

 Severity 

 HIGH 

 Framework 

 Terraform, Terraform Plan 

 Impact 

 Allowing public access is generally a bad practice in security terms, as it can potentially expose sensitive data or functionality. Without proper access controls in place, unauthorized users could potentially gain access to secure areas, manipulate data, invoke functions, or even take control of the system or resources. This rule ensures that public access is not permitted, thereby maintaining a tighter control over who can interact with the system. 

 How to Fix 

 Resource: google_iam_policy 

 Arguments: binding 

 Instead of using 'allUsers' or 'allAuthenticatedUsers' which grants permissions to any user on the internet, specific user, role, or service account should be given permissions. 

 This code allows only the specified users and service account to get 'objectViewer' permissions. Making such changes to your IAM policies will keep your resources secure by preventing unauthorized access. This adheres to the policy of ensuring IAM policy does not define public access. [source,go] 

 resource "google_project_iam_policy" "project" { project = "your-project-id" policy_data = "${data.google_iam_policy.admin.policy_data}" } 

 data "google_iam_policy" "admin" { binding { role = "roles/storage.objectViewer" 

 members = [ "user:individual-email", "serviceAccount:service-account-email", ] } } 

 Previous KMS policy allows public access misconfiguration detected in code 

 Next Basic roles utilized at the organization level misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?
