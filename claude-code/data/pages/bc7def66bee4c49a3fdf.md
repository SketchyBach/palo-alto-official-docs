---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/release-notes/prisma-access-cloudblade-cloud-managed-release-notes/prisma-access-cloudblade-integration-release-3-1-5
fetched_at: 2026-09-16T07:48:59Z
source: strata-and-sase
---

# Prisma Access CloudBlade Integration Release 3.1.5 Clear

Updated on 

 Tue Apr 08 09:55:56 PDT 2025 

 Focus 

 Home 

 Prisma SD-WAN 

 Prisma Access CloudBlade Integration Release 3.1.5 

 Download PDF 

 Prisma SD-WAN 

 Prisma Access CloudBlade Integration Release 3.1.5 

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

 Prisma Access CloudBlade Integration Release 3.1.6 

 Next 

 Prisma Access CloudBlade Integration Release 3.1.1 

 Prisma Access CloudBlade Integration Release 3.1.5 

 Learn about the Prisma Access CloudBlade Integration release 3.1 5 release
 information. 

 This document contains the Prisma Access for Networks (Cloud managed) CloudBlade,
 version 3.1.5 release notes. 

 Features Introduced in Prisma Access CloudBlade 3.1.5 

 The new features introduced in Prisma Access CloudBlade version 3.1.5
 are: 

 Configure Quality of Service (QoS) in Prisma Access 
 (Cloud managed) for aggregate bandwidth, including
 creating a QoS profile, editing a QoS profile, and
 tagging the QoS profile on the Prisma SD-WAN web interface. 

 Prisma Access deployment can be managed
 by both Panorama and
 Cloud
 Management interfaces. Prisma Access allows
 Panorama to Cloud
 Management migration where existing
 customers can use the in-product workflow to migrate
 their Prisma Access configuration. 

 When a new license is purchased which has both Prisma Access and Prisma SD-WAN for
 a specific tenant, a TSG ID is generated
 automatically as part of the license. The Prisma Access CloudBlade integrates the Prisma SD-WAN tenant with the Prisma Access tenant under the same TSG ID. 

 Limitations and Caveats in Release 3.1.5 

 The following caveat is applicable for Release 3.1.5: 

 When migrating from CloudBlade version 3.1.1 to version
 3.1.5 in Non-Aggregate Licensing mode in Prisma Access , tunnels may be rebuilt on sites
 that use ECMP tagging. The 3.1.5 CloudBlade version
 now considers all available ports for tunnel
 formation, rather than just the tagged ones. In such
 scenarios, you could experience some downtime for
 such sites. It is recommended to enable the dry
 run option to identify possible changes during
 migration to 3.1.5. 

 Previous 

 Prisma Access CloudBlade Integration Release 3.1.6 

 Next 

 Prisma Access CloudBlade Integration Release 3.1.1
