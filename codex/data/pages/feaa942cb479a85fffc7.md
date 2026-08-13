---
url: https://docs.paloaltonetworks.com/pan-os/10-1/pan-os-admin/certificate-management/export-a-certificate-and-private-key
fetched_at: 2026-08-13T16:59:13Z
source: palo-alto-main
---

# Export a Certificate and Private Key Clear

Export a Certificate and Private Key 

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

 Export a Certificate and Private Key 

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

 Certificate Management 

 Export a Certificate and Private Key 

 Download PDF 

 Next-Generation Firewall 

 Export a Certificate and Private Key 

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

 Deploy Certificates Using SCEP 

 Next 

 Blocking Private Key Export 

 Export a Certificate and Private Key 

 You can export certificates and keys directly from the firewall or Panorama for
 various applications. 

 Palo Alto Networks recommends that you use your enterprise public key
 infrastructure (PKI) to distribute a certificate and private key in your
 organization. However, if necessary, you can also export a certificate and private
 key from the firewall or Panorama. You can use an exported certificate and private
 key in the following cases: 

 Configure
 Certificate-Based Administrator Authentication to the Web
 Interface 

 Enable SSL
 Between GlobalProtect LSVPN Components to configure GlobalProtect
 agent/app authentication to portals and gateways 

 SSL Forward Proxy 
 decryption 

 Obtain a
 Certificate from an External CA 

 Select Device Certificate Management Certificates , then Device Certificates ( PAN-OS 11.2 and
 earlier ) or
 Custom Certificates ( PAN-OS 12.1.0 and
 later ) . 

 If the firewall has more than one virtual system (vsys), select a
 Location (a specific vsys or
 Shared ) for the certificate. 

 Select the certificate, click Export , and select a
 File Format : 

 Base64 Encoded Certificate (PEM) —This is the
 default format. It is the most common and has the broadest support
 on the Internet. If you want the exported file to include the
 private key, select the Export Private Key 
 check box. 

 Encrypted Private Key and Certificate
 (PKCS12) —This format is more secure than PEM but is not
 as common or as broadly supported. The exported file will
 automatically include the private key. 

 Binary Encoded Certificate (DER) —More
 operating system types support this format than the others. You can
 export only the certificate, not the key: ignore the
 Export Private Key check box and
 passphrase fields. 

 Enter a Passphrase and Confirm
 Passphrase to encrypt the private key if the File
 Format is PKCS12 or if it is PEM and you selected the
 Export Private Key check box. You will use this
 passphrase when importing the certificate and key into client systems. 

 ( Panorama managed firewalls ) If you
 enabled Block Private Key Export when you generated or imported the certificate,
 you must be sure to Import Private Key and add the
 key File when you import the exported
 certificate. This is required to successfully push configuration changes
 from Panorama to managed firewalls that you imported the certificate to.

 Click OK and save the certificate/key file to your
 computer. 

 Previous 

 Deploy Certificates Using SCEP 

 Next 

 Blocking Private Key Export 

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

 Certificate Management 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
