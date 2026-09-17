---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-3.x/cortex-xdr-3.x-documentation/cortex-xdr-xql/functions/avg
fetched_at: 2026-09-16T08:44:21Z
source: cortex-platform
---

# avg | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR 

 Cortex XDR 3.x Documentation 

 Cortex XDR 3.x Documentation 

 Cortex XDR XQL 

 Functions 

 Cortex XDR 3.x 

 avg 

 Learn more about the Cortex Query Language avg used with both comp and windowcomp stages. 

 Syntax 

 comp stage 

 Ask Copy 

 comp avg(<field>) [as <alias>] by <field_1>,<field_2> [addrawdata = true|false [as <target field>]] 

 windowcomp stage 

 Ask Copy 

 windowcomp avg(<field>) [by <field> [,<field>,...]] [sort [asc|desc] <field1> [, [asc|desc] <field2>,...]] [between 0|null|<number>|-<number> [and 0|null|<number>|-<number>] [frame_type=range]] [as <alias>] 

 Description 

 The avg() function is used to return the average value of an integer field over a group of rows. The function syntax and application is based on the preceding stage: 

 comp stage 

 When the avg aggregation function is used with a comp stage, the function returns a single average value of an integer field for a group of rows, for all records that contain matching values for the fields identified in the by clause. 

 In addition, you can configure whether the raw data events are displayed by setting addrawdata to either true or false (default), which are used to configure the final comp results. When including raw data events in your query, the query runs for up to 50 fields that you define and displays up to 100 events. 

 windowcomp stage 

 When the avg aggregate function is used with a windowcomp stage, the function returns a single average value of an integer field for each row in the group of rows, for all records that contain matching values for the fields identified using a combination of the by clause, sort , and between window frame clause. The results are provided in a new column in the results table. 

 Examples 

 comp example 

 Return a single average value of the action_total_download field for a group of rows, for all records that have matching values for their actor_process_image_path and actor_process_command_line values. The query calculates a maximum of 100 xdr_data records and includes a raw_data column listing a single value for the results. 

 Ask Copy 

 dataset = xdr_data 
 | fields actor_process_image_path as Process_Path, actor_process_command_line as Process_CMD, action_total_download as Download 
 | filter Download > 0 
 | limit 100 
 | comp avg(Download) as average_download by Process_Path, Process_CMD 
 addrawdata = true as raw_data 

 windowcomp example 

 Return the events that are above average per Process_Path and Process_CMD . The query returns a maximum of 100 xdr_data records in a column called avg_download . 

 Ask Copy 

 dataset = xdr_data 
 | fields actor_process_image_path as Process_Path, actor_process_command_line as Process_CMD, action_total_download as Download 
 | filter Download > 0 
 | limit 100 
 | windowcomp avg(Download) by Process_Path, Process_CMD as avg_download 
 | filter Download > avg_download 

 Previous arraystring 

 Next coalesce 

 Last updated 1 month ago 

 Was this helpful?
