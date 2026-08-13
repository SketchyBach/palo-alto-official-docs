---
url: https://docs.paloaltonetworks.com/enterprise-dlp/administration/configure-enterprise-dlp/enterprise-dlp-end-user-alerting-with-cortex-xsoar/set-up-the-enterprise-dlp-end-user-alerting-with-cortex-xsoar
fetched_at: 2026-08-13T15:32:17Z
source: palo-alto-main
---

# Set Up Enterprise DLP End User Alerting with Cortex XSOAR Clear

Set Up Enterprise DLP End User Alerting with Cortex XSOAR 

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

 Set Up Enterprise DLP End User Alerting with Cortex XSOAR 

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

 Enterprise DLP End User Alerting with Cortex XSOAR 

 Set Up Enterprise DLP End User Alerting with Cortex XSOAR 

 Download PDF 

 Enterprise DLP 

 Set Up Enterprise DLP End User Alerting with Cortex XSOAR 

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

 About Enterprise DLP End User Alerting with Cortex XSOAR 

 Next 

 Respond to Blocked Traffic Using Enterprise DLP End User Alerting with Cortex XSOAR 

 Set Up Enterprise DLP End User Alerting with Cortex XSOAR 

 Set up Cortex XSOAR to use Enterprise Data Loss Prevention (E-DLP) End User
 Alerting. 

 On May 7, 2025 , Palo Alto Networks is introducing new Evidence Storage and Syslog Forwarding service IP
 addresses to improve performance and expand availability for these services
 globally. 

 You must allow these new service IP addresses on your network
 to avoid disruptions for these services. Review the Enterprise DLP 
 Release Notes for more
 information. 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by Panorama or Strata Cloud Manager) 

 Prisma Access (Managed by Panorama or Strata Cloud Manager) 

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

 Integrate Enterprise Data Loss Prevention (E-DLP) with Cortex XSOAR to use
 the Enterprise DLP End User Alerting. 

 ( Slack ) To set up Enterprise Data Loss Prevention (E-DLP) End User Alerting with Cortex XSOAR and set up automatic Slack alerts, you need to
 integrate your preferred IP address directory service to map IP addresses to
 emails to allow for automatic messages to be sent on Slack. After
 integration, you must enable Slack, email send integration, and Enterprise DLP with Cortex XSOAR . This chain of integration
 allows the DLP cloud service to automate sending Slack messages to team
 members who upload a file that matches your data profiles. 

 ( Microsoft Teams ) To set up Enterprise Data Loss Prevention (E-DLP) End User Alerting
 with Cortex XSOAR and set up automatic Microsoft Teams alerts, you
 need to set up integration with Microsoft Teams and Enterprise DLP with
 Cortex XSOAR . This is integration allows the DLP cloud
 service to automate sending Microsoft Teams messages to team members who
 upload a file that matches your data profiles. 

 ( Email ) To set up Enterprise Data Loss Prevention (E-DLP) End User Alerting with Cortex XSOAR and set up automatic email alerts, you need to
 integrate your preferred IP address directory service and Enterprise DLP with Cortex XSOAR . This is integration allows the DLP cloud
 service to automate sending email messages to team members who upload a file
 that matches your data profiles. 

 After you successfully integrate Slack, Microsoft Teams, or your Email provider
 and Enterprise DLP with Cortex XSOAR , you need to enable End
 User Alerting with Cortex XSOAR functionality on Strata Cloud Manager and configure the End User Alerting settings as needed. 

 Slack 

 Microsoft Teams 

 Email 

 Slack 

 Set up Cortex XSOAR to use Enterprise Data Loss Prevention (E-DLP) End User Alerting for
 Slack. 

 Integrate your preferred IP address directory service using one of the
 following procedures. 

 Integrate AWS - Identity and Access Management 

 Integrate MSGraphAzure
 Users 

 Integrate Okta v2 

 Integrate PingOne 

 Integrate SailPoint
 IdentityIQ 

 Integrate SailPoint
 IdentityNow 

 Enable Slack Integration with
XSOAR . 

 Configure Enterprise DLP authentication. 

 Strata Cloud Manager and Prisma Access (Managed by Panorama) 
 (TSG-enabled) 

 Access the Common Services Identity and
 & Access settings and add a Service Account to
 generate the Client ID and
 Client Secret . 

 If you already have a Service Account created, you can Reset Client Secret to
 recover a lost Client Secret . 

 The Client ID and Client
 Secret are used for authentication. 

 When you create the Service Account, the Client
 ID and Client Secret 
 are displayed in the Client Credentials . You
 can manually copy the Client Credentials or Download CSV
 File to download the Client Credentials in plaintext
 locally to your device. 

 Panorama (Not TSG-enabled) 

 Log in to the DLP app on the
 hub . 

 If you don’t already have access to the DLP app on the hub,
 see the hub Getting Started
 Guide . Only Superusers can access the hub. 

 Select API and Create
 Token . 

 Enter a descriptive Token Name and
 Create the access token. 

 Copy the Access Token and
 Refresh Token and save them in a
 secure location. 

 Enable Enterprise DLP on Cortex XSOAR . 

 Strata Cloud Manager and Prisma Access (Managed by Panorama) 
 (TSG-enabled) 

 Add the Client Credentials to Cortex XSOAR . 
 On Cortex XSOAR , select Settings Integrations Credentials and add a New 
 credential. 

 Enter a descriptive Credential
 Name . 

 For the Username , enter
 the Client ID created in
 the previous step. 

 For the Password , enter
 the Client Secret created
 in the previous step. 

 Save . 

 Select Marketplace Browse and search for Enterprise DLP . 

 Install the Enterprise DLP 
 content pack. 

 Select Settings Integrations Instances and search for Enterprise
 DLP . 

 Click Add Instance to integrate Enterprise DLP . See Integrate Enterprise DLP
 on XSOAR for more information. 

 Select a descriptive Name . 

 For the Incident Type, verify Data Loss
 Prevention is selected. 
 If
 Data Loss Prevention is not
 displayed, hover your mouse over the field to
 display the list of available incident types to
 search for and select Data Loss
 Prevention . 

 for the Mapper , verify that
 Data Loss Prevention is
 selected. 

 If Data Loss Prevention is not
 displayed, hover your mouse over the field to
 display the list of available incident types to
 search for and select Data Loss
 Prevention . 

 Click Switch to
 credentials . 

 Enter the Client Credentials generated in the
 previous step. 

 Check (enable) Long running
 instance . 

 ( Optional) Modify the automated
 Slack Bot Message . 

 Test to confirm Cortex XSOAR has successfully integrated with
 Enterprise DLP . 
 A
 Success is displayed
 when Cortex XSOAR successfully integrates
 with Enterprise DLP . 

 Panorama (Not TSG-enabled) 

 On Cortex XSOAR , select Marketplace Browse and search for Enterprise DLP . 

 Install the Enterprise DLP 
 content pack. 

 Select Settings Integrations Instances and search for Enterprise
 DLP . 

 Click Add Instance to integrate Enterprise DLP . See Integrate Enterprise DLP
 on XSOAR for more information. 

 Select a descriptive Name . 

 For the Incident Type, verify Data Loss
 Prevention is selected. 
 If
 Data Loss Prevention is not
 displayed, hover your mouse over the field to
 display the list of available incident types to
 search for and select Data Loss
 Prevention . 

 for the Mapper , verify that
 Data Loss Prevention is
 selected. 

 If Data Loss Prevention is not
 displayed, hover your mouse over the field to
 display the list of available incident types to
 search for and select Data Loss
 Prevention . 

 Add the Access Token and
 Refresh Token you created in
 the previous step. 

 Check (enable) Long running
 instance . 

 ( Optional) Modify the automated
 Slack Bot Message . 

 Test to confirm Cortex XSOAR has successfully integrated with
 Enterprise DLP . 
 A
 Success is displayed
 when Cortex XSOAR successfully integrates
 with Enterprise DLP . 

 Configure the DLP Incident Feedback Loop Cortex XSOAR playbook 

 In Dashboard & Reports, select
 Playbooks . 

 Select DLP Incident Feedback Loops Playbook Triggered . 

 Configure the Cortex XSOAR playbook. 

 For ApprovalTarget , enter
 Manager to send an exemption
 request to the sender's manager. This information is pulled
 from your preferred IP address directory service. 

 For the UserMessageApp , verify
 Slack is displayed. 

 For the ApproverMessageApp ,
 enter Slack . 

 ( Optional ) For the
 DenyMessage , enter a custom
 response when a file extension is denied by the sender's
 manager, 

 Save . 

 Confirm the Cortex XSOAR integration with Enterprise DLP . 

 Log in to 
 Strata Cloud Manager . 

 Select Configuration Data Loss Prevention Settings Alerts XSOAR Integration Setup and expand the Setup Instructions 
 section. 

 Toggle the Confirm the status for XSOAR
 Integration setting to On . 

 Expand the Configuration section to define the
 Exemption Duration for exempted files that prompt the
 End User Alerting with Cortex XSOAR notification. 
 This setting defines how long a specific file is granted an block exemption
 when your administrator responds to blocked traffic .
 The default is 12 hours. 

 Microsoft Teams 

 Set up Cortex XSOAR to use Enterprise Data Loss Prevention (E-DLP) End User Alerting for
 Microsoft Teams. 

 Set up the prerequisites needed to begin integrating Microsoft Teams with Cortex XSOAR . 

 Integrate referred IP address directory service using one of the
 following procedures. 

 Integrate AWS - Identity and Access
 Management 

 Integrate MSGraphAzure
 Users 

 Integrate Okta v2 

 Integrate PingOne 

 Integrate SailPoint
 IdentityIQ 

 Integrate SailPoint
 IdentityNow 

 Create the Demisto Bot in Microsoft
 Teams . 

 Grant the Demisto Bot Permissions in
 Microsoft Graph . 

 Configure Microsoft Teams on . 

 Add the Demisto Bot to a
 Team . 

 Integrate Microsoft Teams with Cortex XSOAR . 

 You can use one of the following methods based on your preferences. 

 Using 

 Using NGINX as Reverse
 Proxy 

 Using Apache Reverse Proxy and

 Using Cloudflare 

 Configure Enterprise DLP authentication. 

 Strata Cloud Manager and Prisma Access (Managed by Panorama) 
 (TSG-enabled) 

 Access the Common Services Identity and
 & Access settings and add a Service Account to
 generate the Client ID and
 Client Secret . 

 If you already have a Service Account created, you can Reset Client Secret to
 recover a lost Client Secret . 

 The Client ID and Client
 Secret are used for authentication. 

 When you create the Service Account, the Client
 ID and Client Secret 
 are displayed in the Client Credentials . You
 can manually copy the Client Credentials or Download CSV
 File to download the Client Credentials in plaintext
 locally to your device. 

 Panorama (Not TSG-enabled) 

 Log in to the DLP app on the
 hub . 

 If you don’t already have access to the DLP app on the hub,
 see the hub Getting Started
 Guide . Only Superusers can access the hub. 

 Select API and Create
 Token . 

 Enter a descriptive Token Name and
 Create the access token. 

 Copy the Access Token and
 Refresh Token and save them in a
 secure location. 

 Enable Enterprise DLP on Cortex XSOAR . 

 Strata Cloud Manager and Prisma Access (Managed by Panorama) 
 (TSG-enabled) 

 Add the Client Credentials to Cortex XSOAR . 
 On Cortex XSOAR , select Settings Integrations Credentials and add a New 
 credential. 

 Enter a descriptive Credential
 Name . 

 For the Username , enter
 the Client ID created in
 the previous step. 

 For the Password , enter
 the Client Secret created
 in the previous step. 

 Save . 

 Select Marketplace Browse and search for Enterprise DLP . 

 Install the Enterprise DLP 
 content pack. 

 Select Settings Integrations Instances and search for Enterprise
 DLP . 

 Click Add Instance to integrate Enterprise DLP . See Integrate Enterprise DLP
 on XSOAR for more information. 

 Select a descriptive Name . 

 For the Incident Type, verify Data Loss
 Prevention is selected. 
 If
 Data Loss Prevention is not
 displayed, hover your mouse over the field to
 display the list of available incident types to
 search for and select Data Loss
 Prevention . 

 for the Mapper , verify that
 Data Loss Prevention is
 selected. 

 If Data Loss Prevention is not
 displayed, hover your mouse over the field to
 display the list of available incident types to
 search for and select Data Loss
 Prevention . 

 Click Switch to
 credentials . 

 Enter the Client Credentials generated in the
 previous step. 

 Check (enable) Long running
 instance . 

 Test to confirm Cortex XSOAR has successfully integrated with
 Enterprise DLP . 
 A
 Success is displayed
 when Cortex XSOAR successfully integrates
 with Enterprise DLP . 

 Panorama (Not TSG-enabled) 

 On Cortex XSOAR , select Marketplace Browse and search for Enterprise DLP . 

 Install the Enterprise DLP 
 content pack. 

 Select Settings Integrations Instances and search for Enterprise
 DLP . 

 Click Add Instance to integrate Enterprise DLP . See Integrate Enterprise DLP
 on XSOAR for more information. 

 Select a descriptive Name . 

 For the Incident Type, verify Data Loss
 Prevention is selected. 
 If
 Data Loss Prevention is not
 displayed, hover your mouse over the field to
 display the list of available incident types to
 search for and select Data Loss
 Prevention . 

 for the Mapper , verify that
 Data Loss Prevention is
 selected. 

 If Data Loss Prevention is not
 displayed, hover your mouse over the field to
 display the list of available incident types to
 search for and select Data Loss
 Prevention . 

 Add the Access Token and
 Refresh Token you created in
 the previous step. 

 Check (enable) Long running
 instance . 

 ( Optional) Modify the automated
 Slack Bot Message . 

 Test to confirm Cortex XSOAR has successfully integrated with
 Enterprise DLP . 
 A
 Success is displayed
 when Cortex XSOAR successfully integrates
 with Enterprise DLP . 

 Configure the DLP Incident Feedback Loop Cortex XSOAR playbook 

 In Dashboard & Reports, select
 Playbooks . 

 Select DLP Incident Feedback Loops Playbook Triggered . 

 Configure the Cortex XSOAR playbook. 

 For ApprovalTarget , enter
 Manager to send an exemption
 request to the sender's manager. This information is pulled
 from your preferred IP address directory service. 

 For the UserMessageApp , verify
 Microsoft Teams is displayed. 

 For the ApproverMessageApp ,
 enter Microsoft Teams . 

 ( Optional ) For the
 DenyMessage , enter a custom
 response when a file extension is denied by the sender's
 manager, 

 Save . 

 Confirm the Cortex XSOAR integration with Enterprise DLP . 

 Log in to 
 Strata Cloud Manager . 

 Select Configuration Data Loss Prevention Settings Alerts XSOAR Integration Setup and expand the Setup Instructions 
 section. 

 Toggle the Confirm the status for XSOAR
 Integration setting to On . 

 Expand the Configuration section to define the
 Exemption Duration for exempted files that prompt the
 End User Alerting with Cortex XSOAR notification. 
 This setting defines how long a specific file is granted an block exemption
 when your administrator responds to blocked traffic .
 The default is 12 hours. 

 Email 

 Set up Cortex XSOAR to use Enterprise Data Loss Prevention (E-DLP) End User Alerting for
 Email. 

 Integrate referred IP address directory service using one of the following
 procedures. 

 Integrate AWS - Identity and Access Management 

 Integrate MSGraphAzure
 Users 

 Integrate Okta v2 

 Integrate PingOne 

 Integrate SailPoint
 IdentityIQ 

 Integrate SailPoint
 IdentityNow 

 Enable Mail Send Integration with Cortex
 XSOAR . 

 Configure Enterprise DLP authentication. 

 Strata Cloud Manager and Prisma Access (Managed by Panorama) 
 (TSG-enabled) 

 Access the Common Services Identity and
 & Access settings and add a Service Account to
 generate the Client ID and
 Client Secret . 

 If you already have a Service Account created, you can Reset Client Secret to
 recover a lost Client Secret . 

 The Client ID and Client
 Secret are used for authentication. 

 When you create the Service Account, the Client
 ID and Client Secret 
 are displayed in the Client Credentials . You
 can manually copy the Client Credentials or Download CSV
 File to download the Client Credentials in plaintext
 locally to your device. 

 Panorama (Not TSG-enabled) 

 Log in to the DLP app on the
 hub . 

 If you don’t already have access to the DLP app on the hub,
 see the hub Getting Started
 Guide . Only Superusers can access the hub. 

 Select API and Create
 Token . 

 Enter a descriptive Token Name and
 Create the access token. 

 Copy the Access Token and
 Refresh Token and save them in a
 secure location. 

 Enable Enterprise DLP on Cortex XSOAR . 

 Strata Cloud Manager and Prisma Access (Managed by Panorama) 
 (TSG-enabled) 

 Add the Client Credentials to Cortex XSOAR . 
 On Cortex XSOAR , select Settings Integrations Credentials and add a New 
 credential. 

 Enter a descriptive Credential
 Name . 

 For the Username , enter
 the Client ID created in
 the previous step. 

 For the Password , enter
 the Client Secret created
 in the previous step. 

 Save . 

 Select Marketplace Browse and search for Enterprise DLP . 

 Install the Enterprise DLP 
 content pack. 

 Select Settings Integrations Instances and search for Enterprise
 DLP . 

 Click Add Instance to integrate Enterprise DLP . See Integrate Enterprise DLP
 on XSOAR for more information. 

 Select a descriptive Name . 

 For the Incident Type, verify Data Loss
 Prevention is selected. 
 If
 Data Loss Prevention is not
 displayed, hover your mouse over the field to
 display the list of available incident types to
 search for and select Data Loss
 Prevention . 

 for the Mapper , verify that
 Data Loss Prevention is
 selected. 

 If Data Loss Prevention is not
 displayed, hover your mouse over the field to
 display the list of available incident types to
 search for and select Data Loss
 Prevention . 

 Click Switch to
 credentials . 

 Enter the Client Credentials generated in the
 previous step. 

 Check (enable) Long running
 instance . 

 Test to confirm Cortex XSOAR has successfully integrated with
 Enterprise DLP . 
 A
 Success is displayed
 when Cortex XSOAR successfully integrates
 with Enterprise DLP . 

 Panorama (Not TSG-enabled) 

 On Cortex XSOAR , select Marketplace Browse and search for Enterprise DLP . 

 Install the Enterprise DLP 
 content pack. 

 Select Settings Integrations Instances and search for Enterprise
 DLP . 

 Click Add Instance to integrate Enterprise DLP . See Integrate Enterprise DLP
 on XSOAR for more information. 

 Select a descriptive Name . 

 For the Incident Type, verify Data Loss
 Prevention is selected. 
 If
 Data Loss Prevention is not
 displayed, hover your mouse over the field to
 display the list of available incident types to
 search for and select Data Loss
 Prevention . 

 for the Mapper , verify that
 Data Loss Prevention is
 selected. 

 If Data Loss Prevention is not
 displayed, hover your mouse over the field to
 display the list of available incident types to
 search for and select Data Loss
 Prevention . 

 Add the Access Token and
 Refresh Token you created in
 the previous step. 

 Check (enable) Long running
 instance . 

 ( Optional) Modify the automated
 Slack Bot Message . 

 Test to confirm Cortex XSOAR has successfully integrated with
 Enterprise DLP . 
 A
 Success is displayed
 when Cortex XSOAR successfully integrates
 with Enterprise DLP . 

 Configure the DLP Incident Feedback Loop Cortex XSOAR playbook 

 In Dashboard & Reports, select
 Playbooks . 

 Select DLP Incident Feedback Loops Playbook Triggered . 

 Configure the Cortex XSOAR playbook. 

 For ApprovalTarget , enter
 Manager to send an exemption
 request to the sender's manager. This information is pulled
 from your preferred IP address directory service. 

 For the UserMessageApp , verify
 Email is displayed. 

 For the ApproverMessageApp ,
 enter Email . 

 ( Optional ) For the
 DenyMessage , enter a custom
 response when a file extension is denied by the sender's
 manager, 

 Save . 

 Confirm the Cortex XSOAR integration with Enterprise DLP . 

 Log in to 
 Strata Cloud Manager . 

 Select Configuration Data Loss Prevention Settings Alerts XSOAR Integration Setup and expand the Setup Instructions 
 section. 

 Toggle the Confirm the status for XSOAR
 Integration setting to On . 

 Expand the Configuration section to define the
 Exemption Duration for exempted files that prompt the
 End User Alerting with Cortex XSOAR notification. 
 This setting defines how long a specific file is granted an block exemption
 when your administrator responds to blocked traffic .
 The default is 12 hours. 

 Previous 

 About Enterprise DLP End User Alerting with Cortex XSOAR 

 Next 

 Respond to Blocked Traffic Using Enterprise DLP End User Alerting with Cortex XSOAR 

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

 Administration 

 Cloud-Delivered Security Services 

 Data Filtering 

 Enterprise DLP 

 Task 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
