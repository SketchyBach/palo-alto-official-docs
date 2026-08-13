---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/engines/install-an-engine/docker/troubleshoot-docker-issues
fetched_at: 2026-08-13T15:09:03Z
source: cortex-platform
---

# Troubleshoot Docker Issues | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

Troubleshoot Docker Issues | Cortex Documentation Portal 

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

 What is an engine? 

 Engine requirements 

 Install an engine 

 Docker 

 Install Docker 

 Install Docker distribution for Red Hat 

 Docker image security 

 Docker FAQs 

 Troubleshoot Docker Issues 

 Configure Docker pull rate limit 

 Change the Docker Installation folder 

 Docker hardening guide 

 Podman 

 Manage engines 

 Upgrade an engine 

 Remove an engine 

 Configure engines 

 Use an engine in an integration 

 Run a script using an engine 

 Troubleshoot engines 

 Troubleshoot integrations running on engines 

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

 Engines 

 Install an engine 

 Docker 

 Troubleshoot Docker Issues 

 The following provides troubleshooting solutions for Docker networking and performance issues. 

 Troubleshoot Docker networking issues 

 In Cortex XSIAM, integrations and scripts run either on the tenant, or on an engine. 

 If you have Docker networking issues when using an engine, you need to modify the d1.conf file. 

 On the machine where the Engine is installed, open the d1.conf file. 

 Add the following to the d1.conf file: 

 Ask Copy 

 { 
 "LogLevel": "info", 
 "LogFile": "/var/log/demisto/d1.log", 
 "EngineURLs": [ 
 "wss://1234.demisto.live/d1ws" 
 ], 
 "BindAddress": ":443", 
 "EngineID": "XYZ", 
 "ServerPublic": "ABC" 
 "ArtifactsFolder": "", 
 "TempFolder": "", 
 "python.pass.extra.keys": "--network=host" 
 } 

 Save the file. 

 Restart the engine using systemctl restart d1 or service d1 restart . 

 Troubleshoot Docker performance issues 

 This information is intended to help resolve the following Docker performance issues. 

 Containers are getting stuck. 

 The Docker process consumes a lot of resources. 

 Time synchronization issues between the container and the operating system. 

 Cause 

 The installed Docker package and its dependencies are not up to date. 

 Workaround 

 Update the package manager cache. 

 Linux Distribution 

 Command 

 Debian 

 apt-get update 

 (Optional) Check for a newer version of the Docker package. 

 Linux Distribution 

 Command 

 Debian 

 apt-cache policy docker 

 Update the Docker package. 

 Linux Distribution 

 Command 

 Debian 

 apt-get update docker 

 Previous Docker FAQs Next Configure Docker pull rate limit 

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
