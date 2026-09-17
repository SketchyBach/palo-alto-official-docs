---
url: https://cortex-docs.paloaltonetworks.com/xql-command-reference-guide/readme/functions/first_value
fetched_at: 2026-09-16T09:04:54Z
source: cortex-platform
---

# first_value | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 XQL 

 XQL Command Reference Guide 

 Cortex XQL Command Reference 

 Functions 

 first_value 

 Use the first_value() function to retrieve the first value of a specified field within an ordered partition of records, typically used for baseline comparisons across a sequence of events. 

 Syntax 

 first_value(<field>) 

 Parameters 

 Name 

 Type 

 Required 

 Description 

 field 

 any 

 Yes 

 The field from which to extract the first recorded value based on the window's defined ordering. 

 Returns 

 The first_value() function returns the value of the specified field from the first row of the evaluated window frame. The data type of the returned value matches the data type of the input field. 

 Usage Notes 

 The first_value() function is a window function and must be used strictly within the windowcomp stage. 

 The chronological or logical order of the records is determined by the order by clause within the over() partition statement. 

 Unlike the first() aggregate function used in the comp stage, first_value() appends the retrieved baseline value to every row in the partition without collapsing the dataset, enabling row-by-row comparative analysis. 

 If the evaluated field for the first row in the window is NULL, the function will return NULL for the records in that window frame. 

 Examples 

 Example 1: Establish an Initial Process Baseline per Host** 

 Goal : Identify the first recorded process name executed on each endpoint and append this baseline value alongside all subsequent process executions to spot deviations. 

 XQL Code : 

 Explanation : You use the windowcomp stage to partition the events by agent_hostname and order them chronologically using _time asc. The first_value() function evaluates this ordered window and captures the first action_process_image_name encountered in each partition. This value is assigned to the initial_process alias and appended to every row for that host, allowing you to easily compare the current process (action_process_image_name) against the first process (initial_process). 

 Output : 

 _TIME 

 AGENT_HOSTNAME 

 ACTION_PROCESS_IMAGE_NAME 

 INITIAL_PROCESS 

 2023-10-26 10:00:00 UTC 

 endpoint-win-01 

 C:\Windows\System32\smss.exe 

 C:\Windows\System32\smss.exe 

 2023-10-26 10:05:30 UTC 

 endpoint-win-01 

 C:\Windows\System32\cmd.exe 

 C:\Windows\System32\smss.exe 

 2023-10-26 10:20:00 UTC 

 endpoint-win-01 

 C:\Windows\System32\powershell.exe 

 C:\Windows\System32\smss.exe 

 Example 2: Return the first value of a field 

 Goal : Extract the original remote port in a network connection. 

 XQL Code : 

 Explanation : The windowcomp partition operates within the parameters defined in the over() partition statement. The query organizes the data to evaluate by agent_hostname according to the ascending chronological order of its creation time. The results returned in the new field first_remote_port provide the remote port value of the earliest creation time event for each agent hostname. Because this calculation utilizes the windowcomp stage, all lines of the dataset are returned along with this new field value. 

 Output : 

 AGENT_HOSTNAME 

 ACTION_REMOTE_PORT 

 FIRST_REMOTE_PORT 

 _TIME 

 mac-agent-1 

 443 

 443 

 Mar 26th 2026 09:26:07 

 mac-agent-1 

 443 

 443 

 Mar 26th 2026 09:26:08 

 mac-agent-1 

 80 

 443 

 Mar 26th 2026 09:26:09 

 Related Articles 

 Stages : windowcomp , filter , fields , limit 

 Functions : last_value() , first() , lag() 

 Datasets : xdr_data 

 Previous first 

 Next floor 

 Last updated 3 months ago 

 Was this helpful?
