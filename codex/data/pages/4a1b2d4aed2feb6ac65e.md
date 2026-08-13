---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/ion-cli-reference/use-cli-commands/inspect-commands/inspect-network-policy-conflicts
fetched_at: 2026-08-13T17:30:56Z
source: palo-alto-main
---

# inspect network-policy conflicts Clear

inspect network-policy conflicts 

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

 inspect network-policy conflicts 

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

 Inspect Commands 

 inspect network-policy conflicts 

 Download PDF 

 Prisma SD-WAN 

 inspect network-policy conflicts 

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

 inspect memory summary 

 Next 

 inspect network-policy dropped 

 inspect network-policy conflicts 

 Use the inspect network-policy conflicts command to detect and display network policy rules with overlapping classification criteria that create ambiguity about which rule applies to matching traffic. 

 Use the inspect network-policy conflicts command to scan your network policy configuration and surface rules with overlapping classification criteria. A conflict occurs when two or more rules have the same source prefix, destination prefix, application, and network context, and the system cannot determine which rule applies to matching traffic. Unlike priority policy conflicts, network policy rules also consider user and user group scope, which can contribute to overlap when rules differ only on identity criteria. Run this command to pinpoint exactly which rules have overlapping criteria, which specific source and destination address pairs trigger the overlap, and which policy set and stack position each rule occupies. Use this information to resolve ambiguity by tightening match criteria, adjusting rule ordering, or separating overlapping rules into distinct policy sets. 

 Command 

 inspect network-policy conflicts 

 Options 

 None 

 When to Use 

 After adding or modifying network policy rules, before the changes go live, to confirm no new overlaps were introduced. 

 When traffic to a destination is receiving inconsistent handling and more than one rule could plausibly match the same flow. 

 When policies include user or user group scope, where address-range overlap can exist independently of identity criteria and is harder to catch without running this command. 

 Command Notes 

 Role Super, Read Only 

 Related Commands 

 inspect network-policy lookup 

 Introduced in Release 5.0.1 

 Example 

 The following example shows two conflicting network policy rules. For each rule, the output shows the overlapping source and destination address pairs and the conflicting rule: 

 inspect network-policy conflicts
Network Policy Rule : 1664343200310006628 : match icmp
 Policy Set : 1662009498094024828 : test user-id
 Stack Index | Order Number: 0 | 1024
 Source Prefix : 1658477619909015028 : Branch 1 Lan client
 Destination Prefix: none
 Users : UserGroups :
 : CN=engineering,DC=sdwanamsteltest,DC=onmicrosoft,DC=com :
 : CN=sales,DC=example,DC=onmicrosoft,DC=com :
 Application Id : 1658139887050014528 : icmp
 Network_Context Id: none
 Source : Destination : Conflicting Policy
 10.1.1.2/32 : 0.0.0.0/0 : 1664346696667006328 : match icmp duplicate

Network Policy Rule : 1664346696667006328 : match icmp duplicate
 Policy Set : 1662009498094024828 : test user-id
 Stack Index | Order Number: 0 | 1024
 Source Prefix : 1664346663085024328 : Branch 1 Lan client duplicate
 Destination Prefix: none
 Application Id : 1658139887050014528 : icmp
 Network_Context Id: none
 Source : Destination : Conflicting Policy
 10.1.1.2/32 : 0.0.0.0/0 : 1664343200310006628 : match icmp 

 Output Fields 

 Network Policy Rule: The numeric ID and name of the rule being evaluated. 

 Policy Set: The ID and name of the policy set the rule belongs to. 

 Stack Index | Order Number: The stack position and evaluation priority of the rule within the policy set. 

 Source Prefix / Destination Prefix: The traffic match criteria (prefix ID and name) defined in the rule, or none if unconfigured. 

 Users / UserGroups: The user or group identity scope of the rule. When present, these contribute to the conflict if the overlapping address pairs would otherwise match both rules. 

 Application Id: The application in the rule's scope. 

 Network_Context Id: The network context the rule applies to, or none if unconfigured. 

 Source / Destination / Conflicting Policy: The specific source and destination IP pairs that overlap, and the ID and name of the rule they conflict with. 

 Troubleshooting 

 Condition Possible Cause Action 

 Conflict reported between rules that belong to different policy sets Policy sets on the same stack can produce cross-set rule overlap Review stack ordering; separate conflicting rules into non-overlapping prefix ranges or distinct applications 

 Rules with Users or UserGroups fields show conflicts despite different identity scope Address overlap exists independent of identity; the device cannot distinguish flows by user identity alone at the prefix level Add more specific source or destination prefixes to separate the rules, rather than relying on identity scope to resolve the conflict 

 No conflicts reported but traffic is still routed unexpectedly This command only detects classification-criteria conflicts; rule ordering within the stack also determines which rule applies to a flow Use inspect network-policy lookup to trace which rule is actually applied to the affected flow 

 Previous 

 inspect memory summary 

 Next 

 inspect network-policy dropped 

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
