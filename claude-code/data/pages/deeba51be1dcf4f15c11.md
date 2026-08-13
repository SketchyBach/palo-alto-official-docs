---
url: https://docs.paloaltonetworks.com/pan-os/11-2/pan-os-release-notes/pan-os-11-2-7-known-and-addressed-issues/pan-os-11-2-7-h17-addressed-issues
fetched_at: 2026-08-13T17:13:35Z
source: palo-alto-main
---

# PAN-OS 11.2.7-h17 Addressed Issues Clear

PAN-OS 11.2.7-h17 Addressed Issues 

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

 PAN-OS 11.2.7-h17 Addressed Issues 

 Updated on 

 Mon Aug 10 15:44:33 PDT 2026 

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

 Mon Aug 10 15:44:33 PDT 2026 

 Focus 

 Home 

 PAN-OS 

 PAN-OS 11.2.7 Known and Addressed Issues 

 PAN-OS 11.2.7-h17 Addressed Issues 

 Download PDF 

 PAN-OS 11.2.7-h17 Addressed Issues 

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

 PAN-OS 11.2.7-h18 Addressed Issues 

 Next 

 PAN-OS 11.2.7-h16 Addressed Issues 

 PAN-OS 11.2.7-h17 Addressed Issues 

 Lists the addressed issues in PAN-OS 11.2.7-h17. 

 The following table lists the addressed issues in PAN-OS 11.2.7-h17. 

 Issue ID 

 Description 

 PAN-320598 

 Fixed an issue where internal and external DNS names did not resolve when connected to a GlobalProtect gateway. 

 PAN-317755 

 Fixed an issue on Panorama where selective push operations failed when plugin configurations included access-domain or log-collector references. 

 PAN-315337 

 Fixed an issue where GlobalProtect throughput was reduced after an upgrade. 

 PAN-314319 

 Added a CLI command to enable and disable AHO software offload optimization. 

 PAN-313606 

 Fixed an issue where Panorama pushed commits took longer than expected to complete without displaying an error message when committing due to slow cloud-app compilation. 

 PAN-310263 

 ( VM-Series firewalls only ) Fixed an issue where enabling TLS1.3 in a decryption profile prevented access to websites. 

 PAN-310240 

 Fixed an issue where software packet buffers were completely utilized when performing a Data Loss Prevention longevity test. 

 PAN-307618 

 Added a debug CLI command to address where remote networks for Prisma Access tenants randomly dropped monitoring packets from peer devices, which caused tunnels to be marked as down. This occurred when a CPU core suddenly experienced high utilization. 

 To utilize this fix, run debug dataplane set ssl-decrypt use-new-peek-window yes . 

 PAN-307470 

 Fixed an issue where an External Dynamic List (EDL) fetch with an invalid certificate was skipped on newly provisioned GlobalProtect gateway instances. 

 PAN-266905 

 Fixed an issue where sessions ended with the message decrypt error in the logs for traffic that matched a no-decrypt policy. 

 PAN-234302 

 Fixed an issue where commit operations took longer than expected to complete due to EDL timeouts occurring on passive nodes when a service route was enabled. 

 Previous 

 PAN-OS 11.2.7-h18 Addressed Issues 

 Next 

 PAN-OS 11.2.7-h16 Addressed Issues 

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

 11.2 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
