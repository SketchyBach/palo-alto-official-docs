---
url: https://cortex-docs.paloaltonetworks.com/cortex-cloud-api/cortex-platform/run-xql-query-apis
fetched_at: 2026-09-16T09:03:37Z
source: cortex-platform
---

# Run XQL query APIs | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center arrow-counterclockwise

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 API 

 Cortex Cloud 

 Cortex Cloud APIs 

 Cortex Platform 

 Run XQL query APIs 

 Cortex Cloud enables you to run XQL queries on your data sources using a series of APIs. To execute XQL APIs you must have: 

 Valid API Key and API Key ID that include the Instance Administrator role permissions. 

 Available query quota. 

 Query quota is made up of query units that enable you to run XQL APIs. Each XQL API query entails a cost of query units calculated according to the complexity and number of search results. The query cost for each API query is displayed in the Get Query Results API. You can also track the query cost per XQL API search, overall usage, and remaining quota in Cortex Cloud or by running a Get XQL Query Quota API. Cortex Cloud provides a free daily quota relative to your license size for you to run XQL API queries. 

 Note : You will be able to purchase additional query units in future Cortex Cloud versions. 

 To execute a XQL API, you need to run a series of APIs. Each API requires a response value from the previous API to continue. This allows you to track the number of XQL queries you want to run, which in turn helps you manage your daily quota. Queries called without enough quota will fail. To ensure you don't surpass your quota, Cortex Cloud allows you to run up to four API queries in parallel. 

 Run the following APIs to call an XQL query: 

 Start an XQL Query —Run an XQL query. Response returns a unique execution ID used to retrieve the results by the Get XQL Query Results API. 

 Get XQL Query Results —Retrieve XQL query results. API displays up to 1,000 results. If query generated more than 1,000 results, the response returns a unique stream ID used to retrieve additional results by the Get XQL Query Results Stream API. 

 Get XQL Query Results Stream —Retrieve XQL query with more than 1,000 results. 

 Previous Models 

 Next Additional References 

 Last updated 25 days ago 

 Was this helpful?
