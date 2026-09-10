---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-3.x/cortex-xdr-3.x-documentation/cortex-xdr-xql/functions/approx_count
fetched_at: 2026-09-06T09:51:21Z
source: cortex-platform
---

# approx_count | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

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

 approx_count 

 Learn more about the Cortex Query Language approx_count approximate aggregate comp function. 

 Syntax 

 Ask Copy 

 comp approx_count(<field>) [as <alias>] [by <field1>[,<field2>...]] [addrawdata = true|false [as <target field>]] 

 Description 

 The approx_count approximate aggregate is a comp function that counts the number of distinct values in the given field over a group of rows. For the group of rows, the function returns an approximate result as a single interger value, for all records that contain matching values for the fields identified in the by clause. Use this approximate aggregate function to produce approximate results, instead of exact results used with regular aggregate functions, which are more scalable in terms of memory usage and time. This approximate aggregate function is used in combination with a comp stage. 

 In addition, you can configure whether the raw data events are displayed by setting addrawdata to either true or false (default), which are used to configure the final comp results. When including raw data events in your query, the query runs for up to 50 fields that you define and displays up to 100 events. 

 Example 

 Returns a single integer value after approximately counting the number of distinct values in the event_id field over a group of rows. 

 Ask Copy 

 dataset = xdr_data 
 | fields event_id 
 | comp approx_count(event_id) 

 Previous add 

 Next approx_quantiles 

 Last updated 1 month ago 

 Was this helpful?
