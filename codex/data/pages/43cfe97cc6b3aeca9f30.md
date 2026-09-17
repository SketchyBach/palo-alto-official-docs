---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/ci-cd-security/flow-control-mechanism/appsec-cicd-152
fetched_at: 2026-09-16T09:11:06Z
source: cortex-platform
---

# Repository does not dismiss pull request approvals on the default branch when new commits are pushed | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 CI/CD Security 

 Flow Control Mechanism 

 Repository does not dismiss pull request approvals on the default branch when new commits are pushed 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_CICD_152 

 Category 

 Flow Control Mechanism 

 Severity 

 MEDIUM 

 Impact 

 When a pull request is approved, it means that the code changes have been reviewed and can be merged into the target branch. However, if new commits are added to the request after it has been approved, those commits are not automatically required to be reviewed again. This can lead to bypassing a branch protection rule by merging unreviewed commits into the default branch, potentially introducing malicious code. 

 Recommended Solution - Buildtime 

 It is recommended to configure branch protection rules to dismiss pull request approvals when new commits are pushed. 

 In GitHub, browse to the repository Settings > Branches . 

 Ensure or add a branch protection rule on the default branch. 

 Under Protect matching branches , select Requires a pull request before merging . 

 Check Dismiss stale pull request approvals when new commits are pushed . 

 Note: This option is available after performing step 3 above. 

 Previous Reviews may no longer be required before merging 

 Next Pull request reviews are not required in Azure Repos before merging to the default branch 

 Last updated 1 month ago 

 Was this helpful?
