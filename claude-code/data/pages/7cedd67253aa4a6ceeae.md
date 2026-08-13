---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/administration/prisma-sd-wan-stacked-policies/add-a-path-policy-rule
fetched_at: 2026-08-13T17:28:44Z
source: palo-alto-main
---

# Add a Path Policy Rule Clear

Add a Path Policy Rule 

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

 Add a Path Policy Rule 

 Updated on 

 Aug 10, 2026 

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

 Aug 10, 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Prisma SD-WAN Administrator’s Guide 

 Prisma SD-WAN Stacked Policies 

 Add a Path Policy Rule 

 Download PDF 

 Prisma SD-WAN 

 Add a Path Policy Rule 

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

 Add a Path Policy Set 

 Next 

 Configure User-ID based Policy Rules 

 Add a Path Policy Rule 

 Learn how to add a path policy rule in Prisma SD-WAN . 

 Where Can I Use
 This? What Do I
 Need? 

 Prisma SD-WAN (Managed by Strata Cloud Manager ) 

 Prisma SD-WAN 

 Path policy rules define network paths for application sessions to leverage. Path Policy Rules
 use network contexts, prefixes, ports, protocols, Application ID, User/Group ID, and
 Device ID. Layer 3 paths can be private or internet paths, VPN, or standard VPNs.
 You can directly add policy rules to a simple path stack by clicking a simple path
 stack and then clicking Add Rule . For advanced stacks, select
 a stack, then a policy set within the stack, and then add policy rules to the policy
 set. 

 Add a path policy rule to a simple path stack. 

 Select Configuration Prisma SD-WAN Policies Path Path Stacks Simple , select a Path and click Add
 Rule . 

 Select an order for the rule. 

 Policy rules follow explicit ordering and implicit ordering. In
 explicit ordering, each rule within a policy set has an order number
 that is used to explicitly order rules overriding an implicit order,
 a set of match criteria, and a set of actions. If two rules have the
 same order, then the rules follow implicit ordering wherein policy
 rules with more specific attributes get precedence over rules with
 less specific attributes. 

 In the Info tab, enter a
 Name for the policy rule, and
 optionally enter description and tags. 

 Enter an Order between 1-65535 for the
 policy rule. 

 An order of 1 indicates the highest priority for the
 policy rule. The default is 1024. 

 (Optional) Select Disable
 Rule if you do not want the ION device to
 consider this rule. 

 (Optional) Configure
network contexts. 

 On the Network Contexts screen,
select a previously configured Network Context or
click the + icon to create a network context. 

 (Optional) Configure
Prefixes. 

 On the Prefixes tab, select a Source
Prefix and a Destination Prefix . 

 (Optional) Add Device Profile. 
 On the Devices tab, select a
 Source and/or Destination Device
 Profile in the drop-down. 

 (Optional) Add users or user groups . 
 On the Users tab, select a
 User and/or a Group 
 from the User/Group drop-down. 

 (Optional) Select applications. 

 On the Apps tab, select the applications
to apply the policy rule. You can select 256 applications for one
policy rule. 

 You can filter applications based on: 

 For sites 6.4.1 or above—Select this option
 to view applications supported for device version 6.4.1 and
 above. 

 For sites above 6.0.1 and less than 6.4.1—Select this option
 to view system applications supported between releases 6.0.1
 and pre-6.4.1. 

 For sites below 6.0.1—Select this option to view applications supported for devices versions
 below 6.0.1. 

 For any site—Use this option to view applications supported for all device versions. 

 (Optional) You can check the type of application - System or
 Custom by selecting the application first
 and then using the filters to view the type of application. 

 Configure paths. 

 On the Paths tab, choose
 Active/Backup/L3 Failure Paths for the
 application from the drop-down list. 

 Select an Overlay and a
 Circuit Category for a path. You cannot
 repeat a combination of an overlay and a circuit category for a
 policy rule. The choices for the Overlay are - Direct, Prisma SD-WAN
 VPN and Standard VPN. 

 You must configure an active path. You can optionally configure
 backup paths and L3 failure paths . You
 can configure an L3 failure path without configuring a backup
 path. 

 The Backup Path activates when the primary path is poor or
 unavailable—but the L3 Failure Path is reserved as the ultimate
 emergency route, only triggered by a complete loss of Layer 3
 reachability across all links. 

 In ION devices running 5.2.1 and higher versions, the default setting
 moves flows back to the active path in the policy as soon as the
 active path becomes available. 

 Configure paths. 

 On the Paths tab, choose either SLA
 Compliant Path or Best Path
 Selection . 

 SLA Compliant Path 
 Choose a path based
 on performance metrics defined in the policy rule to meet
 SLAs . Select
 Active ,
 Backup , and
 L3Failure paths for the
 application, an Overlay (Direct,
 Prisma SD-WAN VPN or Standard VPN) and the
 Circuit Category for a pathYou
 can utilize metrics for: 

 Link Quality: Latency, Loss, Jitter, and MOS. 

 Probe: ICMP (latency, loss, jitter), DNS (transaction
 time, failure rate), and HTTP/S (transaction time,
 failure rate), depending on your probe
 configuration. 

 App Metrics: TCP (Init Failure and RTT) and TRT for
 UDP. 

 All metrics can be used simultaneously, however, you
 cannot repeat a combination of an overlay and a circuit
 category for a policy rule. You must configure an active
 path and can optionally configure backup and L3 failure
 paths. Active Paths will be used first and load shared as
 long as they are SLA compliant. If no Active Paths are SLA
 compliant then any backup paths will be used. If all Active
 and Backup paths are completely down (not degraded) the L3
 Failure Paths will be used. 

 In ION devices running 5.2.1 and higher versions, the
 default setting moves back to the active path in the policy as
 soon as the active path becomes available. 

 Best Path Policy 
 Choose either an
 LQM based or Probe based
 best path selection. It selects the path with the absolute
 lowest metric specified in the path policy rule, using
 Active paths primarily and
 L3 Failure paths only if all
 active paths are down. 

 LQM : Select the best path based
 on a single metric (latency, loss, or jitter), focusing
 on the lowest value of the specified metric while
 disregarding available bandwidth. 

 Probe : Select ICMP (latency,
 loss, jitter), DNS (transaction time, failure rate), and
 HTTP/S (transaction time, failure rate), depending on
 your probe configuration. 

 Only one metric can be used per policy
 rule. Load sharing for this traffic class will not be performed when
 using best path selection. 

 Select Service and DC Groups. 

 Select Service & DC
Groups , and then select Active/Backup Service & DC Groups
from the drop-down. 

 If the Required check box
is selected, traffic will always transit through the Service and
DC Groups. If not selected, traffic may or may not transit through
the Service and DC Groups per policy. You cannot select Required ,
if you have selected at least one direct path in the Paths tab. 

 Confirm the information displayed in the Summary tab
and then click Save & Exit . 

 Add a path policy rule to an advanced path policy set. 

 Select Configuration Prisma SD-WAN Policies Path Path Stacks Advanced Select a Stack Add Rule . 

 Follow the steps above for adding
a path policy rule to a simple policy stack. 

 Previous 

 Add a Path Policy Set 

 Next 

 Configure User-ID based Policy Rules 

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
