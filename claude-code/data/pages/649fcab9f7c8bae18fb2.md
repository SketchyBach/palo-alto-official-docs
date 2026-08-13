---
url: https://docs.paloaltonetworks.com/iot/administration/configure-iot-networks/network-segments-configuration
fetched_at: 2026-08-13T16:36:14Z
source: palo-alto-main
---

# Network Segments Configuration Clear

Network Segments Configuration 

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

 Network Segments Configuration 

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

 Download PDF 

 Device Security 

 Network Segments Configuration 

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

 Subnet-Site Mapping 

 Next 

 Device Context Segments 

 Network Segments Configuration 

 Device Security uses network segments to identify unique devices that use a shared
 IP address block, and to scope device context to the firewalls and virtual systems
 that belong to each segment.

 Where Can I Use This? What Do I Need? 

 Device Security (Managed by Strata Cloud Manager) 

 (Legacy) IoT Security (Standalone portal) 

 One of the following subscriptions: 

 Device Security subscription

 Precision AI bundle subscription

 Device Security X subscription

 Device Security uses network segments to identify devices with
 overlapping IP addresses.
 If you are using Device Security in Strata Cloud Manager , log in as a user with the
 Superuser role, and select Networks Network Segments . If you are using the Device Security portal, log in as a user with
 owner or administrator privileges, and select Networks Networks and Sites Network Segments Configuration . There you can add, view, edit, and delete network segments used for
 identifying
 devices with overlapping IP addresses .
 Network segments rely on IP address-based site assignment to be effective. While you can
 manage network segments when using firewall-based site assignment, they won't have any
 effect.

 There are two sections on the Network Segments Configuration page. 

 At the top is a title bar, with titles for Networks, Network Segments
 Configuration, and Sites tabs. There is a global filter that controls the
 content displayed on the page by site, and the option to filter or query the
 content displayed on the page by firewall.

 The Segments section is a table with information about individual network segments.

 Start with
 Create and Manage Network Segments and
 Reset and Delete Network Segments to learn
 how to work with Device Security -managed segments in the portal. If your
 deployment also uses multi-vsys firewalls and Device-ID , review the sections
 below to compare Device Security network segments and
 PAN-OS device context segments and to plan any migration between the two.

 If you have multi-vsys firewalls or use Device-ID to enforce
 Security policies, you should create PAN-OS device context segments 
 instead of Device Security network segments. Device context segments
 operate similarly to Device Security network segments,
 but let you assign both firewalls and virtual systems to them.
 EAL logs include device context segment identifiers to help Device Security 
 identify devices correctly based on the firewall and vsys the device traffic
 passes through. Device Security sends the device context segment identifier back
 to PAN-OS when delivering device context, so you can enforce
 Security policies on the correct device when your network uses shared IP address blocks.

 Create and Manage Network Segments 

 When creating a new network segment, enter a name and one or more firewalls to
 assign to the network segment. A network segment can have multiple firewalls
 assigned to it, but each firewall can only be assigned to one network segment. If
 you enter a firewall that is already assigned to a different network segment, the
 old assignment will be removed when you save the new network segment.

 Optionally, enter a description and a site assignment for the network segment. A
 network segment can be assigned to only one site at a time. If no site is specified,
 the network segment is assigned to the default site.

 To edit an existing network segment, find the network segment in the Segments table
 and click on the name to bring up the edit dialog.

 You can create and edit network segments in Device Security only for segments
 that Device Security manages. Panorama-managed segments appear in the Segments
 table in read-only mode. To create, edit, or reassign firewalls and virtual systems
 for a Panorama-managed segment, use Panorama.

 Reset and Delete Network Segments 

 When you reset or delete a network segment, all devices and attributes learned
 through the network segment assignment are deleted from the assets inventory.

 If you update the firewalls or the sites for a network segment, reset the network
 segment. Resetting the network segment ensures that traffic is properly mapped to
 the right device and avoids potential duplication or overriding of device
 attributes. In the Segments table, select the check boxes next to the network
 segments to reset, and then click Reset .

 Delete network segments that you no longer need to avoid misidentification of
 devices and device attributes. In the Segments table, select the network segments to
 delete, and then click Delete . The network segment no longer
 appears in the Segments table.

 Reset and delete actions in Device Security apply to Device Security -managed
 segments. To reset or delete a Panorama-managed segment, remove the firewall or
 virtual system assignments in Panorama or delete the segment definition in Panorama,
 then push the configuration to the managed firewalls.

 Previous 

 Subnet-Site Mapping 

 Next 

 Device Context Segments 

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
