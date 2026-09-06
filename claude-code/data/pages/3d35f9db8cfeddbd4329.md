---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-administrator-guide/6.13/customize-cortex-xsoar/customize-and-configure-cortex-xsoar/indicators/indicator-customization/indicator-fields/indicator-field-trigger-scripts
fetched_at: 2026-09-06T10:45:36Z
source: cortex-platform
---

# Indicator Field Trigger Scripts | 6.13 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Administrator Guides 

 6.13 

 Customize Cortex XSOAR 

 Customize and Configure Cortex XSOAR 

 Indicators 

 Indicator Customization 

 Indicator Fields 

 Cortex XSOAR 6.13 

 Indicator Field Trigger Scripts 

 Run scripts when indicator field values change. 

 You can associate indicator fields with trigger automation scripts that check for field changes and then take actions based on them. These scripts can perform any action when the conditions are met. Indicator field trigger scripts allow indicators to become a proactive force within Cortex XSOAR. For example, you can: 

 Define a script that will run when the Verdict field of an indicator has changed. For example, the script will fetch all incidents related to that indicator and take any action that is configured (reopen, change severity, etc.). 

 Define a script that will run when the Expiration Status field has changed. For example, you can define a script that will immediately update the relevant allow/block list (and not wait for the next iteration) as seen in the following script example: 

 Ask Copy 

 indicators = demisto.args().get('indicators') 
 new_value = demisto.args().get('new') 

 indicator_values = [] 
 for indicator in indicators: 
 current_value = indicator.get('value') 
 indicator_values.append(current_value) 

 if new_value == "Expired": 
 # update allow/block list regarding expired indicators 
 else: 
 # update allow/block list regarding active indicators 

 Note 

 You must have a TIM license to run field change triggered scripts on indicator fields. 

 Automations can be created in Python, PowerShell, or JavaScript in the Automation page. To use a field trigger automation, you need to add the field-change-triggered-indicator tag when creating the automation. You can then add the automation in the Attributes tab, when you edit or Create a Custom Indicator Field . If you did not add the tag when creating the automation, the automation will not be available for use. 

 Automation Arguments - Related Information 

 When an automation is triggered on a field, it has the following triggered field information available as arguments (args): 

 Argument 

 Description 

 associatedToAll 

 If the field is associated to all or some incidents. Value: true or false . 

 associatedTypes 

 An array of the incident types, with which the field is associated. 

 cliName 

 The name of the field when called from the command line. 

 description 

 The description of the field. 

 indicators 

 A list of indicators that had the current change. 

 isReadOnly 

 Specifies whether the field is non editable. Value: true or false . 

 name 

 The name of the field. 

 new 

 The new value of the field. 

 old 

 The old value of the field. 

 ownerOnly 

 Specifies that only the creator of the field can edit. Value: true or false . 

 placeholder 

 The placeholder text. 

 required 

 Specifies whether this is a mandatory field. Value: true or false . 

 selectValues 

 If this is a multi-select type field, these are the values the field can take. 

 system 

 Whether it is a Cortex XSOAR defined field. 

 type 

 The field type. 

 user 

 The username of the user who triggered the script. 

 Script Limitations and Best Practices 

 Indicator field trigger scripts react to changes that have already occurred to the field and cannot validate or block changes to the field. 

 Indicator field trigger scripts can be configured on: Verdict , Related Incidents , Expiration Status , Indicator Type , and all custom indicator fields in the system. 

 Indicator field trigger scripts work in all TIM (Threat Intelligence Management) scenarios and workflows, except for feed ingestion. 

 Fields that may hold a list (related incidents, multi-select/tag/role type custom fields) will provide an array of the delta. For example, if a multi-select field value has changed from ["a"] to ["a", "b"], the new argument of the script will get a value of ["b"]. 

 Indicator field trigger scripts run as a batch. This means that if multiple indicators were changed in the same way and are set to trigger the same action, it will happen in one batch. For example: 

 There's a configured indicator field trigger script named myTriggerScript on the Verdict indicator field. 

 The Threat Intel Library has two existing Malicious indicators: 1.1.1.1, 2.2.2.2. 

 The user runs the following command !setIndicators indicatorsValues="1.1.1.1,2.2.2.2" verdict=Benign . 

 The myTriggerScript script will run just once, with the following parameters: 

 new - "Benign" 

 old - "Malicious" 

 indicators - "[{<indicator_1.1.1.1>},{<indicator_2.2.2.2}]" 

 When writing indicator field trigger scripts, it's crucial to avoid scenarios that will call the scripts endlessly (for example, a change in field A triggers script X, which changes field B's value, which in turn calls script Y, which changes field A's value). 

 Previous Configure the HTML Field 

 Next Indicator Layouts 

 Last updated 3 days ago 

 Was this helpful?
