---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-feature-changes/cortex-xsoar-8-feature-changes/cortex-xsoar-8-api-changes
fetched_at: 2026-09-16T08:55:49Z
source: cortex-platform
---

# Cortex XSOAR 8 API Changes | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 8 

 Cortex XSOAR 8 Feature Changes 

 Cortex XSOAR 8 Feature Changes 

 Cortex XSOAR 8 SaaS Cortex XSOAR 8x On-prem 

 Cortex XSOAR 8 API Changes 

 Review API changes for Cortex XSOAR 8 SaaS and Cortex XSOAR 8x On-prem. 

 The following table describes some of the API changes for Cortex XSOAR 8. 

 Feature 

 Comments 

 API Key 

 Standard and Advanced keys: You can create Standard or Advanced Keys (default is Advanced). 

 Standard keys can be used via CURL, and still require the key in the authorization header, but also require an additional header ( x-xdr-auth-id ) with the value of the key ID, if using a Standard key. 

 Advanced keys require a nonce to prevent replay attacks which is sent in headers. 

 API Structure 

 The API is now like Cortex XDR, where the API is not the server URL, but rather: api-{tenant}/public_api/v1/{name of api}/{name of call} . 

 Example of an old API Call with server URL: curl 'https://hostname:443/incidents/search' 

 Example of a new API Call with API URL: curl -X POST https://api-{fqdn}/xsoar/{name of api}/{name of call}/ 

 Previous Integration Instance Changes in Cortex XSOAR 8 

 Last updated 14 days ago 

 Was this helpful?
