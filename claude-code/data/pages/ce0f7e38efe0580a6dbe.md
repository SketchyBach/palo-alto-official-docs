---
url: https://docs.paloaltonetworks.com/network-security/quantum-security/administration/quantum-safe-security/how-to-use-the-quantum-safe-security-app
fetched_at: 2026-08-13T16:38:23Z
source: palo-alto-main
---

# How To Use the Quantum-Safe Security App Clear

How To Use the Quantum-Safe Security App 

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

 How To Use the Quantum-Safe Security App 

 Updated on 

 Mon Jul 20 09:20:53 PDT 2026 

 Focus 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

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

 Mon Jul 20 09:20:53 PDT 2026 

 Focus 

 Home 

 Network Security 

 Quantum-Safe Security App 

 How To Use the Quantum-Safe Security App 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Network Security 

 How To Use the Quantum-Safe Security App 

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

 Previous 

 Enable Comprehensive Cryptographic Visibility 

 Next 

 Configure Asset Criticality 

 How To Use the Quantum-Safe Security App 

 Accomplish common PQC migration planning and preparation tasks. 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by Strata Cloud Manager) 

 Prisma Access (Managed by Strata Cloud Manager) 

 Quantum-Safe Security
 license 

 Includes access to Strata Logging
 Service and Strata Cloud Manager
 Essentials . If you do not have a Strata Cloud
 Manager Pro or Strata Logging Service subscription, this
 license covers all feature prerequisites. 

 Device Telemetry 
 enabled for your NGFWs 

 The Quantum-Safe Security app translates asset and cryptographic metadata into actionable
 insights and recommendation workflows. You can leverage the inventory and dashboard to
 streamline critical PQC migration planning and preparation tasks, including
 assessing risk at the organizational and individual asset levels, identifying
 remediation options, and setting migration priorities. 

 The following table outlines common use cases and how to use the app to achieve the
 specific goal. 

 Use Case How to do it 

 I want to identify specific assets that are ready for
 migration. 

 Select the Inventory tab, and then click
 Add Filter . Apply the Quantum
 Readiness filter and select
 Ready to see all assets whose underlying
 hardware and software currently support PQC. 

 To narrow your focus further, combine this with the
 Type filter. For example, to identify web
 applications ready for migration, select the
 Internet filter for
 Type 
 and the Quantum Readiness filter
 ( Ready ). 

 I want to prioritize assets vulnerable to Harvest Now, Decrypt Later
 (HNDL) attacks. 

 Open the Overview dashboard and look
 at the central pie chart to view the total volume of data
 currently exposed to HNDL risks. 

 Click View Details on the HNDL risk
 category to reveal top risk contributors and other
 information. 

 Switch to the Inventory view, click
 Add Filter , and then filter by
 Cryptography Risk to isolate the
 specific assets transmitting this vulnerable data so you can
 move them to the top of your migration queue. 

 I want to prioritize PQC migration for my most business-critical
 assets. 

 In the Inventory , click
 Configure Impact to define
 automated rules that classify
 Applications or User
 Devices as High 
 business impact based on App-ID categories or user
 groups. 

 Alternatively, or to manually configure asset
 criticality for any asset type, select one or
 more assets and click Modify Business
 Impact . 

 Check the Business Context: Impact column
 to confirm each asset's rating. 

 Use the Cryptography Risk (select
 Harvest Now, Decrypt Later ) and
 Business Impact (select
 High ) filters to build a prioritized
 remediation roadmap. 

 I want to pinpoint the root cause of a weak cryptographic
 session. 

 Select the problematic asset in the Inventory 
 view (click the Asset Name ) to inspect
 details, such as the cryptography in use. 

 The app automatically traces the vulnerability back to its exact
 source, revealing whether the weak cryptography stems from a
 specific underlying crypto-library (such as a deprecated OpenSSL
 version) or an outdated operating system. 

 I want to secure legacy IoT devices or infrastructure that I cannot
 easily upgrade. 

 Use the Inventory view to identify
 non-upgradable assets. For these devices or infrastructure, you see
 cipher translation recommendations. To enable the Cipher Translation
 Proxy, follow the steps in the recommendations panel. Your NGFW then
 acts as an inline proxy that intercepts the legacy classical
 algorithms and re-encrypts the traffic into quantum-resistant
 algorithms ( ML-KEM ) at the network
 edge in real time, requiring zero code changes to the legacy
 endpoint itself. 

 I want to find the exact upgrade path to make an asset
 quantum-safe. 

 In the Inventory view, click
 Show Recommendations . 

 Click the Quantum Safe category of
 recommendations. 

 This opens a dedicated side panel displaying targeted
 mitigation steps. You can use the search bar within the
 recommendations panel to look for specific terms like
 "hardware" or "software" to find exact guidance, such as
 whether a device requires an OS upgrade or a certificate
 compliance change. 

 I want to identify the specific firewall configurations and policies
 permitting weak cryptography. 

 Select the problematic asset (click the Asset
 Name ) in the Inventory view.
 The app provides policy-level visibility that reveals exactly which
 decryption profiles, decryption policy rules, or security policy
 rules are actively allowing weak or vulnerable
 sessions. This enables you to assess the business impact of a
 configuration change before applying it to block the vulnerable
 cryptography. 

 You can also filter assets by the Data
 Exposure risk and view recommendations specific to
 these assets. 

 I want to share my organization's quantum posture with executives and
 compliance stakeholders. 

 I want to share the percentage of business-critical assets that are
 quantum-ready. 

 Generate a Quantum-Safe Security
 report from the Overview or
 Inventory view of the Quantum-Safe
 Security app or from Strata Canvas Reports . Reports are downloadable as PDFs and can be shared
 with specific recipients or scheduled for recurring delivery. 

 Report sections that analyze business-critical assets
 require you to configure asset
 criticality . These sections remain empty until you
 designate assets as critical. 

 Previous 

 Enable Comprehensive Cryptographic Visibility 

 Next 

 Configure Asset Criticality 

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

 Network Visibility 

 Network Security 

 PAN-OS 

 Next-Generation Firewall 

 Quantum Security 

 Strata Cloud Manager 

 Core 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
