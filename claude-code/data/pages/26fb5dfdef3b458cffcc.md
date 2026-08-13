---
url: https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-mobile-users/mobile-users-globalprotect/globalprotect-pre-logon/globalprotect-pre-logon-panorama
fetched_at: 2026-08-13T17:25:07Z
source: palo-alto-main
---

# GlobalProtect Pre-Logon (Panorama) Clear

GlobalProtect Pre-Logon (Panorama) 

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

 GlobalProtect Pre-Logon (Panorama) 

 Updated on 

 Mon Aug 10 14:01:14 PDT 2026 

 Focus 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deutsch (German) 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Access Docs 

 Release Notes 

 Select a Document 

 6.2 Preferred and Innovation 

 6.1 Preferred and Innovation 

 6.0 Preferred and Innovation 

 5.2 Preferred and Innovation 

 5.1 Preferred and Innovation 

 5.0 Preferred and Innovation 

 4.2 Preferred 

 4.1 Preferred 

 4.0 Preferred 

 3.2 Preferred and Innovation 

 Activation & Onboarding 

 Administration 

 Select a Document 

 4.0 & Later 

 Prisma Access China 

 Integrations 

 Incidents & Alerts 

 New Features 

 Updated on 

 Mon Aug 10 14:01:14 PDT 2026 

 Focus 

 Home 

 Prisma Access 

 Prisma Access Administration 

 Prisma Access Mobile Users 

 Mobile Users: GlobalProtect 

 GlobalProtect Pre-Logon 

 GlobalProtect Pre-Logon (Panorama) 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deutsch (German) 

 Prisma Access 

 GlobalProtect Pre-Logon (Panorama) 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Access Docs 

 Release Notes 

 Select a Document 

 6.2 Preferred and Innovation 

 6.1 Preferred and Innovation 

 6.0 Preferred and Innovation 

 5.2 Preferred and Innovation 

 5.1 Preferred and Innovation 

 5.0 Preferred and Innovation 

 4.2 Preferred 

 4.1 Preferred 

 4.0 Preferred 

 3.2 Preferred and Innovation 

 Activation & Onboarding 

 Administration 

 Select a Document 

 4.0 & Later 

 Prisma Access China 

 Integrations 

 Incidents & Alerts 

 New Features 

 GlobalProtect Pre-Logon ( Panorama ) 

 Learn how to enable the pre-logon connect method for GlobalProtect mobile
 users. 

 Configure Pre-Logon Certificate and Profile 

 Configure a machine certificate as an authentication method to establish a tunnel
 from an endpoint before logging in to Prisma Access, and then create a
 certificate profile that includes the pre-logon CA certificate. 

 Configure a self-signed CA, and use it to generate a machine certificate in
 the Mobile User template. Go to Device Certificate Management Certificates . 

 Be sure that you're in the Mobile_User_Template and the
 Location is set to Shared . 

 Name the certificate; for example, Pre-logon CA Cert . 

 Enter a Common Name . 
 The Common Name (CN) is the domain name, such as
 www.yourdomainname.com, you want to secure with your
 certificate. 

 Leave the Signed By field blank, and click the
 Certificate Authority check box. 

 Generate the certificate for use in
 Pre-logon connections. 

 After you configure the self-signed CA, generate the machine certificate. 

 Enter a Certificate Name and a Common
 Name . 

 In the Signed By drop-down, select the Pre-logon
 CA Cert that you created in step 1. 

 Generate the Windows VM Machine
 Certificate that you later install on a Windows
 machine. 

 This certificate is a child of the Pre-logon CA. 

 To create a certificate profile that includes the pre-logon CA certificate,
 go to Device Certificate Management Certificate Profile . 
 Use this CA to validate the machine certificate presented by the
 GlobalProtect client during the pre-logon tunnel initialization. 

 Create and name the profile. Ensure that the Username
 Field is None to prevent the
 certificate mapping to a user. 

 Under CA Certificates , select Add and select
 Pre-logon CA Cert from the drop-down. 

 Select OK , and then select OK 
 again. 

 Configure the GlobalProtect Portal for Pre-Logon 

 Configure the GlobalProtect portal to authenticate connections with a machine
 certificate. 

 Go to Network GlobalProtect Portals GlobalProtect_Portal Authentication . 

 Under Allow Authentication with User Credentials OR Client
 Certificate , select No to enforce
 certificate-based authentication only. 

 For Certificate Profile , select the Pre-logon_Profile you
 created, and click OK . 

 Select Agent and open the Agent configuration for
 authenticated users. 

 Select the App tab. 

 Select Pre-logon (Always On) , and select
 OK to return to the Agent area. 

 In the Agent area, Clone the default configuration.
 Change the configuration name to Pre-logon to match
 the connect method for machine certificate authentication. 

 Select the newly cloned agent configuration. 

 Select Config Selection Criteria . Under the User/User Group 
 configuration, select pre-logon from the drop-down above the
 USER/USER Group configuration box, and ensure that the
 configuration is set to Any . 

 Configure the App settings as needed and select OK .
 Ensure that you select a pre-logon connect method for both the pre-logon and
 current configuration. 

 Move the pre-logon agent configuration to the top of the CONFIGS 
 list to ensure it matches first with the pre-logon condition. 

 Click OK to save the portal configuration. 

 Configure the Prisma Access GlobalProtect Gateways 

 Configure the GlobalProtect gateways in Panorama Managed Prisma
 Access. 

 This configuration enforces certificate-based authentication
 only. 

 Go to Network GlobalProtect Gateways GlobalProtect_External_Gateway Authentication . 

 Select the Default authentication method. 
 If you already have a client authentication (such as SAML) configured,
 select it instead of Default . 

 Under Allow Authentication with User Credentials or Client
 Certificate , select No , and then
 select OK to save the configuration. 

 Install a Machine Certificate—Windows 

 Install the machine certificate at the mobile users' endpoints, which are used
 for authentication. 

 Go to Device Certificate Management Certificates . 

 Be sure that you're still in the Mobile_User_Template. Select the
 Windows VM Machine Cert that you created
 previously, and select Export Certificate to download
 it as a PKCS12 file with a passphrase. 

 Export the pre-logon CA cert as a base64 encoded certificate. 

 Transfer the certificate files to a Windows machine. 

 Install the root pre-logon CA certificate in the Trusted Root
 Certification Authorities store of your local machine. 

 Install the pre-logon machine certificate in the local machine store
 location. Complete the permissions, and select Next 
 to proceed with the installation. 

 Validate the filename to the certificate, and select
 Next . 

 Enter the password, which is the passphrase you used during the certificate
 export from Panorama, and select Next . 

 In the Certificate Store dialog, select Place all
 certificates in the following store , and select
 Browse . 

 Select the Personal folder where you want to install
 the machine certificate, and select OK . 

 Select Next to proceed with installation. 

 Connect to the GlobalProtect portal, and delete all cookies from the
 host. 

 ( Optional ) Sign out of your machine and view the GlobalProtect
 logs to verify the pre-logon connection. 

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

 SASE 

 4.1 Preferred 

 5.1 Preferred and Innovation 

 5.0.1 Preferred and Innovation 

 Panorama 

 6.0 Preferred and Innovation 

 5.0 Preferred and Innovation 

 Administration 

 Prisma Access 

 GlobalProtect 

 Prisma Access 

 Prisma SASE 

 4.0 Preferred 

 Strata Cloud Manager 

 4.0 & Later 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
