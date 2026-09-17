---
url: https://cortex-docs.paloaltonetworks.com/application-security/code-security/application-security-scans-management/manage-scans-through-the-tenant-ui/ci-scans/references/reference-f-ci-scan-sources
fetched_at: 2026-09-16T08:49:30Z
source: cortex-platform
---

# Reference F: CI scan sources | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center shield-alt

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

 Reference F: CI scan sources 

 Two integration families write results to the CI Scans inventory. Both evaluate policies at the CI Scan trigger. Both block through Block CI/CD . Their enforcement mechanisms differ. 

 Source 

 How the scan starts 

 How a block is enforced 

 Notes 

 Cortex CLI in a pipeline — Cortex CLI, CircleCI, GitHub Actions, Jenkins, AWS CodeBuild 

 A pipeline step invokes the Cortex CLI. 

 The CLI returns exit code 1 . The pipeline fails the step. 

 This guide covers this workflow. 

 Terraform run tasks — HCP Terraform, Terraform Enterprise 

 A Terraform run task calls Cortex Cloud during plan or apply. 

 Cortex Cloud posts a result that governs whether the run proceeds. 

 Results appear in the same inventory. Configure enforcement in the Terraform run task. 

 Both sources share one inventory. A repository can produce rows from a pipeline, a Terraform run task, or both. Enable the hidden Provider column to distinguish them. Confirm the source before determining pipeline coverage. 

 Previous Reference E: Issue category routing 

 Next Reference G: Scanner to issue category mapping 

 Last updated 28 days ago 

 Was this helpful?
