---
url: https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/user-id/map-ip-addresses-to-users/map-ip-addresses-to-usernames-using-captive-portal/captive-portal-modes
fetched_at: 2026-08-13T17:10:11Z
source: palo-alto-main
---

# Authentication Portal Modes Clear

Authentication Portal Modes 

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

 Authentication Portal Modes 

 Updated on 

 Mon Aug 03 13:41:44 PDT 2026 

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

 Mon Aug 03 13:41:44 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 User-ID 

 Map IP Addresses to Users 

 Map IP Addresses to Usernames Using Authentication Portal 

 Authentication Portal Modes 

 Download PDF 

 Next-Generation Firewall 

 Authentication Portal Modes 

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

 Authentication Portal Authentication Methods 

 Next 

 Configure Authentication Portal 

 Authentication Portal Modes 

 The Authentication Portal mode defines how the firewall
captures web requests for authentication: 

 Mode 

 Description 

 Transparent 

 The firewall intercepts the browser traffic
per the Authentication policy rule and impersonates the original destination
URL, issuing an HTTP 401 to invoke authentication. However, because
the firewall does not have the real certificate for the destination
URL, the browser displays a certificate error to users attempting
to access a secure site. Therefore, use this mode only when absolutely
necessary, such as in Layer 2 or virtual wire deployments. 

 Redirect 

 The firewall intercepts unknown HTTP or
HTTPS sessions and redirects them to a Layer 3 interface
on the firewall using an HTTP 302 redirect to perform authentication.
This is the preferred mode because it provides a better end-user
experience (no certificate errors). However, it does require additional
Layer 3 configuration. Another benefit of the Redirect mode is that
it provides for the use of session cookies, which enable the user
to continue browsing to authenticated sites without requiring re-mapping
each time the timeouts expire. This is especially useful for users
who roam from one IP address to another (for example, from the corporate
LAN to the wireless network) because they won’t need to re-authenticate
when the IP address changes as long as the session stays open. 

 If
you use Kerberos SSO, you must use Redirect mode because the browser
will provide credentials only to trusted sites. Redirect mode is
also required if you use Multi-Factor Authentication to authenticate
Authentication Portal users. 

 Previous 

 Authentication Portal Authentication Methods 

 Next 

 Configure Authentication Portal 

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

 Network Security 

 PAN-OS 

 Next-Generation Firewall 

 Administration 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
