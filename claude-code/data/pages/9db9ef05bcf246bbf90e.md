---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-5.x/configure-cortex-xdr/cortex-xdr-data-sources/administration-and-troubleshooting/verify-collector-connectivity
fetched_at: 2026-09-06T09:42:07Z
source: cortex-platform
---

# Verify collector connectivity | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR 

 Cortex XDR 5.x Documentation 

 Configure Cortex XDR 

 Cortex XDR Data Sources and Connectors 

 Administration and troubleshooting 

 Verify collector connectivity 

 Manage and troubleshoot Cortex XDR data integrations. 

 You can verify the connectivity status of a collector instance on the Data Sources & Integrations page. Instances are grouped by integration, and the Instances Status column shows icons that summarize the instance statuses for the integration. Click the integration to see details for each individual instance. 

 Troubleshooting collector errors 

 Note 

 For more information on troubleshooting data collector applet errors, see Troubleshoot Broker VM applet connectivity. 

 Where can I see if I have a connectivity error on a collector instance? 

 On the Data Sources & Integrations page, instances in error status display an error icon. Hover over the error icon next to the instance name to see the error message as received from the API. 

 Where can I trace the connectivity changes of a collector instance? 

 Each status change of an instance is logged in the collection_auditing dataset. Querying this dataset can help you see all the connectivity changes of an instance over time, the escalation or recovery of the connectivity status, and the error, warning, and informational messages related to status changes. 

 Example 92. 

 This example searches for status changes on Strata IOT integrations: 

 Ask Copy 

 dataset = collection_auditing  
 |filter collector_type = "STRATA_IOT" 

 How can I set up correlation rules to trigger collection issues? 

 You can create correlation rules that are based on the fields in the collection_auditing dataset. 

 In this example, a correlation rule triggers an issue if an integration of the Strata IOT collector changes to error status. 

 Example XQL: 

 Ask Copy 

 dataset = collection_auditing  
 |filter classification = "Error" and collector_type = "STRATA_IOT" 

 Additional fields to specify in the correlation rule: 

 Additional fields to specify in the correlation rule: 

 Field 

 Value 

 Time Schedule 

 Hourly 

 Query time frame 

 1 Hour 

 Issue Suppression 

 Select Enable issue suppression. 

 Action 

 Select Generate issue. 

 Severity 

 Medium 

 Category 

 Collection 

 Previous Manage credentials 

 Next Overview of data ingestion metrics 

 Last updated 5 days ago 

 Was this helpful?
