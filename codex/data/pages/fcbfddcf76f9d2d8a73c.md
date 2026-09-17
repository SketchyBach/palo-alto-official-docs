---
url: https://cortex-docs.paloaltonetworks.com/xsoar-migration-guide/cortex-xsoar-8-saas-multi-tenant-migration/migrate-from-cortex-xsoar-6-multi-tenant-to-cortex-xsoar-8-saas-multi-tenant-using-the-migration-wiz/step-3.-run-user-acceptance-tests-uat-in-a-multi-tenant-deployment-using-the-migration-wizard/engines-multi-tenant
fetched_at: 2026-09-16T08:55:54Z
source: cortex-platform
---

# Engines - Multi-Tenant | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 8 

 Cortex XSOAR Migration Guide 

 Cortex XSOAR 8 SaaS Multi-Tenant Migration 

 Migrate from Cortex XSOAR 6 Multi-Tenant to Cortex XSOAR 8 Multi-Tenant using the migration wizard 

 Step 3. Run user acceptance tests (UAT) in a Multi-Tenant Deployment using the Migration Wizard 

 Engines - Multi-Tenant 

 At the initial data sync, although your engine data has been migrated, engines are not connected to the Cortex XSOAR 8 tenant. 

 To connect the engines to both Cortex XSOAR 6 and 8, you need to update the Cortex XSOAR 6 d1.conf file on each machine where an engine is installed with the new Cortex XSOAR 8 engine configuration and IP address. 

 Note 

 If using an engine, you must update your settings in all tenants (main, child, and development). 

 Before updating the file, we recommend copying your existing settings in case you need to revert. 

 Any engine that you have connected during the UAT phase remains connected after the switchover date. There is no need to change the configuration again. 

 The Cortex XSOAR 6 engine is supported up to 30 days after the switchover date to resolve any potential engine migration issues. To have a definitive engine in the XSOAR 8 environment, you need to deploy XSOAR 8 Engines. For more information, see Install an engine . 

 Update your Cortex XSOAR 6 instance. 

 Go to Settings → ABOUT → Troubleshooting . 

 In the Server Configuration section, click Add Server Configuration . 

 Add the following key and value: 

 Key 

 Value 

 migration.op.engines.enabled 

 true 

 Save the server configuration. 

 In Cortex XSOAR 8, download the engine configuration file to get the new engine attribute values. 

 Go to the Engines page. 

 For each engine, select Download Configuration . 

 Copy the values for the following attributes: 

 http.authentication.header 

 ServerPublic 

 EngineURLs 

 On the engine machine, edit the Cortex XSOAR 6 d1.conf file by adding the attribute values you copied in step 2. 

 On the machine on which you installed the engine, navigate to the d1.conf file: 

 Installation Type 

 Location 

 RPM, DEB, Shell 

 /usr/local/demisto 

 If using multiple engines, the location is /usr/local/demisto/ name of the engine> . For example, /usr/local/demisto/d1_e1 

 ZIP 

 Same folder as the binary. 

 Note 

 If you have a Shell installation, you can update the d1.conf file directly from the Engines page. For more information, see Configure engines . 

 Add the following attributes (the values are taken from step 2). 

 Ask Copy 

 { 
 "additionalurls": { 
 "migration": { 
 "engineHeaderKey": "<The value of the Cortex XSOAR 8 http.authentication.header attribute>", 
 "serverPublicKey": "<The value of the Cortex XSOAR 8 ServerPublic attribute>", 
 "urls": [ 
 "<The value of the Cortex XSOAR 8 EngineURLs attribute>" 
 ] 
 } 
 } 
 } 

 Save the file. 

 Run the following commands: 

 sudo systemctl stop demisto 

 sudo systemctl start demisto 

 Note 

 We recommend waiting at least 5 seconds between stopping and starting the engine. 

 Verify that the engines are connected and working. 

 In your firewall configuration, ensure that you have enabled access to EngineURLs in the following format: 

 api-<xsoar-tenant>.crtx.<region>.paloaltonetworks.com 

 For more information, see Enable access to Palo Alto Network resources . 

 Previous Security and Authentication - Multi-Tenant 

 Next Remote Repositories - Multi-Tenant 

 Last updated 1 month ago 

 Was this helpful?
