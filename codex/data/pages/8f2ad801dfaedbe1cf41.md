---
url: https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-release-notes/pan-os-10-2-13-known-and-addressed-issues/pan-os-10-2-13-h4-addressed-issues
fetched_at: 2026-08-13T17:07:08Z
source: palo-alto-main
---

# PAN-OS 10.2.13-h4 Addressed Issues Clear

PAN-OS 10.2.13-h4 Addressed Issues 

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

 PAN-OS 10.2.13-h4 Addressed Issues 

 Updated on 

 Wed Jul 15 10:01:50 PDT 2026 

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

 Wed Jul 15 10:01:50 PDT 2026 

 Focus 

 Home 

 PAN-OS 

 PAN-OS 10.2.13 Known and Addressed Issues 

 PAN-OS 10.2.13-h4 Addressed Issues 

 Download PDF 

 PAN-OS 10.2.13-h4 Addressed Issues 

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

 Previous 

 PAN-OS 10.2.13-h5 Addressed Issues 

 Next 

 PAN-OS 10.2.13-h3 Addressed Issues 

 PAN-OS 10.2.13-h4 Addressed Issues 

 Addressed issues for the PAN-OS 10.2.13-h4 general available hotfix
 release. 

 Issue ID 

 Description 

 PAN-279604 

 Fixed an issue where scheduled SaaS application usage reports were
 generated incorrectly, and the login page was displayed instead of
 the report content. 

 PAN-276822 

 Fixed an issue where the packet buffer size increased significantly
 when WildFire File Forwarding was continued after a threat detection
 and then canceled. 

 PAN-274592 

 ( Firewalls in HA configurations only ) Fixed an issue where
 the firewall did not fail over when the active firewall experienced
 data plane issues. 

 PAN-273277 

 Fixed an issue where GlobalProtect clients on macOS devices were
 prompted to enter their username and password for Kerberos SSO
 authentication. 

 PAN-273153 

 Fixed an issue where the Panorama web interface was slower than
 expected due to excessive polling of the
 MonitorDirect.getTasks API by the
 Task Manager. 

 PAN-272006 

 Fixed an issue where the firewall did not trigger a kernel core dump
 as a large core when the CPLD (Complex Programmable Logic Device)
 sent a Non-Maskable Interrupt (NMI) to the CPU. 

 PAN-271301 

 ( VM-Series firewalls on Amazon Web Services (AWS) environments
 with GWLB integrated only ) Fixed an issue where DNS queries
 timed out when overlay routing was enabled. 

 PAN-268489 

 Fixed a Threat log PCAP ID overwrapping issue. 

 PAN-267704 

 Fixed an issue where the firewall did not send an ICMP error packet
 to Envoy when the MSS was exceeded 

 PAN-267660 

 Fixed an issue where UserID stopped working when the
 show object registered user CLI
 command was used with start-point and limit options. 

 PAN-265399 

 Fixed an issue where DNS queries for uppercase internal domain (SRV
 record) timed out when DNS Security was enabled. 

 PAN-264762 

 Fixed an issue where the firewall showed the status of SFP+
 interfaces as not up, or up but not configured, when a
 PAN-SFP-PLUS-SR cable was connected. 

 PAN-263465 

 Fixed an issue where the logrcvr process stopped
 responding due to a memory leak and buffer overrun. 

 PAN-261074 

 Fixed an issue where the firewall delayed video file transfers over
 SMB when Exclude Video Traffic from the
 Tunnel feature was enabled and no applications were added to the
 list. 

 PAN-260827 

 Fixed an issue where the firewall consumed excessive CPU while
 processing traffic for a workload running on a GKE cluster, which
 caused reduced throughput. 

 PAN-253921 

 Fixed an issue where the firewall displayed the following error
 message: critical userid register 0 fail to integrate
 the update of registered ip addresses since 2 seconds ago;
 critical system log alerts observed . 

 PAN-253213 

 Fixed an issue where the firewall sent HIP notifications every time
 it received a HIP report instead of every two hours. 

 PAN-246304 

 Fixed an issue on Panorama where commits failed due to a timeout in
 the sysd process during decryption. 

 Previous 

 PAN-OS 10.2.13-h5 Addressed Issues 

 Next 

 PAN-OS 10.2.13-h3 Addressed Issues 

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

 Network Security 

 PAN-OS 

 10.2 

 Next-Generation Firewall 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
