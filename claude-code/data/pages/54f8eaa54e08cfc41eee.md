---
url: https://docs.paloaltonetworks.com/globalprotect/user-guide/6-0/globalprotect-app-for-linux/uninstall-the-globalprotect-app-for-linux
fetched_at: 2026-08-13T16:33:20Z
source: palo-alto-main
---

# Uninstall the GlobalProtect App for Linux Clear

Uninstall the GlobalProtect App for Linux 

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

 Uninstall the GlobalProtect App for Linux 

 Updated on 

 Fri Nov 07 16:16:53 PST 2025 

 Focus 

 Download PDF 

 English 

 한국어 (Korean) 

 Filter

 Expand All 
 | 
 Collapse All 

 GlobalProtect Docs 

 Getting Started 

 Activation & Onboarding 

 Administration 

 User Guide 

 Select a Document 

 6.3 

 6.2 

 6.1 

 6.0 

 Release Notes 

 Select a Document 

 6.3 

 6.2 

 6.1 

 6.0 

 New Features 

 Updated on 

 Fri Nov 07 16:16:53 PST 2025 

 Focus 

 Home 

 GlobalProtect 

 GlobalProtect App for Linux 

 Uninstall the GlobalProtect App for Linux 

 Download PDF 

 English 

 한국어 (Korean) 

 GlobalProtect 

 Uninstall the GlobalProtect App for Linux 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 GlobalProtect Docs 

 Getting Started 

 Activation & Onboarding 

 Administration 

 User Guide 

 Select a Document 

 6.3 

 6.2 

 6.1 

 6.0 

 Release Notes 

 Select a Document 

 6.3 

 6.2 

 6.1 

 6.0 

 New Features 

 Previous 

 Disconnect the GlobalProtect App for Linux 

 Next 

 GlobalProtect for IoT Devices 

 Uninstall the GlobalProtect App for Linux 

 Where Can I Use This? What Do I Need? 

 Linux endpoints only 

 GlobalProtect app version 6.0 or later 

 You can uninstall the GlobalProtect app for
Linux using either the dpkg and the apt-get utility. To uninstall
the GlobalProtect app, you must run the command with root permissions: 

 Begin the uninstallation process by
entering the sudo dpkg -P globalprotect command. 

 user@linuxhost:~$ sudo dpkg -P globalprotect 
(Reading database ... 209181 files and directories currently installed.)
Removing globalprotect (4.1.0-12) ...
gp service is running and we need to stop it...
Disable service...
Removing gp service...
gp service has been removed successfully
Removing configuration...

 Uninstall the GlobalProtect app for Linux by entering
the sudo apt-get remove globalprotect command. 

 Previous 

 Disconnect the GlobalProtect App for Linux 

 Next 

 GlobalProtect for IoT Devices 

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

 Hardware Reference 

 ION 1000 

 ION 1200 

 ION 1200-S 

 ION 2000 

 ION 3000 

 ION 3200 

 ION 5200 

 ION 7000 

 ION 9000 

 ION 9200 

 Hardware Quick Start Guides 

 ION 1200 

 ION 1200 4G 

 ION 1200 5G 

 ION 1200-S 

 ION 1200-S 4G 

 ION 1200-S 5G 

 ION 3200 

 ION 5200 

 ION 9200 

 Virtual ION Deployment 

 Virtual ION on AWS 

 Virtual ION on Azure 

 Virtual ION on GCP 

 Virtual ION on KVM for NFV 

 Virtual ION on OCI 

 Virtual ION on VMware 

 3rd Party Integrations 

 AWS Cloud-WAN Integration (GRE Connect) 

 AWS Cloud-WAN Integration (Tunnel-less Connect) 

 Checkpoint Integration 

 LiveAction Integration 

 Netskope Integration 

 Symantec Web Security Services Integration 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 User Guide 

 GlobalProtect App User Guide 

 English 

 SASE 

 GlobalProtect App 

 GlobalProtect User Guide 

 6.0 

 GlobalProtect 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
