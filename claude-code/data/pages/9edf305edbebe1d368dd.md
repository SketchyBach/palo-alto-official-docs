---
url: https://cortex-docs.paloaltonetworks.com/cortex-agentix/reference-and-developer-docs/cortex-agentix-xql/build-xql-queries/overview-of-the-query-center
fetched_at: 2026-09-16T08:51:27Z
source: cortex-platform
---

# Overview of the Query Center | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex AgentiX 

 Cortex AgentiX Documentation 

 Reference and Developer Docs 

 Cortex AgentiX XQL 

 Build XQL queries 

 Cortex AgentiX 

 Overview of the Query Center 

 Monitor in-progress and completed XQL queries in Query Center in Cortex AgentiX. 

 The Query Center displays information about all queries that were run on the tenant, and the queries that are currently In Progress . The Query Center displays the following tabs: 

 Query History 

 View and manage all completed Cortex Query Language (XQL) and Graph Search queries. On this tab you can view query results, re-run and adjust queries, and schedule when a query runs. You can also see details of cancelled queries, including the query type and source, and the name of the user who cancelled the query. 

 Active Queries 

 View and manage all queries that are currently In Progress on the tenant. You can view details about a running query, including the user who ran the query, the context from which it ran, the source of the query, and the amount of time that the query has been running. From this tab you can also cancel active queries. 

 Note 

 Very short queries might not be listed. 

 You cannot cancel correlation queries. 

 The default retention period for historic queries is aligned with issue retention. 

 Query Center reference information 

 The table below lists the common fields in the Query Center, where the options differ for an XQL query versus a Graph Search query. 

 Note 

 Certain fields are exposed and hidden by default. An asterisk (*) is beside every field that is exposed by default. 

 Query Center table 

 Field 

 Description 

 BQL 

 Indicates whether the Cortex Query Language (XQL) query was created by the native search. 

 Native search has been deprecated; this field allows you to view data for XQL queries performed before deprecation. 

 COMPUTE UNIT USAGE 

 For XQL queries, indicates the number of query units that were used to execute the API query and Cold Storage query. 

 ISSUED BY * 

 For XQL queries, indicates the user who ran or scheduled the query. For Graph Search queries, indicates the user who ran the query. 

 DURATION (SEC) 

 Number of seconds it took to execute the XQL query. 

 EXECUTION ID 

 Unique identifier of XQL and Graph Search queries in the tenant. The identifier ID generated for queries executed in Cortex AgentiX and XQL query API. 

 NUM OF RESULTS * 

 Number of results returned by the query. 

 PUBLIC API 

 Whether the source executing the XQL query was an XQL query API. 

 QUERY DESCRIPTION * 

 Query parameters used to run the query. 

 QUERY ID 

 Unique identifier of the query. 

 QUERY NAME * 

 For saved queries, the Query Name identifies the query specified according to a randomly generated number. 

 XQL queries use the format XQL-QUERY-<number> , such as XQL-QUERY-12 . 

 Graph Search queries use the format Graph-Query-<number> , such as Graph-Query-1247 . 

 For scheduled queries, the Query Name identifies the auto-generated name of the parent XQL query. Scheduled queries also display an icon to the left of the name to indicate that the XQL query is recurring. 

 QUERY STATUS * 

 Status of the query, where the options differ based on the query type: 

 XQL queries: 

 Queued : The query is queued and will run when there is an available slot. 

 Running 

 Failed 

 Partially completed : The query was stopped after exceeding the maximum number of permitted results. The default results for a Cortex Data Model (XDM) query or an XQL dataset query is limited to 1000, when no limit is explicitly stated in the query. This applies to basic queries with no stages except the fields stage. This default limit does not apply to widgets, Correlation Rules, public APIs, saved queries, or scheduled queries, where the limit is a maximum of 1,000,000 results. Queries based on legacy templates are limited to 10,000 results. To reduce the number of results returned, you can adjust the query settings and rerun. 

 Stopped : The query was stopped by an administrator. 

 Completed 

 Deleted : The query was pruned. 

 Graph Search queries: 

 Failed 

 Completed 

 QUERY SYNTAX 

 The exact syntax used to write the query. 

 RESULTS SAVED * 

 For XQL queries, you can choose whether to save the query results, so the output of the field is either Yes or No . Yet, for Graph Search queries, the results can't be saved and must be run each time again, so the field is always No . 

 SIMULATED COMPUTE UNITS 

 Number of XQL query units that were used to execute the Hot Storage query. 

 Source 

 Source from which the query was run, for example Playbook, Report, or Investigation. 

 Source ID 

 ID of the source from where the query was run. 

 Source Name 

 Name of the source from where the query was run. 

 TIMESTAMP * 

 Date and time the query was created. 

 XQL 

 Indicates whether the XQL query was created by an XQL search. 

 Previous Query Builder template examples 

 Next Edit and run queries in Query Center 

 Last updated 19 days ago 

 Was this helpful?
