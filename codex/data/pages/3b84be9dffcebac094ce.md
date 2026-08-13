---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/ion-cli-reference/use-cli-commands/debug-commands/trace-route
fetched_at: 2026-08-13T17:29:56Z
source: palo-alto-main
---

# traceroute Clear

traceroute 

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

 traceroute 

 Updated on 

 Tue Jun 02 09:34:24 PDT 2026 

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

 Tue Jun 02 09:34:24 PDT 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Use CLI Commands 

 Debug Commands 

 traceroute 

 Download PDF 

 Prisma SD-WAN 

 traceroute 

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

 tcpping 

 Next 

 traceroute6 

 traceroute 

 Use the traceroute command to
print the route taken by packets to a destination and to identify the
route or measure packet transit delays across a network. 

 Command 

 traceroute interface dst-ipv4 (args=" ") 

 Options 

 dst-ipv4 Enter the interface to listen on. 

 interface Enter the interface name or ID. 

 args= "-F" Use when probe packets should not be fragmented. 

 args= "-l" Displays the time-to-live (TTL) value of the returned
packet. 

 args="-l" Use ICMP ECHO instead of UDP datagrams. 

 args="-m number" Enter the maximum number of hops (max TTL value)
that trace route probe. 

 args= "-n" Print hop addresses numerically rather than symbolically. 

 args="-p string" This is the base UDP port number used in probes (default
value is 33434). 

 args="-q number" Enter the number of probe packets per TTL.
The default value is 3. 

 args= "-t number" Enter a value for Type of Service (TOS) in
probe packets. The default value is 0. 

 args="-w number" Enter a time (in seconds) to wait for a response to
a probe. The default value is 3 seconds. 

 Command Notes 

 Role Super, Read Only 

 Related Commands — 

 Introduced in Release 4.4.1 

 Example 

 traceroute 1 8.8.8.8 args="-n"
 traceroute to 8.8.8.8 (8.8.8.8), 30 hops max, 46 byte packets 1
 200.30.0.2 92.231 ms 92.298 ms 92.241 ms 2 10.0.0.1 92.336 ms
 92.327 ms 92.388 ms 3 66.128.148.171 93.410 ms 93.279 ms * 4
 206.72.210.41 102.026 ms 102.013 ms 103.401 ms 5 108.170.247.225
 101.901 ms * 108.170.247.161 101.729 ms 6 108.177.3.235 102.291 ms
 72.14.232.197 102.165 ms 108.170.238.7 102.435 ms 7 8.8.8.8
 101.937 ms 101.563 ms 102.023 ms 

 Previous 

 tcpping 

 Next 

 traceroute6 

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

 CLI 

 Reference 

 Prisma SASE 

 Prisma SD-WAN ION CLI Reference 

 Prisma SD-WAN 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
