---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/protect-your-endpoints/endpoint-security/install-and-manage-endpoints/manage-endpoint-protection/monitor-agent-operational-status
fetched_at: 2026-08-13T15:14:29Z
source: cortex-platform
---

# Monitor agent operational status | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

Monitor agent operational status | Cortex Documentation Portal 

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

 Endpoint protection 

 Install and manage endpoints 

 Set up endpoint protection 

 Define endpoint groups 

 Configure global agent settings 

 Apply profiles to endpoints 

 Create an agent installation package 

 Harden endpoint security 

 Manage endpoint protection 

 Move agents between managing servers 

 Manage endpoint tags 

 Manage endpoint prevention profiles 

 Create a new prevention policy rule for serverless function 

 View information about your endpoint prevention profiles 

 Upgrade Cortex XDR agents 

 Restart agent 

 Uninstall the Cortex XDR agent 

 Clear agent database 

 Delete Cortex XDR agents 

 Manage agent tokens 

 Retrieve support file password 

 Send push notifications to iOS 

 Monitor agent operational status 

 Monitor agent activity 

 Monitor agent upgrade status 

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

 Protect your endpoints 

 Endpoint security 

 Install and manage endpoints 

 Manage endpoint protection 

 Monitor agent operational status 

 In Cortex XSIAM, you have full visibility into the Cortex XDR agent operational status on the endpoint, which indicates whether the agent is protecting according to its predefined security policies and profiles. By observing the operational status on the endpoint, you can identify when the agent may suffer from a technical issue or misconfiguration that interferes with the agent’s protection capabilities or interaction with Cortex XDR and other applications. The Cortex XDR agent reports the operational status as follows: 

 Protected : Indicates that the Cortex XDR agent is running as configured and did not report any exceptions to Cortex XDR. 

 Partially protected : Indicates that the Cortex XDR agent reported one or more exceptions to Cortex XDR. 

 Unprotected : Indicates that the Cortex XDR agent is not enforcing protection on the endpoint. 

 Local Resource Impact : Indicates that the Cortex XDR agent machine resources currently available for use are not enough for the agent to operate smoothly. 

 You can monitor the Cortex XDR agent Operational Status in Inventory → Endpoints → All Endpoints. If the Operational Status field is missing, add it. 

 The operational status that the agent reports varies according to the exceptions reported by the XDR agent. 

 Status 

 Description 

 Protected 

 Windows, Mac, and Linux : Indicates that all protection modules are running as configured on the endpoint. 

 iOS : Indicates that all required configurations are correct, and all required permissions are granted: 

 Notifications permission 

 Background app refresh permission 

 The Cortex XDR widget is in use on the home screen. When the Network Shield is disabled, the Cortex XDR widget is required. The widget is mandatory on unsupervised devices. 

 Android : Indicates that communication with the tenant is active. 

 Partially protected 

 Windows 

 XDR data collection is not running, or not set 

 Behavioral threat protection is not running 

 Malware protection is not running 

 Exploit protection is not running 

 Mac 

 Operating system adaptive mode* 

 XDR Data Collection is not running, or not set 

 Behavioral threat protection is not running 

 Malware protection is not running 

 Exploit protection is not running 

 Linux 

 Kernel module not loaded** 

 Kernel module compatible but not loaded** 

 Kernel version not compatible** 

 XDR Data Collection is not running, or not set 

 Behavioral threat protection is not running 

 Anti-malware flow is asynchronous 

 Malware protection is not running 

 Exploit protection is not running 

 iOS 

 The device is not fully protected, because some, but not all, of the configuration and permission requirements are fulfilled 

 Any of the listed items could lead to a partially protected state. Refer to the Cortex XDR management console for specific reasons for the state. 

 Unprotected 

 Windows, Mac, and Linux: 

 Behavioral threat protection and Malware protection are not running 

 Exploit protection and malware protection are not running 

 The content is unavailable 

 iOS: 

 The device is not fully protected, due to one or more of the following reasons: 

 Configurations might be incorrect 

 The required permissions might not be enabled 

 Android: 

 The device is not fully protected, because communication between the device and the tenant has been inactive for three or more hours 

 Local Resource Impact 

 Windows, Mac, Linux 

 Machine CPU impact on the agent operation 

 Machine memory impact on the agent operation 

 In addition to the status, either one of the following sub-statuses appear: 

 Low local available memory 

 No local available memory 

 Status can have the following implications on the endpoint: 

 *( Status ): The exploit protection module is not running. 

 **( Status ): 

 XDR data collection is not running 

 Behavioral threat protection is not running 

 Anti-malware flow is asynchronous 

 Local privilege escalation protection is asynchronous 

 Previous Send push notifications to iOS Next Monitor agent activity 

 Last updated 16 days ago 

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
