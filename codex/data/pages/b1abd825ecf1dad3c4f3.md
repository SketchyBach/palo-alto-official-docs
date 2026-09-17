---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-5.x/detect-investigate-and-respond-to-threats/monitor-dashboards-and-reports/create-reports/create-a-report-template-from-scratch
fetched_at: 2026-09-16T08:42:50Z
source: cortex-platform
---

# Create a report template from scratch | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR 

 Cortex XDR 5.x Documentation 

 Detect, investigate, and respond to threats 

 Monitor dashboards and reports 

 Create reports 

 Cortex XDR 5.x 

 Create a report template from scratch 

 Build a report template from an empty layout. 

 You can use report templates to standardize and automate your data delivery—allowing you to generate one-time or recurring reports on a schedule and seamlessly distribute them to different user groups or mailing lists. 

 Use the following high-level workflow to create and distribute a report, guiding you from initial setup through layout design and distribution. 

 1 

 Open the report builder 

 Depending on your starting point, open the report builder as follows: 

 Build a report from scratch: Go to Dashboards & reports > Reports and click Create template . 

 Use a system template: Go to Dashboards & reports > Reports and click Create template . In the report builder, click Browse templates to see the available options. 

 Save a dashboard as a report template: You can save a dashboard as a report template during dashboard creation, or from the Dashboard Manager choose a dashboard and select Save as report template . 

 Click Edit to make changes to the template or to run the report without making changes, select Generate report . 

 2 

 Build your report layout 

 Add or remove widgets from your canvas: Drag widgets directly onto the canvas from the Widget Library : 

 Predefined Widgets: Search the Widget library (filter by Owner, Category, Chart type, or data source) and drag your selected widgets onto the canvas. Click on a widget to see a graphical preview and configuration details. 

 Tip: To find widgets that can be modified, select the Editable widget only option. These widgets can be duplicated and edited to suit your specific needs without starting from scratch. 

 Custom Widgets: If the library does not contain the widgets you require, you can create custom widgets using XQL queries, scripts, or generate them using AI. For more information, see Create custom widgets . 

 (Optional) Refine widget data: For certain widgets you can refine the displayed data as follows: 

 For agent-related widgets, you can apply an endpoint scope to refine the displayed data to only show results from specific endpoint groups. Select the menu on the top right corner of the widget, select Groups , and select one or more endpoint groups. 

 For case-related widgets, you can refine the displayed data to only show results from cases that match a case starring configuration. A purple star indicates that the widget is displaying only starred cases. For more information, see <Case starring>. 

 3 

 Configure filters 

 If your report contains custom XQL widgets with defined parameters, you can add configure filters to refine the data in your report. Follow the steps in Configure Global Filters . 

 4 

 Finalize the layout 

 Name your report: Enter a unique, descriptive name in the title field. 

 (Optional) Add static text: Click Static Elements to add headers, titles, or free text blocks. 

 Arrange the layout: Reports are formatted in A4 pages. You can scroll all pages in the report in the navigation panel. To optimize the space in the report, select Auto arrange layout from the Settings menu, or arrange the widgets manually. 

 5 

 Save and define report settings 

 Open save settings: Click the Save button in the report builder header. 

 Add a description: Provide a detailed description explaining the purpose of the report to help other users identify its use case. 

 Configure timeframe: Select the timeframe for the widget data. 

 Configure automated distribution and scheduling settings: including email recipients, Slack notifications, delivery, and scheduling. 

 To send reports to Slack, Slack must be configured as an external application. For more information, see Integrate Slack for outbound notifications 

 Configure CSV data attachments: Select Attach CSV to include raw data from XQL widgets. From the menu, select one or more of your custom widgets to attach to the report. The CSV files of the widgets are attached to the report along with the report PDF. Depending on how you selected to send the report, the CSV file is attached as follows: 

 Email: Sent as separate attachments for each widget. The total size of the attachment in the email cannot exceed 20 MB. 

 Slack: Sent within a ZIP file that includes the PDF file. 

 Save the report: Click Save to commit all changes. 

 Tip: You can configure a notification rule to send an email or send a notification to a syslog server if a report fails to run due to a timeout or fails to upload to the GCP bucket. For more information see Configure the notification rule for a failed report . 

 6 

 Share the report template 

 By default, all new custom report templates are Restricted and visible only to you (the Owner). Once created, you can share the report template with specific users or groups, or make it Public to all authorized users. 

 Sharing of report templates must be enabled by your administrator. For more information, see Manage access to objects . 

 How to share a dashboard 

 Open share settings: In the Report templates tab, find the template name and select Share from the right-click menu. 

 Update your visibility settings: 

 To share globally: Under General access , change the setting to Public so all authorized users in your organization can view it. 

 To share selectively: Keep the status as Restricted , add specific users or groups, and assign them a role ( Viewer or Editor ). 

 Save your changes: Click Share to apply your settings. 

 Previous Create reports 

 Next Advanced configuration 

 Last updated 1 month ago 

 Was this helpful?
