---
url: https://docs.paloaltonetworks.com/pan-os/u-v/routing-engine-migration-reference/routing-protocol-migration-exceptions/ospfv3
fetched_at: 2026-08-13T17:17:25Z
source: palo-alto-main
---

# OSPFv3 Clear

OSPFv3 

 Home 

 EN

 Location 

 Documentation Home 

 Palo Alto Networks 

 Support 

 Live Community 

 Knowledge Base 

 Strata Copilot

 Advanced Routing Engine Migration Reference 

 : 
 OSPFv3 

 Updated on 

 Mon Jan 26 20:40:12 PST 2026 

 Focus 

 Download PDF 

 Filter

 Expand all | Collapse all 

 Get Started with Routing Engine Migration 

 Plan Your Routing Engine Migration 

 Learn the Differences Between Legacy and Advanced Routing Engine 

 Routing Protocol Migration Exceptions 

 MP-BGP 

 OSPF 

 OSPFv3 

 PIM 

 IGMP 

 Updated on 

 Mon Jan 26 20:40:12 PST 2026 

 Focus 

 Home 

 PAN-OS 

 Advanced Routing Engine Migration Reference 

 Routing Protocol Migration Exceptions 

 OSPFv3 

 Download PDF 

 Advanced Routing Engine Migration Reference 

 OSPFv3 

 Table of Contents 

 Filter

 Expand all | Collapse all 

 Get Started with Routing Engine Migration 

 Plan Your Routing Engine Migration 

 Learn the Differences Between Legacy and Advanced Routing Engine 

 Routing Protocol Migration Exceptions 

 MP-BGP 

 OSPF 

 OSPFv3 

 PIM 

 IGMP 

 OSPFv3 

 OSPFv3 routing protocol configuration parameter differences
between legacy and advanced routing engine. 

 There are parameter setting differences between legacy and advanced routing engines when
 configuring OSPFv3 settings. 

 Route Redistribution 

 OSPFv3 handles route redistribution to another routing protocol differently in the legacy and
 advanced routing engines. When redistributing from OSPFv3, filters are based on a
 variety of criteria. 

 Migration Exception: The advanced routing engine does not allow redistribution of
 routes based on Link State Advertisement (LSA) type (external-1, external-2,
 inter-area, or intra-area) or origin area. You can, however, use prefixes and tags
 associated with LSA updates. 

 CONFIGURED IN (LEGACY ROUTING ENGINE) 

 LEGACY ROUTING ENGINE 

 MIGRATED TO (ADVANCED ROUTING ENGINE) 

 ADVANCED ROUTING ENGINE 

 Network Virtual Router OSPFv3 Export Rules 

 Supports redistribution of routes that match the following criteria : 

 Interface 

 Address 

 Next Hop 

 Path Type 

 Area 

 Tag 

 Network Routing Routing Profiles OSPFv3 OSPFv3 Redistribution Profile 

 Supports Redistribute Route-Map that Match the
 following criteria : 

 Interface 

 Address (using Prefix List or Access List ) 

 Next Hop (using Prefix List or Access List ) 

 Metric 

 Tag 

 Authentication Profile 

 Migration Exception: In the advanced routing engine, the authentication profile
 variables are retained globally for reuse which can cause an issue with the Security
 Policy Index (SPI). The advanced routing engine does not allow multiple interface
 authentication profiles within a single virtual system (vsys) to share the same SPI
 value. 

 CONFIGURED IN (LEGACY ROUTING ENGINE) 

 LEGACY ROUTING ENGINE 

 MIGRATED TO (ADVANCED ROUTING ENGINE) 

 ADVANCED ROUTING ENGINE 

 Network Virtual Router OSPFv3 Auth Profiles 

 Maintains the authentication profile variables within
the context of virtual routers. 

 Network Routing Routing Profiles OSPFv3 OSPFv3 Interface Auth Profile 

 Retains the authentication profile 
 variables globally for reuse. 

 Previous 

 OSPF 

 Next 

 PIM 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
