---
url: https://cortex-docs.paloaltonetworks.com/application-security/code-security/application-security-scans-management/manage-scans-through-the-tenant-ui/pull-request-scans/references/reference-d-pr-status-values
fetched_at: 2026-09-06T10:13:27Z
source: cortex-platform
---

# Reference D: PR status values | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center shield-alt

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Application Security 

 Code Security 

 Manage Application Security scans 

 Manage scans through the tenant (UI) 

 Pull Request scans 

 References 

 Reference D: PR status values 

 PR status reports the policy evaluation result and determines the merge outcome. It applies to pull request scans and CI scans. Branch periodic scans have no scan status. 

 PR status 

 Meaning 

 Merge consequence 

 Passed 

 The scan completed and no policy violation was detected 

 The status check reports success and the merge proceeds 

 Failed 

 A finding matched an enabled Block PR policy, or a scanner failed while Fail PR on scan error is enabled 

 The status check reports failure. The merge is blocked where the VCS requires the status check 

 In Progress 

 The scan is currently executing 

 The status check reports a pending state 

 Important: Configure Cortex AppSec - Code analysis as a required target-branch check. Otherwise, a Failed scan records the violation but does not stop a merge. 

 Last updated 19 days ago 

 Was this helpful?
