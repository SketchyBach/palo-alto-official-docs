---
url: https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/user-id/user-id-concepts/group-mapping
fetched_at: 2026-08-13T17:05:26Z
source: palo-alto-main
---

# Group
Mapping Clear

Group
Mapping 

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

 Group
Mapping 

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

 User-ID
Concepts 

 Group
Mapping 

 Download PDF 

 Next-Generation Firewall 

 Group
Mapping 

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

 User-ID Concepts 

 Next 

 User Mapping 

 Group
Mapping 

 Learn why the firewall needs to query an LDAP directory for group membership even when your IdP sends group information in authentication assertions. 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by PAN-OS or Panorama) 

 No prerequisites needed 

 To define policy rules based on user or group, first
you create an LDAP server profile that defines how the firewall
connects and authenticates to your directory server. The firewall
supports a variety of directory servers, including Microsoft Active
Directory (AD), Novell eDirectory, and Sun ONE Directory Server.
The server profile also defines how the firewall searches the directory
to retrieve the list of groups and the corresponding list of members.
If you are using a directory server that is not natively supported
by the firewall, you can integrate the group mapping function using
the XML API. You can then create a group mapping configuration to Map Users to Groups and Enable User- and Group-Based Policy . 

 When you use SAML, RADIUS, or TACACS+ for authentication, the identity provider (IdP)
sends an assertion that reflects user attributes at the moment of authentication. PAN-OS®
references SAML group attributes in one specific context: the User Group
Attribute in an authentication profile, where the firewall compares the value
against the Allow List to control who can authenticate. The firewall does not use SAML
assertion data to populate its user-to-group mapping table for policy enforcement or
reporting. Group-based security policy evaluation, GlobalProtect® app configurations, and
log queries and reports by user group all require a persistent, queryable source of group
information. LDAP-based group mapping or the Cloud Identity Engine (CIE) fills this role.
User-ID™ queries your directory service and builds a local user-to-group mapping table that
the firewall refreshes at a configurable interval. During policy evaluation, the firewall
checks this directory-built table, not the IdP assertion. 

 Defining policy rules based on group membership rather than on
individual users simplifies administration because you don't have
to update the rules whenever new users are added to a group. When
configuring group mapping, you can limit which groups will be available
in policy rules. You can specify groups that already exist in your
directory service or define custom groups based on LDAP filters.
Defining custom groups can be quicker than creating new groups or
changing existing ones on an LDAP server, and doesn't require an
LDAP administrator to intervene. User-ID maps all the LDAP directory
users who match the filter to the custom group. For example, you
might want a security policy that allows contractors in the Marketing Department
to access social networking sites. If no Active Directory group
exists for that department, you can configure an LDAP filter that
matches users for whom the LDAP attribute Department is set to Marketing.
Log queries and reports that are based on user groups will include
custom groups. 

 Previous 

 User-ID Concepts 

 Next 

 User Mapping 

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
