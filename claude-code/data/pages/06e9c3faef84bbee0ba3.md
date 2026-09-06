---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-administrator-guide/6.12/configure-cortex-xsoar/customize-and-configure-cortex-xsoar/dashboards/dashboard-overview
fetched_at: 2026-09-06T10:48:55Z
source: cortex-platform
---

# Dashboard Overview | 6.12 (EoL) | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Administrator Guides 

 6.12 (EoL) 

 Configure Cortex XSOAR 

 Customize and Configure Cortex XSOAR 

 Dashboards 

 Cortex XSOAR 6.12 EoL 

 Dashboard Overview 

 Understand dashboards and widgets in Cortex XSOAR 6.12. 

 The dashboard consists of visualized data powered by fully customizable widgets, which enables you to analyze data from inside or outside Cortex XSOAR, in different formats such as graphs, pie charts, or text. For more information about widgets, see Widgets Overview . 

 When you first install Cortex XSOAR, the following dashboard tabs are created: 

 Dashboard 

 Description 

 My Dashboard 

 A personalized dashboard relating to your incidents, tasks, etc. 

 My Threat Landscape 

 Information about malicious/suspicious indicators in incidents, top 10 indicators in related incidents, Unit 42 feed (if enabled). 

 System Health 

 Information relating to the Cortex XSOAR Server. 

 SLA 

 Information relating to your Service Level Agreements. 

 Troubleshooting Playbooks 

 Information relating to playbook run and execution errors. 

 Incidents 

 Information relating to incidents, such as severity type, active incidents, unassigned incidents, etc. 

 API Execution Metrics 

 Information about API calls. You can use the API Execution Metrics for Enrichment Command widget for troubleshooting and to make decisions about indicator enrichment. 

 Cost Optimization Playbooks 

 Information about playbooks including task executions, average runtime, etc. 

 Troubleshooting Instances 

 Information about integration instance errors. 

 Threat Intelligence Feeds 

 Information about TIM feeds that are being ingested into Cortex XSOAR. 

 Cost Optimization Instances 

 Information about commands that have been executed in Cortex XSOAR. 

 MITRE ATT&CK 

 Information about MITRE ATT&CK techniques. Part of the MITRE ATT&CK content pack . 

 Note 

 You can add this to your dashboard when clicking Add dashboard . 

 Threat Intel Management 

 Information about active indicators by reputation, type, expired indicators, etc. 

 Note 

 You can add this to your dashboard when clicking Add dashboard . 

 VirusTotal API Execution Metrics 

 Information about VirusTotal API commands. Part of the VirusTotal content pack . 

 Note 

 You can add this to your dashboard when clicking Add dashboard . 

 If you install a content pack which contain dashboards, these can be added when creating a new dashboard. To change the order of the dashboards, click next to the relevant dashboard, and then drag and drop the dashboard into the required location. 

 Dashboard Options 

 In every dashboard, you can set the date range from which to return data and the refresh rate. In the DASHBOARDS tab, you can do the following: 

 Filter Data for all widgets 

 You can filter dashboard data by either typing the query in the query bar, or in the relevant widget, by clicking Filter In . When clicking Filter In the query is added to the query bar. To filter out, delete the query. For example, if you only want to see Cortex XDR incidents that are critical, in the Incident Severity by Type widget, hover over the Cortex XDR incident and click Filter In . 

 Note 

 In widgets that group excess results under an Other category (such as the Owners widget), you cannot use the Filter in or Filter out options for the Other item. Doing so creates a search query that returns no results. To view or filter these excess items, create a custom widget and increase the limit of displayed results or disable the grouping option. 

 dashboards-pivot.png 

 In the Active Incidents by Severity widget, hover over Critical and click Filter In . The dashboard only shows active critical incidents relating to Cortex XDR. 

 widget-filter.png 

 To remove the filter, delete the query. 

 Tip 

 If you want to see more information about the data, click the data to take you to the relevant page. For example, in the Active Incidents by Severity widget, to see only critical incidents, click Critical . This takes you to the Incident page, where you can see all the active critical incidents. 

 After you have created the filter, you can send the URL of the filtered dashboard to other users. 

 Change Color of Items in Widgets : You can change the color of items (such as indicator types, incident types, etc.) in some widgets, depending on the widget type and the chart/graph type. While viewing a dashboard, hover over the relevant legend item, click the ellipses, and select Edit color . For example, you can change the display color for the Phishing incident type within the Active Incidents widget. Changes you make to a widget while viewing or editing a dashboard only apply to the widget in that dashboard. To make changes that apply every time you use the widget in a report or dashboard, edit the widget directly in the Widgets Library . 

 Copy the value : While viewing a dashboard, you can click on the ellipses next to an item in the legend and select Copy value . This enables you to copy the value from the widget for commands in the War Room, etc. 

 Create a Dashboard 

 Edit a Dashboard 

 Import and export a dashboard, which is useful in a test and production environment. 

 The dashboard is exported as a JSON file. You can make any changes you require and then import the file. 

 Add default dashboards 

 In a production environment, an administrator defines the default dashboards for each user, which is dependent on a user’s role. If a user has not modified their dashboard, these dashboards are added automatically, otherwise users can add these dashboards to their existing dashboards. These default dashboards can be removed but not deleted, and can be added again if required. 

 Share a Dashboard 

 Duplicate, delete or remove (if shared) a dashboard. 

 Create a report 

 You can generate a report from the dashboard as is, or add new widgets as required. You can set the format, when to run, orientation, etc. To run the report, click Run Now . The Report is generated and it also appears in the Reports tab, which can be run again. For more information about creating reports, see Create a Report . 

 Previous Dashboards 

 Next Create a Dashboard 

 Last updated 3 days ago 

 Was this helpful?
