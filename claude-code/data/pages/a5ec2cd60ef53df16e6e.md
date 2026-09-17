---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/reference-and-developer-docs/role-based-access-control/investigation-and-response-permissions/search-permissions/query-center-permissions
fetched_at: 2026-09-16T08:37:35Z
source: cortex-platform
---

# Query Center permissions | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSIAM 

 Cortex XSIAM Documentation 

 Reference and developer docs 

 Role-Based Access Control 

 Investigation and Response permissions 

 Search permissions 

 Cortex XSIAM 

 Query Center permissions 

 Manage access to write, run, schedule, and export XQL queries in Cortex XSIAM. 

 Controls access to the Query Center (under Investigation & Response → Search ), which is the primary interface for writing, executing, and managing XQL queries in Cortex XSIAM. It is the core investigation tool that enables security analysts to search across all ingested data using a powerful query language. Key capabilities: 

 Write and execute XQL queries against any ingested dataset. 

 View query execution history and results. 

 Schedule recurring queries 

 Export query results 

 Caution 

 Access to the Query Center is strictly governed by Scope-Based Access Control (SBAC). Even if users have View/Edit permissions, they will only see data returned from the endpoint groups or log sources defined in their specific role scope. 

 For more information, see Overview of the Query Center . 

 Permission 

 Description 

 Roles Example 

 None 

 The entire Investigation section is hidden: Query Center, Query Builder, and Scheduled Queries are all inaccessible. 

 View 

 Read-only access to the Query Center. Users can view query history, view scheduled queries, view active queries, and view individual execution results, but cannot run new queries. 

 Most viewer-type roles. 

 View/Edit 

 Full read and write access, including scheduling, canceling, running queries, deleting execution data, and deleting executions. 

 Most roles require query execution, scheduling, and management. 

 Required and recommended permissions 

 To make the most of the Query Center capabilities, consider adding the following permissions: 

 Permission 

 Permission Level 

 Reason 

 Dashboards 

 Enabled 

 Strongly recommended for the analyst to take an XQL query and Save to Dashboard to create a visual monitoring widget. 

 Reports 

 View/Edit 

 Recommended if the analyst needs to turn a search result into a scheduled PDF report for management. 

 Query Library 

 Enabled with checkboxes selected 

 Recommended to view saved queries. 

 Dataset Access 

 N/a 

 Ensure the role's Data Scope includes the necessary pro-datasets (e.g., Cloud, Network, Endpoint) or the user will receive "No Results Found" even with a perfect query. 

 Previous Query Library permissions 

 Next Forensics permissions 

 Last updated 20 days ago 

 Was this helpful?
