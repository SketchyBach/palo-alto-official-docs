---
url: https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-release-notes/pan-os-10-2-16-known-and-addressed-issues/pan-os-10-2-16-h7-addressed-issues
fetched_at: 2026-08-13T17:07:10Z
source: palo-alto-main
---

# PAN-OS 10.2.16-h7 Addressed Issues Clear

PAN-OS 10.2.16-h7 Addressed Issues 

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

 PAN-OS 10.2.16-h7 Addressed Issues 

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

 PAN-OS 10.2.16 Known and Addressed Issues 

 PAN-OS 10.2.16-h7 Addressed Issues 

 Download PDF 

 PAN-OS 10.2.16-h7 Addressed Issues 

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

 PAN-OS 10.2.16-h8 Addressed Issues 

 Next 

 PAN-OS 10.2.16-h6 Addressed Issues 

 PAN-OS 10.2.16-h7 Addressed Issues 

 PAN-OS® 10.2.16-h7 addressed issues. 

 After upgrading to this release, all GlobalProtect users
 will be required to reauthenticate. 

 Issue ID 

 Description 

 — 

 Fixes were made to address the following CVEs: 

 CVE-2026-0265 

 CVE-2026-0264 

 CVE-2026-0262 

 CVE-2026-0261 

 CVE-2026-0258 

 CVE-2026-0257 

 CVE-2026-0256 

 CVE-2026-0259 

 CVE-2026-0300 

 PAN-316911 

 ( VM-Series firewalls on Amazon Web Services (AWS) environments
 only ) Fixed an issue where a newly bootstrapped firewall
 required a management server restart, relicensing, or license push
 from Panorama to invoke the device certificate. 

 PAN-313828 

 Fixed an issue where the firewall did not forward traffic due to
 memory issues on a forwarding component. 

 PAN-308507 

 ( Panorama managed firewalls only ) Fixed an issue where the
 firewall intermittently failed to maintain active log forwarding
 streams to Strata Logging Service (SLS) even when duplicate logging
 and enhanced application logging were enabled. 

 PAN-305415 

 Fixed an issue where commits caused high dataplane CPU utilization
 and briefly increased Packet Descriptors, which disrupted
 traffic. 

 PAN-303051 

 Fixed an issue on Panorama where a memory leak occurred related to
 the reportd process due to retaining memory that was
 temporarily used for report generation instead of releasing the
 memory for reuse, which resulted in continuous accumulation and
 memory exhaustion. 

 PAN-301409 

 Fixed an issue where Panorama failed to perform a selective push to a
 managed device when device tags were added or modified on the policy
 rules. The selective push failed with the error message
 Failed to generate selective push configuration.
 Schema validation failed. Please try a full
 push . 

 PAN-297610 

 Fixed an issue where the firewall became unresponsive after an
 upgrade due to the fsck command scanning drive
 partitions in parallel with the root partition, which caused the
 process to take an extended amount of time. 

 PAN-297295 

 ( VM-Series firewalls in Microsoft Azure environments only )
 Fixed an issue where the firewall repeatedly restarted due to high
 packet rates on the synthetic path in DPDK mode. 

 PAN-295470 

 Fixed an issue on the firewall where the useridd process
 continuously increased its memory consumption, which resulted in an
 OOM condition that caused the firewall to restart. 

 PAN-292393 

 Fixed an issue where TFTP file transfers intermittently timed out in
 active-active HA pairs when the TFTP control channel was processed
 by one firewall and the data channel was processed by the other.
 This occurred because the firewall receiving the data channel failed
 to match the predicted session due to asynchronous processing of HA
 messages. 

 PAN-291067 

 Fixed an issue where the devsrvr process periodically
 exceeded its virtual memory limit and restarted, which led to
 intermittent outages. 

 PAN-289249 

 Fixed an issue where a memory leak occurred on the
 reportd process when a WildFire update was
 initiated while device telemetry data collection was in progress.
 This resulted in an OOM condition. 

 PAN-286094 

 Fixed an issue where the firewall did not forward logs to SLS when
 using a proxy server configuration due to an OCSP validation
 failure. 

 PAN-285208 

 Fixed an issue where the firewall did not automatically recover after
 a machine check exception (MCE) occurred. 

 PAN-242952 

 Fixed an issue where high SSL traffic depleted flex memory, which
 prevented the firewall from revalidating SSLVPN client CAs during
 configuration pushes. 

 Previous 

 PAN-OS 10.2.16-h8 Addressed Issues 

 Next 

 PAN-OS 10.2.16-h6 Addressed Issues 

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
