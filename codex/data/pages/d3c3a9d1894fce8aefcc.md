---
url: https://docs.paloaltonetworks.com/vm-series/deployment/private-cloud/deploy-the-vm-series-firewall-on-cisco-csp
fetched_at: 2026-08-13T17:41:14Z
source: palo-alto-main
---

# Deploy the VM-Series Firewall on Cisco CSP Clear

Deploy the VM-Series Firewall on Cisco CSP 

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

 Deploy the VM-Series Firewall on Cisco CSP 

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

 Deploy the VM-Series Firewall on Cisco CSP 

 Download PDF 

 VM-Series 

 Deploy the VM-Series Firewall on Cisco CSP 

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

 Deploy the VM-Series Firewall on Cisco ENCS 

 Deploy the VM-Series Firewall on Cisco CSP 

 Deploy the VM-Series firewall on the Cisco Cloud Security Platform (CSP) with the
 VM-Series base image from Palo Alto Networks Customer Support Portal. 

 Where Can I Use This? What Do I Need? 

 Cisco CSP 

 VM-Series plugin 

 Panorama 

 VM-Series licenses 

 Panorama plugin for Cisco CSP 

 You can deploy the VM-Series firewall as a network virtual service on
 the Cisco Cloud Security Platform (CSP). Since the Cisco CSP runs on the RHEL KVM
 platform, you can deploy the VM-Series firewall using the VM-Series firewall for a
 KVM base image. 

 With the VM-Series firewall on Cisco CSP, you can protect your workloads, prevent
 advanced threats, and improve visibility into the applications on your virtual
 network. 

 System Requirements 

 You can create and deploy multiple instances—standalone or as an HA
 pair—of the VM-Series firewall on your Cisco CSP. 

 See the Compatibility Matrix for supported
 versions of Palo Alto Networks Customer Support Portal and PAN-OS. 

 Bootstrap Package converted to an
 ISO file. 

 See VM-Series System Requirements for
 the minimum hardware requirements for your VM-Series model. 

 The VM-Series firewall on Cisco CSP supports all VM-Series models except the
 VM-50. 

 Minimum of two network interfaces (vNICs). One is a dedicated vNIC for the
 management interface and one is for the data interface. You can then add up
 to eight more vNICs for data traffic. 

 SR-IOV and packet MMAP mode only; DPDK isn't supported. 

 Follow the steps below to deploy the VM-Series firewall as a service on Cisco CSP. 

 Download the VM-Series qcow2 base image file from the Customer Support Portal . 

 Create a Bootstrap Package for your VM-Series
 firewall. Create an ISO file containing the bootstrap package using your
 preferred tool. 

 Log in to the Cisco CSP web interface. 

 Upload the VM-Series firewall qcow2 image and ISO file. 

 Select Configuration Repository . 

 Click the plus (+) icon. 

 Select Browse and navigate to your qcow2 
 file. 

 Select Upload . 

 Select Browse and navigate to your ISO file.

 Select Upload . 

 Create the VM-Series firewall service. 

 Enter a descriptive Name for
the VM-Series firewall. 

 Select the Target Host Name . 

 Select the qcow2 file you uploaded from the Image
 Name . 

 Select the Day Zero Config. 

 Select the bootstrap ISO file in Source File
 Name . 

 Select Submit . 

 Allocate the number of cores and memory required for your VM-Series firewall . 

 Add enough vNICs to support the number of VM-Series
interfaces configured in your bootstrap ISO file. 

 See the Cisco Cloud Service Platform
documentation for more information about creating and deploying
a service instance. 

 After the bootstrap process is complete, log in to your VM-Series firewall
 using the management IP address you specified in the bootstrap ISO file. 

 The firewall should be up and configured based on the parameters you defined
 in the bootstrap package. 

 Previous 

 Deploy the VM-Series Firewall on Cisco ENCS 

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
