---
url: https://docs.paloaltonetworks.com/ngfw/help/12-2/device/device-setup-pan-os-security
fetched_at: 2026-08-13T16:51:34Z
source: palo-alto-main
---

# Device > Setup > PAN-OS Security Clear

Device > Setup > PAN-OS Security 

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

 Device > Setup > PAN-OS Security 

 Updated on 

 Mon Aug 03 19:43:33 PDT 2026 

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

 Mon Aug 03 19:43:33 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 PAN-OS Web Interface Help 

 Device 

 Device > Setup > PAN-OS Security 

 Download PDF 

 Next-Generation Firewall 

 Device > Setup > PAN-OS Security 

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

 Device > Setup > Quantum 

 Next 

 Device > Setup > DLP 

 Device > Setup > PAN-OS Security 

 Configure PAN-OS security settings and PAN-OS Shield to protect the firewall
 against system-level security violations and vulnerability exploits targeting PAN-OS
 services. 

 Device Setup PAN-OS Security 

 Panorama Setup PAN-OS Security 

 The PAN-OS Device Security Settings provide a choice of action for the Panorama
 appliance or firewall when PAN-OS detects a compromise or an attempt at compromise of
 the system. These internal protections detect and prevent attacks that attempt to change
 system files. 

 PAN-OS Shield provides Advanced Threat Protection based vulnerability protection for
 firewalls with GlobalProtect gateway or portal. When enabled, the firewall scans inbound
 control traffic using threat prevention signatures to detect and block exploitation
 attempts before they reach the management plane. An Advanced Threat Protection license is
 not required for PAN-OS Shield to provide PAN-OS specific vulnerability
 protections. 

 You can enable PAN-OS Shield without GlobalProtect gateway or portal configured, but
 the feature does not provide protection until GlobalProtect control traffic is
 present. 

 Field 

 Description 

 Device Security Settings 

 Select what the appliance or firewall should do if a system-level
 security violation is detected. 

 continue-running : (Default setting.) The
 appliance or firewall continues running if a system-level
 security violation is detected. 

 maintenance-mode : Automatically boot the
 appliance or firewall into maintenance mode as soon as a
 system-level security violation is detected. 

 This setting does not change the behavior of the System Integrity
 Checker; a failure of which will trigger maintenance mode in all
 circumstances. 

 PAN-OS Shield 

 Enable PAN-OS Shield to scan control traffic destined for the
 firewall for vulnerability exploits before it reaches the
 management plane. 

 When enabled, the firewall inspects inbound control traffic using
 threat prevention signatures delivered through content updates. If a
 threat is detected, the configured action is taken and a threat log
 is generated. 

 The vulnerability protection profile and security policy are
 delivered through content updates and are read-only. You can add
 threat exceptions to handle false positives by changing the action
 for a specific threat ID. 

 This feature is disabled by default. A commit and reboot is required
 after enabling or disabling PAN-OS Shield. 

 Previous 

 Device > Setup > Quantum 

 Next 

 Device > Setup > DLP 

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

 12.2 

 PAN-OS 

 Help 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
