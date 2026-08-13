---
url: https://docs.paloaltonetworks.com/pan-os/9-1/pan-os-release-notes/pan-os-9-1-addressed-issues/pan-os-9-1-11-h2-addressed-issues
fetched_at: 2026-08-13T17:14:08Z
source: palo-alto-main
---

# PAN-OS 9.1.11-h2 Addressed Issues Clear

PAN-OS 9.1.11-h2 Addressed Issues 

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

 PAN-OS 9.1.11-h2 Addressed Issues 

 Updated on 

 Tue Jul 22 10:17:59 PDT 2025 

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

 Updated on 

 Tue Jul 22 10:17:59 PDT 2025 

 Focus 

 Home 

 PAN-OS 

 PAN-OS 9.1 Addressed Issues 

 PAN-OS 9.1.11-h2 Addressed Issues 

 Download PDF 

 PAN-OS 9.1.11-h2 Addressed Issues 

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

 End-of-Life (EoL)

 Previous 

 PAN-OS 9.1.11-h3 Addressed Issues 

 Next 

 PAN-OS 9.1.11 Addressed Issues 

 PAN-OS 9.1.11-h2 Addressed Issues 

 PAN-OS® 9.1.11-h2 addressed issues. 

 Issue ID 

 Description 

 PAN-178814 

 Fixed an issue where autocommits failed
when upgrading from a PAN-OS 8.1 release to a PAN-OS 9.1 release
due to large configurations with a high number of policies with
reference to IP addresses. 

 PAN-176661 

 Fixed an issue in Simple Certificate Enrollment
Protocol (SCEP) ( CVE-2021-3060 ). 

 PAN-176655 and PAN-158334 

 A fix was made to address an OS command
injection vulnerability in the PAN-OS CLI that enabled an authenticated
administrator with access to the CLI to execute arbitrary OS commands
to escalate privileges ( CVE-2021-3061 ). 

 PAN-176653 

 A fix was made to address an OS command
injection vulnerability in the PAN-OS web interface that enabled
an authenticated administrator with permissions to use XML API to
execute arbitrary OS commands to escalate privileges ( CVE-2021-3058 ). 

 PAN-176618 

 A fix was made to address an OS command
injection vulnerability in PAN-OS that existed when performing dynamic
updates ( CVE-2021-3059 ). 

 PAN-176461 

 Fixed an issue where a process ( mdb )
stopped responding after downgrading from a PAN-OS 9.1 release to
an earlier release due to discrepancies in the mongodb process version. 

 To
utilize this fix, first install a PAN-OS 9.0 release on the web
interface, and then, prior to reboot, run the following CLI command: debug mongo clear instance mdb .
Running this command removes any historical operational data (such
as rule hit counts, monitoring data, and so on) collected on Panorama. 

 PAN-176131 

 Fixed an issue where the Simple Network
Management Protocol (SNMP) object identifier (OID) for panSessionCps did
not show the correct session count. 

 PAN-169173 

 Fixed an issue where, if you continuously
performed partial commits of a configuration with a high number
of Dynamic Address Groups, Panorama became unresponsive and commits
were slower than expected. 

 Previous 

 PAN-OS 9.1.11-h3 Addressed Issues 

 Next 

 PAN-OS 9.1.11 Addressed Issues 

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

 Release Notes 

 PAN-OS 

 Next-Generation Firewall 

 9.1 (EoL) 

 Panorama 

 English 

 Network Security 

 VM-Series 

 Advanced Wildfire 

 GlobalProtect 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
