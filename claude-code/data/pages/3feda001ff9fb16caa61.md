---
url: https://docs.paloaltonetworks.com/advanced-url-filtering/administration/configuring-url-filtering/get-started-with-url-filtering
fetched_at: 2026-08-13T15:18:31Z
source: palo-alto-main
---

# Get Started with URL Filtering Clear

Get Started with URL Filtering 

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

 Get Started with URL Filtering 

 Updated on 

 Thu Jul 30 16:45:14 PDT 2026 

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

 Advanced URL Filtering 

 Administration 

 Updated on 

 Thu Jul 30 16:45:14 PDT 2026 

 Focus 

 Home 

 Advanced URL Filtering 

 Configure URL Filtering 

 Get Started with URL Filtering 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Advanced URL Filtering 

 Get Started with URL Filtering 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Advanced URL Filtering 

 Administration 

 Previous 

 Activate Advanced URL Filtering License 

 Next 

 Configure URL Filtering 

 Get Started with URL Filtering 

 Basic setup for a URL filtering deployment that informs a more robust
 configuration 

 Where can I use
this? What do I need? 

 Prisma Access (Managed by Strata Cloud Manager) 

 Prisma Access (Managed by Panorama) 

 NGFW (Managed by Strata Cloud Manager) 

 NGFW (Managed by PAN-OS or Panorama) 

 Advanced URL Filtering (or a legacy
 URL filtering license) 

 Notes: 

 Legacy URL filtering licenses are discontinued,
 but active legacy licenses are still
 supported. 

 Prisma Access licenses include Advanced URL Filtering capabilities. 

 The first step to get started with URL filtering is understanding the web activity patterns of
 users on your network. 

 To safely observe these patterns, we recommend the following: 
 Review Palo Alto Networks predefined URL
 categories . 

 Enter URLs into our Test A Site engine to see how PAN-DB
 categorizes them. 

 Create a (mostly) passive URL Filtering profile that alerts on most
 categories. When you select the alert 
 setting for a URL category, the firewall logs traffic to that category.
 Then, you can see the sites your users are accessing and decide on the
 appropriate site access for URL categories and specific sites. 

 Alerting on all web activity might create a large number of log
 files. As a result, you might only want to do this as part of an
 initial deployment. At that time, you can also reduce URL filtering
 logs by enabling the Log container page only 
 option in the URL Filtering profile so only the main page that
 matches the category will be logged, not subsequent pages or
 categories that may be loaded within the container page. 

 Block URL categories that we know are bad: malware, command-and-control,
 and phishing. 

 Strata Cloud Manager 

 PAN-OS & Panorama 

 Get Started with Advanced URL Filtering ( Strata Cloud Manager ) 

 If you’re using Panorama to manage Prisma Access : 

 Toggle over to the PAN-OS & Panorama tab
and follow the guidance there. 

 If you’re using Strata Cloud Manager , continue here. 

 Use Test A Site to check how PAN-DB categorizes a
 specific website. 

 You can also use the platform to request a categorization change 
 for any website that you believe has been incorrectly categorized. 

 Create a passive URL Access Management profile that alerts on all
 categories. 

 The firewall generates a URL filtering log entry for websites in URL
 categories with an action other than allow . 

 Select Configuration NGFW and Prisma Access Security Services URL Access Management . 

 Under URL Access Management Profiles, select the checkbox next to the
 best-practices profile and then Clone the
 profile. 

 The cloned profile appears under the profiles with the name
 best-practices-1 . 

 Select the best-practices-1 profile and rename
 it. For example, rename it to
 url-monitoring . 

 Alert on all categories except
malware, command-and-control, and phishing, which should remain
blocked. 

 Under Access Control , select all categories,
 then exclude malware ,
 command-and-control , and
 phishing . 

 With the categories still highlighted, click Set Access and
choose Alert . 

 Block access to
 malware ,
 command-and-control , and
 phishing other known dangerous URL
 categories: 

 phishing 

 dynamic-dns 

 unknown 

 extremism 

 copyright-infringement 

 proxy-avoidance-and-anonymizers 

 newly-registered-domain 

 grayware 

 parked 

 Save the profile. 

 Apply the URL Access Management profile to Security policy rules that allow
 traffic from clients in the trust zone to the internet. 

 A URL Access Management Profile is only active when it’s included in a
 profile group that a Security policy rule references. 

 Follow the steps to activate a URL Access Management
 profile (and any Security profile). 

 Make sure the Source Zone in the Security
 policy rules you apply to URL Access Management profiles to is set to a
 protected internal network. 

 Push Config to commit the configuration. 

 Check the URL logs to see which website categories your users are accessing.
 Blocked websites are also logged. 

 For information on viewing the logs and generating reports, see Monitoring Web
 Activity . 

 Select Log
 Viewer and then the URL log type from
 the drop down. URL Filtering reports provide a view of web activity in a
 24-hour period. 

 Next Steps: 

 For everything that you don't allow or block, use risk
 categories to write policy rules based on website safety.
 PAN-DB categorizes every URL with a risk-level (high, medium, and
 low). While high and medium-risk sites are not confirmed malicious,
 they are closely associated with malicious sites. For example, they
 might be on the same domain as malicious sites or maybe they hosted
 malicious content until only very recently. 

 You can take precautionary measures
to limit your users’ interaction high-risk sites especially, as
there might be some cases where you want to give your users access
to sites that might also present safety concerns (for example, you
might want to allow your developers to use developer blogs for research,
yet blogs are a category known to commonly host malware). 

 Pair URL filtering with User-ID to control web
access based on organization or department and to block corporate
credential submissions to unsanctioned sites: 

 URL filtering prevents credential
 theft by detecting corporate credential
 submissions to sites based on the site category. Block users
 from submitting credentials to malicious and untrusted
 sites, warn users against entering corporate credentials on
 unknown sites or reusing corporate credentials on
 non-corporate sites, and explicitly allow users to submit
 credentials to corporate sites. 

 Add or update a Security policy rule with the passive URL
Access Management profile so that it applies to a department user
group, for example, Marketing or Engineering. Monitor
the department activity, and get feedback from department members
to understand the web resources that are essential to the work they
do. 

 Consider all the ways of leveraging
 URL filtering to reduce your attack surface. For example,
 a school may use URL filtering to enforce strict safe
 search for students. Or, if you have a security
 operations center, you might give only threat analysts password access 
 to compromised or dangerous sites for research. 

 Follow URL filtering best
practices . 

 Get Started with Advanced URL Filtering ( PAN-OS & Panorama ) 

 Follow these recommended practices for deploying Palo
Alto Networks URL filtering solution. 

 Use Test A Site to check how PAN-DB categorizes a
 specific website. 

 You can also use the platform to request a categorization change 
 for any website that you believe has been incorrectly categorized. 

 Create a passive URL Filtering profile that alerts on all
 categories. 

 Select Objects Security Profiles URL Filtering . 

 Select the default profile, and then click
 Clone . The new profile will be named
 default-1 . 

 Select the default-1 profile and rename it. For
 example, rename it to URL-Monitoring. 

 Configure the action for all categories to alert ,
except for malware, command-and-control, and phishing, which should
remain blocked. 

 In the section that lists all URL categories,
select all categories and then de-select malware, command-and-control,
and phishing. 

 To the right of the Action column heading, mouse
over and select the down arrow and then select Set Selected Actions and
choose alert . 

 Block access to known dangerous
URL categories. 

 Block access to malware, phishing,
dynamic-dns, unknown, command-and-control, extremism, copyright-infringement, proxy-avoidance-and-anonymizers,
newly-registered-domain, grayware, and parked URL categories. 

 Click OK to save the profile. 

 Apply the URL Filtering profile to Security policy rules
that allow traffic from clients in the trust zone to the Internet. 

 Make sure the Source Zone in the
Security policy rules you add URL Access Management profiles to
is set to a protected internal network. 

 Select Policies Security . Then, select a Security
policy rule to modify. 

 On the Actions tab, edit the
Profile Setting. 

 For Profile Type , select Profiles .
A list of profiles appears. 

 For URL Filtering profile,
select the profile you just created. 

 Click OK to save your changes. 

 Commit the configuration. 

 View the URL filtering logs to see all of the website
categories that your users are accessing. The categories you’ve
set to block are also logged. 

 For information on viewing the logs and generating reports,
see Monitoring Web
Activity . 

 Select Monitor Logs URL Filtering . A log entry will be created for any website that exists in
 the URL filtering database that is in a category set to any action other
 than allow . URL Filtering reports give you a view of
 web activity in a 24-hour period. ( Monitor Reports ). 

 Next Steps: 

 PAN-DB categorizes every URL with up to four categories, and every URL has a risk category (high,
 medium, and low). While high and medium-risk sites are not confirmed
 malicious, they are closely associated with malicious sites. For
 example, they might be on the same domain as malicious sites or
 maybe they hosted malicious content until only very recently. For
 everything that you do not allow or block, you can use risk categories to write
 simple policy rules based on website safety. 

 You
can take precautionary measures to limit your users’ interaction high-risk
sites especially, as there might be some cases where you want to
give your users access to sites that might also present safety concerns
(for example, you might want to allow your developers to use developer
blogs for research, yet blogs are a category known to commonly host
malware). 

 Pair URL filtering with User-ID to control web
access based on organization or department and to block corporate
credential submissions to unsanctioned sites: 

 URL
filtering prevents credential
theft by detecting corporate credential submissions to sites
based on the site category. Block users from submitting credentials
to malicious and untrusted sites, warn users against entering corporate
credentials on unknown sites or reusing corporate credentials on
non-corporate sites, and explicitly allow users to submit credentials
to corporate sites. 

 Add or update a Security policy rule with the passive URL
Filtering profile so that it applies to a department user group,
for example, Marketing or Engineering ( Policies Security User ). Monitor
the department activity, and get feedback from department members
to understand the web resources that are essential to the work they do. 

 Consider all the ways of leveraging
 URL filtering to reduce your attack surface. For example,
 a school may use URL filtering to enforce strict safe
 search for students. Or, if you have a security
 operations center, you might give only threat analysts password access 
 to compromised or dangerous sites for research. 

 Follow URL filtering best
practices . 

 Previous 

 Activate Advanced URL Filtering License 

 Next 

 Configure URL Filtering 

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

 IPSec VPN 

 Security Policy 

 Quantum Security 

 Endpoints 

 GlobalProtect 

 Remote Browser Isolation 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 11.0 

 10.1 

 Network Security 

 PAN-OS 

 10.2 

 11.1 

 Cloud-Delivered Security Services 

 Panorama 

 URL Filtering 

 Administration 

 Information Type 

 Prisma Access 

 Strata Cloud Manager 

 9.1 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
