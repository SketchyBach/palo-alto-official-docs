---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-administrator-guide/6.13/onboard-cortex-xsoar/engines/manage-engines
fetched_at: 2026-09-16T08:56:52Z
source: cortex-platform
---

# Manage Engines | 6.13 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Administrator Guides 

 6.13 

 Onboard Cortex XSOAR 

 Engines 

 Cortex XSOAR 6.13 

 Manage Engines 

 Manage engines and load balancing groups in Cortex XSOAR 6.13. 

 After you have installed the engine, you can manage engines and Load-Balancing groups by going to Settings → INTEGRATIONS → Engines . 

 You can view engine names, hosts, status, connection, etc. 

 Note 

 In the Service Name column, if the service name starts with a d1 prefix, it is a multiple engine. 

 You can do the following: 

 Add/remove engines to the Load-Balancing Group . 

 You can only add the engine to the Load-Balancing group after you have connected the engine. 

 If you want to remove the last engine from a specific Load-Balancing group, if one or more integration instances use that engine, you will get an error. Before moving the engine, you need to assign Run on to a different engine or no engine for each of the integration instance settings. 

 Create Load-Balancing Groups 

 When selecting Load-Balancing Group → Add to new group , you can create multiple Load-Balancing groups and decide which engines are part of each group. It is useful to create separate Load-Balancing groups. For example, 

 Use separate Load-Balancing groups for different integrations and instances. Create Load-Balancing groups for certain tasks, which can help segregate the infrastructure of critical integrations. 

 Managed Security Service Providers may want to split internal engines and SaaS product engines. 

 If you have multiple AWS accounts that are not connected and do not want a single point of failure for AWS integrations that use STS. 

 For high availability, you may want multiple Load-Balancing groups of engines in different locations. 

 It can also help managing the load in a multi tenant environment 

 Users can move an engine from one group to another. A group will be deleted when the last engine is removed from it. 

 Each engine can only belong to one group. 

 Note 

 (Multi-Tenant) When clicking Load-Balancing and Propagation , you can share engines with tenants for integration purposes. 

 Get engine logs 

 Logs are located in /var/log/demisto . For multiple engines, logs are located in /var/log/demisto/ <name of the engine> . For example, var/log/demisto.d1_e1 . 

 Upgrade an engine 

 Whenever there is a Cortex XSOAR major version change or a change in server-engine protocol version, your engines require an upgrade. The Status column shows those engines that require upgrades. 

 To upgrade the engine, select the checkbox for the engine that requires the upgrade and click Upgrade Engine . When the upgrade finishes, the version appears in the Cortex XSOAR Version . The upgrade procedure can take several minutes. 

 You can only upgrade the engine if you installed the engine with the shell installer. To upgrade engines that were not installed with the shell installer, you need to remove the engine and do a fresh install. For more information, see Install a Cortex XSOAR Engine . For troubleshooting, see Troubleshoot Engine Upgrades . 

 Note 

 By default, auto upgrade extracts the files to the /tmp directory. In some cases, you might need to use a different directory. For example, a common use case is if your /tmp directory is mounted as a non-executable directory. To use a different directory, edit the XSOAR_ENGINE_AUTO_UPGRADE_TMP_DIR env variable. The env variable can be specified as a global variable or can be edited in the crontab of the root user that runs the engine upgrade script. To edit the crontab of root, run sudo crontab -e . An example: 

 Ask Copy 

 # d1 engine 
 XSOAR_ENGINE_AUTO_UPGRADE_TMP_DIR=/root/tmp 
 PATH=/sbin:/bin:/usr/sbin:/usr/bin 
 * * * * * /usr/local/demisto/upgrade_engine.sh >> /var/log/demisto/demisto_install.log 

 Delete engines 

 Previous Run a Script using an Engine 

 Next Configure Engines 

 Last updated 1 month ago 

 Was this helpful?
