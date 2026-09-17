---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-3.x/cortex-xdr-3.x-documentation/data-management/data-ingestion/external-data-ingestion/additional-log-ingestion-methods/ingest-csv-files-as-datasets
fetched_at: 2026-09-16T08:44:17Z
source: cortex-platform
---

# Ingest CSV files as datasets | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

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

 Ingest CSV files as datasets 

 Cortex XDR can receive CSV log files from a shared Windows directory, where the CSV log files must conform to specific guidelines. 

 Notice 

 Ingestion of logs and data requires a Cortex XDR Pro per GB license. 

 Note 

 This data source is only available in your tenant if the tenant was activated before October 1, 2025 with an active Cortex XDR Pro per GB license. 

 Cortex XDR can receive CSV log files from a shared Windows directory directly to your log repository for query and visualization purposes. After you activate the CSV Collector applet on a Broker VM in your network, which includes defining the list of folders mounted to the Broker VM and setting the list of CSV files to monitor and upload to Cortex XDR (using a username and password), you can ingest CSV files as datasets. 

 The ingested CSV log files must conform to the following guidelines: 

 Header field names must contain only letters (a-z, A-Z) or numbers (0-9) and must start with a letter. Spaces are converted to underscores (_). 

 Date values can be in either of the following formats: 

 YYYY-MM-DD (optionally including HH:MM:SS) 

 Unix Epoch time. For example, 1614858795. 

 After Cortex XDR begins receiving logs from the shared Windows directory, Cortex XDR automatically parses the logs and creates a dataset with the specific name you set as the target dataset when you configured the CSV Collector. The CSV Collector checks for any changes in the configured CSV files, as well as any new CSV files added to the configuration folders, in the Windows directory every 10 minutes and replaces the data in the dataset with the data from those files. You can then use XQL Search queries to view logs and create new Correlation Rules. 

 Configure Cortex XDR to receive CSV files as datasets from a shared Windows directory. 

 Ensure that you share the applicable CSV files in your Windows directory. 

 Activate the CSV Collector applet on a Broker VM within your network. 

 Use the XQL Search to locate and review logs. 

 Previous Ingest Apache Kafka events as datasets 

 Next Ingest database data as datasets 

 Last updated 1 month ago 

 Was this helpful?
