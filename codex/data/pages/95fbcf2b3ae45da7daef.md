---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-3.x/cortex-xdr-3.x-documentation/data-management/xdr-collectors/xdr-collector-datasets
fetched_at: 2026-09-06T09:50:14Z
source: cortex-platform
---

# XDR Collector datasets | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR 

 Cortex XDR 3.x Documentation 

 Cortex XDR 3.x Documentation 

 Data management 

 XDR Collectors 

 Cortex XDR 3.x 

 XDR Collector datasets 

 After Cortex XDR begins receiving data from your XDR Collectors configuration, the app automatically creates an XQL dataset. 

 Notice 

 Ingestion of logs and data requires a Cortex XDR Pro per GB license. 

 After Cortex XDR begins receiving data from your XDR Collectors configuration that are dedicated for on-premises data collection on Windows and Linux machines. 

 For Filebeat, the app automatically creates an Cortex Query Language (XQL) dataset of event logs using the vendor name and the product name specified in the configuration file section of the Filebeat profile. The dataset name follows the format <vendor>_<product>_raw . If not specified, Cortex XDR automatically creates a new default dataset in the format <module>_<module>_raw or <input>_<input>_raw . For example, if you are using the NGINX module, the dataset is called nginx_nginx_raw . 

 For Winlogbeat, the app automatically creates an XQL dataset of event logs using the vendor name and the product name specified in the configuration file section of the Winlogbeat profile. The dataset name follows the format <vendor>_<product>_raw . If not specified, Cortex XDR automatically creates a new default dataset, microsoft_windows_raw , for event log collection. Winlogbeat data is also normalized to xdr_data (and thus the xdr_event_log preset). 

 After Cortex XDR creates the dataset, you can search for your XDR Collector data using XQL Search. 

 Previous Apply profiles to collection machine policies 

 Next Data Ingestion 

 Last updated 1 month ago 

 Was this helpful?
