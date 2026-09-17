---
url: https://cortex-docs.paloaltonetworks.com/xql-command-reference-guide/readme/functions/format_timestamp
fetched_at: 2026-09-16T09:04:54Z
source: cortex-platform
---

# format_timestamp | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 XQL 

 XQL Command Reference Guide 

 Cortex XQL Command Reference 

 Functions 

 format_timestamp 

 Use the format_timestamp() function to return a string by formatting a given timestamp according to a specified string format. 

 Syntax 

 Ask Copy 

 format_timestamp ( " <format string> " , < timestamp field > [, "<time zone>"]) 

 Parameters 

 Name 

 Type 

 Required 

 Description 

 format_string 

 string 

 Yes 

 The string literal that defines how the timestamp will be formatted (for example, %Y/%m/%d %H:%M:%S ). 

 timestamp_field 

 timestamp 

 Yes 

 The timestamp value to be formatted. 

 time_zone 

 string 

 No 

 An optional time zone specified using either an hours offset (for example, +08:00 ) or a time zone name (for example, America/Chicago ). The default is UTC. 

 Returns 

 The format_timestamp() function returns a string representation of the timestamp. 

 Usage notes 

 The function requires a format string and a timestamp field as input. 

 An optional time zone can be specified to adjust the displayed time. 

 If no time zone is configured, the function defaults to UTC. 

 This function is typically used within the alter stage to create new fields containing formatted time strings. 

 Examples 

 Example 1: Without a time zone configured 

 Goal : Format the _time field into a specific string format using the default UTC time zone. 

 XQL code : 

 Explanation : The _time field, which is in UTC, is formatted directly into a string. Since no time zone is specified in the format_timestamp() function, the output new_time string reflects the UTC time. 

 Output : 

 EVENT_ID 

 _TIME 

 NEW_TIME 

 101 

 Oct 26th 2023 10:00:00 

 2023/10/26 10:00:00 

 102 

 Oct 26th 2023 10:05:30 

 2023/10/26 10:05:30 

 103 

 Oct 26th 2023 10:15:15 

 2023/10/26 10:15:15 

 Example 2: With a time zone configured using an hours offset 

 Goal : Format the _time field into a string, adjusting the time by a specific hours offset. 

 XQL code : 

 Explanation : The _time field (UTC) is adjusted by adding three hours ( +03:00 ) before it is formatted into the new_time string. For example, 10:00:00 UTC becomes 13:00:00 in the formatted string. 

 Output : 

 EVENT_ID 

 _TIME 

 NEW_TIME 

 101 

 Oct 26th 2023 10:00:00 

 2023/10/26 13:00:00 

 102 

 Oct 26th 2023 10:05:30 

 2023/10/26 13:05:30 

 103 

 Oct 26th 2023 10:15:15 

 2023/10/26 13:15:15 

 Example 3: With a time zone name configured 

 Goal : Format the _time field into a string, applying a specific named time zone. 

 XQL code : 

 Explanation : The _time field (UTC) is converted to the America/Chicago time zone (UTC-5 for this date) before being formatted. For example, 10:00:00 UTC becomes 05:00:00 in the formatted new_time string. 

 Output : 

 EVENT_ID 

 _TIME 

 NEW_TIME 

 101 

 Oct 26th 2023 10:00:00 

 2023/10/26 05:00:00 

 102 

 Oct 26th 2023 10:05:30 

 2023/10/26 05:05:30 

 103 

 Oct 26th 2023 10:15:15 

 2023/10/26 05:15:15 

 Related articles 

 Stages : alter , config , fields , limit 

 Functions : parse_timestamp , to_timestamp 

 Previous format_string 

 Next greatest 

 Last updated 3 months ago 

 Was this helpful?
