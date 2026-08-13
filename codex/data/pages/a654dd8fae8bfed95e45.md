---
url: https://docs.paloaltonetworks.com/ngfw/help/11-1/panorama-web-interface/panorama-managed-collectors/software-updates-for-dedicated-log-collectors
fetched_at: 2026-08-13T16:46:39Z
source: palo-alto-main
---

# Software Updates for Dedicated Log Collectors Clear

Software Updates for Dedicated Log Collectors 

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

 Software Updates for Dedicated Log Collectors 

 Updated on 

 Thu Jun 25 17:39:35 PDT 2026 

 Focus 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 한국어 (Korean) 

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

 Thu Jun 25 17:39:35 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 Panorama Web Interface 

 Panorama > Managed Collectors 

 Software Updates for Dedicated Log Collectors 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 한국어 (Korean) 

 Next-Generation Firewall 

 Software Updates for Dedicated Log Collectors 

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

 Previous 

 Communication Settings 

 Next 

 Panorama > Collector Groups 

 Software Updates for Dedicated Log Collectors 

 Panorama > Managed Collectors 

 To install a software image on a Dedicated Log Collector, download
or upload the image to Panorama (see Panorama
> Device Deployment ), click Install and complete
the following fields. 

 Because the Panorama management server shares its operating
system with the local default Log Collector, you upgrade both when
installing a software update on the Panorama management server (see Panorama
> Software ). 

 For Dedicated Log Collectors, you can
also select Panorama Device
Deployment Software to
install updates (see Manage
Software and Content Updates ). 

 To reduce traffic on
the management (MGT) interface, you can configure Panorama to use
a separate interface for deploying updates (see Panorama
> Setup > Interfaces ). 

 Fields to Install
a Software Update on a Log Collector 

 Description 

 File 

 Select a downloaded or uploaded software
image. 

 Devices 

 Select the Log Collectors on which to install
the software. The dialog displays the following information for
each Log Collector: 

 Device Name —The name of
the Dedicated Log Collector. 

 Current Version —The Panorama software release currently installed
on the Log Collector. 

 HA Status —This column does not apply to Log Collectors. Dedicated
Log Collectors do not support high availability. 

 Filter Selected 

 To display only specific Log Collectors,
select the Log Collectors and Filter Selected . 

 Upload only to device (do not Install) 

 Select to upload the software to the Log
Collector without automatically rebooting it. The image is not installed
until you manually reboot by logging into the Log Collector CLI
and running the request restart system operational command. 

 Reboot device after Install 

 Select to upload and automatically install
the software. The installation process reboots the Log Collector. 

 Previous 

 Communication Settings 

 Next 

 Panorama > Collector Groups 

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

 PAN-OS 

 11.1 

 Next-Generation Firewall 

 Help 

 Web Interface 

 Panorama 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
