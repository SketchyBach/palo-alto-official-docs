---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/ion-cli-reference/use-cli-commands/dump-commands/dump-routing-running-config
fetched_at: 2026-08-13T17:30:32Z
source: palo-alto-main
---

# dump routing running-config Clear

dump routing running-config 

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

 dump routing running-config 

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

 Dump Commands 

 dump routing running-config 

 Download PDF 

 Prisma SD-WAN 

 dump routing running-config 

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

 dump routing routemap 

 Next 

 dump routing summary 

 dump routing running-config 

 Use the dump routing running-config command
to display the current routing configuration for a device. 

 Command 

 dump routing running-config

 Options 

 None 

 Command Notes 

 Role Super, Read Only, Monitor 

 Related Commands — 

 Introduced in Release 5.0.1 

 Example 

 dump routing running-config
 Building configuration...
 Current configuration:
 !
 log syslog notifications
 log facility syslog
 bgp multiple-instance
 !
 debug zebra rib
 debug bgp
 !
 password default
 !
 interface br0
 ipv6 nd suppress-ra
 !
 ...
 router bgp 7000
 bgp router-id 172.20.75.146
 neighbor 172.120.16.8 remote-as 1234
 neighbor 172.120.16.8 description "core peer 15296501950110247"
 neighbor 172.120.16.8 advertisement-interval 1
 neighbor 172.120.16.8 timers 30 90 |
 neighbor 172.120.16.8 timers connect 120
 neighbor 172.120.16.8 soft-reconfiguration inbound
 neighbor 172.120.16.8 route-map auto-core-15296501950110247-routemap-in in
 neighbor 172.120.16.8 route-map auto-core-15296501950110247-routemap-out out
 !
 ip prefix-list PLC seq 2 permit 10.10.10.0/24 ge 28 le 30
 ip prefix-list 172.120.16.8 seq 5 permit 172.120.16.8/32
 !
 ip as-path access-list auto-core-15296501950110247-as-path-outpermit .*
 !
 route-map auto-core-15296501950110247-route-map-in permit 10
 set local-preference 100
 !
 route-map auto-core-15296501950110247-route-map-out permit 99
 match as-path auto-core-15296501950110247-as-path-out
 match ip address prefix-list auto-prefix-adv-and-distribute set
 as-path prepend 7000,7000,7000,7000
 !
 route-map peer-172.120.16.8-show permit 10
 match ip next-hop prefix-list 172.120.16.8
 !
 ip forwarding!line vty
 !
 end 

 Previous 

 dump routing routemap 

 Next 

 dump routing summary 

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
