---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-3.x/cortex-xdr-3.x-documentation/detect-threats-and-analyze-data/forensic-investigations/manage-an-investigation/user-permissions
fetched_at: 2026-09-16T08:44:10Z
source: cortex-platform
---

# User permissions | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR 

 Cortex XDR 3.x Documentation 

 Cortex XDR 3.x Documentation 

 Detect threats and analyze data 

 Forensic investigations 

 Manage an investigation 

 Cortex XDR 3.x 

 User permissions 

 You can assign users to the investigation for them to view and manage the investigation. 

 By default, investigation permissions utilize the role-based access control (RBAC) settings configured in the system. Users must have a role with the Forensic permissions set to View in order to view forensic investigations. In order to create investigations or collections, a user must have a role where the Forensics permissions is set to View/Edit . Without either role, a user cannot interact with the forensics interface. 

 If Scope-Based Access Control (SBAC) is enabled on your system, from the Permissions table, you can select the users from which to assign permissions to the investigation. 

 Users with account administrator or instance administrator roles have access to investigations and can't be cleared from the Permissions table. They can view and edit all Investigations, including adding/removing users, creating/deleting collections, closing the Investigation. This prevents investigation lockout in the event of a user leaving before the Investigation is complete. 

 Note 

 Even if a user does not have access to view an investigation via the Forensics Investigations page, they can still query the results of the collections using an XQL query. 

 The Permissions fields describe the following information: 

 Field 

 Description 

 User Name 

 Name of the user as logged in the Settings +Configurations → Access Management → Users . 

 Email 

 The user's email as logged in the Settings +Configurations → Access Management → Users . 

 User Type 

 Indicates whether the user was defined in Cortex XDR using the CSP (Customer Support Portal), SSO (single sign-on) using your organization’s IdP, or both CSP/SSO. 

 Role 

 Name of the role assigned specifically to the user that is not inherited from somewhere else, such as a User Group. When the user does not have any Cortex XDR access permissions that are assigned specifically to them, the field displays No-Role. 

 Permissions 

 Options are None, View, View/Edit 

 Previous Close an investigation 

 Next Data collection 

 Last updated 20 days ago 

 Was this helpful?
