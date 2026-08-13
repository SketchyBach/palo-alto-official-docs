---
url: https://docs.paloaltonetworks.com/network-security/security-policy/administration/security-profiles/security-profile-url-filtering/configure-url-filtering-cloud-management
fetched_at: 2026-08-12T14:08:13Z
source: strata-and-sase
---

# Configure URL Filtering (Strata Cloud Manager) Clear

Configure URL Filtering (Strata Cloud Manager) 

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

 Configure URL Filtering (Strata Cloud Manager) 

 Updated on 

 Aug 5, 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Network Security Docs 

 Security Policy 

 IPsec VPN 

 Decryption 

 Device-ID 

 Quantum Security 

 Quality of Service 

 Updated on 

 Aug 5, 2026 

 Focus 

 Home 

 Network Security 

 Network Security: Security Policy 

 Security Profiles 

 Security Profile: URL Filtering 

 Configure URL Filtering (Strata Cloud Manager) 

 Download PDF 

 Network Security 

 Configure URL Filtering (Strata Cloud Manager) 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Network Security Docs 

 Security Policy 

 IPsec VPN 

 Decryption 

 Device-ID 

 Quantum Security 

 Quality of Service 

 Configure URL Filtering (Strata Cloud Manager) 

 Follow these steps to configure URL Filtering profiles and settings that meet your
 organization’s business and security needs. 

 After you plan your URL filtering deployment, you should have a basic understanding
 of the types of websites your users are accessing. Use this information to create a
 URL Filtering profile that defines how the firewall handles traffic to specific URL
 categories. You can also restrict the sites to which users can submit corporate
 credentials or enforce strict safe search. To activate these settings, apply the URL
 Filtering profile to Security rules that allow web access. 

 Follow these steps to configure URL Filtering profiles and settings that meet your
 organization’s business and security needs. See Advanced URL Filtering: Configure URL
 Filtering for detailed steps. 

 Go to Configuration NGFW and Prisma Access Security Services URL Access Management 

 Review and customize General URL Filtering Settings. 

 Automatically append end tokens to URLs in an EDL or a custom URL
 category 

 If you use URLs in custom URL categories or external dynamic lists (EDLs)
 and do not append an ending token, it is possible to allow more URLs
 than you intended. For example, entering example.com as a matching URL
 instead of example.com/ would also match example.com.website.info or
 example.com.br.Prisma Access can automatically set an ending token to
 URLs in EDLs or custom URL categories so that, if you enter example.com,
 Prisma Access treats it as it would treat example.com/ and only match
 that URL. 

 Go to System Settings General Settings and enable the option to Append End Token to
 Entries . 

 Create a URL Access Management profile. 

 Apply the URL Access Management profile to a Security rule. 

 A URL Access Management profile is only active when it’s included in a
 profile group that a Security policy rule references. Follow the steps to
 activate a URL Access Management profile (and any
 Security profile). 

 Select Save and Push
 Config . 

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

 © 2026 Palo Alto Networks, Inc. All rights reserved.
