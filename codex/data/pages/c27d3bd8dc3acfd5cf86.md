---
url: https://docs.paloaltonetworks.com/panorama/getting-started/set-up-panorama/set-up-the-m-series-appliance/m-series-setup-overview/set-up-an-m-series-appliance-in-management-only-mode
fetched_at: 2026-08-13T17:18:30Z
source: palo-alto-main
---

# Set Up an M-Series Appliance in Management Only Mode Clear

Set Up an M-Series Appliance in Management Only Mode 

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

 Set Up an M-Series Appliance in Management Only Mode 

 Updated on 

 Tue Jul 14 08:53:35 PDT 2026 

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

 Tue Jul 14 08:53:35 PDT 2026 

 Focus 

 Home 

 Panorama 

 Set Up Panorama 

 Set Up the M-Series Appliance 

 M-Series Setup Overview 

 Set Up an M-Series Appliance in Management Only Mode 

 Download PDF 

 Panorama 

 Set Up an M-Series Appliance in Management Only Mode 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Panorama Docs 

 Getting Started 

 Administration 

 New Features 

 Set Up an M-Series Appliance in Management Only Mode 

 How to set up an M-Series appliance in Management Only
mode. 

 Set up the Panorama management server in Management
Only mode to dedicate Panorama to managing firewalls and Dedicated
Log Collectors. Panorama in Management Only mode have no log collection
capabilities, except for config and system logs, and requires a
Dedicated Log Collector to store logs. 

 If you configured a local Log Collector, the local Log Collector still exists on Panorama when
 you change to Management Only mode despite having no log collection
 capabilities. Deleting the local Log Collector ( Panorama Managed Collectors ) deletes the Eth1/1 interface configuration the local Log
 Collector uses by default. If you decide to delete the local Log Collector, you
 must reconfigure the Eth1/1
 interface . 

 Rack mount the M-Series appliance. Refer to the M-Series
Appliance Hardware Reference Guide for instructions. 

 Perform
Initial Configuration of the M-Series Appliance . 

 Register
Panorama and Install Licenses . 

 Install content and software
updates on Panorama . 

 Change to Management Only mode. 

 Log in to the Panorama CLI . 

 Switch from Panorama mode to Management Only mode: 
 request system system-mode management-only 

 Enter Y to confirm the mode
change. The Panorama management server reboots. If the reboot process
terminates your terminal emulation software session, reconnect to
the Panorama management server to see the Panorama login prompt. 

 If you see a CMS Login prompt,
this means the Panorama management server has not finished rebooting.
Press Enter at the prompt without typing a username or password. 

 Log back in to the CLI. 

 Verify that the switch to Management Only mode succeeded: 
 show system info | match system-mode 
 If
the mode change succeeded, the output displays: 
 system mode:management-only 

 Configure Administrative Access to
 Panorama 

 Manage Firewalls 

 Manage Log Collection 

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
