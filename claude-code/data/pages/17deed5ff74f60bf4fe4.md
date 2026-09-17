---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-administrator-guide/6.13/onboard-cortex-xsoar/users-and-roles/roles-in-cortex-xsoar/pre-set-query-per-role
fetched_at: 2026-09-16T08:56:46Z
source: cortex-platform
---

# Pre-set Query per Role | 6.13 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Administrator Guides 

 6.13 

 Onboard Cortex XSOAR 

 Users and Roles 

 Roles in Cortex XSOAR 

 Cortex XSOAR 6.13 

 Pre-set Query per Role 

 Configure pre-set queries for roles in Cortex XSOAR 6.13. 

 Choose a pre-set query for each role and supported component. 

 When users access a component, Cortex XSOAR runs their role’s pre-set query. New users receive this query by default. Existing users can select their own default query. 

 Supported components 

 Incidents 

 Indicators 

 Jobs 

 War Room 

 Create and save the query on its component page. Then select it while creating or editing the role. 

 A pre-set query is available from Saved queries . It includes (Pre-set) in its name. Users cannot delete it. 

 If a user has multiple roles, Cortex XSOAR shows multiple pre-set queries. It uses the highest nested role first. Otherwise, it uses alphabetical order. 

 If a user’s role changes, Cortex XSOAR automatically updates their pre-set role query. 

 When you edit or create roles, the available queries are based on the role’s editing permissions as follows. 

 Page 

 Page Access or Role Permissions 

 Incidents 

 Incidents 

 Indicators 

 Indicators 

 Jobs 

 Jobs 

 War Room 

 Investigation > data > read 

 When you edit a role, the list of queries is re-populated with your own saved queries. If you change the pre-set query for a role, the query will be added to the users’ queries, but not as the pre-set query. However, if you delete one of your own queries after you configure a role, the role’s list of queries is not affected. 

 When you remove a role’s pre-set query, if a query exists for that role, it will automatically become the pre-set query for the role. 

 Users can view the pre-set query based on their role when clicking Saved queries. The pre-set role query will have (Pre-set) appended to the name of the query. Although users can change their default query, they cannot delete the pre-set role query. If a user has multiple roles, the user will see multiple queries. The pre-set role query will be the highest nested one or the first one that appears alphabetically. 

 If a user’s role changes, the user’s pre-set role query is automatically updated. 

 Users can create and save queries for a component page and select any one of the saved queries to be their default query. 

 Previous Roles in Cortex XSOAR 

 Next Define a Role 

 Last updated 13 days ago 

 Was this helpful?
