---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/cortex-xsiam-data-sources/generic-on-premise-data-collectors/broker-vm-data-collector-applets/activate-netflow-collector
fetched_at: 2026-08-13T15:01:02Z
source: cortex-platform
---

# Activate NetFlow Collector | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

Activate NetFlow Collector | Cortex Documentation Portal 

 ⌘ Ctrl k 

 Blog Support 
 More 

 Home 

 Products 

 Guides 

 Release Notes 

 API 

 Reference 

 AI Assistant 

 Good afternoon 
 I'm here to help you with the docs. 

 What is this page about? What should I read next? Can you give an example? 

 ⌘ Ctrl i 

 AI Based on your context 
 Send 

 Learn about Cortex XSIAM 

 Navigate the Cortex XSIAM docs 

 Get started with Cortex XSIAM 

 Agentic AI in Cortex XSIAM 

 Cortex XSIAM product licenses 

 In-product support ticket creation 

 Supported web browsers 

 Use the interface 

 Manage API keys 

 Onboard Cortex XSIAM 

 How to onboard Cortex XSIAM 

 Plan and prepare 

 Deployment steps 

 Post-deployment 

 Configure Cortex XSIAM 

 Learn how to configure Cortex XSIAM 

 Data management 

 Cortex XSIAM Data Sources and Connectors 

 What are Cortex XSIAM data sources and connectors? 

 Complete data source and connector catalog 

 Vendor-specific data sources and connectors 

 Connectors 

 Standard data sources 

 Cloud service provider (CSP) onboarding 

 Generic on-premise data collectors 

 Broker VM data collector applets 

 Activate Apache Kafka Collector 

 Activate Cortex Network Scanner 

 Activate CSV Collector 

 Activate Database Collector 

 Activate DSPM Fileshare 

 Activate Files and Folders Collector 

 Activate FTP Collector 

 Activate Local Agent Settings 

 Activate NetFlow Collector 

 Activate Network Mapper 

 Activate Registry Scanner 

 Syslog Collector applet 

 Activate Transporter 

 Activate Windows Event Collector 

 XDR Collectors 

 Palo Alto Networks integrations 

 Cloud Posture and Runtime Security data sources 

 External alerts using External Issue Mapping 

 Administration and troubleshooting 

 Marketplace 

 Configure the Cortex Agentic Assistant 

 Cortex MCP server 

 Automations 

 Engines 

 Remote repository management 

 Customize cases and issues 

 XQL query management 

 Multi-Tenant 

 Managed Services configuration in Cortex 

 Protect your endpoints 

 Endpoint security 

 Endpoint DLP 

 Detect, Investigate, and respond to threats 

 Monitor dashboards and reports 

 Investigation and response 

 Agentic Assistant chat 

 Asset management 

 Threat management 

 Attack surface management 

 Vulnerability management 

 Exposure management 

 Cortex Advanced Email Security 

 Identity Threat Detection and Response (ITDR) 

 Cloud Security 

 Monitor and track compliance adherence 

 Cloud security rules and policies 

 Cortex Cloud Data Classification 

 Cortex Data Security 

 Cloud Identity Security 

 Network exposure detection 

 Cortex Cloud SaaS Security 

 Cortex Cloud AI Security 

 Serverless function posture security 

 Cortex Cloud Application Security 

 Cloud workload policies and rules 

 Base image rules 

 Web and API Security (WAAS) 

 Serverless function runtime security 

 Reference and developer docs 

 Cortex XSIAM XQL 

 Graph Search 

 Cortex CLI 

 Role-Based Access Control 

 API documentation 

 Reference 

 Migrating to a new Broker VM image 

 Learn more about migrating to the latest broker VM image 

 Standalone Broker VM 

 Broker VM high availability cluster node 

 On this page 

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

 Activate NetFlow Collector 

 To receive NetFlow flow records from an external source, you must first set up the NetFlow Collector applet on a Broker VM within your network. NetFlow versions 5, 9, and IPFIX are supported. 

 To increase the log ingestion rate, you can add additional CPUs to the Broker VM. The NetFlow Collector listens for flow records on specific ports either from any, or from specific IP addresses. 

 After the NetFlow Collector is activated, the NetFlow Exporter sends flow records to the NetFlow Collector, which receives, stores, and pre-processes that data for later analysis. 

 Performance Requirements 

 The following setups are required to meet your performance needs: 

 4 CPUs for up to 50K flows per second (FPS). 

 8 CPUs for up to 100K FPS. 

 Note 

 Since multiple network devices can send data to a single NetFlow Collector, we recommend that you configure a maximum of 50 NetFlow Collectors per Broker VM applet, with a maximum aggregated rate of approximately 50K flows per second (FPS) to maintain system performance. 

 Prerequisite 

 Set up and configure Broker VM 

 How to activate the NetFlow Collector 

 Select Settings → Configurations → Data Broker → Broker VMs. 

 Do one of the following: 

 On the Brokers tab, find the Broker VM, and in the APPS column, left-click Add → NetFlow Collector. 

 On the Clusters tab, find the Broker VM, and in the APPS column, left-click Add → NetFlow Collector. 

 Click +Add New. 

 Configure your NetFlow Collector. 

 General Settings 

 Specify the number of the UDP Port on which the NetFlow Collector listens for flow records (default 2055). 

 This port number must match the UDP port number in the NetFlow exporter device. The rules for each port are evaluated, line by line, on a first match basis. Cortex XSIAM discards logs for non-configured flow records without an “Any” rule. 

 Since Cortex XSIAM reserves some port numbers, it is best to select a port number that is not in the range of 0-1024 (except for 514), in the range of 63000-65000 or has one of the following values: 4369, 5671, 5672, 5986, 6379, 8000, 8888, 9100, 15672, or 28672. 

 Custom Settings 

 Field 

 Description 

 Source Network 

 Specify the IP address or a Classless Inter-Domain Routing (CIDR) of the source network device that sends the flow records to Cortex XSIAM . Leave the field empty to receive data from any device on the specified port (default). If you do not specify an IP address or a CIDR, Cortex XSIAM can receive data from any source IP address or CIDR that transmits via the specified port. If IP addresses overlap in multiple rows in the Source Network field, such as 10.0.0.10 in the first row and 10.0.0.0/24 in the second row, the NetFlow Collector captures the IP address in the first row. 

 Vendor and Product 

 Specify a particular vendor and product to be associated with each dataset entry or leave the default IP Flow setting. 

 The Vendor and Product values are used to define the name of your Cortex Query Language (XQL) dataset <Vendor>_<Product>_raw . If you do not define a vendor or product, Cortex XSIAM uses the default values with the resulting dataset name ip_flow_ip_flow_raw . Consider changing the default values in order to uniquely identify the source network device. 

 After each configuration, select to save your changes and then select Done to update the NetFlow Collector with your settings. 

 (Optional) Make additional changes to the NetFlow Collector data sources. 

 You can make additional changes to the Port by right-clicking the applicable UDP port and selecting the following: 

 Edit: To change the UDP Port, Source Network, Vendor, or Product defined. 

 Remove: To delete a Port. 

 You can make additional changes to the Source Network by right-clicking on the Source Network value. 

 The options available change, according to the set Source Network value. 

 Option 

 Description 

 Edit 

 To change the UDP Port, Source Network, Vendor, or Product defined. 

 Remove 

 To delete a Port. 

 Copy entire row 

 To copy the Source Network, Product, and Vendor information. 

 Open IP View 

 To view network operations and to view any open cases on this IP within a defined period. This option is only available when the Source Network value is a specific IP address or CIDR. 

 Open in Quick Launcher 

 To search for information using the Quick Launcher shortcut . This option is only available when the Source Network value is a specific IP address or CIDR. 

 To prioritize the order of the NetFlow formats listed for the configured data source, drag and drop the rows to change their order. 

 Activate the NetFlow collector applet. 

 After successful activation, the APPS field displays NetFlow with a green dot indicating a successful connection. 

 (Optional) To view NetFlow Collector metrics, left-click the NetFlow connection in the APPS field for your Broker VM. 

 Cortex XSIAM displays the following information: 

 Option 

 Description 

 Connectivity Status 

 Whether the applet is connected to Cortex XSIAM. 

 Logs Received and Logs Sent 

 Number of logs that the applet received and sent per second over the last 24 hours. If there are more logs received than sent, this can indicate a connectivity issue. 

 Resources 

 Displays the amount of CPU, Memory, and Disk space the applet uses. 

 Manage the NetFlow Collector. 

 After you activate the NetFlow Collector, you can make additional changes. To modify a configuration, left-click the NetFlow connection in the APPS column to display the NetFlow Collector settings, and select: 

 Configure to redefine the NetFlow Collector configurations. 

 Deactivate to disable the NetFlow Collector. 

 You can also Ingest NetFlow flow records as datasets . 

 Previous Activate Local Agent Settings Next Activate Network Mapper 

 Last updated 17 days ago 

 Was this helpful? 

 ‍ 

 Trust Center 

 ‍ 

 Privacy 

 ‍ 

 Terms of Use 

 ‍ 

 Legal 

 © 2026 Palo Alto Networks, Inc. All rights reserved. 

 Performance Requirements 

 Prerequisite 

 How to activate the NetFlow Collector 

 Was this helpful?
