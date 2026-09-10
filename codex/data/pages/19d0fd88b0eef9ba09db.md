---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/data-management/dataset-management/monitor-datasets-and-dataset-views-activity
fetched_at: 2026-09-06T09:20:42Z
source: cortex-platform
---

# Monitor datasets and dataset views activity | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSIAM 

 Cortex XSIAM Documentation 

 Configure Cortex XSIAM 

 Data management 

 Dataset management 

 Cortex XSIAM 

 Monitor datasets and dataset views activity 

 Monitor dataset and dataset view activity in Cortex XSIAM. 

 Prerequisite 

 Dataset Management requires View/Edit RBAC permissions for Data Management (under Configurations → Data Management ), which are the same permissions required for Parsing Rules, Data Model Rules, and Event Forwarding. 

 Cortex XSIAM logs entries for events related to datasets and dataset views monitored activities. Cortex XSIAM stores the logs for 365 days. To view the datasets and dataset views audit logs, select Settings → Management Audit Logs . 

 You can customize your view of the logs by adding or removing filters to the Management Audit Logs table. You can also filter the page result to narrow down your search. The following table describes the default and optional fields that you can view in the Cortex XSIAM Management Audit Logs table: 

 Note 

 Certain fields are exposed and hidden by default. An asterisk (*) is beside every field that is exposed by default. 

 Field 

 Description 

 Description* 

 Log message that describes the action. 

 Email 

 Email of the user who performed the action. 

 Host Name* 

 This field is not applicable for datasets and dataset views logs. 

 ID 

 Unique ID of the action. 

 Reason 

 This field is not applicable for datasets and dataset views logs. 

 Result* 

 The result of the action ( Success , Fail , or N/A ) 

 Severity* 

 Severity associated with the log: Critical , High , Medium , Low , or Informational . 

 Timestamp* 

 Date and time when the action occurred. 

 Type* and Sub-Type* 

 Additional classifications of dataset and dataset view logs. Datasets: Create Dataset, Delete Dataset, and Update Dataset. Dataset Views: Create Dataset View, Delete Dataset View, and Update Dataset View. 

 User Name* 

 Name of the user who performed the action. 

 Previous Set time to live for lookup datasets 

 Next Archived data 

 Last updated 10 days ago 

 Was this helpful?
