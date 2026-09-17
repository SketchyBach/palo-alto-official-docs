---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-on-prem/8.11/configure-cortex-xsoar/users-and-roles-management/roles-management/manage-roles-in-the-cortex-xsoar-tenant
fetched_at: 2026-09-16T08:54:33Z
source: cortex-platform
---

# Manage roles in the Cortex XSOAR tenant | 8.11 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 8 

 Cortex XSOAR 8 On-prem Documentation 

 8.11 

 Configure Cortex XSOAR 

 Users and Roles Management 

 Roles management 

 Cortex XSOAR 8.11 On-prem 

 Manage roles in the Cortex XSOAR tenant 

 Manage roles in Cortex XSOAR 8.11 On-prem. 

 On the Roles page, you can view all roles in Cortex XSOAR, whether they are custom roles, who created the role, when it was created, the tenant, either main or child, where the role can be created and additional information about the roles. When right-clicking on a role, you can edit the role and permissions. 

 Cortex XSOAR includes the following role types: 

 Predefined roles: Includes Account Admin and Instance Administrator roles. Permissions cannot be changed. You can create a duplicate of these roles, but you cannot remove them. 

 Custom roles: Includes out-of-the-box roles and custom roles. 

 When right-clicking a role, you can perform several actions, such as editing a role, saving it as a new role, and removing a role (deleting a role that is not assigned to a user). 

 Create a role 

 The roles you create provide more granular access control. You can add as many new roles as you need and combine them with user groups. When you create or edit a role, you can perform activities such as adding permissions and permission levels, defining shift periods, and setting default dashboards. 

 To create, edit, or delete a role, you must have administrator permissions. 

 Tip 

 For analysts, we recommend the following settings: 

 Remove the ability to delete incidents in production environments ( DATA → Data → Delete incidents ). 

 Remove the ability to install, delete, and contribute to Marketplace which should be reserved for engineers and administrators. We recommend setting Marketplace permissions for analysts to None or View . 

 Remove access to API keys. Under CONFIGURATIONS , set the Public API access to None or View . If you select None , the user role can still use the API, but they cannot view API keys in the UI. 

 In the Cortex XSOAR tenant, select Settings & Info → Settings → Access Management → Roles → New Role . 

 Tip 

 We recommend making a copy of out-of-the-box roles and editing the copies, rather than creating new roles, to avoid missing any important permissions. 

 Add the Role name and a meaningful Description . 

 In the Components tab, add the permissions as required. For more information, see Role-based permissions . 

 In the Advanced tab, do the following: 

 Define dashboards 

 Define preset role queries 

 Set up shift management 

 Save the role. 

 You can create user groups and add roles to them (recommended), assign roles directly to users after they have been added, or both. 

 Define dashboards 

 In a production environment, an administrator defines the default dashboard for each user and selects the default dashboards that the user sees when logging into the tenant, depending on a user’s role. If a user has not modified their dashboard, these dashboards are added automatically, otherwise users can add these dashboards to their existing dashboards. These default dashboards can be removed but not deleted, and can be added again if required. 

 If you select Only allow these dashboards , the current role will only be able to access the designated default dashboards. The role will not be able to import, edit, create, or duplicate any other dashboards. It will not be possible to share any additional dashboards with this role. 

 If a user had a role that accessed certain dashboards and the Admin changes the role to access only specific default dashboards, then the user will lose access to the previous dashboards. 

 The admin unselects Only allow these dashboards for the role. 

 The user exports the relevant dashboards and shares them with the Admin. 

 The Admin then adds the relevant dashboards to the default dashboards list for the role and reselects Only allow these dashboards . 

 Define preset role queries 

 A default query associated with a user’s role is useful for new users who are unsure which query to use when accessing the incident, indicators, and jobs pages. When accessing the relevant page, the role's preset query is the default query for a new user. Existing users can keep their default query, but the default query is available for selection. 

 When you define or edit a role, in the Advanced tab, you can view or edit a list of queries for incidents, indicators, and jobs, which are based on your saved queries for these components. 

 On the component page, such as the Incidents page, create the query. 

 Save the query (next to the query field). 

 Go to Settings & Info → Settings → Roles . 

 Select the role you want to update. 

 In the Advanced tab, select the relevant query. 

 The list of queries is populated with your own saved queries. 

 Save the role. 

 The preset query runs when a user with that role accesses that component page. If you update the preset query for a role, the query is added to the users’ queries, but not as the preset query. If you delete one of your queries after you configure a role, the role’s list of queries is unaffected. 

 Users can view the preset query based on their role when clicking the ellipsis on each component page. The preset role query has (Pre-set) appended to the name of the query. Although users can change their default query, they cannot delete the preset role query. If a user has permissions for multiple roles, the user sees multiple queries. The preset role queries appear at the top of the saved queries list. 

 If a user’s role changes, the user’s preset role query is automatically updated. 

 Set up shift management 

 Shift management helps you define multiple shifts within Cortex XSOAR. You can create user groups, so each shift can be assigned to a user group role, and you can assign one or more analysts across different shifts. 

 With shift management, you can: 

 Enable incidents to be routed automatically to analysts based on shifts, ensuring full staff coverage for incoming incidents. 

 Define multiple shifts, which can be added to a role, and in turn assigned to a user group. 

 Automatically reassign incidents when shifts change. 

 Note 

 To view suggestions for on-call users to assign to an incident, run the getOwnerSuggestions command with the shiftOnly=true argument. 

 When assigning an incident, you can manually assign it to analysts who are on-call or you can use the AssignAnalystToIncident script with argument onCall=true to automatically assign it to users who are on call and active. 

 How to define and assign shifts 

 Create or edit a role. 

 In the Advanced tab, Shifts field, click Add Shift and add the required period. 

 Weekly shifts start on Sunday and are specified in the UTC timezone format. 

 For example, create a role called First Shift and add a shift starting on Sunday and ending Monday. 

 Save the role. 

 Create a user group and assign the shift role to the user group. 

 For more information about how to create a user group, see User group management . 

 Assign one or more users to the user group. 

 Tip 

 (Optional) We recommend installing the Shift Management content pack. This content pack includes widgets to view Roles Per Shift, Users On-Call, and more in a dashboard, as well as playbooks and scripts for assigning incidents to on-call users. 

 Previous Role-based permissions 

 Next User group management 

 Last updated 1 month ago 

 Was this helpful?
