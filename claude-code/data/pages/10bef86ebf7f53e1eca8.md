---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/automations/autonomous-playbooks/manage-autonomous-automation-rules
fetched_at: 2026-09-16T08:34:12Z
source: cortex-platform
---

# Manage autonomous automation rules | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSIAM 

 Cortex XSIAM Documentation 

 Configure Cortex XSIAM 

 Automations 

 Autonomous playbooks 

 Cortex XSIAM 

 Manage autonomous automation rules 

 Manage Cortex XSIAM automation rules that trigger autonomous playbooks. 

 When the Autonomous Playbooks feature is enabled, the relevant autonomous automation rules are automatically added to Cortex XSIAM and can be viewed at Investigation & Response → Automation → Automation Rules . 

 Autonomous automation rules are grouped together and are displayed as a collapsed block that you can expand. By default, the autonomous automation rules are placed at the end of the list of automation rules, but you can adjust the position of the block. For all automation rules, autonomous and regular, rules are evaluated in order, and only the first rule that matches the trigger conditions is executed. 

 You cannot edit, duplicate, or delete autonomous automation rules and you cannot delete or change the playbook assigned to the rule. 

 If you need to temporarily stop a specific autonomous playbook from triggering automatically, you can disable its rule. On the automation rules screen, right-click the specific rule within the autonomous block and select Disable . You can also add your own automation rules that apply the same condition but run a different playbook or Quick Action. If your custom automation rule is higher in the list than the autonomous automation rule, your rule is executed when the condition is met and the autonomous automation rule with the same condition is ignored. 

 As new autonomous automation rules for Cortex Analytics are released, they automatically appear in the Automation Rules pages. By default, they are enabled. 

 Autonomous automation rules only work with autonomous playbooks. You cannot trigger an autonomous playbook with a custom automation rule. 

 Previous Manage autonomous playbooks 

 Next Work Plan for autonomous playbooks 

 Last updated 1 month ago 

 Was this helpful?
