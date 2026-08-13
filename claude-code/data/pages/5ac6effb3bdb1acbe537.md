---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/onboard-cortex-xsiam/deployment-steps/set-up-authentication/authenticate-users-using-sso
fetched_at: 2026-08-13T14:11:52Z
source: cortex-platform
---

# Authenticate users using SSO | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

Authenticate users using SSO | Cortex Documentation Portal 

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

 Authenticate users using SSO 

 Cortex XSIAM enables you to authenticate system users securely across enterprise-wide applications and websites with one set of credentials using single sign-on (SSO) with SAML 2.0. System users can authenticate using your organization's Identity Provider (IdP), such as Okta or PingOne. You can integrate with any IdP that is supported by SAML 2.0. 

 Use SAML SSO when you want your platform users to be authenticated according to your organization's precise security standards as implemented within your enterprise IdP. This is critical for enforcing corporate Multi-Factor Authentication (MFA) mandates, identity verification policies, handling automatic de-provisioning (for example, when a user leaves the company), or specific conditional network access rules before granting portal access. 

 Configuring SSO with SAML 2.0 is dependent on your organization’s IdP. Some of the parameter values need to be supplied from your organization’s IdP and some need to be added to your organization’s IdP. You must have sufficient knowledge about IdPs, how to access your organization’s IdP, which values to add to Cortex XSIAM, and which values to add to your IdP fields. 

 Note 

 To set up SSO authentication in the tenant, you must be assigned an Instance Administrator or Account Admin role. 

 SAML 2.0 users must log in to Cortex XSIAM using the FQDN (full URL) of the tenant. To allow login directly from the IdP to , you must set the relay state on the IdP to the FQDN of the tenant. 

 If you have multiple tenants, you must set up the SSO configuration separately for each tenant, both in the IdP and in Cortex XSIAM. 

 If you are using AWS SSO, the Application ACS URL refers to the Single Sign-On URL and the Application SAML Audience refers to the Audience URL (SP Entity ID) . Both values can be copied from the Authentication Settings in Cortex XSIAM. 

 Unlike users who authenticate through the Customer Support Portal (CSP), users who log in via SSO do not require the Cortex User role to be assigned in the CSP. Their access and permissions are governed by the SAML Group Mapping configured in Cortex XSIAM. 

 Identity provisioning and de-provisioning lifecycle 

 Just-In-Time (JIT) account creation 

 When an enterprise user authenticates through your configured Identity Provider (IdP) for the very first time, an explicit user account entry is dynamically generated inside the platform via Just-In-Time (JIT) provisioning. Once provisioned, this newly formed user identity appears within the primary Users Table console. 

 Following initial JIT creation, administrators can open the account entry to assign targeted Access Management controls, defining precise Roles and granular data Scopes. You can choose to select an optional global Default Role parameter within the general SSO configuration menu to automatically apply baseline permissions to newly provisioned users. 

 To maintain a secure posture, it is critical that this Default Role is configured with the least-privileged permissions possible (such as read-only or a basic viewer role) to ensure users without explicit role or group assignments inherit minimal access by default. For detailed implementation steps and advice on structuring these permissions, see. 

 SECURITY MINIMIZATION BEST PRACTICE : If a Default Role is utilized for JIT automation, it is strongly recommended to restrict this role to the most minimal, low-privilege read-only permissions possible. This ensures that if a platform administrator forgets to manually apply an explicit target role or scope assignment to a newly synced user, that account remains structurally isolated from sensitive security controls or data views. 

 Once account objects successfully register via JIT login, administrators can manually pair those known identities directly with local Custom Cortex User Groups within the console. 

 Deprovisioning and account disabling actions 

 Identity Provider (IdP) account suspensions : If a user account is deleted, suspended, or disabled directly within your organization's external Identity Provider (IdP), that target user is blocked from executing any further single sign-on validation attempts into Cortex XSIAM if you set SSO as the authentication method, taking effect upon their next login sequence. For continuity tracking purposes, the historical record for that user will continue to populate inside the internal console Users table until an inactivity threshold triggers a backend purge. For more information, see the [Inactivity removal cycles] policy explained directly below. 

 Inactivity removal cycles : For accounts bound to both single sign-on (SSO) pipelines and native Customer Support Portal (CSP) infrastructure, identity profiles and group mappings are automatically purged and removed from the platform console following a specified period of prolonged system inactivity. This inactivity threshold is explicitly configured by navigating to Settings → Configurations → General → Security Settings and selecting Enabled from the Deactivate Inactive User drop-down menu. Selecting this option exposes the Deactivation period field, which is set to 30 days by default, allowing administrators to specify the exact number of inactive days required to trigger user deactivation. 

 Cloud Identity Engine (CIE) separation boundary : Disabling, removing, or changing user records directly inside the Cloud Identity Engine interface does not disable, modify, or block corresponding user accounts inside Cortex XSIAM. User lifecycle connectivity is governed purely by active IdP authentication responses or CSP invitation status. 

 If you are configuring Okta or Microsoft Entra ID, follow the procedure in Okta or Microsoft Entra ID. You can also adapt these instructions for use with any similar SAML 2.0 IdP. 

 In Cortex XSIAM, go to Settings → Configurations → Access Management → Authentication Settings . 

 In the Login Options tab, toggle SSO Disabled to on. 

 You can see the SSO settings, so you can configure them according to your organization’s IdP. 

 If you want to add another SSO connection to enable managing user groups with different roles and different IdPs, click Add SSO Connection . 

 Different SSO parameters for an SSO are displayed to configure according to your organization’s additional IdP. 

 Note 

 The first SSO cannot be deleted; it can only be deactivated by toggling SSO Enabled to off. 

 The Domain parameter is predefined for the first SSO. 

 If you add additional SSO providers, you must provide the email Domain in the SSO Integration settings for all providers except the first. Cortex XSIAM uses this domain to determine to which identity provider to send the user for authentication. 

 When mapping IdP user groups to Cortex XSIAM user groups, you must include the group attribute for each IdP you want to use. For example, if you are using Microsoft Entra ID and Okta, your Cortex XSIAM user group SAML Group Mapping field must include the IdP groups for each provider. Each group name is separated by a comma. 

 Set the following parameters using your organization’s IdP, where the field parameters are explained in the tables below. 

 General parameters 

 IdP Attribute Mapping 

 Advanced Settings (optional) 

 Save your changes. 

 Whenever an SSO user logs in to Cortex XSIAM, the following login options are available. 

 Sign-in with SSO 

 If you have enabled more than one SSO provider, an optional email field appears. If the user does not enter an email address or if the email address does not match an existing domain, the user is automatically directed to the default IdP provider (the first in the list of SSO providers in the Authentication Settings). If the user enters an email address and it matches a domain listed in the Domain field in the SSO Integration settings for one of your IdPs, Sign-In with SSO sends the user to the IdP associated with that email domain. 

 Important 

 PROGRAMMATIC CONTRAINT : 

 There is no public API endpoint available to provision or de-provision users programmatically within Cortex XSIAM. All target accounts must be initialized or explicitly managed using the native interactive Single Sign-On (SSO) or Customer Support Portal (CSP) interface workflows defined in this guide. To review the list of supported programmatic actions and ingestion endpoints, see the Cortex XSIAM API Reference guide. 

 General parameters 

 Parameter 

 Description 

 IdP SSO or Metadata URL 

 Select the option that meets your organization's requirements. 

 Indicates your SSO URL, which is a fixed, read-only value based on your tenant's URL using the format https:// <name of tenant> .crtx.paloaltonetworks.com/idp/saml . For example, https://tenant1.crtx.paloaltonetworks.com/idp/saml 

 You need this value when configuring your IdP. 

 IdP SSO URL 

 Specify your organization’s SSO URL, which is copied from your organization’s IdP. 

 Metadata URL 

 Audience URI (SP Entity ID) 

 Indicates your Service Provider Entity ID, also known as the ACS URL. It is a fixed, read-only value using the format, https:// <name of tenant> .paloaltonetworks.com . For example https://tenant1.crtx.paloaltonetworks.com . 

 You need this value when configuring your organization’s IdP. 

 Default Role 

 (Optional) Select the default role that you want any user to automatically receive when they are granted access to Cortex XSIAM through SSO. This is an inherited role and is not the same as a direct role assigned to the user. 

 IdP Issuer ID 

 Specify your organization’s IdP Issuer ID, which is copied from your organization’s IdP. 

 X.509 Certificate 

 Specify your X.509 digital certificate, which is copied from your organization’s IdP. 

 Domain 

 Relevant only for multiple SSOs. For one SSO, this is a fixed, read-only value. Associate this IdP with a specific email domain (user@<domain>). When logging in, users are redirected to the IdP associated with their email domain or to the default IdP if no association exists. 

 IdP attribute mapping 

 These IdP attribute mappings are dependent on your organization’s IdP. 

 Parameter 

 Description 

 Email 

 Specify the email mapping according to your organization’s IdP. 

 Group Membership 

 Specify the group membership mapping according to your organization’s IdP. 

 Note 

 Cortex XSIAM requires the IdP to send the group membership as part of the SAML token. Some IdPs send values in a format that include a comma, which is not compatible with Cortex XSIAM. In that case, you must configure your IdP to send a single value without a comma for each group membership. For example, if your IdP sends the Group DN (a comma-separated list), by default, you must configure IdP to send the Group CN (Common Name) instead. 

 First Name 

 Specify the first name mapping according to your organization’s IdP. 

 Last Name 

 Specify the last name mapping according to your organization’s IdP. 

 Advanced settings 

 The following advanced settings are optional to configure and some are specific for a particular IdP. 

 Parameter 

 Description 

 Relay State 

 (Optional) Specify the URL for a specific page that you want users to be directed to after they’ve been authenticated by your organization’s IdP and log in to Cortex XSIAM. 

 IdP Single logout URL 

 (Optional) Specify your IdP single logout URL provided by your organization’s IdP to ensure that when a user initiates a logout from Cortex XSIAM, the identity provider logs the user out of all applications in the current identity provider login session. 

 SP Logout URL 

 (Optional) Indicates the Service Provider logout URL that you need to provide when configuring a single logout from your organization’s IdP to ensure that when a user initiates a logout from Cortex XSIAM, the identity provider logs the user out of all applications in the current identity provider login session. This field is read-only and uses the following format https://<name of tenant>.crtx.paloaltonetworks.com/idp/logout , such as https://tenant1.crtx.paloaltonetworks.com/idp/logout . 

 Service Provider Public Certificate 

 (Optional) Specify your organization’s IdP service provider public certificate. 

 Service Provider Private Key (Pem Format) 

 (Optional) Specify your organization’s IdP service provider private key in Pem Format. 

 Remove SAML RequestedAuthnContext 

 (Optional) Requires users to log in to Cortex XSIAM using additional authentication methods, such as biometric authentication. 

 Selecting this removes the error generated when the authentication method used for previous authentication is different from the one currently being requested. See here for more details about the RequestedAuthnContext authentication mismatch error. 

 Force Authentication 

 (Optional) Requires users to reauthenticate to access the Cortex XSIAM tenant if requested by the idP, even if they already authenticated to access other applications. 

 Troubleshoot SSO issues 

 The following list describes the common errors and issues when using SAML 2.0 authentication. 

 Errors in your IdP could mean the Service Provider Entity ID and/or Service Identifier are not properly configured in the IdP or in the Cortex XSIAM settings. 

 SAML attributes from the IdP are not properly mapped in Cortex XSIAM. The attributes are case sensitive and must exactly match in your IdP and in the Cortex XSIAM IdP Attributes Mapping . 

 Group memberships from the IdP have not been properly mapped to Cortex XSIAM user groups. Verify the values your identity provider is sending, to properly map the groups in Cortex XSIAM. 

 The identity provider is not configured to sign both the SAML response and the assertion on the login token. Your IdP must be configured to sign both to ensure a secure login. 

 If you require further troubleshooting, we recommend using your browser's built-in developer tools or additional browser plugins to capture the login request and SAML token. 

 Previous Authenticate users through the Customer Support Portal Next Set up Okta as the Identity Provider Using SAML 2.0 

 Last updated 21 days ago 

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
