---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/administration/prisma-sd-wan-nat-policies/use-cases
fetched_at: 2026-08-13T17:28:02Z
source: palo-alto-main
---

# NAT Topologies Use Cases Clear

NAT Topologies Use Cases 

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

 NAT Topologies Use Cases 

 Updated on 

 Mon Aug 10 04:14:37 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma SD-WAN Docs 

 Activation & Onboarding 

 Administration 

 CloudBlades 

 Select a Document 

 CloudBlade Integrations 

 CloudBlades Integration with Prisma Access 

 Deployment 

 Incidents & Alerts 

 Reference 

 Release Notes 

 Select a Document 

 ION 6.8 

 ION 6.6 

 ION 6.5 

 ION 6.4 

 ION 6.3 

 ION 6.1 

 ION 5.6 

 Prisma SD-WAN Controller 

 Prisma SD-WAN On-Premises Controller 

 Prisma SD-WAN CloudBlades 

 Prisma Access CloudBlade Cloud Managed 

 Prisma Access CloudBlade Panorama Managed 

 New Features 

 Updated on 

 Mon Aug 10 04:14:37 PDT 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Prisma SD-WAN Administrator’s Guide 

 Prisma SD-WAN NAT Policies 

 NAT Topologies Use Cases 

 Download PDF 

 Prisma SD-WAN 

 NAT Topologies Use Cases 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma SD-WAN Docs 

 Activation & Onboarding 

 Administration 

 CloudBlades 

 Select a Document 

 CloudBlade Integrations 

 CloudBlades Integration with Prisma Access 

 Deployment 

 Incidents & Alerts 

 Reference 

 Release Notes 

 Select a Document 

 ION 6.8 

 ION 6.6 

 ION 6.5 

 ION 6.4 

 ION 6.3 

 ION 6.1 

 ION 5.6 

 Prisma SD-WAN Controller 

 Prisma SD-WAN On-Premises Controller 

 Prisma SD-WAN CloudBlades 

 Prisma Access CloudBlade Cloud Managed 

 Prisma Access CloudBlade Panorama Managed 

 New Features 

 Previous 

 Configure NAT Prefixes 

 Next 

 Supported NAT Protocol Translation Types 

 NAT Topologies Use Cases 

 Learn the Prisma SD-WAN NAT policies use cases. 

 Where Can I Use
 This? What Do I Need? 

 Prisma SD-WAN (Managed by Strata Cloud Manager ) 

 Prisma SD-WAN 

 Prisma SD-WAN supports several Network Address Translation (NAT)
 topologies to handle common networking needs. The available NAT capabilities include the
 Source
 NAT (which is the default configuration), Destination NAT , Static Source NAT , Static Destination NAT , and the ALG Disable feature. 

 Sample Use Case Typical NAT Capabilities 

 Internal users/devices with private IP addresses need to access to
 the Internet. Source NAT 

 External entities need to communicate with internal entities with
 private IP addresses. Destination NAT 

 Specific internal server needs to communicate with external
 entities. Static Source NAT 

 External entities need to communicate with a specific application
 hosted on an internal server with a private IP address. Static Destination NAT 

 Internal IP phones with private IP addresses need to communicate with
 an external UCaaS system over SIP. ALG Disable 

 Source NAT (Default) 

 By default, Prisma SD-WAN provides an out-of-the-box
 configuration that automatically performs Source NAT on traffic destined directly to
 public internet interfaces. 

 Fields Description 

 1 A new flow source is from Host PC1 with a source
 address of 10.10.10.10 and a destination address of
 60.60.60.60. 

 2 A packet arrives at the ION device’s LAN Interface. A
 policy lookup and a path selection decision perform to put the
 traffic on the link to ISP A. 

 3 Place the packet onto the internet segment; the
 Default-NATPolicySet matches against the
 Default-InternetRule. 
 This rule contains the following
 configuration: 

 Destination Zone Rule: NAT Zone Internet 

 Match Criteria: any protocol, any prefix, any port 

 Action: Source NAT 
 In this rule: 
 The NAT Pool is blank by default, and the system uses the IP
 Address bound to the internet interface. 

 The ION device will ARP for IP addresses where the NAT Pool
 intersects with the configured interface subnet on the ION
 device. 

 Apply the packet's policy; the source
 address of 10.10.10.10 overwrites by the address bound to the
 Internet Interface (50.50.50.1). The source port changes to a
 random port during this operation. 

 In this example the
 original packet: (s) 10.10.10.10:12345: (d) 60.60.60.60:443. Is
 rewritten to: (s) 50.50.50.1:54321: (d)
 60.60.60.60:443. 

 4 Traffic arrives at the internet-based SaaS
 application. 

 5 Traffic returns to the destination of
 50.50.50.1:54321. 

 6 Traffic arrives at the ION device's internet
 interface, where a translation table check is performed on the flow
 to ensure that there is an active connection. 

 7 Establish the traffic onto the LAN segment; the
 destination IP address returns from 50.50.50.1:54321 to
 10.10.10.10:12345. 

 Destination NAT 

 Prisma SD-WAN destination NAT securely permits inbound
 connections from the internet to access internal private IP resources at a branch
 site location. 

 One of the use cases involves physical security monitoring services that
 require direct inbound connections from the internet and outbound connections from
 the local device, often implemented with a dedicated 1:1 NAT configuration. In this
 example, the external system Host 1 needs to communicate with Server 1 in the branch
 location across the internet. For Host 1, the IP address for the branch service is
 50.50.50.2 and port 443. 

 Fields Description 

 1 A new flow source from Host 1 with a source address
 of 70.70.70.70 and a destination address of 50.50.50.2. 

 2 The packet arrives at the ION device's internet
 interface. It performs the policy lookup and the traffic on the LAN
 path. 

 3 Place the packet onto the LAN segment and match it
 against the recently created NAT Policy Rule. 
 This rule contains
 the following configuration: 

 Source Zone Rule: NAT Zone Internet 
 The NAT Zone Internet
 is bound to the interface. 

 Match Criteria: 
 Protocol: TCP 

 Source Prefix: Any 

 Source Port Range: Any: Any 

 Destination Prefix: Internet-Services-Prefix 
 This
 a local prefix filter, and the entry for this site
 is 50.50.50.2/32 

 Destination Port Range: 443:443 (leave blank if all
 ports are allowed) 

 The ION
 device sends GARP messages and responds to ARP
 requests for 50.50.50.2. 

 Action: Destination NAT 

 NAT Pool: LAN-Services 

 The NAT Pool LAN-Services define as 10.10.10.20 -
 10.10.10.20 on the branch ION device. 

 NAT Pools are defined in persisting ranges and can be
 configured through the NAT Policy UI or directly through the
 device-level interface configuration. 

 As the policy
 applies to the packet, the original destination address is
 50.50.50.2, overwrites by the NAT Pool LAN-Services address. In this
 example the original packet (s) 70.70.70.70:12345: (d)
 50.50.50.2:443. Is rewritten to: (s) 70.70.70.70:12345: (d)
 10.10.10.20:443. 

 4 Traffic arrives on the LAN at the server hosting
 inbound services from the internet. 

 5 Sends the return traffic to the destination of
 70.70.70.70:12345. 

 6 Traffic arrives at the ION device's LAN interface,
 where a translation table check is performed on the flow to ensure
 that there is an active connection. 

 7 Establish the traffic onto the LAN segment, the
 source IP address is rewritten from 10.10.10.10:443 to
 50.50.50.2:443. 

 If traffic that originates
 from Server 1 (10.10.10.20) also needs to be translated to
 50.50.50.2 and a corresponding Source NAT Rule is
 configured. 

 Static NAT 

 Prisma SD-WAN provides scenarios that require a 1:1
 mapping of a range of IP addresses to another range of IP addresses. 

 Scenarios include direct mapping of a publicly routable range of IP addresses to RFC
 1918 addresses. For example, they translate 50.50.50.16-31 to 10.10.10.16-31 in a
 1:1 manner where traffic would translate to 50.50.50.20 to 10.10.10.20 and vice
 versa across the entire IP range. 

 Another common scenario would be when IP prefix overlap occurs due to a company
 merger. In this situation, it would also translate the IP addresses bound to the
 hosts in a 1:1 manner from one RFC 1918 range to another RFC 1918m range. In this
 example, application requirements specify that each internal server must have a
 unique internet IP address. Each server must initiate connections on ephemeral ports
 and receive inbound links on the same persistent IP address on port 443. To enable
 this most efficiently, use static source NAT and static destination NAT. 

 Static Source NAT 

 Another NAT usecase is inbound connection from the Internet. 

 Fields Description 

 5 A new flow source from Server 1 with a source
 address of 10.10.10.20 and a destination address of
 70.70.70.80. 

 6 A packet arrives at the ION device's internet
 interface. Perform a policy lookup and the traffic on the LAN
 segment. 

 7 Place the packet onto the internet segment; it
 matches against the recently created NAT Policy Rule. 
 This
 rule contains the following configuration: 

 Destination Zone Rule: NAT Zone Internet 
 The NAT Zone
 internet is bound to the interface. 

 Match Criteria: 
 Protocol: Any: Any (blank) 

 Source Prefix: LAN-Services-Prefix 
 This is a
 local prefix filter, and the entry for this site
 is 10.10.10.16/28 

 Source Port Range: Any: Any (blank) 

 Destination Prefix: Any: Any (blank) 

 Action: Static Destination NAT 

 NAT Pool: Internet-Services 

 The NAT Pool Internet-Services is defined as
 50.50.50.50.16 - 50.50.50.50.31 on the branch ION
 device. 

 The ION device sends GARP
 messages and responds to ARP requests for 50.50.50.16/28.
 NAT Pools can be configured through the NAT Policy UI or
 directly on the interface configuration and defined in
 contiguous ranges. 

 As the policy applies to the
 packet, the original source address of 10.10.10.20 overwrites by
 the address defined in the NAT Pool Internet-Services. In this
 example the original packet: (s) 10.10.10.20:12345: (d)
 70.70.70.80:443. Is rewritten to: (s) 50.50.50.20:12345: (d)
 70.70.70.80:443. 

 8 Traffic crosses the internet and arrives at the
 destination server 70.70.70.80. Return traffic processes in the
 reverse order, and the ION device references the original
 outbound connection previously opened with the Static Source NAT
 action. 

 Static Destination NAT 

 Case: Outbound Connection from the Local Server to an Internet Service. 

 Fields Description 

 1 A new flow source from Host 1 with a source
 address of 70.70.70.70 and a destination address of
 50.50.50.20. 

 2 A packet arrives at the ION device's internet
 interface. Perform a policy lookup and the traffic on the LAN
 segment. 

 3 Place the packet onto the LAN segment; it matches
 against the recently created NAT Policy Rule. 
 This rule
 contains the following configuration: 

 Source Zone Rule: NAT Zone Internet 
 The NAT Zone
 internet is bound to the interface. 

 Match Criteria: 
 Protocol: TCP (leave blank for any
 protocol) 

 Source Prefix: Any 

 Source Port Range: Any: Any (blank) 

 Destination Prefix: Internet-Services 
 This is
 a local prefix filter, and the entry for this site
 is 50.50.50.16/28 

 Destination Port Range: 443:443 (leave blank if
 all ports are allowed) 

 The
 ION device sends GARP messages and responds to ARP
 requests for 50.50.50.2. 

 Action: Static Destination NAT 

 NAT Pool: LAN-Services 

 The NAT Pool LAN-Services is defined as 10.10.10.16 -
 10.10.10.31 on the branch ION device. It can be configured
 through the NAT Policy UI or directly on the interface
 configuration of the device. 

 NAT
 Pools are in contiguous ranges. 

 As the policy
 applies to the packet, the original destination address of
 50.50.50.20 overwrites by the address defined in the NAT
 Pool LAN-Services. In this example the original packet: (s)
 70.70.70.70:12345: (d) 50.50.50.20:443. Is rewritten to: (s)
 70.70.70.70:12345: (d) 10.10.10.20:443. 

 4 Traffic arrives on the LAN at the server hosting
 inbound services from the internet. 

 5 Sends the return traffic to the destination of
 70.70.70.70:12345. 

 6 Traffic arrives at the ION device's LAN
 interface, where a translation table check is performed on the
 flow to ensure that there is an active connection. 

 7 Establish the traffic onto the LAN segment, the
 source IP address is rewritten from 10.10.10.10:443 to
 50.50.50.2:443. 

 ALG Disable 

 Prisma SD-WAN application fabric is a critical enabler of
 this transition by emphasizing Voice & Video quality reporting and SLA
 assurance. As the consumption of these services has changed, it has driven new
 demands of the network. Specifically, many UCaaS systems require that network
 solution providers disable the SIP ALG (Application Layer Gateway) for any traffic
 that crosses a NAT boundary destined for a SIP provider. 

 In this example, a phone is configured at the branch to communicate with
 a UCaaS system on the internet via SIP (Session Initiation Protocol), a standard
 protocol used by collaboration endpoints to register with the intended control
 system. The SIP traffic (via Path Policy) configures to be placed directly onto any
 available internet link. As such, it uses the default NAT policy. The UCaaS provider
 has also specified that any SIP ALG must be disabled. Disabling the SIP ALG prevents
 issues from occurring that may affect phone registration and 1-way audio. 

 Fields Description 

 1 A new SIP registration source from Phone 1 with a
 source address of 10.10.20.20 and a destination address of
 80.80.80.80. 

 2 A packet arrives at the ION device's LAN interface.
 Perform a policy lookup and the traffic on the internet
 segment. 

 3 Place the packet onto the internet segment; the
 Default-NATPolicySet it matches against the
 Default-InternetRule. 
 This rule contains the following
 configuration: 

 Destination Zone Rule: NAT Zone Internet 

 Match Criteria: Any Protocol, Any Prefix, Any Port 

 Action: Source NAT 

 In this rule, the NAT Pool is blank by default, and the
 system uses the IP Address bound to the internet
 interface. 

 Apply the packet's policy;
 the source address of 10.10.10.10 overwrites by the address
 bound to the Internet Interface (50.50.50.1), and it might
 change the source port to a random port during this
 operation. 

 In this example the original packet: (s)
 10.10.20.20:12345: (d) 80.80.80.80:5060. Is rewritten to: (s)
 50.50.50.1:54321: (d) 80.80.80.80:5060. 

 4 In addition to the default NAT policy, the traffic
 also matches the recently created rule to disable the SIP ALG. 
 Destination Zone Rule: NAT Zone Internet 

 Match Criteria: 
 Protocol: Any: Any (blank) 

 Source Prefix: 
 Local Prefix Filter - 10.10.20.0/24 (Phone
 Network) 

 Source Port Range: Any: Any (blank) 

 Destination Prefix: Any (blank) 

 Destination Port Range: Any: Any (blank) 

 Action: ALG Disable 

 ALG Protocols to Disable: SIP 

 5 Traffic arrives at the SIP server directly on the
 internet. 

 6 Send the return traffic to the destination of
 50.50.50.1:54321. A translation table check is performed on the flow
 to ensure that there is an active connection. 

 7 Establish the traffic onto the LAN segment; the
 destination IP address is rewritten from 50.50.50.1:54321 to
 10.10.20.20:12345. 

 To clone the
 Default-NATPolicySet, add the appropriate policy settings and
 apply this newly created set to the intended target site(s).When
 required to change ALG behavior, it is best practice to create a
 new Policy Set Stack. Once created, add the Default-NATPolicySet
 to the stack, then create a new NAT Set with a rule that
 disables ALG. Bind the new NAT Set to the new NAT
 Stack. 

 Previous 

 Configure NAT Prefixes 

 Next 

 Supported NAT Protocol Translation Types 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Activate a License or Product 

 Cloud Identity Engine 

 Hub 

 Identity and Access Management 

 Tenant Management 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 AI-Powered ADEM 

 Prisma Access Monitoring and Visibility 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 FedRAMP 

 Prisma SASE for FedRAMP 

 Hardware Reference 

 ION 1000 

 ION 1200 

 ION 1200-S 

 ION 2000 

 ION 3000 

 ION 3200 and ION 3200H 

 ION 5200 

 ION 7000 

 ION 9000 

 ION 9200 

 Hardware Quick Start Guides 

 ION 1200 

 ION 1200 4G 

 ION 1200 5G 

 ION 1200-S 

 ION 1200-S 4G 

 ION 1200-S 5G 

 ION 3200 

 ION 3200H 

 ION 3200H 5G 

 ION 5200 

 ION 9200 

 Virtual ION Deployment 

 Virtual ION on AWS 

 Virtual ION on Azure 

 Virtual ION on GCP 

 Virtual ION on Alibaba Cloud 

 Virtual ION on KVM for NFV 

 Virtual ION on OCI 

 Virtual ION on VMware 

 Virtual ION on Megaport Virtual Edge 

 Virtual ION on Dell PowerEdge 

 Prisma SD-WAN Integration 

 AWS Cloud-WAN Integration (GRE Connect) 

 AWS Cloud-WAN Integration (Tunnel-less Connect) 

 Checkpoint Integration 

 LiveAction Integration 

 Netskope Integration 

 Symantec Web Security Services Integration 

 Prisma SD-WAN Experts Corner 

 Network Policy 

 QoS Whitepaper 

 Security Architecture Whitepaper 

 External Antennas for ION-C Series 

 Dynamic Path Selection 

 Best Practices 

 Best Practices Library 

 Resources 

 All Products A - Z 

 Compatibility Matrix 

 SASE 

 Administration 

 Prisma SD-WAN 

 Strata Cloud Manager 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
