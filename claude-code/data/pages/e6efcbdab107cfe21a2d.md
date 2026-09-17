---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/cloudblades/cloudblade-integrations/chatbot-ms-teams-cloudblade-integration/create-user-groups-and-configure-chatbot-ms-teams
fetched_at: 2026-09-16T07:48:02Z
source: strata-and-sase
---

# Create User Groups and Configure Chatbot MS Teams   Clear

Updated on 

 Wed Feb 25 08:09:59 PST 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Chatbot MS Teams CloudBlade Integration 

 Create User Groups and Configure Chatbot MS Teams 

 Download PDF 

 Prisma SD-WAN 

 Create User Groups and Configure Chatbot MS Teams 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma SD-WAN Docs 

 Activation & Onboarding 

 Administration 

 CloudBlades 

 Select a Document 

 CloudBlade Integrations 

 CloudBlades Integration with Prisma Access 

 Deployment 

 Incidents & Alerts 

 Reference 

 Release Notes 

 Select a Document 

 ION 6.8 

 ION 6.6 

 ION 6.5 

 ION 6.4 

 ION 6.3 

 ION 6.1 

 ION 5.6 

 Prisma SD-WAN Controller 

 Prisma SD-WAN On-Premises Controller 

 Prisma SD-WAN CloudBlades 

 Prisma Access CloudBlade Cloud Managed 

 Prisma Access CloudBlade Panorama Managed 

 New Features 

 Previous 

 Chatbot MS Teams CloudBlade Integration 

 Next 

 Assign Chatbot to a Channel/Team 

 Create User Groups and Configure Chatbot MS Teams 

 Learn to create user groups and configure the chatbot MS teams
 cloudblade. 

 Where Can I Use This? What Do I Need? 

 Prisma SD-WAN (Managed by Strata Cloud Manager ) 

 Prisma SD-WAN 

 Chatbot MS Teams CloudBlade 

 Create a user group on MS Teams. You can follow any of the following methods to
 create a user group: 

 Create a user group on Azure
 Active Directory 

 Create a team/user group from
 scratch 

 Create a team from an existing
 team 

 Create a team from an existing
 group 

 After a user group is created on MS Teams, copy the User Group ID (object ID). 

 Enter the ID when configuring the Chatbot-MS Teams CloudBlade on Prisma SD-WAN . You can configure more than one user group on
 the CloudBlade. The User Group ID(s) can be retrieved by any of the
 following methods: 

 Azure Active Directory 

 Go to the Azure Active Directory
 portal and select
 Groups on the left panel. 

 Search and select the specific User
 Group and copy the
 object-id from the Azure
 portal. 

 Microsoft Teams 

 Go to your Team More Options Get a link to Team . 

 This provides a URL that contains the group-id. 

 For example, the Get link to Team option will display
 a URL like the one below. Embedded in the URL is the
 groupId highlighted below. Only copy the groupId
 text between = and & for
 configuration on the CloudBlade. 

 https://teams.microsoft.com/l/team/19%3afZljepRtSxrVfX1hkf876XCvPFY_jion787GBcD5lvY1%40thread.tacv2/conversations?groupId =abc6d320-b3f1-87c2-8755-02e9endaeda1 &tenantId=123dr678-h456-b758-b010-41830555h3bd 

 Configure Chatbot MS Teams 

 From the Strata Cloud Manager, select Configuration Prisma SD-WAN CloudBlades . 

 In CloudBlades, locate the Chatbot MS Teams tile and
 click Configure . 

 Contact the Palo Alto Support team if this CloudBlade does not appear in
 the list. 

 In the Chatbot-MS Teams page, enter the following
 information in the fields shown below, change where appropriate. 

 Version : Select the latest version of the
 Chatbot-MS Teams CloudBlade. 

 Admin State : For Admin State, select
 Enabled. 

 Microsoft Teams Group Information : Enter the Teams
 group Azure Active Directory ID obtained in the previous section. 

 To add multiple user groups, enter the IDs as comma-separated values. For
 example: Teams_group_AAD_ID1, Teams_group_AAD_ID2, Teams_group_AAD_ID3.

 Click Save and Install . 

 Previous 

 Chatbot MS Teams CloudBlade Integration 

 Next 

 Assign Chatbot to a Channel/Team
