---
url: https://cortex-docs.paloaltonetworks.com/xql-command-reference-guide/readme/functions/median_with_windowcomp_stage
fetched_at: 2026-09-16T09:05:33Z
source: cortex-platform
---

# median (windowcomp) | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 XQL 

 XQL Command Reference Guide 

 Cortex XQL Command Reference 

 Functions 

 median (windowcomp) 

 Use the median() function within the windowcomp stage to compute the median value of a specified numeric field over a window of rows. Unlike the comp stage version, the windowcomp version preserves all original rows and adds the computed median as a new field. This is equivalent to PERCENTILE_CONT(0.5) OVER(...) in SQL. 

 Syntax 

 Ask Copy 

 | windowcomp median( < field > ) [by <partition_field1>, <partition_field2>, ...] [sort [asc|desc] < sort_field1 > , ...] [between <lower> [and <upper>] [frame_type=rows|range]] [as <alias>] 

 Parameters 

 Name 

 Type 

 Required 

 Description 

 field 

 numeric 

 Yes 

 The numeric field from which to compute the median value. 

 partition_field 

 any 

 No 

 One or more fields to partition the data by (equivalent to SQL PARTITION BY ). 

 sort_field 

 any 

 No 

 One or more fields to define the order within each partition (equivalent to SQL ORDER BY ). Defaults to ascending. 

 lower 

 integer or null 

 No 

 Lower bound of the window frame. 0 = current row, negative = rows before, null = unbounded. 

 upper 

 integer or null 

 No 

 Upper bound of the window frame. 0 = current row, positive = rows after, null = unbounded. 

 frame_type 

 rows or range 

 No 

 Type of window frame. rows (default) uses physical row offsets; range uses value-based offsets on the sort field. 

 alias 

 string 

 No 

 An alias for the output field. 

 Returns 

 Type : numeric (float) 

 Description : The median() function returns the median value within the defined window for each row. All original rows are preserved. 

 Usage notes 

 Row preservation : Unlike comp median() , the windowcomp median() does not reduce the number of rows. 

 Percentile : The median is the 50th percentile of the values within the window. 

 Null handling : NULL values are ignored in the computation. 

 Default frame : If no window frame is specified, the default frame is from the start of the partition to the current row ( between null and 0 ). 

 Trend analysis : Useful for computing running medians or sliding window medians for trend analysis. 

 Examples 

 Example 1: Median bytes per host (all rows preserved) 

 Goal : Compute the median bytes received for each host while preserving all original rows. 

 XQL code : 

 Explanation : The median() function computes the median of action_network_bytes_received within each agent_hostname partition. All original rows are preserved, and each row receives the partition's median value in median_bytes_per_host . 

 Output : 

 _TIME 

 AGENT_HOSTNAME 

 ACTION_NETWORK_BYTES_RECEIVED 

 MEDIAN_BYTES_PER_HOST 

 2024-01-15 08:00:00 

 workstation-1 

 100 

 200.0 

 2024-01-15 09:00:00 

 workstation-1 

 300 

 200.0 

 2024-01-15 10:00:00 

 workstation-1 

 200 

 200.0 

 2024-01-15 08:30:00 

 workstation-2 

 500 

 400.0 

 2024-01-15 09:30:00 

 workstation-2 

 300 

 400.0 

 Example 2: Running median of response times 

 Goal : Compute a running median of response times, ordered by time. 

 XQL code : 

 Explanation : By sorting on _time in ascending order, the median() function computes a running median of action_total_time from the start of the dataset up to the current row. 

 Output : 

 _TIME 

 ACTION_TOTAL_TIME 

 RUNNING_MEDIAN 

 2024-01-15 08:00:00 

 50 

 50.0 

 2024-01-15 09:00:00 

 30 

 40.0 

 2024-01-15 10:00:00 

 70 

 50.0 

 2024-01-15 11:00:00 

 40 

 45.0 

 Related articles 

 Stages : windowcomp , comp , sort 

 Functions : median (comp) , avg() , max() 

 Datasets : xdr_data 

 Previous median (comp) 

 Next min (comp) 

 Last updated 3 months ago 

 Was this helpful?
