---
url: https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/configuration-scm/manage-configuration-ngfw-and-prisma-access/objects/certificate-management/ngts-scm-integration-overview
fetched_at: 2026-08-13T17:37:27Z
source: palo-alto-main
---

# Strata Cloud Manager Integration with Next-Gen Trust Security Clear

Strata Cloud Manager Integration with Next-Gen Trust Security 

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

 Strata Cloud Manager Integration with Next-Gen Trust Security 

 Updated on 

 Aug 3, 2026 

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

 Strata Cloud Manager Docs 

 Activation & Onboarding 

 Subscription & Tenant Management 

 Getting Started 

 AIOps 

 Release Notes 

 New Features 

 Updated on 

 Aug 3, 2026 

 Focus 

 Home 

 Strata Cloud Manager 

 Strata Cloud Manager Getting Started 

 Configuration: Strata Cloud Manager 

 Configuration:
 NGFW and Prisma Access 

 Configuration:
 Objects 

 Certificate Management 

 Strata Cloud Manager Integration with Next-Gen Trust Security 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deutsch (German) 

 Strata Cloud Manager 

 Strata Cloud Manager Integration with Next-Gen Trust Security 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Strata Cloud Manager Docs 

 Activation & Onboarding 

 Subscription & Tenant Management 

 Getting Started 

 AIOps 

 Release Notes 

 New Features 

 Previous 

 Certificate Management 

 Next 

 Access the Network Trust Security Page 

 Strata Cloud Manager Integration with Next-Gen Trust Security 

 Use Next-Gen Trust Security to manage certificate lifecycles for certificates in your
 Strata Cloud Manager configuration. 

 Where Can I Use This? What Do I Need? 

 Strata Cloud Manager 

 Secure-Flex Credits 

 Strata Cloud Manager (Essentials or Pro) 

 For Strata Cloud Manager Shared Services, one of these roles:

 To view certificates: Network Administrator, View Only Administrator, Tier 1 Support, Tier 2 Support, Security Administrator, Superuser 

 To manage and renew certificates: Security Administrator, Superuser 

 Next-Gen Trust Security provides visibility to PKI Administrators and enables full Certificate Lifecycle Management (CLM) capabilities, allowing you to seamlessly discover, manage, and renew certificates with enterprise-approved CAs directly within Strata Cloud Manager. 

 Digital certificates secure communications, including TLS, SSH, HTTPS, authentication portals, and VPN connections. Without centralized management, certificate sprawl across hundreds or thousands of certificates leads to expired certificates, insecure cryptography, and network disruptions. The Network Trust Security integration brings Next-Gen Trust Security certificate lifecycle management capabilities directly into Strata Cloud Manager. 

 How Certificate Synchronization Works 

 When you access the Network Trust Security page in Strata Cloud Manager, certificates from your Strata Cloud Manager configuration sync to the Next-Gen Trust Security inventory. Next-Gen Trust Security discovers certificates across your deployment, including those used in authentication portals, decryption policies, VPN configurations, and device management. Certain certificate types do not sync: certificates in subscribed snippets, the GP_Log_Certificate, certificate signing requests (CSRs), CA certificates, and certificates used in decryption rules. 

 Certificate Management States 

 Certificates exist in two states within the Network Trust Security integration: 

 Unmanaged: Unmanaged certificates appear in your Strata Cloud Manager configuration but aren't tracked by Next-Gen Trust Security—they won't appear in the Next-Gen Trust Security certificate inventory. Unmanaged certificates don't count against your license. 

 Managed: You must explicitly manage certificates through the Network
 Trust Security page in Strata Cloud Manager to enable Next-Gen Trust Security
 lifecycle capabilities. Managing Strata Cloud Manager certificates brings them
 under the same centralized visibility, policy enforcement, and lifecycle
 management as other critical certificates in your organization—ensuring
 consistent security standards, renewal processes, and monitoring across your
 entire certificate infrastructure. Managed certificates count against your
 license. Once managed, certificates become visible in the Next-Gen Trust Security certificate
 inventory , where you can monitor their health, view usage locations,
 and initiate renewal workflows. 

 Certificate Renewal Through Next-Gen Trust Security 

 Certificate renewal uses issuing templates that PKI administrators configure in the Next-Gen Trust Security console. Issuing templates are policies that define cryptographic standards for certificate generation. These templates specify: 

 Key algorithm and length (for example, RSA 2048-bit or RSA 4096-bit) 

 Subject and Subject Alternative Names (SANs) that are allowed 

 Certificate validity period 

 Extended key usage fields 

 Other cryptographic parameters 

 By defining issuing templates, PKI administrators ensure all renewed certificates meet organizational security standards. Next-Gen Trust Security helps you prevent certificate expiration by automating renewal workflows and providing visibility into certificate lifecycle status across your infrastructure. 

 When you initiate renewal from the Network Trust Security page in Strata Cloud Manager, Next-Gen Trust Security generates a new private key and certificate signing request (CSR) based on the template, submits the CSR to a certificate authority, and imports the renewed certificate with its private key back into Strata Cloud Manager. 

 The imported certificate's trust chain may be different than it was for the previous certificate if the issuer changed. Plan accordingly and verify trust chain compatibility with your applications and services. 

 After the renewed certificate is imported into Strata Cloud Manager, you must manually push the configuration to your firewalls to complete the certificate update. 

 Next Steps 

 To get started with certificate management through Next-Gen Trust Security in Strata Cloud Manager: 

 Access the Network Trust Security page (see Access the Network Trust Security Page ) 

 Manage certificates to bring them under Next-Gen Trust Security lifecycle tracking (see Manage Certificates in Next-Gen Trust Security ) 

 Renew certificates using enterprise-approved certificate authorities (see Renew Certificates Using Next-Gen Trust Security ) 

 Push the updated configuration to your firewalls 

 For comprehensive information about Next-Gen Trust Security capabilities, see the Next-Gen Trust Security documentation . 

 Previous 

 Certificate Management 

 Next 

 Access the Network Trust Security Page 

 On This Page 

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

 Endpoints 

 GlobalProtect 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Getting Started 

 Strata Cloud Manager 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
