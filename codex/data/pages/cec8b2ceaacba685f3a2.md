---
url: https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-panorama-api/pan-os-xml-api-use-cases/show-and-manage-globalprotect-users-api
fetched_at: 2026-08-13T17:06:52Z
source: palo-alto-main
---

# Show and Manage GlobalProtect Users (API) Clear

Show and Manage GlobalProtect Users (API) 

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

 Show and Manage GlobalProtect Users (API) 

 Updated on 

 Aug 28, 2025 

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

 New Features 

 Updated on 

 Aug 28, 2025 

 Focus 

 Home 

 Next-Generation Firewall 

 PAN-OS XML API Use Cases 

 Show and Manage GlobalProtect Users (API) 

 Download PDF 

 Next-Generation Firewall 

 Show and Manage GlobalProtect Users (API) 

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

 Upgrade a Firewall to the Latest PAN-OS Version (API) 

 Next 

 Query a Firewall from Panorama (API) 

 Show and Manage GlobalProtect Users (API) 

 Get and manage GlobalProtect user information using the XML API. 

 One common use of the PAN-OS XML API is to manage and view information about your GlobalProtect
 users. To learn more about getting started with GlobalProtect , view the GlobalProtect Get Started
 chapter. You must have a working GlobalProtect configuration to get meaningful results from
 the API. 

 You can use two API requests to view and then disconnect a Global Protect user who has been
 logged in for too long, using this guide you can seen an example of retrieving those users
 as well as disconnecting them. 

 View all GlobalProtect users. 

 Make a request to view all GlobalProtect users: 

 curl -X POST 'https://<firewall>/api?type=op&cmd=<show><global-protect-gateway><current-user/>
 </global-protect-gateway></show>' 

 The response contains a list of users along
with related information including IP addresses, logins, and client
information: 

 <response status="success">
 <result>
 <entry>
 <domain/>
 <islocal>yes</islocal>
 <username>dward</username>
 <computer>Dan’s iPhone</computer>
 <client>Apple iOS 8.1.2</client>
 <vpn-type>Device Level VPN</vpn-type>
 <virtual-ip>192.168.2.1</virtual-ip>
 <public-ip>166.173.63.240</public-ip>
 <tunnel-type>SSL</tunnel-type>
 <login-time>Jan.22 01:50:36</login-time>
 <login-time-utc>1421916636</login-time-utc>
 <lifetime>2592000</lifetime>
 </entry>
 </result>
</response>

 The <login-time-utc> field
is the login date/time in UNIX time format (number of seconds elapsed
since 00:00:00 1 Jan 1970). To find the list of users, filter the
output for this field and compare the <login-time-utc> value
to current date and time (or another date and time). 

 Disconnect a GlobalProtect user. 

 Upon identifying the user that you want to disconnect,
send a request that includes the GlobalProtect gateway, username,
computer, and a force-logout reason: 

 curl -X POST 'https://<firewall>/api?type=op&cmd=<request><global-protect-gateway><client-logout>
 <gateway>Home-N</gateway><user>dward</user><reason>force-logout</reason>
 <computer>Dan’s%20iPhone</computer></client-logout></global-protect-gateway>
 </request>' 

 A successful response shows that the user has
been successfully disconnected: 

 <response status="success">
 <result>
 <response status="success">
 <gateway>Home-N</gateway>
 <domain>(null)</domain>
 <user>dward</user>
 <computer>Dan’s iPhone</computer>
 </response>
 </result>
</response>

 Previous 

 Upgrade a Firewall to the Latest PAN-OS Version (API) 

 Next 

 Query a Firewall from Panorama (API) 

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

 Next-Generation Firewall 

 Reference 

 API 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
