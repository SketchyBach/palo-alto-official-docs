---
url: https://cortex-docs.paloaltonetworks.com/application-security/code-to-cloud/code-to-cloud/troubleshooting
fetched_at: 2026-09-16T08:49:03Z
source: cortex-platform
---

# Troubleshooting | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center shield-alt

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Application Security 

 code-to-cloud 

 Code-to-Cloud 

 Troubleshooting 

 If the Code-to-Cloud lineage is incomplete, one or more specific signals are missing. Use the following table to diagnose and resolve common lineage gaps. 

 Symptom 

 Likely cause 

 Resolution 

 IaC resources show as untraced despite being scanned 

 Missing YOR tags. IaC resources without tags cannot be mapped to runtime 

 The system prompts tagging for these resources. See Workflow 3: Enabling Infrastructure Lineage via YOR 

 Repository shows no trace beyond the Code stage 

 Missing pipeline integration. If a pipeline integration is missing, the link between code and build artifacts breaks 

 Onboard the relevant CI/CD data source via the Onboard Pipeline call-to-action or the Coverage dashboard's Onboard CI/CD instances recommended action 

 Pipeline is integrated but the repository still shows as untraced 

 Inactive pipeline. Lineage is generated during pipeline runs; an integrated but never-run pipeline produces no lineage 

 Trigger a build to generate the necessary artifacts and establish the connection 

 IaC resources are tagged but still show as untraced 

 The matching cloud asset has not been discovered — the cloud account may not be onboarded 

 Onboard the missing cloud account via the Onboard Cloud Accounts recommended action 

 A recently onboarded repository shows as untraced 

 Lineage is calculated by the periodic tracing job; a newly onboarded repository shows Code-2-Cloud = NULL (treated as untraced) until the next tracing run completes 

 Wait for the next tracing-job cycle. No action required 

 Empty-state or troubleshooting guidance is not visible 

 Empty-state messages and troubleshooting guidance for missing lineage are only visible to users with an active license 

 Confirm the Cortex Cloud license is active and includes the required ASPM/AppSec entitlements 

 Coverage % does not match the count of traced repositories 

 The Coverage % depends on the Include not-onboarded repositories and Reach runtime instead of registry configuration toggles, both of which change the calculation without changing the absolute traced count 

 Review the toggle settings. See Reference B: Coverage % calculation and configuration toggles 

 Coverage dashboard filters do not scope past one lineage hop 

 The dashboard supports single-hop filters only in this release (for example, a filter scoping repositories that reach a specific pipeline instance is not supported) 

 Use the single-hop filters available for the current view, or pivot to the affected UAI table directly 

 A recommended action has no action button 

 Recommendations labeled Tagging Needed or Lineage termination (assets that legitimately cannot be traced further) currently have no one-click action 

 Use the deep link to the affected assets and apply the remediation manually through the tagging bot or manual cloud-resource tagging 

 Previous API endpoints for C2C 

 Next FAQs 

 Last updated 1 month ago 

 Was this helpful?
