---
url: https://docs.paloaltonetworks.com/pan-os/10-1/pan-os-admin/firewall-administration/manage-firewall-administrators/administrative-authentication
fetched_at: 2026-09-16T07:34:14Z
source: palo-alto-main
---

# Administrative Authentication Clear

Updated on 

 Mon Aug 31 04:46:16 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 Firewall Administration 

 Manage Firewall Administrators 

 Administrative Authentication 

 Download PDF 

 Next-Generation Firewall 

 Administrative Authentication 

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

 Example Admin Role Profile Construction 

 Next 

 Configure Administrative Accounts and Authentication 

 Administrative Authentication 

 Configure authentication methods for PAN-OS firewall administrators including local
 accounts, external authentication servers, and multi-factor authentication
 options. 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by PAN-OS or Panorama) 

 No prerequisites needed 

 You can configure the following types of authentication
and authorization (role and access domain assignment) for firewall
administrators: 

 Authentication Method 

 Authorization Method 

 Description 

 Local 

 Local 

 The administrative account credentials and
authentication mechanisms are local to the firewall. You can define
the accounts with or without a user database that is local to the firewall—see Local
Authentication for the advantages and disadvantages of using
a local database. You use the firewall to manage role assignments
but access domains are not supported. For details, see Configure
Local or External Authentication for Firewall Administrators . 

 SSH Keys 

 Local 

 The administrative accounts are local to
the firewall, but authentication to the CLI is based on SSH keys.
You use the firewall to manage role assignments but access domains
are not supported. For details, see Configure
SSH Key-Based Administrator Authentication to the CLI . 

 Certificates 

 Local 

 The administrative accounts are local to
the firewall, but authentication to the web interface is based on
client certificates. You use the firewall to manage role assignments
but access domains are not supported. For details, see Configure
Certificate-Based Administrator Authentication to the Web Interface . 

 External service 

 Local 

 The administrative accounts you define locally
on the firewall serve as references to the accounts defined on an
external Multi-Factor
Authentication , SAML , Kerberos , TACACS+ , RADIUS ,
or LDAP server.
The external server performs authentication. You use the firewall
to manage role assignments but access domains are not supported.
For details, see Configure
Local or External Authentication for Firewall Administrators . 

 External service 

 External service 

 The administrative accounts are defined
on an external SAML , TACACS+ ,
or RADIUS server.
The server performs both authentication and authorization. For authorization,
you define Vendor-Specific Attributes (VSAs) on the TACACS+ or RADIUS
server, or SAML attributes on the SAML server. PAN-OS maps the attributes
to administrator roles, access domains, user groups, and virtual
systems that you define on the firewall. For details, see: 

 Configure
SAML Authentication 

 Configure
TACACS+ Authentication 

 Configure
RADIUS Authentication 

 Previous 

 Example Admin Role Profile Construction 

 Next 

 Configure Administrative Accounts and Authentication
