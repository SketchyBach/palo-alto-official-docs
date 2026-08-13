---
url: https://docs.paloaltonetworks.com/enterprise-dlp/administration/configure-enterprise-dlp/create-an-enterprise-dlp-data-profile/archive-and-restore-a-data-profile
fetched_at: 2026-08-13T15:32:11Z
source: palo-alto-main
---

# Archive and Restore a Data Profile Clear

Archive and Restore a Data Profile 

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

 Archive and Restore a Data Profile 

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

 Data Profiles 

 Archive and Restore a Data Profile 

 Download PDF 

 Enterprise DLP 

 Archive and Restore a Data Profile 

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

 Test a Data Profile 

 Next 

 Resolve Data Profile Synchronization Conflicts 

 Archive and Restore a Data Profile 

 Archive and restore your custom Enterprise Data Loss Prevention (E-DLP) data profiles to reduce
 configuration sprawl. 

 On May 7, 2025 , Palo Alto Networks is introducing new Evidence Storage and Syslog Forwarding service IP
 addresses to improve performance and expand availability for these services
 globally. 

 You must allow these new service IP addresses on your network
 to avoid disruptions for these services. Review the Enterprise DLP 
 Release Notes for more
 information. 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by Strata Cloud Manager) 

 Prisma Access (Managed by Strata Cloud Manager) 

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

 Effective data loss prevention requires continuous adaptation to evolving data
 security needs. You can archive and restore your custom Enterprise Data Loss Prevention (E-DLP) 
 data profiles to eliminate configuration sprawl, reduce administrative overhead,
 and maintain an optimized data protection strategy. 

 Before you can archive a data profile, you must remove the data profile from
 all active Security policy rules across inline Enterprise DLP , Email DLP,
 Endpoint DLP, Data Security (SaaS API), SaaS Security Inline , Prisma Browser , and Prisma AIRS . If the data profile is
 currently in use, Enterprise DLP identifies the active policy rules using the
 data profile and provides direct links so you can update them before archiving. Once
 archived, the data profile can't be referenced in any new Security policy rule
 across any product unless you restore it. You can't archive predefined data
 profiles. Archiving a data profile doesn't affect historical data logs or past
 enforcement actions. 

 You can restore an archived data profile to return it to active status and
 make it available for policy configuration again. During restoration, you must
 provide a unique name if the original data profile name is already in use. 

 Enterprise DLP generates an audit log when you archive or
 restore a data profile. The audit log captures the user who performed the action,
 the affected data profile, and the timestamp. 

 Enterprise DLP doesn't support data profile archive and restore, and won't
 display the Archive and Restore 
 buttons, if your tenant has a Panorama® management server associated with it even if
 you manage your Enterprise DLP explicitly from Strata Cloud Manager . 

 Archive 

 Restore 

 Archive a Data Profile 

 Archive a custom Enterprise Data Loss Prevention (E-DLP) data profile that is no longer
 required. 

 Log in to 
 Strata Cloud Manager . 

 Create a data profile if you don't
 already have a custom data profile to archive. 

 Enterprise DLP doesn't support archiving a predefined data profile. 

 Select Configuration Data Loss Prevention Data Profiles . 

 ( Optional ) In the Active data profiles, apply
 any filters or search for the data profile you want to archive. 

 Expand the Action menu and
 Archive the data profile. 

 You can archive one data profile at a time. 

 Resolve any data profile in-use errors preventing archival. 

 Skip this step and confirm the archival if the data profile you selected
 isn't in use and there are no errors to resolve. 

 Enterprise DLP prompts you if the data profile you want to archive is
 currently referenced in one or more active Security policy rules or by other
 custom data profiles (nested or granular). Enterprise DLP provides
 hyperlinks to the Security policy rules so you can quickly update them as
 needed. 

 After removing the data profile from all active Security policy rules and
 resolving any nested data profile dependencies, select Configuration Data Loss Prevention Data Profiles and expand the Action menu to
 Archive the data profile. 

 You're prompted to confirm archiving the data profile. Click
 Archive to confirm. 

 Archiving the data profile doesn't impact existing DLP incidents or audit logs . 

 It can take up to 10 minutes for the archived status to take effect in
 profile group menus ( Configuration NGFW and Prisma Access Security Services Profile Groups ). During this time, the archived data profile might still
 appear as an available selection in the Data Loss Prevention
 Profile dropdown when you configure a profile group. 

 Enterprise DLP confirms that it successfully archived the data profile. 

 Click Archived to view the list of archived data
 profiles. 

 Restore a Data Profile 

 Restore an archived Enterprise Data Loss Prevention (E-DLP) data profile to return it to active
 status. 

 Log in to 
 Strata Cloud Manager . 

 Archive a custom data profile. 

 Select Configuration Data Loss Prevention Data Profiles and select Archived . 

 ( Optional ) Apply any filters or search for the data profile you want
 to restore. 

 Locate the data profile you want to restore and expand the
 Action menu to Restore the
 data profile. 

 You can restore one data profile at a time. 

 You're prompted to confirm restoring the data profile. Click
 Restore to confirm. 

 Enterprise DLP confirms that it successfully restored the data profile. 

 View your Active data profiles and verify that Enterprise DLP successfully restored the data profile. 

 Remove any search terms if you filtered your
 Archived data profiles using a search
 filter. 

 Previous 

 Test a Data Profile 

 Next 

 Resolve Data Profile Synchronization Conflicts 

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

 © 2026 Palo Alto Networks, Inc. All rights reserved.
