---
url: https://docs.paloaltonetworks.com/sd-wan/release-notes/panorama-plugin-for-sd-wan/sd-wan-plugin-330/known-issues-in-sd-wan-plugin-330
fetched_at: 2026-08-13T17:36:03Z
source: palo-alto-main
---

# Known Issues in SD-WAN Plugin 3.3 Clear

Known Issues in SD-WAN Plugin 3.3 

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

 Known Issues in SD-WAN Plugin 3.3 

 Updated on 

 Thu Jul 30 23:22:25 PDT 2026 

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

 Thu Jul 30 23:22:25 PDT 2026 

 Focus 

 Home 

 SD-WAN 

 Panorama Plugin for SD-WAN 

 Panorama Plugin for SD-WAN 3.3 

 Known Issues in SD-WAN Plugin 3.3 

 Download PDF 

 SD-WAN 

 Known Issues in SD-WAN Plugin 3.3 

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

 Changes to Default Behavior in SD-WAN Plugin 3.3.1 

 Next 

 Panorama Plugin for SD-WAN 3.2 

 Known Issues in SD-WAN Plugin 3.3 

 Known issues in SD-WAN 3.3. 

 The following list includes all known issues that impact an SD-WAN 3.3
 release. This list includes both outstanding issues and issues that are addressed, as
 well as known issues that apply more generally or that are not identified by a specific
 issue ID. Refer to PAN-OS Release Notes for additional known
 issues affecting SD-WAN Plugin 3.3. 

 PAN-280467 

 Description of PAN-280467. 

 When multiple VPN clusters with post-quantum pre-shared key ( PQ PPK ) share a hub firewall, SD-WAN tunnel
 functionality is impacted as follows: 
 the SD-WAN tunnels become nonfunctional from the second PQ PPK cluster onwards.
 However, the first VPN cluster with the shared hub firewall will work fine. 

 the shared hub firewall cannot simultaneously support some clusters with PQ PPK
 enabled and others using standard PSK authentication. That is, all VPN clusters
 connected to a shared hub firewall must either use PSK or use PQ PPK. 

 PAN-273413 

 Description of PAN-273413. 

 When you add a new SD-WAN hub or branch firewall to an existing PQ PPK enabled SD-WAN
 cluster, the IKE/IPSec SA configuration resets automatically (causing IPSec tunnel
 flaps) for all the devices in the cluster. 

 PAN-273286 

 Description of PAN-273286. 

 When you add a new SD-WAN cluster with a shared hub, then the IKE/IPsec SA configuration
 resets automatically (causing IPSec tunnel flaps) for all the devices in those clusters
 with the shared hub. The IPSec tunnel flapping occurs when at least one of the SD-WAN
 clusters is PQ PPK enabled with a shared hub firewall. 

 PAN-261971 

 Description of PAN-261971. 

 If the SD-WAN branch firewall is a multi-DP firewall (that is, a firewall model with
 multiple data planes and/or multiple slots), it drops the traffic sent over the non-DIA
 virtual interface when the multiple virtual routers are configured on the firewall. 

 PLUG-23014 

 Description of PLUG-23014. 

 Fixed an issue on the Monitoring site detail page where the Prisma Access Onboarding
 section becomes visible when you change the browser resolution, even if the Cloud
 Service plugin is not installed. 

 This issue is addressed in SD-WAN plugin 3.3.4-h1. 

 PLUG-22748 

 Description of PLUG-22748. 

 Fixed an issue where adding an upstream NAT IP address to a new subinterface in an
 aggregate group caused the system to duplicate the NAT IP across both subinterfaces. 

 This issue is addressed in SD-WAN plugin 3.4.2 , 3.2.4-h2 and 3.3.4-h1. 

 PLUG-22581 

 Description of PLUG-22581. 

 Fixed an issue where a Panorama plugin upgrade failed because Panorama is in FIPS-CC
 mode. Run

 > debug plugins sd_wan export-mongo-collections deletepass 

 > debug plugins sd_wan export-mongo-collections export 

 for troubleshooting. 

 This issue is addressed in SD-WAN plugin 3.3.4, 3.3.4-h1 , 3.4.2 and
 3.2.4-h2 . 

 PLUG-22317 

 Description of PLUG-22317. 

 If your Panorama management server runs a version newer than PAN-OS® 10.1 (such as PAN-OS
 10.2) when you add a new device PAN-OS® 10.1 to SD-WAN cluster, the commit-all operation
 fails. To ensure a successful push, your Panorama and firewalls must run the same
 version for PAN-OS 10.1.x. 

 PLUG-21660 

 Description of PLUG-21660. 

 ( HA Deployments only ) When you remove one of the peers of an SD-WAN HA device
 from a VPN cluster, a commit error occurs because the plugin requires both HA peers to
 be present in the cluster. The commit error persists, but now includes a more
 informative error message to help identify the serial number that needs to be
 updated. 

 This issue is addressed in SD-WAN plugin 3.2.4-h1 ,
 3.3.3-h2 and
 3.4.1 . 

 PLUG-21340 

 Description of PLUG-21340. 

 Panorama now includes a preventative fix to ensure tunnel IP addresses remain
 synchronized. As part of this fix, the following CLI command is deprecated:
 debug plugins sd_wan drop-config-cache . 

 Workaround 

 To resolve the synchronization issue, first perform a configuration push to the affected
 Branch node to generate the new tunnel monitor IP address. Once the push is complete,
 identify the new tunnel monitor IP address and manually enter it into the BGP Peer IP
 field for the corresponding peer in the Panorama Cloud Services plugin. Finally, perform
 a configuration push to the Remote Network (RN) to align the settings and restore
 connectivity. 

 This issue is addressed in SD-WAN plugin 
 3.0.9-h1 , 3.4.2 , 3.3.4 and 3.5.0 . 

 - PAN-OS 12.2.2 or later versions 

 PLUG-20345 

 Description of PLUG-20345. 

 Panorama configuration push fails when the hub and branch firewalls with logical router
 configuration are bulk imported using the SD-WAN plugin's CSV import feature. 

 This issue is addressed in SD-WAN plugin 3.3.3-h1. 

 PLUG-20267 

 Description of PLUG-20267. 

 Your local commit on Panorama will fail when an invalid HA pair is present in your SD-WAN
 cluster, as the SD-WAN plugin does not support active/active HA configurations within
 VPN clusters. 

 This issue is addressed in SD-WAN plugin 3.2.4 
 , 3.0.9 and 3.3.3-h2 . 

 PLUG-20071 

 Description of PLUG-20071. 

 Redundant 4-byte ASN entries were created in the hub configuration when connected to
 multiple branches with the 4-byte ASN feature enabled. 

 This issue is addressed in SD-WAN plugin 3.3.3-h2 , 3.4.1 ,3.3.4 and 3.2.4-h1 . 

 PLUG-19986 

 Description of PLUG-19986. 

 The SD-WAN plugin requires unique interface numbers across different interface types. The
 commit all operation on managed firewalls fails if you mix the interface types (such as,
 Ethernet, Cellular) with the same interface number. For example, the configuration push
 or commit all operation fails if your SD-WAN configuration contains Ethernet and
 Cellular interface types with the same interface numbers, like ethernet1/1 and
 cellular1/1. 

 Workaround : Ensure that you don't use the same interface number for different
 interfaces for your firewalls. Always verify interface numbering when configuring SD-WAN
 interfaces to prevent deployment issues. 

 This issue is addressed in SD-WAN plugin 3.3.3-h1 
 and 3.4.0 . 

 PLUG-19495 

 Description of PLUG-19495. 

 The commit all operation in Panorama fails when a branch or hub firewall is added to an
 existing SD-WAN cluster. 

 This issue is addressed in SD-WAN plugin 3.2.3-h2, 3.2.4, 3.3.3 , and 3.4.0 . 

 PLUG-19165 

 Description of PLUG-19165. 

 All the hub and branch firewalls in the SD-WAN cluster must show the same HA status for
 the active and passive Panorama. SD-WAN plugin displays the following error when the
 firewalls of the SD-WAN cluster shows different HA
 status: 
 The active Panorama's MongoDB -is not synchronized with the passive Panorama. Please get them in-sync

 This issue is addressed in SD-WAN plugin 2.2.7-h5, 3.2.3-h1 , and 3.3.3 . 

 After installing the SD-WAN plugin 3.2.3-h1 , 2.2.7-h5, 
 or 3.3.3 version, follow these
 steps: 
 Perform a minor change on active Panorama followed by a commit or commit force
 from active Panorama CLI. 

 Execute debug plugins sd_wan mongo-db sync-db-to-peer 
 from the active Panorama CLI. 

 After running this
 command, if the CLI displays the following message (that the MongoDB
 synchronization is still in progress), then you must restart the configd on
 active Panorama using debug software restart process
 configd and again synchronize the MongoDB using
 debug plugins sd_wan mongo-db sync-db-to-peer 
 from the active Panorama.

 MongoDB collection sync is in-progress. Please sync the collections after sometime. 

 Execute the synchronization job or request high-availability
 sync-to-remote running-config from the active Panorama CLI.

 PLUG-19159 

 Description of PLUG-19159. 

 After installing SD-WAN plugin 2.2.7 version, the SD-WAN Devices 
 page ( Panorama SD-WAN Devices ) does not load intermittently. 

 This issue is addressed in SD-WAN plugin 2.2.7-h5 , 3.2.4 , 3.3.3-h2 , and 3.4.0 . 

 PLUG-18888 

 Description of PLUG-18888. 

 ( SD-WAN Mesh topology only ) BGP connectivity cannot be established between the
 SD-WAN branch and hub firewalls. 

 This issue is addressed in SD-WAN plugin 3.4.0 and 3.3.3-h2 . 

 PLUG-18873 

 Description of PLUG-18873. 

 In Panorama, when you configure User-ID in the zone and push the configuration to the hub
 firewall, the configuration does not get enabled in the firewall. 

 This issue is addressed in SD-WAN plugin 3.2.3 , 3.2.4 , 3.4.0 , 3.0.9 and 3.3.4 . 

 PLUG-18380 

 Description of PLUG-18380. 

 ( SD-WAN hub-and-spoke deployments only ) DDNS validation fails on Panorama
 (throwing a commit error) when one or more SD-WAN branches are configured with dynamic
 IP addresses and hub configured with static IP address. 

 This issue is addressed in SD-WAN plugin 3.3.3 and
 3.4.0 . 

 PLUG-17378 

 Description of PLUG-17378. 

 When SD-WAN is configured with only cellular interface on the 4G/5G PAN-OS firewalls
 along with Allow DIA VPN enabled, the SD-WAN hub virtual
 interface (VIF) does not get listed in the DIA interface. Due to this, the DIA Anypath does not work properly that may
 impact the DIA failover. 

 This issue is addressed in SD-WAN plugin 3.3.2. 

 PLUG-16507 

 Description of PLUG-16507. 

 ( HA deployments only ) You may observe SD-WAN tunnel flapping and changes to the
 SD-WAN interfaces when you perform a commit operation after any of the following: 

 HA failover 

 PAN-OS upgrade or downgrade 

 Reboot the HA pair 

 This issue is addressed in SD-WAN plugin 3.3.2,
 3.3.1 , 3.2.2, 
 3.0.8 
 , and 2.2.7 . 

 PLUG-16141 

 Description of PLUG-16141. 

 The SD-WAN log files are overwritten and the critical events does not get captured in the
 system logs that cause difficulty in debugging the SD-WAN plugin-related issues. 

 This issue is addressed in SD-WAN plugin 2.2.7, 3.0.8
 , 3.2.2 , and 3.3.2 . After the fix, the following
 critical events are added to the system logs. 
 PSK creation or PSK change for a VPN cluster 

 Tunnel name, IP address creation, or IP address change 

 PLUG-16048 

 Description of PLUG-16048. 

 ( HA deployments only ) Passive Panorama makes changes to the SD-WAN plugin
 database cache entries. 

 This issue is addressed in SD-WAN plugin 2.2.7, 3.0.8
 , 3.2.2 , and 3.3.2 . 

 PLUG-15823 

 Description of PLUG-15823. 

 ( Full mesh topology only ) The SD-WAN devices neither go out-of-sync nor show up
 in the commit scope when a new hub device gets added to the full mesh VPN cluster. 

 This issue is addressed in SD-WAN plugin 2.2.7,
 3.0.7-h2 , 3.0.8 , 3.2.2 ,
 3.3.1 , and 3.3.2 . 

 PLUG-15764 

 Description of PLUG-15764 

 SD-WAN internal database-related activities will be impacted if you install the PAN-OS
 version before an SD-WAN plugin version. We recommend you to install the compatible
 SD-WAN plugin version first and then the corresponding PAN-OS version to avoid any
 SD-WAN database-related issues. 

 Workaround: If you wish to install the PAN-OS version first followed by the
 compatible SD-WAN plugin version, you must execute the following command to avoid any
 SD-WAN database-related issues. 

 debug plugins sd_wan manage-visibility-data mode recap 

 PLUG-15761 

 Description of PLUG-15761. 

 In some cases, after HA failover followed by a commit and commit push from the Panorama
 will result in the tunnel going down. It's because a new tunnel IP address gets
 generated for the firewall after a HA failover. 

 Workaround : After committing the configuration changes to Panorama, perform a
 commit and push on the all the SD-WAN devices in the SD-WAN VPN cluster even if the
 templates are in synchronization with the Panorama management server. 

 This issue is addressed in SD-WAN plugin 2.2.7, 3.0.8, 3.2.2, 3.3.1 , and 3.3.2 . 

 PLUG-15732 

 Description of PLUG-15732 

 The exported CSV files from SD-WAN devices won't have the Upstream
 NAT configurations. Hence, when you import the same CSV file, the
 Upstream NAT configurations would be missing. 

 This issue is addressed in SD-WAN plugin
 3.3.1. 

 PLUG-15673 

 Description of PLUG-15673. 

 The link characteristics for an application ( Panorama SD-WAN Monitoring ) does not display bandwidth, jitter, packet loss for SaaS enabled
 applications. 

 This issue is addressed in SD-WAN plugin 3.3.1. 

 PLUG-15526 

 Description of PLUG-15526. 

 The SD-WAN trend collection does not get recapped when you execute a command to recap the
 collection. 

 This issue is addressed in SD-WAN plugin 3.0.7-h2 and 3.3.1 . 

 PLUG-15525 

 Description of PLUG-15525. 

 It's not possible to revert to any of the earlier pre-shared keys except the current
 pre-shared key. 

 This issue is addressed in SD-WAN plugin 2.2.7, 3.0.8
 , 3.2.2 , and 3.3.2 . After the fix, you can revert
 to any of the earlier pre-shared keys (if it's available). 

 PLUG-15415 

 Description of PLUG-15415. 

 ( HA deployments only ) The HA synchronization failure occurs on the passive
 Panorama when you either upgrade or downgrade the HA Panorama. The issue is caused due
 to HA failover between the active and passive SD-WAN devices. 

 This issue is addressed in SD-WAN plugin 2.2.7, 3.0.8, 
 , 3.2.2 , 3.3.1 , and 3.3.2 . 

 PLUG-15323 

 Description of PLUG-15323 

 The SD-WAN allows you to choose any device group irrespective of the device type (branch
 or hub) selected while adding the BGP Security policy. For example, even though you
 select the device type as branch, you will be able to choose the hub device group in
 addition to the branch device group while adding the BGP policy. 

 This issue is addressed in SD-WAN plugin
 3.3.1. 

 PLUG-15276 

 Description of PLUG-15276 

 ( Full mesh topology only ) In the SD-WAN VPN cluster, an SD-WAN branch cannot
 create a VPN tunnel with another SD-WAN branch firewall if the branch firewall is
 configured behind the NAT device. 

 This issue is addressed in SD-WAN plugin 3.0.7-h2,
 3.1.3 , 3.2.1 , 3.3.0 ,
 and 3.3.1 . 

 PLUG-15258 

 Description of PLUG-15258 

 The SD-WAN monitoring report generation takes more time than expected. 

 This issue is addressed in SD-WAN plugin 3.2.1 and 3.3.1 . 

 PLUG-14953 

 Description of PLUG-14953. 

 ( HA deployments only ) After an HA failover, the Link Performance summary
 displays the previous active device (device that was active before the failover) as the
 hostname instead of the current active device. 

 PLUG-14559 

 Description of PLUG-14559. 

 A commit failure occurs when you attempt to rename the vsys to a name other than vsys1
 for a multi-vsys firewall with private link type (in an SD-WAN Interface
 Profile ). 

 This issue is addressed in SD-WAN plugin 3.0.7 ,
 3.1.3 
 , 3.2.1 
 , and 3.3.0 . 

 PLUG-14413 

 Description of PLUG-14413. 

 ( HA Deployments only ) If the HA environment is not configured correctly or when
 either of HA pair is not present, then no proper commit failure is displayed for
 troubleshooting. 

 This issue is addressed in SD-WAN
 plugin 2.2.7, 3.0.8 , 3.2.2 ,
 and 3.3.2 . After the fix, the improved failure message helps in identifying
 the missing HA device in the HA deployment. 

 PLUG-14402 

 Description of PLUG-14402 

 The return merchandise authentication (RMA) process won't be successful if you delete the
 replacement firewall without removing it from the SD-WAN plugin first. 

 This issue is addressed in SD-WAN plugin 2.2.6 ,
 3.0.7 , 3.2.1 , and 3.3.0 . Follow the instructions to replace an SD-WAN
 device. 

 PLUG-13536 

 Description of PLUG-13536. 

 When you disable Remove Private AS option
 (' remove-private-as ') and attempt to push the configuration
 from SD-WAN plugin to the branch firewalls, the changes to the Remove Private
 AS option ( SD-WAN Devices Branch BGP IPV4 BGP ) does not take effect and remains enabled on the branch firewalls. This
 issue is seen after upgrading the Panorama management server to 11.0.2 release. 

 This issue is addressed in SD-WAN plugin 3.1.3 ,
 3.2.1 , and 3.3.0 . 

 PLUG-13100 

 Description of PLUG-13100 

 On Prisma Access Onboarding tab, the aggregated interfaces don't
 get listed in the Interface drop-down. 

 This issue is addressed in SD-WAN plugin 3.0.5 ,
 3.1.3 , 3.2.1 , and 3.3.0 . 

 PLUG-12241 

 Description of PLUG-12241 

 You won't be able to push the configuration changes (like VPN cluster name) of an already
 configured VPN cluster to the Panorama management server. 

 This issue is addressed in SD-WAN plugin 3.1.3 ,
 3.2.1 , and 3.3.0 . 

 PLUG-12224 

 Description of PLUG-12224. 

 For an SD-WAN tunnel between a hub and a branch, the hub/branch tunnel interface should
 have the same IP address on the HA active and passive firewalls, but the hub/branch has
 different IP addresses on the HA active and passive firewalls. 

 This issue is addressed in SD-WAN plugin 2.2.4, 2.2.7,
 3.0.4, 3.0.8, 3.1.0-h6
 , 3.2.2 , and 3.3.2 . Tunnel ID changes will take
 effect from SD-WAN plugin 2.2.4. If you are running SD-WAN plugin 2.2.2 and upgrade
 to 2.2.4, you must regenerate the cluster configuration and push to devices to see
 those changes. 

 PLUG-12156 

 Description of PLUG-12156 

 On the Hub-Spoke VPN cluster type, if you make any changes to an
 existing cluster member configuration or add a new device to the cluster, the push gets
 enabled for all the VPN cluster members. 

 This issue is addressed in SD-WAN plugin 2.2.6 ,
 3.0.7-h2 , 3.2.1 
 , and 3.3.0 . 

 PLUG-11223 

 Description of PLUG-11223. 

 In a high availability (HA) deployment, the SD-WAN tunnel will go down due to a key ID
 mismatch when the following events occur in sequence: 
 An HA failover 

 The SD-WAN plugin cache removes the current HA pair relation from the database
 when debug plugins sd_wan drop-config-cache all command
 is executed 

 A commit and push fails on either the hub or a branch active node 

 In certain scenarios, replacing one of the HA devices during the RMA process can cause
 the SD-WAN tunnel to go down due to a key ID mismatch. For more details, refer to Replace an SD-WAN Device . 

 Workaround : Resolve the Key ID mismatch by ensuring that the Peer
 Identification of the hub firewall matches with the Local
 Identification of the branch firewall and the Local
 Identification of the hub firewall matches with the Peer
 Identification of the branch firewall. 

 Log in to the hub or a branch firewall where the SD-WAN tunnel is down due to Key ID
 mismatch and select Network Network Profiles IKE Gateways . 

 Select the IKE gateway of the hub firewall and click Override 
 at the bottom of the screen. 

 Copy the Local Identification value from the hub firewall to
 the Peer Identification value in the branch firewall. 

 Copy the Peer Identification value from the hub firewall to
 the Local Identification value in the branch firewall. 

 Click OK and Commit your changes. 

 This issue is addressed in SD-WAN plugin 2.2.5 ,
 2.2.7 , 3.0.8 , 3.1.3 
 , 3.2.1 ,
 3.2.2 
 , 3.3.0 ,
 and 3.3.2 . 

 After this fix, the key ID may
 change after the Panorama commit. Therefore, you must ensure to commit and push to
 all the devices in the VPN cluster or clusters. 

 Previous 

 Changes to Default Behavior in SD-WAN Plugin 3.3.1 

 Next 

 Panorama Plugin for SD-WAN 3.2 

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

 Release Notes 

 Network Security 

 PAN-OS 

 Next-Generation Firewall 

 Plugins 

 Panorama 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
