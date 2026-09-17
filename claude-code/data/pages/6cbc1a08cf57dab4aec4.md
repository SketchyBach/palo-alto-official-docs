---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-3.x/cortex-xdr-3.x-documentation/data-management/data-ingestion/verifying-collector-connectivity
fetched_at: 2026-09-16T08:44:18Z
source: cortex-platform
---

# Verifying collector connectivity | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR 

 Cortex XDR 3.x Documentation 

 Cortex XDR 3.x Documentation 

 Data management 

 Data Ingestion 

 Cortex XDR 3.x 

 Verifying collector connectivity 

 Verify collector connectivity and troubleshoot collector errors. 

 Notice 

 Ingestion of logs and data requires a Cortex XDR Pro per GB license. 

 You can verify the connectivity status of a collector instance on the Collection Integrations page. Instances are grouped by integration, and a status icon shows a summary of instance statuses for each integration. Expand the integration section to see the status of each individual instance, and hover over the status icons to see details about warning or error statuses. 

 Troubleshooting collector errors 

 Note 

 For more information on troubleshooting data collector applet errors, see Troubleshoot Broker VM applet errors . 

 Where can I see if I have a connectivity error on a collector instance? 

 On the Collection Integrations page, instances in error status display an error icon. Hover over the error icon next to the instance name to see the error message as received from the API. 

 Where can I trace the connectivity changes of a collector instance? 

 Each status change of an instance is logged in the collection_auditing dataset. Querying this dataset can help you see all the connectivity changes of an instance over time, the escalation or recovery of the connectivity status, and the error, warning, and informational messages related to status changes. 

 Example: 

 This example searches for status changes on Strata IOT integrations: 

 Ask Copy 

 dataset = collection_auditing  
 |filter collector_type = "STRATA_IOT" 

 How can I set up correlation rules to trigger collection alerts? 

 You can create correlation rules that are based on the fields in the collection_auditing dataset. 

 Example: Trigger collection alerts for error statuses on the STRATA_IOT collector 

 In this example, a correlation rule triggers an alert if an integration of the Strata IOT collector changes to error status. 

 Example XQL: 

 Ask Copy 

 dataset = collection_auditing  
 |filter classification = "Error" and collector_type = "STRATA_IOT" 

 Additional fields to specify in the correlation rule: 

 Field 

 Value 

 Time Schedule 

 Hourly 

 Query time frame 

 1 Hour 

 Alert Suppression 

 Select Enable alert suppression . 

 Action 

 Select Generate alert . 

 Severity 

 Medium 

 Category 

 Collection 

 Previous Measuring data freshness 

 Next Dataset management 

 Last updated 20 days ago 

 Was this helpful?
