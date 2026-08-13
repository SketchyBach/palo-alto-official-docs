---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/engines/install-an-engine/docker/docker-hardening-guide/configure-the-memory-limitation
fetched_at: 2026-08-13T15:09:18Z
source: cortex-platform
---

# Configure the memory limitation | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

Configure the memory limitation | Cortex Documentation Portal 

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

 Docker network hardening 

 Configure Docker images 

 Run Docker with non-root internal users 

 Configure the memory limit support without swap capabilities 

 Configure the memory limitation 

 Configure the CPU, PIDs, and open the file descriptors limit 

 Check Docker hardening configurations 

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

 Docker hardening guide 

 Configure the memory limitation 

 We recommend limiting available memory for each container to 1 GB. 

 If swap limit capabilities is enabled (see How to check if your system supports swap limit capabilities above), in Cortex XSIAM configure the memory limitation using the following advanced parameters. 

 Edit the engine configuration file either by editing the d1.conf file, or If you installed via Shell, you can edit the configuration in the UI as well as editing the file directly. For details, see Configure engines . 

 Add the following keys. 

 "limit.docker.memory": true, "docker.memory.limit": "1g" 

 If you do not want to apply Docker memory limitations, you should explicitly set the advanced parameter: limit.docker.memory to false . 

 Save the changes. 

 Restart the demisto service on the engine machine. 

 sudo systemctl start d1 

 (Ubuntu) sudo service d1 restart 

 Test the memory limit. 

 Go to Investigation & Response → Automation → Scripts → New Script. 

 In the Script Name file, type TestMemory . 

 Add the following script: 

 Ask Copy 

 from multiprocessing import Process 
 import os 

 def big_string(size): 
 sys.stdin = os.fdopen(0, "r") 
 s = 'a' * 1024 
 while len(s) < size: 
 s = s * 2 
 print('completed creating string of length: {}'.format(len(s))) 

 size = 1 * 1024 * 1024 * 1024 
 p = Process(target=big_string, args=(size, )) 
 p.start() 
 p.join() 
 if p.exitcode != 0: 
 return_error("Return code from sub process indicates failure: {}".format(p.exitcode)) 
 else: 
 print("Success allocating memory of size: {}".format(size)) 

 In the SCRIPT SETTINGS section, select the script to run on the Single engine and select the engine where you want to run the script. 

 Save the script. 

 To test the memory limit, type !TestMemory . The command returns an error when it fails to allocate 1 GB of memory. 

 Previous Configure the memory limit support without swap capabilities Next Configure the CPU, PIDs, and open the file descriptors limit 

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
