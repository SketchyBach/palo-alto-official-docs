---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/iam/appsec-glb-4
fetched_at: 2026-09-16T09:09:12Z
source: cortex-platform
---

# Gitlab project defined in Terraform does not require signed commits misconfiguration detected in cod | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 IAM 

 Gitlab project defined in Terraform does not require signed commits misconfiguration detected in cod 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_GLB_4 

 Category - Subcategory 

 IAM - Overly Permissive 

 Provider 

 OTHER 

 Severity 

 LOW 

 Framework 

 Terraform 

 Impact 

 In GitLab, administrators can turn on the capability to require signed commits for a project. When you enable required commit signing on a branch, contributors and bots can only push commits that have been signed and verified to the branch. If a collaborator pushes an unsigned commit to a branch that requires commit signatures, the collaborator will need to rebase the commit to include a verified signature, then force push the rewritten commit to the branch. 

 How to Fix 

 Resource: gitlab_project 

 Attribute: prevent_secrets [source,go] 

 resource "gitlab_project" "example-two" { ... push_rules { ... 

 reject_unsigned_commits = true } } 

 Previous Gitlab branch protection rules defined in Terraform allow force push misconfiguration detected in co 

 Next Containers run with AllowPrivilegeEscalation based on Pod Security Policy setting misconfiguration d 

 Last updated 1 month ago 

 Was this helpful?
