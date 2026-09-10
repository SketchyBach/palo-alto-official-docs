---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-3.x/cortex-xdr-3.x-documentation/data-management/data-ingestion/palo-alto-networks-integrations/ingest-alerts-from-prisma-cloud
fetched_at: 2026-09-06T09:50:19Z
source: cortex-platform
---

# Ingest Alerts from Prisma Cloud | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR 

 Cortex XDR 3.x Documentation 

 Cortex XDR 3.x Documentation 

 Data management 

 Data Ingestion 

 Palo Alto Networks integrations 

 Cortex XDR 3.x 

 Ingest Alerts from Prisma Cloud 

 Configure Data Collection Settings in Cortex XDR to receive alerts from Prisma Cloud. 

 Notice 

 Ingestion of logs and data requires a Cortex XDR Pro per GB license. 

 To receive alerts from Prisma Cloud, first configure the Collection Integrations settings in Cortex XDR. After you set up collection integration, Cortex XDR begins to receive alerts from Prisma Cloud every 30 seconds. 

 Cortex XDR then groups these alerts into incidents and adds them to the Alerts table. When Cortex XDR begins receiving the alerts, it creates a new Cortex Query Language (XQL) dataset ( prisma_cloud_raw ), which you can use to initiate XQL Search queries and create Correlation Rules. The in-app XQL Library contains sample search queries. 

 You can also configure Cortex XDR to collect data directly from other cloud providers using an applicable collector. For more information on the cloud collectors, see External Data Ingestion Vendor Support. The Prisma Cloud alerts are stitched to this data. 

 Complete the following tasks before you begin configuring Cortex XDR to receive alerts from Prisma Cloud. 

 Create an Access Key and Secret Key as explained in the Create and Manage Access Keys section of the [Prisma Cloud Administrator’s Guide]. Prisma Cloud System Admin privileges are required for this task. 

 Copy or download the Access Key ID and Secret Key as you will need them when configuring the Prisma Cloud Collector in Cortex XDR. 

 Configure Cortex XDR to receive alerts from Prisma Cloud. 

 Select Settings → Configurations → Data Collection → Collection Integrations . 

 In the Prisma Cloud Collector configuration, click Add Instance . 

 Set the following parameters. 

 Specify a Name to identify the connection. 

 Specify the Domain URL for Prisma Cloud. 

 Note 

 You can find your default Prisma Cloud domain in the Prisma Cloud API URL table . 

 Specify the Prisma Cloud Access Key Id that you received when you created an Access Key. 

 Specify the Prisma Cloud Secret Key that you received when you created an Access Key. 

 To create Cortex XDR alerts from the ingested Prisma Cloud alerts, click Advanced Settings , and select the desired options: 

 Incidents : Create Cortex XDR alerts for runtime alerts detected by Prisma Cloud. 

 Risks : Create Cortex XDR alerts for Prisma Cloud findings and vulnerabilities that could be exploited by threat actors. 

 Click Test to validate the connection, and then click Enable . 

 In Cortex XDR, once alerts start to come in, a green check mark appears underneath the Prisma Cloud Collector configuration with the amount of data received. 

 (Optional) Manage your Prisma Cloud Collector. 

 After you enable the Prisma Cloud Collector, you can make additional changes, as needed. 

 To modify a configuration, select any of the following options. 

 Edit the Prisma Cloud Collector settings. 

 Disable the Prisma Cloud Collector. 

 Delete the Prisma Cloud Collector. 

 After Cortex XDR begins receiving data from Prisma Cloud, you can use XQL Search to search for specific data, using the prisma_cloud_raw dataset and to view alerts in the Alerts table. In the Cortex XDR Alerts table, the Prisma Cloud alerts are listed as Prisma Cloud in the ALERT SOURCE column. 

 Previous Ingest Alerts from Prisma Cloud Compute 

 Next Ingest detection data from Strata Logging Service 

 Last updated 1 month ago 

 Was this helpful?
