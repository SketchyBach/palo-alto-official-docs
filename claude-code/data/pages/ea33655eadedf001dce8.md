---
url: https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-release-notes/pan-os-10-2-9-known-and-addressed-issues/pan-os-10-2-9-addressed-issues
fetched_at: 2026-08-13T17:07:25Z
source: palo-alto-main
---

# PAN-OS 10.2.9 Addressed Issues Clear

PAN-OS 10.2.9 Addressed Issues 

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

 PAN-OS 10.2.9 Addressed Issues 

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

 PAN-OS 10.2.9 Known and Addressed Issues 

 PAN-OS 10.2.9 Addressed Issues 

 Download PDF 

 PAN-OS 10.2.9 Addressed Issues 

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

 PAN-OS 10.2.9-h1 Addressed Issues 

 Next 

 PAN-OS 10.2.8 Known and Addressed Issues 

 PAN-OS 10.2.9 Addressed Issues 

 PAN-OS 10.2.9 addressed issues. 

 Issue ID 

 Description 

 PAN-250686 

 Fixed an issue where selective push operations did not work when more
 than one admin user simultaneously performed changes and partial
 commits on Panorama. 

 PAN-247403 

 ( VM-Series firewalls only ) Fixed an issue where the push scope CLI command took longer than expected, which caused the web interface to be slow. 

 PAN-246431 

 Fixed an issue where a Push to Device operation remained at the state None when performing a selective push to device groups and templates that included both connected and disconnected firewalls. 

 PAN-245701 

 Fixed an issue where the returned values to SNMP requests for data port statistics were
 incorrect. 

 PAN-244836 

 A knob was introduced to toggle the default behavior of BGP in the Advanced Routing stack to not suppress duplicate updates. By default, the prefix updates are suppressed for optimization. 

 PAN-244548 

 Fixed an issue where ECMP sessions changed destination MAC addresses
 mid-session, which caused connections to be reset. 

 PAN-244493 

 Fixed a memory limitation with mapping subinterfaces to VPCE endpoints for GCP IPS, Amazon Web Services (AWS) integration with GWLB, and NSX service chain mapping. 

 PAN-243463 

 Fixed an issue where high Enhanced Application Log traffic used
 excess system resources and caused processes to not work. 

 PAN-242910 

 Fixed an issue where a custom based non-Superuser was unable to push to firewalls. 

 PAN-242627 

 Fixed an issue where selective push did not work. 

 PAN-241018 

 ( VM-Series firewalls in Microsoft Azure environments only )
 Fixed a Dataplane Development Kit (DPDK) issue where interfaces remained
 in a link-down stage after an Azure hot plug event. 

 PAN-240477 

 Fixed a temporary hardware issue that caused PAN-SFP-PLUS-CU-5M to
 not be able to link up on PA-5400 Series, PA-3400 Series, and
 PA-1400 Series firewalls. 

 PAN-240066 

 Fixed a duplicate MAC address issue where an ethernet interface sent
 out Gratuitous ARP (GARP) messages for an IP address that was not
 configured on it. 

 PAN-239722 

 Fixed an issue where SNMP scans to the firewall took longer than expected and intermittently timed out. 

 PAN-238643 

 Fixed an issue where a memory leak caused multiple processes to stop responding when VM Information Sources was configured. 

 PAN-237991 

 Fixed an issue where the log collector sent fewer logs than expected to the syslog server. 

 PAN-233692 

 Fixed an issue on Panorama where the configd process stopped, which caused performance issues. 

 PAN-233684 

 Fixed an issue on Panorama where Push to
 Devices or Commit and Push 
 operations took longer than expected on the web interface. 

 PAN-231439 

 Fixed an issue where, when a VoIP call using dynamic IP and NAT was put on hold, the audio became one-way due to early termination of NAT ports. 

 PAN-230746 

 Fixed an issue on the web interface where device groups with a large number of managed firewalls displayed the Policy page more slowly than expected. 

 PAN-228515 

 Fixed an issue where the Elasticsearch cluster health status displayed as yellow or red due to Elasticsearch SSH tunnel flaps. 

 PAN-224500 

 Fixed an issue where IPv6 addresses in XFF were displayed in Traffic logs. 

 PAN-222188 

 A CLI command was introduced to address an issue where SNMP monitoring performance was slower
 than expected, which resulted in
 snmpwalk timeouts. 

 PAN-215430 

 Fixed an issue where dynamic IP address NAT with SIP intermittently failed to convert RTP Predict
 sessions. 

 PAN-212553 

 Fixed an issue where the ikemgr process stopped responding due to memory corruption, which caused VPN tunnels to go down. 

 PAN-207092 

 Fixed an issue where logging in using default credentials after changing to FIPS-CC for NSX-T firewalls did not work. 

 Previous 

 PAN-OS 10.2.9-h1 Addressed Issues 

 Next 

 PAN-OS 10.2.8 Known and Addressed Issues 

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
