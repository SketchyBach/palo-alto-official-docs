---
url: https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/cortex-cloud-data-sources-and-connectors/generic-on-premise-data-collectors/xdr-collectors/xdr-collector-datasets
fetched_at: 2026-09-06T10:01:26Z
source: cortex-platform
---

# XDR Collector datasets | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Cortex CLOUD Runtime Security 

 Cortex Cloud Data Sources and Connectors 

 Generic on-premise data collectors 

 XDR Collectors 

 XDR Collector datasets 

 After Cortex Cloud begins receiving data from your XDR Collectors configuration, the app automatically creates an XQL dataset. 

 After Cortex Cloud begins receiving data from your XDR Collectors configuration that are dedicated for on-premises data collection on Windows and Linux machines. 

 For Filebeat, the app automatically creates an Cortex Query Language (XQL) dataset of event logs using the vendor name and the product name specified in the configuration file section of the Filebeat profile. The dataset name follows the format <vendor>_<product>_raw . If not specified, Cortex Cloud automatically creates a new default dataset in the format <module>_<module>_raw or <input>_<input>_raw . For example, if you are using the NGINX module, the dataset is called nginx_nginx_raw . 

 For Winlogbeat, the app automatically creates an XQL dataset of event logs using the vendor name and the product name specified in the configuration file section of the Winlogbeat profile. The dataset name follows the format <vendor>_<product>_raw . If not specified, Cortex Cloud automatically creates a new default dataset, microsoft_windows_raw , for event log collection. Winlogbeat data is also normalized to xdr_data (and thus the xdr_event_log preset). 

 After Cortex Cloud creates the dataset, you can search for your XDR Collector data using XQL Search. 

 Previous Apply profiles to collection machine policies 

 Next Palo Alto Networks integrations 

 Last updated 1 month ago 

 Was this helpful?
