---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-administrator-guide/6.14/customize-cortex-xsoar/customize-and-configure-cortex-xsoar/playbooks/automations
fetched_at: 2026-09-16T08:56:19Z
source: cortex-platform
---

# Automations | 6.14 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Administrator Guides 

 6.14 

 Customize Cortex XSOAR 

 Customize and Configure Cortex XSOAR 

 Playbooks 

 Cortex XSOAR 6.14 

 Automations 

 Create and manage Cortex XSOAR 6.14 automations for playbook workflows. 

 Automations perform specific actions and are comprised of commands, which are used in playbook tasks and when running commands in the War Room. 

 In the Automation page, you can view, edit, and create automations in JavaScript, Python, or PowerShell. When creating an automation, you can access all Cortex XSOAR APIs, including access to incidents, investigations, share data to the War Room, etc. Automations can receive and access arguments, and can be password protected. 

 You can use the Script Helper when creating an automation, which provides a list of available commands and scripts, ordered alphabetically. For more information about the automations used in Cortex XSOAR, see the List of Automations (Scripts) . 

 Automation Permissions 

 Permissions for automations in Cortex XSOAR are determined by the Run as and Role fields. Run as determines the permissions with which the automation runs. Role determines who the automation can be seen and executed by. 

 By default, most automations in Cortex XSOAR are run as the limited user. However, some automations require higher permissions and are delivered, out-of-the-box with Run as set to DbotRole , which means the automation executes with elevated permissions. When an automation runs with elevated permissions, its results can be viewed even by users with lower permissions. To mitigate this, you should assign a role to the automation that is aligned with the users to whom you want to expose the information the automation can extract. 

 Note 

 As content packs may use a number of these automations, and the automations could have some dependency on each another, it is important that you assign the Run as and Role parameters consistently to ensure that all of the automations can run properly. 

 For example, you have an automation that searches for all incidents in the system. The following scenarios show how the system behaves given the various configurations. 

 Scenario 1 

 Set the automation with Run as , defined as DBotRole and do not set the Role parameter. 

 Anyone can run the automation, whether they are an analyst or administrator, and they have access to all incidents that are returned. 

 automation-runas.png 

 Scenario 2 

 Set the Run as parameter to DBotRole , and set the Role parameter to Analyst . Any user with at least analyst permissions will have access to execute the automation. All other users are not able to implement the automation in playbook tasks. They cannot run the automation manually, neither from the command line nor in a playbook. 

 All users can see the results of the execution in the War Room. 

 automations-scen2.png 

 Scenario 3 

 Set the Run as parameter to Analyst and do not set a role. Everyone can run the automation, but only incidents that are viewable by the analyst role are returned. 

 automations-scen3.png 

 Scenario 4 

 You set the Run as as parameter to Analyst and define the Role parameter as Analyst . Only users with at least the analyst role are able to execute the automation. Only incidents that are viewable by the analyst role are returned. 

 automations-scen4.png 

 For example, you implemented the following roles on your incidents: 

 Incident 1 viewable to Administrators 

 Incident 2 without any role assigned 

 Incident 3 viewable by Analysts 

 Incident 4 viewable by nested Analyst (custom role) 

 As a nested analyst, you run the automation to search for the incidents in your system. 

 In scenario 1, you will see incidents 1 through 4. 

 In scenario 2, you will not be able to execute the automation, but if a playbook runs the automation, you will see incidents 1 through 4. 

 In scenario 3, you will be able to see incidents 2 through 4. 

 In scenario 4, you will not be able to execute the automation, however, if a playbook runs the automation, you will see incidents 2 and 4. 

 Note 

 When you change permissions for an automation, those permissions do not affect playbooks that are already using the automation. The playbooks continue using the previous permissions even when the playbook is triggered manually. 

 For more information, see Role-based Permission Levels . 

 Detach and Attach Automations 

 When installing an automation from a content pack, by default, the automation is attached, which means that it is not editable. To edit the automation, you need to either make a copy or detach it. 

 Note 

 You can make some changes to the automation settings, such as Propagation Labels, Run as, Roles, etc., without having to detach, or duplicate the automation. 

 While the automation is detached, it is not updated by the content pack. This may be useful when you want to update the automation without breaking customization. If you want to update the automation through content pack updates, you need to reattach it, but any changes are overwritten by the content pack on upgrade. If you want to keep the changes, make a copy before reattaching. 

 Automation Settings 

 In Script settings you can define the following information: 

 Basic 

 Parameter 

 Description 

 Name 

 An identifying name for the automation. 

 Language type 

 Select the automation language. 

 Version 

 The automation language version. 

 Description 

 A meaningful description for the automation. 

 Tags 

 Predefined script identifiers that determine where the automation is available. For example, to use this automation as a pre-processing automation, it must be tagged with the pre-processing tag. 

 Run on 

 The Cortex XSOAR server, single engine, or Load-balancing group. 

 Note 

 You need to create an engine for this field to appear. 

 Propagation Labels 

 (Multi-tenant) Select the propagation labels for the automation. 

 Enabled 

 Whether the automation is available for playbook tasks, indicator types, incident types and fields. 

 Content Pack 

 The Content Pack for which the automation belongs. 

 Arguments 

 Click Add Argument to add new arguments as required. 

 Parameter 

 Description 

 Argument 

 An identifying name. 

 Mandatory 

 Makes the argument mandatory. 

 Default 

 Makes this argument the default argument for the automation. 

 Sensitive 

 Hides the argument from being displayed in the UI and in logs. 

 Description 

 A meaningful description for the argument. 

 Initial value 

 The initial default value for the argument. 

 Is array 

 Specifies that the argument is an array. 

 Type 

 The value type of the argument. Options are Unknown, Key-Value, Text Area. 

 List options 

 CSV list of argument values. 

 Outputs 

 Click Add output to add the outputs according to string, number, date, boolean, etc. For more information, see Context and Outputs . 

 Parameter 

 Description 

 Context Path 

 A dot notation representation of the path to access the Context. For example, ThreatStream.Analysis.ReportID . 

 Description 

 A short description of what the context path represents. For example, The ID of the report submitted to the sandbox . 

 Type 

 The value type of the context path, such as string, number, etc. Enables Cortex XSOAR to format the data correctly. 

 Important 

 Click Add important to add information for backwards compatibility only for previous Cortex XSOAR versions. 

 Permissions 

 Parameter 

 Description 

 Password Protect 

 Enables you to add a password for the automation, which will be required when running the script from the CLI 

 Run as 

 Determines which role the automation runs as. Select the role from the dropdown list. 

 Roles 

 The assigned roles determine who can run the automation. 

 Advanced 

 Parameter 

 Description 

 Timeout (seconds) 

 Time (in seconds) before the automation times out. Default is 180. 

 Run on 

 The Cortex XSOAR server. 

 Docker image name 

 For Python automation, the name of the Docker image to use to run this automation. 

 Run on a separate container 

 Runs the automation on a separate container. 

 Depends on Commands 

 You can set the commands that the automation depends on directly from these settings. You still have the option to set the dependencies in the automation YAML file. 

 Related pages 

 Special Automation Tags 

 Common Scripts to use in Automations 

 Previous Create Custom Filter and Transformer Operators 

 Next Special Automation Tags 

 Last updated 13 days ago 

 Was this helpful?
