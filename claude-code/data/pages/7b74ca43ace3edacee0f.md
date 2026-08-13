---
url: https://docs.paloaltonetworks.com/prisma-access/activation-and-onboarding/your-prisma-access-license/all-available-apps-and-services/cheat-sheet-dlp-with-prisma-access
fetched_at: 2026-08-13T17:24:02Z
source: palo-alto-main
---

# Cheat Sheet: Enterprise DLP with Prisma Access Clear

Cheat Sheet: Enterprise DLP with Prisma Access 

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

 Cheat Sheet: Enterprise DLP with Prisma Access 

 Updated on 

 Apr 14, 2026 

 Focus 

 Download PDF 

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

 Apr 14, 2026 

 Focus 

 Home 

 Prisma Access 

 Prisma Access Activation and Onboarding 

 Your Prisma Access License 

 All Available Apps and Services 

 Cheat Sheet: Enterprise DLP with Prisma Access 

 Download PDF 

 Prisma Access 

 Cheat Sheet: Enterprise DLP with Prisma Access 

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

 Cheat Sheet: IoT Security with Prisma Access 

 Next 

 Cheat Sheet: SaaS Security with Prisma Access 

 Cheat Sheet: Enterprise DLP with Prisma Access 

 Data loss prevention (DLP) is a set of tools and processes
that allow you to protect sensitive information against unauthorized
access, misuse, extraction, or sharing. 

 Where Can I Use
This? What Do I Need? 

 Prisma Access (Managed by Strata Cloud Manager) 

 Prisma Access (Managed by Panorama) 

 Prisma Access license 

 Data loss prevention (DLP) protects sensitive information against unauthorized access,
 misuse, extraction, or sharing. Enterprise DLP on Prisma Access enables you to enforce
 your organization’s data security standards and prevent the loss of sensitive data
 across mobile users and remote networks. 

 Prisma Access integrates its DLP capability to allow Prisma Access (Managed by Strata Cloud Manager) to use
 the same DLP capabilities as those used in Panorama and on next-generation firewalls.
 This integration provides you with an improved experience that allows you to use the
 same DLP patterns, profiles, and rules as those used in next-generation firewalls. 

 Strata Cloud Manager 

 Panorama 

 Cheat Sheet: Enterprise DLP with Prisma Access (Managed by Strata Cloud Manager) 

 Enterprise DLP on Prisma Access (Managed by Strata Cloud Manager) enables
you to enforce your organization’s data security standards and prevent
the loss of sensitive data. 

 Important: If you’re already using Panorama to manage Enterprise DLP for next-gen
 firewalls, your DLP configuration (data patterns and DLP profiles) in Prisma Access 
 Cloud Management is read-only; continue to manage DLP from Panorama. 

 Feature Highlights 

 Get Started 

 Feature Highlights 

 The Data Loss Prevention Dashboard 
 In Strata
 Cloud Manager, go to Configuration Data Loss Prevention to configure and manage Enterprise DLP. 

 Your Enterprise DLP
 configuration is shared across the products where you’re using Enterprise DLP.
 So, you might see settings here that were configured elsewhere, and some
 settings you can configure here can also be leveraged in other
 products. 
 Predefined + Custom Enterprise DLP Settings 
 Enterprise DLP
 includes built-in settings that you can use to quickly start protecting your
 most sensitive content: 

 Predefined data patterns 
 specify common types of sensitive information (like credit cards and
 social security numbers) that you might want to scan for and protect 

 Predefined DLP Profiles group
 together data patterns that commonly require the same type of
 enforcement 

 You can also create custom data patterns and profiles directly in Prisma
 Access Cloud Management. 
 Investigation for DLP Incidents 
 A DLP
 incident is generated when traffic matches a DLP data profile on Prisma Access (Managed by Strata Cloud Manager) . On the DLP Incidents dashboard , you can view
 details for the traffic that triggered the incident, such as matched data
 patterns, the source and destination of the traffic, the file and file type. Go
 to Configuration Data Loss Prevention DLP Incidents . 
 Scanning for Images in Supported File
 Formats 
 Strengthen your security posture to further prevent accidental
 data misuse, loss, or theft with Optical Character Recognition (OCR) .
 OCR allows the DLP cloud service to scan supported file types with images
 containing sensitive information that match your Enterprise DLP filtering
 profiles. 
 Exact Data Matching (EDM) 
 EDM is an advanced detection tool to
 monitor and protect sensitive data from exfiltration. Use EDM to detect
 sensitive and personally identifiable information (PII) such as social security
 numbers, Medical Record Numbers, bank account numbers, and credit card numbers,
 in a structured data source such as databases, directory servers, or structured
 data files (CSV and TSV), with high accuracy. 
 Role-Based Access for
 Enterprise DLP 
 You can provide role-based access to Enterprise DLP
 controls inside Prisma Access (Managed by Strata Cloud Manager) : 

 Data Loss Prevention Admin —Can access Enterprise DLP settings but
 can't push configuration changes to Prisma Access . 

 Data Security Admin —Can access Enterprise DLP and SaaS Security
 controls, but can't push configuration changes to Prisma Access . 

 Get Started 

 Here’s how to get up and running with Enterprise DLP on Prisma Access (Managed by Strata Cloud Manager) . 

 Check that Your License Covers Enterprise DLP. 

 Here’s how to
 check what’s available with your license 

 Enable Role-Based Access for Enterprise DLP. 

 Here’s how to add a Data Loss
 Prevention Admin or a Data Security Admin 

 Set Up decryption for Enterprise DLP 

 Enterprise DLP supports HTTP/1.1. Some applications, like SharePoint and
 OneDrive, support HTTP/2 for uploads by default. To make applications
 that use HTTP/2 compatible with Enterprise DLP, you’ll need to strip
 ALPN headers from uploaded files. 

 In Strata Cloud Manager, go to Configuration NGFW and Prisma Access Security Services Decryption . Select the Prisma Access 
 configuration scope and: 

 Create a decryption profile, and set it to Strip
 ALPN . 

 (Find the Advanced Settings in the
 SSL Forward Proxy section). 

 Add the decryption profile to an SSL Forward
 Proxy decryption rule. 

 Create a Data Pattern. 

 Enterprise DLP data patterns specify what content is sensitive and needs
 to be protected—this is the content you’re filtering. You can create a
 custom data pattern based on regular
 expressions or a data pattern based on file
 properties . 

 Create a Data Profile. 

 Group data patterns that should be enforced the same way into a data
 profile. You can also use data profiles to specify additional match
 criteria and confidence levels for matching. 

 Data profiles can contain regular expression data patterns, Exact Data Matching (EDM) data
 patterns, or a combination of both. 

 Here’s how to create a data
 profile 

 Create a DLP rule. 

 Specify the traffic and file types you want Enterprise DLP to protect.
 Set the action for Enterprise DLP to take when it detects a DLP
 incident. 

 Here’s how to create a DLP
 rule 

 Enable the DLP rule. 

 In Prisma Access (Managed by Strata Cloud Manager) , a DLP rule is a type of security
 profile. To enable a security profile to enforce traffic: Add it to a
 profile group, and add the profile group to a security rule. 

 Here’s how to enable a security
 profile (including a DLP rule) 

 Cheat Sheet: Enterprise DLP with Prisma Access (Managed by Panorama) 

 Enterprise DLP on Prisma Access (Managed by Panorama) enables
you to enforce your organization’s data security standards and prevent
the loss of sensitive data. 

 Use DLP with Prisma Access (Managed by Panorama) by installing the Enterprise DLP plugin on the
 same Panorama appliance that manages Prisma Access. 

 If you have migrated from an existing DLP on Prisma Access license to the DLP plugin, the
 locations of data patterns and data filtering profiles move in Panorama after the
 migration: 

 Data
patterns move from Objects Custom Objects Data Patterns to Objects DLP DLP
Data Patterns . 

 Data filtering profiles move from Objects Security Profiles Data Filtering to Objects DLP DLP
Data Filters . 

 Previous 

 Cheat Sheet: IoT Security with Prisma Access 

 Next 

 Cheat Sheet: SaaS Security with Prisma Access 

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

 Activation & Onboarding 

 Prisma SASE 

 Prisma Access 

 Panorama 

 Strata Cloud Manager 

 4.0 & Later 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
