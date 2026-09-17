---
url: https://cortex-docs.paloaltonetworks.com/application-security/code-security/code-security-scanners/secrets-scans/understand-the-secrets-issues-table
fetched_at: 2026-09-16T08:49:24Z
source: cortex-platform
---

# Understand the secrets issues table | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center shield-alt

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Application Security 

 Code Security 

 Code Security scanners 

 Secrets scans 

 Understand the secrets issues table 

 The Secrets page combines triage widgets with a detailed issue table. Use the widgets to identify priority work. Use the table to investigate and remediate specific misconfiguration issues. 

 Navigate to Application Security > Issues > Secrets . 

 Widgets 

 Use the widgets to identify and prioritize the most urgent issues before opening the detailed table. Selecting a widget value filters the table to matching issues. 

 Urgency breakdown 

 The Urgency widget charts the count of open issues per Urgency level. Read the proportions rather than the absolute counts. Urgency for a secret issue incorporates the validation status of the credential, the visibility of the containing repository, and the privileges the credential grants. For the complete secret metric table, refer to AppSec issue prioritization (Urgency). 

 SLA Status 

 The SLA Status widget groups issues by SLA compliance status. 

 Insights 

 Each insight card pairs an Urgency level with another risk dimension and shows the number of issues matching both conditions. Dimensions include SLA status, credential validation status, repository visibility, secret sprawl across repositories, and business criticality. 

 Note: A secret issue differs from a vulnerability issue in that deleting the exposed credential does not resolve the exposure. A credential that reached a protected branch must be rotated. Read the widgets as a rotation queue rather than as an upgrade queue. 

 Secrets table 

 The Secrets table provides a consolidated view of secret issues. Each row represents an issue created when a scanner finding matches a unified policy. Each row links the detected credential to the detection rule that identified the credential, the file and line where the credential appears, the commit that introduced the credential, the repository, and the triggering policy. 

 The columns in this table are documented in a shared reference. For descriptions of every available column, the attributes common to all code scan issue tables and the attributes specific to this issue type, see Issue table attributes reference . 

 Filter and sort the table 

 Use the filter bar at the top of the Secrets table to narrow results by any filterable column. Apply the following strategies to scope the table to a working set. 

 Strategy 

 Filter 

 Use when 

 Focus on usable credentials 

 Validation set to Valid and Privileged 

 You are building the rotation queue. A valid credential is exploitable now; an invalid one is not 

 Focus on public exposure 

 Repository Visibility set to Public 

 The credential is readable by anyone, so the exposure window began at commit time 

 Scope to production-bound code 

 Branch set to the default or release branch 

 You are separating credentials that reached a protected branch, which require rotation, from credentials still confined to a feature branch 

 Separate untriaged from active work 

 Resolution Status set to New, then to In Progress 

 You are measuring triage backlog against rotation throughput 

 Quantify secret sprawl 

 Number of Occurrences sorted descending 

 One credential appears across many repositories, and a single rotation resolves every occurrence 

 Suppress entropy noise 

 Detection Rule excluding the entropy-based rules 

 You are reviewing a large backlog and entropy detections dominate the low-severity tier 

 Note: Filtering scopes the population; sorting orders it. Apply both. Sort by Number of Occurrences in descending order to find the credentials whose rotation resolves the most issues. 

 Manage issues 

 Right-click a row in the Secrets table to access the following actions. 

 Action 

 Description 

 Change Status 

 Modify the resolution status of the issue. Values: New, In Progress, Resolved 

 Change Severity 

 Modify the severity level of the issue. Values: Critical, High, Medium, Low 

 Change Assignee 

 Change the user or identity assigned to address the issue 

 Copy text to clipboard 

 Copy the selected cell text 

 Copy entire row 

 Copy the full row of data 

 Copy issue URL 

 Copy the URL of the issue, to share or reference the issue 

 Show/hide rows with the severity level 

 Show or hide all rows matching the severity level of the selected row 

 Caution: Setting a secret issue to Resolved records a triage decision. Setting the status to Resolved does not invalidate the exposed credential. Rotate the credential at the issuing provider before resolving the issue. 

 Previous Secrets scans 

 Next Investigate, prioritize, and remediate secrets issues 

 Last updated 1 month ago 

 Was this helpful?
