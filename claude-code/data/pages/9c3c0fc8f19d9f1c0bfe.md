---
url: https://docs.paloaltonetworks.com/enterprise-dlp/administration/configure-enterprise-dlp/configure-exact-data-matching
fetched_at: 2026-08-13T15:32:11Z
source: palo-alto-main
---

# Exact Data Matching (EDM) Clear

Exact Data Matching (EDM) 

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

 Exact Data Matching (EDM) 

 Updated on 

 Fri Jul 10 12:56:22 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Enterprise DLP Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Reference 

 Release Notes 

 New Features by OS Version 

 New Features by Month 

 Updated on 

 Fri Jul 10 12:56:22 PDT 2026 

 Focus 

 Home 

 Enterprise DLP 

 Administration 

 Configure Enterprise DLP 

 Exact Data Matching (EDM) 

 Download PDF 

 Enterprise DLP 

 Exact Data Matching (EDM) 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Enterprise DLP Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Reference 

 Release Notes 

 New Features by OS Version 

 New Features by Month 

 Previous 

 Archive and Restore a Data Pattern 

 Next 

 Supported EDM Data Set Formats 

 Exact Data Matching (EDM) 

 Use the secure Exact Data Matching (EDM) CLI app to configure an EDM profile for Enterprise Data Loss Prevention (E-DLP) . 

 On May 7, 2025 , Palo Alto Networks is introducing new Evidence Storage and Syslog Forwarding service IP
 addresses to improve performance and expand availability for these services
 globally. 

 You must allow these new service IP addresses on your network
 to avoid disruptions for these services. Review the Enterprise DLP 
 Release Notes for more
 information. 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by Panorama or Strata Cloud Manager) 

 Prisma Access (Managed by Panorama or Strata Cloud Manager) 

 Prisma Browser 

 Enterprise Data Loss Prevention (E-DLP) license 

 Review the Supported
 Platforms for details on the required license
 for each enforcement point. 

 Or any of the following licenses that include the Enterprise DLP license 

 Prisma Access CASB license 

 Next-Generation
CASB for Prisma Access and NGFW (CASB-X) license 

 Data Security license 

 Exact Data Matching (EDM) for Enterprise Data Loss Prevention (E-DLP) is an advanced detection tool
 to monitor and protect sensitive data from exfiltration. Use EDM to detect sensitive and
 personally identifiable information (PII) such as social security numbers, Medical
 Record Numbers, bank account numbers, and credit card numbers, in a structured data
 source such as databases, directory servers, or structured data files, with high
 accuracy. 

 For example, you upload an EDM dataset that contains the following data: 

 FName 

 LName 

 SSN 

 BankAccNum 

 CCN 

 Bill 

 Smith 

 123-45-6789 

 22334455 

 1111-2222-3333-4444 

 In this case, Enterprise DLP detects sensitive data in inspected traffic if
 Smith and 22334455 are
 within 100 characters of each other. 

 Encryption of Uploaded EDM Data Sets 

 To use EDM, Enterprise DLP relies on the encrypted hash of the sensitive
 data you upload to Enterprise DLP . Enterprise DLP indexes the
 encrypted hash of uploaded EDM datasets. To prevent the exfiltration of
 sensitive data, Enterprise DLP uses the indexed hash dataset in the
 Security policy rule for matching outbound traffic. 

 The EDM CLI App first hashes the dataset using the SHA256 hash function when you
 initiate an EDM dataset upload. The EDM CLI App then encrypts the EDM dataset
 using AES Symmetric encryption before beginning the EDM dataset upload to the
 Enterprise DLP EDM dataset storage bucket. The raw data in your EDM
 datasets never leave your organization's network, and Enterprise DLP does
 not store or have access to the raw EDM dataset data. Enterprise DLP stores
 only hashed and encrypted EDM dataset data in the EDM dataset storage bucket . 

 Data Residency for Uploaded EDM Data Sets 

 You can configure the EDM CLI app version 4.0 and later to upload your hashed and
 encrypted EDM datasets to region-specific storage bucket when configuring
 connectivity for the EDM CLI app. Review the FQDNs for EDM to see the full list of
 regions Enterprise DLP supports. 

 Supported EDM Data Set Formats 

 Set Up the EDM CLI App 

 Create a Service Account for EDM Dataset Uploads 

 Configure EDM CLI App Connectivity to Enterprise DLP 

 Upload an Encrypted EDM Data Set to Enterprise DLP Using a Configuration File 

 Create and Upload an Encrypted EDM Data to Enterprise DLP in Interactive Mode 

 Update an Existing EDM Data Set on Enterprise DLP 

 Previous 

 Archive and Restore a Data Pattern 

 Next 

 Supported EDM Data Set Formats 

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

 SaaS Security 

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

 Administration 

 Cloud-Delivered Security Services 

 Data Filtering 

 Enterprise DLP 

 Concept 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
