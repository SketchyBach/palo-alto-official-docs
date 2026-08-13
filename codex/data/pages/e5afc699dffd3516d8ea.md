---
url: https://docs.paloaltonetworks.com/ngfw/help/11-1/user-identification/device-user-identification-user-mapping/monitor-servers/manage-access-to-monitored-servers
fetched_at: 2026-08-13T16:47:01Z
source: palo-alto-main
---

# Manage Access to Monitored Servers Clear

Manage Access to Monitored Servers 

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

 Manage Access to Monitored Servers 

 Updated on 

 Thu Jun 25 17:39:35 PDT 2026 

 Focus 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 한국어 (Korean) 

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

 Updated on 

 Thu Jun 25 17:39:35 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 User Identification 

 Device > User Identification > User Mapping 

 Monitor Servers 

 Manage Access to Monitored Servers 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 한국어 (Korean) 

 Next-Generation Firewall 

 Manage Access to Monitored Servers 

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

 Configure Access to Monitored Servers 

 Next 

 Include or Exclude Subnetworks for User Mapping 

 Manage Access to Monitored Servers 

 Perform the following tasks in the Server Monitoring
section to manage access to the servers that the User-ID agent monitors
for user mapping information. 

 Task 

 Description 

 Display server information 

 For each monitored server, the User Mapping
page displays the Status of the connection from the User-ID agent
to the server. After you Add a server, the firewall
tries to connect to it. If the connection attempt is successful,
the Server Monitoring section displays Connected in the Status column.
If the firewall cannot connect, the Status column displays an error
condition, such as Connection refused or Connection
timeout . 

 For details on the other fields that
the Server Monitoring section displays, see Configure
Access to Monitored Servers . 

 Add 

 To Configure
Access to Monitored Servers , Add each
server that the User-ID agent will monitor for user mapping information. 

 Delete 

 To remove a server from the user mapping
process (discovery), select the server and Delete it. 

 Tip :
To remove a server from discovery without deleting its configuration, edit
the server entry and clear Enabled . 

 Discover 

 You can automatically Discover Microsoft
Active Directory domain controllers using DNS. The firewall will
discover domain controllers based on the domain name entered in
the Device Setup Management page, General
Settings section, Domain field.
After discovering a domain controller, the firewall creates an entry
for it in the Server Monitoring list; you can then enable the server
for monitoring. 

 The Discover feature
works for domain controllers only, not Exchange servers or eDirectory
servers. 

 Previous 

 Configure Access to Monitored Servers 

 Next 

 Include or Exclude Subnetworks for User Mapping 

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

 PAN-OS 

 11.1 

 Next-Generation Firewall 

 Help 

 Web Interface 

 Panorama 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
