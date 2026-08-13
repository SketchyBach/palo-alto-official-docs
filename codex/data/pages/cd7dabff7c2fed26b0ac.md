---
url: https://docs.paloaltonetworks.com/enterprise-dlp/administration/configure-enterprise-dlp/enterprise-dlp-and-ai-apps/create-a-security-policy-rule-for-chatgpt
fetched_at: 2026-08-13T15:32:17Z
source: palo-alto-main
---

# Create a Security Policy Rule for ChatGPT Clear

Create a Security Policy Rule for ChatGPT 

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

 Create a Security Policy Rule for ChatGPT 

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

 Enterprise DLP and AI Apps 

 Create a Security Policy Rule for ChatGPT 

 Download PDF 

 Enterprise DLP 

 Create a Security Policy Rule for ChatGPT 

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

 How Enterprise DLP Safeguards Against ChatGPT Data Leakage 

 Next 

 Email DLP 

 Create a Security Policy Rule for ChatGPT 

 Use Enterprise Data Loss Prevention (E-DLP) in a Security policy rule to prevent exfiltration of
 sensitive data to ChatGPT. 

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

 Use Enterprise Data Loss Prevention (E-DLP) to prevent exfiltration of sensitive data to ChatGPT. in a
 new or existing Security policy rule. 

 ( SaaS Security only ) If you would rather block access to ChatGPT on your network, you
 can do so from the SaaS Security Applications dashboard ( Configuration Security Services SaaS Application Management Discovered Apps Applications ). Using the SaaS Security Application dashboard to
 Block Access allows you to quickly generate a policy rule
 recommendation, rather than manually creating one on your own. 

 ( Strata Cloud Manager and SaaS Security ) Support for non-file based HTTP/2 traffic
 inspection is required to successfully prevent exfiltration to ChatGPT. Your Strata Cloud Manager tenant must be running Software Version 10.2.3 or later
 release. 

 ( Panorama ) Support for non-file based HTTP/2 traffic
 inspection is required to successfully prevent exfiltration to ChatGPT. You must
 upgrade Panorama and all managed firewalls to PAN-OS 10.2.3 or later
 release. Additionally, you must upgrade the Panorama plugin for Enterprise DLP to 3.0.2 or later release. 

 Strata Cloud Manager 

 SaaS Security 

 Panorama 

 Strata Cloud Manager 

 Create a security policy rule to prevent exfiltration of sensitive data to ChatGPT
 for Prisma Access (Managed by Strata Cloud Manager) on Strata Cloud Manager . 

 Log into Strata Cloud Manager . 

 Enable Non-File Inspection . 

 Select Configuration NGFW and Prisma Access Security Services Decryption and create the decryption profile and policy
 rule required to enable Enterprise DLP on Strata Cloud Manager . 

 Do not enable Strip ALPN in the decryption
 profile. Enterprise DLP cannot inspect egress traffic to ChatGPT if
 you remove application-layer protocol negotiation (ALPN) headers from
 decrypted traffic. 

 ( Optional ) Create a data
 pattern . 
 Create a custom regex data pattern to define your own match criteria. You can
 skip this step if you plan to use predefined or existing data patterns to define
 match criteria in your data filtering profile. 

 Create a data profile or use an existing
 data profile. 

 Select Configuration Data Loss Prevention DLP Rules and in the Actions column, Edit the DLP
 rule. 

 Enable Non-File Based Match Criteria . 

 DLP rules configured for non-file detection are required to prevent
 exfiltration of sensitive data to ChatGPT. You can further modify the DLP
 rule to enforce your organization’s data security
 standards. The DLP rule has an identical name as the data profile
 from which it was automatically created. 

 You can keep File Based Matched Criteria 
 enabled or disable as needed. Enabling this setting has no impact on
 detection of egress traffic to ChatGPT as long as
 Non-File Based Match Criteria is enabled. 

 Modify the Action and Log
 Severity . 

 Modify the rest of the DLP rule as needed. 

 Save . 

 Create a Shared Profile Group for the Enterprise DLP data filtering profile. 

 Select Configuration NGFW and Prisma Access Security Services Profile Groups and Add Profile Group . 

 Enter a descriptive Name for the Profile
 Group. 

 For the Data Loss Prevention Profile, select the Enterprise DLP 
 data profile. 

 Add any other additional profiles as needed. 

 Save the profile group. 

 Create a Security policy and attach the Profile Group. 

 Alternatively, you can create or add ChatGPT to an Internet
 Access policy rule . You can skip this step if you create a
 Internet Access policy rule for ChatGPT. 

 Select Configuration Security Services Security Policy and Add Rule . 

 You can also update an existing Security policy to attach a Profile
 Group for Enterprise DLP filtering. 

 In the Applications, Services, and URLs section, Add
 Applications to search for and select
 openai-chatgpt . 

 Navigate to the Action and Advanced Inspection section, and select the
 Profile Group you created in the previous
 step. 

 Configure the Security policy as needed. 

 The Action you specify in the data profile
 determines whether egress traffic to ChatGPT is blocked. The
 Security policy rule Action does not
 impact whether matched traffic is blocked. 

 For example, you configured the data filtering profile to
 Block matching egress traffic but
 configure the Security policy rule Action 
 to Allow . In this scenario, the matching
 egress traffic to ChatGPT is blocked. 

 Save the Security policy. 

 Push your Security policy rule. 

 For the Admin Scope, select All Admins to ensure Enterprise DLP configuration changes propagate to all enforcement
 points. 

 Enterprise DLP configuration changes don't display in
 Strata Cloud Manager 
 config snapshots . 

 Push Config and
 Push . 

 Select (enable) Remote Networks and
 Mobile Users . 

 Push . 

 SaaS Security 

 Create a security policy rule to prevent exfiltration of sensitive data to ChatGPT
 for SaaS Security on Strata Cloud Manager . 

 Log into Strata Cloud Manager . 

 Enable Non-File Inspection . 

 Select Configuration NGFW and Prisma Access Security Services Decryption and create the decryption profile and policy
 rule required to enable Enterprise DLP on Strata Cloud Manager . 

 Do not enable Strip ALPN in the decryption
 profile. Enterprise DLP cannot inspect egress traffic to ChatGPT if
 you remove application-layer protocol negotiation (ALPN) headers from
 decrypted traffic. 

 ( Optional ) Create a data
 pattern . 
 Create a custom regex data pattern to define your own match criteria. You can
 skip this step if you plan to use predefined or existing data patterns to define
 match criteria in your data filtering profile. 

 Create a data profile or use an existing
 data profile. 

 Select Configuration Data Loss Prevention DLP Rules and in the Actions column, Edit the DLP
 rule. 

 Enable Non-File Based Match Criteria . 

 DLP rules configured for non-file detection are required to prevent
 exfiltration of sensitive data to ChatGPT. You can further modify the DLP
 rule to enforce your organization’s data security
 standards. The DLP rule has an identical name as the data profile
 from which it was automatically created. 

 You can keep File Based Matched Criteria 
 enabled or disable as needed. Enabling this setting has no impact on
 detection of egress traffic to ChatGPT as long as
 Non-File Based Match Criteria is enabled. 

 Modify the Action and Log
 Severity . 

 Modify the rest of the DLP rule as needed. 

 Save . 

 Select Configuration SaaS Security Discovered Apps Policy Recommendations to create a Security policy rule
 recommendation . 

 A SaaS policy rule recommendation is
 required to leverage the Enterprise Data Loss Prevention (E-DLP) 
 data profile in SaaS Security . 

 In the Select Applications section, search for and select
 ChatGPT . 

 In the Data Profile section, search for and select the data profile you
 enabled in the previous step. 

 Configure the policy rule recommendation as needed. 

 Save . 

 Panorama 

 Create a security policy rule to prevent exfiltration of sensitive data to ChatGPT on
 the Panorama® management server . 

 Upgrade Panorama , managed firewalls, and the Enterprise DLP 
 plugin to the minimum required versions. 

 Upgrade to
 PAN-OS 10.2.3 or later release. 

 Upgrade the plugin to 3.0.2 or later release. 

 Upgrade managed firewalls to
 PAN-OS 10.2.3 or later release. 

 Log in to the Panorama web
 interface. 

 Create the decryption policy rule required for Enterprise DLP . 

 Select Objects Decryption Decryption Profile and specify the Device
 Group . 

 Add a new decryption profile. The default
 decryption profile configuration is all that is required for Enterprise DLP to inspect traffic. 

 Do not enable Strip ALPN in the decryption
 profile. Enterprise DLP cannot inspect egress traffic to
 ChatGPT if you remove application-layer protocol negotiation
 (ALPN) headers from decrypted traffic. 

 Select Policies Decryption and specify the Device
 Group . 

 Add a new decryption policy rule. Select
 Options and assign the decryption
 profile. 

 For the Action , select
 Decrypt . 

 Select the Decryption Profile you
 created. 

 Click OK . 

 Enable Non-File Inspection . 

 Data filtering profiles configured for non-file detection are required to
 prevent exfiltration of sensitive data to ChatGPT. You can create a new data
 filtering profile or use existing data filtering profiles as needed. You can
 add any combination of custom or predefined data patterns to define the
 match criteria. 

 Create a data profile on Panorama or Strata Cloud Manager , or use an existing data profile. 

 Attach the data filtering profile to a Security policy rule. 

 Select Policies Security . 

 You can select an existing Security policy rule or
 Add a new Security policy rule. 

 Configure the General and
 Source as needed. 

 Configure the Destination as needed. 

 For the Application , Add 
 and search for openai-chatgpt . 

 Skip this step if your Security policy rule applies to
 Any application. ChatGPT is automatically
 included for a Security policy rule that applies to
 Any application. 

 Select Actions and configure the Profile
 Settings. 

 Select Profiles and select the Data
 Filtering profile you created in the previous
 step. 

 If the data filtering profile is part of a Security Profile Group ( Objects Security Profile Groups ), select Group and select the
 Security Profile Group the data filtering profile is associated
 with. 

 Configure the rest of the Security policy rule as needed. 

 The Action you specify in the data
 filtering profile determines whether egress traffic to ChatGPT
 is blocked. The Security policy rule
 Action does not impact whether
 matched traffic is blocked. 

 For example, if you configured the data filtering profile to
 Block matching egress traffic but
 configure the Security policy rule Action 
 to Allow , the matching egress traffic to
 ChatGPT will be blocked. 

 Click OK . 

 Commit and push the new configuration to your managed firewalls to complete the
 Enterprise DLP plugin installation. 

 This step is required for Enterprise DLP data filtering profile names to
 appear in Data Filtering logs. 

 The Commit and Push command isn’t recommended for
 Enterprise DLP configuration changes. Using the
 Commit and Push command requires the
 additional and unnecessary overheard of manually selecting the impacted
 templates and managed firewalls in the Push Scope Selection. 

 Full configuration push from Panorama 

 Select Commit Commit to Panorama and Commit . 

 Select Commit Push to Devices and Edit
 Selections . 

 Select Device Groups and
 Include Device and Network
 Templates . 

 Click OK . 

 Push your configuration changes to
 your managed firewalls that are using Enterprise DLP . 

 Partial configuration push from Panorama 

 You must always include the temporary
 __dlp administrator when
 performing a partial configuration push. This is required to
 keep Panorama and the DLP cloud service in sync. 

 For example, you have an admin 
 Panorama admin user who is allowed to commit and push
 configuration changes. The admin 
 user made changes to the Enterprise DLP configuration and
 only wants to commit and push these changes to managed
 firewalls. In this case, the admin 
 user is required to also select the
 __dlp user in the partial
 commit and push operations. 

 Select Commit Commit to Panorama . 

 Select Commit Changes Made By and then
 click the current Panorama admin user to select additional
 admins to include in the partial commit. 

 In this example, the admin user
 is currently logged in and performing the commit operation.
 The admin user must click
 admin and then select the
 __dlp user. If there are
 additional configuration changes made by other Panorama
 admins they can be selected here as well. 

 Click OK to continue. 

 Commit . 

 Select Commit Push to Devices . 

 Select Push Changes Made By and then
 click the current Panorama admin user to select additional
 admins to include in the partial push. 

 In this example, the admin user
 is currently logged in and performing the push operation.
 The admin user must click
 admin and then select the
 __dlp user. If there are
 additional configuration changes made by other Panorama
 admins they can be selected here as well. 

 Click OK to continue. 

 Select Device Groups and
 Include Device and Network
 Templates . 

 Click OK . 

 Push your configuration changes to
 your managed firewalls that are using Enterprise DLP . 

 Previous 

 How Enterprise DLP Safeguards Against ChatGPT Data Leakage 

 Next 

 Email DLP 

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
