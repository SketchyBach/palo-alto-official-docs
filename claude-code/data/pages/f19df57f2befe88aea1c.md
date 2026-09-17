---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-administrator-guide/6.14/onboard-cortex-xsoar/deployment-checklist-best-practices
fetched_at: 2026-09-16T08:55:57Z
source: cortex-platform
---

# Deployment Checklist - Best Practices | 6.14 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Administrator Guides 

 6.14 

 Onboard Cortex XSOAR 

 Cortex XSOAR 6.14 

 Deployment Checklist - Best Practices 

 Overview of the deployment process, including best practices for Cortex XSOAR 6.14 installation and maintenance. 

 The Cortex XSOAR Deployment Checklist provides an overview of the deployment process, including best practices for installation and maintenance. Unless otherwise specified, instructions apply to on-premise deployments with BoltDB or Elasticsearch, as well as hosted deployments. Each section includes links to more extensive documentation. 

 Install Cortex XSOAR 6 

 For Bolt DB: 

 Review the System Requirements and provision servers to at least the recommended minimums. 

 Follow instructions for Single Server installation. 

 Perform the Server Post-Installation Health Check . 

 For Elasticsearch: 

 Review the Elasticsearch Overview and Elasticsearch Best Practices . 

 Review the Elasticsearch System Requirements and provision to at least the recommended minimums. 

 Follow instructions for Single Server Elasticsearch installation. 

 Perform the Server Post-Installation Health Check . 

 Note 

 Multi-tenant deployments have separate requirements and configurations. See the Multi-Tenant Guide for more information. 

 To install Cortex XSOAR on a server without internet connectivity, see Install the Server Offline . 

 When you install Cortex XSOAR for the first time, you are prompted for the default admin password. You should store this password securely for use in an emergency. If the default admin password is lost, the administrator password can be reset . 

 Tip 

 The email for the admin user can be set as the distribution list for multiple administrators of the Cortex XSOAR system. This can be useful when configuring system notifications. 

 If you want to use High Availability with Elasticsearch, see Set Up High Availability . 

 Configure Docker/Podman 

 Docker/Podman is required to run Cortex XSOAR. When installing Cortex XSOAR, Docker/Podman is automatically installed unless running specific operating systems. Follow the Docker Hardening Guide and Docker Network Hardening Guide to efficiently and securely run Docker containers according to best practices. 

 Proxy 

 If using a Proxy , you need to configure Cortex XSOAR and Docker/Podman. 

 Users and Roles 

 After installation, one of your first steps is setting up users, configuring user authentication and appropriate roles and permissions. There are three options for authentication to Cortex XSOAR. 

 SAML : SAML 2.0 is the recommended method to authenticate and authorize users to Cortex XSOAR, as it allows for multi-factor authentication. We strongly recommended implementing MFA and the appropriate conditional access policies at the identity provider. We also recommend you enable signature verification on the incoming SAML authentication token. If using a remote repository, this must be done in both the development and production environments. View the SAML 2.0 video for more information. 

 After setting up SAML, verify you can log in with the default admin account or as a local user, in the event that there are issues with the SAML configuration. 

 Active Directory : Users can log in to Cortex XSOAR with their Active Directory username and passwords, and their permissions in Cortex XSOAR are set according to the groups and mapping set in Active Directory. View the Active Directory video for more information. 

 Local Users: If SAML or Active Directory are not available options, local users can be provisioned. Local users are not the recommended option. 

 We recommend setting up role-based access for users. You can use group memberships from SAML or Active Directory, or assign roles when creating local users. Roles define permissions for users, including limiting access to incidents, dashboards and queries, running integration commands , for scripts, and playbooks, and creating custom content. 

 Tip 

 When deploying a new system, the most common updates to the out-of-the-box Analyst Role include 

 Removing the permission to delete incidents. 

 Removing the permissions to install and contribute Marketplace content. 

 Configuring default dashboards, queries, and shifts. 

 Recommended Server Settings 

 The following are recommended server configurations for new Cortex XSOAR deployments. If you have multiple application servers, each server configuration needs to be added to each Cortex XSOAR server. We recommend you regularly review your server configurations and remove any configurations that are no longer needed. 

 Server Configuration 

 Description 

 instance.execute.external = true 

 Makes External Dynamic Lists (EDLs) or Export Indicators available via port 443 on the server. 

 ignore.default.in.playbooks = true 

 When configuring an integration instance, you can select Do not use by default to prevent commands from exceeding API quotas. The ignore.default.in.playbooks = true configuration enables the same option for playbooks. 

 playbook.willnotexecute.old.eval = false 

 Prevents repeated task checks in playbooks. Repeated task checks can impact performance in large playbooks with many tasks. Do not change to true unless instructed to do so by Customer Support. 

 ui.summary.page.hide.empty.fields = false 

 Shows empty fields in the incident summary tab. 

 demisto.audits.purge = true 

 Enables automatic rolling of the audit logs. 

 demisto.audits.purge.retention = 365 

 Sets the retention period, in days, for the audit logs. 

 To add server configurations, go to Settings → About → Troubleshooting . Server configurations are added as key value pairs. After adding a server configuration, click Save to commit. Server configurations take effect immediately unless otherwise specified. 

 Note 

 Some server configurations are restricted for Hosted Service deployments. If you need to add a server configuration that is not allowed via the UI, open a support ticket specifying the server URL, server environment (development or production), and the requested server configuration. 

 Incidents 

 Classification and Mapping 

 When creating incidents in Cortex XSOAR, use unique incident types for each specific type of alert that is created/ingested. Do not create one incident type for a variety of alerts since this can cause performance issues and make playbook development overly complex. Use classifiers and mappers to make your playbooks more efficient. 

 Pre-Process Rules 

 Consider configuring pre-process rules to drop or close incoming events that are not needed. If you use a pre-processing script, avoid scripts with a long run time as that can delay incident ingestion. 

 Playbooks 

 Quiet Mode 

 Quiet mode prevents tasks from writing unneeded entries to the war room and disables indicator extraction on the task results. Playbooks in quiet mode create only warning and error entries. Indicators are not extracted. Task inputs and outputs are not saved. 

 Individual tasks can be set to quiet mode, or you can set this for the entire playbook and turn off quiet mode for specific tasks that require it. 

 We recommend you configure playbooks which produce large numbers of War Room entries to use quiet mode, in order to reduce the overall size of incidents and improve load times. This is especially relevant for Vulnerability Management playbooks and playbooks running in jobs. TIM playbooks are set by default to use quiet mode. 

 To enable quiet mode for a playbook, edit the Playbook Settings and select Quiet Mode under Advanced . To edit the setting for an individual task, select Use playbook default , On , or Off , in the task's Advanced tab. 

 More information on best practices for playbooks can be found in Playbook Best Practices . 

 Indicator Extraction 

 When configuring playbooks, set indicator extraction to none where possible and extract indicators only in specific tasks where required. 

 Sub-Playbooks 

 If a playbook has more than 30 tasks, consider redistributing some or all of the tasks to sub-playbooks. Sub-playbooks are easier to manage and can be easier to follow. 

 Automations 

 Update automations and integration commands in playbook tasks to their most current version. Automations that have updates are designated by a yellow triangle. 

 Unused Tasks 

 For playbooks in production, remove playbook tasks that are not connected to the playbook workflow. 

 Optimize Parallel Automation Runs 

 When an automation runs, a worker is used. The number of configured workers determines the maximum number of automations that can run in parallel. By default, the number of workers on a Cortex XSOAR instance is 4 x the number of CPU cores. For example, for 8 CPU cores, there are 32 configured workers. 

 Exclude Indicators 

 We recommend you consider deleting and excluding common indicators which appear in a large number of incidents. You can view these indicators in the Top common indicators widget on the Threat Intel / Indicators page. 

 You can manually indicators to the exclusion list or you can define indicators using a regular expression (regex) or CIDR. 

 Regex enables you to identify a sequence of characters in an unknown string. The following example would identify www.demisto.com: [A-Za-z0-9!@#$%\.&]demisto[A-Za-z0-9!@#$%\.&] . 

 Classless inter-domain routing (CIDR) enables you to define a range of IP addresses. For example, the IPv4 block 192.168.100.0/22 represents the 1024 IPv4 addresses from 192.168.100.0 to 192.168.103.255. 

 Excluded indicators are not extracted and enriched and excluding indicators can improve overall system performance. 

 For more information, see Exclusion List . 

 Performance Settings 

 Archive Data 

 We recommend archiving data partitions older than one year. For BoltDB, follow the steps in Free up Disk Space with Data Archiving . For Elasticsearch deployments, follow the steps in Archive Data with Elasticsearch . Hosted customers can request data be archived, via a support ticket. Archived partitions can be provided to hosted customers for offline storage, as needed. 

 Task Indexing (BoltDB) 

 The investigation task indexes are used to index the results of playbook tasks and entries in the War Room. Tasks are indexed in order to perform searches in widgets and incident layouts. Disabling indexes does not affect what is displayed in the Work Plan. To improve performance, we recommend either dropping and disabling these indexes or limiting what is indexed. Hosted customers can request this change via a support ticket. 

 Action 

 How to 

 Disable investigation task indexing and drop these indexes. 

 Add the server configuration "investigation.task.index": false . 

 Delete the invTaskIdx files from /var/lib/demisto/data/invTasIdx* . 

 Enable partial indexing on investigation tasks. 

 You can instead enable partial indexing. Add the server configuration investigation.task.partial.index = 31 . This limits task indexing to manual tasks, tasks with an assignee, tasks with a due date, error state tasks, and large tasks. 

 Limit Workers for Search the Database (BoltDB) 

 For performance optimization, we recommend limiting the number of workers used to search the database. This ensures that as system usage increases, analyst or playbook searches for incidents do not overburden server resources required for running playbooks. 

 You can edit the demisto.conf file to add workers.count.search = 3 to restrict the number of available workers for searching the BoltDB database. 

 Before you start create a backup of /etc/demisto.conf file. 

 Edit the /etc/demist.conf file 

 To limit the number of workers, for example, to 3, add " workers.count.search":"3 " to the file. 

 Restart Cortex XSOAR. 

 sudo systemctl restart demisto 

 System Diagnostics 

 The System Diagnostics page enables you to monitor and improve system performance and resilience. You can view the System Diagnostics page at Settings → About → System Diagnostics . System diagnostics thresholds can be customized for your deployment through server configurations, and you can also enable and disable email notifications and change the recipients. 

 Server Monitoring 

 We recommend setting up system monitoring using both Cortex XSOAR tools and independent monitoring tools to run on the Cortex XSOAR server. Monitoring tools should generate alerts for sustained CPU, sustained high memory usage, and high disk usage (operating system and Cortex XSOAR data disk). 

 In addition, the /workers/status API endpoint provides information about the number of available workers and running workers consumed by automations in playbooks. Workers are consumed as required. If the number of busy workers = available workers for extended periods of time, this could indicate an issue with a playbook or integration. The /workers/status API endpoint shows the tasks that are holding workers; this information can be used for troubleshooting. 

 The /health/containers API endpoint shows the number of Docker containers running on the server. Containers are started/stopped by Cortex XSOAR as required, and a number of containers are kept running on standby. If the number of running containers is above 100 for an extended period of time, then this could indicate high load or potentially an issue with the Docker sub-system. 

 Engines 

 Cortex XSOAR engines are installed in a remote network and allow communication between the remote network and the Cortex XSOAR server. You can run scripts and integration commands on an engine to offload work from the Cortex XSOAR server. Engines also act as a go-between, allowing connections to integrations that the server may not be able to access directly. For hosted service deployments, engines enable connectivity between the hosted Cortex XSOAR server and on-premise infrastructure. 

 You can deploy one or more engines depending on your requirements and the integrations you are connecting to. Review the engine requirements and network requirements for engines. 

 Engine installers can be created via Settings → Engines . We recommend installing engines using the Shell script as the install method, if available for your operating system, as this enables you to later upgrade your engine from within the UI. 

 After updating your servers to a new version/build, you must upgrade your engine(s) as well. If the engine was deployed using the Shell installer, this can be done via the UI from Settings → Engines . 

 Marketplace 

 The Cortex XSOAR Marketplace is the central location for installing , exchanging, contributing , and managing all of your content, including playbooks, integrations, automations, fields, layouts, and more. 

 When a Content Pack is available for update, you see a notification next to the Marketplace icon. You can update to the latest content version or to a specific version. All dependent Content Packs update automatically with the Content Pack. We recommend periodically reviewing your installed Marketplace packs for any available updates, and updating as required. 

 Integrations 

 Integrations are configured on the Settings > Integrations page. 

 Email Integrations 

 We recommend configuring an email integration during your initial set up. An email integration enables the server to send emails and can be used for system notifications and playbooks. The following are the most frequently used integrations for email: 

 EWS v2 

 Mail Sender (New) 

 IoT Security Third-party Integrations Add-on 

 You can use use Cortex XSOAR with IoT Security to integrate with third-party systems without buying an IoT Security Third-party Integration Add-on license. For Cortex XSOAR to support IoT Security third-party integrations, you must install the IoT Security content pack and configure an integration instance on the Cortex XSOAR server. The content pack contains third-party integrations, playbooks, and jobs. 

 Go to the IoT Security portal to download the latest version of the IoT Security content pack. For more details, see the IoT Security Integration Guide . 

 Integration Credentials 

 When applicable, use the Cortex XSOAR Credentials page at Settings → Integrations → Credentials to store credentials used for integrations. Credentials are stored encrypted in the database and can be updated on the Credentials page. Changes made on the Credentials page apply automatically to all integrations that are configured to use the credential. 

 Integrations that support credentials have an option to Switch to Credentials and allow you to pick the credential from the list. 

 Integrations should be updated as needed, to the latest version. We recommend you remove deprecated integrations that are no longer maintained or updated, as well as any integrations that are no longer needed. To find deprecated integrations that are still in use, go to Settings → Instances and view Enabled instances, with the filter option set to Show Deprecated . 

 Integration Use Cases 

 This section includes common use cases for the different categories of Cortex XSOAR integrations. While this list is not meant to be exhaustive, it's a good starting point for you to understand what use cases could be supported by your integration. 

 Subject 

 Top Use Cases 

 Analytics and SIEM 

 Fetch Incidents with relevant filters 

 Create, close and delete incidents/events/cases 

 Update Incidents - Update status, assignees, Severity, SLA, etc. 

 Get events related to an incident/case for enrichment/investigation purposes 

 Query SIEM (consider aggregating logs) 

 Note 

 Ususally includes the Fetch Incidents possibility for the instance. It can also include list-incidents or get-incident as integration commands, or important information for an Event/Incident. 

 Analytics & SIEM Integration Example: ArcSight ESM 

 Authentication 

 Use credentials from the authentication vault in order to configure instances in Cortex XSOAR. (Save credentials in: Settings → Integrations → Credentials .) The integration should include the isFetchCredentials parameter, and other integrations that will use credentials from the vault, should have the Switch to credentials option. 

 Lock/Delete Account – Use an integration to lock/unlock a third party account. 

 Reset Account - Perform a reset password command for a third party account 

 Lock an external credentials vault - in case of emergency (if the vault has been compromised), allow the option to lock/unlock the entire vault via an integration. 

 Step-Up authentication - Enforce Multi Factor Authentication for an account. 

 Authentication Integration Example: CyberArk AIM 

 Case Management 

 Create, get, edit, close a ticket/issue, add + view comments 

 Assign a ticket/issue to a specified user 

 List all tickets, filter by name, date, assignee 

 Get details about a managed object, update, create, delete 

 Add and manage users 

 Case Management/Ticketing Integration Example: ServiceNow 

 Data Enrichment & Threat Intel 

 Enriching information about different IOC types: Upload object for scan and get the scan results. (If there’s a possibility to upload private/public, the default should be set to private.) Search for former scan results about an object. (This way you can get information about a sample without uploading it yourself.) Enrich information and scoring for the object. 

 Add/Search for indicators in the system 

 Add indicators to the exclusion list 

 Calculate DBot Score for indicators 

 Data Enrichment & Threat Intelligence Integration Example: VirusTotal 

 Email Gateway 

 Get message – Download the email itself, retrieve metadata, body 

 Download attachments for a given message 

 Manage senders – Block/ Allow specified mail senders 

 Manage URLs – Block/ Allow the sending of specified URLs 

 Encode/ Decode URLs in messages 

 Release a held message (The gateway can place suspicious messages on hold, and sometimes they would need to be released to the receiver.) 

 Email Gateway Integration Example: MimeCast 

 Endpoint 

 Fetch Incidents & Events 

 Get event details (from specified incident) 

 Quarantine File 

 Isolate and contain endpoints 

 Update Indicators (Network, hashes, etc.) by policy (can be block, monitor) – deny list 

 Add indicators to the exclusion list 

 Search for indicators in the system (Seen indicators and related incidents/events) 

 Download file (based on hash, path) 

 Trigger scans on specified hosts 

 Update .DAT files for signatures and compare existing .DAT file to the newest one on the server 

 Get information for a specified host (OS, users, addresses, hostname) 

 Get policy information and assign policies to endpoints 

 Endpoint Integration Examples: Cortex XDR, Tanium and Carbon Black Protection 

 Forensics and Malware Analysis 

 Submit a file and get a report (detonation) 

 Submit a URL and get a report (detonation) 

 Search for past analysis (input being a hash/URL) 

 Retrieve a PCAP file 

 Retrieve screenshots taken during analysis 

 Sandbox Integration Example: Cuckoo Sandbox 

 Network Security (Firewall) 

 Create block/accept policies (Source, Destination, Port), for IP addresses and domains 

 Add addresses and ports (services) to predefined groups, create groups, etc. 

 Support custom URL categories 

 Fetch network logs for a specific address for a configurable time frame 

 URL filtering categorization change request 

 Built-in blocked rule command for fast-blocking 

 If there is a Management FW, allow the option to manage policy rules through it 

 Network Security Firewall Integration Example: Palo Alto Networks PAN-OS 

 Network Security (IDS/IPS) 

 Get/Fetch alerts 

 Get PCAP file, packet 

 Get network logs filtered by time range, IP addresses, ports, etc. 

 Create/manage/delete policies and rules 

 Update signatures from an online source / upload + Get last signature update information 

 Install policy (if existing) 

 Network Security (IPS/IDS) Integration Example: Protectwise 

 Vulnerability Management 

 Enrich asset – get vulnerability information for an asset (or a group of assets) in the organization 

 Generate/Trigger a scan on specified assets 

 Get a scan report including vulnerability information for a specified scan and export it 

 Get details for a specified vulnerability 

 Scan assets for a specific vulnerability 

 Vulnerability Management Integration Example: Tenable.io 

 Troubleshooting and Support 

 When creating a support ticket, include the Cortex XSOAR logs . 

 Change Log Level and Download Logs 

 Go to Settings → About → Troubleshooting and set the log level to Debug . 

 Reproduce the issue. 

 Go back to Settings → About → Troubleshooting and download the logs. 

 Attach the logs to the support ticket. 

 Go back to Settings → About → Troubleshooting and change log level back to desired setting. The default level is Info . 

 Audit Logs 

 The audit trail displays a log of all administrative user interactions with Cortex XSOAR. The log is sorted by date and shows which users interacted with system objects and associated data and the details of these interactions. 

 The audit trail does not include actions performed in the War Room . These actions are documented only in the War Room . 

 You can search the audit trail log for user interactions based on free text. To view the audit trail, navigate to Settings → Users and Roles → Audit Trail . You also have the option to send the audit log to an external syslog service . 

 By default, audit logs are stored for 365 days. We recommend automatically purging the audit trail logs, by adding the demisto.audits.purge and demisto.audits.purge.retention server configurations, as listed in Logs Server Configurations . You can also manually purge older logs in batches, using the Cortex XSOAR API. We recommend doing this in one-month batches to avoid performance issues during purging. 

 If you want to drop older audit logs completely and start new log files, you need to open a support ticket request. You should verify the current logs are properly stored in the external log server prior to purging all data. 

 Backups 

 Cortex XSOAR BoltDB deployments have an option for automated backups, configured at Settings → Advanced → Backups . By default, the backups are stored at /var/lib/demisto/backup , but should also be copied to a separate storage solution/server offline using appropriate enterprise backup software. 

 Cortex XSOAR Elasticsearch deployments use Elasticsearch snapshots , which can be configured through the Elasticsearch API. 

 Disaster Recovery and Live Backup 

 Live Backup enables you to mirror your production server to a backup server. In a disaster recovery situation, you can easily convert your backup server to be the production server. 

 Note 

 When using Cortex XSOAR with Elasticsearch, Live Backup is not available. To back up or restore the contents of your Elasticsearch database, follow the instructions for Disaster Recovery for Elasticsearch. Alternatively, you can implement a full high availability solution. 

 Integrations and Incidents Health Check 

 The Integrations and Incidents Health Check content pack enables users to review all of the failed integrations, incidents, and playbooks. This pack is available from the Cortex XSOAR Marketplace and works in tandem with System Diagnostics to enable administrators to manage their deployments. 

 The Integrations and Incidents Health Check content pack includes out-of-the-box layouts, dashboards, an incident type, and incident fields. All of these are customizable to suit the needs of your organization. You can configure the job on an hourly/daily/weekly basis to perform the health check. The job will run the checkup playbook that tests all enabled integrations and searches for open incidents with errors to get their status and retrieve error information 

 Content Management 

 Cortex XSOAR provides three options for content management : manual, remote repositories and CI/CD . 

 Note 

 Configuration settings, such as integration instance configurations including URLs, usernames, passwords, etc., are not considered content and must be manually updated for each Cortex XSOAR environment. 

 In addition to remote repositories and CI/CD, you can also manually export custom content from one Cortex XSOAR server to another. In this case, you export either a single content item (download from the content item page) or all custom content (via Settings → About → Troubleshooting Export Custom Content) and then either upload the single item or import all custom content (via Settings → About → Troubleshooting Import Custom Content) on the destination machine. The community supported XSOAR - Simple Dev to Prod content pack enables you to create a custom content bundle with only selected items from the server’s custom content. If you are not using a remote repository or CI/CD, marketplace packs must be installed and maintained on each Cortex XSOAR environment and manually synced as needed. 

 Install the Slack Content Pack 

 If your organization uses Slack, we recommend installing the Slack content pack. The Slack content pack enables you to send messages and notifications to your Slack team and integrates with Slack's services to execute create, read, update, and delete operations for employee lifecycle processes. 

 Strata Logging Service 

 You can integrate Strata Logging Service with Cortex XSOAR, which provides cloud-based, centralized log storage and aggregation for your on-prem, virtual (private cloud and public cloud) firewalls, Prisma Access, and cloud-delivered services such as Cortex XDR. You can activate this using the PANW Hub . For more information about the hub, see Getting Started with the PANW Hub . 

 To use Strata Logging Service in Cortex XSOAR, install the Strata Logging Service Content Pack to run queries for critical threat logs, social applications, threat logs, etc. You can also Install the PAN-OS to Strata Logging Service Monitoring content pack to monitor the PAN-OS FW log in a recurring job. 

 For more information about Strata Logging Service, see Getting Started with Strata Logging Service . 

 Server Upgrades 

 To upgrade your server, download the latest version via the download link you received in your welcome email. If you have lost your download link, request a new one through the Palo Alto Support Portal. 

 You can subscribe to the release announcements via our Live Community to be notified when new versions are available. Notifications include a link to the release notes. 

 The release announcements page has a Subscribe button. You can manage your subscriptions from the My Settings page, under Subscriptions & Notifications → My Subscriptions . The Notification Settings tab enables you to turn on or off email, push, and mobile notifications. 

 If you have engines deployed, upgrade deployed engines after upgrading the server. If the engine was deployed using the Shell installer, upgrading can be done via the UI from Settings → Engines . 

 Multi-Tenant Deployments 

 Monitoring Multi-Tenant Deployments 

 We recommend installing the Multi-Tenant Performance content pack for monitoring CPU, disk, and memory usage, as well as the number of active Docker containers. The content pack collects information from each host server and displays the data in dashboards. 

 Note 

 If you are using a non default partition for your hosts and you want to monitor it, add the server configuration server.disk.partition on the hosts. The value should be the path and name of the partition. 

 Server Configurations for Multi-Tenant Deployments 

 Server configurations do not automatically propagate to tenants, but any configurations that you push from the main account are sent to all tenant accounts. There is no option to specify a subset of tenant accounts. 

 Multi-Tenant Propagation Labels 

 By default, the label for content items is all , which means the content item is pushed to all tenant accounts. A tenant with no labels receives only content with the all label. 

 A content item with no labels is not pushed to any tenants. 

 If you create custom propagation labels, both the content and the tenant account must have the same propagation label for the content to be pushed from the main account to the tenant account. 

 For more information, see Manage Content in the Cortex XSOAR Multi-Tenant Guide. 

 Content Syncing 

 To push content to tenant accounts, you select the tenant(s) from the Account Management page on the main account, and click Sync . You have the option to not sync selected content items. For more information about syncing content, see Sync Content to Tenant Accounts . 

 Integrations 

 Integrations must be installed and pushed from the main account to tenant accounts. Some integration instances can be configured on the main account before being propagated to tenant accounts. Others need to be configured directly on the individual tenants. 

 Reference 

 Performance Tuning for Cortex XSOAR - Troubleshoot performance issues including memory usage, CPU spikes, slow playbooks, and WebSocket errors. 

 Monitor Components - Monitor the server and engines. 

 Cortex XSOAR Playbook Best Practices - Design and build playbooks. 

 Previous Onboarding in Cortex XSOAR 

 Next Single Server Deployment 

 Last updated 20 days ago 

 Was this helpful?
