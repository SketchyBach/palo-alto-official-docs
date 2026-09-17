---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-administrator-guide/6.13/onboard-cortex-xsoar/engines/configure-engines/configure-the-engine-to-use-a-web-proxy
fetched_at: 2026-09-16T08:56:53Z
source: cortex-platform
---

# Configure the Engine to Use a Web Proxy | 6.13 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Administrator Guides 

 6.13 

 Onboard Cortex XSOAR 

 Engines 

 Configure Engines 

 Cortex XSOAR 6.13 

 Configure the Engine to Use a Web Proxy 

 Configure an engine web proxy in Cortex XSOAR 6.13. 

 The engine uses a web proxy if the following environment variables are set: 

 http_proxy 

 https_proxy 

 If the environment variables are not set, or you wish to use a different settings than those specified in the environment variables, set the configuration with your specific proxy details in the d1.conf file. For example: 

 Ask Copy 

 {"http_proxy": "http://proxy.host.local:8080", 
 "https_proxy": "https://proxy.host.local:8443"} 

 Previous Common Properties When Editing an Engine Configuration 

 Next Configure the Engine to Call the Server Without Using a Proxy 

 Last updated 1 month ago 

 Was this helpful?
