---
url: https://docs.paloaltonetworks.com/iot/administration/saas-agent-security-support-table
fetched_at: 2026-08-13T16:36:30Z
source: palo-alto-main
---

# Configure IoT Networks Clear

Configure IoT Networks 

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

 Configure IoT Networks 

 Updated on 

 Thu Jul 30 16:42:12 PDT 2026 

 Focus 

 Download PDF 

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

 Updated on 

 Thu Jul 30 16:42:12 PDT 2026 

 Focus 

 Home 

 Device Security 

 Device Security Administration Guide 

 Configure IoT Networks 

 Download PDF 

 Device Security 

 Configure IoT Networks 

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

 Vertical-themed Portals 

 Next 

 Device-to-Site Mapping 

 Configure IoT Networks 

 Learn how Device Security displays network structure and how you can configure
 your network for Device Security .

 Where Can I Use This? What Do I Need? 

 Device Security (Managed by Strata Cloud Manager) 

 (Legacy) IoT Security (Standalone portal) 

 One of the following subscriptions: 

 Device Security subscription

 Precision AI bundle subscription

 Device Security X subscription

 Device Security combines networks and sites to create a comprehensive model of your
 organization's network topology. This integrated approach enhances device discovery,
 classification, and risk assessment capabilities.

 Networks 
 form the foundation, representing logical groupings of IP subnets that align
 with your network infrastructure. Device Security learns about your networks by
 observing firewall traffic, IPAM integrations, SNMP crawls, and manual user subnet
 upload. Device Security also creates CIDR blocks where appropriate based on
 discovered subnets. You can define network segments 
 within these networks to further refine device organization and policy application when
 different sites use overlapping IP addresses. This granular approach allows you to group
 devices with similar functions or security requirements, enabling more precise control
 over your IoT environment.

 Sites 
 overlay your network architecture, representing physical locations or logical
 groupings of your infrastructure. The site hierarchy facilitates efficient multi-site
 management and location-specific policy implementation. You can create parent sites for
 larger entities like countries or regions, and child sites for specific locations such
 as individual offices or campuses. This structure mirrors your organization's layout,
 making it easier to manage devices across diverse geographical or organizational
 boundaries.

 By integrating networks and sites, Device Security develops an understanding of your
 network topology. This comprehensive view enables more accurate device discovery, as the
 system can identify devices in context of their network and site location. It also
 facilitates precise classification, taking into account the device's network segment and
 site-specific characteristics.

 Device Security automatically maps discovered devices to sites based on their network
 location. This automatic mapping streamlines device management and ensures that security
 policies consider both network segmentation and physical or logical location.
 Device Security can evaluate device risks by assessing factors such as network
 exposure, site-specific threats, and the device's role within its segment. This
 contextual risk assessment allows you to prioritize security measures more effectively.

 Furthermore, this integrated model allows for targeted policy enforcement. Using
 Device-ID , you can apply
 security policies based on a combination of network, segment, and site parameters,
 ensuring that devices receive appropriate protections regardless of their location or
 network position.

 The flexibility of this approach accommodates various network architectures and
 organizational structures. Whether you manage a single office or a global enterprise
 with multiple sites and complex network segmentation, Device Security adapts to and
 helps secure your specific topology.

 Previous 

 Vertical-themed Portals 

 Next 

 Device-to-Site Mapping 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Activate a License or Product 

 Cloud Identity Engine 

 Strata Logging Service 

 Device Associations 

 Hub 

 Identity and Access Management 

 Tenant Management 

 Next-Generation Firewalls 

 AIOps for NGFW 

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 Service Provider 

 VM-Series 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 Device Security 

 Administration 

 Cloud-Delivered Security Services 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
