---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/cortex-xsiam-data-sources/generic-on-premise-data-collectors/broker-vm-data-collector-applets/syslog-collector-applet/ingest-logs-from-a-syslog-receiver
fetched_at: 2026-09-16T08:26:27Z
source: cortex-platform
---

# Ingest logs from a Syslog receiver | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSIAM 

 Cortex XSIAM Documentation 

 Configure Cortex XSIAM 

 Cortex XSIAM Data Sources and Connectors 

 Generic on-premise data collectors 

 Broker VM data collector applets 

 Syslog Collector applet 

 Cortex XSIAM 

 Ingest logs from a Syslog receiver 

 To extend visibility, Cortex XSIAM can receive Syslog from additional vendors that use CEF or LEEF formatted over Syslog (TLS not supported). 

 Cortex XSIAM can receive Syslog from a variety of supported vendors (see Syslog Collector applet ). In addition, Cortex XSIAM can receive Syslog from additional vendors that use CEF, LEEF, CISCO, CORELIGHT, or RAW formatted over Syslog.External data ingestion vendor support 

 After Cortex XSIAM begins receiving logs from the third-party source, Cortex XSIAM automatically parses the logs in CEF, LEEF, CISCO, CORELIGHT, or RAW format and creates a dataset with the name <vendor>_<product>_raw . You can then use XQL Search queries to view logs and create new IOC, BIOC, and Correlation Rules. 

 To receive Syslog from an external source: 

 Set up your Syslog receiver to forward logs. 

 Activate the Syslog collector applet on a Broker VM within your network. For more information, see Activate the Syslog Collector . 

 Use the XQL Search to search your logs. 

 Previous Activate Syslog Collector 

 Next Check Point FW1 VPN1 

 Last updated 1 month ago 

 Was this helpful?
