---
url: https://docs.paloaltonetworks.com/globalprotect/release-notes/6-3/known-issues-related-to-gp-app/globalprotect-6-3-3-h2-linux-known-issues
fetched_at: 2026-08-13T16:33:15Z
source: palo-alto-main
---

# GlobalProtect 6.3.3-h2 (6.3.3-c42) Linux Known Issues Clear

GlobalProtect 6.3.3-h2 (6.3.3-c42) Linux Known Issues 

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

 GlobalProtect 6.3.3-h2 (6.3.3-c42) Linux Known Issues 

 Updated on 

 Wed Aug 12 12:42:31 PDT 2026 

 Focus 

 Download PDF 

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

 Wed Aug 12 12:42:31 PDT 2026 

 Focus 

 Home 

 GlobalProtect 

 GlobalProtect™ App Release Notes 

 Known Issues 

 GlobalProtect 6.3.3-h2 (6.3.3-c42) Linux Known Issues 

 Download PDF 

 GlobalProtect 

 GlobalProtect 6.3.3-h2 (6.3.3-c42) Linux Known Issues 

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

 GlobalProtect 6.3.3-h11 (6.3.3-c1016) Windows and macOS (Preferred) Known Issues 

 Next 

 GlobalProtect 6.3.3-h9 (6.3.3-c999) Windows and macOS Known Issues 

 GlobalProtect 6.3.3-h2 (6.3.3-c42) Linux Known Issues 

 The following table lists the issues addressed in GlobalProtect app 6.3.3-h2 (6.3.3-c42)
 Linux. 

 Issue ID 

 Description 

 GPC-25973 

 After uninstalling the GlobalProtect agent from a Red Hat Enterprise
 Linux 9.6 system, the `gpd0` virtual interface remains listed as an
 unmanaged interface when using the `nmcli` command. Additionally,
 configuration files related to the `gpd0` interface are not removed
 from the `/etc/NetworkManager/conf.d` directory. DNS and interface
 configurations previously set by GlobalProtect may also persist in
 `nmcli`, `systemd-resolved` settings, and the `/etc/resolv.conf`
 file. This persistence does not cause any functional impact on
 network operations. 

 GPC-26289 

 After a fresh installation of the GlobalProtect client on Fedora 43
 with GNOME (Wayland), the GlobalProtect icon does not automatically
 appear in the system tray. Users must manually launch the
 GlobalProtect user interface by searching for "GlobalProtect" in the
 Applications menu or by running the `globalprotect launch-ui`
 command. The icon appears correctly in the system tray after a
 system reboot. 

 GPC-26290 

 When Direct Local Subnet Access (DLSA) is disabled, traffic between
 devices on the same local subnet does not route through the VPN
 tunnel as expected. Instead, this traffic attempts to route directly
 via the physical interface, which can lead to connection failures.
 This issue affects all Linux platforms, including RHEL, Ubuntu, and
 Fedora. 

 GPC-26293 

 When installing GlobalProtect on Ubuntu using a custom installation
 path, the installation process does not complete successfully. 

 Previous 

 GlobalProtect 6.3.3-h11 (6.3.3-c1016) Windows and macOS (Preferred) Known Issues 

 Next 

 GlobalProtect 6.3.3-h9 (6.3.3-c999) Windows and macOS Known Issues 

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

 Release Notes 

 May 2026 

 GlobalProtect 

 English 

 6.3 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
