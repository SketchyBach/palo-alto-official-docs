---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/administration/get-started-with-prisma-sd-wan/prisma-sd-wan-command-center-dashboard
fetched_at: 2026-09-16T07:47:31Z
source: strata-and-sase
---

# Prisma SD-WAN Command Center Dashboard Clear

Updated on 

 Mon Aug 24 08:54:44 PDT 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Prisma SD-WAN Administrator’s Guide 

 Get Started with Prisma SD-WAN 

 Prisma SD-WAN Command Center Dashboard 

 Download PDF 

 Prisma SD-WAN 

 Prisma SD-WAN Command Center Dashboard 

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

 Prisma SD-WAN Link Quality Dashboard 

 Next 

 Prisma SD-WAN Subscription Usage 

 Prisma SD-WAN Command Center Dashboard 

 Learn how to understand the Prisma SD-WAN Command Center dashboard. 

 Where Can I Use This? What Do I Need? 

 Prisma SD-WAN (Managed by Strata Cloud Manager ) 

 Strata Cloud Manager 

 Prisma SD-WAN 

 Strata Logging Service 

 Strata Cloud Manager Pro 

 The Command Center is a unified dashboard in Strata Cloud Manager that
 integrates network health, security, and efficiency data from various Palo Alto Networks
 products. This feature extends visibility to your SASE and standalone Prisma SD-WAN
 deployments. This provides a single pane of glass to monitor overall health, security
 posture, and traffic patterns across your entire network ecosystem. This functionality
 relies on a centralized logging infrastructure. Data from your Prisma SD-WAN deployments
 and other Palo Alto Networks products is sent to the Strata Logging Service, and the
 Command Center queries this aggregated data to construct its visualizations. 

 The Command Center dashboard helps by providing: 

 Unified Network Visibility – Gain a comprehensive view of network
 health, security, and efficiency across your SASE and standalone Prisma SD-WAN
 deployments. 

 Enhanced Threat Monitoring – Consolidate SD-WAN security events
 into a single, aggregated threat dashboard for quicker detection and response. 

 Actionable Insights – Classify hosts (Users, IoT, Unclassified) and
 applications (Internet, SaaS, Private) to understand traffic patterns and security
 posture. 

 Streamlined Operations – Quickly identify and differentiate between
 Prisma SD-WAN sites and other network traffic for targeted management. 

 The dashboard displays sources, platforms, and applications data: 

 Sources — Entities initiating network traffic. These identify
 endpoint types: 

 IoT Devices 

 Users 

 Unclassified Hosts 

 Platforms — Network infrastructure components through which
 traffic traverses. These show which Palo Alto Networks products process your
 traffic: 

 NGFW 

 Prisma Access 

 Prisma SD-WAN (represented as Direct Access and Secure Direct
 Access) 

 Direct Access — Represents Prisma SD-WAN branches lacking an active
 Branch Security license or any configured security policies. 

 Secure Direct Access — Represents Prisma SD-WAN branches
 with an active Branch Security license and at least one configured
 security policy. 
 For the Command Center to display
 'Secure Direct Access' information, Prisma SD-WAN branches must
 have an active Branch Security license and configured security
 policies. 

 Applications — The ultimate destinations or services
 accessed by your traffic. These categorize application types: 

 Internet Apps 

 SaaS Apps 

 Private Apps 

 For more information on Command Center, refer to the Strata Cloud Manager Command Center . 

 Previous 

 Prisma SD-WAN Link Quality Dashboard 

 Next 

 Prisma SD-WAN Subscription Usage
