---
url: https://docs.paloaltonetworks.com/ngfw/help/11-2/device/device-authentication-profile/export-saml-metadata-from-an-authentication-profile
fetched_at: 2026-08-13T16:47:10Z
source: palo-alto-main
---

# SAML Metadata Export from an Authentication Profile Clear

SAML Metadata Export from an Authentication Profile 

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

 SAML Metadata Export from an Authentication Profile 

 Updated on 

 Thu Jun 25 17:41:47 PDT 2026 

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

 Thu Jun 25 17:41:47 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 Device 

 Device > Authentication Profile 

 SAML Metadata Export from an Authentication Profile 

 Download PDF 

 Next-Generation Firewall 

 SAML Metadata Export from an Authentication Profile 

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

 Authentication Profile 

 Next 

 Device > Authentication Sequence 

 SAML Metadata Export from an Authentication Profile 

 Device > Authentication Profile 

 The firewall and Panorama can use a SAML identity provider (IdP) to authenticate
users who request services. For administrators, the service
can be access to the web interface. For end users, the service can
be Authentication Portal or GlobalProtect, which enable access to
your network resources. To enable SAML authentication for a service,
you must register that service by entering specific information
about it on the IdP in the form of SAML metadata. The firewall and
Panorama simplify registration by automatically generating a SAML
metadata file based on the authentication profile that you assigned
to the service and you can export this metadata file to the IdP.
Exporting the metadata is an easier alternative to typing the values
for each metadata field in the IdP. 

 Some of the metadata in the exported file derives from
the SAML IdP server profile assigned to the authentication profile
( Device
> Server Profiles > SAML Identity Provider ). However, the
exported file always specifies POST as the HTTP binding method,
regardless of the method specified in the SAML IdP server profile. The
IdP will use the POST method to send SAML messages to the firewall
or Panorama. 

 To export SAML metadata from an authentication profile, click
the SAML Metadata link in the Authentication
column and complete the following fields. To import the metadata
file into an IdP, refer to your IdP documentation. 

 SAML Metadata Export Settings 

 Description 

 Commands 

 Select the service for which you want to
export SAML metadata: 

 management (default)—Provides
administrator access to the web interface. 

 authentication-portal —Provides end
user access to network resources through Authentication Portal. 

 global-protect —Provides end user access
to network resources through GlobalProtect. 

 Your
selection determines which other fields the dialog displays. 

 [Management | Authentication Portal | GlobalProtect]
Auth Profile 

 Enter the name of the authentication profile
from which you are exporting metadata. The default value is the
profile from which you opened the dialog by clicking the Metadata link. 

 Management Choice 

 ( Management
only ) 

 Select an option for specifying an interface
that is enabled for management traffic (such as the MGT interface): 

 Interface —Select the interface from
the list of interfaces on the firewall. 

 IP Hostname —Enter the IP address or
hostname of the interface. If you enter a hostname, the DNS server
must have an address (A) record that maps to the IP address. 

 [Authentication Portal | GlobalProtect] Virtual
System 

 ( Authentication Portal or GlobalProtect only ) 

 Select the virtual system for which the
Authentication Portal settings or GlobalProtect portal are defined. 

 IP Hostname 

 ( Authentication Portal
or GlobalProtect only ) 

 Enter the IP address or hostname of the
service. 

 Authentication Portal —Enter the Redirect
Host IP address or hostname ( Device User Identification Authentication Portal
Settings ). 

 GlobalProtect —Enter the Hostname or IP
Address of the GlobalProtect portal. 

 If
you enter a hostname, the DNS server must have an address (A) record
that maps to the IP address. 

 Previous 

 Authentication Profile 

 Next 

 Device > Authentication Sequence 

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

 11.2 

 Help 

 Panorama 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
