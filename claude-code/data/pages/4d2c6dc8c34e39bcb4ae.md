---
url: https://docs.paloaltonetworks.com/ngfw/getting-started/configure-your-ngfws/enable-free-wildfire-forwarding-on-the-ngfw
fetched_at: 2026-08-13T16:40:59Z
source: palo-alto-main
---

# Enable Free WildFire Forwarding on the NGFW Clear

Enable Free WildFire Forwarding on the NGFW 

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

 Enable Free WildFire Forwarding on the NGFW 

 Updated on 

 Tue Mar 24 19:20:23 PDT 2026 

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

 Tue Mar 24 19:20:23 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 Configure Your NGFWs 

 Enable Free WildFire Forwarding on the NGFW 

 Download PDF 

 Next-Generation Firewall 

 Enable Free WildFire Forwarding on the NGFW 

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

 Enable Free WildFire Forwarding on the NGFW 

 Learn how to enable free WildFire forwarding on your PAN-OS or Panorama managed NGFWs. 

 Where Can I Use This? What Do I Need? 

 NGFW (PAN-OS or Panorama) 

 This feature has no prerequisites; go ahead and get
 started 

 WildFire is a cloud-based virtual
 environment that analyzes and executes unknown samples (files and email links) and
 determines the samples to be malicious, phishing, grayware, or benign. With WildFire
 enabled, a Palo Alto Networks firewall can forward unknown samples to WildFire for
 analysis. For newly-discovered malware, WildFire generates a signature to detect the
 malware, which is made available for retrieval in real-time for all firewalls with
 an active WildFire subscription. This enables all Palo Alto next-generation
 firewalls worldwide to detect and prevent malware found by a single firewall.
 Malware signatures often match multiple variants of the same malware family, and as
 such, block new malware variants that the firewall has never seen before. The Palo
 Alto Networks threat research team uses the threat intelligence gathered from
 malware variants to block malicious IP addresses, domains, and URLs. 

 A basic WildFire service is included as part of the Palo Alto Networks
 next-generation firewall and does not require a WildFire subscription. With the
 basic WildFire service, you can enable the firewall to forward portable executable
 (PE) files. Additionally, if you do not have a WildFire subscription, but you do
 have a Threat Prevention subscription, you can receive signatures for malware
 WildFire identifies every 24- 48 hours (as part of the Antivirus updates). 

 Beyond the basic WildFire service, a WildFire subscription is required for the
 firewall to: 

 Get the latest WildFire signatures in real-time. 

 Prevent malicious PE (portable executables), ELF and MS Office files, and
 PowerShell and shell scripts from entering your network in real-time using
 WildFire Inline ML . 

 Forward advanced file types and email links for analysis. 

 Use the WildFire API. 

 Use a WildFire appliance to host a WildFire private cloud or a WildFire
 hybrid cloud. 

 If you have a WildFire subscription, go ahead and get started with WildFire to get the most
 out of your subscription. Otherwise, take the following steps to enable basic
 WildFire forwarding: 

 Confirm that your firewall is registered and that you have a valid support
 account as well as any subscriptions you require. 
 Log in to the Palo Alto Networks Customer Support
 Portal (CSP) and on the left-hand side navigation pane,
 select Assets Devices . 

 Verify that the firewall is listed. If it is not listed, select
 Register New Device and continue to Register Your NGFW . 

 ( Optional ) If you have a Threat Prevention subscription, be
 sure to Activate Subscription
 Licenses . 

 Log in to the firewall and configure WildFire forwarding settings. 
 Select Device Setup WildFire and edit the General Settings. 

 Set the WildFire Public Cloud field to forward
 files to the WildFire global cloud (U.S.) at:
 wildfire.paloaltonetworks.com . 

 You can also forward files to a WildFire regional cloud or a
 private cloud based on
 your location and your organizational requirements. 

 Review the File Size Limits for PEs the firewall
 forwards for WildFire analysis. set the Size
 Limit for PEs that the firewall can forward to the
 maximum available limit of 10 MB. 

 As a WildFire best
 practice , set the Size Limit for
 PEs to the maximum available limit of 10 MB. 

 Click OK to save your changes. 

 Enable the firewall to forward PEs for analysis. 
 Select Objects Security Profiles WildFire Analysis and Add a new profile rule. 

 Name the new profile rule. 

 Add a forwarding rule and enter a
 Name for it. 

 In the File Types column, add
 pe files to the forwarding rule. 

 In the Analysis column, select
 public-cloud to forward PEs to the WildFire
 public cloud. 

 Click OK . 

 Apply the new WildFire Analysis profile to traffic that the firewall
 allows. 
 Select Policies Security and either select an existing policy rule or create a new
 policy rule as described in Set Up a Basic
 Security Policy . 

 Select Actions and in the Profile Settings
 section, set the Profile Type to
 Profiles . 

 Select the WildFire Analysis profile you just
 created to apply that profile rule to all traffic this policy rule
 allows. 

 Click OK . 

 Enable the firewall to forward decrypted SSL traffic for
 WildFire analysis. 

 Review and implement WildFire best practices to ensure that
 you are getting the most of WildFire detection and prevention
 capabilities. 

 Commit your configuration updates. 

 Verify that the firewall is forwarding PE files to the WildFire public
 cloud. 

 Select Monitor Logs WildFire Submissions to view log entries for PEs the firewall successfully
 submitted for WildFire analysis. The Verdict column displays whether
 WildFire found the PE to be malicious, grayware, or benign. (WildFire only
 assigns the phishing verdict to email links). The Action column indicates
 whether the firewall allowed or blocked the sample. The Severity column indicates how much
 of a threat a sample poses to an organization using the following values:
 critical, high, medium, low, information. 

 ( Threat Prevention subscription only ) If you have a Threat Prevention
 subscription, but do not have a WildFire subscription, you can still receive
 WildFire signature updates every 24- 48 hours. 
 Select Device Dynamic Updates . 

 Check that the firewall is scheduled to download, and install Antivirus
 updates. 

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

 Getting Started 

 Panorama 

 Strata Cloud Manager 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
