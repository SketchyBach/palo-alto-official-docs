---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-3.x/cortex-xdr-3.x-documentation/data-management/data-ingestion/external-data-ingestion/additional-log-ingestion-methods/ingest-logs-from-proofpoint-targeted-attack-protection
fetched_at: 2026-09-06T09:50:43Z
source: cortex-platform
---

# Ingest Logs from Proofpoint Targeted Attack Protection | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR 

 Cortex XDR 3.x Documentation 

 Cortex XDR 3.x Documentation 

 Data management 

 Data Ingestion 

 External data ingestion 

 Additional log ingestion methods 

 Cortex XDR 3.x 

 Ingest Logs from Proofpoint Targeted Attack Protection 

 Ingest logs from Proofpoint Targeted Attack Protection (TAP). 

 Notice 

 Ingestion of logs and data requires a Cortex XDR Pro per GB license. 

 Note 

 This data source is only available in your tenant if the tenant was activated before October 1, 2025 with an active Cortex XDR Pro per GB license. 

 To receive logs from Proofpoint Targeted Attack Protection (TAP), you must first configure TAP service credentials in the TAP dashboard, and then the Collection Integrations settings in Cortex XDR based on your Proofpoint TAP configuration. After you set up data collection, Cortex XDR begins receiving new logs and data from the source. 

 When Cortex XDR begins receiving logs, the app creates a new dataset ( proofpoint_tap_raw ) that you can use to initiate XQL Search queries. For example queries, refer to the in-app XQL Library. 

 Configure the Proofpoint TAP collection in Cortex XDR. 

 Generate TAP Service Credentials in Proofpoint TAP. 

 TAP service credentials can be generated in the TAP Dashboard, where you will receive a Proofpoint Service Principal for authentication and Proofpoint API Secret for authentication. Record these credentials as you will need to provide them when configuring the Proofpoint Targeted Attack Protection data collector in Cortex XDR. For more information on generating TAP service credentials, see Generate TAP Service Credentials . 

 Configure the Proofpoint TAP collection in Cortex XDR. 

 Select Settings → Configurations → Data Collection → Collection Integrations . 

 In the Proofpoint Targeted Attack Protection configuration, click Add Instance . 

 Set these parameters: 

 Name : Specify a descriptive name for your log collection configuration. 

 Proofpoint Endpoint : All Proofpoint endpoints are available on the tap-api-v2.proofpoint.com host. You can leave the default configuration or specify another host. 

 Service Principal : Specify the Proofpoint Service Principal for authentication. TAP service credentials can be generated in the TAP Dashboard. 

 API Secret : Specify the Proofpoint API Secret for authentication. TAP service credentials can be generated in the TAP Dashboard. 

 Click Test to validate access, and then click Enable . 

 Once events start to come in, a green check mark appears underneath the Proofpoint Targeted Attack Protection configuration with the amount of data received. 

 (Optional) Manage your Proofpoint Targeted Attack Protection data collector. 

 After you enable the Proofpoint Targeted Attack Protection data collector, you can make additional changes as needed. 

 You can perform any of the following: 

 Edit the Proofpoint Targeted Attack Protection data collector settings. 

 Disable the Proofpoint Targeted Attack Protection data collector. 

 Delete the Proofpoint Targeted Attack Protection data collector. 

 Previous Ingest logs from Forcepoint DLP 

 Next Ingest logs and data from Salesforce.com 

 Last updated 1 month ago 

 Was this helpful?
