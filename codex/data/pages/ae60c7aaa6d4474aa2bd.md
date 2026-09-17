---
url: https://docs.paloaltonetworks.com/content/techdocs/en_US/pan-os/10-0/pan-os-panorama-api/pan-os-xml-api-use-cases/manage-certificates-api.html
fetched_at: 2026-09-16T11:04:42Z
source: palo-alto-main
---

# Manage Certificates (API) Clear

Updated on 

 Jul 23, 2022 

 Focus 

 Home 

 PAN-OS 

 PAN-OS® and Panorama™ API Usage Guide 

 PAN-OS XML API Use Cases 

 Manage Certificates (API) 

 Download PDF 

 PAN-OS® and Panorama™ API Usage Guide 

 Manage Certificates (API) 

 Table of Contents 

 Filter

 Version 

 10.0 (EoL) 

 11.1 & Later 

 10.2 

 10.1 

 10.0 (EoL) 

 Expand all | Collapse all 

 About the PAN-OS API 

 PAN-OS XML API Components 

 Structure of a PAN-OS XML API Request 

 API Authentication and Security 

 XML and XPath 

 XPath Node Selection 

 Get Started with the PAN-OS XML API 

 Enable API Access 

 Get Your API Key 

 Authenticate Your API Requests 

 Make Your First API Call 

 Explore the API 

 Use the API Browser 

 Use the CLI to Find XML API Syntax 

 Use the Web Interface to Find XML API Syntax 

 PAN-OS XML API Error Codes 

 PAN-OS XML API Use Cases 

 Upgrade a Firewall to the Latest PAN-OS Version (API) 

 Show and Manage GlobalProtect Users (API) 

 Query a Firewall from Panorama (API) 

 Upgrade PAN-OS on Multiple HA Firewalls through Panorama (API) 

 Automatically Check for and Install Content Updates (API) 

 Enforce Policy using External Dynamic Lists and AutoFocus Artifacts (API) 

 Configure SAML 2.0 Authentication (API) 

 Quarantine Compromised Devices (API) 

 Manage Certificates (API) 

 PAN-OS XML API Request Types 

 PAN-OS XML API Request Types and Actions 

 Request Types 

 Configuration Actions 

 Actions for Modifying a Configuration 

 Actions for Reading a Configuration 

 Asynchronous and Synchronous Requests to the PAN-OS XML API 

 Configuration (API) 

 Get Active Configuration 

 Use XPath to Get Active Configuration 

 Use XPath to Get ARP Information 

 Get Candidate Configuration 

 Set Configuration 

 Edit Configuration 

 Delete Configuration 

 Rename Configuration 

 Clone Configuration 

 Move Configuration 

 Override Configuration 

 Multi-Move or Multi-Clone Configuration 

 Multi-config Request (API) 

 View Configuration Node Values for XPath 

 Commit Configuration (API) 

 Commit 

 Commit-All 

 Run Operational Mode Commands (API) 

 Get Reports (API) 

 Dynamic Reports 

 Predefined Reports 

 Custom Reports 

 Export Files (API) 

 Export Packet Captures 

 Export Application PCAPS 

 Export Threat, Filter, and Data Filtering PCAPs 

 Export Certificates and Keys 

 Export Technical Support Data 

 Import Files (API) 

 Importing Basics 

 Import Files 

 Retrieve Logs (API) 

 API Log Retrieval Parameters 

 Example: Use the API to Retrieve Traffic Logs 

 Apply User-ID Mapping and Populate Dynamic Groups (API) 

 Get Version Info (API) 

 Get Started with the PAN-OS REST API 

 PAN-OS REST API 

 Access the PAN-OS REST API 

 Resource Methods and Query Parameters (REST API) 

 PAN-OS REST API Request and Response Structure 

 PAN-OS REST API Error Codes 

 Work With Objects (REST API) 

 Create a Security Policy Rule (REST API) 

 Work with Policy Rules on Panorama (REST API) 

 Create a Tag (REST API) 

 Configure a Security Zone (REST API) 

 Configure an SD-WAN Interface (REST API) 

 Create an SD-WAN Policy Pre Rule (REST API) 

 Configure an Ethernet Interface (REST API) 

 Update a Virtual Router (REST API) 

 Work With Decryption (APIs) 

 End-of-Life (EoL)

 Manage Certificates (API) 

 Manage certificates using the Palo Alto Networks XML
 API. 

 Using the XML API, you can automate the management
 workflow for certificates. You can programatically: 

 Generate
 self-signed certificates 

 Configure Certificate Authorities (CAs) to sign certificates 

 Set certificates as Trusted Root CAs, Forward Trust Certificates,
 and Forward Untrust Certificates 

 Renew and revoke certificates 

 Bulk import and export certificates 

 For more
 information about the use of certificates on Palo Alto Networks
 Firewalls, see:
 Keys and Certificates .

 Send
 a request to generate a self-signed certificate. 

 With the XML API, you can generate certificates, flag the
 certificates as self-signed, and set cryptographic and certificate
 attributes in a single request. 

 The following example creates
 a certificate named SSCert with an IP address of 10.1.1.1 using
 RSA as the cryptographic algorithm. This certificate is set as a
 self-signed certificate using the element
 <ca> set
 to
 yes :

 curl -X GET "<firewall>/api/?key<apikey>&type=op&cmd=<request><certificate><generate><algorithm><RSA><rsa-nbits>512</rsa-nbits></RSA></algorithm><certificate-name>SSCert</certificate-name><name>10.1.1.1</name><ca>yes</ca></generate></certificate></request>"

 Send a request to set the certificate you created above
 as a trusted root certificate and a forward trust certificate. 

 The following requests use the configuration command and
 the xpath of the certificate you generated to set the certificate
 as a forward trust certificate and as a trusted root certificate. 

 curl -X GET "<firewall>/api/?key=<apikey>&type=config&action=set&xpath=/config/shared/ssl-decrypt&element=<trusted-root-CA><member>SSCert</member></trusted-root-CA>" 

 curl -X GET "<firewall>/api/?key=<apikey>&type=config&action=set&xpath=/config/shared/ssl-decrypt&element=<forward-trust-certificate><rsa>SSCert</rsa></forward-trust-certificate>"` 

 Send a
 request to create a subordinate certificate using the self-signed
 certificate you generated. 

 The following request creates a subordinate of the SSCert
 that you can use to get more granular control in the chain of trust. 

 curl -X GET "<firewall>/api/?key=<apikey>&type=op&cmd=<request><certificate><generate><algorithm><RSA><rsa-nbits>512</rsa-nbits></RSA></algorithm><certificate-name>subordinate</certificate-name><name>subordinateip</name><digest>sha256</digest><signed-by>SSCert</signed-by></generate></certificate></request>"

 Send a request to export certificates locally so that
 you can install the certificates on your clients. 

 The following request downloads the self-signed certificate
 as SSCert.pem. 

 curl -o SSCert.pem "<firewall>/api/?key=<apikey>&type=op&cmd=<download><certificate><certificate-name>SSCert</certificate-name><format>pem</format></certificate></download>"

 Import the certificates to other firewalls. 

 The following request uploads the SSCert certificate to
 a firewall. 

 curl -F "file=@<path of the file>" "<firewall>/api/?key=<apikey>&type=import&category=certificate&certificate-name=SSCert&format=pem"

 Alternatively, to import both the certificate
 and private key to your firewalls at the same time, use the following
 command:

 curl -F "file=@<path of the file>" "<firewall>/api?key=<apikey>type=import&category=keypair&certificate-name=SSCert.pem.txt&format=pem&passphrase=
 secretphrase

 To import a certificate to a specific
 template and device on Panorama, use the following command:

 curl -F "file=@<path of the file>" "<firewall>/api/?key=<apikey>&type=import&category=certificate&certificate-name=SSCert&format=pem&target-tpl=template&target-tpl-vsys=vsys1" 

 Renew and revoke certificates. 

 The following request revokes the subordinate certificates. 

 curl - X GET "<firewall>/api/?key=<apikey>&type=op&cmd=<request><certificate><revoke><certificate-name>subordinate</certificate-name></revoke></request></certificate>"

 The following request renews the self-signed
 root certificate that you generated. 

 curl - X GET "<firewall>/api/?key=<apikey>&type=op&cmd=<request><certificate><renew><certificate-name>SSCert</certificate-name><days-till-expiry>365</days-till-expiry></renew></certificate></request>"

 Send a request to commit the changes. 

 curl - X GET "<firewall>/api/?type=commit&cmd=<commit></commit>&key=<apikey>"

 Previous 

 Quarantine Compromised Devices (API) 

 Next 

 PAN-OS XML API Request Types
