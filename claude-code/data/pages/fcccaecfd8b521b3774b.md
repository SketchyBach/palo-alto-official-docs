---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsoar-6-installation-guides/6.14/cortex-xsoar-installation-guide/upgrade-your-installation/upgrade-the-live-backup-environment
fetched_at: 2026-09-16T08:58:35Z
source: cortex-platform
---

# Upgrade the Live Backup Environment | 6.14  | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Installation Guides 

 6.14 

 Cortex XSOAR Installation Guide 

 Upgrade Your Installation 

 Cortex XSOAR 6.14 Installation 

 Upgrade the Live Backup Environment 

 Upgrade the Cortex XSOAR 6.14 live backup environment. 

 Live Backup enables you to mirror your production server to a backup server. In a disaster recovery situation, you can easily convert your backup server to the production server. See Disaster Recovery and Live Backup Overview for more details. 

 Caution 

 Before you begin, verify that your system meets the system requirements, including the required operating system. 

 Note 

 The -y flag answers all installer questions with y/yes and uses default settings, including accepting the Cortex XSOAR EULA. If you apply the -y flag when upgrading the Live Backup Environment, it will use /tmp as the backup directory. If there is insufficient space in the /tmp directory to back up the /var/lib/demisto/data directory, the upgrade will fail. 

 Follow this procedure when upgrading your Cortex XSOAR version. 

 Stop the main Cortex XSOAR server and the DR Cortex XSOAR server by typing the following command. 

 sudo systemctl stop demisto 

 Upgrade the DR Cortex XSOAR server. 

 sudo ./demistoserver-X.sh -- -dr -y 

 (Multi-tenant) - For multi-tenant deployments: sudo ./demistoserver-X.sh -- -multi-tenant -dr -y 

 Upgrade the main Cortex XSOAR server. 

 sudo ./demistoserver-X.sh -- -y 

 (Multi-tenant) - For multi-tenant deployments: sudo ./demistoserver-X.sh -- -multi-tenant -y 

 If the DR Cortex XSOAR server did not start, restart the DR Cortex XSOAR server. 

 sudo systemctl start demisto 

 If the main Cortex XSOAR server did not start, restart the main Cortex XSOAR server. 

 sudo systemctl start demisto 

 Previous Upgrade Your Multi-Tenant Deployment 

 Last updated 1 month ago 

 Was this helpful?
