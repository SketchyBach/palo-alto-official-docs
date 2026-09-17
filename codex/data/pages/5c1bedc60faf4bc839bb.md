---
url: https://docs.prismacloud.io/content-collections/administration/setup-sso-integration-on-prisma-cloud/get-started-with-saml-sso/setup-sso-integration-on-prisma-cloud-for-google
fetched_at: 2026-09-16T13:35:07Z
source: prisma-cloud
---

# Set up Google SSO on Prisma Cloud | Prisma Cloud arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Enterprise Edition 

 Content Collections 

 Administration 

 Set up SSO Integration on Prisma Cloud 

 Get Started with SAML SSO 

 Set up Google SSO on Prisma Cloud 

 To secure administrator access to Prisma Cloud, set up Google as the Identity Provider (IdP) and then configure Prisma Cloud as the Service Provider (SP) for SSO. 

 On Prisma Cloud, you can enable single sign-on (SSO) using Google. To enable SSO, you must first complete the setup on Google. You can then log in with System Administrator privilege on Prisma Cloud to configure SSO and redirect login requests to the Google login page so that your Prisma Cloud administrative users can log in using SSO. 

 Set up Google for SSO. 

 Before you begin to set up Google configuration, log in to your Prisma Cloud instance, select Settings > SSO and copy the Audience URI (SP Entity ID). For example: https://app.prismacloud.io/settings/sso . 

 Log in to Google Workspace as a Super Administrator. 

 From the left navigation menu, select Apps > Web and mobile Apps . 

 Select Add App > Add custom SAML App . 

 Enter a Name for your application, for example Prisma App1, upload an icon (optional), and Continue . 

 SSO connection details are displayed. You can either Download the IdP metadata (Option 1) or Copy the following information (Option 2), and Continue : 

 SSO URL 

 Entity ID 

 Certificate 

 Enter the following Prisma Cloud (service provider) details and Continue : 

 ACS URL —Enter your Prisma Cloud URL, however, replace app with api and add saml at the end. For example, if you access Prisma Cloud at https://app.prismacloud.io , enter https://api.prismacloud.io/saml . 

 Entity ID —Enter the Audience URI (SP Entity ID) value you copied in Step 1 above. 

 tt:[(Optional)]Enable Just in Time (JIT) Provisioning for SSO users. 

 Enable JIT Provisioning , if you want to create a local account for users who are authenticated by Google. With JIT, the user is provisioned with the first five roles mapped to the user’s profile on Google. 

 Finish to complete setting up Google as an IdP. Do not close the Google Workspace page in order to validate SSO after you complete setting up Prism Cloud. 

 Configure SSO on Prisma Cloud. 

 Log in to Prisma Cloud and select Settings > SSO . 

 Enable SSO . 

 Paste the values you copied in Step 6 above. 

 Identity Provider Issuer —Enter the Entity ID value. 

 Certificate —Enter the Certificate value in the standard X.509 format. 

 tt:[(Optional)] Identity Provider Logout URL —Enter the SSO URL value to which a user is redirected to, when Prisma Cloud times out or when the user logs out. 

 Select Allow select users to authenticate directly with Prisma Cloud to configure some users to access Prisma Cloud directly using their email address and password registered with Prisma Cloud, in addition to logging in using Google IdP. 

 When you enable SSO, make sure to select a few users who can also access Prisma Cloud directly using the email and password that is registered locally on Prisma Cloud to ensure that you are not locked out of the console in the event you have misconfigured SSO and need to modify the IdP settings. For accessing data through APIs, you need to authenticate directly to Prisma Cloud. 

 Select the Users who can access Prisma Cloud either using local authentication credentials on Prisma Cloud or using SSO. 

 The users listed in the allow list can log in using SSO and also using a local account username and password that you have created on Prisma Cloud. 

 Save to complete setting up Prisma Cloud to trust Google as an IdP. 

 On the Google Workspace page, click Test SAML Login to verify access using SSO. When prompted for user details, make sure to enter the email of a user who has already been provisioned on Prisma Cloud. 

 Previous Set up Azure AD SSO on Prisma Cloud 

 Next Set up Just-in-Time Provisioning on Google 

 Last updated 1 month ago 

 Was this helpful?
