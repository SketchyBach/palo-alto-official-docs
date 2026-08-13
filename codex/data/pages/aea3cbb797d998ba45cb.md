---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/engines/install-an-engine/podman/change-the-container-storage
fetched_at: 2026-08-13T15:09:33Z
source: cortex-platform
---

# Change the Container storage | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

Change the Container storage | Cortex Documentation Portal 

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

 Podman 

 Change the Container storage 

 Install Podman 

 Migrate from Docker to Podman 

 Troubleshoot Podman 

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

 Podman 

 Change the Container storage 

 Configure Podman container storage for an engine. 

 By default, Podman uses the $HOME/.local/share/containers/storage directory. To use a different directory for container storage, edit the Podman config file located at /home/demisto/.config/containers/storage.conf . If the Podman config file does not exist, you need to create it and change the ownership. 

 The new storage directory needs to be owned by the demisto user, otherwise, they will be denied access to it. 

 Do not use NAS storage or a temporary (tmpfs) directory for the graphroot setting. The graphroot needs to be a local, non-temporary directory for Podman to work. For more information, see https://en.wikipedia.org/wiki/Network-attached_storage . 

 We recommend reserving 150 GB for container storage, either in the /home partition or a different storage directory that you have set using the graphroot key. 

 If the Podman config file does not exist: 

 Create the Podman config file. 

 sudo mkdir -p /home/demisto/.config/containers 

 cp /etc/containers/storage.conf /home/demisto/.config/containers 

 Change the ownership of the Podman config file. 

 sudo chown -R demisto:demisto /home/demisto 

 To set a different directory for container storage, change the key: graphroot in the storage.conf file. For example: 

 graphroot = "/var/lib/containers/cortex-storage" 

 Some additional changes are required in the storage.conf file. Comment out the runroot setting by adding a # (hash) before it. For example: 

 #runroot = "/run/containers/storage" 

 Alternatively, the runroot setting may be set to some temporary directory that is accessible by the user demisto. If you choose to set the runroot , it must be a directory that is mounted as tmpfs (temporary filesystem), unlike the graphroot. 

 Under [storage.options.overlay], uncomment the following line (remove the # from the start): 

 mount_program = "/usr/bin/fuse-overlayfs" 

 If the engine has already been installed, apply your changes to any existing containers: 

 sudo -u demisto podman system migrate 

 Verify the change (once the engine is installed): 

 sudo -u demisto podman info | grep graph 

 Previous Podman Next Install Podman 

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
