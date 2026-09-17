---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-administrator-guide/6.14/customize-cortex-xsoar/customize-and-configure-cortex-xsoar/widgets/create-a-widget-using-the-widget-builder
fetched_at: 2026-09-16T08:56:26Z
source: cortex-platform
---

# Create a Widget using the Widget Builder | 6.14 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Administrator Guides 

 6.14 

 Customize Cortex XSOAR 

 Customize and Configure Cortex XSOAR 

 Widgets 

 Cortex XSOAR 6.14 

 Create a Widget using the Widget Builder 

 Create Cortex XSOAR 6.14 widgets with the Widget Builder for dashboards and reports. 

 Widgets are visual components that populate dashboards and reports with specific data. Although there are various out-of-the-box system widgets available, you can create custom widgets in the Widgets Library. You can also create them from an incident or an indicator . 

 Create or edit a report or dashboard . 

 In the Widgets Library click the + button. 

 From the dropdown list, select one of the data type widgets, such as Incidents . 

 The relevant data is fetched into the data type. For example, when creating an incident type widget, the results are fetched. You can see a preview of the widget on the right hand side. 

 From the Quick chart definitions window, in the Query tab, define the widget data. 

 Add the following information: 

 Parameter 

 Description 

 Widget type 

 Select one of the widget types, by clicking on one of the graphics, such as pie chart, line chart, etc. 

 Widget Name 

 Type a meaningful name for the widget. 

 Data source 

 The type of data to query. 

 Incidents 

 Indicators 

 SOAR Metrics 

 War Room Entries 

 Tasks 

 Scripts 

 Threat Intel Reports 

 When selecting Scripts, if your script does not appear you need to add it to the Automation page and add the widget label. 

 Query 

 Queries data in the Lucene query syntax form relating to the data source. For example when the data source is incidents and the query is: -status:closed and owner:"" , it queries all incidents that are not closed, which does not have an owner. 

 Script 

 Select the script that you added when you created a custom widget using an automation script . Add the argument values, if required. 

 Date range 

 The time frame to retrieve data. 

 Select how you want to display the information, such as pie chart, timer widget, etc. You can see a preview of how the widget appears. 

 Configure the data as required, by clicking the Operations tab. 

 Not relevant for Script and Entries types. 

 In the Values section, select one of the following values: 

 Count 

 Average 

 Sum 

 Min 

 Max 

 (Not relevant for Count) Select one of the fields from the dropdown list or create your own custom calculations by selecting Custom calculations on fields . 

 If adding custom calculations, type the calculation as required. 

 The custom calculation modal suggests incident fields based on the widget data type, which are automatically validated. You can add your own fields (provided these fields exist), according to the widget data type, by using the CLI name. These fields are not validated. 

 In the Group by field, from the dropdown list, select the group you want to add. 

 By default the results are limited to the top 10 most popular results. If you want to change the top most popular to the least popular, change the number, or you want to see the remaining results that are not covered in one group (the Show ‘Others’ checkbox), click the edit button and update as required. 

 If you want to add a custom field, ensure that the Make data available for search field is checked, when editing or creating a new field. 

 (Optional) To define the groups (for example, you may want to define particular owners in the owner group): 

 Click Custom ‘Group by’ . 

 In the Create Custom groups window, click Equals (String) to change the operator. 

 Select a value from the dropdown list. 

 Change the name as required. 

 If you want to create a second group, click Add custom group . 

 If you want to add a group for all other values that have not been defined, click the Create and display a group for all remaining values checkbox. 

 In the Second group by field, add the group as required. For example, to see data filtered by owner and severity, select Group By Owner and Second Group by Severity. 

 Define how the widget appears by clicking the Visuals tab. 

 Add the following information: 

 Parameter 

 Description 

 Axis name 

 The name of the axis for both horizontal and vertical. 

 Format 

 Select the format of the table for both horizontal and vertical axis. For example, hours, minutes, days, weeks, etc. 

 Reference Line 

 Whether you want a line showing the average, minimum, maximum, or custom line. 

 Show Legend 

 Whether you want to see the legend in your widget. 

 Show also percentage 

 Displays the percentage when selecting a pie chart. 

 Show values on the graph 

 Add the values on the chart widget. 

 Display trend 

 Compares dates for a particular period in a number widget. For example, this week vs. last week, this year vs. last year, and so on. To change the comparison period, in the Time frame field from the dropdown list, select the relevant date. 

 Widget color threshold 

 Select the Widget color threshold in a number or duration widget to highlight the threshold data and define the threshold by selecting the Widget color threshold checkbox. For example, if less than 150 red, 100 yellow, 50 green. To add more thresholds, click Add new threshold . You can change the colors as required. 

 To change the color, in the preview section, hover next to the legend, click the ellipsis and then click Edit color . 

 Click Save . 

 The widget is added to the widgets library. 

 Add the widget to the dashboard or report. 

 When you add the widget, it automatically uses the date range of the dashboard or report. You can change it by clicking the settings icon and selecting Use widget’s date range. To revert, click the settings icon again and select Use dashboard’s date range 

 Create a Widget Using the Widget Builder Examples 

 Average Time to Close Incidents per Day 

 In this example we want to create a bar chart widget that shows the following: 

 The average time it takes to close incidents per day 

 Classified according to incident types 

 Incidents that occurred during the previous seven days 

 In the Widgets Library click the add button. 

 Select Incident data . 

 In the Query tab, define the following: 

 Data Type: Incidents 

 Data query: -category:job and -status:Closed. 

 Time frame: Last 7 days 

 Type: Bar chart 

 In the Operations tab: 

 Change Count to Average . 

 From the dropdown list, select Custom calculations on fields . 

 Type remediationsla.startDate-detectionsla.startDate 

 Group by: Data Occurred 

 Second Group by: Type 

 widget-example.png 

 How Many Incidents Occurred in the Last 7 Days 

 In this example, we want to view the following data: 

 How many incidents occurred in the last 7 days 

 Closed vs not closed (pending or active) 

 Line chart. 

 In the Quick Chart definitions window, use the following data: 

 widget-ex-quick.png 

 In the Operations tab, the first group is Date Occurred . 

 In the second group, from the dropdown list, select status . 

 Click Custom Group by to add the following data: 

 widget-eg.png 

 Average Time for Open Incidents That are Late 

 In this example, we want to create the following incident type widget: 

 The average time for open incidents that are late. 

 Grouped by two groups (group A and group B) and by type. 

 In a Bar Chart 

 In the Query tab, type: 

 widget-query.png 

 In the Operations tab, add the following information: 

 In the Values section, select Average . 

 From the dropdown list, click Custom calculations on fields . 

 Type {now}-remediationsla.dueDate . 

 We want to see the average time that incidents are late (from today’s date). We add a variable {now} , so that we do not have to change the date. 

 In the Group by field, select Owner and then click Custom Group by . 

 Add the following information: 

 widget-group.png 

 Select the Create and display a group for all remaining values checkbox. 

 We have additional users that are not in the groups that we want to see. 

 In the second group by field, from the dropdown list, select Type . 

 In the Visuals tab, select the following: 

 Horizontal options - Axis name: TEAM . 

 Vertical options - Axis name: REMEDIATION TIME . 

 widget-customgroup.png 

 Previous Widgets Overview 

 Next Create a Custom Widget Using a JSON File 

 Last updated 14 days ago 

 Was this helpful?
