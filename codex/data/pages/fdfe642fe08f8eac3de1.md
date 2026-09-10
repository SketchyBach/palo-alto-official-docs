---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-3.x/cortex-xdr-3.x-documentation/cortex-xdr-xql/stages/filter
fetched_at: 2026-09-06T09:51:15Z
source: cortex-platform
---

# filter | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR 

 Cortex XDR 3.x Documentation 

 Cortex XDR 3.x Documentation 

 Cortex XDR XQL 

 Stages 

 Cortex XDR 3.x 

 filter 

 Learn more about the Cortex Query Language filter stage that narrows down the displayed results. 

 Syntax 

 Ask Copy 

 filter <boolean expr> 

 Description 

 The filter stage identifies which data records should be returned by the query. Filters are boolean expressions that can use a wide range of functions and operators to express the filter. If a record matches the filter as the filter expression returns true when applied to the record, the record is returned in the query's result set. 

 The functions you can use with a filter are described in Functions . For a list of supported operators, see Supported operators . 

 Single vs triple double quotes behavior 

 Cortex XDR enables you to use single double quotes ( "<text>" ) or triple double quotes ( """<text>""" ) when defining your XQL syntax for string manipulation. This specific syntax is used with different stages, functions, and operators, with or without wildcards. Typically, the alter and filter stages are used with single or triple double quotes. 

 Using single double quotes 

 Single double quotes ( "<text>" ) include the following functionality: 

 Treats the string value literally. 

 Wildcards using the asterisk (*) are processed as XQL wildcards, and match any sequence of characters. 

 Escape sequences, such as \n (new line) or \t (tab), are not processed and are treated as plain characters. 

 Example: 

 "\test\" means to look for \test\ 

 Using triple double quotes 

 Triple double quotes ( """<text>""" ) include the following functionality: 

 Enables regex-style pattern matching and escape sequence interpretation. 

 Escape sequences, such as \n (new line) or \t (tab), are processed. 

 Wildcards using the asterisk (*) are processed as XQL wildcards, and match any sequence of characters. 

 Example: 

 """\\test\\""" means to look for \test\ 

 Understanding the results : 

 The double backslashes ( \\ ) at the beginning becomes a single backlash ( \ ) as it's processed as an escaped backslash. 

 test is interpreted as literal. 

 The double backslashes ( \\ ) at the end becomes a single backlash ( \ ) as it's processed as an escaped backslash. 

 Query example using filter 

 When using the filter stage, you can use both single ( "<text>" ) and triple ( """<text>""" ) double quotes when specifying string values. The difference lies in how special characters and pattern matching are interpreted. 

 The examples provided are based on the following data table for a dataset called test_dataset : 

 _TIME 

 TEST 

 Mar 26th 2022 19:26:07 

 12\t3 

 May 7th 2023 15:16:00 

 12 3 

 Jun 8th 2024 16:56:27 

 1233 

 Mar 26th 2024 19:26:07 

 123 

 Apr 5th 2024 11:21:02 

 12\t34563 

 Apr 9th 2025 13:22:22 

 1233345 

 May 9th 2025 13:22:22 

 12 35897 

 May 30th 2025 21:45:02 

 116 

 Example: 

 Ask Copy 

 config timeframe = 10y 
 | dataset = test_dataset 
 | filter test = "12\t3*" 
 | fields test 

 Output results table : 

 _TIME 

 TEST 

 Mar 26th 2022 19:26:07 

 12\t3 

 Apr 5th 2024 11:21:02 

 12\t34563 

 Explanation of results : 

 The asterisk ( * ) in "12\t3*" means to process the string field as an XQL wildcard by matching any sequence of characters that begins with 12\t3 . In addition, the \t characters are not processed as an escape character, but as plain characters. 

 Example: 

 Ask Copy 

 config timeframe = 10y 
 | dataset = test_dataset 
 | filter test = """12\t3*""" 
 | fields test 

 Output results table : 

 _TIME 

 TEST 

 May 7th 2023 15:16:00 

 12 3 

 May 9th 2025 13:22:22 

 12 35897 

 Explanation of results : 

 The \t in """12\t3*""" is processed as a tab escape character. The asterisk ( * ) in """12\t3*""" means to process the string field as an XQL wildcard by matching any sequence of characters that begins with 12<tab>3 . 

 Examples 

 Return xdr_data records where the event_type is NETWORK and the event_sub_type is NETWORK_HTTP_HEADER . 

 Note 

 When entering filters to the XQL Search user interface, possible field values for fields of type enum are available using the auto-complete feature. However, the autocomplete can only show enum values that are known to the schema. In some cases, on data import an enum value is included that is not known to the defined schema. In this case, the value will appear in the result set as an unknown value, such as event_type_unknown_4 . Be aware that even though this value appears in the result set, you cannot create a filter using it. For example, this query will fail, even if you know the value appears in your result set: 

 When using fields of type enum , the following syntax is supported. 

 Syntax format A 

 Syntax format B 

 Previous fields 

 Next getrole 

 Last updated 10 days ago 

 Was this helpful?
