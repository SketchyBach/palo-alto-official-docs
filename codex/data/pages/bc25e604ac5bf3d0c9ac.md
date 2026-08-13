---
url: https://docs.paloaltonetworks.com/panorama/administration/manage-log-collection/configure-authentication-for-a-dedicated-log-collector/configure-ldap-authentication-for-a-dedicated-log-collector
fetched_at: 2026-08-13T17:17:52Z
source: palo-alto-main
---

# Configure LDAP Authentication for a Dedicated Log Collector Clear

Configure LDAP Authentication for a Dedicated Log Collector 

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

 Configure LDAP Authentication for a Dedicated Log Collector 

 Updated on 

 Thu Jul 30 16:22:01 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Panorama Docs 

 Getting Started 

 Administration 

 New Features 

 Updated on 

 Thu Jul 30 16:22:01 PDT 2026 

 Focus 

 Home 

 Panorama 

 Manage Log Collection 

 Configure Authentication for a Dedicated Log Collector 

 Configure LDAP Authentication for a Dedicated Log Collector 

 Download PDF 

 Panorama 

 Configure LDAP Authentication for a Dedicated Log Collector 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Panorama Docs 

 Getting Started 

 Administration 

 New Features 

 Configure LDAP Authentication for a Dedicated Log Collector 

 Configure LDAP authentication for a Dedicated Log Collector. 

 You can use LDAP to authenticate end
users who access Dedicated Log Collector web interface. 

 Log in to the Panorama web
 interface . 

 Configure a Managed Collector . 

 Add an
LDAP server profile. 

 The profile defines how the Dedicated Log Collector connects
to the LDAP server. 

 Only Superuser administrators are
 supported when configuring an administrative account for a Dedicated Log
 Collector. Local or Panorama Administrators with any other admin role
 type is not supported. 

 Select Panorama Server Profiles LDAP and Add a
server profile. 

 Enter a Profile Name to identify
the server profile. 

 Add the LDAP servers (up to
four). For each server, enter a Name (to
identify the server), LDAP Server IP address
or FQDN, and server Port (default 389). 

 If you use an FQDN address object to identify the
server and you subsequently change the address, you must commit
the change for the new server address to take effect. 

 Select the server Type . 

 Select the Base DN . 
 To identify the Base DN of your directory, open the Active
Directory Domains and Trusts Microsoft Management Console
snap-in and use the name of the top-level domain. 

 Enter the Bind DN and Password to
enable the authentication service to authenticate the firewall. 

 The Bind DN account must have permission to read the
LDAP directory. 

 Enter the Bind Timeout and Search
Timeout in seconds (default is 30 for both). 

 Enter the Retry Interval in
seconds (default is 60). 

 ( Optional ) If you want the endpoint to use
SSL or TLS for a more secure connection with the directory server,
enable the option to Require SSL/TLS secured connection (enabled
by default). The protocol that the endpoint uses depends on the
server port: 

 389 (default)—TLS (Specifically, the Dedicated
Log Collector uses the StartTLS operation , which
upgrades the initial plaintext connection to TLS.) 

 636—SSL 

 Any other port—The Dedicated Log Collector first attempts
to use TLS. If the directory server doesn’t support TLS, the Dedicated
Log Collector falls back to SSL. 

 ( Optional ) For additional security, enable
to the option to Verify Server Certificate for SSL sessions so
that the endpoint verifies the certificate that the directory server
presents for SSL/TLS connections. To enable verification, you must also
enable the option to Require SSL/TLS secured connection .
For verification to succeed, the certificate must meet one of the
following conditions: 

 It is in the list of Panorama certificates: Panorama Certificate Management Certificates Device Certificates. If
necessary, import the certificate into Panorama. 

 The certificate signer is in the list of trusted certificate
authorities: Panorama Certificate
Management Certificates . 

 Click OK to save the server
profile. 

 Configure the authentication for the Dedicated Log Collector. 

 Select Panorama Managed Collectors and select
the Dedicated Log Collector you previously added. 

 Configure the authentication Timeout Configuration for
the Dedicated Log Collector. 

 Enter the number of Failed Attempt s
before a user is locked out of the Dedicated Log Collector CLI. 

 Enter the Lockout Time , in minutes,
for which the Dedicated Log Collector locks out a user account after
that user reaches the configured number of Failed Attempts . 

 Enter the Idle Timeout , in minutes,
before the user account is automatically logged out due to inactivity. 

 Enter the Max Session Count to set
how many user accounts can simultaneously access the Dedicated Log
Collector. 

 Enter the Max Session Time the administrator
can be logged in before being automatically logged out. 

 Add the Dedicated Log Collector administrators. 

 Administrators may either be added as a local administrator
or as an imported Panorama administrator—but not both. Adding the
same administrator as both a local administrator and as an imported
Panorama administrator is not supported and causes the Panorama
commit to fail. For example, the commit to Panorama fails if you
add admin1 as both a local and Panorama administrator. 

 Configure the local administrators. 

 Configure
new administrators unique to the Dedicated Log Collector. These administrators
are specific to the Dedicated Log Collector for which they are created
and you manage these administrators from this table. 

 Add one
or more new local administrator. 

 Enter a Name for the local administrator. 

 Assign an Authentication Profile you
previously created. 

 LDAP authentication profiles are
supported only for individual local administrators. 

 Enable (check) Use Public Key Authentication (SSH) to
import a public key file for authentication. 

 Select a Password Profile to set the
expiration parameters. 

 Import existing Panorama administrators 

 Import existing
administrators configured on Panorama. These administrators are
configured and managed on Panorama and imported to Dedicated Log
Collector. 

 Add an
existing Panorama administrator 

 Click OK to save the Dedicated
Log Collector authentication configuration. 

 Configure the authentication for the Dedicated Log Collector. 

 Select Panorama Managed Collectors and select
the Dedicated Log Collector you previously added. 

 Select the Authentication Profile you
configured in the previous step. 

 Configure the authentication Timeout Configuration for
the Dedicated Log Collector. 

 Enter the number of Failed Attempt s
before a user is locked out of the Dedicated Log Collector CLI. 

 Enter the Lockout Time , in minutes,
for which the Dedicated Log Collector locks out a user account after
that user reaches the configured number of Failed Attempts . 

 Enter the Idle Timeout , in minutes,
before the user account is automatically logged out due to inactivity. 

 Enter the Max Session Count to set
how many user accounts can simultaneously access the Dedicated Log
Collector. 

 Enter the Max Session Time the administrator
can be logged in before being automatically logged out. 

 Add the Dedicated Log Collector administrators. 

 You must add the administrator ( admin )
as either a local administrator or as an imported Panorama administrator—but
not both. The push to managed collectors fails if an administrator
is not added or if the administrator is added as both a local administrator
and as an imported Panorama administrator. 

 Add and
configure new administrators unique to the Dedicated Log Collector. These
administrators are specific to the Dedicated Log Collector for which they
are created and you manage these administrators from this table. 

 Add any administrators configured on
Panorama. These administrators are created on Panorama and imported
to the Dedicated Log Collector. 

 Click OK to save the Dedicated
Log Collector authentication configuration. 

 Commit and then Commit
and Push your configuration changes. 

 Log in to the Panorama CLI of the
 Dedicated Log Collector to verify you can successfully access the Dedicated Log
 Collector using the local admin user. 

 On This Page 

 Activation and Onboarding 

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

 Panorama 

 Service Provider 

 VM-Series 

 Plugins 

 SASE 

 Prisma Access 

 Prisma SASE Multitenant Platform 

 AI-Powered ADEM 

 Prisma Access Monitoring & Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

 Cloud-Delivered Security Services 

 Advanced WildFire 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 AI Access Security 

 Device Security 

 Enterprise DLP 

 SaaS Security 

 Network Security 

 Shared Policy for NGFWs and Prisma Access 

 IPSec VPN 

 Security Policy 

 Quantum Security 

 Endpoints 

 GlobalProtect 

 Remote Browser Isolation 

 Prisma Access Agent 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 FedRAMP 

 Prisma SASE for FedRAMP 

 Autonomous DEM for FedRAMP 

 Prisma SD-WAN Experts Corner 

 Network Policy 

 QoS Whitepaper 

 Security Architecture Whitepaper 

 External Antennas for ION-C Series 

 Dynamic Path Selection 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Resources 

 All Products A - Z 

 All Release Notes 

 Compatibility Matrix 

 Experts Corner 

 Network Security Platform 

 Security Policy 

 Decryption 

 Device-ID 

 IPSec VPN 

 Quality of Service 

 Quantum Security 

 11.1 & Later 

 Next-Generation Firewall 

 Administration 

 Panorama 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
