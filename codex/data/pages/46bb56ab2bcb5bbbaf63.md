---
url: https://cortex-docs.paloaltonetworks.com/application-security/software-supply-chain-security/visibililty-and-inventory/supply-chain-assets/technologies-as-assets/troubleshoot-repository-technology-detection
fetched_at: 2026-09-16T08:49:14Z
source: cortex-platform
---

# Troubleshoot repository technology detection | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center shield-alt

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Application Security 

 Software supply chain security 

 Visibililty and inventory 

 Supply Chain assets 

 Technologies as assets 

 Troubleshoot repository technology detection 

 Resolve technology detection issues and review common questions. 

 Resolve common technology detection issues. Review how composition percentages and technology metadata work. 

 Frequently asked questions 

 Can users manually tag a repository with a custom technology? 

 No. Technology detection is automated and cannot be manually overridden or supplemented. 

 The detection engine analyzes files during repository scans. Undetected custom frameworks do not appear in Technologies . 

 Use repository Tags for custom metadata. Tags appear in the repository side card. 

 What happens when a new language is added? 

 The technology appears after the next repository scan. Select Rescan in the repository side card to update it immediately. 

 Are technology percentages based on lines of code or file count? 

 Percentages represent each technology's proportional share of the repository codebase. File-level analysis calculates the proportions, which total 100%. 

 Do technologies affect security scanning or policy evaluation? 

 Technologies are informational Asset Inventory metadata. They can inform scanner configuration and policy scoping. 

 Troubleshoot technology detection 

 If a known technology is missing, review these causes and resolutions: 

 Cause 

 Resolution 

 The repository has not been scanned recently 

 Select the repository row, then select Rescan in the side-card actions. 

 All scanners are disabled for the repository 

 Enable at least one scanner. The Rescan action is unavailable otherwise. 

 Technology files are on an unscanned branch 

 Confirm that the branch is included in the scanning scope. 

 The technology is unsupported 

 Standard technologies are detected broadly. Proprietary frameworks might not be detected. 

 Previous Technologies as assets 

 Next Software packages as assets 

 Last updated 1 month ago 

 Was this helpful?
