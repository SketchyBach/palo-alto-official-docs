---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/cortex-xsiam-data-sources/generic-on-premise-data-collectors/broker-vm-data-collector-applets/syslog-collector-applet/ingest-logs-from-a-syslog-receiver
fetched_at: 2026-08-13T15:01:06Z
source: cortex-platform
---

# Ingest logs from a Syslog receiver | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

Ingest logs from a Syslog receiver | Cortex Documentation Portal 

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

 Activate Syslog Collector 

 Ingest logs from a Syslog receiver 

 Check Point FW1 VPN1 

 Cisco ASA firewalls and AnyConnect 

 Corelight Zeek 

 Forcepoint DLP 

 Fortinet Fortigate 

 Next Generation Firewall 

 PingFederate 

 Zscaler Internet Access 

 Zscaler Private Access 

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

 Syslog Collector applet 

 Ingest logs from a Syslog receiver 

 To extend visibility, Cortex XSIAM can receive Syslog from additional vendors that use CEF or LEEF formatted over Syslog (TLS not supported). 

 Cortex XSIAM can receive Syslog from a variety of supported vendors (see Syslog Collector applet ). In addition, Cortex XSIAM can receive Syslog from additional vendors that use CEF, LEEF, CISCO, CORELIGHT, or RAW formatted over Syslog.External data ingestion vendor support 

 After Cortex XSIAM begins receiving logs from the third-party source, Cortex XSIAM automatically parses the logs in CEF, LEEF, CISCO, CORELIGHT, or RAW format and creates a dataset with the name <vendor>_<product>_raw . You can then use XQL Search queries to view logs and create new IOC, BIOC, and Correlation Rules. 

 To receive Syslog from an external source: 

 Set up your Syslog receiver to forward logs. 

 Activate the Syslog collector applet on a Broker VM within your network. For more information, see Activate the Syslog Collector . 

 Use the XQL Search to search your logs. 

 Previous Activate Syslog Collector Next Check Point FW1 VPN1 

 Last updated 5 days ago 

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

 Was this helpful?
