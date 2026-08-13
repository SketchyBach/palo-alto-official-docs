---
url: https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-release-notes/pan-os-11-1-6-known-and-addressed-issues/pan-os-11-1-6-h7-addressed-issues
fetched_at: 2026-08-13T17:12:38Z
source: palo-alto-main
---

# PAN-OS 11.1.6-h7 Addressed Issues Clear

PAN-OS 11.1.6-h7 Addressed Issues 

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

 PAN-OS 11.1.6-h7 Addressed Issues 

 Updated on 

 Tue Aug 11 16:14:24 PDT 2026 

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

 Tue Aug 11 16:14:24 PDT 2026 

 Focus 

 Home 

 PAN-OS 

 PAN-OS 11.1.6 Known and Addressed Issues 

 PAN-OS 11.1.6-h7 Addressed Issues 

 Download PDF 

 PAN-OS 11.1.6-h7 Addressed Issues 

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

 PAN-OS 11.1.6-h10 Addressed Issues 

 Next 

 PAN-OS 11.1.6-h6 Addressed Issues 

 PAN-OS 11.1.6-h7 Addressed Issues 

 PAN-OS 11.1.6-h7 addressed issues. 

 Issue ID 

 Description 

 PAN-286255 

 Fixed an issue where, when the firewall received an unexpected
 termination request for SSL sessions, the dataplane experienced a
 slow buffer resource leak. 

 PAN-285941 

 Fixed an issue where high memory consumption occurred on the
 logrcvr process. 

 PAN-285651 

 ( Panorama appliances in active/passive HA configurations on
 Microsoft Azure environments only ) Fixed an issue on
 Panorama that caused firewalls to disconnect unexpectedly. 

 PAN-285597 

 Fixed an issue where a routed process memory leak
 occurred when advanced routing was enabled. 

 PAN-282391 

 Fixed an issue on Panorama where a memory leak occurred after cloning
 a template, resulting in an increase in memory use, which caused OOM
 errors. 

 PAN-282206 

 Fixed an issue where configuring Secure Web Gateway (SWG) in
 no-auth mode led to latency when no
 decryption policy rules or No-decrypt policy
 rules were present. 

 PAN-282069 

 Fixed an issue on Panorama where Security policy rules were removed
 from device groups when you cloned or edited Security policy rules
 that used more than 63 characters. 

 PAN-281649 

 Fixed an issue where the index size limit was incorrectly calculated
 and indices rolled over earlier than expected, which resulted in
 high memory and OOM errors. 

 PAN-280942 

 Fixed an issue where the logrcvr process stopped
 responding. 

 PAN-279691 

 ( Firewalls in active/passive HA configurations only ) Fixed
 an issue where the firewall didn't synchronize IPSec SAs (security
 associations) to the passive firewall if the tunnel was not
 initially established by the active firewall. 

 PAN-274671 

 Fixed an issue where empty traffic logdb folders were
 generated for each day even when trafcfic logs were not received by
 the logrcvr process. 

 PAN-274570 

 Fixed an issue where the devsrvr process restarted after
 a failed commit due to an invalid memory access. 

 PAN-271701 

 Fixed an issue where Advanced Services, App-ID Cloud Engine (ACE),
 and Enhanced Application Log stopped working due to incorrect memory
 usage accounting, which caused memory usage to remain at 99% after
 an extended period of time. 

 PAN-271273 

 Fixed an issue where dynamic update downloads failed when
 IPv6 firewalling was enabled on the
 firewall and both IPv4 and IPv6 were configured on the management
 interface. 

 PAN-271175 

 Fixed an issue where the all_task process stopped
 responding with a SIGABRT. 

 PAN-269027 

 Fixed an issue related to external dynamic lists that caused commit
 times on the firewall to be higher than expected. 

 PAN-268614 

 Fixed an issue on the web interface where, when all rules were
 highlighted when a read-only admin user clicked the
 Highlight Unused Rules checkbox. 

 PAN-268118 

 Fixed an issue on firewalls in active/passive HA configurations
 where, after a failover, irrelevant routing FIB entries were seen in
 the routing table on the newly active firewall. 

 PAN-267444 

 Fixed an issue where large file downloads or uploads failed or
 remained in an incomplete state when using DLP HTTP2 mirror mode.

 PAN-260015 

 Fixed an issue on the firewall where the dataplane restarted due to
 insufficient allocation of memory buffers. 

 PAN-256867 

 Fixed an issue where the logrcvr process stopped
 responding while processing session logs for forwarding to the LFC.

 PAN-255914 

 ( VM-Series firewalls on Amazon Web Services (AWS) environments
 only ) Fixed an issue where a newly bootstrapped firewall
 required a management server restart, relicensing, or license push
 from Panorama to invoke the device certificate. 

 Previous 

 PAN-OS 11.1.6-h10 Addressed Issues 

 Next 

 PAN-OS 11.1.6-h6 Addressed Issues 

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

 11.1 

 Next-Generation Firewall 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
