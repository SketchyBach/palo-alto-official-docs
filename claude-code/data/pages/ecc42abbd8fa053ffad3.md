---
url: https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/configure-dynamic-privilege-access-settings/set-up-the-prisma-access-agent-dpa/configure-staged-rollouts-for-the-prisma-access-agent-dpa.html
fetched_at: 2026-09-16T11:26:06Z
source: palo-alto-main
---

# Configure Staged Rollouts for the Prisma Agent Clear

Updated on 

 Thu Sep 03 12:12:03 PDT 2026 

 Focus 

 Home 

 Prisma Access 

 Prisma Access Administration 

 Configure Dynamic Privilege Access Settings 

 Set Up the Prisma Agent for Dynamic Privilege Access 

 Configure Staged Rollouts for the Prisma Agent 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deutsch (German) 

 Prisma Access 

 Configure Staged Rollouts for the Prisma Agent 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Access Docs 

 Release Notes 

 Select a Document 

 6.2 Preferred and Innovation 

 6.1 Preferred and Innovation 

 6.0 Preferred and Innovation 

 5.2 Preferred and Innovation 

 5.1 Preferred and Innovation 

 5.0 Preferred and Innovation 

 4.2 Preferred 

 4.1 Preferred 

 4.0 Preferred 

 3.2 Preferred and Innovation 

 Activation & Onboarding 

 Administration 

 Select a Document 

 4.0 & Later 

 Prisma Access China 

 Integrations 

 Incidents & Alerts 

 New Features 

 Previous 

 Set Up the Prisma Agent for Dynamic Privilege Access 

 Next 

 Configure General Global Settings for Prisma Agents 

 Configure Staged Rollouts for the Prisma Agent 

 Configure staged rollouts to automatically upgrade batches of Prisma Agents in a particular order. 

 The Prisma Access Agent upgrade rollout functionality provides
 administrators with a way to upgrade groups of devices in a specific order. With
 upgrade rollouts, you no longer have to rely on mobile device management (MDM)
 software, such as Jamf Pro and Microsoft Intune, to upgrade Prisma Access
 Agents. 

 Stage upgrade rollouts can
 occur only after the initial deployment or installation of the Prisma Access Agent on
 your end users' devices. 

 Before you begin, learn about staged rollouts of Prisma Access
 Agents . 

 To stage the rollout of Prisma Access Agent upgrades, you can
 configure upgrade rings with match criteria based on users, groups, and operating
 systems. Devices that match the criteria are upgraded in the order of the upgrade
 rings (Ring 0 to Ring 4, Default ring). 

 You can optionally define upgrade rings when you onboard mobile users
 using the Access Agent Setup page for the Prisma Access Agent. If you choose not to
 define upgrade rings during the initial agent configuration, all devices are placed
 in the default ring. You can return to Prisma Access Agent Setup page later to
 define the upgrade rings and push the configuration to Prisma Access. These changes
 will take effect during the next staged rollout, or after you stop and start a
 staged rollout. 

 To configure an upgrade ring: 

 In Strata Cloud Manager, select Configuration NGFW and Prisma Access Configuration Scope Access Agent Setup Prisma Access Agent . 

 In the Staged Rollouts section, click Add
 Ring . 

 Select a predefined Name for the ring. You can select
 from Ring0 to Ring4 . The first
 ring that you will add is Ring0 . 

 Enter a meaningful Description for the ring. 

 Specify the criteria for the ring based on the User ,
 Groups , or Device OS 
 attributes. 

 Add a criteria. 

 For each criterion, select an
 Attribute , Operator ,
 Value , and then click
 Add . You can select only one attribute and
 operator per criterion. The value depends on what you selected for the
 attribute and operator:

 For the Username 
 attribute: 
 If you select Operator Contains , select or search for a username from the
 Value list. To start a
 search, start typing the username. You can select one or
 more usesrnames from the list. 

 If you select Operator Equals , select or search for a username from the
 Value list. To start a
 search, start typing the username. You can select one
 usesrname from the list. 

 For the Groups 
 attribute: 
 If you select Operator Contains , select or search for a group from the
 Value list. To start a
 search, start typing the group name. You can select one
 or more groups from the list. 

 If you select Operator Equals , select or search for a group from the
 Value list. To start a
 search, start typing the group name. You can one group
 from the list. 

 For the OS attribute,
 select an OS type ( Windows or
 macOS ). Then: 
 If you select Operator Contains , search for or select one or more OS
 versions from the Value list. To
 start a search, start typing the OS and version. You can
 select one or more OS versions from the list. 

 If you select the Greater than or
 Less than operator, search
 for or select an OS version from the
 Value list. To start a
 search, start typing the OS and version. You can select
 one OS version from the list. 

 If needed, Add more criteria. You can specify up
 to three criteria per ring. 

 You can use an attribute only once per ring. After you add a criteria
 using an attribute, that attribute will no longer appear in the
 Attribute drop-down. 

 After you added the criteria, the criteria is displayed in the
 Criteria table in the Ring Criteria page.
 When Prisma Access evaluates the criteria, the values listed in the
 same cell are evaluated using the logical OR operator, while the
 attributes and values between the rows are evaluated using the
 logical AND operator. 

 For instance, the criteria in the following image will match those
 devices that belong in the gp-auto-saml-group 
 or Okta Administrators group and run the
 Windows 11 operating system. 

 Save the ring criteria. 

 To create more rings, repeat steps 2-5. You can create a total of five rings
 (Ring 0 to Ring 4). 

 Push the configuration to Prisma Access. 

 Select Push Config Push . 

 Enter a Description for the job. 

 Select the Global Prisma Access Mobile Users Access Agent container and click Push . 

 Wait for the job to finish and Close the Jobs
 dialog. 

 You can monitor the staged rollout in the
 Inventory page ( Configuration Endpoint Management ). 

 Previous 

 Set Up the Prisma Agent for Dynamic Privilege Access 

 Next 

 Configure General Global Settings for Prisma Agents
