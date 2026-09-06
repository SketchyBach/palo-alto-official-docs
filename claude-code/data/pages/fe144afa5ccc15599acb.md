---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-administrator-guide/6.14/onboard-cortex-xsoar/high-availability/deploy-engines-in-a-high-availability-environment
fetched_at: 2026-09-06T10:40:11Z
source: cortex-platform
---

# Deploy Engines in a High Availability Environment | 6.14 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Administrator Guides 

 6.14 

 Onboard Cortex XSOAR 

 High Availability 

 Cortex XSOAR 6.14 

 Deploy Engines in a High Availability Environment 

 Deploy Cortex XSOAR 6.14 engines in high availability and route engine connections through a load balancer. 

 Engines deployed prior to the migration to Elasticsearch will remain connected to the newly migrated Cortex XSOAR application server. 

 When additional Cortex XSOAR application servers are deployed, and placed behind a load balancer, you need to update the engines to connect through the load balancer. 

 Verify that the BaseURL and ExternalHostname server configurations have been updated on the servers to reference the load balancer url. 

 Stop the engine service. 

 Create a backup of the /usr/local/demisto/d1.conf file. 

 Edit the /usr/local/demisto/d1.conf file on the engine. 

 Set the first line in the EngineURLs section to point to the new load balancer URL. 

 Ask Copy 

 { 
 "LogLevel": "info", 
 "LogFile": "d1.log", 
 "EngineURLs": [ 
 "wss://LOADBALANCERURL/d1ws" 
 ], 
 … 
 } 

 Start the engine service. 

 Validate the engine is connected by going to Settings → Engines . 

 Previous Install Additional App Servers 

 Next Use a Signed Certificate 

 Last updated 11 days ago 

 Was this helpful?
