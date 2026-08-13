---
url: https://docs.paloaltonetworks.com/autonomous-dem/activation-and-onboarding/deploy-universal-agent/deploy-universal-agent-on-virtual-machines
fetched_at: 2026-08-13T15:31:10Z
source: palo-alto-main
---

# Deploy Universal Agent on Virtual Machines Clear

Deploy Universal Agent on Virtual Machines 

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

 Deploy Universal Agent on Virtual Machines 

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

 Download PDF 

 Autonomous DEM 

 Deploy Universal Agent on Virtual Machines 

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

 Deploy Universal Agent as Container 

 Next 

 Install Universal Agent on ESXI 

 Deploy Universal Agent on Virtual Machines 

 Deploy ADEM Universal Agent VMs on VMware, Hyper-V, VirtualBox, or KVM for flexible,
 consistent network monitoring across diverse environments managed by Strata™ Cloud
 Manager. 

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

 The ADEM Universal Agent can be deployed on Virtual Machines (VMs) in addition to
 current container deployments. You can deploy Universal Agent on VMs running
 on-premises or hypervisor-based infrastructure. The supported hypervisors are Vmware
 ESXi, Oracle VirtualBox, Microsoft Hyper-V, and KVM. The Universal Agent deployment
 procedure varies based on the hypervisor types. The first step to the Universal
 Agent deployment is to generate and download deployment assets required to install
 the agent on your hypervisor. 

 Generate and Download Deployment Assets 

 Login to Strata Cloud Manager Settings Access Experience Management Universal Agent Add Agent 

 Select Virtual Machine as the installation type to
 enable VM-specific configuration options. 

 Select your VM Type from the dropdown menu, for example,
 ESXi . This ensures the system provides the appropriate base VM image
 and configuration options for your hypervisor. 

 Select the Quantity as Single for single agent deployment or
 Bulk for multiple agents. 

 Configure Network Settings ; select In-band or
 Out-of-band Management . These settings define how the agent VM
 communicates with your network. 

 In-band Management (Single NIC) : Use
 this if you want application traffic and management data to share
 the same interface. 

 Out-band Management (Dual NICs) : This separates
 management traffic on NIC1 and application/CPE traffic on NIC2 for
 better security and performance. 

 Enter a Hostname Prefix to be assigned to the VM (for
 example, Appliance-srv-). This helps in identifying the machine within your
 local DNS or DHCP logs. 

 Enter the IP addresses of the DNS servers the agent should use. 

 Choose DHCP to automatically assign network settings to the agent, or
 Static IP to manually configure a fixed IP address , Subnet
 Mask , and Gateway . 

 Click Generate Deployment Assets . This triggers the
 download of the bootstrap.iso file and the base VM image (for example, an .ova
 file for ESXi, vhdx file for Hyper V). 

 The bootstrap token embedded in the ISO typically expires after 12 hours. 

 The VM image file contains the pre-packaged containerized agent, while the
 bootstrap.iso contains dynamic configuration specific to your template. 

 Note: When you click Generate Deployment Assets , the ISO
 file downloads first, followed by the OVA file. Because the OVA file is
 significantly larger, it will take longer to download. Note that the
 user interface does not show a progress indicator, but the download
 should complete within a few minutes. 

 Confirm any browser prompts for multiple downloads. 

 Previous 

 Deploy Universal Agent as Container 

 Next 

 Install Universal Agent on ESXI 

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
