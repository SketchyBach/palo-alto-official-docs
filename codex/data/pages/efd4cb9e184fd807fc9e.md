---
url: https://docs.paloaltonetworks.com/vm-series/deployment/public-cloud/set-up-the-vm-series-firewall-on-aws/aws-terminology
fetched_at: 2026-08-13T17:41:47Z
source: palo-alto-main
---

# AWS Terminology Clear

AWS Terminology 

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

 AWS Terminology 

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

 AWS Terminology 

 Download PDF 

 VM-Series 

 AWS Terminology 

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

 VM-Series Firewall on AWS 

 Next 

 VM-Series Firewall on AWS Cloud Environments 

 AWS Terminology 

 A list of AWS terminologies used in this deployment guide for AWS. 

 Where Can I Use This? What Do I Need? 

 AWS 

 AWS account 

 Amazon Machine Image (AMI) ID 

 VM-Series License (PAYG or BYOL) 

 VM-Series plugin 

 Panorama 

 Panorama plugin for AWS 

 This document assumes that you're familiar with the networking and configuration of the AWS VPC.
 To provide context for the terms used in this section, here’s a brief refresher on the
 AWS terms (some definitions are taken directly from the AWS glossary) that are referred
 to in this document: 

 Term 

 Description 

 EC2 

 Elastic Compute Cloud 

 A web service
that enables you to launch and manage Linux/UNIX and Windows server
instances in Amazon's data centers. 

 AMI 

 Amazon Machine Image 

 An AMI provides
the information required to launch an instance, which is a virtual
server in the cloud. 

 The VM-Series AMI is an encrypted machine image that includes the operating system
 required to instantiate the VM-Series firewall on an
 EC2 instance. 

 ELB 

 Elastic Load Balancing 

 ELB is an Amazon Web Service that helps you improve the availability and scalability of your
 applications by routing traffic across multiple Elastic Compute
 Cloud (EC2) instances. ELB detects unhealthy EC2 instances and
 reroutes traffic to healthy instances until the unhealthy instances
 are restored. ELB can send traffic only to the primary interface of
 the next hop load-balanced EC2 instance. So, to use ELB with a
 VM-Series firewall on AWS, the firewall must be able to use the
 primary interface for dataplane traffic. 

 ENI 

 Elastic Network Interface 

 An additional
network interface that can be attached to an EC2 instance. ENIs
can include a primary private IP address, one or more secondary private
IP addresses, a public IP address, an elastic IP address ( optional ),
a MAC address, membership in specified security groups, a description,
and a source/destination check flag. 

 IP address types for EC2 instances 

 An EC2 instance can have different types of IP addresses. 

 Public IP address: An IP address that can be routed across
 the internet. 

 Private IP address: An IP address in the private IP address
 range as defined in the RFC 1918. You can choose to manually
 assign an IP address or to auto assign an IP address within
 the range in the CIDR block for the subnet in which you
 launch the EC2 instance. 

 If you're manually assigning an IP address, Amazon reserves the
 first four (4) IP addresses and the last one (1) IP address in every
 subnet for IP networking purposes. 

 Elastic IP address (EIP): A static IP address that you have
 allocated in Amazon EC2 or Amazon VPC and then attached to
 an instance. Elastic IP addresses are associated with your
 account, not with a specific instance. They are elastic
 because you can easily allocate, attach, detach, and free
 them as your needs change. 

 An instance in a public subnet can have a Private IP address, a
 Public IP address, and an Elastic IP address (EIP); an instance in a
 private subnet will have a private IP address and optionally have an
 EIP. 

 Instance type 

 Amazon-defined specifications that stipulate
the memory, CPU, storage capacity, and hourly cost for an instance.
Some instance types are designed for standard applications, whereas
others are designed for CPU-intensive, memory-intensive applications,
and so on. 

 VPC 

 Virtual Private Cloud 

 An elastic network
populated by infrastructure, platform, and application services
that share common security and interconnection. 

 IGW 

 Internet gateway provided by Amazon. 

 Connects
a network to the internet. You can route traffic for IP addresses outside
your VPC to the internet gateway. 

 IAM Role 

 Identity and Access Management 

 Required for enabling high availability for the VM-Series firewall on AWS. The IAM role defines
 the API actions and resources the application can use after assuming
 the role. On failover, the IAM Role allows the VM-Series firewall to
 securely make API requests to switch the dataplane interfaces from
 the active peer to the passive peer. 

 An IAM role is also
required for VM Monitoring. See List
of Attributes Monitored on the AWS VPC . 

 Subnets 

 A segment of the IP address range of a VPC
to which EC2 instances can be attached. EC2 instances are grouped
into subnets based on your security and operational needs. 

 There
are two types of subnets: 

 Private subnet: The EC2
instances in this subnet cannot be reached from the internet. 

 Public subnet: The internet gateway is attached to the public
subnet, and the EC2 instances in this subnet can be reached from
the internet. 

 Security groups 

 A security group is attached to an ENI and
it specifies the list of protocols, ports, and IP address ranges
that are allowed to establish inbound/outbound connections on the
interface. 

 In the AWS VPC, security groups and network ACLs control inbound and outbound traffic; security
 groups regulate access to the EC2 instance, while network ACLs
 regulate access to the subnet. Because you're deploying the
 VM-Series firewall, set more permissive rules in your security
 groups and network ACLs and allow the firewall to safely enable
 applications in the VPC. 

 Route tables 

 A set of routing rules that controls the
traffic leaving any subnet that is associated with the route table.
A subnet can be associated with only one route table. 

 Key pair 

 A set of security credentials you use to
prove your identity electronically. The key pair consists of a private
key and a public key. At time of launching the VM-Series firewall,
you must generate a key pair or select an existing key pair for
the VM-Series firewall. The private key is required to access the
firewall in maintenance mode. 

 CloudWatch 

 Amazon CloudWatch is a monitoring service
that allows you to collect and track metrics for the VM-Series firewalls
on AWS. When enabled, the firewalls use AWS APIs to publish native
PAN-OS metrics to CloudWatch. 

 Previous 

 VM-Series Firewall on AWS 

 Next 

 VM-Series Firewall on AWS Cloud Environments 

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
