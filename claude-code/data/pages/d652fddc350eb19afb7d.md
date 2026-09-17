---
url: https://docs.prismacloud.io/content-collections/administration/setup-sso-integration-on-prisma-cloud/get-started-with-oidc-sso/set-up-oidc-on-azure
fetched_at: 2026-09-16T13:35:07Z
source: prisma-cloud
---

# Set up OIDC on Azure Active Directory | Prisma Cloud arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Enterprise Edition 

 Content Collections 

 Administration 

 Set up SSO Integration on Prisma Cloud 

 Get Started with OIDC SSO 

 Set up OIDC on Azure Active Directory 

 Complete the steps below to configure OIDC on Azure AD. Begin by first adding an OpenID application on Azure. 

 On the Azure portal, select Azure Active Directory . 

 Select Enterprise applications > All applications . 

 Select New application from the dialog box. 

 Create the Prisma Cloud Config using the values listed below: 

 Client ID config element: Find this under AAD Registered Application → Overview. Use value of Application (client) ID under Essentials section. 

 Client Secret config element: Find this under AAD Registered Application → Secrets and Certificates. Generate a new Client Secret and use this value. Make sure you note the expiration date and set up a scheduled refresh. 

 Issuer config element: Find this here https://login.microsoftonline.com/ 

 Auth URI config element: Find this here https://login.microsoftonline.com/common/oauth2/v2.0/authorize 

 Token URI config element: Find this here https://login.microsoftonline.com/common/oauth2/v2.0/token 

 JWK Set URI config element: https://login.microsoftonline.com/common/discovery/keys 

 Previous Get Started with OIDC SSO 

 Next Set up OIDC on Okta 

 Last updated 2 months ago 

 Was this helpful?
