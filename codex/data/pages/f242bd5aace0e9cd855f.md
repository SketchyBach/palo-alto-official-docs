---
url: https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/cortex-cloud-data-sources-and-connectors/generic-on-premise-data-collectors/broker-vm-data-collector-applets/syslog-collector-applet/corelight-zeek/ingest-logs-from-corelight-zeek
fetched_at: 2026-09-16T08:46:12Z
source: cortex-platform
---

# Ingest logs from Corelight Zeek | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Cortex CLOUD Runtime Security 

 Cortex Cloud Data Sources and Connectors 

 Generic on-premise data collectors 

 Broker VM data collector applets 

 Syslog Collector applet 

 Corelight Zeek 

 Ingest logs from Corelight Zeek 

 If you use Corelight Zeek sensors for network monitoring, you can still take advantage of Cortex Cloud investigation and detection capabilities by forwarding your network connection logs to Cortex Cloud. This enables Cortex Cloud to examine your network traffic to detect anomalous behavior. Cortex Cloud can use Corelight Zeek logs as the sole data source, but can also use logs in conjunction with Palo Alto Networks or third-party firewall logs. For additional endpoint context, you can also use Cortex Cloud to collect and alert on endpoint data. 

 As soon as Cortex Cloud starts to receive logs, the app can begin stitching network connection logs with other logs to form network stories. Cortex Cloud can also analyze your logs to generate Analytics issues, and can apply IOC, BIOC, and Correlation Rule matching. You can also use queries to search your network connection logs. 

 To integrate your logs, you first need to set up an applet in a Broker VM within your network to act as a Syslog Collector. You then configure forwarding on your Corelight Zeek sensors (using the default Syslog export option of RFC5424 over TCP) to send logs to the Syslog Collector. 

 Activate the Syslog Collector . During activation, you define the Listening Port over which you want the Syslog Collector to receive logs. You must also set TCP as the transport Protocol and Corelight as the Syslog Format. 

 Increase log storage for Corelight Zeek logs. For proper sizing calculations, test the log sizes and log rates produced by your Corelight Zeek Sensors. Then adjust your Cortex Cloud log storage. For more information, see Manage Your Log Storage within Cortex Cloud. 

 Forward logs to the Syslog Collector. Cortex Cloud can receive logs from Corelight Zeek sensors that use the Syslog export option of RFC5424 over TCP. 

 In the Syslog configuration of Corelight Zeek (Sensor → Export), specify the details for your Syslog Collector including the hostname or IP address of the Broker VM and corresponding listening port that you defined during activation of the Syslog Collector, default Syslog format (RFC5424), and any log exclusions or filters. 

 Save your Syslog configuration to apply the configuration to your Corelight Zeek Sensors.
For full setup instructions, see the Corelight Zeek documentation. 

 Previous Corelight Zeek 

 Next Forcepoint DLP 

 Last updated 1 month ago 

 Was this helpful?
