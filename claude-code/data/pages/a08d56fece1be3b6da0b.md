---
url: https://cortex-docs.paloaltonetworks.com/xdr-3-api/run-xql-query-apis
fetched_at: 2026-09-06T10:55:28Z
source: cortex-platform
---

# Run XQL Query APIs | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 API 

 Cortex XDR 

 XDR 3.x APIs 

 Run XQL Query APIs 

 Cortex XDR enables you to run XQL queries on your data sources using a series of APIs. To execute XQL APIs you must have: 

 Cortex XDR Pro per Endpoint or Cortex XDR Pro per TB license. 

 Valid API Key and API Key ID that include the Instance Administrator role permissions. 

 Available query quota. 

 Query quota is made up of query units that enable you to run XQL APIs. Each XQL API query entails a cost of query units calculated according to the complexity and number of search results. The query cost for each API query is displayed in the Get Query Results API. You can also track the query cost per XQL API search, overall usage, and remaining quota in Cortex XDR or by running a Get XQL Query Quota API. Cortex XDR provides a free daily quota relative to your license size for you to run XQL API queries. In the case of Managed Security, the parent quota depends solely on the children licenses. 

 Note : You will be able to purchase additional query units in future Cortex XDR versions. 

 To execute a XQL API, you need to run a series of APIs. Each API requires a response value from the previous API to continue. This allows you to track the number of XQL queries you want to run, which in turn helps you manage your daily quota. Queries called without enough quota will fail. To ensure you don't surpass your quota, Cortex XDR allows you to run up to four API queries in parallel. 

 Run the following APIs to call an XQL query: 

 Start an XQL Query —Run an XQL query. Response returns a unique execution ID used to retrieve the results by the Get XQL Query Results API. 

 Get XQL Query Results —Retrieve XQL query results. API displays up to 1,000 results. If query generated more than 1,000 results, the response returns a unique stream ID used to retrieve additional results by the Get XQL Query Results Stream API. 

 Get XQL Query Results Stream —Retrieve XQL query with more than 1,000 results. 

 Previous Get started with Cortex XDR 3.x APIs 

 Next Cortex XDR APIs Overview 

 Last updated 1 month ago 

 Was this helpful?
