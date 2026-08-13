---
url: https://docs.paloaltonetworks.com/vm-series/deployment/public-cloud/set-up-the-vm-series-firewall-on-aws/high-availability-for-vm-series-firewall-on-aws
fetched_at: 2026-08-13T17:41:50Z
source: palo-alto-main
---

# High Availability for VM-Series Firewall on AWS Clear

High Availability for VM-Series Firewall on AWS 

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

 High Availability for VM-Series Firewall on AWS 

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

 VM-Series Firewall on AWS 

 High Availability for VM-Series Firewall on AWS 

 Download PDF 

 VM-Series 

 High Availability for VM-Series Firewall on AWS 

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

 Enable Session Resiliency on VM-Series for AWS 

 Next 

 IAM Roles for HA 

 High Availability for VM-Series Firewall on AWS 

 Learn the prerequisites and the steps to enable high availability for VM-Series firewall deployment in AWS. 

 Where Can I Use This? What Do I Need? 

 AWS 

 AWS account 

 Amazon Machine Image (AMI) ID 

 VM-Series License (PAYG or BYOL) 

 VM-Series plugin 

 Panorama 

 Panorama plugin for AWS 

 The VM-Series firewall on AWS supports active/passive HA only; if it is deployed with
 Amazon Elastic Load Balancing (ELB), it does not support HA (in this case ELB provides
 the failover capabilities). 

 To ensure redundancy, you can deploy the VM-Series firewalls on AWS in an active/passive
 high availability (HA) configuration. The active peer continuously synchronizes its
 configuration and session information with the identically configured passive peer. A
 heartbeat connection between the two devices ensures failover if the active device goes
 down. There are two options for deploying the VM-Series firewall on AWS in HA—Secondary
 IP move and Dataplane Interface (ENI) move. 

 To ensure that all traffic to your internet-facing applications passes through the
 firewall, you have two options. You can either configure the application’s public IP
 address on the Untrust interface (E1/2 in the illustration above) of the VM-Series
 firewall, or you can configure AWS ingress routing. The AWS ingress routing capability
 allows you to associate route tables with the AWS internet gateway and add route rules
 to redirect the application traffic through the VM-Series firewall. This redirection
 ensures that all internet traffic passes through the firewall without having to
 reconfigure the application endpoints. 

 Secondary IP Move 

 When the active peer goes down, the passive peer detects this failure and becomes
 active. Additionally, it triggers API calls to the AWS infrastructure to move the
 configured secondary IP addresses from the dataplane interfaces of the failed peer
 to itself. Additionally, AWS updates the route tables to ensure that traffic is
 directed to the active firewall instance. These two operations ensure that inbound
 and outbound traffic sessions are restored after failover. This option allows you to
 take advantage of DPDK to improve the performance of your VM-Series firewall
 instances and provides better failover time than interface-move HA, while supporting
 all the features provided by interface-move. 

 Secondary IP Move HA requires VM-Series plugin 2.0.1 or later. 

 You can now configure up to four IP addresses per SD-WAN interface, to achieve HA
 failover in active/passive configurations of your AWS public cloud environment.
 You can achieve this by configuring a second floating IP address on the SD-WAN
 interfaces. The floating IP on the SD-WAN interface of the external zone must
 match with that of the internal zone. This feature is supported on PAN-OS 11.1.0
 and above and on IPv4 addresses only. 

 Dataplane Interface Move 

 When the active peer goes down, the passive peer detects the failure and becomes
 active. Additionally, it triggers API calls to the AWS infrastructure to move all
 the dataplane interfaces (ENIs) from the failed peer to itself. 

 HA Links 

 The devices in an HA pair use HA links to synchronize data and maintain state
 information. On AWS, the VM-Series firewall uses the following ports: 

 Control Link —The HA1 link is used to exchange hellos, heartbeats, and
 HA state information, and management plane sync for routing and User-ID
 information. This link is also used to synchronize configuration changes on
 either the active or passive device with its peer. 

 The management port is used for HA1. TCP port 28769 and 28260 for cleartext
 communication; port 28 for encrypted communication (SSH over TCP). 

 Data Link —The HA2 link is used to synchronize sessions, forwarding
 tables, IPSec security associations and ARP tables between devices in an HA
 pair. Data flow on the HA2 link is always unidirectional (except for the HA2
 keep-alive); it flows from the active device to the passive device. 

 Ethernet1/1 must be assigned as the HA2 link; this is required to deploy the
 VM-Series firewall on AWS in HA. The HA data link can be configured to use
 either IP (protocol number 99) or UDP (port 29281) as the transport. 

 The VM-Series firewall on AWS does not support backup links for HA1 or HA2. 

 Heartbeat Polling and Hello Messages 

 The firewalls use hello message and heartbeats to verify that the peer device is
 responsive and operational. Hello messages are sent from one peer to the other at
 the configured Hello Interval to verify the state of the device. The
 heartbeat is an ICMP ping to the HA peer over the control link, and the peer
 responds to the ping to establish that the devices are connected and responsive. For
 details on the HA timers that trigger a failover, see HA Timers . (The HA timers for the VM-Series firewall are the same as that
 of the PA-5200 Series firewalls). 

 Device Priority and Preemption 

 The devices in an HA pair can be assigned a device priority value to
 indicate a preference for which device should assume the active role and manage
 traffic upon failover. If you need to use a specific device in the HA pair for
 actively securing traffic, you must enable the preemptive behavior on both the
 firewalls and assign a device priority value for each device. The device with the
 lower numerical value, and therefore higher priority , is designated as
 active and manages all traffic on the network. The other device is in a passive
 state, and synchronizes configuration and state information with the active device
 so that it is ready to transition to an active state should a failure occur. 

 By default, preemption is disabled on the firewalls and must be enabled on both
 devices. When enabled, the preemptive behavior allows the firewall with the
 higher priority (lower numerical value) to resume as active after
 it recovers from a failure. When preemption occurs, the event is logged in the
 system logs. 

 Preemption is not recommended for HA in the VM-Series firewall on AWS. 

 HA Timers 

 High availability (HA) timers are used to detect a firewall failure and trigger a
 failover. To reduce the complexity in configuring HA timers, you can select from
 three profiles: Recommended ,
 Aggressive , and Advanced . These
 profiles auto-populate the optimum HA timer values for the specific firewall
 platform to enable a speedier HA deployment. 

 Use the Recommended profile for typical failover timer
 settings and the Aggressive profile for faster failover timer
 settings. The Advanced profile allows you to customize the
 timer values to suit your network requirements. 

 HA Timer on the VM-Series on AWS 

 Default values for Recommended/Aggressive
 profiles 

 Promotion hold time 

 2000/500 ms 

 Hello interval 

 8000/8000 ms 

 Heartbeat interval 

 2000/1000 ms 

 Max number of flaps 

 3/3 

 Preemption hold time 

 1/1 min 

 Monitor fail hold up time 

 0/0 ms 

 Additional master hold up time 

 500/500 ms 

 Previous 

 Enable Session Resiliency on VM-Series for AWS 

 Next 

 IAM Roles for HA 

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
