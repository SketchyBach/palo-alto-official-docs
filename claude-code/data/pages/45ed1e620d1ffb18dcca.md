---
url: https://docs.paloaltonetworks.com/pan-os/10-1/pan-os-admin/firewall-administration/reference-web-interface-administrator-access/web-interface-access-privileges/provide-granular-access-to-operations-settings
fetched_at: 2026-09-16T07:34:17Z
source: palo-alto-main
---

# Provide Granular Access to Operations Settings Clear

Updated on 

 Mon Aug 31 04:46:16 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 Firewall Administration 

 Reference: Web Interface Administrator Access 

 Web Interface Access Privileges 

 Provide Granular Access to Operations Settings 

 Download PDF 

 Next-Generation Firewall 

 Provide Granular Access to Operations Settings 

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

 New Features 

 Previous 

 Provide Granular Access to the Panorama Tab 

 Next 

 Panorama Web Interface Access Privileges 

 Provide Granular Access to Operations Settings 

 Configure granular administrator access privileges for operations settings in PAN-OS
 firewall web interface to control user permissions. 

 To define which operations settings an
administrator has access to, when creating or editing an admin role
profile for a firewall ( Device Admin Roles ), scroll down to
the Operations option on the Web
UI tab. 

 Access Level 

 Description 

 Enable 

 Read Only 

 Disable 

 Reboot 

 Restart the firewall. The firewall logs out
all users, reloads the PAN-OS software and active configuration,
closes and logs existing sessions, and creates a system log entry
that shows the name of the administrator that initiated the reboot.
This access also affects Shutdown operations. 

 Yes 

 N/A 

 Yes 

 Generate Tech Support File 

 Generate a tech support system
file that the Palo Alto Networks support team can use to troubleshoot
issues that you may be experiencing with the firewall. 

 Yes 

 N/A 

 Yes 

 Generate Stats Dump File 

 Generate and download a set of XML reports
that summarizes network traffic over the last seven days for the firewall. 

 Yes 

 N/A 

 Yes 

 Download Core Files 

 If the firewall experiences a system process
failure, a core file is automatically generated that contains details
about the process and why it failed. You can download this core
file to upload to your Palo Alto Networks support case to obtain further
assistance in resolving the issue. 

 Yes 

 N/A 

 Yes 

 Download Debug and Management Pcap Files 

 If your firewall experiences a packet capture
failure, it generates a packet capture (pcap) file that contains
debug and management details for why it failed. You can download
this pcap file to upload it to a Palo Alto Networks support case
to obtain assistance in resolving the issue. 

 Yes 

 N/A 

 Yes 

 Previous 

 Provide Granular Access to the Panorama Tab 

 Next 

 Panorama Web Interface Access Privileges
