---
url: https://docs.paloaltonetworks.com/panorama/administration/manage-firewalls/manage-device-groups/add-a-device-group
fetched_at: 2026-08-13T17:17:39Z
source: palo-alto-main
---

# Add a Device Group Clear

Add a Device Group 

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

 Add a Device Group 

 Updated on 

 Thu Jul 30 16:22:01 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Panorama Docs 

 Getting Started 

 Administration 

 New Features 

 Updated on 

 Thu Jul 30 16:22:01 PDT 2026 

 Focus 

 Home 

 Panorama 

 Manage Firewalls with Panorama 

 Manage Device Groups 

 Add a Device Group 

 Download PDF 

 Panorama 

 Add a Device Group 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Panorama Docs 

 Getting Started 

 Administration 

 New Features 

 Previous 

 Manage Device Groups 

 Next 

 Move a Firewall to a Different Device Group 

 Add a Device Group 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by Panorama) 

 Device Management License 

 Panorama administrator or device group administrator
 role 

 After adding firewalls (see Add a Firewall as a Managed Device ), you can group them
 into device groups (up to 1,024), as follows.
 Be sure to assign both firewalls in an active-passive high availability (HA)
 configuration to the same device group so that Panorama will push the same policy
 rules and objects to those firewalls. PAN-OS doesn’t synchronize pushed rules across
 HA peers. To manage rules and objects at different administrative levels in your
 organization, Create a Device Group Hierarchy . 

 Select
 Panorama Device Groups , and click
 Add . 

 Enter a unique
 Name and a
 Description 
 to identify the device group. 

 In the
 Devices section, select check boxes to assign firewalls to the group.
 To search a long list
 of firewalls, use the Filters. 

 You can assign any firewall to only one device group. You can assign each
 virtual system on a firewall to a different device group. To move a
 firewall from one device group to another, see Move a Firewall to a Different Device
 Group . 

 In the Reference Template section,
 Add 
 any templates or template stacks
 with
 objects referenced by the device group configuration. 

 You must assign the appropriate template or template stack references to the
 device group in order to successfully associate the template or template
 stack to the device group. This allows you to reference objects configured
 in a template or template stack without adding an unrelated device to a
 template stack. 

 Skip this step if the device group configuration does not reference any
 objects configured in a template or template stack. 

 ( Optional )
 Select Group HA Peers for firewalls that are HA
 peers. 

 You can only group managed firewall HA peers if they are in the same device
 group. 

 The firewall name of the passive or active-secondary peer is in
 parentheses. Grouping HA peers is a visual change and no configuration
 change occurs. 

 Select
 the Parent Device Group (default is
 Shared ) that will be just above the device group you
 are creating in the device group hierarchy. 

 If your policy rules will reference users and groups,
 assign
 a Master firewall. 

 This will be the only firewall in the device group from which Panorama
 gathers username and user group information. 

 Click
 OK to save your changes. 

 Select Commit Commit and Push and then
 Commit
 and Push your changes to the Panorama configuration and to the
 device group you added. 

 Previous 

 Manage Device Groups 

 Next 

 Move a Firewall to a Different Device Group 

 On This Page 

 Activation and Onboarding 

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

 Cloud Management for NGFWs 

 Cloud NGFW for AWS 

 Cloud NGFW for Azure 

 CN-Series 

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 Panorama 

 Service Provider 

 VM-Series 

 Plugins 

 SASE 

 Prisma Access 

 Prisma SASE Multitenant Platform 

 AI-Powered ADEM 

 Prisma Access Monitoring & Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

 Cloud-Delivered Security Services 

 Advanced WildFire 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 AI Access Security 

 Device Security 

 Enterprise DLP 

 SaaS Security 

 Network Security 

 Shared Policy for NGFWs and Prisma Access 

 IPSec VPN 

 Security Policy 

 Quantum Security 

 Endpoints 

 GlobalProtect 

 Remote Browser Isolation 

 Prisma Access Agent 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 FedRAMP 

 Prisma SASE for FedRAMP 

 Autonomous DEM for FedRAMP 

 Prisma SD-WAN Experts Corner 

 Network Policy 

 QoS Whitepaper 

 Security Architecture Whitepaper 

 External Antennas for ION-C Series 

 Dynamic Path Selection 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Resources 

 All Products A - Z 

 All Release Notes 

 Compatibility Matrix 

 Experts Corner 

 Network Security Platform 

 Security Policy 

 Decryption 

 Device-ID 

 IPSec VPN 

 Quality of Service 

 Quantum Security 

 11.1 & Later 

 Next-Generation Firewall 

 Administration 

 Panorama 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
