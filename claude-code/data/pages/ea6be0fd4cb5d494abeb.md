---
url: https://docs.paloaltonetworks.com/autonomous-dem/activation-and-onboarding/deploy-universal-agent/deploy-universal-agent-on-virtual-machines/deploy-universal-agent-on-hyperv
fetched_at: 2026-08-13T15:24:58Z
source: palo-alto-main
---

# Install Universal Agent on Hyper V Clear

Install Universal Agent on Hyper V 

 Home 

 EN

 Location 

 Documentation Home 

 Palo Alto Networks 

 Support 

 Live Community 

 Knowledge Base 

 >

 Strata Copilot

 Install Universal Agent on Hyper V 

 Updated on 

 Tue Jun 02 00:10:43 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Autonomous DEM Docs 

 Activation & Onboarding 

 Administration 

 Select a Document 

 AI-Powered ADEM 

 Autonomous DEM for China 

 User Guide 

 Release Notes 

 New Features 

 Updated on 

 Tue Jun 02 00:10:43 PDT 2026 

 Focus 

 Home 

 Autonomous DEM 

 Deploy Universal Agent to Monitor SD-WAN 

 Deploy Universal Agent on Virtual Machines 

 Install Universal Agent on Hyper V 

 Download PDF 

 Autonomous DEM 

 Install Universal Agent on Hyper V 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Autonomous DEM Docs 

 Activation & Onboarding 

 Administration 

 Select a Document 

 AI-Powered ADEM 

 Autonomous DEM for China 

 User Guide 

 Release Notes 

 New Features 

 Previous 

 Install Universal Agent on ESXI 

 Next 

 Types of Application Experience Monitoring 

 Next 

 AI- Powered Autonomous DEM for China 

 Install Universal Agent on Hyper V 

 Deploy Universal Agent on Hyper V. 

 Where Can I Use
 This? What Do I Need? 

 Prisma Access (Managed by Strata Cloud Manager) 

 ADEM or Strata Cloud Manager Pro 
 license 

 Prisma Access license 

 Access to the Palo Alto Networks® image
 store 

 Access to Palo Alto Networks® image
 repository 

 Recommended host hardware specifications- 2
 virtual CPUs, 1GB RAM, 2GB storage after
 installation 

 Generate and download deployment assets .

 Create and configure the Virtual Machine. 

 From Hyper-V Manager, create a new virtual machine. 

 Ensure the option to Power on automatically is deselected. 

 Enter a name for the VM and select the VM generation type as
 Generation 1 and click Next . 

 Assign a minimum of 4 GB memory. 

 Configure networking by assigning the appropriate switch. 

 Connect using the existing virtual hard disk and attach the downloaded
 VHDX file. 

 Edit the settings for the VM deployed. 

 Under IDE Controller 1, ensure DVD Drive is added. 

 Under Processor , assign a minimum of 2 virtual processors. 

 Verify the network adapter is configured for the correct network. If
 dual NIC was specified in template, add the Network Adaptor 2 from
 Add Hardware > Network Adapter > Add . 

 Select the appropriate switch for the second Network Adaptor 2. 

 Apply the changes. 

 Power on the VM and verify agent registration. 

 Power on the configured Virtual Machine. 

 Once the VM has booted, log in to the VM using the default
 username and password. 

 Navigate to your Strata Cloud Manager portal and verify the new
 agent appears with an Active status. 

 Previous 

 Install Universal Agent on ESXI 

 Next 

 Types of Application Experience Monitoring 

 Next 

 AI- Powered Autonomous DEM for China 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Activate a License or Product 

 Cloud Identity Engine 

 Strata Logging Service 

 Device Associations 

 Hub 

 Identity and Access Management 

 Tenant Management 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 AI-Powered ADEM 

 Prisma Access Monitoring and Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Activation & Onboarding 

 Autonomous DEM 

 Prisma SASE 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
