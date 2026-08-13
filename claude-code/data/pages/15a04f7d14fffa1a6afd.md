---
url: https://docs.paloaltonetworks.com/iot/administration/configure-iot-networks/network-segments-configuration/device-context-segments
fetched_at: 2026-08-13T16:36:14Z
source: palo-alto-main
---

# Device Context Segments Clear

Device Context Segments 

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

 Device Context Segments 

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

 Network Segments Configuration 

 Device Context Segments 

 Download PDF 

 Device Security 

 Device Context Segments 

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

 Network Segments Configuration 

 Next 

 Migrate to Device Context Segments 

 Device Context Segments 

 Learn about Panorama -managed device context segments and how they differ from
 Device Security -managed network segments.

 Where Can I Use This? What Do I Need? 

 Device Security (Managed by Strata Cloud Manager) 

 (Legacy) IoT Security (Standalone portal) 

 One of the following subscriptions: 

 Device Security subscription

 Precision AI bundle subscription

 Device Security X subscription

 To use device context segments, your firewalls must run
 PAN-OS 12.2 or later. You can create device context segments
 directly on a firewall. However, if you have firewalls in cluster mode, then
 you must manage their device context segments through Panorama .

 If you have multi-vsys firewalls or use Device-ID to enforce
 Security policies, you can create PAN-OS device context segments
 instead of Device Security network segments. Device context segments
 operate similarly to Device Security network segments,
 but let you assign both firewalls and virtual systems to them.
 EAL logs include device context segment identifiers to help Device Security 
 identify devices correctly based on the firewall and vsys the device traffic
 passes through. Device Security sends the device context segment identifier back
 to PAN-OS when delivering device context, so you can enforce
 Security policies on the correct device when your network uses shared IP address blocks.

 Device context segments in PAN-OS still appear in the Device Security 
 network segments table, and you can view their details in Device Security .
 You can't modify the firewall or vsys assignments or delete device context segments
 in Device Security , but you can choose to restrict device context sharing for
 those segments in Device Security .

 You can have both Device Security network segments and
 device context segments in your deployment, but a
 firewall can only be assigned to one segment, regardless of the type of segment.

 Compare Device Security -Managed and PAN-OS -Managed Segments 

 You can define network segments in Device Security or you can define
 device context segments in PAN-OS .

 Device Security network segments
 give you an application-native workflow with Device Security networks,
 device discovery, and third-party integrations. They are only aware of
 firewalls in your Device Security network, not including any virtual systems (vsys)
 on those firewalls. Device Security network segments aren't sent
 to PAN-OS when delivering device context to the Edge Service.

 PAN-OS device context segments give you firewall and vsys granularity that
 Device Security network segments cannot. Two vsys on the same firewall can belong
 to different segments. Device context segments include an identifier that
 Device Security receives from EAL, helping Device Security separate device context
 along the same boundaries you use for your network on multi-vsys firewalls.
 Device Security can send the segment identifier back to PAN-OS when delivering
 device context for Security policy enforcement.

 Each vsys can belong to only one device context segment. However, a 
 device context segment can be assigned to multiple vsys on the same firewall,
 or to multiple firewalls within the same tenant. If a vsys doesn't have a
 device context segment assigned, it belongs to the default segment. You must
 remove an existing device context segment assignment on a vsys before
 assigning a new segment. A firewall can support up to 1000 segments.

 Both segment types can coexist in the same tenant. The
 Panorama Managed Segment column in the
 Device Security Network Segments table identifies the source. Firewalls and
 virtual systems that are not explicitly assigned to a segment belong to the
 default segment, which Device Security creates and maintains automatically.

 You do not need PAN-OS device context segments to use
 Device Security network segments. Choose device context segments when you need
 vsys granularity for device identification or for
 Device-ID policy enforcement.

 To migrate your segments, see
 Migrate to Device Context Segments .

 Restrict Device Context Sharing 

 Each device context segment includes a
 Restrict Device Context Sharing setting that controls
 whether device context that Device Security learns outside of shared IP
 address blocks is shared with other segments. By default, the setting is off and
 Device Security sends non-shared IP address block device contexts to every segment
 so that firewalls in one segment can enforce Device-ID policy on devices first seen
 in another segment. When you enable Restrict Device Context Sharing on a segment,
 that segment doesn't send non-shared IP address block device context from its
 firewalls and vsys to other segments.

 From Device Security , enable the restriction setting on device context segments
 that correspond to distinct administrative or geographic boundaries where you want
 to keep device visibility contained. The restriction setting has no effect on
 devices in shared IP address blocks — those device contexts are always limited to
 the segment where the device was learned.

 Previous 

 Network Segments Configuration 

 Next 

 Migrate to Device Context Segments 

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
