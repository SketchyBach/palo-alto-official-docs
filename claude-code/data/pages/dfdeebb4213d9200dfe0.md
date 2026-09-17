---
url: https://cortex-docs.paloaltonetworks.com/analytics-alerts/alerts-by-name/azure-vm-extension-abuse-attempt
fetched_at: 2026-09-16T09:06:39Z
source: cortex-platform
---

# Azure VM extension abuse attempt | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 Analytics Alerts 

 Alerts by name 

 Azure VM extension abuse attempt 

 Synopsis 

 Field 

 Value 

 Activation Period 

 14 Days 

 Training Period 

 30 Days 

 Test Period 

 N/A (single event) 

 Deduplication Period 

 1 Day 

 Required Data 

 Azure Audit Log 

 Detection Modules 

 Cloud 

 ATT&CK Tactic 

 Execution (TA0002), Persistence (TA0003), Defense Impairment (TA0112) 

 ATT&CK Technique 

 Cloud Administration Command (T1651), Command and Scripting Interpreter: Cloud API (T1059.009), Account Manipulation (T1098), Disable or Modify Tools (T1685) 

 Severity 

 Informational 

 Description 

 A suspicious Azure VM extension operation was detected. Attackers can use CustomScriptExtension to execute arbitrary scripts on VMs, VMAccessExtension to reset local passwords for persistence, or delete the IaaSAntimalware extension to disable antimalware protection and evade detection. 

 Attacker's Goals 

 Execute arbitrary code on VMs without network access (CustomScriptExtension). 

 Gain persistent access by resetting local admin passwords (VMAccessExtension). 

 Disable antimalware to deploy malware undetected (IaaSAntimalware deletion). 

 Investigative actions 

 Identify the extension type involved (CustomScriptExtension, VMAccessExtension, IaaSAntimalware). 

 For CustomScriptExtension: review the script payload executed on the VM. 

 For VMAccessExtension: check if local admin credentials were reset and audit subsequent logins. 

 For IaaSAntimalware deletion: verify the virtual machine audit log after the extension was removed. 

 Verify whether the identity performing the operation is authorized to manage VM extensions. 

 Check for correlated suspicious activity such as new role assignments or lateral movement. 

 Variations 
 Unusual azure VM extension abuse 

 Synopsis 

 Field 

 Value 

 ATT&CK Tactic 

 Execution (TA0002), Persistence (TA0003), Defense Impairment (TA0112) 

 ATT&CK Technique 

 Cloud Administration Command (T1651), Command and Scripting Interpreter: Cloud API (T1059.009), Account Manipulation (T1098), Disable or Modify Tools (T1685) 

 Severity 

 Low 

 Description 

 A suspicious Azure VM extension operation was detected. Attackers can use CustomScriptExtension to execute arbitrary scripts on VMs, VMAccessExtension to reset local passwords for persistence, or delete the IaaSAntimalware extension to disable antimalware protection and evade detection. 

 Attacker's Goals 

 Execute arbitrary code on VMs without network access (CustomScriptExtension). 

 Gain persistent access by resetting local admin passwords (VMAccessExtension). 

 Disable antimalware to deploy malware undetected (IaaSAntimalware deletion). 

 Investigative actions 

 Identify the extension type involved (CustomScriptExtension, VMAccessExtension, IaaSAntimalware). 

 For CustomScriptExtension: review the script payload executed on the VM. 

 For VMAccessExtension: check if local admin credentials were reset and audit subsequent logins. 

 For IaaSAntimalware deletion: verify the virtual machine audit log after the extension was removed. 

 Verify whether the identity performing the operation is authorized to manage VM extensions. 

 Check for correlated suspicious activity such as new role assignments or lateral movement. 

 Previous Azure virtual machine commands execution 

 Next Bedrock model shared with a foreign account 

 Was this helpful?
