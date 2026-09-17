---
url: https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-release-notes/pan-os-11-1-2-known-and-addressed-issues/pan-os-11-1-2-h14-addressed-issues
fetched_at: 2026-09-16T07:40:20Z
source: palo-alto-main
---

# PAN-OS 11.1.2-h14 Addressed Issues Clear

Updated on 

 Sep 9, 2026 

 Focus 

 Home 

 PAN-OS 

 PAN-OS 11.1.2 Known and Addressed Issues 

 PAN-OS 11.1.2-h14 Addressed Issues 

 Download PDF 

 PAN-OS 11.1.2-h14 Addressed Issues 

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

 PAN-OS 11.1.2-h15 Addressed Issues 

 Next 

 PAN-OS 11.1.2-h12 Addressed Issues 

 PAN-OS 11.1.2-h14 Addressed Issues 

 PAN-OS 11.1.2-h14 addressed issues. 

 Issue ID 

 Description 

 PAN-262287 

 Fixed an issue where dereferencing a NULL pointer that occurred
 caused pan_task processes to stop responding. 

 PAN-261673 

 ( VM-Series firewalls on Microsoft Azure environments only )
 Fixed an issue where, when Accelerated Networking was enabled,
 traffic was dropped because of the 
 flow_parse_ip_hdr counter related to an Nvidia
 driver issue. 

 PAN-259151 

 Fixed an issue where unused objects were pushed to the firewall,
 which caused configuration pushes to fail with the error
 Number of address groups exceed platform
 capacity . 

 PAN-259002 

 Fixed an issue where frequent external dynamic list updates caused
 the configd process to restart. 

 PAN-257601 

 ( PA-5450 firewalls only ) Fixed an issue where Networking
 Cards (NC) experienced an internal link fault which caused path
 monitoring failure on the Dataplane Processing Card (DPC). 

 PAN-257327 

 Fixed an issue where a failover event occurred unexpectedly on the
 firewall. 

 PAN-253626 

 Fixed an issue on Panorama where unused objects were pushed to the
 firewall, which caused the push operations to intermittently
 fail. 

 PAN-236191 

 Fixed an issue where the web interface performance was slower than
 expected. 

 PAN-222542 

 ( PA-7000 Series firewalls only ) Fixed an issue where Log
 Forward Cards (LFC) were incorrectly identified as distribution
 policies, which caused packet loss due to traffic, BFD, and other
 control packets being forwarded to the LFC. 

 Previous 

 PAN-OS 11.1.2-h15 Addressed Issues 

 Next 

 PAN-OS 11.1.2-h12 Addressed Issues
