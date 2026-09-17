---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-5.x/onboard-cortex-xdr/post-deployment-steps/manage-user-roles-and-access-management
fetched_at: 2026-09-16T08:37:58Z
source: cortex-platform
---

# Manage user roles and access management | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR 

 Cortex XDR 5.x Documentation 

 Onboard Cortex XDR 

 Post-deployment steps 

 Cortex XDR 5.x 

 Manage user roles and access management 

 Learn how to manage access for users, user roles, user groups, and Single Sign-On (SSO) for users on a specific Cortex XDR tenant. 

 Prerequisite 

 Managing users, roles, scopes, user groups, authentication settings in Cortex XDR Access Management requires View/Edit RBAC permissions for Access Management (under Configurations ). Account Admin and Instance Administrator roles are granted this permission by default. For more information, see Predefined user roles in Set up users and roles . 

 Access management enables you to control who can access the different parts of your organization's resources. It ensures only authorized users can interact with sensitive data. 

 Cortex XDR uses a combination of Role-Based Access Control (RBAC) and Scope-Based Access Control (SBAC) to ensure scalability and granular control. 

 What is the difference between RBAC and SBAC? 

 RBAC assigns permissions based on a user's organizational role, such as Investigator or Responder, establishing a clear hierarchy and set of capabilities for each role and simplifying management by linking access to job functions. RBAC does this by helping to manage access to Cortex XDR components and Cortex Query Language (XQL) datasets, so that users, based on their roles, are granted minimal access required to accomplish their tasks. 

 SBAC refines RBAC by granting access only to the relevant data that the user requires for their designated role. Users with Access Management permission apply scopes to limit the data and content that users can be granted access to in Cortex XDR, which are divided into different scoping areas. The scoping areas include Assets, Cases and Issues, and Endpoints, which can be applied as relevant to the enforcement area or entity. 

 For example, an Investigator role might have access to asset information based on the RBAC permissions, but SBAC granular scoping could limit that investigator's view and control to only assets within a particular scoping area. This hybrid approach ensures scalability and granular control, significantly strengthening system security. 

 Understanding more about access management concepts 

 You can manage access for users, and create and assign user roles and user groups for a specific tenant. When Single Sign-On (SSO) is enabled, you can manage SSO for users. 

 Users 

 You can manage access permissions and activities for users allocated to a specific Customer Support Portal account and tenant. All users must belong to a user group or have an assigned role. 

 Note 

 To remove users added to your CSP account, you must do so in the CSP, not in Cortex Gateway. 

 User roles 

 User roles enable you to define the type of access and actions a user can perform. User roles are assigned to users, user groups, or API keys. 

 Note 

 For more information on assigning user roles when generating an API key, see Manage API keys . 

 Predefined user roles 

 Cortex XDR provides predefined built-in user roles that provide specific access rights that cannot be modified. You can also create custom, editable user roles. To view the predefined permissions for each default role, go to Settings → Configurations → Access Management → Roles . 

 Dataset access permissions 

 You can also set dataset access permissions using user roles or set specific permissions using role-based access control (RBAC). Configuring administrative access depends on the security requirements of your organization. Dataset permissions control dataset access for all components, while RBAC controls access to a specific component. By default, dataset access management is disabled, and users have access to all datasets. If you enable dataset access management, you must configure access permissions for each dataset type, and for each user role. When a dataset component is enabled for a particular role, the Issues and Cases pages include information about datasets. For more information on how to set dataset access permissions, see Manage user roles . 

 Note 

 Some features are license-dependent. Accordingly, users may not see a specific feature if the feature is not supported by the license type or if they do not have access based on their assigned role or scope. 

 User groups and scoping areas 

 You can use user groups to streamline configuration activities by grouping together users whose access permission requirements are similar. Import user groups from Active Directory, or create them from scratch in Cortex XDR. 

 Users with Access Management permission can further restrict access of these user groups, specifically for the designated role and list of users configured in the user group by granting access only to the relevant data that the user requires for their designated role. This is performed by applying scopes to limit the data and content that users can be granted access to in Cortex XDR, which are divided into different scoping areas. The scoping areas include Assets, Cases and Issues, and Endpoints, which can be applied as relevant to the enforcement area or entity. This enables you to adhere to your company's security policies of limiting user access by specifying, for example, which groups of assets users can access and what actions they can perform. 

 Note 

 For features where scoping is not applicable, Role-Based Access Control (RBAC) is used and can be configured when managing user roles. For more information, see Manage user roles . 

 Single Sign-On 

 Manage your SSO integration with the Security Assertion Markup Language (SAML) 2.0 standard to securely authenticate system users across enterprise-wide applications and websites, with one set of credentials. This configuration allows system users to authenticate using your organization's Identity Provider (IdP), such as Okta or PingOne. You can integrate any IdP with Cortex XDR supported by SAML 2.0. 

 SSO with SAML 2.0 configuration activities are dependent on your organization’s IdP. Some of the field values need to be obtained from your organization’s IdP, and some values need to be added to your organization’s IdP. It is your responsibility to understand how to access your organization’s IdP to provide these fields, and to add any fields from Cortex XDR to your IdP. 

 After SSO configuration is complete, when you sign in as an SSO user, the Cortex XDR permissions granted to you after logging in, either from the group mapping or from the default role configuration, are effective throughout the entire session for the defined maximum session length. Maximum session length is defined in your Cortex XDR Session Security Settings. This applies even if the default role configuration is updated, or the group membership settings were changed. 

 Previous Analytics log format 

 Next Manage user roles 

 Last updated 9 days ago 

 Was this helpful?
