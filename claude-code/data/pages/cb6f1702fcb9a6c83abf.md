---
url: https://docs.paloaltonetworks.com/iot/integration/network-management/integrate-iot-security-with-solarwinds-platform.html
fetched_at: 2026-09-16T11:15:10Z
source: palo-alto-main
---

# Integrate Device Security with SolarWinds Platform Clear

Updated on 

 Mon Aug 17 11:22:37 PDT 2026 

 Focus 

 Home 

 Device Security 

 Device Security Integration Guide 

 Network Management 

 Integrate Device Security with SolarWinds Platform 

 Download PDF 

 Device Security 

 Integrate Device Security with SolarWinds Platform 

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

 Set up Device Security and Cortex XSOAR for Palo Alto Networks PAN-OS Integration 

 Next 

 Set up SolarWinds Platform for Integration 

 Integrate Device Security with SolarWinds Platform 

 Integrate Device Security with SolarWinds Platform to gain network 
 subnet information and track physical locations of IoT/OT devices.

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

 Integrate Device Security with SolarWinds Platform (previously 
 SolarWinds Orion modules) to gain network subnet information and track 
 physical locations of IoT/OT devices. This integration addresses challenges in 
 understanding device network connections and automating IP subnet definition 
 imports, thereby providing crucial context for device identification, network 
 management, and security.

 Device Security built and verified this integration with the legacy 
 SolarWinds Orion modules. SolarWinds now hosts 
 SolarWinds Orion modules on SolarWinds Platform .

 Device Security takes advantage of the IP Address Management (IPAM) and User 
 Device Tracking (UDT) capabilities of SolarWinds . When configuring the 
 integration, the SolarWinds solution you choose affects what 
 Device Security learns from the integration.

 SolarWinds Platform IPAM solution : subnet 
 configurations, VLAN identifiers, and descriptions from your SolarWinds 
 infrastructure. The information learned from the IPAM solution lets you reuse 
 the SolarWinds subnet definitions in Device Security .

 SolarWinds Platform UDT solution : individual 
 device details and their specific switch and port connection, such as switch 
 names, port numbers, VLAN assignments, and wireless access point information. 
 The information learned from the UDT solution gives more context when assessing 
 network security.

 If you already have SolarWinds Platform , integrating with Device Security 
 provides operational benefits by enabling location-based device grouping, supporting 
 queries based on physical network placement, and triggering alerts when devices 
 change network locations. You get better visibility into device movement patterns 
 and can quickly identify devices that relocate between switches or ports. This 
 visibility helps with enterprise security monitoring, compliance tracking, and 
 operational troubleshooting in complex environments.

 For a full list of attributes that Device Security can learn through the
 integration, see
 SolarWinds UDT Attribute Reference .

 Integrating with SolarWinds requires either a 
 full-featured Cortex XSOAR server or 
 the 
 activation of a Device Security free 
 cohosted Cortex XSOAR instance .

 Previous 

 Set up Device Security and Cortex XSOAR for Palo Alto Networks PAN-OS Integration 

 Next 

 Set up SolarWinds Platform for Integration
