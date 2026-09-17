---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/ci-cd-security/data-protection/appsec-cicd-82
fetched_at: 2026-09-16T09:10:51Z
source: cortex-platform
---

# Force push to default branch is allowed in GitLab | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 CI/CD Security 

 Data Protection 

 Force push to default branch is allowed in GitLab 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_CICD_82 

 Category 

 Data Protection 

 Severity 

 LOW 

 Impact 

 User accounts with Write permissions can force push to a default branch of an actively used repository and overwrite the commit history. If the repository is not stored on another source, a malicious user account can permanently delete the entire git history of the repository. An actively used repository has at least two contributors, over 50 commits, and was updated in the last 90 days. 

 Previous Project webhook SSL verification disabled 

 Next Private repository made public 

 Last updated 1 month ago 

 Was this helpful?
