---
url: https://cortex-docs.paloaltonetworks.com/application-security/application-security-posture-management-aspm/manage-code-weakness-issues/navigate-to-sast-code-weakness-issues
fetched_at: 2026-09-16T08:49:10Z
source: cortex-platform
---

# Navigate to SAST code weakness issues | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center shield-alt

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Application Security 

 Application Security Posture Management (ASPM) 

 Manage SAST code weakness issues 

 Navigate to SAST code weakness issues 

 To access SAST code violation issues, under Modules , select Application Security → Issues → Code Weaknesses . 

 You an also view SAST issues in dedicated tabs in the Repositories and Business Applications asset side cards, or the All Issues inventory, filtering by Detection Method =SAST Scanner . 

 The Code Weaknesses page displays a filterable, sortable table of all code weakness issues detected across monitored repositories. 

 Note 

 The default sort order is by Severity (descending). The default filter shows issues with a status of New and In Progress . Resolved issues are hidden by default. 

 The Code Weaknesses page contains two tabs: Issues and Findings . 

 Issues tab : Displays deduplicated, policy-evaluated code weakness issues. The Issues tab is the default view and the primary workspace for triage and remediation. Issues are created when a raw scanner finding matches a unified policy 

 Findings tab : Displays all raw code weakness findings detected by the SAST scanner before policy evaluation. The Findings tab provides visibility into the complete scanner output, including findings that did not generate issues because no matching unified policy exists. Use the Findings tab to audit scanner coverage, review findings excluded by current policy configurations, and identify opportunities to create new policies for uncovered finding patterns. For more information, refer to Ingest third-party data sources 

 Note 

 Findings in the Findings tab are raw scanner output and do not have resolution statuses, SLA tracking, or assignees. To track remediation for a specific finding, create or update a unified policy that matches the finding pattern to generate an actionable issue in the Issues tab. 

 Previous Manage SAST code weakness issues 

 Next Understand the Code Weaknesses table 

 Last updated 2 months ago 

 Was this helpful?
