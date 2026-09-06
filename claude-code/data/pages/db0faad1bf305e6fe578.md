---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-3.x/cortex-xdr-3.x-documentation/cortex-xdr-xql/functions/format_string
fetched_at: 2026-09-06T09:51:44Z
source: cortex-platform
---

# format_string | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

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

 format_string 

 Learn more about the Cortex Query Language format_string() function. 

 Syntax 

 Ask Copy 

 format_string("<format string>", <field_1>, <field_2>,...<field_n> ) 

 Description 

 The format_string() function returns a string from a format string that contains zero or more format specifiers, along with a variable length list of additional arguments that matches the format specifiers. A format specifier is initiated by the % symbol, and must map to one or more of the remaining arguments. Usually, this is a one-to-one mapping, except when the * specifier is used. 

 Examples 

 STRING 

 Ask Copy 

 dataset = xdr_data 
 | alter stylished_action_category_appID = format_string("-%s-", action_category_of_app_id ) 
 | fields stylished_action_category_appID 
 | limit 100 

 Simple integer 

 Ask Copy 

 dataset = xdr_data 
 | filter action_remote_ip_int != null 
 | alter simple_int = format_string("%d", action_remote_ip_int) 
 | fields simple_int 
 | limit 100 

 Integer with left blank padding 

 Ask Copy 

 dataset = xdr_data 
 | filter action_remote_ip_int != null 
 | alter int_with_left_blank = format_string("|%100d|", action_remote_ip_int) 
 | fields int_with_left_blank 
 | limit 100 

 Integer with left zero padding 

 Ask Copy 

 dataset = xdr_data 
 | filter action_remote_ip_int != null 
 | alter int_with_left_zero_padding = format_string("+%0100d+", action_remote_ip_int) 
 | fields int_with_left_zero_padding 
 | limit 100 

 Previous floor 

 Next format_timestamp 

 Last updated 1 month ago 

 Was this helpful?
