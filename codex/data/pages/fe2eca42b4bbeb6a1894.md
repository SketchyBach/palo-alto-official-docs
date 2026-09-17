---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-administrator-guide/6.12/onboard-cortex-xsoar/users-and-roles/authenticate-users-with-saml-2.0/set-up-okta-as-the-identity-provider-using-saml-2.0/configure-the-saml-2.0-integration-for-okta/saml-2.0-okta-parameters
fetched_at: 2026-09-16T08:57:27Z
source: cortex-platform
---

# SAML 2.0 Okta Parameters | 6.12 (EoL) | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Administrator Guides 

 6.12 (EoL) 

 Onboard Cortex XSOAR 

 Users and Roles 

 Authenticate Users with SAML 2.0 

 Set up Okta as the Identity Provider Using SAML 2.0 

 Configure the SAML 2.0 Integration for Okta 

 Cortex XSOAR 6.12 EoL 

 SAML 2.0 Okta Parameters 

 Reference Okta SAML 2.0 parameters in Cortex XSOAR 6.12. 

 The following table describes the SAML 2.0 parameters for Okta when adding a new instance in Cortex XSOAR. 

 Attribute 

 Description 

 Name 

 A name for the integration instance. 

 Service Provider Entity ID 

 The URL of your Cortex XSOAR server (also known as an ACS URL). In the format: https://yourdomain.com/saml 

 IdP metadata URL 

 URL of your organization’s IdP metadata file. You can find this in the Sign On tab in Otka or when defining an Okta application, as described in Define the Okta Application to authenticate Cortex XSOAR .

 IdP metadata file 

 Your organization’s IdP metadata file. You either need to add the IdP metadata URL or the file. 

 IdP SSO URL 

 The URL of the IdP application that corresponds to Cortex XSOAR. You can copy and paste the IdP SSO URL in Okta, when clicking View Setup Instructions . 

 Attribute to get username 

 Attribute in your IdP for the user name. 

 Attribute to get email 

 Attribute in your IdP for the user's email address. 

 Attribute to get first name 

 Attribute in your IdP for the user's first name. 

 Attribute to get last name 

 Attribute in your IdP for the user's last name. 

 Attribute to get phone 

 Attribute in your IdP for the user's phone number. 

 Attribute to get groups 

 Attribute in your IdP for the groups of which the user is a member. 

 Groups delimiter 

 Groups list separator. 

 Default role 

 Role to assign to the user when they are not a member of any group. 

 RelayState 

 Only used by certain IdPs. If your IdP uses relay state, you need to supply the relay state. 

 Sign request and verify response signature 

 Method for the IdP to verify the user sign-in request using the IdP vendor certificate. 

 Identity Provider public certificate 

 Public certificate for your IdP. 

 Private key 

 Service Provider Private key (pem format). 

 Do not map SAML groups to Cortex XSOAR roles 

 SAML groups will not be mapped to Cortex XSOAR roles. 

 Previous Configure the SAML 2.0 Integration for Okta 

 Next Map Okta Groups to Cortex XSOAR Roles 

 Last updated 12 days ago 

 Was this helpful?
