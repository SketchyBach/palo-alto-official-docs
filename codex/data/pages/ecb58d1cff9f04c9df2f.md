---
url: https://docs.paloaltonetworks.com/vm-series/deployment/private-cloud/set-up-a-vm-series-firewall-on-an-esxi-server/install-a-vm-series-firewall-on-vmware-vsphere-hypervisor-esxi/provision-the-vm-series-firewall-on-an-esxi-server
fetched_at: 2026-08-13T17:41:20Z
source: palo-alto-main
---

# Provision the VM-Series Firewall on an ESXi Server Clear

Provision the VM-Series Firewall on an ESXi Server 

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

 Provision the VM-Series Firewall on an ESXi Server 

 Updated on 

 Fri Jun 19 07:13:50 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 VM-Series Firewall Docs 

 Activation & Onboarding 

 Getting Started 

 Upgrade 

 Deployment 

 Select a Document 

 Public Cloud 

 Private Cloud 

 Updated on 

 Fri Jun 19 07:13:50 PDT 2026 

 Focus 

 Home 

 VM-Series 

 VM-Series Firewall on an ESXi Server 

 Install a VM-Series Firewall on VMware vSphere Hypervisor (ESXi) 

 Provision the VM-Series Firewall on an ESXi Server 

 Download PDF 

 VM-Series 

 Provision the VM-Series Firewall on an ESXi Server 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 VM-Series Firewall Docs 

 Activation & Onboarding 

 Getting Started 

 Upgrade 

 Deployment 

 Select a Document 

 Public Cloud 

 Private Cloud 

 Previous 

 Install a VM-Series Firewall on VMware vSphere Hypervisor (ESXi) 

 Next 

 Perform Initial Configuration on the VM-Series on ESXi 

 Provision the VM-Series Firewall on an ESXi Server 

 Prepare your ESXi server to deploy the VM-Series firewall. 

 Where Can I Use
 This? What Do I Need? 

 ESXi Server 

 VM-Series Firewall License (BYOL) 

 Panorama 

 VM-Series plugin 

 Panorama plugin for ESXi 

 Use these instructions to deploy the VM-Series firewall on a (standalone) ESXi
 server. For deploying the VM-Series NSX edition firewall, see VM-Series Firewall on VMware NSX-T . 

 Download the OVA file. 

 Register your VM-Series firewall and obtain the OVA file
from the Palo Alto Networks Customer Support web site . 

 The OVA file contains the base installation. After the base installation is complete, you must
 download and install the latest PAN-OS version from the Customer Support
 Portal. This ensures that you have the latest fixes implemented since
 the base image was created. For instructions, see Upgrade the PAN-OS Software Version
 (Standalone Version) . 

 Before deploying the OVA file, set up virtual standard switches or virtual
 distributed switches that you need for the VM-Series firewall. 

 If you are deploying the VM-Series firewall with Layer 3 interfaces, your
 firewall uses Hypervisor Assigned MAC Addresses 
 by default. If you choose to disable hypervisor assigned MAC address, or if
 you are deploying the firewall with Layer 2, virtual wire, or tap
 interfaces, you must configure (set to Accept ) any
 virtual switch attached to the VM-Series firewall to allow the following
 modes: promiscuous mode, MAC address changes, and Forged transmits. 

 Configure a virtual standard switch or a virtual
 distributed switch to receive frames for the VM-Series firewall. 

 Virtual Standard Switch 

 Navigate to Home Hosts and Clusters and select a host. 

 Click the Configure tab and view
 Virtual Switches . For each VM-Series
 firewall attached a virtual switch, click on
 Properties . 

 Highlight a port group corresponding to a virtual switch and click
 Edit Settings . In the vSwitch properties,
 click the Security tab and set
 Promiscuous Mode, MAC Address Changes and
 Forged Transmits to
 Accept and then click
 OK . This change propagates to all port
 groups on the virtual switch. 

 Virtual Distributed Switch 

 Select Home Networking . Select your virtual distributed switch and highlight
 the Distributed Port Group you want to edit.

 Click Edit Settings , select Policies Security , and set Promiscuous Mode, MAC Address
 Changes and Forged Transmits 
 to Accept and click
 OK . 

 Deploy the OVA. 

 If you add additional interfaces (vNICs) to the VM-Series
firewall, you must reboot (because new interfaces are detected during
the boot cycle). To minimize the need to reboot the firewall, activate
the interfaces at initial deployment or during a maintenance window. 

 To view the progress of the installation, monitor
the Recent Tasks list. 

 Log in to vCenter using the vSphere client.
You can also go directly to the target ESXi host if needed. 

 From the vSphere web client, go to Hosts
and Clusters , right-click your host, and select Deploy
OVF Template . 

 Browse to the OVA file that you downloaded previously.
Select the file, and click Next . Review the
template’s details and click Next . 

 Name the VM-Series firewall instance, and in the Inventory
Location window, select a Data Center and Folder, and
click Next . 

 Select an ESXi host for the VM-Series firewall, and
click Next . 

 Select the datastore to use for the VM-Series firewall,
and click Next . 

 Leave the default settings for the datastore provisioning,
and click Next . The default is Thick
Provision Lazy Zeroed . 

 Select the networks to use for the two initial vNICs.
The first vNIC is used for the management interface and the second
vNIC for the first data port. Make sure that the Source
Networks map to the correct Destination Networks . 

 Review the details, select Power on after
deployment , and click Next . 

 When the deployment is complete, click the Summary tab
to review the current status. 

 Previous 

 Install a VM-Series Firewall on VMware vSphere Hypervisor (ESXi) 

 Next 

 Perform Initial Configuration on the VM-Series on ESXi 

 On This Page 

 Activation and Onboarding 

 Strata Cloud Manager 

 Next-Generation Firewalls 

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 VM-Series 

 Plugins 

 Cloud-Delivered Security Services 

 Advanced WildFire 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 AI Access Security 

 Device Security 

 Enterprise DLP 

 SaaS Security 

 Network Security 

 Shared Policy for NGFWs and Prisma Access 

 IPSec VPN 

 Security Policy 

 Quantum Security 

 Endpoints 

 GlobalProtect 

 Resources 

 All Release Notes 

 Compatibility Matrix 

 Experts Corner 

 VM-Series 

 Deployment 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
