---
url: https://docs.paloaltonetworks.com/pan-os/10-1/pan-os-admin/authentication/plan-your-authentication-deployment
fetched_at: 2026-08-13T16:59:05Z
source: palo-alto-main
---

# Plan Your Authentication Deployment Clear

Plan Your Authentication Deployment 

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

 Plan Your Authentication Deployment 

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

 Plan Your Authentication Deployment 

 Download PDF 

 Next-Generation Firewall 

 Plan Your Authentication Deployment 

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

 Local Authentication 

 Next 

 Configure Multi-Factor Authentication 

 Plan Your Authentication Deployment 

 Learn about the things to consider before you implement
an authentication solution on your next-gen firewall. 

 The following are key questions to consider before you
implement an authentication solution for administrators who access
the firewall and end users who access services and applications
through Authentication Portal. 

 For both end users and administrators, consider: 

 How can you leverage your existing
security infrastructure? Usually, integrating the firewall with
an existing infrastructure is faster and cheaper than setting up a
new, separate solution just for firewall services. The firewall
can integrate with Multi-Factor
Authentication , SAML , Kerberos , TACACS+ , RADIUS ,
and LDAP servers.
If your users access services and applications that are external
to your network, you can use SAML to integrate the firewall with
an identity provider (IdP) that controls access to both external
and internal services and applications. 

 How can you optimize the user experience? If you don’t want
users to authenticate manually and you have a public key infrastructure,
you can implement certificate authentication. Another option is
to implement Kerberos or SAML single
sign-on (SSO) so that users can access multiple services and applications after
logging in to just one. If your network requires additional security,
you can combine certificate authentication with interactive (challenge-response) authentication. 

 Do you require special user accounts that you don’t manage
through the directory servers that your organization reserves for
regular accounts? For example, you might define a superuser account
that is local to the firewall so that you can access the firewall
even if the directory server is down. You can configure Local
Authentication for these special-purpose accounts. 

 External
Authentication Services are usually preferable to local authentication
because they provide central account management, reliable authentication
services, and usually logging and troubleshooting features. 

 Are the user names for your user accounts properly formatted?
Leveraging SAML , Kerberos , TACACS+ , RADIUS ,
and LDAP authentication
requires all user names adhere to the regular expression Linux login
name rule. User names must have the format [a-zA-Z0-9_.][a-zA-Z0-9_.-]{0,30}[a-zA-Z0-9_.$-] . 

 This
means that: 

 The first character of the user name must
be an upper or lower case alphabetical letter, a number (0-9), or
either _ (underscore) or . (period). 

 Other than the first and last characters, the user name may
contain upper or lower case alphabetical characters, numbers (0-9),
and _ (underscore), . (period),
or - (dash). The maximum length is 30 characters
excluding the first and last characters. 

 The last character of the user name may be an upper or lower
case alphabetical letter, a number (0-9), or _ (underscore), . (period), $ ,
or - (dash). 

 Adhering to
the regular expression Linux login name rule is required for PAN-OS administrators
only. It is not required for GlobalProtect and Captive Portal users. 

 For end users only, consider: 

 Which services and applications
are more sensitive than others? For example, you might want stronger
authentication for key financial documents than for search engines.
To protect your most sensitive services and applications, you can
configure Multi-Factor
Authentication (MFA) to ensure that each user authenticates
using multiple methods (factors) when accessing those services and
applications. To accommodate a variety of security needs, Configure
Authentication Policy rules that trigger MFA or single factor
authentication (such as login credentials or certificates) based
on specific services, applications, and end users. Other ways to
reduce your attack surface include network segmentation and user groups for allowed applications . 

 For administrators only, consider: 

 Do you use an external server
to centrally manage authorization for all administrative accounts?
By defining Vendor-Specific Attributes (VSAs) on the external server,
you can quickly change administrative role assignments through your
directory service instead of reconfiguring settings on the firewall. VSAs
also enable you to specify access domains for administrators of
firewalls with multiple virtual systems. SAML , TACACS+ ,
and RADIUS support
external authorization. 

 Previous 

 Local Authentication 

 Next 

 Configure Multi-Factor Authentication 

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
