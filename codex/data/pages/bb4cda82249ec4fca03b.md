---
url: https://docs.paloaltonetworks.com/network-security/security-policy/administration/security-profiles/security-profile-dns-security/enable-dns-security-pm
fetched_at: 2026-08-12T14:08:09Z
source: strata-and-sase
---

# Security Profile: DNS Security (PAN-OS & Panorama) Clear

Security Profile: DNS Security (PAN-OS & Panorama) 

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

 Security Profile: DNS Security (PAN-OS & Panorama) 

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

 Security Profile: DNS Security 

 Security Profile: DNS Security (PAN-OS & Panorama) 

 Download PDF 

 Network Security 

 Security Profile: DNS Security (PAN-OS & Panorama) 

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

 Security Profile: DNS Security (PAN-OS & Panorama) 

 Learn how to configure a DNS Security profile in PAN-OS & Panorama. 

 Here's how to configure a DNS Security profile. See Enable DNS Security for detailed
 steps. 

 To take advantage of DNS Security, you must have an active DNS Security and
 Threat Prevention (or Advanced Threat Prevention) subscription. 

 Verify that you have the necessary subscriptions. To verify which
 subscriptions that you currently have licenses for, select Device Licenses and verify that the appropriate licenses display and have not
 expired. 

 Verify that the paloalto-dns-security App-ID in your security policy is
 configured to enable traffic from the DNS security cloud security service. 

 If your firewall deployment routes your management traffic though an
 Internet-facing perimeter firewall configured to enforce App-ID security
 policies, you must allow the App-IDs on the perimeter firewall; failure
 to do so will prevent DNS security connectivity. 

 Configure DNS Security signature policy settings to send malicious DNS queries
 to the defined sinkhole. 

 If you use an external dynamic list as a domain allow list, it does not
 have precedence over the DNS Security domain policy actions. As a
 result, when there is a domain match to an entry in the EDL and a DNS
 Security domain category, the action specified under DNS Security is
 still applied, even when the EDL is explicitly configured with an action
 of Allow. If you want to add DNS domain exceptions, either configure an
 EDL with an Alert action or add them to the DNS Domain/FQDN Allow List
 located in the DNS Exceptions tab. 

 Attach the Anti-Spyware profile to a Security policy rule. 

 Test that the policy action is enforced. 

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
