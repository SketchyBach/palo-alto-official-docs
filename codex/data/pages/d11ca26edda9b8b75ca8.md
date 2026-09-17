---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-5.x/reference-and-developer-docs/cortex-xdr-xql/build-xql-queries/legacy-query-builder
fetched_at: 2026-09-16T08:43:12Z
source: cortex-platform
---

# XQL query entities | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR 

 Cortex XDR 5.x Documentation 

 Reference and developer docs 

 Cortex XDR XQL 

 Build XQL queries 

 Cortex XDR 5.x 

 XQL query entities 

 Learn more about the entities in the Legacy Query Builder. 

 With Query Builder, you can build complex queries for entities and entity attributes so that you can surface and identify connections between them. Cortex XDR provides Cortex Query Language (XQL) queries for different types of entities in the Query Builder that search predefined datasets. The Query Builder searches the raw data and logs stored in Cortex XDR tenant and for the entities and attributes you specify, it returns up to 1,000,000 results. 

 The Query Builder provides queries for the following types of entities: 

 Process : Search on process execution and injection by process name, hash, path, command line arguments, and more. See Create process query . 

 File : Search on file creation and modification activity by file name and path. See Create file query . 

 Network : Search network activity by IP address, port, host name, protocol, and more. See Create network query . 

 Image Load : Search on module load into process events by module IDs and more. See Create image load query . 

 Registry : Search on registry creation and modification activity by key, key value, path, and data. See Create registry query . 

 Event Log : Search Windows event logs and Linux system authentication logs by username, log event ID (Windows only), log level, and message. See Create event log query . 

 Network Connections : Search security event logs by firewall logs, endpoint raw data over your network. See Create network connections query . 

 Authentications : Search on authentication events by identity, target outcome, and more. See Create authentication query . 

 All Actions : Search across all network, registry, file, and process activity by endpoint or process. See Query across all entities . 

 The Query Builder also provides flexibility for both on-demand query generation and scheduled queries. 

 Previous Graph query results 

 Next Create authentication query 

 Last updated 1 month ago 

 Was this helpful?
