---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-on-prem/8.12/investigate-and-respond-to-threats/threat-intel-management/indicator-configuration/indicator-extraction/create-indicator-extraction-rules-for-an-incident-type
fetched_at: 2026-09-16T08:54:16Z
source: cortex-platform
---

# Create indicator extraction rules for an incident type | 8.12 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 8 

 Cortex XSOAR 8 On-prem Documentation 

 8.12 

 Investigate and Respond to Threats 

 Threat Intel Management 

 Indicator configuration 

 Indicator extraction 

 Cortex XSOAR 8.12 On-prem 

 Create indicator extraction rules for an incident type 

 In Cortex XSOAR 8.12 On-prem, create indicator extraction rules for incident types. 

 You can extract indicators from incident fields on creation of an incident and when a field changes. For example, you might want to extract the IP address upon incident creation and again when the field changes. 

 The indicator extraction feature extracts indicators from incident fields and enriches them using commands and scripts defined for the indicator type. 

 Go to Settings & Info → Settings → Object Setup → Incidents → Types . 

 For a content pack installed incident type, detach or duplicate the incident type, and then click the detached or duplicated incident type. For custom incident types, click the incident type. 

 From the Indicators Extraction Rules tab, in the On incident creation and the On field change fields, select the required indicator extraction mode. 

 If you select Out of band , the extracted indicators do not appear in the context. If you want the extracted indicators to appear, select Inline . For more information, see Indicator extraction modes . 

 In the What to Extract section, if you want to extract all incident fields, select Extract all indicators from all fields . 

 If you want to choose which indicators are extracted according to each field, select Extract specific indicators . 

 You can search and filter the incident fields. For each field, use the dropdown menu to control the indicator types to extract: 

 (Optional) You can select all indicators, set all indicators to none, or copy settings from an incident type by clicking (to the right of the table’s column headers). 

 Indicator type to extract 

 Description 

 None 

 No indicators are extracted. 

 All indicator types with regex 

 Some indicator types are associated with a regex (such as IP), and some are not (such as Registry Key). 

 Only indicators that are associated with a regex are extracted. 

 Specific indicator types 

 You can choose one or more indicator types based on regex. The system extracts values that match the regex from this incident field. 

 Select the Use field value checkbox, to use any indicator based on the field value (not regex based). This creates an indicator out of the entire value of the field, regardless whether the indicator type has a configured regex. This can be used in cases such as extracting hostnames. 

 Note 

 We recommend turning off (setting to None ) incident extraction for the Labels incident field. When an incident JSON is received from an integration, the JSON members are mapped to incident fields (based on the mapping configuration). Every member in the JSON that was not mapped to a field, will be written to the Labels field. If the Labels field extracts indicators, it can expose unmapped or unknown data to external sources. You should only map the relevant data to fields and set their extraction settings. 

 If you want to extract attachments, select the attachment field and then select File as the indicator type to extract. The File extracts a hash (usually SHA-256), which can be viewed in the War Room. You may want to disable indicator extraction for attachments to reduce external API usage and protect restricted data (the hash) from being sent. 

 Click Save . 

 (Optional) If you want to configure which scripts and commands the indicator type executes, go to Settings & Info → Settings → Object Setup → Indicators → Types and edit or Create an indicator type . 

 Add scripts and reputation commands for the indicator type. When indicator extraction occurs, indicators are extracted as defined in an indicator type, and enriched using the commands and scripts associated with the indicator type. For example, the URL indicator is enriched using the !url command. 

 In this example, if an email is forwarded that potentially includes phishing, we want to extract at incident creation (inline) and upon a field change (out of band): 

 Campaign Email Subject : Extract all indicators. 

 Campaign Email Body : Extract all indicators. 

 Email Delete Result : Extract email only. 

 Email Delete Reason : Extract email only. 

 Previous Indicator extraction modes 

 Next Set the indicator extraction mode for a playbook task 

 Last updated 9 days ago 

 Was this helpful?
