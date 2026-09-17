---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-administrator-guide/6.14/customize-cortex-xsoar/customize-and-configure-cortex-xsoar/widgets/create-a-custom-widget-using-a-json-file
fetched_at: 2026-09-16T08:56:29Z
source: cortex-platform
---

# Create a Custom Widget Using a JSON File | 6.14 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

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

 Create a Custom Widget Using a JSON File 

 Create custom Cortex XSOAR 6.14 widgets from JSON files for dashboards and reports. 

 You can create a custom widget for your dashboard or report using a JSON file and then add the new widget to a new or edited dashboard or report. If you want to create more complicated widgets using scripts, see Create a Custom Widget Using an Automation Script . 

 Create a JSON file, and add the JSON File Widget Parameters . 

 Create or edit a dashboard or report. 

 In the Widget Library section, select the add button → Upload . 

 Select the JSON file you created in step 1 and click Open . 

 To add the widget to the dashboard or report, click Add . 

 JSON File Widget Parameters 

 The following table describes the parameters for a JSON file when creating a widget. For an example of a JSON file, see JSON File Widget Example . 

 Parameter 

 Description 

 id 

 The unique identifier for the widget. 

 definitionId 

 The definition ID of the widget. Used for widgets with a datatype of generics to define the object type of the widget. This parameter currently supports widgets with a data source of Threat Intel Reports . Any such widgets must be given a definitionId value of ThreatIntelReport . 

 name 

 The display name of the widget. 

 dataType 

 The data source of the widget. Must be one of the following: 

 incidents 

 indicators 

 messages 

 entries 

 scripts 

 Relevant only when you are creating an automation script. 

 tasks 

 generics 

 Relevant when creating Threat Intel reports. When used, the definitionId value must be ThreatIntelReport . 

 query 

 Queries query data in the Lucene query syntax form relating to the dataType . For example when dataType is incidents and the query is: -status:closed and owner:"" , it queries all incidents that are not closed, which does not have an owner. 

 For script based widgets, the query is the name of the script. 

 sort 

 Sorts the data, when displaying the widgetType (applies to table and list widget types) as a list of objects, which consists of the following: 

 field : The field name for which to sort. 

 asc : Whether to sort data in ascending values. If true, the order is in ascending value. 

 widgetType 

 The type of widget you want to create. Must be one of the following: 

 bar 

 column 

 pie 

 number 

 line 

 table 

 trend 

 list 

 duration 

 image 

 size 

 The maximum number of returning elements. Use ** 0 **for the widgetType 's default. 

 Note 

 Table/List : To change the size, go to Settings → About → Troubleshooting → Add Server Configuration add the default.statistics.table.size. key and then add the value. Default is up to 13 

 Chart : Default is up to 10. 

 Number and Trend : Ignores the size value. 

 category 

 Adds a category name. The widget appears under a category instead of being classified by dataType . 

 dataRange 

 The time period for which to return data. The time period is overridden by the dashboard or report time period. Default is all times. 

 fromDate : The start date from which to return data in the format: “YYYY-MM-DDTHH:MM:SSZ” . For example, "2019-01-01T16:30:00Z" . 

 toDate : The end date for which to return data in the format: "YYYY-MM-DDTHH:MM:SSZ" . For example, "2019-01-01T16:30:00Z" . 

 period : An object describing a period of relative time. If using the fromDate/toDate parameters, this parameter is ignored. 

 byTo : The to period unit of measurement. Values are ‘minutes', 'hours', 'days', 'weeks', 'months' . 

 byFrom : The from period unit of measurement. Values are: 'hours', 'days', 'weeks', 'months' . 

 toValue : The duration of the to period. Integer. 

 fromValue : The duration of the from period. Integer. For example, last 7 days - { byFrom: 'days', fromValue: 7 } . 

 description 

 The description of the widget in the Widget Library. 

 params 

 Enriches the widget with specific parameters, mainly based on the widgetType . Includes the following: 

 groupBy : An array of field names for which to group the returned values. Used when widget type is bar, column, line or pie. For example, ["type", "owner"] : Groups results by type and owner, and returns a nested result for each type with statistics according to the owner. 

 Note 

 Bar/column charts defined with two groups can become stacked. 

 hideLegend : Shows or hides the legend, if it exists. Default is false. 

 keys : An array that enables processing the data value and modifies it by the given list of keys. For example, **`["avg 

 legend 

 An array of objects that consists of a name and color. The name must match a group name. The color can be the name of the color, the hexadecimal representation of the color, or the rgb color value. 

 JSON File Widget Example 

 In the following example, create a JSON file to display incident severity by type, which contains the following: 

 Bar chart 

 Incidents from the last 30 days 

 Grouped by severity and for each severity display the nested group size (count of incidents displayed by the length of the bar) colored according to type. 

 Create the following JSON file: 

 You can see the following parameters: 

 The Widget is called Incident Severity by type . 

 The data type is incidents . 

 The widget type is bar . 

 The query specifies that you do not want to return incidents that are categorized as job nor incidents that are archived and closed. 

 For the date range, the fromValue sets the widget to display the last 30 units of time. The byFrom sets the units of time to days, which results in the last 30 days. 

 The params parameter is set with a groupBy value marking the first group by severity name and then by type (making the bar chart stacked). 

 After you import the widget into the Widget Library the following widget appears: 

 widget_incident.png 

 You can see the incidents are grouped by severity and the number of incidents are displayed by the length of the bar, which are colored according to type. 

 In the next example, create a JSON file to display incidents by type. The widget contains the following: 

 Vertical bar chart 

 Incidents from the last 7 days 

 Grouped by date and type and sorted by date occurred 

 You can see the following parameters: 

 The Widget is called Change Sort Order In Column Chart - Sort by Date . 

 The data type is incidents . 

 The widget type is column . 

 For the date range, the fromValue sets the widget to display the last 7 units of time. The byFrom sets the units of time to days, which results in the last 7 days. 

 The params parameter is set with a groupBy value marking the first group by occurrence date and then by type (making the column chart stacked). 

 After you import the widget into the Widget Library the following widget appears: 

 widget-example2.png 

 Previous Create a Widget using the Widget Builder 

 Next Create a Custom Widget Using an Automation Script 

 Last updated 13 days ago 

 Was this helpful?
