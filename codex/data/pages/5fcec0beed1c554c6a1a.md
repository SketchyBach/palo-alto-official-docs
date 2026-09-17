---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-saas/investigate-and-respond-to-threats/threat-intel-management/indicator-management
fetched_at: 2026-09-16T08:52:38Z
source: cortex-platform
---

# Indicator management | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 8 

 Cortex XSOAR 8 SaaS Documentation 

 Investigate and Respond to Threats 

 Threat Intel Management 

 Cortex XSOAR 8 (SaaS) 

 Indicator management 

 Manage indicators in Cortex XSOAR 8 SaaS Threat Intel Management. 

 Indicators are artifacts associated with security incidents and are an essential part of the incident management and remediation process. They help correlate incidents, create hunting operations, and enable you to easily analyze incidents and reduce Mean Time to Response (MTTR). 

 Note 

 If you don't have a TIM license, you can only view the Indicators tab. For more information, see Manage indicators . 

 Indicators 

 Displays a list of indicators added to Cortex XSOAR, where you can perform several indicator actions. 

 Note 

 If you are unable to perform a specific action or view data, you may not have sufficient user role permissions. Contact your Cortex XSOAR administrator for more details. 

 You can perform the following actions on the Threat Intel page. 

 Action 

 Description 

 Investigate an indicator 

 Click on an indicator to view and take action on the indicator. 

 Create an indicator 

 Indicators are added to the Indicators table from incoming incidents, feed integrations, or manually creating a new indicator. 

 When creating an indicator, in the Verdict field, you can either select a verdict or leave it blank to calculate it by clicking Save & Enrich , which updates the indicator from enrichment sources. After you select an indicator type, you can add any custom field data. 

 Note 

 In the CLI, you can run the !createNewIndicator command. 

 Create an incident 

 Create an incident from the selected indicator and populate relevant incident fields with indicator data. 

 Edit 

 Edit a single indicator or select multiple indicators to perform a bulk edit. 

 Delete and Exclude 

 Delete and exclude one or more indicators from all indicator types or a subset of indicator types. 

 If you select the Do not add to exclusion list checkbox, the selected indicators are only deleted. 

 Export CSV 

 Export the selected indicators to a CSV file. By default, the CSV file is generated in UTF8 format. Administrator permission is required to update server configurations, including changing the format, see Export incidents and indicators to CSV using the UTF8-BOM format . 

 Export STIX 

 Export the selected indicators to a STIX file. 

 Upload a STIX file 

 To upload a STIX file, click the upload button (top right of the page) and add the indicators from the file. 

 Note 

 By default, when editing a list or text values in an incident/indicator, the changes are not saved until you confirm your changes (clicking the checkmark icon in the value field). These icons are designed to give you additional security when updating fields in incidents, indicators, and Threat Intel Reports. 

 You can change this default behavior by updating the server configuration. You need administrator permission to update server configurations. For more information, see Configure inline value fields . 

 Threat Intel Reports 

 Threat Intel Reports summarize and share threat intelligence research conducted within your organization by threat analysts and threat hunters. Threat Intel Reports help you communicate the current threat landscape to internal and external stakeholders, whether in the form of high-level summary reports for C-level executives, or detailed, tactical reports for the SOC and other security stakeholders. For more information, see Manage Threat Intel Reports . 

 Previous Create a Threat Intel Report layout 

 Next Query indicators 

 Last updated 14 days ago 

 Was this helpful?
