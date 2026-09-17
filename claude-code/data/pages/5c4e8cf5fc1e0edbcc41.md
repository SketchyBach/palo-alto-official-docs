---
url: https://docs.paloaltonetworks.com/iot/iot-security-integration/ip-address-management/integrate-iot-security-with-infoblox-ipam
fetched_at: 2026-09-16T12:58:35Z
source: palo-alto-main
---

# Integrate Device Security with Infoblox IPAM
     Clear

Updated on 

 Mon Aug 17 11:22:37 PDT 2026 

 Focus 

 Home 

 Device Security 

 Device Security Integration Guide 

 IP Address Management 

 Integrate Device Security with Infoblox IPAM

 Download PDF 

 Device Security 

 Integrate Device Security with Infoblox IPAM

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Device Security Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Enterprise Administration 

 Integrations 

 Release Notes 

 Best Practice 

 New Features 

 Previous 

 Set up Device Security and XSOAR for BlueCat Integration 

 Next 

 Set up Infoblox for Integration 

 Integrate Device Security with Infoblox IPAM

 Integrate Device Security through Cortex XSOAR with Infoblox to import and
 maintain IPAM data in real time or on a schedule.

 Where Can I Use This? What Do I Need? 

 Device Security (Managed by Strata Cloud Manager) 

 (Legacy) IoT Security (Standalone portal) 

 One of the following subscriptions: 

 Device Security subscription

 Precision AI bundle subscription

 Device Security X subscription

 One of the following Cortex XSOAR setups:

 A free, cohosted, limited-featured
 Cortex XSOAR instance

 AND 

 A free Cortex XSOAR Engine (on-premises integration)

 A full-featured Cortex XSOAR server

 Infoblox Internet Protocol Address Management (IPAM) provides a means for managing
 the IP address space of a network. When you integrate Device Security through
 Cortex XSOAR with Infoblox IPAM, you can import all the IP address blocks and
 subnets (called containers and networks in Infoblox) into
 Device Security and then display them on the Networks page.
 You can also specify subnet scopes to limit the IP CIDR blocks and subnets retrieved
 from Infoblox. 

 Device Security supports two methods of integrating with Infoblox:

 A direct integration, which is useful for bulk ingestion of data and for
 configuring a recurring schedule for the integration jobs.

 An integration with the Infoblox Outbound API, which is useful for real-time
 synchronization between Infoblox networks and Device Security networks.

 The two integration modes are complementary. Use the bulk read integration for the
 initial synchronization and as a safety net; enable the Outbound API for near
 real-time updates.

 Through integration with Infoblox, Device Security can learn the following types
 of information about the IP address blocks and subnets on the network:

 Prefix (for example, 10.1.0.0/16) 

 Type : Block or
 Subnet 

 Description (if configured on Infoblox) 

 Site (if configured on Infoblox) 

 VLAN (subnets only) 

 For a full list of attributes that Device Security can learn through the
 integration, see
 Infoblox Attribute Reference .

 Integrating with Infoblox requires either a full-featured Cortex XSOAR™ server 
 or the activation of a Device Security free
 cohosted Cortex XSOAR instance .

 Previous 

 Set up Device Security and XSOAR for BlueCat Integration 

 Next 

 Set up Infoblox for Integration
