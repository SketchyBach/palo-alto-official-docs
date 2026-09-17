---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-administrator-guide/6.12/onboard-cortex-xsoar/users-and-roles/authenticate-users-with-saml-2.0/duo-for-single-sign-on/create-duo-groups-for-cortex-xsoar-users
fetched_at: 2026-09-16T08:57:30Z
source: cortex-platform
---

# Create Duo Groups for Cortex XSOAR Users | 6.12 (EoL) | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

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

 Duo for Single Sign-On 

 Cortex XSOAR 6.12 EoL 

 Create Duo Groups for Cortex XSOAR Users 

 Create Duo groups for users in Cortex XSOAR 6.12. 

 To authenticate Cortex XSOAR users with Duo, you need to have at least one Duo group of Cortex XSOAR users. You can import a CSV file with a list of users, manually create users in the Duo application, or add your existing Duo users to a group. 

 There are two common methods for grouping and mapping users: 

 Create a single Duo group for all users. For example, Cortex All Users. 

 Create a Duo group for each business unit. For example, Cortex XSOAR IT, Cortex XSOAR Analysts, Cortex XSOAR Admins. 

 Log in to Duo and click Groups . 

 Select Add Group . 

 Type a name and description for the group. 

 The name and description should enable you to easily identify the users of that group. 

 Click Add Group . 

 Leave the Status as Active and click Save Changes . 

 Select +Add Users to Group and select the users you want to add to the group. 

 If you import a CSV file with your users, you can specify the group name(s) in the CSV file. If you import a CSV file before creating a group in Duo and the CSV file contains group name(s), the group(s) will be created automatically in Duo. 

 Define the Duo application to authenticate Cortex XSOAR . 

 Return to Duo for Single Sign-On . 

 Previous Duo for Single Sign-On 

 Next Define Duo to authenticate Cortex XSOAR 

 Last updated 1 month ago 

 Was this helpful?
