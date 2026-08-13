---
url: https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-new-features/virtualization-features/linear-scaling-of-the-vm-series-firewall
fetched_at: 2026-08-13T17:06:36Z
source: palo-alto-main
---

# Memory Scaling of the VM-Series Firewall Clear

Memory Scaling of the VM-Series Firewall 

 Home 

 EN

 Location 

 Documentation Home 

 Palo Alto Networks 

 Support 

 Live Community 

 Knowledge Base 

 Strata Copilot

 PAN-OS ® New Features Guide 

 : 
 Memory Scaling of the VM-Series Firewall 

 Updated on 

 Tue Nov 07 16:09:15 PST 2023 

 Focus 

 Download PDF 

 Filter

 Version 

 10.2 

 10.2 

 Expand all | Collapse all 

 Panorama Features 

 Administrator-Level Push 

 Automatic Content Push for VM-Series and CN-Series Firewalls 

 Increased Device Management Capacity for the Panorama Virtual Appliance 

 Log Collector Health Monitoring on Panorama 

 IoT Security Features 

 Simplified IoT Security Onboarding 

 Data Collection for IoT Security 

 Management Features 

 AIOps for NGFW 

 Selective Commit of Configuration Changes 

 Simplified Software Upgrade 

 Policy Rulebase Management Using Tags 

 Networking Features 

 Advanced Routing Engine 

 IPv4 Multicast for Advanced Routing Engine 

 Policy Features 

 Security Policy Rule Top-Down Order When Wildcard Masks Overlap 

 Content Inspection Features 

 Advanced Threat Prevention: Inline Cloud Analysis 

 Domain Fronting Detection 

 Decryption Features 

 Multiple Certificate Support for SSL Inbound Inspection 

 URL Filtering Features 

 Inline Deep Learning Analysis for Advanced URL Filtering 

 HTTP Header Expansion 

 Mobile Infrastructure Security Features 

 New Deployment Option for GTP Security in 3G/4G Networks 

 Mobile Network Security Support on New Mid-Range Hardware Platforms 

 Virtualization Features 

 CN-Series Firewall as a Kubernetes CNF 

 High Availability Support for CN-Series Firewall as a Kubernetes CNF 

 High Availability Support for CN-Series Firewall on AWS EKS 

 DPDK Support for CN-Series Firewall 

 Daemonset(vWire) IPv6 Support 

 Panorama Plugin for Kubernetes 3.0.0 

 L3 IPV4 Support for CN-Series 

 47 Dataplane Cores Support for VM-Series and CN-Series Firewalls 

 Memory Scaling of the VM-Series Firewall 

 SD-WAN Features 

 Copy ToS Header Support 

 Enterprise Data Loss Prevention Features 

 Web Form Data Inspection for Enterprise Data Loss Prevention 

 Updated on 

 Tue Nov 07 16:09:15 PST 2023 

 Focus 

 Home 

 PAN-OS 

 PAN-OS ® New Features Guide 

 Virtualization Features 

 Memory Scaling of the VM-Series Firewall 

 Download PDF 

 PAN-OS ® New Features Guide 

 Memory Scaling of the VM-Series Firewall 

 Table of Contents 

 Filter

 Version 

 10.2 

 10.2 

 Expand all | Collapse all 

 Panorama Features 

 Administrator-Level Push 

 Automatic Content Push for VM-Series and CN-Series Firewalls 

 Increased Device Management Capacity for the Panorama Virtual Appliance 

 Log Collector Health Monitoring on Panorama 

 IoT Security Features 

 Simplified IoT Security Onboarding 

 Data Collection for IoT Security 

 Management Features 

 AIOps for NGFW 

 Selective Commit of Configuration Changes 

 Simplified Software Upgrade 

 Policy Rulebase Management Using Tags 

 Networking Features 

 Advanced Routing Engine 

 IPv4 Multicast for Advanced Routing Engine 

 Policy Features 

 Security Policy Rule Top-Down Order When Wildcard Masks Overlap 

 Content Inspection Features 

 Advanced Threat Prevention: Inline Cloud Analysis 

 Domain Fronting Detection 

 Decryption Features 

 Multiple Certificate Support for SSL Inbound Inspection 

 URL Filtering Features 

 Inline Deep Learning Analysis for Advanced URL Filtering 

 HTTP Header Expansion 

 Mobile Infrastructure Security Features 

 New Deployment Option for GTP Security in 3G/4G Networks 

 Mobile Network Security Support on New Mid-Range Hardware Platforms 

 Virtualization Features 

 CN-Series Firewall as a Kubernetes CNF 

 High Availability Support for CN-Series Firewall as a Kubernetes CNF 

 High Availability Support for CN-Series Firewall on AWS EKS 

 DPDK Support for CN-Series Firewall 

 Daemonset(vWire) IPv6 Support 

 Panorama Plugin for Kubernetes 3.0.0 

 L3 IPV4 Support for CN-Series 

 47 Dataplane Cores Support for VM-Series and CN-Series Firewalls 

 Memory Scaling of the VM-Series Firewall 

 SD-WAN Features 

 Copy ToS Header Support 

 Enterprise Data Loss Prevention Features 

 Web Form Data Inspection for Enterprise Data Loss Prevention 

 Memory Scaling of the VM-Series Firewall 

 Beginning with PAN-OS 10.2, the maximum number of sessions supported
on an individual VM-Series firewall scales with the amount of memory
allocated to the VM-Series instance. Because memory increments are
not locked in place, you can increase the amount of memory as needed
for your environment. For example, if your VM-Series is assigned
16GB of memory (2,000,000 sessions) but you need to support 3,000,000
sessions, you can increase the memory to 24GB instead of having
to jump all the way to 56GB as in previous PAN-OS releases . Therefore,
in deployments where resources are tight, you no longer need to
statically allocate more memory than necessary to achieve the capacity
you require. 

 For linear scaling, increments of memory are grouped into tiers
that represent the configuration capacity of the VM-Series firewall. Regardless
of the amount of memory you assign to a VM-Series firewall instance,
the tier that amount of memory falls into determine the limit for
non-sessions values, such as security rules, address objects, security
profiles, etc. 

 This feature is enabled by default and requires
no configuration on the VM-Series firewall. VM-Series firewall capacity
scales dynamically with the allocated memory. 

 Previous 

 47 Dataplane Cores Support for VM-Series and CN-Series Firewalls 

 Next 

 SD-WAN Features 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
