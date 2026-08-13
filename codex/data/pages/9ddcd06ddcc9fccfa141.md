---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/onboard-cortex-xsiam/deployment-steps/set-up-authentication/set-up-microsoft-entra-id-as-the-identity-provider-using-saml-2.0
fetched_at: 2026-08-13T14:12:00Z
source: cortex-platform
---

# Set up Microsoft Entra ID as the Identity Provider Using SAML 2.0 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

Set up Microsoft Entra ID as the Identity Provider Using SAML 2.0 | Cortex Documentation Portal 

 ⌘ Ctrl k 

 Blog Support 
 More 

 Home 

 Products 

 Guides 

 Release Notes 

 API 

 Reference 

 AI Assistant 

 Good afternoon 
 I'm here to help you with the docs. 

 What is this page about? What should I read next? Can you give an example? 

 ⌘ Ctrl i 

 AI Based on your context 
 Send 

 Learn about Cortex XSIAM 

 Navigate the Cortex XSIAM docs 

 Get started with Cortex XSIAM 

 Agentic AI in Cortex XSIAM 

 Cortex XSIAM product licenses 

 In-product support ticket creation 

 Supported web browsers 

 Use the interface 

 Manage API keys 

 Onboard Cortex XSIAM 

 How to onboard Cortex XSIAM 

 Plan and prepare 

 Deployment steps 

 Cortex XSIAM onboarding checklist 

 Activate Cortex XSIAM 

 Set up users, groups, and roles 

 Set up authentication 

 Authenticate users through the Customer Support Portal 

 Authenticate users using SSO 

 Set up Okta as the Identity Provider Using SAML 2.0 

 Set up Microsoft Entra ID as the Identity Provider Using SAML 2.0 

 Configure content 

 Set up Cloud Identity Engine 

 Install Cortex XDR agents 

 Cortex XSIAM - Analytics 

 FedRAMP overview 

 Post-deployment 

 Configure Cortex XSIAM 

 Learn how to configure Cortex XSIAM 

 Data management 

 Cortex XSIAM Data Sources and Connectors 

 Marketplace 

 Configure the Cortex Agentic Assistant 

 Cortex MCP server 

 Automations 

 Engines 

 Remote repository management 

 Customize cases and issues 

 XQL query management 

 Multi-Tenant 

 Managed Services configuration in Cortex 

 Protect your endpoints 

 Endpoint security 

 Endpoint DLP 

 Detect, Investigate, and respond to threats 

 Monitor dashboards and reports 

 Investigation and response 

 Agentic Assistant chat 

 Asset management 

 Threat management 

 Attack surface management 

 Vulnerability management 

 Exposure management 

 Cortex Advanced Email Security 

 Identity Threat Detection and Response (ITDR) 

 Cloud Security 

 Monitor and track compliance adherence 

 Cloud security rules and policies 

 Cortex Cloud Data Classification 

 Cortex Data Security 

 Cloud Identity Security 

 Network exposure detection 

 Cortex Cloud SaaS Security 

 Cortex Cloud AI Security 

 Serverless function posture security 

 Cortex Cloud Application Security 

 Cloud workload policies and rules 

 Base image rules 

 Web and API Security (WAAS) 

 Serverless function runtime security 

 Reference and developer docs 

 Cortex XSIAM XQL 

 Graph Search 

 Cortex CLI 

 Role-Based Access Control 

 API documentation 

 Reference 

 Migrating to a new Broker VM image 

 Learn more about migrating to the latest broker VM image 

 Standalone Broker VM 

 Broker VM high availability cluster node 

 On this page 

 For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSIAM 

 Cortex XSIAM Documentation 

 Onboard Cortex XSIAM 

 Deployment steps 

 Set up authentication 

 Set up Microsoft Entra ID as the Identity Provider Using SAML 2.0 

 This topic provides specific instructions for using Microsoft Entra ID (formerly Azure AD) to authenticate your Cortex XSIAM users. As Microsoft Entra ID is a third-party software, specific procedures, and screenshots may change without notice. We encourage you to also review the Microsoft Entra ID documentation . 

 To configure SAML SSO in Cortex XSIAM, you must be a user who can access the Cortex XSIAM tenant and have either the Account Admin or Instance Administrator role assigned. 

 The following video is a step-by-step guide configuring SSO for Microsoft Entra ID: Microsoft Entra ID SSO . 

 Task 1. Configure Microsoft Entra ID Security Groups 

 Within Microsoft Entra ID, assign users to security groups that match the user groups they will belong to in Cortex XSIAM. Users can be assigned to multiple Microsoft Entra ID groups and receive permissions associated with multiple user groups in Cortex XSIAM. Use an identifying word or phrase, such as Cortex XSIAM, within the group names. For example, Cortex XSIAM Analysts. This allows you to send only relevant group information to Cortex XSIAM, based on a filter you will set in the group attribute statement. 

 Task 2. Copy Single SSO and Audience URI Values from Cortex XSIAM 

 In Cortex XSIAM go to Settings → Configurations → Access Management → Authentication Settings . 

 In the Login Options tab, toggle SSO Disabled to on. 

 By default, SSO is disabled in Cortex XSIAM. 

 Expand the SSO Integration settings. 

 Copy and save the values for Single Sign-On URL and Audience URI (SP Entity ID) . 

 Both values are needed to configure your IdP settings. 

 Important 

 When copying the Single Sign-On URL value, remove idp/saml and leave the trailing / . 

 For example, if the Single Sign-On URL is https://clientname.panproduct.region.paloaltonetworks.com/idp/saml , just copy https://clientname.panproduct.region.paloaltonetworks.com/ . 

 You cannot save the enabled SSO Integration at this time, as it requires values from your IdP. 

 Task 3. Configure Cortex XSIAM Application in Microsoft Entra ID 

 From within Microsoft Entra ID, create a Cortex XSIAM application and Edit the Basic SAML Configuration . 

 Azure-Basic-SAML-8.png 

 Paste the Single sign-on URL and the Audience URI (SP Entity ID) that you copied from the Cortex XSIAM SSO settings. The Single sign-on URL from Cortex XSIAM should be pasted in the Reply URL and the Sign on URL fields. The Audience URI (SP Entity ID) value from Cortex XSIAM should be pasted in the Identifier (Entity ID) and Relay State fields. This allows users to log in to Cortex XSIAM directly from Microsoft Entra ID. 

 azure-basic-saml.png 

 In the SAML Certificates section, click Edit and verify that Microsoft Entra ID is configured to sign both the response and the assertion. 

 Azure-Sign-Certificate-8.png 

 To have Microsoft Entra ID send group membership for the user in the SAML token, you must + Add a group claim in the Attributes & Claims section. Send the Security groups , using the source attribute Group ID . Use the word or phrase you selected when configuring Microsoft Entra ID security groups (such as Cortex XSIAM) to create a filter. Customize the name of the group claim as memberOf . 

 Azure-memberof-Group-8.png 

 In addition to group membership, verify that there are also claims for: 

 Email address 

 First Name 

 Last Name 

 Task 4. Copy Login URL, Microsoft Entra ID Identifier, and Attribute Claims 

 In Microsoft Entra ID, from the Single sign-on page, in the Set up Cortex XSIAM Production section, copy the values for the Login URL and Microsoft Entra ID Identifier . You need these values to configure the SSO Integration in Cortex XSIAM. 

 Azure-XSOAR-Settings-8.png 

 Edit Attributes & Claims and copy the values in the Claim name column. The claim name is case sensitive. You need these values to configure the SSO Integration in Cortex XSIAM. 

 Note 

 The default attributes shown on the main single sign-on page in Microsoft Entra ID are not the values you need. You must click Edit next to Attributes and Claims to view and copy the actual values. 

 Azure-claim-names-8.png 

 Task 5. Download the Certificate 

 From the SAML Certificates section in Microsoft Entra ID, Download the Certificate (Base64) . You need the contents of this file to configure the Cortex XSIAM SSO Integration. 

 Azure-download-certificate-8.png 

 Task 6. Copy the Source IDs for Microsoft Entra ID Security Groups 

 The claim for the membership attribute that is sent to Cortex XSIAM uses the Object Id of the group. The Object Id is different from the Microsoft Entra ID security group name. You can find the Object Id for each of your Microsoft Entra ID security groups by navigating to Users and groups in Microsoft Entra ID, clicking on the group name, and viewing the Object id . Create a list of the group names and corresponding Object Ids for every Microsoft Entra ID security group you want to map to a Cortex XSIAM user group. 

 Task 7. Configure the Cortex XSIAM SSO Integration 

 In Cortex XSIAM go to Settings → Configurations → Access Management → Authentication Settings . 

 In the Login Options tab, toggle SSO Disabled to on. 

 By default, SSO is disabled in Cortex XSIAM. 

 Expand the SSO Integration settings. 

 Use the following table to complete the SSO Integration settings, based on the values you saved from Microsoft Entra ID. 

 Microsoft Entra ID 

 Cortex XSIAM Field 

 Login URL 

 IdP SSO URL 

 Microsoft Entra ID Identifier 

 IdP Issuer ID 

 Contents of the downloaded certificate file. 

 X.509 Certificate 

 In the IdP Attributes Mapping section, enter the attribute claim names from Microsoft Entra ID. The names are case sensitive and must match exactly. 

 Note 

 The attribute claim name must exactly match the value sent by your IdP. In some cases, this may be the full attribute name/namespace, depending on the configuration of our IdP 

 Azure-XSOAR-Attributes-8.png 

 (Optional) Under Advanced Settings , select the checkboxes for ADFS and Compress encode URL (ADFS) . In some circumstances, these fields may be required by your Microsoft Entra ID configuration. 

 Save your settings. 

 Task 8. Map SAML Group Memberships to Cortex XSIAM User Groups 

 Select Settings → Configurations → Access Management → User Groups . 

 Right-click a user group and select Edit Group . 

 In the SAML Group Mapping field add the Microsoft Entra ID group(s) Object Ids that should be associated with this user group. Multiple Object Ids should be separated with a comma. The Microsoft Entra ID group Object Id must match the exact value sent in the token. 

 Save your settings. 

 Repeat for each user group. 

 Task 9. Test SSO Login 

 Go to the Cortex XSIAM tenant URL and Sign-In with SSO . 

 Note 

 When using SAML 2.0, users are required to authenticate by logging in directly at the tenant URL. They cannot log in via Cortex Gateway. 

 After authentication to Microsoft Entra ID, you are redirected again to the Cortex XSIAM tenant. 

 When logged in, validate that you have been assigned the proper roles. 

 To view your role and any role assigned to a user group you are a member of, click your name in the bottom left-hand corner, and click About . 

 Previous Set up Okta as the Identity Provider Using SAML 2.0 Next Configure content 

 Last updated 22 days ago 

 Was this helpful? 

 ‍ 

 Trust Center 

 ‍ 

 Privacy 

 ‍ 

 Terms of Use 

 ‍ 

 Legal 

 © 2026 Palo Alto Networks, Inc. All rights reserved. 

 Was this helpful?
