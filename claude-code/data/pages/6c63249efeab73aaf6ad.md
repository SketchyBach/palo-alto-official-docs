---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsoar-6-multi-tenant-guides/6.14/onboard-multi-tenant/multi-tenant-deployment-installation/upgrade-your-multi-tenant-deployment
fetched_at: 2026-09-16T08:58:04Z
source: cortex-platform
---

# Upgrade Your Multi-Tenant Deployment | 6.14 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Multi-Tenant Guides 

 6.14 

 Onboard Multi-Tenant 

 Multi-Tenant Deployment Installation 

 Cortex XSOAR 6.14 Multi-Tenant 

 Upgrade Your Multi-Tenant Deployment 

 Prepare, upgrade, and validate a Cortex XSOAR 6.14 multi-tenant deployment. 

 The upgrade process makes changes to the data in the database which can introduce version incompatibility between the Cortex XSOAR service version and the database version during upgrade. 

 Note 

 Cortex XSOAR with Elasticsearch requires one additional index per tenant, host group, and main account. If you are using Elasticsearch, verify you have sufficient available shards before upgrading to Cortex XSOAR v6.5 and above. 

 Caution 

 Before you begin, verify that your system meets the general system requirements , including the required operating system, as well as the multi-tenant hardware requirements . 

 To limit downtime, you can upgrade the main server, restart your main server, and then upgrade your host servers separately. This enables you to plan your upgrade process more efficiently. Although you do not need to upgrade the host servers immediately after upgrading the main server, we highly recommend completing the upgrade process as soon as possible . 

 Palo Alto Networks does not support any functionality if the version difference between the main server and the host server is greater than one version. For example, if the main server is 6.11 and the host server is 6.10, functionality is supported. If the main server is 6.11 and the host server is 6.9, functionality is not supported. 

 If the version on a host server is no more than one version back (previous version) from the main server, you can still view and edit incidents, work with indicators, and use dashboards. 

 Note that content synchronization and host management is not possible when the main server and host server are not the same version. 

 When the host server is one version earlier than the main server, the following actions are not available: 

 Distribute and update playbooks and scripts 

 Propagate new integrations from Marketplace to host servers 

 Manage hosts - delete, add to high availability group, etc. 

 Manage accounts - move accounts to another host, sync, etc. 

 Add new roles and propagation labels to accounts 

 Warning 

 While you can run Cortex XSOAR if the host server is more than one version from the main server, no functionality is guaranteed and no support is provided. 

 Upgrade Multi-Tenant with High Availability 

 To upgrade a multi-tenant environment with high availability, the procedure should be performed in the following order: 

 Stop the main servers. 

 Upgrade the main servers. 

 Start the main servers. 

 Upgrade each host server group at a time that is convenient. All hosts in the same high availability group must be upgraded at the same time. All other host server groups can continue to run, and their tenants can be accessed directly through the host. 

 Upgrade Multi-Tenant with Disaster Recovery 

 For Disaster Recovery (DR), you have primary servers for the main and host servers and secondary (backup) servers for the main and host servers. The secondary (backup) servers need to be up and running when the primary servers are being upgraded, so you should always upgrade the secondary (backup) servers before the primary servers. To upgrade a multi-tenant environment with disaster recovery, the procedure should be performed in the following order: 

 Upgrade Main Server with Disaster Recovery 

 Stop the main primary server. 

 Stop the main secondary (backup) server. 

 Upgrade the main secondary server. 

 Start the main secondary server. 

 Upgrade the main primary server. 

 Start the main primary server. 

 Upgrade the Host Servers with Disaster Recovery. Can be performed immediately or at a later date. For each host: 

 Stop the primary host server. 

 Stop the secondary (backup) host server. 

 Upgrade the secondary host server. 

 Start the secondary host server. 

 Upgrade the primary host server. 

 Start the primary host server. 

 Multi-Tenant Upgrade Procedure 

 Prepare for Upgrade. 

 Back up your data. 

 Download the new installer and copy it to all the servers that will be upgraded by running the following command. 

 wget -O demisto.sh "<downloadLink>" 

 Note 

 You can use the original URL that was sent to you when installing Cortex XSOAR by changing it to the following: 

 Change download.demisto.works to download.demisto.com 

 If you want a specific version (other than a general available release), add &downloadName=<version>_<latest or build number> to the end of the URL. 

 For example, to upgrade to the latest v6.11 release, type https://download.demisto.com/download-params/?token=xxxxxxx&email=user@paloaltonetworks.com&downloadName=6_11_latest&eula=accept 

 If you do not have the original URL, open a Customer Support ticket and select the Download Link option. The link is then sent automatically. 

 Run the following command to allow the .sh file to run as an executable file. 

 chmod +x demisto.sh 

 Stop the main server. 

 sudo service demisto stop 

 (Multi-tenant High Availability) Stop all the main app servers. 

 Multi-tenant DR) Stop the main primary and secondary servers. 

 Upgrade the main servers. 

 sudo ./demisto.sh -- -multi-tenant 

 (Multi-tenant High Availability) Choose a main app server and run the installer on it. After checking the main app server is up and running, run the installer on the other main app servers. 

 (Multi-tenant DR) Run the installer on the main secondary (backup) server. After checking the main secondary (backup) server is up and running, run the installer on the main primary server. 

 Restart the main server. 

 sudo service demisto start 

 Upgrade the host servers. 

 Repeat this step for all host servers that you want to upgrade. 

 (Multi-tenant High Availability) Repeat this step for all high availability groups. 

 Stop the host server(s) that you want to upgrade. 

 sudo service demisto stop 

 (Multi-tenant DR) Stop host secondary (backup) servers. 

 Run the installer. 

 sudo ./demisto.sh -- -multi-tenant 

 Cortex XSOAR uses the /tmp folder for installation. If the folder is blocked by policy, you need to specify a new directory or use /var/tmp directory by adding the -target argument to installation before any other flag. For example, sudo ./demisto.sh -target /var/tmp --multi-tenant 

 (Multi-tenant High Availability) Choose a host app server and run the installer on it. After checking the host app server is up and running, run the installer on the other host app servers. 

 (Multi-tenant DR) Run the installer on the host secondary (backup) server. After checking the host secondary server is up and running, run the installer on the host primary server. 

 Restart the host server. 

 sudo service demisto 

 Validate the upgrade. 

 (Multi-tenant High Availability) Check that the main servers are accessible through the load balancer the same as before the upgrade. 

 Check that all tenants are accessible through the main server. 

 Previous Install Cortex XSOAR for a Multi-Tenant Deployment with Elasticsearch 

 Next Multi-Tenant Upgrade Procedure 

 Last updated 1 month ago 

 Was this helpful?
