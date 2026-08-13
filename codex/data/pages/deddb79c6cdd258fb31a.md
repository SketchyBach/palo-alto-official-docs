---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/data-management/broker-vm/set-up-and-configure-broker-vm/broker-vm-image-installations/set-up-broker-vm-on-vmware-esxi-using-vsphere-client
fetched_at: 2026-08-13T14:14:44Z
source: cortex-platform
---

# Set up Broker VM on VMware ESXi using vSphere Client | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

Set up Broker VM on VMware ESXi using vSphere Client | Cortex Documentation Portal 

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

 Broker VM image installations 

 Set up Broker VM on Alibaba Cloud 

 Set up Broker VM on Amazon Web Services 

 Set up Broker VM on Google Cloud Platform (GCP) 

 Set up Broker VM on KVM using Ubuntu 

 Set up Broker VM on Microsoft Azure 

 Set up Broker VM on Microsoft Hyper-V 

 Set up Broker VM on Nutanix Hypervisor 

 Set up Broker VM on VMware ESXi using vSphere Client 

 Broker VM data collector applets 

 Manage Broker VM 

 Manage Broker VM data collector applets 

 Broker VM High Availability Cluster 

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

 Set up and configure Broker VM 

 Broker VM image installations 

 Set up Broker VM on VMware ESXi using vSphere Client 

 Learn more about how to set up you Cortex XSIAM Broker VM on VMware ESXi. 

 To set up the Broker VM on VMware ESXi, you deploy the OVA image provided in Cortex XSIAM. VMware ESXi 6.5 or later is supported. The instructions below provide an example of doing this using vSphere Client 7.0.3.01400. 

 Prerequisite 

 Ensure you have a virtualization platform installed that is compatible with an OVA image, and have an authenticated user account. 

 Download a Cortex XSIAM Broker VM OVA image. For more information, see the virtual machine compatibility requirements in Set up and configure Broker VM . 

 1 

 Deploy the Broker VM OVA image on vSphere Client 

 From vSphere Client, right-click an inventory object for the virtual machine of your broker, and select Deploy OVF Template. 

 In the Select an OVF template page of the wizard, select Local file, click UPLOAD FILES to select the OVA image file that you downloaded, and click NEXT. 

 In the Select a name and folder page, enter a unique name for the virtual machine, select a deployment location, and click NEXT. 

 In the Select a compute resource page, select a resource where to run the deployed VM template, and click NEXT. 

 In the Review details page, verify the OVA template details, and click NEXT. 

 In the Select storage page, define where and how to store the files for the deployed OVA template, and click NEXT. For more information on the options available, see the VMware vSphere documentation . 

 In the Select networks page, select a source network and map it to a destination network, and click NEXT. The Source Network column lists all networks that are defined in the OVA template. 

 In the Ready to complete page, review the details and click FINISH. A new task for creating the virtual machine is displayed in the Recent Tasks pane. When the Status of the task reaches 100%, the task is complete, and the new virtual machine is created on the selected resource. 

 Navigate to the resource where the new virual machine is created, right-click the resource, and select Power → Power On. 

 Previous Set up Broker VM on Nutanix Hypervisor Next Broker VM data collector applets 

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
