---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-administrator-guide/6.12/onboard-cortex-xsoar/engines/configure-engines/edit-the-engine-configuration/configure-access-to-communication-tasks-through-an-engine
fetched_at: 2026-09-06T10:48:02Z
source: cortex-platform
---

# Configure Access to Communication Tasks through an Engine | 6.12 (EoL) | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Administrator Guides 

 6.12 (EoL) 

 Onboard Cortex XSOAR 

 Engines 

 Configure Engines 

 Edit the Engine Configuration 

 Cortex XSOAR 6.12 EoL 

 Configure Access to Communication Tasks through an Engine 

 Configure communication task access through an engine in Cortex XSOAR 6.12. 

 You can use engines to enable users who do not have access to the Cortex XSOAR server to access the forms sent out in communication tasks. In such instances, the engine serves as a proxy and passes the information in the forms to the Cortex XSOAR server. To use your own certificate instead of the default self-signed certificate, configure an engine to use custom certificates . 

 Prerequisites 

 Ensure that the BindAddress in the engine d1.conf file is configured to a port on which the engine can listen. The engine server address and the configured BindAddress are required to enable external users to communicate with the Cortex XSOAR server. 

 Navigate to Settings → About → Troubleshooting . 

 Click Add Server Configuration . 

 Key 

 Value 

 data.collection.external.link 

 The address (including the https prefix) of the engine used for external user communication. 

 condition.ask.external.link 

 The address (including the https prefix) of the engine used for external user communication. 

 Click Save . 

 Previous Configure the Engine to Call the Server Without Using a Proxy 

 Next Configure the Number of Workers for the Server 

 Last updated 3 days ago 

 Was this helpful?
