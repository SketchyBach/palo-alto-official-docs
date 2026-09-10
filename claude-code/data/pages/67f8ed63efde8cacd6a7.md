---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsoar-6-multi-tenant-guides/6.14/configure-multi-tenant/configure-the-multi-tenant-deployment/install-engines-on-tenants-in-a-multi-tenant-deployment
fetched_at: 2026-09-06T10:50:04Z
source: cortex-platform
---

# Install Engines on Tenants in a Multi-Tenant Deployment | 6.14 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Multi-Tenant Guides 

 6.14 

 Configure Multi-Tenant 

 Configure the Multi-Tenant Deployment 

 XSOAR 6.14 Multi-Tenant 

 Install Engines on Tenants in a Multi-Tenant Deployment 

 Install tenant engines and configure firewall access in Cortex XSOAR 6.14 multi-tenant deployments. 

 Engines created on tenants use a different encryption handshake for each tenant and connect back to the tenant through the main host server. 

 Configure the base URL. 

 On the tenant, go to Settings → ABOUT → Troubleshooting . 

 In the Base URL field, enter the external tenant URL address in the following format: 

 <main account external address> / <tenant account name> 

 For example, demisto.com:443/acc_myaccount 

 Download and install the engine. 

 Go to Settings → INTEGRATIONS → Engines . 

 Click Create New Engine . 

 Select and download the appropriate installer file. 

 Install the engine on the appropriate remote machine. 

 Propagate the engine to tenants. 

 Go to Settings → Integrations → Engines , select the engine, and click Load-Balancing and Propagation . 

 Assign one or more engine propagation labels. 

 If you want to allow use of the engine for tenant specific integration instances, select Allow tenants to use this engine for custom integration instances . If you do not select this option, the engine can only be used with integration instances that were assigned the engine on the main account level and were propagated to tenants. 

 Go to Settings → Account Management → Accounts , and Sync your selected tenant(s). 

 Go to Settings → INTEGRATIONS → Engines and verify that the engine is connected. 

 In many cases the Cortex XSOAR server has a firewall because the engine is probably installed in a different network. The firewall might stop any communication between the engine machine and the Cortex XSOAR server. 

 Ensure that the engine machine is able to communicate with the main host server. You can use Telnet, or any similar tool to check the engine has access to the main account before you install it. If there is a firewall you may need to allow access from the machine that hosts the engine, so that it can communicate back on port 443 (or any other port the main host may use) or set an ANY ANY rule. 

 Previous Index War Room Entries in a Multi-Tenant Deployment 

 Next Configure User Settings 

 Last updated 1 month ago 

 Was this helpful?
