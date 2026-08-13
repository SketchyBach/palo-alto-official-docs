---
url: https://docs.paloaltonetworks.com/vm-series/deployment/public-cloud/set-up-the-vm-series-firewall-on-oracle-cloud-infrastructure
fetched_at: 2026-08-13T17:42:17Z
source: palo-alto-main
---

# VM-Series Firewall on Oracle Cloud Infrastructure Clear

VM-Series Firewall on Oracle Cloud Infrastructure 

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

 VM-Series Firewall on Oracle Cloud Infrastructure 

 Updated on 

 Jul 8, 2026 

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

 Jul 8, 2026 

 Focus 

 Home 

 VM-Series 

 VM-Series Firewall on Oracle Cloud Infrastructure 

 Download PDF 

 VM-Series 

 VM-Series Firewall on Oracle Cloud Infrastructure 

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

 Deploy the GCP Active/Passive HA 

 Next 

 Prepare to Set Up the VM-Series Firewall on OCI 

 VM-Series Firewall on Oracle Cloud Infrastructure 

 Learn about the VM-Series firewall deployment on OCI. 

 Where Can I Use This? What Do I Need? 

 Oracle Cloud Infrastructure (OCI) instance 

 VM-Series License (BYOL) 

 VM-Series plugin 

 Panorama 

 Panorama plugin for OCI 

 Deploy the VM-Series firewall on Oracle Cloud Infrastructure (OCI)
 cloud. With the VM-Series on OCI, you can protect and segment your
 workloads, prevent advanced threats, and improve visibility into your applications as
 you move to the cloud. 

 OCI is a public cloud computing service that enables you to run your applications in a highly
 available, hosted environment offered by Oracle. You can deploy the VM-Series firewall to secure your applications and services running in
 your OCI environment. 

 The VM-Series firewalls support the following OCI VM shapes.
 See the Oracle Cloud Infrastructure documentation for
 more information about VM shapes. 

 VM-Series Model Minimum OCI Shape OCPUs Memory 

 VM-100 

 Software NFGW Credit-based VM-Series 

 VM.Standard2.4 4 60 

 VM-300 

 Software NFGW Credit-based VM-Series 

 VM.Standard2.4 4 60 

 VM-500 

 Software NFGW Credit-based VM-Series 

 VM.Standard2.8 8 120 

 VM-700 

 Software NFGW Credit-based VM-Series 

 VM.Standard2.16 16 240 

 VM-100, VM-300, VM-500, and VM-700 

 Software NFGW Credit-based VM-Series 

 VM.Optimized3.Flex 

 VM.Standard3.Flex 

 18 256 

 VM-100, VM-300, VM-500, and VM-700 

 Software NFGW Credit-based VM-Series 

 VM.Standard.E4.Flex (AMD instance) comes with default 1 CPU and maximum of 64 OCPUs 64 GB per OCPU, up to 1024 GB total 

 VM.Standard.E5.Flex (AMD instance) comes with default 1 CPU and maximum of 94 OCPUs 64 GB per OCPU, up to 1049 GB total 

 VM.Standard.E6.Flex (AMD instance) comes with default 1 CPU and maximum of 126 OCPUs 64 GB per OCPU, up to 1454 GB total 

 AMD VM.Standard.E4.Flex, VM.Standard.E5.Flex, and VM.Standard.E6.Flex instances come
 with one default CPU and supports one vNIC. For multiple vNICs, configure OCPUs in
 the required range. 

 You can deploy the VM-Series firewall on an OCI instance with more
 resources than the minimum VM-Series System Requirements . If you choose a
 larger shape size for the VM-Series firewall model. Although the firewall
 only uses the maximum vCPUs cores and memory listed on the system requirements page, it
 does take advantage of the faster network performance that the larger shape provides. 

 Deployments Supported on OCI 

 Use the VM-Series firewall on OCI to secure your cloud
 environment in the following scenarios: 

 North-South Traffic —You can use the VM-Series firewall
 to secure traffic entering your cloud network from an untrusted source or
 exiting your cloud network to reach an untrusted source. For either type of
 traffic, you must configure route table rules in your VCN and NAT policy
 rules on the firewall. 

 In this example, outbound traffic is exiting the trust subnet in your VCN.
 You must configure a source address translation policy onto a public IP
 address and a route table rule that redirects that traffic to the firewall.
 The route rule points outgoing traffic to the firewall’s interface in the
 trust subnet of the VCN. When the firewall receives this traffic, it
 performs the source address translation on the traffic and applies any other
 security policy you have configured. 

 Inter-VCN Traffic (East-West) —The VM-Series firewall
 allows you to secure traffic moving within your cloud environment between
 Virtual Cloud Networks (VCN). Each subnet must belong to a different VCN
 because, by default, no route rules are used to enable traffic within a VCN.
 In this scenario, you configure an interface on the firewall connected to a
 subnet in each VCN. 

 In the example below, a user in the Trust subnet wants to access data in the
 DB subnet. Configure a route on OCI that reaches DB subnet CIDR next hop,
 which points to the interface Trust subnet network on the VM-Series
 firewall. 

 OCI uses a series of route tables to send traffic out of your VCN and one route table
 is added to each subnet. A subnet is a division of your VCN. If you don't specify a
 route table, the subnet uses the VCN’s default route table. 

 Each route table rule specifies a destination CIDR block and a next hop (target) for
 any traffic that matches the CIDR. OCI only uses a subnet’s route table if the
 destination IP address is outside the VCN’s specified CIDR block; route rules are
 not required to enable traffic within the VCN. And, if traffic has overlapping
 rules, OCI use the most specific rule in the route table to route traffic. 

 If there is no route rule that matches the traffic that’s attempting to leave the
 VCN, the traffic is dropped. 

 Each subnet requires a route table and once you have added a route table to a subnet,
 you can't change it. However, you can add, remove, or edit rules in a route table
 after it has been created. 

 Previous 

 Deploy the GCP Active/Passive HA 

 Next 

 Prepare to Set Up the VM-Series Firewall on OCI 

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

 Cloud Infrastructure Protection 

 Network Security 

 Deployment 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
