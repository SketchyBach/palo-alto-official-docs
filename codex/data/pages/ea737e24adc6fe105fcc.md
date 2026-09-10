---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-administrator-guide/6.13/investigate-and-respond-to-threats/day-to-day-tasks-in-cortex-xsoar/indicator-management/export-indicators
fetched_at: 2026-09-06T10:46:11Z
source: cortex-platform
---

# Export Indicators | 6.13 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Administrator Guides 

 6.13 

 Investigate and Respond to Threats 

 Day to Day Tasks in Cortex XSOAR 

 Indicator Management 

 Cortex XSOAR 6.13 

 Export Indicators 

 Export indicators as lists or files in Cortex XSOAR 6.13. 

 Manually Export Indicators 

 You can select one or more indicators from the Indicators table and export them as a CSV file or STIX file. The file can then be sent to or pulled by a SIEM or firewall, or can be used as the input for a playbook that processes indicators. 

 Go to the Threat Intel ( Indicators ) page. 

 Select the checkbox for one or more indicators that you want to export to a file. 

 Export the selected indicators. 

 (Optional) Click the Export button to export the indicators to a CSV file. 

 (Optional) Click the Export (STIX) button to export the indicators to a STIX file. 

 By default, the CSV file is generated in UTF8 format. You can change this to the UTF8-BOM format. 

 Export Indicators Integrations 

 You can export indicators from Cortex XSOAR using the Generic Export Indicators Service integration. Exported indicators can be used for firewall block lists, allow lists, monitoring and analysis in Splunk, etc. 

 The Generic Export Indicators Service can be configured to export specific fields in different output formats. Multiple instances of the integration can be configured for different indicator queries, and the output can be customized to work with a variety of third party services. 

 Export an Indicator to CSV Using the UTF8-BOM Format 

 By default, when exporting an indicator to a CSV format, Cortex XSOAR generates the report in UTF8 format. If you want to export an indicator that contains Cyrillic characters, such as Russian, Greek, etc., you need to change the format to UTF8-BOM. 

 Note 

 This server configuration also changes the format for exported incidents to UTF8-BOM. 

 Select Settings → ABOUT → Troubleshooting . 

 In the Server Configuration section, click Add Server Configuration . 

 Add the following key and value. 

 Key 

 Value 

 Export.utf8bom 

 true 

 Click Save . 

 Previous Exclusion List 

 Next Reference 

 Last updated 3 days ago 

 Was this helpful?
