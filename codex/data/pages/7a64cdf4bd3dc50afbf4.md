---
url: https://docs.paloaltonetworks.com/autonomous-dem/activation-and-onboarding/deploy-universal-agent/deploy-universal-agent-on-virtual-machines/deploy-universal-agent-on-esxi-hypervisors
fetched_at: 2026-08-13T15:31:12Z
source: palo-alto-main
---

# Install Universal Agent on ESXI Clear

Install Universal Agent on ESXI 

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

 Install Universal Agent on ESXI 

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

 Install Universal Agent on ESXI 

 Download PDF 

 Autonomous DEM 

 Install Universal Agent on ESXI 

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

 Deploy Universal Agent on Virtual Machines 

 Next 

 Install Universal Agent on Hyper V 

 Install Universal Agent on ESXI 

 Deploy Universal Agent on ESXi hypervisors. 

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

 Upload the downloaded VM image to your ESXi hypervisor. 

 Access your ESXi host or vCenter Server. 

 Upload the downloaded .ova file to a datastore. 

 Create and configure the Virtual Machine. 

 Create a new Virtual Machine. 

 Ensure the option to Power on automatically is deselected. 

 Edit the settings for the VM deployed. 

 Click Add other device and select CD/DVD Drive . 

 Verify the network adapter is configured for the correct network. If
 Dual NIC was specified in template, select the appropriate network for
 Network Adaptor 2 and select the Connect check box. 

 Select Datastore ISO File and browse to select the downloaded
 bootstrap.iso. 

 Ensure the Connect check box is enabled for both the CD/DVD drive
 and the network adapter. 

 Save the VM configuration. 

 Power on the VM and verify agent registration. 

 Power on the configured Virtual Machine. 

 Once the VM has booted, log in to the VM using the default
 username and password. 

 Navigate to your Strata Cloud Manager portal and verify the new
 agent appears with an Active status. 

 Previous 

 Deploy Universal Agent on Virtual Machines 

 Next 

 Install Universal Agent on Hyper V 

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
