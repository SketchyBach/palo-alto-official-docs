---
url: https://docs.paloaltonetworks.com/saas-security/saas-security-inline/identify-risky-saas-apps
fetched_at: 2026-08-13T17:33:53Z
source: palo-alto-main
---

# Identify Risky Unsanctioned SaaS Apps and Users Clear

Identify Risky Unsanctioned SaaS Apps and Users 

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

 Identify Risky Unsanctioned SaaS Apps and Users 

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

 Identify Risky Unsanctioned SaaS Apps and Users 

 Download PDF 

 SaaS Security 

 Identify Risky Unsanctioned SaaS Apps and Users 

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

 How SaaS Security Inline Determines an App's Risk Score 

 Next 

 Generate the SaaS Security Report 

 Identify Risky Unsanctioned SaaS Apps and Users 

 Learn how to identify and remediate risky apps on SaaS Security Inline . 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by Panorama or Strata Cloud Manager) 

 Prisma Access (Managed by Panorama or Strata Cloud Manager) 

 SaaS Security Inline license 

 NGFW or Prisma Access license 

 Or any of the following licenses that include the SaaS Security Inline license: 

 CASB-X 

 CASB-PA 

 SaaS Security Inline provides tools to help you identify risky SaaS apps and users,
 including analytics, risk scores, and reports. After you identify your
 organization’s risks, you have the following solutions to increase your security
 posture: 

 Author and
submit SaaS security policy rule recommendations to address the
risks. However, before you do so, consider some guidelines . 

 Identify a competing product that’s more secure. Search the Application Dictionary by Category to
find a suitable replacement. 

 Notify users of the unsanctioned app to use the alternative, sanctioned app. Don’t forget to
 tag the sanctioned SaaS
 app. 

 Change the
risk score. 

 Identify opportunities to develop training for employees and
internal policies. 

 Identify Risky SaaS Users 

 Although Discovered Users , displays your list of users that are using discovered SaaS apps,
 not all of those uses are risky. You’ll need to observe the users in the context
 of the risky SaaS apps and overall app usage (MB). For example, if you find 100
 users using WeTransfer but only a few people are uploading large amounts of
 data, those users are likely risky users and require more scrutiny. 

 Log in to 
 Strata Cloud Manager . 

 Select Configuration SaaS Security Applications . 

 Filter on SaaS apps with
 a risk score of 4 or 5. 

 Do one of the following: 

 Click on the individual SaaS apps. 

 Click on the number of users for the SaaS apps. 

 Sort the column by Usage . 

 Identify Risky SaaS Apps 

 A risk score in SaaS Security Inline enables you to make decisions about the
 security posture of a given app. The
 risk score is between 1 (low risk) and 5 (high risk) and is based on compliance
 attributes . 
 Key attributes have a higher impact on the score:
 the score is assigned by applying different weights to each compliance attribute
 and calculating the score based on whether the app meets those compliance
 standards. 

 Log in to 
 Strata Cloud Manager . 

 Select Configuration SaaS Security Discovered Apps Applications . 

 To navigate to the Discovered Applications view, select . 

 Sort the table by Risk in descending
order. 

 Observe the Risk score for each SaaS app in the
 High risk category. 

 Risk Score 

 Description 

 4-5 

 High Risk — Very likely to be a risk. 

 3 

 Medium Risk — Moderate risk. 

 1-2 

 Low Risk — Unlikely to be a risk. 

 Open the Application Detail for the SaaS app
 to assess the risk characteristics (compliance attributes) that contribute
 to this risk score. 

 Previous 

 How SaaS Security Inline Determines an App's Risk Score 

 Next 

 Generate the SaaS Security Report 

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
