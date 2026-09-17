---
url: https://cortex-docs.paloaltonetworks.com/application-security/software-supply-chain-security/visibililty-and-inventory/supply-chain-assets/repository-as-an-asset/manage-repository-assets-through-the-tenant-ui
fetched_at: 2026-09-16T08:49:13Z
source: cortex-platform
---

# Manage repository assets through the tenant (UI) | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center shield-alt

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Application Security 

 Software supply chain security 

 Visibililty and inventory 

 Supply Chain assets 

 Repository as an asset 

 Manage repository assets through the tenant (UI) 

 Prerequisites 

 Before viewing and managing repository assets, verify the following: 

 Prerequisite 

 Description 

 License 

 An active Cortex Cloud license with Application Security entitlements 

 RBAC role 

 The AppSec Admin or SOC Analyst role, or an equivalent custom role with asset inventory and issue management permissions 

 VCS integration 

 At least one Version Control System (GitHub, GitLab, Bitbucket, Azure DevOps) integrated and active 

 Repository onboarding 

 At least one repository onboarded through the VCS integration and visible in the asset inventory 

 Understand repository assets 

 To access repository assets, under Inventory , select All Assets → Code → Repositories . 

 The Repositories assets page includes a dashboard and an inventory. 

 Repository dashboard 

 The dashboard includes two widgets: 

 Providers : Displays connected version control providers (such as GitHub and GitLab) and the number of repositories found in each provider 

 Visibilitiy Configuration (privacy state) : Shows the distribution between public and private repositories and the amount of repositories in each category 

 Selecting an item in either widget filters the table accordingly. 

 Repository asset inventory 

 The inventory table displays repository attributes as columns. A default set is exposed, while additional attributes are hidden. Select Menu Settings to add them. 

 See Reference: Repositories asset attributes for details about each attribute. 

 Repository actions 

 After reviewing the repository's health, you can perform the following operations from the Actions menu in the side panel. 

 Rescan a repository: Click Rescan to trigger an on-demand scan using the currently configured scanners 

 Export an SBOM: Click Export SBOM to generate and download a Software Bill of Materials. 

 Level : Select Repository to download the SBOM for the selected repository, or Organization to download all SBOM reports for the parent organization as a ZIP archive 

 Supported formats 

 CycloneDX v1.4: XML or JSON 

 CycloneDX v1.5: XML or JSON 

 CycloneDX v1.6: XML or JSON 

 SDPX v2.3: JSON or TXT 

 Open in GitHub: Click Open in GitHub to pivot directly to the native repository environment to investigate source code, review commit history, or initiate remediation through a pull request 

 View asset data: Click View asset data to view raw repository data in JSON (default) or tree view 

 Filter and prioritize repositories 

 The Repositories page displays a table of all repositories. Use the search bar to find repositories by name, or apply filters to narrow results based on operational and security metadata. 

 High-priority filtering workflows 

 To effectively reduce the organization risk surface, apply the following filter combinations to prioritize remediation efforts: 

 Target critical assets: Filter by Business Application Names to isolate repositories tied to essential services and prioritize their vulnerabilities for remediation 

 Identify public exposure risks: Filter by Repository visibility configuration: Public to identify proprietary repositories inadvertently set to public in the VCS provider 

 Find active repositories missing scanner coverage: Filter by Is repository archived: No and sort the table by the Last Scan Date column to highlight actively maintained repositories that have never been scanned 

 Filter out noise from stale code: Filter by Is repository archived: Yes or sort by the oldest Last Commit Date to isolate abandoned or read-only codebases 

 Scope by business unit or environment: Use the repository tag metadata filter to isolate the inventory for specific engineering teams or deployment environments 

 Next steps 

 Investigate repository assets 

 Previous Repository as an asset 

 Next Investigate repository assets 

 Last updated 1 month ago 

 Was this helpful?
