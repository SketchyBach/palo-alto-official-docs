---
url: https://docs.prismacloud.io/content-collections/administration/setup-sso-integration-on-prisma-cloud/get-started-with-oidc-sso/get-started-with-oidc-jit
fetched_at: 2026-09-16T13:35:07Z
source: prisma-cloud
---

# Get Started with OIDC JIT | Prisma Cloud arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Enterprise Edition 

 Content Collections 

 Administration 

 Set up SSO Integration on Prisma Cloud 

 Get Started with OIDC SSO 

 Get Started with OIDC JIT 

 Prisma Cloud offers System Administrators the ability to auto-provision users using the Open ID Connect (OIDC) Single Sign-On (SSO) configuration. This option allows you to manage user identities outside of Prisma Cloud in your organization’s Identity Provider (IdP). Configure OIDC Just in Time (JIT) provisioning to create new Prisma Cloud users on an as needed basis, when users with the appropriate entitlements log in using OIDC SSO. 

 Complete the steps below on the Prisma Cloud console and your IdP to set up OIDC JIT provisioning: 

 Log in to Prisma Cloud using an account with System Administrator privileges to configure SSO. 

 On your Prisma Cloud tenant select Settings > Access Control > SSO and click OIDC . 

 Navigate to Just in Time (JIT) Provisioning and select Enable . 

 Enter information for the users you would like to provision in the following fields: 

 Scopes - "email", "profile", and "openid" or are always enabled. Specify additional scopes if required to expose the Role Claim Name defined below. 

 Role Claim Name - Specify a claim under which Prisma Cloud Role names will be exposed for the purposes of authorization. If no Role Claim Name is entered, a “groups” claim will be used by default. Follow the instructions below for IdP specific configuration: 

 Microsoft Azure 

 On the Azure portal, navigate to Manage > Token Configuration > Add groups claim > Edit groups claim > Customize token properties by type and set all token types to use "sAMAccountName". 

 Navigate to API permissions > Add a permission and capture all permissions available for Microsoft Graph. 

 Okta 

 On the Okta Admin Console, navigate to Home > Applications . Select the Sign On > OpenID Connect ID Token and click edit. Select Add groups claim filter . 

 On the Okta Admin Console, navigate to Security > API > Authorization Servers > Default and ensure that groups scope is enabled. 

 Add “groups” to the Scopes defined in Step 4 above. 

 Default Role - Authenticated users that do not present a valid Prisma Cloud Role name under the Role Name Claim are granted access to this role if specified. 

 If specified, all authenticated users will have access to the Default Role. If default access for all authenticated users is required, a read-only Prisma Cloud Role is recommended. While not prohibited, use of a System Administrator Role is strongly discouraged. 

 Previous Set up OIDC on Okta 

 Next Get Started with SAML SSO 

 Last updated 1 month ago 

 Was this helpful?
