---
url: https://docs.paloaltonetworks.com/ngfw/getting-started/onboard-your-ngfws/onboard-a-firewall
fetched_at: 2026-08-13T16:41:05Z
source: palo-alto-main
---

# Onboard a Firewall Clear

Onboard a Firewall 

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

 Onboard a Firewall 

 Updated on 

 Mar 24, 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Generation Firewall Docs 

 Getting Started 

 Administration 

 Networking 

 Quick Start 

 Reference 

 Incidents & Alerts 

 Release Notes 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 11.0 (EoL) 

 PAN-OS 10.2 

 PAN-OS 10.1 (EoL) 

 PAN-OS 10.0 (EoL) 

 PAN-OS 9.1 (EoL) 

 PAN-OS 9.0 (EoL) 

 PAN-OS 8.1 (EoL) 

 Help 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 10.2 

 PAN-OS 10.1 

 New Features 

 Updated on 

 Mar 24, 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 Onboard Your NGFWs 

 Onboard a Firewall 

 Download PDF 

 Next-Generation Firewall 

 Onboard a Firewall 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Generation Firewall Docs 

 Getting Started 

 Administration 

 Networking 

 Quick Start 

 Reference 

 Incidents & Alerts 

 Release Notes 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 11.0 (EoL) 

 PAN-OS 10.2 

 PAN-OS 10.1 (EoL) 

 PAN-OS 10.0 (EoL) 

 PAN-OS 9.1 (EoL) 

 PAN-OS 9.0 (EoL) 

 PAN-OS 8.1 (EoL) 

 Help 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 10.2 

 PAN-OS 10.1 

 New Features 

 Onboard a Firewall 

 Learn how to onbaord your Next-Generation Firewalls to Strata Cloud Manager and Panorama . 

 Where Can I Use
 This? What Do I Need? 

 NGFW (Cloud Managed) 

 NGFW (PAN-OS or Panorama Managed) 

 VM-Series, funded with Software NGFW Credits 

 AIOps for NGFW Premium license (use the Strata Cloud Manager app) 

 Cortex
Data Lake license 

 Contact your account team to enable Cloud Management for NGFWs using Strata Cloud
 Manager. 

 To use Strata Cloud Manager or the Panorama™ management server for managing
 Next-Generation Firewalls, you must first add the firewalls as a managed device. 

 Cloud Management 

 Panorama 

 Cloud Management 

 Learn how to configure and onboard firewalls in Strata Cloud Manager . 

 After you activate your AIOps for NGFW Premium license, you can begin to
 onboard Palo Alto Networks firewalls to Strata Cloud Manager . Onboarding to Strata Cloud Manager is supported for firewalls running PAN-OS 10.2.3 and later
 releases. 

 There are four components involved in firewall onboarding: 

 The tenant — Created when you activate a product license on your
 Customer Support Portal (CSP) account. You add firewalls to your tenant to
 associate them with Strata Cloud Manager . 

 The firewall — The Palo Alto Networks firewall that you intend to use with
 Strata Cloud Manager . 

 You can only onboard a firewall not already associated with Cortex Data
 Lake (CDL). If a firewall is already associated with CDL, it’s
 ineligible for Strata Cloud Manager and isn’t displayed. 

 AIOps for NGFW Premium —License required for cloud management of
 firewalls. 

 Strata Cloud Manager — The app you will be associating with the firewall to
 manage its configuration from the cloud. 

 Review the prerequisites for onboarding your
 firewall to Strata Cloud Manager . 

 Activate the Cortex
Data Lake license. 

 Skip this step if you already activated the Prisma Access
(Cloud Management) license on
 the same tenant you are activating AIOps for NGFW Premium license.

 Activate the AIOps for NGFW Premium license. 

 Skip this step if you already activated the AIOps for NGFW Premium 
 license. 

 ( Optional ) Activate the Cloud Identity Engine 
 license. 

 Activate Cloud Identity Engine (CIE) if you plan to use user-based
 authentication policies. CIE activation is not required for initial
 onboarding and can be activated at a later time as needed. 

 Register the firewall with the Palo Alto Networks Customer Support Portal (CSP)
 and activate licenses. 
 Log in to the firewall web
 interface and find the Serial # 
 under the General Information widget in the
 Dashboard . 

 Register your Next-Generation
 Firewall . 

 Activate the Support license 
 on the firewall. 

 Install the device certificate on the
 firewall. 

 This is required to successfully authenticate the firewall with the Palo Alto
 Networks CSP and use Strata Cloud Manager . 

 Configure the firewall Panorama Settings required to connect to Strata Cloud Manager . 
 Log in to the firewall web
 interface . 

 Configure the firewall DNS and NTP servers. 

 This is required to successfully connect the firewall to Strata Cloud Manager and install software and content updates. 

 Select Device Setup Services and edit the Services. 

 Select Servers and configure the
 Primary DNS Server and
 Secondary DNS Server . 

 Select NTP and configure the Primary
 and Secondary NTP Server Address . 

 Click OK . 

 Configure the Panorama Settings. 

 Select Device Setup Management and edit the Panorama Settings. 

 Select Managed By Cloud Service . 

 Click OK . 

 Commit . 

 Associate a firewall with your Palo
 Alto Networks Customer Support Portal (CSP) account. 
 Log in to Strata Cloud Manager . 

 In the bottom-left corner of the window, select the icon for your
 tenant and select Settings Device Associations . 

 Add Devices . 

 Select one or more firewalls you want to onboard with your CSP
 account. 

 You can use the firewall serial number you gathered in the previous
 step to search for a specific firewall. 

 Save . 

 Associate the firewall with Strata Cloud Manager . 
 In Device Associations, select the firewall you added and
 Associate Apps . 

 For the Licensed Products, select AIOps for
 NGFW . 

 From the Select Firewall Model, License Type, and
 Term drop-down, select the firewall and support license
 to apply to the firewall. 

 The model for the firewall license must match the firewall model you
 are onboarding to Strata Cloud Manager . 

 Apply Licenses . 

 In the Device Associations page, verify the Associated Apps for the
 onboarded firewall display AIOps for NGFW 
 and Cortex Data Lake . 

 Add the available device to Strata Cloud Manager . 
 Select Workflows NGFW Setup Device Management Available Devices . 

 In the Available Devices select the
 firewall you just added. 

 Move to Cloud Management . 

 You are prompted to confirm the number of selected firewalls. Click
 Move to Cloud Management to continue. 

 Confirm that the selected firewall is now listed in the list of
 Cloud Managed Devices . 

 Verify that the firewall successfully onboarded to Strata Cloud Manager . 

 Two configuration pushes occur by default to the firewall after
 successful onboarding to Strata Cloud Manager . The first push from Strata Cloud Manager enables Advanced Routing and restarts the
 firewall. The second pushes the configuration from Strata Cloud Manager 
 to the firewall. 

 Select Workflows NGFW Setup Device Management Cloud Managed Devices . 

 You should see the serial number for the firewall that you just
 added, but you won’t see any additional device information for it
 yet. 

 Log in to the firewall CLI and
 verify the firewall successfully connected to Strata Cloud Manager . 

 After you connect the firewall to Strata Cloud Manager , it’s
 automatically converted to logical router mode, restarted, and Strata Cloud Manager pushes the default configuration to the
 firewall. 

 For this to work, make sure: 

 You’ve completed the earlier step to install the device
 certificate on the firewall. 

 The firewall meets the prerequisites for Strata Cloud Manager . 

 You’ve resolved variables. If variables aren’t resolved,
 Strata Cloud Manager will fail to push the default
 configuration to the firewall. 

 admin> show cloud-management-status 

 Verify the firewall successfully connected to a Strata Cloud Manager 
 Endpoint and that the
 Connected status displays
 Yes . 

 Once the firewall is Connected , the
 firewall automatically converts to logical router mode and restarts,
 and Strata Cloud Manager pushes the default configuration to the
 firewall. 

 Return to Strata Cloud Manager and select Workflows NGFW Setup Device Management and verify that the details for the firewall appear, such
 as serial number, model, type, and IP address. 

 By default, newly onboarded firewalls are added to the Firewalls
 folder. 

 Create and associate your firewall with a folder . 

 Folders are used to logically group your firewalls for simplified
 configuration management. 

 ( HA only ) Both firewalls must be in the same folder to configure
 HA. If you need to configure your firewalls in a high availability (HA)
 configuration, be sure to plan your folder structure accordingly and
 move both firewalls to the same folder before you configure HA. 

 Additionally, firewalls in an HA configuration cannot be moved to a new
 folder. To move them, you must first break the HA configuration, move
 both firewalls to the new folder, and then reconfigure HA. 

 Select Workflows NGFW Setup Folder Management and Add Folder to create a new
 folder. 

 Locate the newly added firewall that is associated with the
 All Firewalls by default. 

 In the Action column, Move the firewall to the
 folder you created. 

 ( Optional ) Modify the displayed firewall name. 

 By default, firewalls onboarded to Strata Cloud Manager display the firewall
 serial number as the displayed firewall name throughout Strata Cloud Manager . Rename the displayed firewall from the serial number to a more
 user-friendly name to make it easier to identify. 

 Select Workflows NGFW Setup Folder Management and locate the firewall you onboarded. 

 In the Actions column, expand the Actions menu and
 Edit . 

 Enter a new Display Name for the firewall. 

 Save . 

 Review the predefined interface and logical router configurations. 

 The predefined interfaces and logical router configuration are required to
 successfully push configuration changes to managed firewalls after they’re
 successfully added to Strata Cloud Manager . 

 $eth-internet (eth1/3) —Ethernet interface for outbound
 internet connections. Associated with the default logical router
 configuration. 

 $eth-local (eth1/4) —Ethernet interface for local network
 connections. Associated with the default router configuration. 

 The predefined interface and logical router configuration are associated with
 the default All Firewalls folder and are
 inherited by all other folders you create. You might reassign the
 $eth-internet and $eth-local
 interfaces for a newly created folder or for the individual
 firewall as needed. 

 Select Manage Configuration Device Settings Interfaces Ethernet and verify that
 $eth-internet and
 $eth-local are displayed. 

 To reassign the interface, click the interface name to select a
 new Default Interface Assignment and
 Save . 

 Select Manage Configuration Device Settings Routing Logical Routers and verify the default 
 logical router is displayed. 

 Push Config to push your configuration changes. 

 Select Manage Operation Push Status and to verify that your configuration push was successful. 

 Panorama 

 Learn how to onboard firewalls to Panorama. 

 Next-Generation Firewalls can be centrally managed using Panorama. 

 To start onboarding your Next-Generation Firewalls to Panorama, follow the guide
 here . 

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

 PAN-OS SD-WAN 

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

 Device Security 

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

 PAN-OS 

 Next-Generation Firewall 

 Getting Started 

 Panorama 

 Strata Cloud Manager 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
