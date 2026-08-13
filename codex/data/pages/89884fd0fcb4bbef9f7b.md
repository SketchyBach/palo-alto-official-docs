---
url: https://docs.paloaltonetworks.com/saas-security/saas-security-inline/manage-saas-security-inline-policy/create-saas-policy-rule-recommendations
fetched_at: 2026-08-13T17:33:55Z
source: palo-alto-main
---

# Create SaaS Policy Rule Recommendations Clear

Create SaaS Policy Rule Recommendations 

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

 Create SaaS Policy Rule Recommendations 

 Updated on 

 May 26, 2026 

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

 May 26, 2026 

 Focus 

 Home 

 SaaS Security 

 Manage Policy for Unsanctioned SaaS Apps 

 Create SaaS Policy Rule Recommendations 

 Download PDF 

 SaaS Security 

 Create SaaS Policy Rule Recommendations 

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

 Apply Predefined SaaS Policy Rule Recommendations 

 Next 

 Enable SaaS Policy Rule Recommendations 

 Create SaaS Policy Rule Recommendations 

 Learn how to create SaaS policy rule recommendations on SaaS Security Inline . 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by Panorama or Strata Cloud Manager) 

 Prisma Access (Managed by Panorama or Strata Cloud Manager) 

 SaaS Security Inline license 

 NGFW or Prisma Access license 

 Or any of the following licenses that include the SaaS Security Inline license: 

 CASB-X 

 CASB-PA 

 You can create a SaaS policy rule
 recommendation from scratch, or, alternatively, apply a predefined policy rule recommendation 
 or copy an existing recommendation. Before you create any recommendations, consider
 a few collaboration and authoring guidelines . 

 SaaS policy rule recommendations enable you to recommend Security policy rules to
 your Palo Alto Networks 
 NGFW administrator or Prisma Access administrator. SaaS Security Inline pushes SaaS policy rule recommendations to your NGFW or Prisma Access . Your NGFW administrator or
 Prisma Access administrator will see your policy rule recommendations in the
 NGFW web interface or Prisma Access web interface, then can
 accept and commit the SaaS Security policy rule. After your NGFW administrator or Prisma Access administrator commits the
 policy rule, the policy rule becomes active. You can update your SaaS rule
 recommendations at any time. 

 Alternatively, SaaS Security administrators can create Internet Access rules instead of policy
 rule recommendations to simplify policy rule creation for SaaS app security using
 snippets and folder configurations. This allows you to
 enforce consistent SaaS app security regardless of the enforcement point, eliminate
 policy implementation delay, and reduce the risk of misconfigurations. This
 streamlined workflow enables you to fully utilize the SaaS Security Inline 
 capabilities, achieve a stronger security posture for your SaaS environment all
 while reducing the managerial overhead of implementing new Security policy rules for
 your SaaS apps. 

 Before you begin : 

 Ask your NGFW administrator to verify that SSL decryption is enabled
 on the NGFW . SSL decryption is required for PAN-OS to detect specific
 user activities, such as upload or download activities, in the network traffic. SSL
 decryption is also required for PAN-OS to identify individual app tenants in the
 network traffic. 

 ( NGFW Only ) Ask your NGFW administrator to verify that all
 NGFW have log forwarding enabled as instructed in
 the ACE deployment . The SaaS Security web interface can’t display SaaS app visibility data and might not be able to
 enforce policy rule recommendations without logs for all 
 NGFW . 

 Log in to 
 Strata Cloud Manager 

 Select Configuration SaaS Security Discovered Apps Policy Recommendations . 

 Add Policy . 

 Select the app granularity for your policy recommendation. 

 You can define policy recommendations that are effective at the
 Application Level or at the app Tenant
 Level . App-level policy rules, if committed on the NGFW , will affect all instances of the app identified in the
 policy recommendation. Tenant-level policy rules, if committed on the NGFW , will affect only the app tenants identified in the
 policy recommendation. Before you select the app granularity for your policy
 recommendation, consider some common
 scenarios for defining app-level and tenant-level policy
 recommendations. 

 The option to create tenant-level policy
 recommendations appears only in SaaS Security Inline for NGFW, or on
 tenants that have a Next Generation Cloud Access Security Broker (CASB-X)
 license. 

 Tenant-level policy recommendations have the
 following requirements for NGFW and Prisma Access . Although you can
 submit policy recommendations without meeting these requirements, NGFW and Prisma Access administrators can view and import
 the recommendations only if these requirements are met: 
 NGFW : Tenant-level policy recommendations require a NGFW running PAN-OS 10.2.5 (or a later 10.2 release)
 or PAN-OS 11.1.0 or later. 

 Prisma Access : Tenant-level policy recommendations
 require Prisma Access running a 10.2.8 / PA 5.0 or later
 dataplane. 

 Specify a Rule Name and
 Description . For example, Block
 Unsanctioned, File Sharing Apps from HR . 

 Specify the network traffic to detect and the action to take. 

 If you're defining a policy at the app level, complete the following
 steps: 

 Specify the apps that you want to control. 
 You can only create
 recommendations for enforcement on your NGFW for SaaS
 apps that have an App-ID. You can determine if a given SaaS app in
 the Application Dictionary has an App-ID based on its How is this app
 detected? attribute. 

 Use the filters (such as the
 Category and Risk 
 filters) to help you locate the SaaS apps so that you capture all
 the app SaaS Applications. For example, if your intent is to only
 include high risk SaaS apps, filter by risk. 

 For a rule to take action on a SaaS app, the
 user activities you choose must be supported by all the SaaS apps
 you select. User activities are unique to each SaaS app. For
 example, if a SaaS app does not provide a means for a user to upload
 a file, your rule can’t include that user activity. The SaaS Security Inline web interface returns an error when you
 select a user activity that the SaaS app does not support. Use the
 Capabilities matrix to help you determine
 which user activities the SaaS apps support. 

 Select the User Activity you want the NGFW to detect. 

 Specify a Response to instruct the NGFW or Prisma Access administrator take action on
 the network traffic that matches the policy rule. 

 Although your NGFW or Prisma Access has other actions, SaaS policy rule
 recommendations support Block only. Block denies the traffic that
 matches the rule from entering your network. 

 If you're defining a policy at the tenant level, complete the following
 steps: 

 Select the app that you want to control at the tenant level 

 If the app does not appear in the selection list, SaaS Security Inline does not support tenant-level detection
 for that app. In this case, cancel the recommendation and select
 Application Level instead. 

 Note that some
 apps use different constructs, such as"workspaces" or
 "organizations", that are similar or analogous to tenants. For the
 purpose of tenant-level control, SaaS Security Inline treats
 these constructs as tenants. 

 Configure Required Settings for Tenant-Level Support 
 For certain apps, tenant-level support requires specific settings
 to be enabled on the NGFW or Prisma Access . Refer
 to the Supported Apps for Tenant-Level Control table below to
 see if any of the following settings are required for your chosen
 application: 

 Additional HTTP Header Logging: When
 enabled, the device logs more information about the apps to
 Strata Logging Service, allowing SaaS Security Inline 
 to detect individual tenants for these apps. 

 Session Tracking: When enabled, the device
 logs additional user and tenant information to Strata Logging Service . This enables you to allow
 some app traffic for a tenant, while blocking traffic from
 specific user accounts on that tenant. For example, for a
 trusted vendor, you might allow traffic only for your
 organization's accounts for a particular app, while blocking
 traffic for the vendor's accounts or personal accounts for
 the app. 

 Version Requirements 

 Additional HTTP Header Logging: Requires
 PAN-OS 11.2.3 or later. This can be configured
 for devices managed by either Panorama or Strata Cloud Manager . 

 Session Tracking: Requires PAN-OS
 11.2.5 or later. 

 Currently, Session Tracking can only
 be configured for NGFW or when they are
 managed via Panorama. This setting is not yet available to
 configure for devices managed by Strata Cloud Manager . 

 Enable Settings on NGFW or Prisma Access (Managed by Panorama) 

 Select DEVICE Setup ACE . 

 Under SaaS Inline Settings, enable Enable
 Additional HTTP Header Logging and/or Enable
 Session Tracking based on the requirements in the
 table below. 

 Enable Settings on NGFW or Prisma Access 
 (Managed by Strata Cloud Manager ) 

 Select Strata Cloud Manager Configuration NGFW and Prisma Access . 

 For Configuration Scope, select Global . 

 Select Data Security Customize . 

 Select the Enable Additional Header Logging checkbox and
 Save . 

 Supported Apps for Tenant-Level Control 
 The following
 table outlines the apps supported for tenant-level detection. 

 Understanding the Supported Actions column 

 Allow & Block: These apps allow you to
 create an Allow rule for the specific authorized
 corporate tenant(s). They also support Block rules,
 which can be used to prevent access to specific identified
 tenant(s) or to Any tenant (a wildcard to block all
 other tenants). 

 Block Only: These apps currently only
 support blocking specific identified tenants. They do not
 support an explicit tenant-level Allow action. 

 Understanding the App-Level DLP Requirements
 column 

 Due to certain app behaviors, file
 content for specific activities is not always tied to a specific
 tenant during the request. Refer to the App-Level DLP
 Requirement column: 

 Activity Specified (e.g., Upload, Download):
 If an activity is listed, any Enterprise Data Loss Prevention (E-DLP) 
 profile for the specified activity must be applied to an
 App-Level Allow in your policy stack rather than the
 tenant-level rule. 

 None: All activities for these apps can be
 configured with DLP applied directly to the tenant-level
 policy recommendation. 

 Application Category Detected Tenant Type Supported Traffic Supported Tenant-Level Actions App-Level DLP Requirements Additional Requirements 

 Aha! (Aha.io) Development Tenant Browser Block Only None None 

 Amazon Bedrock Artificial Intelligence Account ID Browser Block Only None Additional HTTP Header Logging 

 Amazon Polly Artificial Intelligence Account ID Browser Block Only None Additional HTTP Header Logging 

 Amazon Q Artificial Intelligence Account ID Browser Block Only None Additional HTTP Header Logging 

 Amazon SageMaker Artificial Intelligence Account ID Browser Block Only None Additional HTTP Header Logging 

 Amazon Sagemaker Ground Truth Artificial Intelligence Account ID Browser Block Only None Additional HTTP Header Logging 

 Amazon Titan Artificial Intelligence Account ID Browser Block Only None Additional HTTP Header Logging 

 Amazon Transcribe Artificial Intelligence Account ID Browser Block Only None Additional HTTP Header Logging 

 Azure AI Services Artificial Intelligence Account ID Browser Block Only None Additional HTTP Header Logging 

 Atlassian Confluence Collaboration & Productivity Tenant Browser Allow & Block None None 

 Azure OpenAI Artificial Intelligence Endpoint Name Browser Block Only None None 

 Bitbucket Development Workspace Browser, Mac, and Windows CLI (For HTTPS
 Config) Allow & Block Download None 

 Box Content Management Tenant Browser Allow & Block None 

 Basic HTTP header logging must be enabled on
 the firewall for the referrer component. For more
 information, see the note following this
 table. 

 ChatGPT Artificial Intelligence Workspace ID Browser Allow & Block Upload, Download Additional HTTP Header Logging 

 Claude Artificial Intelligence Organization ID Browser Allow & Block None None 

 Clockwise Artificial Intelligence Organization email domain Browser Block Only None Additional HTTP Header Logging 

 Codium AI Artificial Intelligence Team ID Mac Native, Windows Native, and
 Browser. Block Only None Additional HTTP Header Logging 

 Docusign Office Programs Account ID Browser Allow & Block None None 

 Dropbox Content Management Team ID Browser Allow & Block None Additional HTTP Header Logging 

 Egnyte Content Management Tenant Browser, Mac Native, and Windows
 Native Block Only None None 

 ElevenLabs Artificial Intelligence 

 Workspace ID 

 To help you distinguish individual tenants, the
 Tenant Name is the detected Workspace ID + the
 email domain. 

 Browser Block Only None Additional HTTP Header Logging 

 Freshdesk Management Tenant Browser Allow & Block None None 

 Frontify Content Management Tenant Browser Block Only None None 

 Github Development Organization Browser, Mac, and Windows CLI (For Https
 Config) Allow & Block Upload None 

 GitLab Development Organization Browser Allow & Block None None 

 Gmail 

 Office Programs Tenant Browser Allow & Block Upload, Download Session Tracking 

 Google Drive File Sharing Tenant Browser Block Only Download Session Tracking 

 Google Keep Internet Utility Tenant Browser Block Only None Session Tracking 

 Google Sites Content Management Tenant Browser Block Only None Session Tracking 

 Jira Collaboration & Productivity Tenant Browser Allow & Block Download None 

 Kintone Management Tenant Browser Allow & Block None None 

 Microsoft OneDrive for Business Collaboration & Productivity Tenant Browser Allow & Block None None 

 Microsoft OneNote Collaboration & Productivity Tenant Browser Allow & Block None Additional HTTP Header Logging 

 Microsoft Outlook Office Tenant Browser Allow & Block None Additional HTTP Header Logging 

 Microsoft Sharepoint Collaboration & Productivity Tenant Browser, Mac Native and Windows
 Native Allow & Block None None 

 Microsoft Teams Collaboration & Productivity Tenant ID Browser, Mac Native, and Windows
 Native Allow & Block None Additional HTTP Header Logging 

 monday.com Social Business Tenant Browser Allow & Block None None 

 MS Powerapps Development Tenant Browser Allow & Block None Additional HTTP Header Logging 

 Murf Artificial Intelligence Workspace ID Browser Block Only None Additional HTTP Header Logging 

 Okta Security Tenant Browser Block Only None None 

 OpenAI API Artificial Intelligence Organization ID Browser Block Only Download Additional HTTP Header Logging 

 PagerDuty Runbook Artificial Intelligence Tenant Browser Block Only None Additional HTTP Header Logging 

 Salesforce Sales Cloud Sales Tenant Browser Allow & Block None None 

 ServiceNow Management Tenant Browser Allow & Block None None 

 Sharefile IT Infrastructure Tenant Browser Allow & Block Download None 

 Slack Collaboration & Productivity Workspace Browser, Mac Native, and Windows
 Native Allow & Block Upload, Download None 

 Tabnine Artificial Intelligence 

 Team ID 

 To help you distinguish individual tenants, the
 Tenant Name is the detected team ID + the email
 domain. 

 Mac Native, Windows Native, and
 Browser. Block Only None Additional HTTP Header Logging 

 Webex App Collaboration & Productivity Tenant Browser Allow & Block None None 

 Windows Azure General Business Tenant Browser Block Only None Additional HTTP Header Logging 

 Workday HCM HR Tenant Browser Allow & Block Upload None 

 Workplace From Meta Collaboration & Productivity Tenant Browser Block Only None None 

 Zendesk Customer Service Tenant Browser Block Only None 

 You must enable Basic HTTP header logging on
 the NGFW for the referrer
 component. For more information, see the note
 following this table. 

 Zoom Collaboration & Productivity Tenant Browser Allow & Block None None 

 To enable SaaS Security Inline to detect Box and
 Zendesk tenants, HTTP header logging
 must be enabled on the NGFW for the referrer component. HTTP header
 logging of referring web pages provides
 added visibility into the web traffic on your network, which
 SaaS Security Inline uses to detect the individual
 tenants. 

 Tenant detection for Microsoft OneDrive for Business 
 does not include personal tenants. To block personal use of
 Microsoft OneDrive, create an app-level policy to block the
 Microsoft OneDrive Personal app. 

 Specify Action, Activity, and Tenants 

 Action: Specify the action to be
 applied to the matching network traffic. 

 The Block action denies matching
 traffic. It is supported for all apps that support
 tenant-level detection. 

 The Allow action is supported only
 for a subset of apps (see table above) and is used
 to permit exceptions to a Block action. 

 For example, you might create a policy recommendation to
 Allow access to Box on certain tenants, and then
 create a separate policy recommendation to Block access
 for Any other tenants. 

 User Activity: Select the specific user
 activities you want to detect, such as file Create, Delete,
 or Share. 

 Tenants: Select at least one
 tenant that you want to control (up to 30). 

 Tenant Names: The Tenant Name is
 based on the detected tenant type shown in the
 Supported Apps table above. For some apps,
 additional information is concatenated to the Tenant
 Name to help you distinguish tenants, such as the
 workspace ID + email domain for ElevenLabs 

 Wildcards: When the Allow 
 action is supported, you can specify that the policy
 recommendation applies to Any tenant. This
 acts as a wildcard to match all current and future
 tenants. On the device, this policy will apply to
 all tenants unless an earlier policy in the
 evaluation order specifies a different action. 

 Filtering: To filter the list of available tenants,
 select a Tenant Type. 

 Configuration & Enforcement Guidelines 
 While authoring your
 recommendations, keep the following enforcement requirements in
 mind. These will be critical for your administrator when they import
 the policy recommendations and order the final security
 policies. 

 Recommended Policy Stack Order 

 Tenant-Level rules should be arranged in the following order
 within the security policy base depending on the app’s supported
 actions: 

 Scenario A: Apps with "Allow & Block"
 Support 
 Top Rule (Allow Corporate Tenant): Position
 your imported Tenant-Level Allow rule here (if
 applicable) to permit users to access authorized corporate
 tenants. On the NGFW or Prisma Access ,
 when traffic matches a policy rule, the defined action is
 triggered and all subsequent rules are disregarded. For this
 reason, a more specific Allow policy must be placed
 before a more general Block Any policy. 

 Middle Rule (Block Other Tenants): Position
 your imported Tenant-Level Block rules here. This
 ensures any other detected tenants are blocked. 

 Bottom Rule (Allow App-Level): 
 Configuration only required for general application access
 in Default Deny environments or when App-Level
 DLP inspection is required (see below). 

 Scenario B: Apps with "Block Only"
 Support 

 Top Rule (Tenant Block): Position your
 imported Tenant-Level Block rule (for specific tenants) here
 to deny access to the selected unauthorized tenants. 

 Bottom Rule (Allow App-Level): 
 Configuration only required for general application access
 in Default Deny environments or when App-Level
 DLP inspection is required (see below). 
 General Guidance for the Bottom Rule (App-Level
 Allow) 

 You must define this rule if your organization
 meets either of the following criteria: 

 Default Deny Environments Because certain
 app traffic is not attributed to a specific tenant, the app
 may fail to function if this app-level traffic is denied. If
 your organization uses a Default Deny posture to
 block all web traffic by default, you require an explicit
 App-Level Allow rule for the standard application App-IDs to
 ensure the application functions as intended with
 tenant-level control. 

 App-Level DLP Requirements For apps with an
 activity listed in the App-Level DLP Requirement 
 column of the above table, you require an explicit App-Level
 Allow rule to apply any E-DLP profile for that activity (for
 example, slack-uploading). 

 ( Optional ) Specify User Accounts 

 The User Accounts field is shown only if the selected
 app can leverage the firewall's session-tracking feature. The apps that can
 leverage the session-tracking feature are shown in the table above. You can
 then use this field to Select user accounts that you
 want to be affected by the policy. For example, for the selected app, you
 can block personal accounts while allowing traffic for corporate accounts.
 By default, the User Accounts setting is
 Any , in which case all user accounts are affected
 by the policy. 

 To use this feature, you must enable session tracking on the firewall. 

 Specify User & Groups . 

 By specifying users or groups, the policy recommendation will apply only to
 those users and groups. Creating policy rule recommendations based on user
 group membership rather than individual users simplifies administration
 because you don’t need to update the recommendation whenever group
 membership changes. 

 The user and group information that is displayed depends on whether the Cloud
 Identity Engine is available on your tenant. 

 If the Cloud Identity Engine is not available on your tenant, then SaaS Security Inline discovers users by using Strata Logging Service logs. To discover groups, SaaS Security Inline uses Azure Active Directory (AD), provided
 you have performed an Azure Active Directory Integration. 

 If the Cloud Identity Engine is available on your tenant, and directory
 sync is configured in Cloud Identity Engine for Azure AD, SaaS Security Inline obtains user and group information from Azure
 AD through the Cloud Identity Engine. If directory sync is configured
 for multiple Azure AD instances, SaaS Security Inline obtains user
 and group information from all Azure AD instances. For obtaining user
 and group information from the Cloud Identity Engine, SaaS Security Inline supports only Azure AD. 
 SaaS Security Inline also obtains the dynamic user groups that
 the Cloud Identity Engine has defined. A dynamic user group uses
 tags as filtering criteria for group membership. As soon as a user
 matches the filtering criteria, that user becomes a member of the
 dynamic user group. Defining dynamic user groups in
 Cloud Identity Engine enables you to create a policy that
 adapts to changes in user behavior, location, and other conditions
 where context plays a key role in determining access. 

 Even
 when the Cloud Identity Engine is available on your tenant, you
 still have the option to view the user information discovered from
 Strata Logging Service logs and groups from the earlier
 method of Azure Active Directory Integration. In this case, you can
 toggle between showing Discovered Users &
 Groups from Strata Logging Service logs or
 showing CIE Users & Groups . The users and
 groups listed in these different views can vary for the following
 reasons: 

 The users in the CIE Users & Groups 
 view will show only the users from one or more Azure AD
 instances that are synced in Cloud Identity Engine. Because the
 users displayed in the Discovered Users &
 Groups view are discovered by examining Strata Logging Service logs, the Discovered
 Users & Groups can show users who don’t have
 accounts in the Azure AD instances. 

 Because the users displayed in the Discovered Users
 & Groups view are discovered by examining
 Strata Logging Service logs, only users who generated
 network traffic are listed in the Discovered Users
 & Groups view. The CIE Users
 & Groups view shows all users from the Azure
 AD instances that are synced in Cloud Identity Engine,
 regardless of whether the users generated network traffic. 

 The CIE Users & Groups view displays
 dynamic user groups. This information is available only through
 Cloud Identity Engine and so these groups are not shown in the
 Discovered Users & Groups 
 view. 

 The groups displayed in the Discovered Users &
 Groups view are obtained from only a single
 instance of Azure AD, provided you have performed an Azure
 Active Directory Integration. The groups displayed in the
 CIE Users & Groups are obtained
 from all the Azure AD instances that are synced to Cloud
 Identity Engine. 

 An advantage of using Cloud Identity Engine is that it provides
 more information in the Users & Groups table, such as a user's
 role, department, and region. You can filter the Users & Groups
 table based on this information to more easily locate the users and
 groups based on their attributes. For example, by using the
 Type filter, you could filter the table
 to show only Users , Active
 Directory Groups , and CIE Dynamic User
 Groups . 

 Select whether you want to create the policy recommendation from the
 Discovered Users & Groups view or from the
 CIE Users & Groups view. If these options
 don’t appear, then the Cloud Identity Engine isn’t available on your tenant
 or does not have directory sync configured for Azure AD. In this case, you
 can select only discovered users and groups. 

 When SaaS Security Inline submits a policy recommendation to the NGFW , it must specify the user and group information in the
 same format that the NGFW uses to identify users and groups
 in policy rules, such as a common-name, distinguished name, or SAM Account
 Name. If SaaS Security Inline sends the user or group information in
 the wrong format, the recommendation can be imported on the NGFW , but won’t have the desired effect. 

 If the policy is identifying users and groups from Cloud Identity Engine, the
 user's Primary Name and Group Name formats are included in the
 recommendation that is sent to the NGFW , and must match the
 formats specified on the NGFW . SaaS Security Inline 
 determines which format to use from the Cloud Identity Engine settings on
 the Settings page. Complete the following steps to ensure that SaaS Security Inline sends the information in the correct format. 

 Select Settings Directory & External Services . 

 Under the Cloud Identity Engine section, make sure that the Directory
 Attribute for the user's Primary Username and the Group Name match the
 user and group attributes 
 specified on the NGFW . On the NGFW , you
 can locate the relevant settings by completing the following steps: 
 Select Device User Identification Cloud Identity Engine . 

 Open the Cloud Identity Engine instance. 

 View the User Attributes tab to identify
 the Primary Username format. 

 View the Group Attributes tab to identify
 the Group Name format. 

 If the policy is identifying users from Strata Logging Service logs,
 SaaS Security Inline discovers the group information from your
 Azure Active Directory integration. If no groups display, verify that you
 performed this integration. SaaS Security Inline determines the format
 to use for group names from the Directory Services settings on the Settings
 page. Complete the following steps to ensure that SaaS Security Inline 
 sends the group information in the correct format. 

 Select Settings Directory & External Services . 

 Under the Directory Services section, click the name of the Azure Active
 Directory. 

 Make sure that the Group Name attribute matches the group attribute specified on
 the NGFW . On the NGFW , you can locate the
 relevant setting by completing the following steps: 
 Selecting Device User Identification Group Mapping Settings . 

 Open the Azure Active Directory instance. 

 View the Group Attributes tab to identify
 the Group Name format. 

 ( Optional ) Specify Device Posture to enforce
 what devices can and can’t access specific SaaS apps, including device ownership
 and device compliance. 

 Your device posture selection automatically creates a Host Information
 Profile (HIP) object for mobile devices after the policy recommendation is
 imported as a policy. 

 Mobile Device Managed Status —Choose
 Managed when the device is company-owned,
 whether a dedicated device or shared with
 Unmanaged when the device is employee-owned,
 or Any for both. 

 Mobile Device Compliant Status —Choose
 Complaint when the device adheres to your
 organization’s security compliance requirements,
 Non‑Compliant when it does not, or
 Any for both. 

 ( Optional ) Specify a Data Profile . 

 If you have an active Enterprise Data Loss Prevention (E-DLP) license, you can add predefined or custom data profiles to prevent
 exfiltration of sensitive data. Data profiles specify how you want to
 enforce the sensitive data that you’re
 filtering . 

 Save the new rule. 

 Enable the recommendation
 when you’re ready to submit the recommendation for enforcement. 

 If you create separate tenant-level Allow and
 Block policy recommendations to achieve
 particular results, remember that your desired results will depend on the
 order in which the policy rules are evaluated on the NGFW .
 Make sure that the NGFW administrator places a more specific
 Allow policy before a general
 Block 
 Any policy. If a general Block 
 Any policy is evaluated first, the NGFW will ignore the more specific Allow policy. 

 Previous 

 Apply Predefined SaaS Policy Rule Recommendations 

 Next 

 Enable SaaS Policy Rule Recommendations 

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
