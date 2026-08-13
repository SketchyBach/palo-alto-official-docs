---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/incidents-and-alerts/incidents-and-alerts
fetched_at: 2026-08-13T17:29:32Z
source: palo-alto-main
---

# Incidents and Alerts Clear

Incidents and Alerts 

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

 Incidents and Alerts 

 Updated on 

 Wed Feb 25 07:20:45 PST 2026 

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

 Wed Feb 25 07:20:45 PST 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Incidents and Alerts 

 Download PDF 

 Prisma SD-WAN 

 Incidents and Alerts 

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

 Understand Error Scenarios 

 Next 

 Monitor Incidents 

 Incidents and Alerts 

 Learn about the incidents and alerts managed in Prisma SD-WAN .
 Generate alerts and incidents when the system reaches system-defined or customer-defined
 thresholds or there is a fault in the system. 

 Where Can I Use This? What Do I Need? 

 Prisma SD-WAN (Managed by Strata Cloud Manager ) 

 Prisma SD-WAN 

 Prisma SD-WAN incidents are now available in Strata Cloud Manager Incidents . The Incidents page provides a consolidated view of incidents across
 all products, enhanced timeline visibility, and built-in notification capabilities. 

 Prisma SD-WAN generates alerts and incidents when the system
 reaches system-defined or customer-defined thresholds or there is a fault in the system.
 You will see the Overview tab that lists the
 Category -wise events that are
 Critical , Warning , or
 Informational in nature. It also displays the
 Incidents by Priority , Your Top
 Incidents , and Your Top Alerts . 

 Use the Incidents and Alerts to troubleshoot the system. 

 An alert may or may not be an indication of a fault in the network. An alert is raised
 when the system reaches system-defined or customer-defined thresholds. 

 An incident is an indication of a fault in the system. Incidents are raised and cleared
 and vary in severity: 

 Critical—Whole or part of a network is down and requires immediate action. 

 Warning—Impacts the network and needs immediate attention. 

 Informational—Network is degraded and needs attention soon. 

 Use the Settings tab to Setup Incident Policies to manage event code suppression based on the
 specified classifications and action attributes configured. You can use incident policy
 rules to suppress or escalate incidents that arise during a scheduled time period. In
 addition, you can also change the default priority of system generated incidents to a
 priority level that is more aligned with your business requirements. 

 Learn about the incidents and alerts generated in the Prisma SD-WAN system. 

 Filter Alerts and Incidents 

 Filter and sort alerts and incidents by various parameters so that you
 can take appropriate action on the events that require attention. Select the
 Filter widget on the
 Troubleshooting page to filter alerts and incidents. 

 Filter and sort alerts and incidents based on the following
 criteria: 

 Acknowledge indicates that you are aware of the incident but
 may not be taking any action at this time. You Acknowledge 
 only unresolved incidents. Acknowledging an incident enables you to display and
 focus on incidents that require attention. You can
 select one or more incidents (bulk acknowledge) for
 Acknowledge . 

 Unacknowledge indicates that you
 are aware of the incident but may not be taking any action at this time. You
 Unacknowledge only acknowledged incidents. You can select
 one or more incidents for Unacknowledge . 

 Filter By —Filter alerts and incidents by their status: 

 Show Resolved—Displays only resolved incidents when the fault causing
 the incident is removed. 

 Include Acknowledged—Displays acknowledged and unacknowledged
 incidents. 

 Show Only Acknowledged—Displays only acknowledged incidents. 

 Show Only Suppressed—Displays only suppressed incidents. 

 Include Suppressed—Displays suppressed and unsuppressed
 incidents. 

 Only incidents are filtered as acknowledged and suppressed. Only Acknowledged incidents are
 filtered and you can unacknowledge those incidents. 

 Sort By —Sort alerts and incidents by time or severity to display the
 latest alerts and incidents first. 

 Sites —Sort alerts and incidents by sites to display based on: 

 Site—Name or address search. 

 Viewing—Traffic volume, initiation failure, transaction failure. 

 Site type—Branch or data center. 

 Admin state of the site—Active, monitor or disabled. 

 Severity —Sort alerts and incidents based on the following severity
 categories: 

 Critical—Whole or part of a network is down and requires immediate
 action. 

 Warning—Impacts the network and needs immediate attention. 

 Informational—Degrades the network and needs attention soon. 

 Priority —Sort alerts and incidents based on the priority level: 

 Priority 1 (P1) 

 Priority P2 (P2) 

 Priority P3 (P3) 

 Priority P4 (P4) 

 Priority P5 (P5) 

 Category —Sort alerts and incidents based on the following
 options: 

 Network—Indicates network faults. 

 Device—Indicates device hardware, software, interface, or
 registration issues. 

 Cellular—Indicates cellular issues. 

 Application—Indicates application issues. 

 Policy—Indicates policy issues. 

 Branch HA—Indicates spoke HA issues. 

 Authentication—Indicates authentication failures. 

 User ID—Indicates User ID issues. 

 Code —Sort alerts and incidents based on the alert and incident event
 codes. 

 Time —Sort alerts by time to display the latest alerts and incidents
 first. 

 Correlation ID —Correlation ID is a system-generated ID for a raised
 incident. An incident is associated with raise and clear states. There can
 be multiple incidents with the same event code in either a raised or cleared
 state at any given time. Using the correlation ID, you may distinguish
 between incidents with the same event code. When an incident is cleared, the
 correlation ID indicates that the specific incident is cleared. This ID is
 always associated with an incident even if the incident is cleared or
 resolved. 

 Event Correlation of Incidents 

 The event engine performs multiple functions such as incident
 correlation, suppression, and escalation depending on the network conditions and the
 administrator configured event policy rules. This improves the operational
 efficiency of the app-fabric by automatically correlating incidents into an event
 and the comprehensive event framework control granted by setting the event
 policies. 

 The controller analyzes the incoming incidents from the ION devices to
 determine if they are related and then it aggregates the incidents into a single
 incident in real time. For example, if the controller receives multiple VPN down
 incidents, the controller analyzes the incident in real time, determines if they are
 related, and generates a single Secure Fabric Link incident for the event, while
 suppressing the original list of incidents. 

 Previous 

 Understand Error Scenarios 

 Next 

 Monitor Incidents 

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

 Incidents & Alerts 

 Prisma SASE 

 Prisma SD-WAN 

 Strata Cloud Manager 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
