---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-administrator-guide/6.14/reference-docs/reference/server-configurations/report-server-configurations
fetched_at: 2026-09-16T08:56:40Z
source: cortex-platform
---

# Report Server Configurations | 6.14 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Administrator Guides 

 6.14 

 Reference Docs 

 Reference 

 Server Configurations 

 Cortex XSOAR 6.14 

 Report Server Configurations 

 Reference Cortex XSOAR 6.14 server configurations for reports. 

 Key 

 Description 

 Default 

 legacy.layout.enabled 

 Enables you to select and customize sections to export from the legacy summary page. For more information, see Select and Customize Sections to Export to a Summary Report . 

 true 

 report.remove.data 

 Enables you to retain the JSON file when creating a report for troubleshooting. For more information, see Troubleshoot Reports . 

 false 

 reports.email.body 

 Changes the email body of a scheduled report. For more information, see Customize the Email When Sending a Report . 

 Check out the attached report 

 reports.email.body.html 

 Changes the body HTML of the email. For more information, see Customize the Email When Sending a Report . 

 Check out the attached report 

 reports.email.subject 

 Changes the subject of the email. For more information, see Customize the Email When Sending a Report . 

 Cortex XSOAR Report - <name of the report> 

 reports.logo.customer 

 Add your own logo <the base64 image or URL for your own logo>. Used with ** reports.logo.customer. **For more information, see Change the Report Logo . 

 N/a 

 reports.logo.demisto 

 Enables you to add your own logo to a report (false). For more information, see Change the Report Logo . 

 true 

 reports.time.format 

 Configures the time/date for widgets in a report. For more information, see Configure the Time Zone and Format in a Report . 

 Local time/location 

 reports.time.zone 

 Configure the timezone for widgets in a report. For more information, see Configure the Time Zone and Format in a Report . 

 Local time/Location 

 script.timeout 

 If generating a report that includes a widget running a script, change the script timeout in minutes (for troubleshooting). For more information, see Troubleshoot Script Timeout for Reports . 

 3 

 reports.script.execution.timeout.seconds 

 If generating a large report results in a script timeout, change the report script execution timeout, in seconds. 

 300 seconds 

 Previous Remote Repository Server Configurations 

 Next Security Headers Server Configurations 

 Last updated 13 days ago 

 Was this helpful?
