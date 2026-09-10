---
url: https://cortex-docs.paloaltonetworks.com/application-security/code-security/application-security-scans-management/manage-scans-through-the-tenant-ui/ci-scans/references/reference-a-ci-scan-concepts
fetched_at: 2026-09-06T10:13:31Z
source: cortex-platform
---

# Reference A: CI scan concepts | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center shield-alt

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Application Security 

 Code Security 

 Manage Application Security scans 

 Manage scans through the tenant (UI) 

 CI scans 

 References 

 Reference A: CI scan concepts 

 CI status gates the build; scan health reports execution 

 CI scans carry two independent signals, and reading one for the other produces incorrect conclusions about enforcement. 

 reports the policy evaluation result — whether the scan passed or was blocked. CI status corresponds to the process exit code the CLI returns to the pipeline, and therefore determines whether the build continues. A scan that detected issues no policy blocked reports 

 Scan health reports the execution health of the scan: whether every scanner completed, some scanners failed, or the scan is still executing 

 The combination to watch is a passing status on degraded health. A build that reports Passed while scan health reports Partially Completed shipped an artifact evaluated on incomplete evidence — a scanner that never executed cannot fail anything 

 Note: For every CI status value and its build consequence, see Reference D: CI status values . For every scan health value, see Reference C: Scan health values . 

 The exit code is the enforcement, not the inventory row 

 Cortex Cloud does not reach into the pipeline to stop a build. The Cortex CLI returns an exit code, and the pipeline decides what to do with it: exit code 1 means a finding matched a blocking policy, and a pipeline that treats a non-zero exit as a failure stops the build. 

 Two consequences follow. A pipeline step configured to ignore failures — or a CLI invoked with --soft-fail — records a blocked result in Cortex Cloud while the build proceeds. And exit code 2 signals an internal, network, or authentication error rather than a policy decision, which fails the build for a reason unrelated to security unless --no-fail-on-crash is set. 

 Treat the inventory as the record of the decision and the pipeline configuration as the enforcement. For the full exit code contract, see Cortex CLI. 

 Not every CI scan reaches the inventory 

 The absence of a row is not evidence that a pipeline ran clean. A CI scan produces no row in any of the following cases: 

 The CLI ran in no-upload mode , either explicitly or because the API key lacks write permission. The scan still evaluates findings locally and can still fail the build 

 The pipeline never invoked the CLI , because the step was removed, skipped by a conditional, or never added to that pipeline 

 The scan failed before reporting , on authentication or network error 

 Important: Counting CI scan rows measures the pipelines that reported, not the pipelines that are gated. A pipeline with no scan step and a pipeline that ran clean are indistinguishable in this inventory. Establish the pipeline population from the CI/CD Pipelines asset inventory — see CI/CD pipeline as an asset — and treat a repository that ships artifacts with no CI scan rows as unverified rather than clean. 

 Issues from CI scans carry no Urgency 

 Urgency combines exploit intelligence with Code-to-Cloud deployment context. Code evaluated at build time is not yet deployed, so the deployment-dependent signals cannot be computed and the Urgency engine returns Not Applicable for CI scan issues by design. 

 Prioritize CI scan issues by severity and by the business criticality of the affected repository. Do not read Not Applicable as low risk. For the Urgency model, see Urgency. 

 Last updated 19 days ago 

 Was this helpful?
