---
url: https://cortex-docs.paloaltonetworks.com/application-security/application-security-posture-management-aspm/repository-as-an-asset
fetched_at: 2026-09-16T08:49:06Z
source: cortex-platform
---

# Repository as an asset | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center shield-alt

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Application Security 

 Application Security Posture Management (ASPM) 

 Repository as an asset 

 Cortex Cloud Application Security discovers and inventories every repository connected through a Version Control System (VCS) integration; GitHub, GitLab, Bitbucket, or Azure DevOps. Each onboarded repository appears in the unified asset inventory as the source-of-truth for the software supply chain, carrying its identity metadata, ownership context, business criticality, security health, and downstream deployment lineage. 

 The repository asset enables security teams to answer three questions about every codebase: What is it? Where does it sit in the organization? What is its security health? 

 What repository assets deliver 

 The repository asset is the central unit of governance in the Cortex Cloud Application Security posture. The repository inventory provides the identity, context, and health telemetry needed to manage every codebase as a governed asset, from discovery through remediation via both the UI console and public APIs. 

 Repository management workflows 

 Manage repository assets through the following workflows: 

 Manage repositories through the tenant (UI) 

 Manage repositories via API 

 Core achievements and use cases 

 Asset discovery and identity: Every repository connected through a VCS integration is automatically discovered and registered in the unified asset inventory with a unique asset identifier, VCS provider, organization, default branch, and onboarding timestamp to serve as the persistent identity record for the codebase 

 Asset metadata enrichment: The repository asset is continuously enriched with metadata synchronized from the VCS provider.Retrieving repository asset details through the API enables synchronization with external asset management systems, CMDB platforms, and compliance reporting tools 

 Code to cloud lineage: The repository asset is the origin node in the code to cloud graph, establishing a traceable lineage from source code through software packages, IaC resources, and CI/CD pipelines to deployed container images and cloud resources 

 Asset health monitoring: The repository asset provides a continuous health profile by aggregating security signals from all scanner types 

 Coverage measurement: The repository inventory quantifies the ratio of discovered repositories to actively scanned repositories, enabling AppSec managers to identify and close coverage gaps manually or programmatically 

 Branch governance automation : Managing scanned branches through the API ensures that release, feature, and hotfix branches are automatically included in scan cycles as part of the release management workflow 

 Compliance evidence: SBOM export (CycloneDX) at the repository level provides auditable evidence of software composition 

 Relationship model 

 The Cortex Cloud platform models the following relationships between the repository asset and other asset categories. 

 Related asset category 

 Inherited metadata and description 

 VCS organization (Parent) 

 The VCS organization that contains the repository, propagating organization-level policies and compliance scopes 

 Software package (Child) 

 Open-source and third-party packages declared in dependency manifest files within the repository 

 IaC resource (Child) 

 Infrastructure-as-Code resources defined within the repository 

 CI/CD pipeline (Child) 

 CI/CD pipeline definitions associated with the repository for deployment lineage tracking 

 Container image (Downstream) 

 Container images built from the repository through CI/CD pipelines 

 Cloud resource (Downstream) 

 Cloud infrastructure provisioned from IaC resources defined in the repository 

 Previous Business application assets 

 Next Manage repository assets through the tenant (UI) 

 Last updated 1 month ago 

 Was this helpful?
