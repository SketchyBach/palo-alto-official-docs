---
url: https://docs.paloaltonetworks.com/sd-wan/activation-and-onboarding/converting-sd-wan-enabled-standalone-panorama-to-panorama-ha/converting-sd-wan-enabled-standalone-panorama-to-panorama-ha-workflow2
fetched_at: 2026-08-13T17:35:02Z
source: palo-alto-main
---

# SD-WAN Plugin 2.2.7-h5 or Later, 3.2.3-h2 or Later, and 3.3.3 or Later Versions Clear

SD-WAN Plugin 2.2.7-h5 or Later, 3.2.3-h2 or Later, and 3.3.3 or Later Versions 

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

 SD-WAN Plugin 2.2.7-h5 or Later, 3.2.3-h2 or Later, and 3.3.3 or Later Versions 

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

 Convert SD-WAN enabled Standalone Panorama to Panorama HA 

 SD-WAN Plugin 2.2.7-h5 or Later, 3.2.3-h2 or Later, and 3.3.3 or Later Versions 

 Download PDF 

 SD-WAN 

 SD-WAN Plugin 2.2.7-h5 or Later, 3.2.3-h2 or Later, and 3.3.3 or Later Versions 

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

 SD-WAN Plugin 2.2.7-h5 or Later, 3.2.3-h2 or Later, and 3.3.3 or Later Versions 

 Workflow for converting a SD-WAN enabled Panorama management server to a Panorama HA
 peer for SD-WAN plugin 2.2.7-h5 or later, 3.2.3-h2 or later, and 3.3.3 or later versions. 

 Configure the new Panorama management server. 

 Install the same OS version as the primary active firewall. 

 Configure the management IP address. 

 Install all the required plugins, application version, and antivirus
 version same as the primary active firewall. 

 Execute the commit force CLI command to commit
 the changes forcefully. 

 Configure high availability (HA). 

 On the standalone Panorama management server: 
 Navigate to Panorama High Availability Setup and configure the IP address and serial number of
 the newly deployed Panorama. 

 Navigate to Panorama High Availability Election Settings , enable Preemptive , set
 priority to
 primary and commit the changes. 

 On the newly deployed Panorama management server. 
 Navigate to Panorama High Availability Setup and configure the IP address and serial number of
 the standalone Panorama, which is already managing the network. 

 Navigate to Panorama High Availability Election Settings , disable Preemptive , set
 priority to
 secondary and commit the
 changes. 

 Once HA is committed, the new Panorama joins the HA cluster. Initially,
 the running configuration won’t be synchronized, and differences will
 appear in the HA dashboard. 

 Address the configuration differences by ensuring the correct versions
 of applications, antivirus, SD-WAN plugins, and any other required
 plugins are installed. 

 Configure the IP address for the newly deployed Panorama as the secondary IP
 address of Panorama in the Panorama settings (under device template of the
 devices managed by standalone Panorama) and commit the changes. 

 Synchronize databases. 

 Run the following synchronization command on the active Panorama HA
 peer: 
 debug plugins sd_wan mongo-db
 sync-db-to-peer 

 If the result shows sync-in-progress , restart the
 configd process using: 

 debug software restart
 process configd 

 Reconnect the active Panorama and run the synchronization command again.
 If successful, the active and passive Panorama MongoDB will be
 synchronized. 

 Synchronize and Verify. 

 Synchronize the running configuration from active Panorama to passive
 Panorama to apply all settings. 

 Verify both active and passive Panorama details in the HA dashboard.

 Check the MongoDB status by running: 
 debug plugins sd_wan
 mongo-db sync-status 

 Perform a force commit on the passive Panorama to finalize the
 setup. 

 Commit and push the changes from active Panorama to all the firewalls to
 configure the secondary Panorama IP address. 

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

 © 2026 Palo Alto Networks, Inc. All rights reserved.
