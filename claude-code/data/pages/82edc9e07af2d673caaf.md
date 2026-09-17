---
url: https://cortex-docs.paloaltonetworks.com/application-security/software-supply-chain-security/risk-and-remediation/cicd-risks
fetched_at: 2026-09-16T08:49:15Z
source: cortex-platform
---

# CI/CD Risks | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center shield-alt

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Application Security 

 Software supply chain security 

 Risk and remediation 

 CI/CD Risks 

 CI/CD risks identify vulnerabilities and misconfigurations in pipelines, then prioritize them into actionable issues for efficient remediation. 

 The CI/CD Risk scanner safeguards your software supply chain by identifying insecure configurations in the pipelines, workflows, and version control settings that build and deliver your software. 

 CI/CD pipeline risks are a set of predefined rules that identify pipeline vulnerabilities. Scans analyze both code and configurations of integrated VCS and CI/CD systems and pipelines, as well as their inter-connectivity, to detect these risks. The risks are classified based on security categories including attack vectors, misconfigurations, and bad practices found throughout your CI/CD pipelines. 

 Workflow 

 Use the child pages for each stage of the workflow: 

 Understand the CI/CD Risks table 

 Investigate, prioritize, and remediate CI/CD risk issues 

 VCS and CI/CD pipeline risk findings 

 Core achievements and use cases 

 Securing the delivery infrastructure : Secure the delivery infrastructure: Detect insecure configurations in pipelines, workflows, and VCS settings to extend security coverage to the systems that build and promote code 

 Remediate pipeline risks : Pinpoint the exact configuration file, the owning team, and the specific change required to fix the risk without manually reverse-engineering the CI/CD setup 

 Reducing noise. Evidence text is generated as either general (platform-neutral) or specific (platform-specific and parameterized), which ensures the evidence reflects the actual VCS platform (GitHub, GitLab, Bitbucket, Azure DevOps) and CI/CD system (Jenkins, CircleCI) where the risk was detected, rather than a generic description that a practitioner must translate before acting 

 Standardize risk reporting : Map pipeline vulnerabilities directly to recognized industry frameworks (OWASP Top 10 CI/CD, CIS Benchmarks) for standardized audits 

 Prevent security regressions : Apply automated security policies to CI/CD workflows to stop previously remediated misconfigurations from being reintroduced 

 Prerequisites 

 Prerequisite 

 Description 

 License 

 An active Cortex Cloud license with Application Security entitlements 

 RBAC role 

 The AppSec Practitioner or AppSec Manager role. The DevSecOps and Developer roles can view CI/CD risk evidence but cannot modify detection rule configurations 

 VCS integration 

 At least one VCS data source (GitHub, GitLab, Bitbucket, or Azure DevOps) onboarded to Cortex Cloud 

 CI/CD risk scanning 

 CI/CD risk scanning enabled for the onboarded data source 

 Completed scan 

 At least one completed scan that includes CI/CD risk scanning results 

 Note 

 Cortex Cloud Application Security CI/CD pipeline scans create a comprehensive inventory of all CI/CD pipelines in your environment. For more information refer to CI/CD pipeline as an asset . 

 Previous Ingest third-party SCA data 

 Next Understand the CI/CD Risks table 

 Last updated 1 month ago 

 Was this helpful?
