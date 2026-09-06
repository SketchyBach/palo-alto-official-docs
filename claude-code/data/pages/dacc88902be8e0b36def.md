---
url: https://cortex-docs.paloaltonetworks.com/cortex-xpanse/users-and-roles/user-authentication/set-up-okta-as-the-identity-provider-using-saml-2.0
fetched_at: 2026-09-06T10:52:22Z
source: cortex-platform
---

# Set up Okta as the Identity Provider Using SAML 2.0 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Xpanse 

 Xpanse Expander Documentation 

 Users and roles 

 User authentication 

 Set up Okta as the Identity Provider Using SAML 2.0 

 Use Okta to authenticate your Cortex Xpanse users. 

 This topic provides specific instructions for using Okta to authenticate your Cortex Xpanse users. As Okta is third-party software, specific procedures, and screenshots may change without notice. We encourage you to also review the Okta documentation for app integrations . 

 To configure SAML SSO in Cortex Xpanse, you must be a user who can access the Cortex Xpanse tenant and have either the Account Admin or Instance Admin role assigned. 

 The following video is a step-by-step guide to configuring SSO for Okta. It shows Cortex XDR, but the same steps apply to Cortex Xpanse. Cortex XDR How-To Video: Okta SSO 

 Step 1: Configure Okta Groups 

 Within Okta, assign users to groups that match the user groups they will belong to in Cortex Xpanse. Users can be assigned to multiple Okta groups and receive permissions associated with multiple user groups in Cortex Xpanse. Use an identifying word or phrase, such as Cortex Xpanse, within the group names. For example, Cortex Xpanse Analysts. This allows you to send only relevant group information to Cortex Xpanse, based on a filter you will set in the group attribute statement. 

 Create a list of the Okta groups and their corresponding Cortex Xpanse user groups (or the Cortex Xpanse user groups you intend to create) and save this list for later use when configuring user groups in Cortex Xpanse. 

 Step 2: Copy Single SSO and Audience URI Values from Cortex Xpanse 

 In Cortex Xpanse, go to Settings → Configurations → Access Management → Single Sign-On . 

 In the Single Sign-On tab, toggle SSO Disabled to on. 

 Expand the SSO Integration settings. 

 Copy and save the values for Single Sign-On URL and Audience URI (SP Entity ID) . 

 Both values are needed to configure your IdP settings. 

 You cannot save the enabled SSO Integration at this time, as it requires values from your IdP. 

 Step 3: Configure Cortex Xpanse Application in Okta 

 From within Okta, create a Cortex Xpanse application and Edit the SAML Settings . 

 Okta-Application-8.png 

 Paste the Single sign-on URL and the Audience URI (SP Entity ID) that you copied from the Cortex Xpanse SSO settings. The Audience URI should also be pasted in the Default RelayState field, which allows users to log in to Cortex Xpanse directly from the Okta dashboard. 

 Okta-SAML-Settings-8.png 

 Click Show Advanced Settings , verify that Okta is configured to sign both the response and the assertion signature for the SAML token, and then click Hide Advanced Settings . 

 Okta-Advanced-Settings-8.png 

 Cortex Xpanse requires the IdP to send four attributes in the SAML token for the authenticating user. 

 Email address 

 Group membership 

 First Name 

 Last Name 

 Okta-Attribute-Statements-8.png 

 Configure Okta to send group memberships of the users using the memberOf attribute. Use the word or phrase you selected when configuring Okta groups (such as Cortex Xpanse) to create a filter for the relevant groups. 

 Copy the exact names of the attribute statements from Okta and save them, as they are required to configure the Cortex Xpanse SSO integration. In the example above, the names are FirstName, LastName, Email, and memberOf. The attribute names are case-sensitive. 

 Step 4: Copy IdP SSO URL, Identity Provider Issuer, and X.509 Certificate Values 

 In Okta, from your Cortex Xpanse application page, click View SAML setup instructions . If you do not see this button, verify you are on the Sign On tab of the application. 

 Copy and save the values for Identity Provider Single Sign-On URL , Identity Provider Insurer , and the X.509 Certificate . These values are needed to configure your Cortex Xpanse SSO Integration. 

 Step 5: Configure the Cortex Xpanse SSO Integration 

 In Cortex Xpanse go to Settings → Configurations → Access Management → Single Sign-On . 

 In the Single Sign-On tab, toggle SSO Disabled to on. 

 Expand the SSO Integration settings. 

 Use the following table to complete the SSO Integration settings, based on the values you saved from Okta. 

 Okta 

 Cortex Xpanse Field 

 Identity Provider Single Sign-On URL 

 IdP SSO URL 

 Identity Provider Issuer 

 IdP Issuer ID 

 X.509 Certificate 

 X.509 Certificate 

 In the IdP Attributes Mapping section, enter the attribute names from Okta. The names are case-sensitive and must match exactly. 

 Save your settings. 

 Step 6: Map SAML Group Memberships to Cortex Xpanse User Groups 

 Select Settings → Configurations → Access Management → User Groups . 

 Right-click a user group and select Edit Group . 

 In the SAML Group Mapping field add the Okta group(s) that should be associated with this user group. Multiple groups should be separated with a comma. The Okta group name must match the exact value sent in the token. 

 Save your settings. 

 Repeat for each user group. 

 Step 7: Test SSO Login 

 Go to the Cortex Xpanse tenant URL and Sign-In with SSO . 

 Note 

 When using SAML 2.0, users are required to authenticate by logging in directly at the tenant URL. They cannot log in via the Cortex Gateway. 

 After authentication to Okta, you are redirected again to the Cortex Xpanse tenant. 

 Once logged in, validate that you have been assigned the proper roles. 

 To view your role and any user group role in which you belong, click your name in the bottom left-hand corner, and click About . 

 Previous Authenticate users through the Cortex Xpanse tenant using SSO 

 Next Set up Microsoft Entra ID as the Identity Provider Using SAML 2.0 

 Last updated 1 month ago 

 Was this helpful?
