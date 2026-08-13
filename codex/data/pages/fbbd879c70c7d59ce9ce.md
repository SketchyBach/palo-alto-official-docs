---
url: https://docs.paloaltonetworks.com/cloud-ngfw-azure/release-notes/cloud-ngfw-for-azure-addressed-issues
fetched_at: 2026-08-13T15:31:11Z
source: palo-alto-main
---

# Cloud NGFW for Azure Addressed Issues Clear

Cloud NGFW for Azure Addressed Issues 

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

 Cloud NGFW for Azure Addressed Issues 

 Updated on 

 Wed Jun 24 06:49:38 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Cloud NGFW for Azure Docs 

 Getting Started 

 Deployment 

 Administration 

 Reference 

 Release Notes 

 New Features 

 Updated on 

 Wed Jun 24 06:49:38 PDT 2026 

 Focus 

 Home 

 Cloud NGFW for Azure Release Notes 

 Cloud NGFW for Azure Addressed Issues 

 Download PDF 

 Cloud NGFW for Azure 

 Cloud NGFW for Azure Addressed Issues 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Cloud NGFW for Azure Docs 

 Getting Started 

 Deployment 

 Administration 

 Reference 

 Release Notes 

 New Features 

 Previous 

 What's New 

 Next 

 Cloud NGFW for Azure Known Issues 

 Cloud NGFW for Azure Addressed Issues 

 Cloud NGFW for AWS addressed issues. 

 The following issues have been addressed at this release of Cloud NGFW for Azure. 

 ID Description 

 PLUG-20294 

 The billing issue related to URL Logging is now fixed. To use
 logging-only functionality, you must now configure the URL filtering
 profiles to exclusively use custom URL categories , setting
 the action for these categories to alert to ensure logs are
 generated. All predefined categories within the profile must have
 their action set to allow. By following this specific configuration,
 you can now maintain full visibility of URL traffic, as required for
 comparison with other firewall services, without the associated
 Advanced URL Filtering billing, since the URL filtering license is
 only required for using and enforcing actions on predefined URL
 categories. 

 FWAAS-15572 

 In CNGFW Azure, the firewall may incorrectly allow all traffic, even
 when Layer 7 Rules (LRS) explicitly restrict specific ports. This
 occurs because the firewall is not correctly retrieving port
 information from the LRS, leading it to default to
 application-default for services instead of the
 configured allowed ports. Consequently, traffic intended for
 restricted ports (such as RDP when only port 443 is allowed) is
 permitted, effectively rendering the firewall unable to enforce
 granular port-based security policies. This issue happens only when
 modifying a rule from specific protocol to port to Application
 default or any. 

 FWAAS-12991 

 When deploying CNGFW on Azure, the Standard Load Balancer (SLB)
 limits SNAT port allocation to 1024 per instance, restricting the
 scaling with additional public IPs. This change yields 1600 SNAT
 ports per instance per IP, enabling proper outbound scaling,
 calculated as (64,000/40)×number of public IPs. 

 FWAAS-3919 

 It is observed that invalid rule names could be generated in Local
 Rulestacks that could cause commit failures. 

 FWAAS-4546 

 Rulehit counter DB entries are not deleted after deleting the rule,
 resulting in old values if a rule is created again with the same
 name. 

 FWAAS-4767 

 The DNS proxy does not update simultaneously on the firewall,
 following a firewall update call. 

 FWAAS-4805 

 Firewall host names are erroneously displayed in logs. 

 FWAAS-7430 

 If you try to delete a new Cloud NGFW resource before the creation is
 complete, the deletion fails. 

 FWAAS-7542 

 Panorama does not always automatically push content and antivirus
 updates to newly created Cloud NGFW for Azure resources. 

 FWAAS-8696 

 Log forwarding to a Panorama virtual appliance may take a long time
 to complete. 

 FWAAS-9041 

 Device server profiles (for example, LDAP, syslog) erroneously appear
 disabled in Panorama templates used for CNGFW devices. 

 FWAAS-9050 

 In some cases, a license on a VM-Series firewall may be removed from
 the Panorama virtual appliance. 

 FWAAS-9055 

 The CNGFW reaches an unhealthy state and loses connectivity to
 Panorama when the Cloud Device Group name is changed. 

 PAN-217460 

 Cloud NGFW resources managed by a Panorama HA pair might show
 disconnected on the secondary Panorama. However, on the primary
 Panorama, the Cloud NGFW resource shows connected. 

 Previous 

 What's New 

 Next 

 Cloud NGFW for Azure Known Issues 

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

 Public Cloud 

 Cloud NGFW for Azure 

 Microsoft Azure 

 Cloud 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
