---
url: https://docs.paloaltonetworks.com/sd-wan/activation-and-onboarding/upgrade-sd-wan-plugin
fetched_at: 2026-08-13T17:35:03Z
source: palo-alto-main
---

# Upgrade SD-WAN Plugin with Compatible PAN-OS Release Clear

Upgrade SD-WAN Plugin with Compatible PAN-OS Release 

 Home 

 EN

 Location 

 Documentation Home 

 Palo Alto Networks 

 Support 

 Live Community 

 Knowledge Base 

 >

 Strata Copilot

 Upgrade SD-WAN Plugin with Compatible PAN-OS Release 

 Updated on 

 Thu Jul 30 16:29:46 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 SD-WAN Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Help 

 Select a Document 

 3.4 

 3.3 

 3.2 

 3.1 

 3.0 

 2.2 

 2.1 

 2.0 

 1.0 

 Release Notes 

 New Features 

 Updated on 

 Thu Jul 30 16:29:46 PDT 2026 

 Focus 

 Home 

 SD-WAN 

 Upgrade SD-WAN Plugin with Compatible PAN-OS Release 

 Download PDF 

 SD-WAN 

 Upgrade SD-WAN Plugin with Compatible PAN-OS Release 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 SD-WAN Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Help 

 Select a Document 

 3.4 

 3.3 

 3.2 

 3.1 

 3.0 

 2.2 

 2.1 

 2.0 

 1.0 

 Release Notes 

 New Features 

 Previous 

 Plan Your SD-WAN Configuration 

 Next 

 Upgrade your SD-WAN Firewalls 

 Upgrade SD-WAN Plugin with Compatible PAN-OS Release 

 Before upgrading the SD-WAN plugin, you need to take the backup of the
 configuration file, generate a technical support file, and install a compatible content
 release version. 

 Where Can I Use This? What Do I Need? 

 NGFW 

 Advanced SD-WAN for NGFW 

 It’s imperative to ensure that an existing network infrastructure remains up to
 date and is capable of upgrading its features to unlock new functionalities. The SD-WAN upgrade guide helps the network administrators to upgrade the
 Panorama management server and Palo Alto Networks firewalls that are compatible with the
 SD-WAN plugin release. 

 ( Versions earlier
 than SD-WAN 3.4.0 ) 
 It is important
 that you have a proper upgrade or downgrade plan before starting actual upgrade or
 downgrade procedure. Refer the valid upgrade and downgrade paths for your currently
 installed SD-WAN plugin
 version. 

 ( PAN-OS 12.1.2 and later versions, SD-WAN 3.4.0 and
 later versions ) The Panorama plugin bundling in PAN-OS 12.1.2 addresses a
 critical operational challenge you face when upgrading Panorama versions.
 Previously, you needed to manually ensure compatibility between the PAN-OS version
 and the corresponding SD-WAN plugin version. 

 Beginning with the PAN-OS 12.1.2, the SD-WAN plugin is bundled within the
 Panorama , ensuring that the SD-WAN plugin version is
 always compatible with your PAN-OS version. When you upgrade your Panorama
 management server, any SD-WAN plugin version you had previously
 installed and configured will automatically upgrade to the new compatible version
 while preserving all existing configurations and data. This seamless transition
 reduces the risk of configuration loss during upgrades. 

 Additionally, Panorama automatically validates resource requirements before
 enabling SD-WAN plugin, preventing scenarios where plugin processes
 fail to start due to insufficient memory or system resources. The Panorama plugin
 bundle approach also enables you to receive plugin updates through regular
 maintenance releases, rather than requiring separate plugin installation procedures
 that could introduce compatibility issues or service disruptions. 

 If your Panorama management server runs a version newer than PAN-OS® 10.1 (such as
 PAN-OS 10.2) when you add a new device PAN-OS® 10.1 to SD-WAN cluster, the
 commit-all operation fails. To ensure a successful push, your Panorama and firewalls
 must run the same version for PAN-OS 10.1.x. 

 Before proceeding with the upgrade process, ensure the following: 

 Take a backup of all the configurations on each device. 

 Refer Panorama plugin compatibility matrix to
 review the features introduced in each version of the Panorama plugin for SD-WAN . 

 You have administrator access to the Palo Alto Networks devices. 

 If panorama is in HA, they must be in synchronized state. 

 All managed HA pairs, which are integral to the SD-WAN cluster, must be healthy and
 synchronize accurately with Panorama. They must operate in an active/passive
 configuration, which the active and passive Panorama management server must
 maintain. 

 Ensure that the commit is synchronized on all the managed firewalls: 
 No pending configuration commits on panorama should exist. 

 Ensure that the `commit-all` operation has been successfully executed and
 all current configurations are synchronized and applied across the
 network. 

 All Device Groups (DGs) and Template Stacks (TSs) must be in synchronization
 on both the active and passive Panorama devices. 

 All tunnels across all SD-WAN clusters are fully operational and report
 Up . You must maintain the stability of these tunnels for
 uninterrupted connectivity throughout the upgrade process. 

 Prerequisites 

 Before you upgrade the Panorama HA pair, it's important to save the configuration
 files, create a technical support file, and check for the compatible content release
 version for your device. Contact Palo Alto Network support team for further
 assistance. 

 MongoDB Database Backup : It is imperative to take a complete backup of
 the MongoDB database from Panorama. This database is important as it contains
 all critical SD-WAN configuration, operational parameters, and historical
 data. 
 Take backup of the MongoDB. Navigate to the Root Directory: cd /

 Execute mongodump command to backup 
 pl_sd_wan database to the specified output directory.

 mongodump --db pl_sd_wan -o 
/opt/panlogs/ld1/mdump 

 Change to the `var/cores` directory: 
 cd
 var/cores 

 Create a Gzipped tar archive to compress the backed-up MongoDB data for
 efficient storage and
 transfer. 

 tar cvzf mdump-plsdwan.tar.gz /opt/panlogs/ld1/mdump 

 After creating the archive, transfer the
 mdump-plsdwan.tar.gz to a secure external location:

 To an SCP server, or 

 Download it locally by navigating to Device Support Core Files and select the
 mdump-plsdwan.tar.gz file 
 This redundancy ensures that the backup remains accessible even if
 Panorama encounters issues. 

 The cluster_map.xml files contain vital information regarding
 the specific SD-WAN cluster configurations for each device. Use the following
 workflow to back up files to restore SD-WAN functionality if an unforeseen issue
 or rollback requirement occurs. 
 Navigate to the SD-WAN
 plugin: 

 cd /opt/pancfg/mgmt/plugins/appdata/sd_wan/ 

 Archive the `candidate-configs` directory that contains the
 device-specific configuration
 files. 

 tar cvzf candidate-configs.tar candidate-configs/ 

 Save the archive in /var/cores to make it available
 for download through the Panorama web
 interface. 

 cp candidate-configs.tar.gz /var/cores/ 

 Similar to the MongoDB backup, transfer the
 candidate-configs.tar.gz file to a secure SCP
 server or download it locally from the Panorama web interface ( Device Support Core Files ). 

 Take a complete configuration snapshot of Panorama that provides a precise,
 point-in-time record of the entire network configuration. This snapshot must
 encompass all device groups, templates, and shared policies, making it crucial
 for a successful rollback if any issues arise during or after the upgrade
 process. 

 Capture and save the output of the show devices all command
 for Panorama. Save this output ( 
 https://<panorama-ip>/php/rest/browse.php/op::show::devices::all )
 to a file because it provides a comprehensive list of all managed devices and
 their current status, allowing it to easily confirm device connectivity and
 management status during pre- and post-upgrade comparisons. 

 Disable preemption before the upgrade to avoid unnecessary failover, and enable
 it once the upgrade is complete. Disabling preemption is critical because when
 it is enabled, a recovering device might immediately reclaim its primary role,
 leading to unnecessary failovers, split-brain conditions, and extended downtime.
 Therefore, the procedure requires to deactivate preemption before the upgrade,
 perform the upgrade on both devices, and then reactivate it once the system
 stabilizes, ensuring a smoother and more effective maintenance window. 

 Back up Your Configuration File 

 Make a backup of the current configuration file. It's recommended to make a
 backup of your current Panorama and firewall configurations: 

 Take the backup of the Panorama and firewall
 configurations before upgrading the device. Perform device state
 backups for the hub firewalls and other strategically identified critical
 sites. In large deployments, comprehensive site backups may be impractical.
 Ensure you prioritize hub firewalls (central connectivity points) and
 business-critical branches for backup coverage. These backups capture the
 operational state and specific configurations of individual firewalls,
 providing a localized recovery point if a single firewall experiences
 issues. 

 Save and export Panorama and firewall
 configurations to restore that backup. 

 Save and export firewall
 configurations to revert to that backup. 

 If you have problems with the upgrade, you can use these backups to
 restore the configuration by loading the configuration backup on the
 firewall managed by the Panorama management server. 

 Generate a Technical Support File 

 It's important to generate the technical support file for debugging purposes. 

 Select Device Support and Generate Tech Support File . 
 The
 technical support file must be generated on both the Panorama HA pair
 for debugging purposes. 

 It
 may take a few minutes to generate a technical support file and the time
 taken to generate would vary. 

 Click Yes when prompted to generate the tech support
 file. 

 Click Download Tech Support File to save it in the
 firewall or Panorama. 

 Install Compatible Content Release Version 

 Ensure that each firewall and Panorama HA pair is running the latest content
 release ( Applications and Threats ) version. 

 All the firewalls and the Panorama must have the same
 version of Applications and Threats downloaded and
 installed for the upgrade to be successful. 

 Refer to the corresponding release notes for the minimum content
 release (such as, Applications and Threats ) version you
 must install for a corresponding PAN-OS release. Make sure to follow the best practices for applications and threat
 content updates . 

 Your firewall and the Panorama running a specific PAN-OS version must contain the
 minimum content release ( Applications and Threats )
 version that’s compatible with the PAN-OS version. 

 Use the following workflow to download and install the content release version
 that’s compatible with the PAN-OS version: 

 For the firewall, select Device Dynamic Updates and for Panorama select Panorama Dynamic Updates to check the version information of the
 Applications and Threats . 

 Check Now to retrieve a list of available
 updates. 

 Locate and Download the appropriate content release
 version. After you successfully download a content update file, the link in
 the Action column changes from Download to
 Install for that content release version. 

 Install the update on the Palo Alto Networks
 firewalls. 

 Important Considerations for Upgrading Panorama 

 The following are the important considerations for upgrading the SD-WAN plugin version on your Panorama management server: 

 ( HA Deployments only ) Both the active and passive Panorama must
 have the same Panorama software and SD-WAN plugin
 versions. 

 ( HA Deployments only ) Maintain the same HA states for both Panorama
 and Palo Alto Networks Next-Generation Firewalls after upgrade and before
 commit or commit all, so that the configuration changes
 are minimal. 

 The Panorama software version must be greater than or equal to the PAN-OS
 version 

 For MongoDB synchronization status for an SD-WAN plugin
 version, refer to MongoDB synchronization
 status with SD-WAN database collections . 

 ( HA Deployments only ) ( For upgrades from prior SD-WAN
 plugin versions to SD-WAN version 2.2.7 ) You must upgrade both
 active and passive Panorama HA pairs simultaneously. 

 After completing the SD-WAN plugin upgrade, you must
 perform a commit force through the CLI command (in configuration mode)
 on the Panorama devices. If you perform commit all instead of commit
 force, then you may lose all the SD-WAN configurations on
 that device. 

 After the upgrade is complete, verify the changes after the
 upgrade . 

 Previous 

 Plan Your SD-WAN Configuration 

 Next 

 Upgrade your SD-WAN Firewalls 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Activate a License or Product 

 Cloud Identity Engine 

 Strata Logging Service 

 Device Associations 

 Hub 

 Identity and Access Management 

 Tenant Management 

 Next-Generation Firewalls 

 AIOps for NGFW 

 Cloud Management for NGFWs 

 Cloud NGFW for AWS 

 Cloud NGFW for Azure 

 CN-Series 

 Firewalls 

 PAN-OS 

 Service Provider 

 VM-Series 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 AI-Powered ADEM 

 Prisma Access Monitoring and Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

 Cloud-Delivered Security Services 

 Advanced WildFire 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 IoT Security 

 Enterprise DLP 

 SaaS Security 

 Network Security 

 Shared Policy for NGFWs and Prisma Access 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Network Security 

 Activation & Onboarding 

 Next-Generation Firewall 

 SD-WAN 

 English 

 Panorama 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
