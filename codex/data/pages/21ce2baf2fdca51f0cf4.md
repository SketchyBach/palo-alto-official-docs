---
url: https://cortex-docs.paloaltonetworks.com/application-security/application-security/onboard-data-sources/cli-pipeline-code-snippets
fetched_at: 2026-09-06T10:11:25Z
source: cortex-platform
---

# CLI pipeline code snippets | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center shield-alt shield-alt

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Application Security 

 Application Security 

 Onboard data sources 

 CLI pipeline code snippets 

 Add Cortex CLI code scans to supported CI/CD pipelines. 

 You can run Cortex CLI directly in your CI/CD pipeline to scan code on every build. Add the snippet for your platform to your pipeline configuration file. 

 For information about the CLI, refer to Cortex CLI . 

 Prerequisites 

 In Cortex, the Data Sources permission with Edit access, used to create the API key the CLI authenticates with 

 In your CI platform, permission to edit pipeline configuration files and to add secrets 

 A build environment running Linux with Node.js 22 or later and curl , jq , and git available 

 Before you begin 

 Create a Cortex API key and note both the key and the key ID. Store them in your CI platform's secret store as CORTEX_API_KEY and CORTEX_API_KEY_ID . Never commit them to your repository. 

 Runner architecture 

 Each snippet downloads the CLI using an architecture parameter of either amd64 or arm64 . Set it to match your runner. The CLI is distributed for Linux only — Windows and macOS runners are not supported. 

 Placeholders 

 Replace every placeholder with your own values before running the pipeline. Where your CI platform exposes built-in variables for repository and branch, the snippet uses them; otherwise you must supply them. 

 Each snippet also sets a --source value identifying the CI platform. Do not change it — Cortex uses it to attribute findings correctly. 

 Pipeline snippets and supported architectures 

 AWS CodeBuild — AMD64 and ARM64 environments 

 Azure Pipelines — AMD64 and ARM64 Linux agents 

 Bitbucket — Hosted AMD64 runners and self-hosted ARM64 runners 

 CircleCI — AMD64 and ARM-compatible executors 

 GitHub Actions — AMD64 and ARM64 runners 

 GitLab Runner — AMD64 and ARM64 runners 

 Jenkins — AMD64 and ARM64 agents 

 Previous Terraform workflow for Run Tasks enforcement 

 Next AWS CodeBuild 

 Last updated 1 month ago 

 Was this helpful?
