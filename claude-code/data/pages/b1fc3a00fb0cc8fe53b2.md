---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-5.x/configure-cortex-xdr/cortex-xdr-data-sources/generic-on-premise-data-collectors/broker-vm-data-collector-applets/activate-network-mapper
fetched_at: 2026-09-06T09:41:23Z
source: cortex-platform
---

# Activate Network Mapper | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR 

 Cortex XDR 5.x Documentation 

 Configure Cortex XDR 

 Cortex XDR Data Sources and Connectors 

 Generic on-premise data collectors 

 Broker VM data collector applets 

 Activate Network Mapper 

 Configure on-premises data collection for Cortex XDR. 

 License 

 Requires a Cortex XDR license that has endpoints, Cortex Cloud Runtime Security, or the Data Collection add-on. 

 Prerequisite 

 After you have configured and registered your Broker VM, you can choose to activate the Network Mapper application. 

 The Network Mapper allows you to scan your network to detect and identify unmanaged hosts in your environment according to defined IP address ranges. The Network Mapper configurations are used to locate unmanaged assets that appear in the Assets table. For more information, see All assets . 

 Select Settings → Configurations → Data Broker → Broker VMs. 

 Do one of the following: 

 On the Brokers tab, find the Broker VM, and in the APPS column, left-click Add → Network Mapper. 

 On the Clusters tab, find the Broker VM, and in the APPS column, left-click Add → Network Mapper. 

 In the Activate Network Mapper window, define the following parameters: 

 Field 

 Description 

 Scan Method 

 Select the either ICMP echo or TCP SYN scan method to identify your network hosts. When selecting TCP SYN you can enter single ports and ranges together, for example 80-83, 443 . 

 Scan Requests per Second 

 Define the maximum number of scan requests you want to send on your network per second. By default, the number of scan requests are defined as 1000. 

 Each IP address range can receive multiple scan requests based on it's availability. 

 Scanning Scheduler 

 Define when you want to run the network mapper scan. You can select either daily, weekly, or monthly at a specific time. 

 Scanned Ranges 

 Select from the list of exiting IP address ranges to scan. Make sure to after each selection. 

 IP address ranges are displayed according to what you defined as your Network Parameters. 

 Activate the applet. 

 After a successful activation, the APPS field displays Network Mapper with a green dot indicating a successful connection. 

 In the APPS field, left-click the Network Mapper connection to view the following scan and applet metrics: 

 Scan Details 

 Field 

 Description 

 Connectivity Status 

 Whether the applet is connected to Cortex XDR. 

 Scan Status 

 State of the scan. 

 Scan Start Time 

 Timestamp of when the scan started. 

 Scan Duration 

 Period of time in minutes and seconds the scan is running. 

 Scan Progress 

 How much of the scan has been completed in percentage and IP address ratio. 

 Detected Hosts 

 Number of hosts identified from within the IP address ranges. 

 Scan Rate 

 Number of IP addresses scanned per second. 

 Applet Metrics 

 Resources: Displays the amount of CPU, Memory, and Disk space the applet is using. 

 Manage the Network Mapper. 

 After the network mapper has been activated, left-click the Network Mapper connection in the APPS column to display the Network Mapper settings, and select: 

 Configure to redefine the network mapper configurations. 

 Scan Now to initiate a scan. 

 Deactivate to disable the network mapper. 

 Previous Activate NetFlow Collector 

 Next Syslog Collector applet 

 Last updated 5 days ago 

 Was this helpful?
