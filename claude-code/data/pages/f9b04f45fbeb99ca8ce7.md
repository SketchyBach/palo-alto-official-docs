---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-3.x/cortex-xdr-3.x-documentation/endpoint-security/install-and-manage-endpoints/manage-endpoint-protection/delete-cortex-xdr-agents
fetched_at: 2026-09-16T08:44:04Z
source: cortex-platform
---

# Delete Cortex XDR agents | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR 

 Cortex XDR 3.x Documentation 

 Cortex XDR 3.x Documentation 

 Endpoint security 

 Install and manage endpoints 

 Manage endpoint protection 

 Delete Cortex XDR agents 

 Delete endpoints from Cortex XDR tenant views. 

 If you have an endpoint that you no longer want to track through Cortex XDR, for example, if the endpoint disconnected from Cortex XDR, or an endpoint where the Cortex XDR agent was uninstalled, you can delete the endpoint from the Cortex XDR tenant views. Deleting an endpoint triggers the following lifespan flow: 

 The endpoint status changes to Deleted , and the license returns immediately to the license pool. After a retention period of 90 days, the agent is deleted from the database and is displayed in Cortex XDR as Endpoint Name - N/A (Deleted) . 

 Data associated with the deleted endpoint is displayed in the Action Center tables and in the Causality View for the standard 90-day retention period. 

 Alerts that already include the endpoint data at the time of alert creation are not affected. 

 Additionally, Cortex XDR automatically deletes agents after a long period of inactivity. 

 Standard agents are deleted after 180 days of inactivity. Where day one is the first 24 hours of continuous inactivity. 

 VDI and TS agents are deleted after 6 hours of inactivity. 

 Note 

 To reinstate an endpoint, you have to uninstall and reinstall the agent. 

 The following workflow describes how to delete the Cortex XDR agent from one or more Windows, Mac, or Linux endpoints. 

 Select Endpoints → All Endpoints . 

 Right-click the endpoint you want to remove. 

 You can also select multiple endpoints if you want to perform a bulk delete. 

 Select Endpoint Control → Delete Endpoint . 

 Previous Uninstall the Cortex XDR agent 

 Next Manage agent tokens 

 Last updated 1 month ago 

 Was this helpful?
