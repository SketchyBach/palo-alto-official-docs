---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-saas/configure-cortex-xsoar/users-and-roles-management/set-up-authentication
fetched_at: 2026-09-16T08:52:19Z
source: cortex-platform
---

# Set up authentication | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 8 

 Cortex XSOAR 8 SaaS Documentation 

 Configure Cortex XSOAR 

 Users and Roles Management 

 Cortex XSOAR 8 (SaaS) 

 Set up authentication 

 Authenticate Cortex XSOAR 8 SaaS users using SAML 2.0 or Cortex Gateway. 

 You can create users in the Customer Support Portal or by using SAML Single Sign-On (SSO) in the tenant. Users authenticate by doing the following: 

 Authenticate through the Customer Support Portal 

 When users log into Cortex Gateway or the tenant (provided they are assigned a role) they are prompted to sign into the Customer Support Portal using their username and password or 2FA (if set up). This is the default method of authentication. 

 After you have created users, add them to user groups or assign roles directly, if you have not already done so. 

 Authenticate using SAML single sign-on in the Cortex XSOAR tenant 

 Users can be authenticated using your IdP provider such as Okta, Ping, orMicrosoft Entra ID. You can use any IdP that supports SAML 2.0. After you configure the SSO integration you need to map group SAML group membership to user groups in Cortex XSOAR. 

 SSO authentication has the following advantages: 

 Removes the administrative burden of requiring separate accounts to be configured through the Customer Support Portal. 

 Enforces multi-factor authentication (MFA) and any conditional access policies on the user login at the IdP before granting a user access to Cortex XSOAR. 

 Maps SAML group memberships to user groups and roles, allowing you to manage role-based access control. 

 Removes access to Cortex XSOAR when a user is removed or disabled in the IdP. 

 Customer Support Portal authentication, by contrast, is useful if you have users who need the same permissions across multiple tenants. If you use SSO for multiple tenants, you must set up the SSO configuration separately for each tenant, both in the IdP and in Cortex XSOAR. 

 If you want to restrict the user login through SSO only, remove any direct role and user group mapping for the user on Cortex Gateway or the Cortex XSOAR tenant. This removes Customer Support Portal access for the user. You then need to ensure that you add the SAML group mapping. The user can access and acquire the user group and roles based on SAML group mapping. Once completed, the user is able to access Cortex XSOAR using SSO only and will not be able to use Customer Support Portal login method. 

 Tip 

 You should have at least one user in the Customer Support Portal for backup, in case of any authentication issues with your IdP provider. 

 Previous User group management 

 Next Authenticate users through the Customer Support Portal 

 Last updated 2 months ago 

 Was this helpful?
