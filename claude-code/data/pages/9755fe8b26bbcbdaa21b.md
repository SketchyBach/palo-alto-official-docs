---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-administrator-guide/6.14/onboard-cortex-xsoar/users-and-roles/authenticate-users-with-saml-2.0
fetched_at: 2026-09-06T10:40:31Z
source: cortex-platform
---

# Authenticate Users with SAML 2.0 | 6.14 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Administrator Guides 

 6.14 

 Onboard Cortex XSOAR 

 Users and Roles 

 Cortex XSOAR 6.14 

 Authenticate Users with SAML 2.0 

 Authenticate Cortex XSOAR 6.14 users with SAML 2.0 identity providers, including Okta, Microsoft Entra ID, ADFS, and Duo. 

 SAML exchanges authentication and authorization data between security domains. SAML 2.0 is an XML-based protocol that uses security tokens containing assertions to pass information about a principal (usually an end user) between a SAML authority (Identity Provider) and a SAML consumer (Service Provider). 

 SAML 2.0 enables web-based authentication and authorization scenarios including cross-domain single sign-on (SSO), which helps reduce the administrative overhead of distributing multiple authentication tokens to the user. For more information about SAML 2.0, see SAML 2.0 Wikipedia . 

 You can authenticate your Cortex XSOAR users using SAML 2.0 authentication with your identity provider, such as Okta. You need to define Cortex XSOAR authentication in your Identity Provider’s account, then create a SAML 2.0 instance in Cortex XSOAR: 

 Set up Okta as the Identity Provider Using SAML 2.0 

 Set Up Microsoft Entra ID as the Identity Provider Using SAML 2.0 

 Set up ADFS as the Identity Provider Using SAML 2.0 

 When configuring the SAML 2.0 integration instance, in the third party application, if the SAML configuration contains the LDAP URL for name, email, phone, SAML populates the user's email field in Cortex XSOAR. 

 If the third party SAML configuration for name, email, phone is left blank, the administrator can modify the user properties and manually enter the information. To set this up, you need to add the following server configuration (Settings → ABOUT → Troubleshooting → Add Server Configuration ): 

 Key 

 Value 

 saml.stick.userfields 

 true 

 This server configuration does not change, no matter how many times you log into or out of Cortex XSOAR. The only time the configuration is overwritten is when the SAML configuration contains the LDAP URL for email or when it is changed manually in the third-party application. 

 Previous Change the Administrator Password 

 Next Set up Okta as the Identity Provider Using SAML 2.0 

 Last updated 4 days ago 

 Was this helpful?
