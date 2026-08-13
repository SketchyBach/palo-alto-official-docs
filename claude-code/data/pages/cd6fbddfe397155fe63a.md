---
url: https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-release-notes/pan-os-11-1-15-known-and-addressed-issues/pan-os-11-1-15-addressed-issues
fetched_at: 2026-08-13T17:12:21Z
source: palo-alto-main
---

# PAN-OS 11.1.15 Addressed Issues Clear

PAN-OS 11.1.15 Addressed Issues 

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

 PAN-OS 11.1.15 Addressed Issues 

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

 PAN-OS 11.1.15 Known and Addressed Issues 

 PAN-OS 11.1.15 Addressed Issues 

 Download PDF 

 PAN-OS 11.1.15 Addressed Issues 

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

 PAN-OS 11.1.15 Known and Addressed Issues 

 Next 

 PAN-OS 11.1.15 Known Issues 

 PAN-OS 11.1.15 Addressed Issues 

 Lists the addressed issues in PAN-OS 11.1.15. 

 The following table lists the addressed issues in PAN-OS 11.1.15. 

 Issue ID 

 Description 

 — 

 Fixes were made to address the following CVEs: 

 CVE-2026-0265 

 CVE-2026-0264 

 CVE-2026-0263 

 CVE-2026-0262 

 CVE-2026-0261 

 CVE-2026-0258 

 CVE-2026-0257 

 CVE-2026-0256 

 CVE-2026-0259 

 CVE-2026-0300 

 PAN-325120 

 Fixed an issue on PA-415, PA-415-5G, PA-445, PA-455, and PA-455-5G platforms where certain PAN-OS versions caused intermittent connectivity failures on the Eth1/1 data port and loss of power on PoE ports. 

 PAN-323243 

 Fixed an issue where a configd crash occurred when the Policies > Security view was updated or refreshed in the web interface. 

 PAN-322815 

 ( VM-Series firewalls on Microsoft Azure environments only ) Fixed an issue where the firewall entered maintenance mode after enabling FIPS-CC mode and rebooted. 

 PAN-319557 

 Fixed an issue where graphical counters did not display correctly in the control plane or dataplane monitor logs. 

 PAN-318784 

 Fixed an issue where the firewall stopped processing traffic and all VPN tunnels went down even when the firewall remained in an active state, and the CLI became unresponsive. 

 PAN-318567 

 Fixed an issue where the OpenConfig plugin stopped working after a configuration update. 

 PAN-317583 

 Fixed an issue with intermittent ICMP ping drops and packet loss in traffic flows between a hub and branch after upgrading to an affected PAN-OS release due to incorrect SD-WAN path monitor state. 

 PAN-317466 

 Fixed an issue where SIP sessions stopped progressing after the firewall received fragmented packets, fragmented at header field. 

 PAN-317372 

 Fixed an issue where custom administrators received an access denied error when attempting to view specific policy rule details from the Rule Shadow tab after a push from Panorama, even when the administrator had permissions to view Security policy rules. 

 PAN-316631 

 Fixed an issue BGP sessions experienced short disruptions across all peers, interfaces, and slots when a multicast event persisted longer than the NGP negotiated hold timers. 

 PAN-315820 

 Fixed an issue where User-ID XML API requests took longer than expected to return a response, which caused the web interface and captive portal pages to respond slowly or fail to load. this occurred when sending XML API requests for IP address-to-user mapping. 

 PAN-314875 

 ( PA-7500 firewalls only ) Fixed an issue where firewall logs were not visible in the Strata Logging Service even though cloud logging was enabled and the firewall was successfully forwarding logs. 

 PAN-314752 

 Fixed an issue on Panorama where, after removing a scheduled configuration push, Panorama still initiated the push at its previously scheduled time. 

 PAN-314385 

 ( Firewalls in active/passive HA clusters only ) Fixed an issue where high dataplane CPU usage occurred and traffic offloading decreased when a failover occurred from the active firewall to the passive firewall, and then back to the active firewall. 

 PAN-314126 

 Fixed an issue where session rematch did not properly apply updated Security policy rules to existing traffic flows after committing changes, which caused traffic to still be allowed when a new Security policy was set to Deny . 

 PAN-314020 

 Fixed an issue where the firewall did not decapsulate GENEVE packets when DNS Security retransmitted a DNS query after receiving a verdict from the cloud. 

 PAN-313828 

 Fixed an issue where the firewall did not forward traffic due to memory issues on a forwarding component. 

 PAN-313827 

 Fixed an issue where a memory leak occurred related to the reportd process when custom reports were run via API. 

 PAN-313711 

 Fixed an issue where the show system environmentals power CLI command displayed duplicate slot names and associated voltage values. 

 PAN-313700 

 Fixed an issue where an unexpected reboot occurred when Inline Cloud Analysis was enabled in an Anti-Spyware and Vulnerability profile. 

 PAN-313193 

 Firewalls in Layer 2 mode only ) Fixed an issue where the new sessions were not able to be established due to the firewall intermittently dropping valid MAC address entries for specific VLANs when a manual switchover sent a high volume of traffic to the firewall. 

 PAN-311248 

 Fixed an issue where the ABR failed to translate and advertise the default route (0.0.0.0/0) from an OSPF NSSA area into the OSPF backbone area as a Type-5 LSA. 

 PAN-310472 

 Fixed an issue on the web interface where checkboxes for default information originate and ABR in OSPF NSSA configurations were automatically enabled which resulted in unexpected configuration changes. 

 PAN-307470 

 Fixed an issue where an External Dynamic List (EDL) fetch with an invalid certificate was skipped on newly provisioned GlobalProtect gateway instances. 

 PAN-298960 

 Fixed an issue where the firewall continuously rebooted when the useridd process repeatedly restarted. 

 PAN-295309 

 Fixed an issue where OSPF session using MD5 authentication experienced intermittent flapping due to out-of-order packet processing. 

 PAN-294001 

 Fixed an issue on Panorama managed firewalls generated Failed in get_pwchange_required error messages in the authd logs for local administators. 

 PAN-293142 

 Fixed an issue where firewall components became unresponsive during sustained operation. 

 PAN-289706 

 Fixed an issue where the authd process crashed intermittently on VM-Series firewalls due to authentication sequence failures. The crashes occurred during memory management operations within a library while releasing memory to its central cache. 

 PAN-285213 

 Fixed an issue where proxy requests for certificate status (OCSP/CRL) from sslmgr contained incorrect values that caused unknown certificates to be blocked. 

 PAN-282335 

 Fixed an issue where firewalls in a cluster experienced approximately 50% packet loss on IPSec NATT tunnels when tunnel acceleration was enabled. 

 PAN-273805 

 Fixed an issue where SAML authentication for GlobalProtect failed when the GlobalProtect portal was accessed externally on a non-standard port. 

 PAN-271412 

 Fixed an issue where the character ( + ) in the authentication message prompt displayed incorrectly as #43; on the GlobalProtect client after upgrading to a PAN-OS 10.2 release. 

 PAN-257879 

 Fixed an issue where, after a system event, selecting a configuration file from maintenance mode loaded the incorrect configuration. 

 PAN-236914 

 Fixed an issue where TCP MSS adjustment did not function as expected for GRE tunnels when TCP SYN or SYN-ACK packets that were received had an MMS higher than 1460 bytes. 

 Previous 

 PAN-OS 11.1.15 Known and Addressed Issues 

 Next 

 PAN-OS 11.1.15 Known Issues 

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

 11.1 

 Next-Generation Firewall 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
