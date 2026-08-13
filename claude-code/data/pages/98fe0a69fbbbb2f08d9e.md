---
url: https://docs.paloaltonetworks.com/saas-security/saas-security-inline/troubleshoot-issues-on-saas-security-inline
fetched_at: 2026-08-13T17:33:57Z
source: palo-alto-main
---

# Troubleshoot Issues on SaaS Security Inline Clear

Troubleshoot Issues on SaaS Security Inline 

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

 Troubleshoot Issues on SaaS Security Inline 

 Updated on 

 Tue May 26 10:16:10 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 SaaS Security Docs 

 Activation & Onboarding 

 Getting Started 

 Data Security 

 SaaS Security Inline 

 SSPM 

 Behavior Threats 

 New Features 

 Updated on 

 Tue May 26 10:16:10 PDT 2026 

 Focus 

 Home 

 SaaS Security 

 Troubleshoot Issues on SaaS Security Inline 

 Download PDF 

 SaaS Security 

 Troubleshoot Issues on SaaS Security Inline 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 SaaS Security Docs 

 Activation & Onboarding 

 Getting Started 

 Data Security 

 SaaS Security Inline 

 SSPM 

 Behavior Threats 

 New Features 

 Previous 

 Perform On Demand Scanning 

 Next 

 Onboard SaaS Apps Supported by SSPM 

 Troubleshoot Issues on SaaS Security Inline 

 Learn how to troubleshoot issues on SaaS Security Inline , including onboarding and
 licensing failures. 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by Panorama or Strata Cloud Manager) 

 Prisma Access (Managed by Panorama or Strata Cloud Manager) 

 SaaS Security Inline license 

 NGFW or Prisma Access license 

 Or any of the following licenses that include the SaaS Security Inline license: 

 CASB-X 

 CASB-PA 

 The issues you might encounter with SaaS Security Inline depend on your platform: 

 Troubleshoot Issues on SaaS Security Inline for Prisma Access (Managed by Strata Cloud Manager) 

 As you use SaaS Security Inline , you might encounter errors. The most common
 errors are related to a missing license. Policy management is a team effort: to
 avoid these errors, it’s imperative that all Prisma Access administrators verify
 licensing before using SaaS Security Inline and configure and manage SaaS
 policy rule recommendations with guidelines in mind. 

 Symptom 

 Explanation 

 Solution 

 New recommendations are not displaying in Prisma Access (Managed by Strata Cloud Manager) . 

 If the SaaS Security Inline license expires, the Prisma Access (Managed by Strata Cloud Manager) no longer pulls SaaS policy recommendations,
 so you can’t see new recommendations. However, SaaS policy
 recommendations that you already imported and applied as
 Security policy continue to work. 

 Renew your SaaS Security Inline license. 

 When your Web Security administrator attempts to import and
 commit a recommendation that uses a data profile, the operation
 fails with DLP profile is not a valid
 reference message. 

 The NGFW must have an Enterprise DLP license
 to have a valid SaaS policy rule recommendation that uses data
 profiles—even if you have an Enterprise DLP license on
 another platform. 

 The SaaS Security Team recommends one of the
 following options: 

 Buy an Enterprise DLP license. 

 Remove the data profile from the SaaS policy rule
 recommendation. 

 . 

 You have automatic
 updates enabled and an update to an existing rule
 recommendation fails. 

 When an update fails, Prisma Access (Managed by Strata Cloud Manager) retries every hour until
 the update succeeds. Such failures often correct themselves over
 the next polling cycle, when an ACE update occurs and new SaaS
 app signatures are made available to identify the SaaS apps
 identified in the rule recommendation. 

 Wait one hour, then click on the Last update failed
 link , and use the information provided to
 resolve the issue. 

 Troubleshoot Issues on SaaS Security Inline for NGFW 

 As you use SaaS Security Inline , you or your NGFW administrator
 might encounter errors if you inadvertently missed a step during SaaS Security Inline onboarding or ACE deployment . The most common errors are
 related to a missing license. Deployment is a team effort: to avoid these errors,
 it’s imperative that you work with your NGFW administrator to verify
 licensing before using SaaS Security Inline . In addition to the errors
 outlined below, there are other errors that display on the NGFW itself. 

 Symptom 

 Explanation 

 Solution 

 New recommendations are not are displayed in the NGFW web interface. 

 If the SaaS Security Inline license expires, the NGFW no longer pulls SaaS policy recommendations,
 so you cannot see new recommendations. However, SaaS policy
 recommendations that you already imported and applied as
 Security policy continue to work. 

 Renew your SaaS Security Inline license. 

 Can’t import recommendations that define specific SaaS apps. 

 If you disable ACE, the NGFW no longer receives
 new cloud application signatures and App-IDs and the NGFW cannot import SaaS policy recommendations
 based on new ACE App-IDs. 

 Re-enable ACE. 

 When you log in to your NGFW web interface,
 SaaS Security license is required for feature
 to function message displays in the
 footer. 

 The NGFW is missing the required SaaS Security Inline license. 

 After you activate, your NGFW administrator must
 retrieve the license
 keys from the license server. 

 When your NGFW administrator attempts to import
 and commit a recommendation that uses a data profile, the
 operation fails with Unknown data-filtering
 profile name message. 

 The NGFW must have an Enterprise DLP license
 to have a valid SaaS policy rule recommendation that uses data
 profiles—even if you have an Enterprise DLP license on
 another platform. 

 The SaaS Security Team recommends one of the following
 options: 

 Buy an Enterprise DLP license. 

 Remove the data profile from the SaaS policy rule
 recommendation. 

 Previous 

 Perform On Demand Scanning 

 Next 

 Onboard SaaS Apps Supported by SSPM 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Cloud Identity Engine 

 Strata Logging Service 

 Device Associations 

 Identity and Access Management 

 Tenant Management 

 Next-Generation Firewalls 

 AIOps for NGFW 

 Cloud Management for NGFWs 

 Firewalls 

 PAN-OS 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 Prisma Access Monitoring and Visibility 

 Next-Generation CASB 

 Cloud-Delivered Security Services 

 Advanced WildFire 

 Enterprise DLP 

 SaaS Security 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 SaaS Security Inline 

 SaaS Security 

 Administration 

 Cloud-Delivered Security Services 

 SaaS Security Inline 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
