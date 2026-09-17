---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-3.x/cortex-xdr-3.x-documentation/investigate-and-respond-to-incidents/dashboards/custom-dashboards/configure-dashboard-drilldowns/variables-in-drilldowns
fetched_at: 2026-09-16T08:44:14Z
source: cortex-platform
---

# Variables in drilldowns | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR 

 Cortex XDR 3.x Documentation 

 Cortex XDR 3.x Documentation 

 Investigate and respond to incidents 

 Dashboards 

 Custom dashboards 

 Configure dashboard drilldowns 

 Cortex XDR 3.x 

 Variables in drilldowns 

 Learn about the widget variable values that you can use in dashboard drilldowns. 

 The following list describes the widget variables that are available in drilldowns, according to widget type. The variable defines the value to capture in the drilldown, according to the element that is clicked. The captured value is then configured as a parameter by which to filter data on drilldown. 

 Chart (Area, Bubble, Column, Funnel, Line, Map, Pie, Scatter, or Word Cloud) 

 DD_example_chart.png 

 $x_axis.name : Selects the x-axis name. 

 $x_axis.value : Selects the x-axis value for the clicked value. 

 $y_axis.name : Selects the y-axis name. 

 $y_axis.value : Selects the y-axis value for the clicked value. 

 Single value or gauge 

 DD_example_gauge.png 

 $y_axis.name : Selects the y-axis name that the single value represents. 

 $y_axis.value : Selects the y-axis value for the clicked value. 

 Table 

 DD_example_table.png 

 $first.name : Selects the leftmost column name in the table. 

 $first.value : Selects the leftmost value in the clicked table row. 

 $clicked.name : Selects the column name of the clicked value. 

 $clicked.value : Selects the value in the clicked table cell. 

 $row.<field_name> : Selects the field (column) from the clicked table row. 

 Previous Configure dashboard drilldowns 

 Next Reports 

 Last updated 1 month ago 

 Was this helpful?
