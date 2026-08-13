---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/cortex-xsiam-data-sources/generic-on-premise-data-collectors/xdr-collectors/manage-xdr-collectors/xdr-collectors-installation-resource-for-windows-and-linux
fetched_at: 2026-08-13T15:02:02Z
source: cortex-platform
---

# XDR Collectors installation resource for Windows and Linux | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

XDR Collectors installation resource for Windows and Linux | Cortex Documentation Portal 

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

 XDR Collectors 

 XDR Collector audit logs 

 XDR Collector machine requirements and supported operating systems 

 Resources required to enable access to XDR collectors 

 Manage XDR Collectors 

 XDR Collectors installation resource for Windows and Linux 

 Create an XDR Collector installation package 

 Install the XDR Collector installation package for Windows 

 Install the XDR Collector installation package for Linux 

 Configure XDR Collector upgrade scheduler 

 Set an application proxy for XDR Collectors 

 Set an alias for an XDR Collector machine 

 Upgrade XDR Collectors 

 Uninstall the XDR Collector 

 Define XDR Collector machine groups 

 About Cortex XDR Collector content updates 

 XDR Collector profiles 

 Apply profiles to collection machine policies 

 XDR Collector datasets 

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

 XDR Collectors 

 Manage XDR Collectors 

 XDR Collectors installation resource for Windows and Linux 

 The following table provides important information about the XDR Collectors installation for Windows and Linux. 

 Installation component 

 Default path 

 Description 

 Related files/Services 

 Installation folder 

 Windows : %PROGRAMFILES%\Palo Alto Networks\XDR Collector 

 Linux : /opt/paloaltonetworks/xdr-collector 

 The default installation path for the XDR Collector. Contains all Program Core files and executables. 

 Windows 

 Service name: XDR Collector 

 Process name: xdrcollectorsvc.exe 

 Linux 

 Service name: xcd 

 Process name: xdr-collector.service 

 Logs 

 Windows : %PROGRAMDATA%\XDR Collector\logs 

 Linux : /opt/paloaltonetworks/xdr-collector/logs 

 Windows : Contains the XDR Collector application Log, the Filebeat application log, and the Winlogbeat application log. Indicates information, warnings, and errors related to the XDR Collector application. 

 Linux : Contains the XDR Collector application Log as well as the Filebeat application log. Indicates information, warnings, and errors related to the XDR Collector application. 

 Contains the XDR Collector application Log as well as the Filebeat application log. Indicates information, warnings, and errors related to the XDR Collector application. 

 Windows 

 scouter.log 

 filebeat 

 winlogbeat 

 Linux 

 scouter.log 

 filebeat 

 Configuration 

 Windows : %PROGRAMFILES%\Palo Alto Networks\XDR Collector\config 

 Linux : /opt/paloaltonetworks/xdr-collector/config 

 Contains the XML configuration file of the XDR Collector for both Windows and Linux. Any change in this XML configuration file is saved to the XDR Collector database and the settings are taken from this file. ### Note In some circumstances, such as after an XDR Collectors upgrade, the configured settings in the XML configuration file can be erased. Yet, this won't affect the saved settings in the XDR Collectors database. 

 For both Windows and Linux, the file name is XDR_Collector.xml . 

 Persistence 

 Windows : %PROGRAMDATA%\XDR Collector\OSPersistence 

 Linux : /etc/panw/OSPersistence/ 

 Contains the Operating System persistence file for the XDR Collector, which issued as part of the registration process. 

 For both Windows and Linux, the file name is .scouter.json . 

 Previous Manage XDR Collectors Next Create an XDR Collector installation package 

 Last updated 22 days ago 

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
