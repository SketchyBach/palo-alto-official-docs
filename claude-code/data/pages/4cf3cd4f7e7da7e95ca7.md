---
url: https://cortex-docs.paloaltonetworks.com/application-security/software-supply-chain-security/risk-and-remediation/software-composition-analysis-sca-scanners/software-composition-analysis-sca-vulnerability-issues/understand-the-vulnerabilities-table
fetched_at: 2026-09-16T08:49:16Z
source: cortex-platform
---

# Understand the Vulnerabilities table | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center shield-alt

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Application Security 

 Software supply chain security 

 Risk and remediation 

 Software Composition Analysis (SCA ) 

 Software Composition Analysis (SCA) vulnerability issues 

 Understand the Vulnerabilities table 

 The Vulnerabilities page combines triage widgets with a detailed issue table. Use widgets to identify priority work. Use the table to investigate and remediate specific CVE vulnerability issues. 

 Widgets 

 Use the widgets to identify and prioritize the most urgent issues before opening the detailed table. Selecting a widget value filters the table to matching issues. 

 Urgency breakdown 

 The Urgency widget charts the count of open issues per Urgency level. Read the proportions rather than the absolute counts. 

 SLA Status 

 Review issues by SLA compliance status. 

 Insights 

 Each insight card pairs an Urgency level with another risk dimension. Dimensions include SLA status, business criticality, internet exposure, fix availability, dependency type, and traceability completeness. Each card shows the number of issues matching both conditions. 

 Vulnerabilities table 

 The table provides a consolidated view of CVE vulnerability issues. Each row represents an issue created when a scanner finding matches a unified policy. It links the vulnerability to its CVE, package, file, repository, and triggering policy. 

 The columns in this table are documented in a shared reference. For descriptions of every available column, the attributes common to all code scan issue tables and the attributes specific to this issue type, see Issue table attributes reference . 

 Filter and sort the table 

 Use the filter bar at the top of the Vulnerabilities table to narrow results by any filterable column. Common filtering strategies include: 

 By severity: Filter to Critical and High severity to focus on the most impactful CVE vulnerabilities 

 By package: Filter to a specific package name (such as log4j-core) to scope remediation to a single dependency 

 By branch: Filter to the main or production branch to focus on vulnerabilities that affect production-bound code 

 By resolution status: Filter to New to identify untriaged CVE vulnerability issues, or to In Progress to monitor active remediation 

 By KEV status: Filter to True to identify vulnerabilities listed in the CISA Known Exploited Vulnerabilities catalog that require immediate attention 

 By reachability: Filter to Reachable to focus on vulnerabilities where the vulnerable function is confirmed to be invoked in the application code 

 By EPSS score: Sort by EPSS score (descending) to prioritize vulnerabilities with the highest probability of active exploitation 

 Manage issues 

 Right-click on a row in the inventory table to access the following actions 

 Change Status . Modify the status of the issue. Values: New, In Progress, Resolved 

 Change Severity : Modify the severity level of the issue. Values: Critical, High, Medium, Low 

 Change Assignee : Change the user or identity assigned to address the issue 

 Copy text to clipboard : Duplicate selected text for easy pasting elsewhere 

 Copy entire row : Duplicate the entire row of data for easy pasting elsewhere 

 Copy issue URL : Duplicate the URL associated with the issue, to share or reference the issue 

 Show/hide rows with the [severity level] : Show/hide rows matching the [severity level] of the selected row 

 Previous Software Composition Analysis (SCA) vulnerability issues 

 Next Investigate, prioritize and remediate vulnerability issues 

 Last updated 1 month ago 

 Was this helpful?
