---
url: https://docs.paloaltonetworks.com/saas-security/behavior-threats/cdug-integration
fetched_at: 2026-09-16T07:49:17Z
source: strata-and-sase
---

# Dynamic User Group Integration Clear

Updated on 

 Mon Jul 27 21:06:34 PDT 2026 

 Focus 

 Home 

 SaaS Security 

 Dynamic User Group Integration 

 Download PDF 

 SaaS Security 

 Dynamic User Group Integration 

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

 View Threat Incidents 

 Next 

 Audit Logging in Behavior Threats 

 Dynamic User Group Integration 

 Learn how Behavior Threats integrates with Cloud Identity Engine to enforce access
 controls through dynamic user groups based on user risk scores. 

 Where Can I Use This? What Do I Need? 

 Strata Cloud Manager 

 Data Security license 

 Or any of the following licenses that include the Data Security license: 

 CASB-X 

 CASB-PA 

 Behavior Threats integrates with Cloud Identity Engine (CIE) to provide real-time
 visibility into a user's dynamic user group (CDUG) membership directly from the user
 detail page. This integration allows you to tightly couple user risk scores with policy
 enforcement, turning Behavior Threats into an active zero trust enforcement engine rather
 than a passive detection tool. 

 CDUG Visibility 

 On the user detail page, you can view all CDUGs associated with the user in CIE. This
 gives you immediate context about which enforcement policies currently apply to a user
 based on their risk level, without needing to switch to a separate interface. 

 Managing CDUG Membership 

 For users who are not yet part of a CDUG-based enforcement flow, click Manage
 CDUG ( Risky User View Details page) to be redirected to CIE. From CIE,
 you can add a risk connection for Behavior Threats. After the risk connection is
 established, you can create risky user groups. 

 Set up Risk Connector Based on User Risk 

 Connect Behavior Threats as a risk source in
 CIE so that user risk data flows automatically into CIE for dynamic group
 enforcement. 

 Real-Time Sync on Score Reset 

 When you reset a user's risk score , the platform removes the user from their
 associated CDUG in near real-time. Users will be automatically removed or added to CDUG
 when meeting the criteria. If that CDUG is used in enforcement policies, those policies
 will apply only to the active users in the group. 

 This automated enforcement loop—where elevated risk scores place users into restrictive
 groups and score resets remove them—enables you to respond to insider threats immediately
 while maintaining the ability to restore access when investigations conclude. 

 Previous 

 View Threat Incidents 

 Next 

 Audit Logging in Behavior Threats
