---
url: https://docs.paloaltonetworks.com/panorama/getting-started/set-up-panorama/manage-large-scale-firewall-deployments/increased-device-management-capacity-for-m-series-panorama-virtual-appliance
fetched_at: 2026-08-13T17:18:26Z
source: palo-alto-main
---

# Increased Device Management Capacity for M-Series and Panorama Virtual Appliance Clear

Increased Device Management Capacity for M-Series and Panorama Virtual Appliance 

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

 Increased Device Management Capacity for M-Series and Panorama Virtual Appliance 

 Updated on 

 Jul 14, 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Panorama Docs 

 Getting Started 

 Administration 

 New Features 

 Updated on 

 Jul 14, 2026 

 Focus 

 Home 

 Panorama 

 Set Up Panorama 

 Manage Large-Scale Firewall Deployments with Panorama 

 Increased Device Management Capacity for M-Series and Panorama Virtual Appliance 

 Download PDF 

 Panorama 

 Increased Device Management Capacity for M-Series and Panorama Virtual Appliance 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Panorama Docs 

 Getting Started 

 Administration 

 New Features 

 Previous 

 Manage Large-Scale Firewall Deployments with Panorama 

 Next 

 Set Up the Panorama Virtual Appliance 

 Increased Device Management Capacity for M-Series and Panorama Virtual Appliance 

 The M-600 and M-700 appliances can manage up to 5,000 firewalls and Panorama™ virtual
 appliance can manage up to 2,500 firewalls. 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by Panorama) 

 Device management licence (per-device) 

 Support license 

 Outbound Internet Access 

 Customer Support Portal (CSP) Account 

 Panorama Superuser Role 

 You can manage up to 5,000 firewalls using a single M-600, M-700 appliance, or Panorama™
 virtual appliance installed on VMware ESXi, or up to 2,5000 firewalls with all other
 supported Panorama virtual appliances in order to reduce the management footprint of
 your large-scale firewall deployment. 

 Increased Device Management Capacity Requirements 

 You can manage up to 5,000 firewalls using a single M-600, M-700 appliance, or
 Panorama™ virtual appliance installed on VMware ESXi, or up to 2,500 firewalls with
 all other supported Panorama virtual appliances. For managing such large deployments
 from a single Panorama management server alleviates the operational complexity of
 configuration management and reduces the security and compliance risk of managing
 multiple Panorama management servers. For details about the maximum number of
 template stacks that Panorama supports, see Template Stacks . 

 For log collection, a single Panorama management server is ideal because it provides
 a centralized location to view and analyze log data from managed devices rather than
 requiring you to access each individual Panorama management server. To provide
 redundancy in the event of system or network failure, Palo Alto Networks recommends
 deploying two Panorama management servers in a high availability (HA) configuration.
 For Panorama system and config logs, an additional disk with a minimum 92GB capacity
 is required. This additional disk is automatically detected by the Panorama virtual
 appliance when Panorama is rebooted and mounted as a partition for system and config
 log storage. 

 For generating pre-defined reports , you must enable
 Panorama to use Panorama data for pre-defined reports. This generates pre-defined
 reports using log data already collected by Panorama or the Dedicated Log Collector,
 which reduces the resource utilization when generating reports. Enabling this
 setting is required, otherwise Panorama performance may be impacted, and Panorama
 may become unresponsive. 

 To manage up to 5,000 firewalls, the Panorama management server must meet the
 following minimum requirements: 

 Requirement 

 5,000 Firewalls 

 2,500 Firewalls 

 Model 

 M-600 

 M-700 

 VMware ESXi 

 All supported Panorama hypervisors. For more information, see
 Panorama Models . 

 Panorama Mode 

 Management Only 

 Management Only 

 System Disk 

 Used to store the operating system files, system logs, software
 updates, and content updates. 

 M-Series Appliances —240GB SSD 

 ESXi —224GB 

 You must manually increase the
 system disk to 224GB. 

 81GB—Used to store the operating system files and system
 logs. 

 Additional disk with a minimum 92GB capacity used for
 storing Panorama system and config logs. 

 CPUs 

 56 

 32 

 Memory 

 256GB 

 256GB 

 Log Collection 

 Local log collection is not supported. 

 See Deploy Panorama with
 Dedicated Log Collectors to set up log
 collection. 

 Logging and Reporting 

 Enable the Use Panorama Data for Pre-Defined
 Reports setting ( Panorama Setup Management Logging and Reporting Settings Log Export and Reporting ) 

 Install Panorama for Increased Device Management Capacity 

 Activate the device management license to manage more than 1,000 firewalls from a
 single M-600 Panorama™ management server or a single Panorama virtual appliance.

 Contact your Palo Alto Networks sales representative to obtain the Panorama
 device management license that enables you to manage up to 5,000
 firewalls. 

 If you are deploying an M-600 appliance, obtain the
 PAN-M-600-P-1K device
 management license. 

 If you are deploying an M-700 appliance, obtain the
 PAN-M-700-P-1K device
 management license. 

 If you are deploying a Panorama virtual appliance, obtain the
 PAN-PRA-1000 device management
 license. 

 Set up the Panorama management server. 

 ( M-600 and M-700 appliances only ) Set Up the M-Series Appliance . 

 or 

 Set Up the Panorama Virtual Appliance . 

 Increase the System Disk for Panorama on an ESXi Server to 224GB. 

 A 224GB system disk is required for a Panorama virtual appliance
 installed on VMware ESXi to manage up to 5,000 firewalls. Review the
 Increased Device Management Capacity
 Requirements for more information. 

 Change the Panorama management server to Management Only mode if Panorama
 is not already in this mode. 

 Begin at Step 5 to Set Up an M-Series Appliance in Management Only Mode . 

 Set up a Panorama Virtual Appliance in Management Only Mode . 

 Register your Panorama management server and install licenses. 

 Register Panorama . 

 Activate a Panorama Support License . 

 Activate the device management license on the Panorama management
 server. 

 Activate/Retrieve a Firewall Management License on the M-Series Appliance . 

 Activate/Retrieve a Firewall Management License when the Panorama Virtual Appliance is not Internet-connected . 

 Activate/Retrieve a Firewall Management License when the Panorama Virtual Appliance is Internet-connected . 

 Select Panorama Licenses and verify that the device management license is successfully
 activated. 

 If you are activating a new device management license on a Panorama,
 you can manage up to 5,000 firewalls with an M-600, M-700 appliance,
 or Panorama virtual appliance on ESXi, or up to 2,500 firewalls with
 a Panorama virtual appliance, but the Description still displays
 Device management license to manage up to 1000
 devices or more . 

 Previous 

 Manage Large-Scale Firewall Deployments with Panorama 

 Next 

 Set Up the Panorama Virtual Appliance 

 On This Page 

 Activation and Onboarding 

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

 Panorama 

 Service Provider 

 VM-Series 

 Plugins 

 SASE 

 Prisma Access 

 Prisma SASE Multitenant Platform 

 AI-Powered ADEM 

 Prisma Access Monitoring & Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

 Cloud-Delivered Security Services 

 Advanced WildFire 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 AI Access Security 

 Device Security 

 Enterprise DLP 

 SaaS Security 

 Network Security 

 Shared Policy for NGFWs and Prisma Access 

 IPSec VPN 

 Security Policy 

 Quantum Security 

 Endpoints 

 GlobalProtect 

 Remote Browser Isolation 

 Prisma Access Agent 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 FedRAMP 

 Prisma SASE for FedRAMP 

 Autonomous DEM for FedRAMP 

 Prisma SD-WAN Experts Corner 

 Network Policy 

 QoS Whitepaper 

 Security Architecture Whitepaper 

 External Antennas for ION-C Series 

 Dynamic Path Selection 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Resources 

 All Products A - Z 

 All Release Notes 

 Compatibility Matrix 

 Experts Corner 

 Network Security Platform 

 Security Policy 

 Decryption 

 Device-ID 

 IPSec VPN 

 Quality of Service 

 Quantum Security 

 11.1 & Later 

 Next-Generation Firewall 

 Getting Started 

 Panorama 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
