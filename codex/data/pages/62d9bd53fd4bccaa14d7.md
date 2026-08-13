---
url: https://docs.paloaltonetworks.com/pan-os/10-1/pan-os-admin/authentication/authentication-types/local-authentication
fetched_at: 2026-08-13T16:58:55Z
source: palo-alto-main
---

# Local Authentication Clear

Local Authentication 

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

 Local Authentication 

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

 Authentication 

 Authentication Types 

 Local Authentication 

 Download PDF 

 Next-Generation Firewall 

 Local Authentication 

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

 LDAP 

 Next 

 Plan Your Authentication Deployment 

 Local Authentication 

 Although the firewall and Panorama provide local authentication
for administrators and end users, External
Authentication Services are preferable in most cases because
they provide central account management. However, you might require
special user accounts that you don’t manage through the directory
servers that your organization reserves for regular accounts. For example,
you might define a superuser account that is local to the firewall
so that you can access the firewall even if the directory server
is down. In such cases, you can use the following local authentication
methods: 

 (Firewall only) Local database authentication —To Configure
Local Database Authentication , you create a database that
runs locally on the firewall and contains user accounts (usernames
and passwords or hashed passwords) and user groups. This type of authentication
is useful for creating user accounts that reuse the credentials
of existing Unix accounts in cases where you know only the hashed
passwords, not the plaintext passwords. Because local database authentication
is associated with authentication profiles, you can accommodate
deployments where different sets of users require different authentication
settings, such as Kerberos single
sign-on (SSO) or Multi-Factor
Authentication (MFA). (For details, see Configure
an Authentication Profile and Sequence ). For administrator
accounts that use an authentication profile, password complexity and expiration
settings are not applied. This authentication method is available
to administrators who access the firewall (but not Panorama) and
end users who access services and applications through Authentication
Portal or GlobalProtect. 

 Local authentication without a database —You can configure firewall administrative accounts or Panorama administrative accounts without
creating a database of users and user groups that runs locally on
the firewall or Panorama. Because this method is not associated
with authentication profiles, you cannot combine it with Kerberos SSO
or MFA. However, this is the only authentication method that allows
password profiles, which enable you to associate individual accounts
with password expiration settings that differ from the global settings.
(For details, see Define password complexity and expiration settings ) 

 Previous 

 LDAP 

 Next 

 Plan Your Authentication Deployment 

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
