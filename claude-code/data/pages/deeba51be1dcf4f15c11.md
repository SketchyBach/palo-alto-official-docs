---
url: https://docs.paloaltonetworks.com/pan-os/11-2/pan-os-release-notes/pan-os-11-2-7-known-and-addressed-issues/pan-os-11-2-7-h17-addressed-issues
fetched_at: 2026-09-16T07:40:41Z
source: palo-alto-main
---

# PAN-OS 11.2.7-h17 Addressed Issues Clear

Updated on 

 Wed Sep 09 08:56:33 PDT 2026 

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
