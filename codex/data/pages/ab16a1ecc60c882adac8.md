---
url: https://cortex-docs.paloaltonetworks.com/xql-command-reference-guide/readme/functions/avg_with_windowcomp_stage
fetched_at: 2026-09-06T10:58:22Z
source: cortex-platform
---

# avg (windowcomp) | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 XQL 

 XQL Command Reference Guide 

 Cortex XQL Command Reference 

 Functions 

 avg (windowcomp) 

 Use the avg() function within the windowcomp stage to calculate and return a single average value of a specified numerical field over a defined "window" or group of rows. The resulting average value is then presented for each row within that window frame, allowing for contextual statistical analysis without collapsing rows. 

 Syntax 

 Ask Copy 

 windowcomp avg ( < field > ) [by <field> [,<field>,...]] [sort [asc|desc] < field1 > [, [asc|desc] < field2 > ,...]] [between 0|null|<number>|-<number> [and 0|null|<number>|-<number>] [frame_type=range]] [as <alias>] 

 Parameters 

 Name 

 Type 

 Required 

 Description 

 field 

 numeric 

 Yes 

 The numerical field for which the average will be calculated. 

 by field 

 string 

 No 

 Partitions the data into distinct groups, allowing the avg() function to operate independently within each of these partitions. 

 sort field 

 string 

 No 

 Defines the order of rows within each partition. This ordering is critical when defining a window using the between clause. 

 between clause 

 string 

 No 

 Defines the "window frame"—a specific range of rows relative to the current row—over which the avg() function calculates. 

 alias 

 string 

 No 

 Assigns an alias name to the new column displaying the result. 

 Returns 

 The avg() function returns a single numerical value representing the average for the defined window. This value is displayed in a new column for every row in the group of rows it applies to. 

 Usage Notes 

 The windowcomp stage must always precede analytic functions like avg() that calculate statistics. 

 Only one function can be defined per field within a single windowcomp stage. 

 If the between clause is omitted, the default window typically encompasses the entire partition. 

 Examples 

 Example 1: avg() over an entire partition (default window) 

 Goal : Calculate the average of duration_seconds for all events within each is_successful group (partition), and replicate this single average value for every row in that group. 

 XQL Code : 

 Explanation : The by is_successful clause partitions the data into two groups: one for false and one for true. The avg() function then calculates the average of the duration_seconds field for each partition. The result is a single average value for each partition, which is then displayed for every row in that partition. The sort clause ensures the rows are ordered by is_successful,_time, and event_id for consistent presentation of the data. 

 Output : 

 _time 

 event_id 

 is_successful 

 duration_seconds 

 avg_in_partition 

 2023-10-26 10:05:30 UTC 

 102 

 false 

 0.8 

 0.9833 

 2023-10-26 10:40:10 UTC 

 106 

 false 

 2.1 

 0.9833 

 2023-10-26 10:55:55 UTC 

 109 

 false 

 0.05 

 0.9833 

 2023-10-26 10:00:00 UTC 

 101 

 true 

 1.5 

 14.2714 

 2023-10-26 10:15:15 UTC 

 103 

 true 

 10.2 

 14.2714 

 2023-10-26 10:20:00 UTC 

 104 

 true 

 0.1 

 14.2714 

 2023-10-26 10:30:45 UTC 

 105 

 true 

 5.0 

 14.2714 

 2023-10-26 10:45:00 UTC 

 107 

 true 

 7.8 

 14.2714 

 2023-10-26 10:50:20 UTC 

 108 

 true 

 15.3 

 14.2714 

 2023-10-26 11:00:10 UTC 

 110 

 true 

 60.0 

 14.2714 

 Example 2: avg() with a rolling window (preceding 2 rows and current row)** 

 Goal : Calculate a rolling average from the duration_seconds of the current row and the two immediately preceding rows within its partition, ordered by _time. 

 XQL Code : 

 Explanation : The code defines a rolling window using between -2 and 0 which includes the current row (0) and the two immediately preceding rows (-2, -1) within its partition. For each row, the avg() function calculates the average of duration_seconds strictly within this rolling window. If there are not enough preceding rows, the window starts from the beginning of the partition. 

 Output : 

 _time 

 event_id 

 is_successful 

 duration_seconds 

 rolling_avg 

 2023-10-26 10:05:30 UTC 

 102 

 false 

 0.8 

 0.8 

 2023-10-26 10:40:10 UTC 

 106 

 false 

 2.1 

 1.45 

 2023-10-26 10:55:55 UTC 

 109 

 false 

 0.05 

 0.9833 

 2023-10-26 10:00:00 UTC 

 101 

 true 

 1.5 

 1.5 

 2023-10-26 10:15:15 UTC 

 103 

 true 

 10.2 

 5.85 

 2023-10-26 10:20:00 UTC 

 104 

 true 

 0.1 

 3.9333 

 2023-10-26 10:30:45 UTC 

 105 

 true 

 5.0 

 5.1 

 2023-10-26 10:45:00 UTC 

 107 

 true 

 7.8 

 4.3 

 2023-10-26 10:50:20 UTC 

 108 

 true 

 15.3 

 9.3667 

 2023-10-26 11:00:10 UTC 

 110 

 true 

 60.0 

 27.7 

 Example 3: avg() with a fixed window (current row to unbounded following row) 

 Goal : Calculate the average for each row over a window that starts from the current row and extends to the end of its partition. 

 XQL Code : 

 Explanation : The code uses the between 0 and null clause to set a window starting from the current row (0) through to the very end of the partition (null). For each row, the avg() calculates the average of duration_seconds utilizing the current row's value up to the last value in its is_successful partition. 

 Output : 

 _time 

 event_id 

 is_successful 

 duration_seconds 

 avg_from_current 

 2023-10-26 10:05:30 UTC 

 102 

 false 

 0.8 

 0.9833 

 2023-10-26 10:40:10 UTC 

 106 

 false 

 2.1 

 1.075 

 2023-10-26 10:55:55 UTC 

 109 

 false 

 0.05 

 0.05 

 2023-10-26 10:00:00 UTC 

 101 

 true 

 1.5 

 14.2714 

 2023-10-26 10:15:15 UTC 

 103 

 true 

 10.2 

 16.4 

 2023-10-26 10:20:00 UTC 

 104 

 true 

 0.1 

 17.64 

 2023-10-26 10:30:45 UTC 

 105 

 true 

 5.0 

 22.025 

 2023-10-26 10:45:00 UTC 

 107 

 true 

 7.8 

 27.7 

 2023-10-26 10:50:20 UTC 

 108 

 true 

 15.3 

 37.65 

 2023-10-26 11:00:10 UTC 

 110 

 true 

 60.0 

 60.0 

 Related Articles 

 Stages : windowcomp , config , timeframe, dataset , fields , sort , limit 

 Functions : count , max , median , min , sum , stddev_population , stddev_sample 

 Previous avg (comp) 

 Next bitwise_and 

 Last updated 2 months ago 

 Was this helpful?
