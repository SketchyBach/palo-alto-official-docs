---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/data-management/broker-vm/broker-vm-high-availability-cluster/manage-broker-vm-clusters/add-applet-to-cluster
fetched_at: 2026-08-13T14:15:07Z
source: cortex-platform
---

# Add applet to cluster | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

Add applet to cluster | Cortex Documentation Portal 

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

 Optimize data management in Cortex XSIAM 

 Configure Cortex Data Lake tier 

 Broker VM 

 What is the Broker VM? 

 Set up and configure Broker VM 

 Manage Broker VM 

 Manage Broker VM data collector applets 

 Broker VM High Availability Cluster 

 Configure High Availability Cluster 

 Manage Broker VM clusters 

 View cluster details 

 Edit cluster 

 Add applet to cluster 

 Add Broker VM to cluster 

 Remove cluster 

 Broker VM notifications 

 Monitor Broker VM activity 

 Troubleshoot Broker VM applet errors 

 Dataset management 

 Archived data 

 Parsing Rules 

 Data Model Rules 

 Manage Event Forwarding 

 Manage compute units 

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

 Data management 

 Broker VM 

 Broker VM High Availability Cluster 

 Manage Broker VM clusters 

 Add applet to cluster 

 You can add an applet to a high availability (HA) cluster from the Clusters tab of the Brokers VM page. 

 You can always add an applet to a cluster, even if the cluster status is Unavailable or Error. When an applet is added to a cluster without any Broker VM nodes, the cluster status is Unavailable and the cluster APPS status displays as Inactive. 

 Select Settings → Configurations → Data Broker → Broker VMs, and select the Clusters tab. 

 In the Clusters table, locate the cluster that you want to add an applet. 

 You can either right-click the cluster, and select Add App → , or in the APPS column, left-click Add → . The applet is only available for you to add to the cluster if it hasn't already been added. 

 Configure your applet. The various applets that you can configure are the same as when configuring a standalone Broker VM. For more information on a particular applet configuration, locate the applet in the Set up Broker VM section in the Cortex XSIAM Admin Guide. The applet is listed with a status indicator in the APPS column, where the colors depict the following statuses: 

 Green (Connected): Indicates the applet has no issues. 

 Orange (Warning): Indicates the applet has minor issues. 

 Red (Error): Indicates the applet has errors. 

 White (Inactive): Indicates the applet is inactive. 

 Note 

 For more information on troubleshooting errors and warnings for these applets, see Troubleshoot Broker VM applet errors . 

 Once the applet configuration is changed in a cluster, the changes are automatically applied to the cluster nodes depending on the applet and cluster node role. For example, if you add the Kafka Collector, which is an "active/passive" applet, the applet is automatically initiated and enters an active state on the Primary node and is on standby on the standby nodes. While if you add the Syslog Collector "active/active" applet, the changes automatically propagate so that the applet is active on all cluster nodes, including Primary and standby. 

 Previous Edit cluster Next Add Broker VM to cluster 

 Last updated 20 days ago 

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
