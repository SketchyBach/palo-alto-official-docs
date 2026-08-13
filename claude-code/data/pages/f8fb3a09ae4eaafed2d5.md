---
url: https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-advanced-deployments/mobile-user-globalprotect-advanced-deployments/configure-multiple-portals-in-prisma-access
fetched_at: 2026-08-13T17:24:35Z
source: palo-alto-main
---

# Configure Multiple Portals in Prisma Access Clear

Configure Multiple Portals in Prisma Access 

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

 Configure Multiple Portals in Prisma Access 

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

 Prisma Access Advanced Deployments 

 Prisma Access Mobile Users—GlobalProtect Advanced Deployments 

 Configure Multiple Portals in Prisma Access 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deutsch (German) 

 Prisma Access 

 Configure Multiple Portals in Prisma Access 

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

 Previous 

 Prisma Access Mobile Users—GlobalProtect Advanced Deployments 

 Next 

 Dynamic DNS Registration Support for Remote Troubleshooting and Updates 

 Configure Multiple Portals in Prisma Access 

 Learn how to configure multiple portals with multiple authentication
 methods. 

 Where Can I Use
 This? What Do I Need? 

 Prisma Access (Managed by Strata Cloud Manager) 

 Prisma Access (Managed by Panorama) 

 Windows, macOS, Android, and iOS endpoints 

 Prisma Access license 

 GlobalProtect version 6.1 and later for Windows, macOS,
 Android, and iOS endpoints 

 This feature is available on request. Contact your account
 team to enable the feature. 

 You can configure two portals based on port numbers in the same Prisma Access tenant,
 with each portal supporting a different authentication method. Enable this feature
 to migrate mobile users from one authentication method to another without creating a
 new Prisma Access tenant. This configuration enables greater authentication
 flexibility by allowing you to gradually move users to cloud-based authentication,
 without the need for a separate Prisma Access instance. 

 Prisma Access with GlobalProtect multiple portals uses a different port number for
 each portal within the same tenant. Configure the first GlobalProtect portal using
 the standard port 443. When you enable the multiple portal feature, Prisma Access 
 configures a second GlobalProtect portal using an alternative port 8443, and allows
 connections to the second portal using the same FQDN as the first. The multiple
 portals feature supports only two portals per FQDN. 

 When a user connects to the portal using port 443, the traffic is sent to the first
 authentication portal with no change to the IP address. This flow is unchanged from
 configurations without the GlobalProtect multiple portals feature. When a user
 connects using port 8443, the traffic instead hits a destination NAT rule. This
 leads the user to the second authentication portal at a different IP address. After
 authenticating at either portal, the user is forwarded to the gateway with the
 authentication override cookie. This feature depends on
 the authentication override cookie settings, and are enabled for both portals and on
 gateways. 

 The following table describes GlobalProtect multiple portals support with
 combinations of authentication methods and certificates using legacy authentication
 (such as RADIUS or LDAP) on the primary portal and cloud authentication (such as
 SAML or SAML with CAS) on the secondary portal. 

 Primary Portal User Authentication Secondary Portal User Authentication Connection Method Options 

 Legacy, No certificate Cloud, No certificate User logon (always-on, on-demand) 

 Legacy, <auth profile selection> AND Client Certificate 

 Note: Certificate profile must be the same. 

 Cloud, <auth profile selection> AND Client Certificate 

 Note: Certificate profile must be the same. 

 User logon (always-on, on-demand) 

 Pre-logon (always-on, on-demand) 

 Legacy, No certificate Cloud, <auth profile selection> OR Client Certificate User logon (always-on, on-demand) 

 Legacy, <auth profile selection> OR Client Certificate 

 Multiple portal configurations don't support clients using only
 client certificate for authentication 

 Cloud, No certificate 

 User logon (always-on, on-demand) 

 Pre-logon (always-on, on-demand), if certificate 

 Legacy, <auth profile selection> OR Client Certificate 

 Multiple portal configurations don't support clients using only
 client certificate for authentication 

 Cloud, <auth profile selection> OR Client Certificate 

 Multiple portal configurations don't support clients using only
 client certificate for authentication 

 User logon (always-on, on-demand) 

 Pre-logon (always-on, on-demand), if certificate 

 Ensure the following before you configure multiple portals: 

 Both portals have the same certificate profiles or no certificate
 profiles 

 Allowlist associated with the authentication profiles should be the same 

 When you accept a cookie for authentication override on the portal, ensure the
 cookie lifetime is the same on the portal as well as on the gateway 

 Multiple portal configurations don't support using only client certificate-based
 authentication 

 Clientless VPN is not supported
 for use on the secondary portal in a multiple portal deployment; however, clientless
 VPN works on the primary portal with your existing authentication method. 

 Strata Cloud Manager 

 Panorama 

 Configure Multiple Portals in Prisma Access ( Strata Cloud Manager ) 

 Learn how to configure multiple portals with multiple authentication methods in Prisma Access (Managed by Strata Cloud Manager) . 

 To activate this functionality, reach out to your
 Palo Alto Networks representative. 

 Configure a mobile user and the authentication method for it. 

 Enable multiple portals for the same gateway. 

 Select Configuration NGFW and Prisma Access Configuration Scope Prisma Access GlobalProtect GlobalProtect Setup Infrastructure . 

 Edit the Infrastructure Settings . 

 Enable Multiple Portal for Multiple Authentication
 Methods . 

 The new portal appears for the 8443 port for the same tenant. This
 portal inherits the configuration settings from the original port,
 which is port 443. 

 Edit the portal configurations to update the authentication
settings. 

 You can edit only the portal's Authentication Settings and
 Certificate Profile authentication settings. 

 If you use certificate-based authentication in both
 portals, ensure that both portals use the same client certificate profile
 for authentication. 

 This feature enables the authentication override
 settings to generate cookie for both portals in the GlobalProtect app
 settings. 

 This feature enables the authentication override
 settings to generate and accept cookie for both portals in the tunnel
 settings. 

 Save all your changes and Push the configuration changes
 to Prisma Access . 

 Add the portals manually or using endpoint management
software in the GlobalProtect app. 

 Verify if you can connect to both portals with different
authentication profiles for the gateway. 

 Log in to your Windows machine. 

 Connect to the portals in your GlobalProtect app. 

 When you change the connection between portals of different
authentication methods, authenticate the user login. 

 If the authentication cookie expires when you connect to the 8443
 portal and switch to the manual gateway, GlobalProtect connects
 to the Best Available Gateway . 

 If your GlobalProtect app uses cached portal configurations,
 fallback to portal does not work. 

 If you're using SAML-based authentication for the
 secondary portal, enter the values as follows while integrating: 
 Single sign on URL : Enter
 https:// Portal-FQDN :443/SAML20/SP/ACS 
 Portal-FQDN 
 is the FQDN for the Prisma Access portal 

 Use portal
 443 even if you have configured the secondary
 portal (8443). 

 Audience URI (SP Entity ID) : Enter
 https:// Portal-FQDN :443/SAML20/SP 

 Configure Multiple Portals in Prisma Access ( Panorama ) 

 Learn how to configure multiple portals with multiple authentication methods in Prisma Access (Managed by Panorama) . 

 Contact your Palo Alto Networks account
 representative to activate this functionality. 

 When configuring multiple GlobalProtect portals with Traffic Steering, do
 not configure Accept Default Routes over Service
 Connections ( Panorama Cloud Services Configuration Traffic Steering Settings Accept Default Route over Service Connection ); if you do, mobile users cannot connect to the secondary
 portal. 

 Configure a mobile user 
 and the authentication method for it. 

 Select Cloud Services Configuration Mobile Users—GlobalProtect Settings Advanced . 

 Enable Multiple Portal for Multiple Authentication
 Methods . 

 The new portal appears for the 8443 port for the same tenant. This portal
 inherits the configuration settings from the original port, which is port
 443. 

 Edit the portal configurations to update the authentication settings. 

 Click the portal hyperlink or select Panorama Templates Network GlobalProtect Portals and click the portal hyperlink. 

 In the Authentication section,
 Add a Client
 Authentication with a different
 Authentication Profile . 

 You can edit only the Client Authentication and
 Certificate Profile authentication settings. 

 If you use certificate-based authentication in both portals, ensure that both
 portals use the same client certificate profile for authentication. 

 This feature enables the authentication override
 settings to generate and accept cookie for both portals in the tunnel
 settings. 

 Commit all your changes to Panorama and push the configuration changes to
 Prisma Access . 

 Click Commit Commit and Push . 

 Edit Selections and, in the Prisma
 Access tab, make sure that Mobile
 Users is selected in the Push
 Scope , then click OK . 

 Click Commit and Push . 

 Add the portals manually or using endpoint management software in the
 GlobalProtect app. 

 Verify if you can connect to both portals with different authentication
 profiles for the gateway. 

 Log in to your Windows machine. 

 Connect to the portals in your GlobalProtect app. 

 When you change the connection between portals of different
 authentication methods, authenticate the user login. 

 If the authentication cookie expires when you connect to the 8443
 portal and switch to the manual gateway, GlobalProtect connects
 to the Best Available Gateway . 

 If your GlobalProtect app uses cached portal configurations,
 fallback to portal does not work. 

 View logs for both portals in Monitor Logs GlobalProtect to see the portal and authentication information. 

 If you're using SAML-based authentication for the
 secondary portal, enter the values as follows while integrating: 
 Single sign on URL : Enter
 https:// Portal-FQDN :443/SAML20/SP/ACS 
 Portal-FQDN 
 is the FQDN for the Prisma Access portal 

 Use portal
 443 even if you have configured the secondary
 portal (8443). 

 Audience URI (SP Entity ID) : Enter
 https:// Portal-FQDN :443/SAML20/SP 

 Previous 

 Prisma Access Mobile Users—GlobalProtect Advanced Deployments 

 Next 

 Dynamic DNS Registration Support for Remote Troubleshooting and Updates 

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

 4.1 Preferred 

 5.0 Preferred and Innovation 

 Administration 

 Prisma SASE 

 Prisma Access 

 Strata Cloud Manager 

 SASE 

 4.2 Preferred 

 5.1 Preferred and Innovation 

 5.0.1 Preferred and Innovation 

 Panorama 

 6.0 Preferred and Innovation 

 Prisma Access 

 4.0 Preferred 

 4.0 & Later 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
