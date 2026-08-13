---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/administration/performance-policy-with-forward-error-correction-fec/add-performance-policy-rules/move-flows
fetched_at: 2026-08-13T17:27:35Z
source: palo-alto-main
---

# Move Flows Clear

Move Flows 

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

 Move Flows 

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

 Prisma SD-WAN Performance Policy 

 Add Performance Policy Rules 

 Move Flows 

 Download PDF 

 Prisma SD-WAN 

 Move Flows 

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

 Add Performance Policy Rules 

 Next 

 Configure App Acceleration 

 Move Flows 

 Learn about the Move Flows SLA action which provides traffic management to maintain
 application performance and enforces SLAs. 

 Where Can I Use This? What Do I Need? 

 Prisma SD-WAN (Managed by Strata Cloud Manager ) 

 Prisma SD-WAN 

 Physical and virtual ION devices running software version 6.3.1
 and higher 

 Prisma SD-WAN measures application performance and enforces Application SLAs
 (Service Level Agreements) through the Performance policy framework. Using link quality
 metrics such as Latency, Loss, and Jitter, and application metrics like Application RTT
 and Init Failure percentage, Prisma SD-WAN adjusts traffic paths to meet SLA
 requirements. 

 The Move Flows action provides traffic
 management to maintain application performance and enforce SLAs . Previously, this action excluded
 SLA-violating paths for new flows, preserved existing flows, and used Link Quality Metrics and Application Metrics unless the field
 was empty, in which case link quality metrics were ignored. The functionality now offers
 greater flexibility with two modes: 
 Move Flows Graceful moves existing flows while excluding
 new flows from using paths that violate SLAs. If Move Flows is empty, the
 system ignores Link Quality Metrics during path selection. With Application
 Performance SLAs, the system redirects only new flows to a better path after a
 performance issue, keeping existing flows on their current path for up to 10
 minutes. In contrast, with LQM SLAs, the system moves both new and existing
 flows to an optimal path when performance degrades. It always maintains
 Application Path Affinity and detects performance issues within one minute, with
 probes improving accuracy in path adjustments. 

 Move Flows Forced ensures that existing flows shift from
 a nonperforming path to a better-performing path, regardless of any NAT boundary
 violation. However, if no better path is available, the NAT boundary is
 violated, and the best available path is selected to move the flows. This
 includes both Link Quality metrics and Application /Probe metrics. 

 The Move Flows Forced action supports path types such as Private
 Layer 2, Direct (Public and Private), SD-WAN VPNs (Public and Private), and Third-Party
 VPNs (Public and Private). It is triggered by the following events and their respective causes: 

 Layer 3 Unreachability Event : when the underlay for a path can't consistently
 reach the internet. 

 LQM (Link Quality Metrics) SLA Violation Event : when link quality metrics
 (latency, jitter, and packet loss) for a path, as measured by system LQM probes,
 fail to meet the default or user-defined path SLAs. 

 App Unreachable Event : when an application on a path, targeting a specific
 destination prefix and port, becomes unreachable. 

 Synthetic Probe SLA Violation Event : when link quality metrics (latency,
 jitter, packet loss, RTT, initialization failure, and DNS-TRT) for a path, based on
 user-defined probes, fail to meet the default or user-defined path SLAs. 

 Service Link Up or Down Event : when an IPSec or GRE tunnel to a third-party
 service goes down or comes back up. 

 Flow Revalidation Event : when a flow is reevaluated after the active path in
 the respective path group becomes reachable. 

 DC Core Reachability with Host Tracking : when the data center core peer goes
 down, or a specific prefix becomes unreachable from the data center. 

 The table outlines the expected behavior of the Move Flows Forced action
 across various network path scenarios. It supports combinations of active and backup
 paths, including Direct Internet , Direct Private , Public and Private
 VPN , Standard VPN , and enterprise VPN configurations. In all cases, the
 system applies the Move Flows Forced action, monitoring path
 performance using LQM and Probes as SLA criteria. It enables expected behavior for
 traffic types like TCP/ICMP/UDP on the internet while enterprise VPN paths provide
 enhanced traffic handling capabilities. 

 Active Path Backup Path Action SLA Criteria Expected Behavior App: Internet 

 Direct internet Direct internet Move Flows Forced LQM, Probes Allowed TCP/ICMP/UDP 

 Direct Private Direct Private Move Flows Forced LQM, Probes Allowed TCP/ICMP/UDP 

 Direct Public and Private Public and Private VPN Move Flows Forced LQM, Probes Allowed TCP/ICMP/UDP 

 Direct Public Standard VPN Move Flows Forced LQM, Probes Allowed TCP/ICMP/UDP 

 Standard VPN to SEP1 Standard VPN to SEP1 Move Flows Forced LQM, Probes Allowed TCP/ICMP/UDP 

 Standard VPN to SEP1 Standard VPN to SEP2 Move Flows Forced LQM, Probes Allowed TCP/ICMP/UDP 

 Standard VPN VPN Move Flows Forced LQM, Probes Allowed TCP/ICMP/UDP + Enterprise 

 VPN1 to DC1 VPN1 to DC2 Move Flows Forced LQM, Probes Allowed TCP/ICMP/UDP + Enterprise 

 VPN1 to DC1 VPN2 to DC2 Move Flows Forced LQM, Probes Allowed TCP/ICMP/UDP + Enterprise 

 The Flow Decision Data indicates whether a
 flow was forcefully moved due to any of the above events. 

 Related CLIs 

 debug performance policy 

 inspect performance policy fec
 status 

 inspect performance policy hits
 analytics 

 inspect performance policy
 incidents 

 inspect performance policy lookup 

 dump performance policy config policy
 rules 

 dump performance policy config policy
 sets 

 dump performance policy config policy set
 stacks 

 dump performance policy config threshold
 profile 

 Previous 

 Add Performance Policy Rules 

 Next 

 Configure App Acceleration 

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
