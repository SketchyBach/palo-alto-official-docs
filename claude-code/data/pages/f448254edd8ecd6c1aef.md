---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-3.x/cortex-xdr-3.x-documentation/cortex-xdr-xql/functions/count
fetched_at: 2026-09-16T08:44:21Z
source: cortex-platform
---

# count | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

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

 count 

 Learn more about the Cortex Query Language count function used with both comp and windowcomp stages. 

 Syntax 

 comp stage 

 Ask Copy 

 comp count([<field>]) [as <alias>] by <field_1>,<field_2> [addrawdata = true|false [as <target field>]] 

 windowcomp stage 

 Ask Copy 

 windowcomp count([<field>]) [by <field> [,<field>,...]] [sort [asc|desc] <field1> [, [asc|desc] <field2>,...]] [between 0|null|<number>|-<number> [and 0|null|<number>|-<number>] [frame_type=range]] [as <alias>] 

 Description 

 The count() function is used to return a single count for the number of rows either for a field over a group of rows, where only the number of non-null values found are returned, or without a field to count the number of rows, including null values. The function syntax and application is based on the preceding stage: 

 comp stage 

 When the count aggregation function is used with a comp stage, the function returns one of the following: 

 With a field: Returns a single count for the number of non-null rows, for all records that contain matching values for the fields identified in the by clause. 

 Without a field: Counts the number of rows and includes null values. 

 In addition, you can configure whether the raw data events are displayed by setting addrawdata to either true or false (default), which are used to configure the final comp results. When including raw data events in your query, the query runs for up to 50 fields that you define and displays up to 100 events. 

 Use count_distinct to retrieve the number of unique values in the result set. 

 windowcomp stage 

 When the count aggregate function is used with a windowcomp stage, the function returns one of the following: 

 With a field: Returns a single count for the number of non-null rows for all records that contain matching values for the fields identified using a combination of the by clause, sort , and between window frame clause. The results are provided in a new column in the results table. 

 Without a field: Counts the number of rows and includes null values. 

 Examples 

 comp example 

 Return a single count of all values found for the actor_process_image_path field in the group of rows, for all records that have matching values for their actor_process_image_path and actor_process_command_line values. The query calculates a maximum of 100 xdr_data records and includes a raw_data column listing a single value for the results. 

 windowcomp example 

 Return a single count for the number of values found in the dns_query_name field for each row in the group of rows, for all records that contain matching values in the agent_ip_addresses field. The query returns a maximum of 100 xdr_data records. The results are provided in the count_dns_query_name column. 

 Previous convert_from_base_64 

 Next count_distinct 

 Last updated 1 month ago 

 Was this helpful?
