---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-release-notes/6.13/known-issues
fetched_at: 2026-09-16T09:02:22Z
source: cortex-platform
---

# Known Issues | 6.13 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Release Notes 

 Cortex XSOAR 

 Cortex XSOAR 6 Release Notes 

 6.13 

 Known Issues 

 Cortex XSOAR known issues. 

 The following table describes the known issues for Cortex XSOAR. 

 Issue # 

 Issue 

 Description 

 42367 

 Mentions widget not working 

 In the War Room, when using the @ to notify a user, although the user is added to the incident, there is no notification record in the Mentions widget in the user's dashboard (My dashboard). 

 37537 

 Upgrade Common Types Content Pack 

 In Marketplace , after upgrading from a version earlier than 6.2, you need to reinstall or update the Common Types content pack to receive the latest indicator types and to create indicator relationships. 

 36500 

 Widgets on the Main Account displaying incorrect data 

 (Multi-tenant) When viewing widget data on the main account, sometimes the results returned may not be complete. If tenants have different top incident type groups, the aggregated data in the main account can be inaccurate. 

 For example, Tenant A has 20 DoS incidents and 15 Authentication incidents. Tenant B has 10 DoS incidents and 10 Authentication incidents. The top result shown in the main account is DoS:20, even though there are 30 DoS incidents in the system and 25 Authentication incidents. 

 When configuring widgets on the main account, setting higher limit values will improve accuracy. 

 38474 

 Tenant status does not appear correctly in the Main account 

 (Multi-tenant) In the Main account → ACCOUNT MANAGEMENT → Account tab, occasionally, some tenants' accounts are shown with a down status, even though they are running and accessible from the host. This may occur when the host fails to register on the main server, and the host has different IDs on the main server database and the host database. 

 In the main server logs, you may see an error similar to this: 

 2021-06-18 02:32:47.0314 error Failed to register host [error 'Address ... some host address ... is already listed for incoming id 4, saved id 3 (8924)'] (source: /builds/gopath/src/github.com/demisto/server/services/host.go:600) 2021-06-18 02:33:23.0978 warning Failed updating HA group id on host ... some host address ... [error 'Address ... some host address ... is already listed for incoming id 4, saved id 3 (8924)'] (source: /builds/gopath/src/github.com/demisto/server/services/host.go:187) 

 If you encounter this problem, contact Customer Support. 

 44524 

 SAML log-in issue 

 (Multi-tenant) When trying to log in directly to the tenant via SAML, login can fail and the following error is issued: 

 error Cannot decrypt private key for saml [error 'Encryption error (10)'] 

 If you encounter this issue in the main account, sync the SAML integration to the tenant account. 

 47141 

 Tenant marked notActive 

 (Multi-tenant) Sometimes, after an upgrade, a tenant account can be marked as notActive and can no longer be accessed. Contact Cortex XSOAR support for assistance to change the notActive property in the database. 

 XSUP-46416 

 Playbook tasks running the deleteContext.js script 

 When running a sub-playbook that contains a task that runs the deleteContext.js script (such as the SetAndHandleEmpty task in the Cortex XDR - Get Entity alert by MITRE tactics playbook) with Shared globally enabled, the script does not delete the correct key as the content is stored in the root of the context rather than under subplaybook-{PlaybookID} , causing the task to fail. 

 XSUP-54035 

 System restart due to high memory usage 

 In rare cases, when using BoltDB, an indexing failure on a monthly partition database can cause high memory usage, resulting in a system restart. If this happens repeatedly, we recommend reindexing the partition. If the issue still recurs, we recommend considering a migration to Elasticsearch or Cortex XSOAR 8 SaaS. 

 XSUP-46848 

 Time-zone issues in Docker Containers 

 By default, the time zone for Docker containers is set to UTC. Users in other regions that use APAC (such as South Korea, Japan, and Australia) may experience time-related discrepancies. Searches for incidents in a month may overlap between 8 and 11 hours from the previous month, resulting in time-zone discrepancies. 

 In addition, when an indicator is created during a specific time gap, for example, APAC hours GMT+8, such as on Jan 2, 2025, at 12:00-08:00, the time-series widget will show it as created on the previous date, Jan 1, 2025. 

 XSUP-45051 

 Script Execution Time Limit 

 Script execution time on engines is limited to 300 seconds (5 minutes). We strongly recommend utilizing short-running scripts to ensure optimal performance. 

 XSUP-56724 

 Incomplete incident search results 

 When searching for incidents based on indicator values, if there are over 10,000 indicators that match the indicator part of the query, the incident results may be incomplete. 

 XSUP-71008 

 Playbooks stuck in error path 

 In some scenarios, playbooks can become stuck when encountering an error path, preventing the expected execution flow or termination of the incident process. To resolve this, manually stop and restart the playbook execution, or skip the affected task to resume the workflow. 

 Previous Addressed Issues 

 Last updated 23 days ago 

 Was this helpful?
