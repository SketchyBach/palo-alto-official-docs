---
url: https://docs.paloaltonetworks.com/enterprise-dlp/administration/configure-enterprise-dlp/email-dlp/onboard-microsoft-exchange-online/obtain-your-microsoft-exchange-domain-and-relay-host
fetched_at: 2026-09-15T15:10:21Z
source: palo-alto-main
---

# Obtain Your Microsoft Exchange Domain and Relay Host Clear

Updated on 

 Sep 10, 2026 

 Focus 

 Home 

 Enterprise DLP 

 Administration 

 Configure Enterprise DLP 

 Email DLP 

 Onboard Microsoft Exchange Online 

 Obtain Your Microsoft Exchange Domain and Relay Host 

 Download PDF 

 Enterprise DLP 

 Obtain Your Microsoft Exchange Domain and Relay Host 

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

 Create Microsoft Exchange Transport Rules 

 Next 

 Onboard Gmail 

 Obtain Your Microsoft Exchange Domain and Relay Host 

 Obtain your Microsoft Exchange domain and relay host to connect Microsoft
 Exchange to Enterprise Data Loss Prevention (E-DLP) . 

 Where Can I Use This? What Do I Need? 

 Data Security 

 One of the following licenses that include the Enterprise DLP license 

 Review the Supported
 Platforms for details on the required license
 for each enforcement point. 

 Prisma Access CASB license 

 Next-Generation
CASB for Prisma Access and NGFW (CASB-X) license 

 Data Security license 

 Email DLP license 

 You must obtain your Microsoft Exchange domain and relay host to connect Microsoft
 Exchange and Enterprise Data Loss Prevention (E-DLP) for inline inspection and prevention of
 sensitive data exfiltration contained in outbound emails. 

 Log in
 to the Microsoft Office 365 Admin Portal . 

 Select Settings Domains . 

 Make note of the Microsoft Exchange domains listed in the Domain
 name list. 

 Enterprise DLP supports inline inspection of emails from multiple
 domains. If you use multiple Microsoft Exchange domains, make sure to make
 note of all email domains for which you want inline inspection of
 emails. 

 Obtain the relay host for the Microsoft Exchange domain. 

 Repeat this step for all Microsoft Exchange domains you want to connect to
 Enterprise DLP . 

 Click the Microsoft Exchange domain. 

 Select DNS records . 

 In the Microsoft Exchange section, locate
 the MX record. 

 The Value column for the MX record lists
 the relay host for the domain. An example of a relay host is shown
 below. 

 The MX record displays a 0 before
 the relay host. This character is not required to connect
 Microsoft Exchange to Enterprise DLP . 

 Previous 

 Create Microsoft Exchange Transport Rules 

 Next 

 Onboard Gmail
