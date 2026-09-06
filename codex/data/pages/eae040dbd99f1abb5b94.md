---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-3.x/cortex-xdr-3.x-documentation/cortex-xdr-xql/build-xql-queries/how-to-build-xql-queries/xql-query-best-practices
fetched_at: 2026-09-06T09:51:03Z
source: cortex-platform
---

# XQL Query best practices | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR 

 Cortex XDR 3.x Documentation 

 Cortex XDR 3.x Documentation 

 Cortex XDR XQL 

 Build XQL queries 

 How to build XQL queries 

 Cortex XDR 3.x 

 XQL Query best practices 

 Learn about best practices for streamlining XQL queries. 

 Notice 

 Building Cortex Query Language (XQL) queries in the Query Builder requires a Cortex XDR Pro license. 

 Cortex XDR includes built-in mechanisms for mitigating long-running queries, such as default limits for the maximum number of allowed alerts. The following suggestions can help you to streamline your queries: 

 Add a smaller limit to queries by using a limit stage. 

 The default results for any query is a maximum of 1,000,000 results, when no limit is explicitly stated in the query. Queries based on XQL query entities are limited to 10,000 results. Adding a smaller limit can greatly reduce the response time. 

 Example: 

 Ask Copy 

 dataset = microsoft_windows_raw 
 | fields *host* 
 | limit 100 

 Use a small time frame for queries by specifying the specific date and time in the Timeframe , such as selecting Relative time and defining Last 30 Minutes , instead of picking the nearest larger option available or defining an extended time period. 

 Use filters that exclude data, along with other possible filters. 

 Select the specific fields that you would like to see in the query results. 

 Previous Useful XQL user interface features 

 Next Expected results when querying fields 

 Last updated 1 month ago 

 Was this helpful?
