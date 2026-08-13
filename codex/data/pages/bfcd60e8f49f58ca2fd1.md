---
url: https://docs.paloaltonetworks.com/saas-security/data-security/add-cloud-apps-to-saas-security-api/begin-scanning-a-cisco-webex-teams-app
fetched_at: 2026-08-13T17:32:51Z
source: palo-alto-main
---

# Begin Scanning a Cisco Webex Teams App Clear

Begin Scanning a Cisco Webex Teams App 

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

 Begin Scanning a Cisco Webex Teams App 

 Updated on 

 Mon Jul 06 09:36:54 PDT 2026 

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

 Mon Jul 06 09:36:54 PDT 2026 

 Focus 

 Home 

 SaaS Security 

 Data Security Administration 

 Onboard Sanctioned SaaS Apps to Data Security 

 Begin Scanning a Cisco Webex Teams App 

 Download PDF 

 SaaS Security 

 Begin Scanning a Cisco Webex Teams App 

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

 Begin Scanning ChatGPT Enterprise App 

 Next 

 Begin Scanning a Confluence App 

 Begin Scanning a Cisco Webex Teams App 

 Use these steps to connect your Cisco Webex Teams application
to Data Security . 

 Where Can I Use This? What Do I Need? 

 Strata Cloud Manager 

 Data Security license 

 Or any of the following licenses that include the Data Security license: 

 CASB-X 

 CASB-PA 

 Data Security scans messages and files shared on spaces within the Cisco Webex Teams
 application. Support for automated remediation capabilities varies by SaaS
 application. 

 Supported
 Content 

 Onboard Cisco Webex App to Data Security 

 Post Onboarding Procedures 

 Supported Content 

 The following table lists the supported content for
 the Cisco Webex app. 

 Support For 

 Details 

 Scan Content 

 Rooms, Messages, Files 

 Backward Scan 

 Yes 

 Forward Scan 

 Yes 

 Rescan 

 No 

 Selective Scan 

 No 

 User Activities 

 Activity Monitoring—No 

 Activity Alerting—No 

 Folder Monitoring—No 

 Remediation Actions 

 Change Sharing—No 

 User Quarantine—No 

 Admin Quarantine—No 

 Post-Remediation Actions (Actions after Admin
 Quarantine): 

 You can delete, restore, or download a quarantined file
 after performing a remediation action (for example
 quarantine or incident generation). 

 Delete—No 

 Restore—No 

 Download—No 

 Notifications 

 Notify File Owner—No 

 Notify Via Slack—Yes (applicable only if you have
 onboarded Slack Enterprise or Slack Pro and
 Business) 

 Exposure 

 Internal, External, Public 

 Snippet Support 

 Yes 

 Known License/Version restrictions 

 Supported Versions 

 Starter 

 Plus 

 Business 

 Enterprise (ensure you enable the Webex
 Events Admin option) 

 Caveats/Notes 

 None 

 Onboard Cisco Webex App to Data Security 

 Prerequisites to be completed on Cisco Webex
 Teams 

 Ensure that the Webex Teams account you plan to use with Data Security has sufficient privileges. 

 To connect a Webex Teams instance to Data Security , you
 must use a Webex Teams account with administrator
 privileges. 

 Log in to https://admin.webex.com, select Management Users admin_account_username Roles and Security . 

 Enable Full administrator and
 Compliance Officer privileges. 

 Ensure that you select the
 Compliance Officer role option.
 Otherwise, Data Security will not perform any scanning. 

 Make sure to request another administrator to assign the
 Compliance Officer role to you, so your account has the correct
 privileges required to search for sensitive information in the
 Cisco Webex Teams app. 

 The Webex Teams standard service plan supports data generated
 during the last 90 days. To enable longer-term visibility,
 consider upgrading to Cisco Webex Teams Pro Pack service
 plan before connecting to Data Security . 

 Add Cisco Webex Teams to Data Security 

 Log in to 
 Strata Cloud Manager . 

 Select Configuration SaaS Security Data Security Applications Add Application Cisco Webex Teams . 

 Click Connect to Connect Cisco
 Webex Teams to Data Security . 
 Data Security redirects you to a Cisco identity broker to
 authorize access so that you can enter the email address and
 password for the administrator account you want to use when
 connecting to the Webex Teams application. 

 Select View Onboarding Status to view the
 onboarded Webex app instance. 

 The new Webex Teams instance is added to the list of Cloud Apps
 as Webex Teams  n, where n is the
 number of Webex Teams instances you have connected to Data Security . For example, if this is the second Webex
 Teams instance you connected to Data Security , the name
 displays as Webex Teams2. 

 Post Onboarding Procedures 

 Define Global Scan Settings 

 Define Your Internal
 Domain When you add the Webex bot, Data Security automatically adds
 webex.bot to the list of internal
 domains to restrict the bot activity to the internal domain.
 Don't delete this entry from the list. 

 Define Untrusted Users and
 Domains 

 Enable Data Masking 

 Add Policy Rules or Edit Existing Policy Rules 
 When you add a new cloud application, Data Security automatically
 scans assets against the default data patterns and displays the match
 occurrences. If you want to generate incidents and identify potential issues
 that are unique to the new instance, as a best practice, consider the
 business use of your app to determine whether you want to Add a New Data Asset Policy Rule . 

 ( Optional ) Configure or Edit Data
 Patterns 

 If you find the existing data patterns don't identify the incidents you
 want to prevent from occurring, you can Configure Data Patterns to
 identify specific strings of text, characters, words, or patterns to
 make it possible to find all instances of text that match a data pattern
 you specify. 

 Start Scanning Cisco Webex Teams for Risks 

 Data Security starts scanning all assets—files, messages—and
 spaces in the associated Webex Teams application and identifies
 incidents. Depending on the number of Webex Teams users and assets, it
 might take some time for the service to complete the process. However,
 as soon as you begin to see this information populating on the
 Dashboard , you can begin to Assess Incidents on Data Security . To
 start scanning the Cisco Webex Teams instance for issues, select Configuration SaaS Security Data Security Applications Cisco Webex Teams View Settings ... Start Scanning . 

 On a Webex Teams account, Data Security monitors the
 following activities. However, activities that occurred
 before you added the Cisco Webex Teams application to Data Security are not displayed on Data Security Users & Activity User Activities . 

 Adding or removing a user from a space. 

 Adding a moderator to a space. 

 Deleting a message — the deletion of a message is logged if the
 message had a file attached to it, or if the message had a
 policy violation and created an incident. 

 Monitor Scan Results 

 As Data Security scans files and matches them against enabled
 policy rules, you can refer to the Monitor Scan Results on the Dashboard 
 section to verify that your policy rules are effective. Monitoring the
 progress of the scan during the discovery phase allows you to Fine-Tune Policy to modify
 the match criteria and ensure better results. 

 Previous 

 Begin Scanning ChatGPT Enterprise App 

 Next 

 Begin Scanning a Confluence App 

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

 SaaS Security 

 Cloud-Delivered Security Services 

 Data Security 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
