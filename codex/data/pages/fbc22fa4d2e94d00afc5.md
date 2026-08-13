---
url: https://docs.paloaltonetworks.com/globalprotect/user-guide/6-0/globalprotect-app-for-mac/remove-the-globalprotect-enforcer-kernel-extension
fetched_at: 2026-08-13T16:33:20Z
source: palo-alto-main
---

# Remove the GlobalProtect Enforcer Kernel Extension Clear

Remove the GlobalProtect Enforcer Kernel Extension 

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

 Remove the GlobalProtect Enforcer Kernel Extension 

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

 GlobalProtect App for macOS 

 Remove the GlobalProtect Enforcer Kernel Extension 

 Download PDF 

 English 

 한국어 (Korean) 

 GlobalProtect 

 Remove the GlobalProtect Enforcer Kernel Extension 

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

 Uninstall the GlobalProtect App for macOS 

 Next 

 Enable the GlobalProtect App for macOS to Use Client Certificates for Authentication 

 Remove the GlobalProtect Enforcer Kernel Extension 

 Where Can I Use This? What Do I Need? 

 macOS endpoints only 

 GlobalProtect app version 6.0 or later 

 When you uninstall the GlobalProtect app for
macOS, and then install a new instance of the app, you may encounter
connection issues if the GlobalProtect enforcer kernel extension
is not updated correctly. A kernel extension ( kext )
is a plugin for the macOS operating system that manages applications.
If you cannot connect to GlobalProtect after installing a new instance
of the app, use the following procedures to locate and remove the
GlobalProtect enforcer kernel extension. 

 Uninstall
the GlobalProtect App for Mac . 

 Determine if the GlobalProtect enforcer kernel extension
exists on the endpoint. 

 On the macOS endpoint, open the Terminal application
under the Applications Utilities folder,
and then enter the following command: 

 kextstat | grep gplock 

 If the extension exists, unload the enforcer. 

 Enter the following command on the Terminal application
to unload the enforcer: 

 sudo kextunload -b com.paloaltonetworks.GlobalProtect.gplock 

 Prevent the enforcer from reloading after a reboot. 

 Enter the following command on the Terminal application
to remove the enforcer from the macOS hard disk: 

 sudo rm -r "/System/Library/Extensions/gplock*.kext" 

 Download
and Install the GlobalProtect App for Mac . 

 Previous 

 Uninstall the GlobalProtect App for macOS 

 Next 

 Enable the GlobalProtect App for macOS to Use Client Certificates for Authentication 

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
