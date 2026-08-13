---
url: https://docs.paloaltonetworks.com/ngfw/help/10-1/device/device-server-profiles-saml-identity-provider
fetched_at: 2026-08-13T16:41:20Z
source: palo-alto-main
---

# Device > Server Profiles > SAML Identity Provider Clear

Device > Server Profiles > SAML Identity Provider 

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

 Device > Server Profiles > SAML Identity Provider 

 Updated on 

 Mon Jan 12 14:16:08 PST 2026 

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

 Mon Jan 12 14:16:08 PST 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 Device 

 Device > Server Profiles > SAML Identity Provider 

 Download PDF 

 Next-Generation Firewall 

 Device > Server Profiles > SAML Identity Provider 

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

 Device > Server Profiles > Kerberos 

 Next 

 Device > Server Profiles > DNS 

 Device > Server Profiles > SAML Identity Provider 

 Use this page to register a Security Assertion Markup
Language (SAML) 2.0 identity provider (IdP) with the firewall or
Panorama. Registration is a necessary step to enable the firewall
or Panorama to function as a SAML service provider, which controls
access to your network resources. When administrators and end users
request resources, the service provider redirects the users to the
IdP for authentication. The end users can be GlobalProtect or Authentication
Portal users. The administrators can be managed locally on the firewall
and Panorama or managed externally in the IdP identity store. You
can configure SAML single sign-on (SSO) so that each user can automatically
access multiple resources after logging into one. You can also configure
SAML single logout (SLO) so that each user can simultaneously log
out of every SSO-enabled service by logging out of any single service. 

 Authentication sequences don’t support authentication profiles
that specify SAML IdP server profiles. 

 In most cases, you
cannot use SSO to access multiple apps on the same mobile device. 

 You
cannot enable SLO for Authentication Portal users. 

 The easiest way to create a SAML IdP server profile is to Import a
metadata file containing the registration information from the IdP.
After saving a server profile with imported values, you can edit
the profile to modify the values. If the IdP doesn’t provide a metadata
file, you can Add the server profile and manually
enter the information. After creating a server profile, assign it
to an authentication profile (see Device
> Authentication Profile ) for specific firewall or Panorama
services. 

 SAML Identity Provider
Server Settings 

 Description 

 Profile Name 

 Enter a name to identify the server (up
to 31 characters). The name is case-sensitive and must be unique.
Use only letters, numbers, spaces, hyphens, and underscores. 

 Location 

 Select the scope in which the profile is
available. In the context of a firewall that has multiple virtual
systems, select a virtual system or select Shared (all
virtual systems). In any other context, you can’t select the Location ; its
value is predefined as Shared ( firewalls ) or as Panorama. After
you save the profile, you can’t change its Location . 

 Administrator Use Only 

 Select this option to specify that only
administrator accounts can use the profile for authentication. For
firewalls that have multiple virtual systems, this option appears
only if the Location is Shared . 

 Identity Provider ID 

 Enter an identifier for the IdP. Your IdP
provides this information. 

 Identity Provider Certificate 

 Select the certificate that the IdP uses
to sign SAML messages that it sends to the firewall. You must select
an IdP certificate to ensure the integrity of messages that the
IdP sends to the firewall. To validate the IdP certificate against
the issuing Certificate Authority (CA), you must specify a Certificate
Profile in any authentication profile that references
the IdP server profile (see Device
> Authentication Profile ). 

 When generating or importing
a certificate and its associated private key, remember that the
key usage attributes specified in the certificate control what you
can use the key for. If the certificate explicitly lists key usage
attributes, one of the attributes must be Digital Signature, which
is not available in certificates that you generate on the firewall.
In this case, you must Import the
certificate and key from your enterprise certificate authority (CA)
or a third-party CA. If the certificate doesn’t specify key usage
attributes, you can use the key for any purpose, including signing
messages. In this case, you can use any method to obtain the certificate and key 

 for
signing SAML messages. 

 IdP certificates support the following
algorithms: 

 Public key algorithms —RSA (1,024 bits
or larger) and ECDSA (all sizes). A firewall in FIPS/CC mode supports
RSA (2,048 bits or larger) and ECDSA (all sizes). 

 Signature algorithms — SHA1, SHA256, SHA384, and SHA512.
A firewall in FIPS/CC mode supports SHA256, SHA384, and SHA512. 

 Identity Provider SSO URL 

 Enter the URL that the IdP advertises for
its single-sign on (SSO) service. 

 If you create the server
profile by importing a metadata file and the file specifies multiple
SSO URLs, the firewall uses the first URL that specifies a POST
or redirect binding method. 

 Palo Alto
Networks strongly recommends using a URL that relies on HTTPS, although
SAML also supports HTTP. 

 Identity Provider SLO URL 

 Enter the URL that the IdP advertises for
its single logout (SLO) service. 

 If you create the server
profile by importing a metadata file and the file specifies multiple
SLO URLs, the firewall uses the first URL that specifies a POST
or redirect binding method. 

 Palo Alto
Networks strongly recommends using a URL that relies on HTTPS, although
SAML also supports HTTP. 

 SSO SAML HTTP Binding 

 Select the HTTP binding associated with
the Identity Provider SSO URL . The firewall
uses the binding to send SAML messages to the IdP. The options are: 

 POST —The firewall sends messages using
base64-encoded HTML forms. 

 Redirect —The firewall sends base64-encoded
and URL-encoded SSO messages within URL parameters. 

 If
you import an IdP metadata file that has multiple SSO URLs, the
firewall uses the binding of the first URL that uses the POST or
redirect method. The firewall ignores URLs that use other bindings. 

 SLO SAML HTTP Binding 

 Select the HTTP binding associated with
the Identity Provider SLO URL . The firewall
uses the binding to send SAML messages to the IdP. The options are: 

 POST —The firewall sends messages using
base64-encoded HTML forms. 

 Redirect —The firewall sends base64-encoded
and URL-encoded SSO messages within URL parameters. 

 If
you import an IdP metadata file that has multiple SLO URLs, the
firewall uses the binding of the first URL that uses the POST or
redirect method. The firewall ignores URLs that use other bindings. 

 Identity Provider Metadata 

 This field displays only if you Import an IdP
metadata file that you uploaded to the firewall from the IdP. The
file specifies the values and signing certificate for a new SAML
IdP server profile. Browse to the file, specify
the Profile
Name and Maximum
Clock Skew , and then click OK to create
the profile. Optionally, you can edit the profile to change the
imported values. 

 Validate Identity Provider Certificate 

 Select this option to validate the chain
of trust and optionally the revocation status of the IdP signing
certificate. 

 To enable this option, a Certificate Authority
(CA) must issue your IdP’s signing certificate. You must create
a Certificate Profile that has the CA that issued the IdP’s signing
certificate. In the Authentication Profile, select the SAML Server
profile and Certificate Profile to validate the IdP certificate
(see Device
> Authentication Profile ). 

 If your IdP signing certificate
is a self-signed certificate, there is no chain of trust; as a result,
you cannot enable this option. The firewall always validates the
signature of the SAML Responses or Assertions against the Identity
Provider certificate that you configure whether or not you enable
the Validate Identity Provider Certificate option.
If your IdP provides a self-signed certificate, ensure that you
are using PAN-OS 10.1 to mitigate exposure to CVE-2020-2021 . 

 Sign SAML Message to IdP 

 Select this option to specify that the firewall
sign messages it sends to the IdP. The firewall uses the Certificate
for Signing Requests that you specify in an authentication profile
(see Device
> Authentication Profile ). 

 Using
a signing certificate ensures the integrity of messages sent to
the IdP. 

 Maximum Clock Skew 

 Enter the maximum acceptable time difference
in seconds between the IdP and firewall system times at the moment
when the firewall validates a message that it receives from the
IdP (range is 1 to 900; default is 60). If the time difference exceeds
this value, the validation (and thus authentication) fails. 

 Previous 

 Device > Server Profiles > Kerberos 

 Next 

 Device > Server Profiles > DNS 

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

 10.1 

 PAN-OS 

 Next-Generation Firewall 

 Help 

 Web Interface 

 Panorama 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
