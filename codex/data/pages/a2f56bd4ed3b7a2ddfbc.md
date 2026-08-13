---
url: https://docs.paloaltonetworks.com/globalprotect/administration/globalprotect-user-authentication/set-up-client-certificate-authentication/deploy-user-specific-client-certificates-for-authentication
fetched_at: 2026-08-13T16:32:52Z
source: palo-alto-main
---

# Deploy User-Specific Client Certificates for Authentication Clear

Deploy User-Specific Client Certificates for Authentication 

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

 Deploy User-Specific Client Certificates for Authentication 

 Updated on 

 Jul 8, 2026 

 Focus 

 Download PDF 

 English 

 日本語 (Japanese) 

 Filter

 Expand All 
 | 
 Collapse All 

 GlobalProtect Docs 

 Getting Started 

 Activation & Onboarding 

 Administration 

 User Guide 

 Select a Document 

 6.3 

 6.2 

 6.1 

 6.0 

 Release Notes 

 Select a Document 

 6.3 

 6.2 

 6.1 

 6.0 

 New Features 

 Updated on 

 Jul 8, 2026 

 Focus 

 Home 

 GlobalProtect 

 GlobalProtect Administrator's Guide 

 GlobalProtect User Authentication 

 Set Up Client Certificate Authentication 

 Deploy User-Specific Client Certificates for Authentication 

 Download PDF 

 English 

 日本語 (Japanese) 

 GlobalProtect 

 Deploy User-Specific Client Certificates for Authentication 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 GlobalProtect Docs 

 Getting Started 

 Activation & Onboarding 

 Administration 

 User Guide 

 Select a Document 

 6.3 

 6.2 

 6.1 

 6.0 

 Release Notes 

 Select a Document 

 6.3 

 6.2 

 6.1 

 6.0 

 New Features 

 Previous 

 Deploy Machine Certificates for Authentication-SCM 

 Next 

 Enable Certificate Selection Based on OID 

 Deploy User-Specific Client Certificates for Authentication 

 To enable individual user authentication with GlobalProtect, issue and deploy unique
 client certificates to endpoints. You can automate this by configuring the GlobalProtect
 portal as a Simple Certificate Enrollment Protocol (SCEP) client to a SCEP server in the
 enterprise PKI. Two-factor authentication can also be set up using the SCEP profile. 

 Where Can I Use This? What Do I Need? 

 NGFW (managed by Panorama or Strata Cloud Manager) 

 Prisma Access (managed by Panorama or Strata Cloud
 Manager) 

 GlobalProtect Gateway license or Prisma Access license with
 the Mobile User subscription 

 To authenticate individual users, you must
issue a unique client certificate to each GlobalProtect user and
deploy the client certificate to the endpoints prior to enabling
GlobalProtect. To automate the generation and deployment of user-specific
client certificates, you can configure your GlobalProtect portal to
act as a Simple Certificate Enrollment Protocol (SCEP) client to
a SCEP server in your enterprise PKI. 

 If you include
a client certificate in the portal configuration for mobile devices,
you can only use client certificate authentication in the gateway configuration
because the client certificate passphrase is saved in the portal
configuration. Additionally, the client certificate can only be
used after the certificate is retrieved from the portal configuration. 

 SCEP
operation is dynamic in that the enterprise PKI generates a user-specific certificate
when the portal requests it and sends the certificate to the portal.
The portal then deploys the certificate to the app transparently.
When a user requests access, the app can then present the client
certificate to authenticate with the portal or gateway. 

 The
GlobalProtect portal or gateway uses identifying information about
the endpoint and the user to evaluate whether to permit access to
the user. GlobalProtect blocks access if the host ID is on a device
block list or if the session matches any blocking options specified
in a certificate profile. If authentication fails due to an invalid
SCEP-based client certificate, the GlobalProtect app tries to authenticate
with the portal (based on the settings in the authentication profile)
and retrieve the certificate. If the app cannot retrieve the certificate
from the portal, the endpoint is not able to connect. 

 Create a SCEP profile. 

 Do one of the following: 

 On Panorama, select Device Certificate Management SCEP , and then Add a new SCEP
 profile 

 On Strata Cloud Manager, select Manage Configuration NGFW and Prisma Access Objects Certificate Management , and then click Add
 SCEP . 

 . 

 Enter a Name to identify the
SCEP profile. 

 If this profile is for a firewall with multiple virtual
systems capability, select a virtual system or Shared as
the Location where the profile is available. 

 ( Optional ) To make the SCEP-based certificate
generation more secure, configure a SCEP challenge-response mechanism
between the PKI and portal for each certificate request. 

 After you configure this mechanism, its operation is invisible,
and no further input is necessary. 

 To comply with the U.S.
Federal Information Processing Standard (FIPS), use a Dynamic SCEP
Challenge and specify a Server URL that
uses HTTPS (see step 7). 

 Select one of the following SCEP
Challenge options: 

 None —( Default )
The SCEP server does not challenge the portal before it issues a
certificate. 

 Fixed —Enter the enrollment challenge Password obtained
from the SCEP server in the PKI infrastructure. 

 Dynamic —Enter a Username and Password of
your choice (possibly the credentials of the PKI administrator)
and the SCEP Server URL where the portal-client
submits these credentials. The credentials are used to authenticate
with the SCEP server, which transparently generates an OTP password
for the portal upon each certificate request (you can see this OTP
change after a screen refresh in The enrollment challengepassword is field
after each certificate request). The PKI transparently passes each
new password to the portal, which then uses the password for its
certificate request. 

 Specify the connection settings between the SCEP server
and the portal to enable the portal to request and receive client
certificates. 

 You can include additional information about the endpoint
or user by specifying tokens in the Subject name
of the certificate. 

 In the Subject field
of the CSR to the SCEP server, the portal includes the token value
as CN and Host-ID as SerialNumber .
The host ID varies by endpoint type: GUID (Windows), MAC address
of the interface (macOS), Android ID (Android endpoints), UDID (iOS
endpoints), or a unique name that GlobalProtect assigns (Chrome). 

 In the Configuration area, enter
the Server URL that the portal uses to reach
the SCEP server in the PKI (for example, http://10.200.101.1/certsrv/mscep/ ). 

 Enter a CA-IDENT Name (up to
255 characters in length) to identify the SCEP server. 

 Enter the Subject name to use
in the certificates generated by the SCEP server. The subject must
be a distinguished name in the < attribute >=< value > format
and must include a common name (CN) attribute ( CN=< variable > ).
The CN supports the following dynamic tokens: 

 $USERNAME —Use this token
to enable the portal to request certificates for a specific user.
To use this variable, you must also Enable
Group Mapping . The username entered by the user must match
the name in the user-group mapping table. 

 $EMAILADDRESS —Use this token
to request certificates associated with a specific email address.
To use this variable, you must also Enable
Group Mapping and configure the Mail Attributes in
the Mail Domains area of the server profile.
If GlobalProtect cannot identify an email address for the user,
it generates a unique ID and populates the CN with that value. 

 $HOSTID —To request certificates for
the endpoint only, specify the host ID token. When a user attempts
to log in to the portal, the endpoint sends identifying information
that includes its host ID value. 

 When the GlobalProtect
portal pushes the SCEP settings to the app, the CN portion of the
subject name is replaced with the actual value (username, host ID, or
email address) of the certificate owner (for example, O=acme,CN=johndoe ). 

 Select the Subject Alternative Name Type : 

 RFC 822 Name —Enter the email
name in a certificate’s subject or Subject Alternative Name extension. 

 DNS Name —Enter the DNS name used to evaluate
certificates. 

 Uniform Resource Identifier —Enter
the name of the resource from which the app will obtain the certificate. 

 None —Do not specify attributes for
the certificate. 

 ( Optional ) Configure Cryptographic Settings for
the certificate. 

 Select the Number of Bits (key length)
for the certificate. 

 If the firewall is in FIPS-CC mode and
the key generation algorithm is RSA. The RSA keys must be 2,048
bits or larger. 

 Select the Digest for CSR which indicates
the digest algorithm for the certificate signing request (CSR):
sha1, sha256, sha384, or sha512. 

 ( Optional ) Configure the permitted uses of the
certificate, either for signing or encryption. 

 To use this certificate for signing, select the Use
as digital signature check box. This option enables
the endpoint to use the private key in the certificate to validate
a digital signature. 

 To use this certificate for encryption, select the Use
for key encipherment check box. This option enables
the app to use the private key in the certificate to encrypt data
exchanged over the HTTPS connection established with the certificates
issued by the SCEP server. 

 ( Optional ) To ensure that the portal is connecting
to the correct SCEP server, enter the CA Certificate
Fingerprint . Obtain this fingerprint from the Thumbprint field
of the SCEP server interface. 

 Enter the URL for the SCEP server’s administrative UI
(for example, http://<hostname or IP>/CertSrv/mscep_admin/ ). 

 Copy the thumbprint and enter it in the CA
Certificate Fingerprint field. 

 Enable
mutual SSL authentication between the SCEP server and the GlobalProtect
portal. This is required to comply with the U.S. Federal Information
Processing Standard (FIPS). 

 FIPS-CC operation is indicated on the
firewall login page and its status bar. 

 Select the
SCEP server’s root CA Certificate . Optionally, you
can enable mutual SSL authentication between the SCEP server and
the GlobalProtect portal by selecting a Client Certificate . 

 Save and commit the configuration. 

 Click OK to save
the settings. 

 Commit the configuration. 

 The portal attempts to request a CA certificate using the
settings in the SCEP profile, and then saves it to the firewall
hosting the portal. If successful, the CA certificate is shown in Device Certificate Management Certificates . 

 ( Optional ) If the portal fails to obtain the
certificate after saving the SCEP profile, you can manually generate
a certificate signing request (CSR) from the portal. 

 Select Device Certificate Management Certificates Device Certificates , and then Generate a
new certificate. 

 Select SCEP as the Certificate
Type . 

 Enter a Certificate Name . This
name cannot contain spaces. 

 Select the SCEP Profile to
use to submit a CSR to your enterprise PKI. 

 Click OK to submit the request
and generate the certificate. 

 Set
Up Two-Factor Authentication . 

 Assign the SCEP profile a GlobalProtect portal agent configuration
to enable the portal to transparently request and deploy client
certificates to apps that receive the configuration. 

 Previous 

 Deploy Machine Certificates for Authentication-SCM 

 Next 

 Enable Certificate Selection Based on OID 

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

 Hardware Reference 

 ION 1000 

 ION 1200 

 ION 1200-S 

 ION 2000 

 ION 3000 

 ION 3200 

 ION 5200 

 ION 7000 

 ION 9000 

 ION 9200 

 Hardware Quick Start Guides 

 ION 1200 

 ION 1200 4G 

 ION 1200 5G 

 ION 1200-S 

 ION 1200-S 4G 

 ION 1200-S 5G 

 ION 3200 

 ION 5200 

 ION 9200 

 Virtual ION Deployment 

 Virtual ION on AWS 

 Virtual ION on Azure 

 Virtual ION on GCP 

 Virtual ION on KVM for NFV 

 Virtual ION on OCI 

 Virtual ION on VMware 

 3rd Party Integrations 

 AWS Cloud-WAN Integration (GRE Connect) 

 AWS Cloud-WAN Integration (Tunnel-less Connect) 

 Checkpoint Integration 

 LiveAction Integration 

 Netskope Integration 

 Symantec Web Security Services Integration 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 GlobalProtect Administration 

 Network Security 

 10.1 & Later 

 Administration 

 GlobalProtect 

 English 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
