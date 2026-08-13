---
url: https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-panorama-api/pan-os-xml-api-request-types/configuration-api/get-active-configuration/use-xpath-to-get-arp-information
fetched_at: 2026-08-13T17:06:45Z
source: palo-alto-main
---

# XPath Node Selection Clear

XPath Node Selection 

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

 XPath Node Selection 

 Updated on 

 Aug 28, 2025 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Generation Firewall Docs 

 Getting Started 

 Administration 

 Networking 

 Quick Start 

 Reference 

 Incidents & Alerts 

 Release Notes 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 11.0 (EoL) 

 PAN-OS 10.2 

 PAN-OS 10.1 (EoL) 

 PAN-OS 10.0 (EoL) 

 PAN-OS 9.1 (EoL) 

 PAN-OS 9.0 (EoL) 

 PAN-OS 8.1 (EoL) 

 Help 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 10.2 

 PAN-OS 10.1 

 New Features 

 Updated on 

 Aug 28, 2025 

 Focus 

 Home 

 Next-Generation Firewall 

 Getting Started with the PAN-OS XML API 

 XPath Node Selection 

 Download PDF 

 Next-Generation Firewall 

 XPath Node Selection 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Generation Firewall Docs 

 Getting Started 

 Administration 

 Networking 

 Quick Start 

 Reference 

 Incidents & Alerts 

 Release Notes 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 11.0 (EoL) 

 PAN-OS 10.2 

 PAN-OS 10.1 (EoL) 

 PAN-OS 10.0 (EoL) 

 PAN-OS 9.1 (EoL) 

 PAN-OS 9.0 (EoL) 

 PAN-OS 8.1 (EoL) 

 Help 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 10.2 

 PAN-OS 10.1 

 New Features 

 Previous 

 PAN-OS XML API Error Codes 

 Next 

 PAN-OS XML API Request Types and Actions 

 XPath Node Selection 

 When making requests, construct an HTTPS POST request with the correct type and action along
 with the correct XPath. Here is an example API request: 

 curl -X POST 'https://firewall/api?type=config&action=show&key=<APIkey>&xpath=/config/devices/entry/vsys/entry/rulebase/security" 

 Ensure you replace variables such as <hostname> and <APIkey> with the IP address or
 hostname of your firewall or Panorama and API key, respectively. 

 When making configuration requests ( type=config) , you can use XPath, a
 syntax for selecting nodes from within an XML document. Use the XPath to isolate and modify
 portions of your configuration. The XML configuration within PAN-OS uses four different types
 of nodes as shown here: 

 <users>
 <entry name="admin">
 <permissions>
 <role-based>
 <superuser>yes</superuser>
 </role-based>
 </permissions>
 </entry>
 <entry name="guest">
 <permissions>
 <role-based>
 <custom>
 <profile>NewUser</profile>
 </custom>
 </role-based>
 </permissions>
 </entry>
</users>

 Root nodes are top-level nodes with no parent. Requesting the root node returns all child
 elements. 

 Element nodes represent containers of information. Element nodes can contain other
 element nodes or simply act as a container of information.
 Example: <permissions></permissions> 

 Attribute nodes are nodes that contain name/value pairs. Example: <entry
 name="admin"></entry> 

 Text nodes contain plain text.
 Example: <superuser>yes</superuser> 

 There are various ways to specify the XPath for an XML
node in an API request. The simplest is to use the location path
of the resource. For example, to select all users within your management
configuration, use the following path: 

 /config/mgt-config/users 

 The above path specifies the following XML node that includes
all users: 

 <users>
 <entry name="admin">
 <permissions>
 <role-based>
 <superuser>yes</superuser>
 </role-based>
 </permissions>
 </entry>
 <entry name="guest">
 <permissions>
 <role-based>
 <custom>
 <profile>NewUser</profile>
 </custom>
 </role-based>
 </permissions>
 </entry>
</users>

 Targeting multiple nodes in an XPath using nested elements results
 in a successful command, but will not update all of the nodes. To update each node, send the
 configuration to each node using multiple successive calls. For
 example: 

 /entry[@name='TEST_IKE_PAN']/protocol/ikev1/dpd&element=<enable>yes</enable></dpd></ikev1><version>ikev2-preferred</version></protocol>&/ikev2&element=<ike-crypto-profile>default</ike-crypto-profile></ikev2>&/peer-address&element=<ip>1.2.3.4</ip> 

 To successfully update each node, target each node individually, for
 example: 

 entry[@name='TEST_IKE_PAN']/peer-address&element=<ip>1.2.3.4</ip> 

 Another method for selecting the XPath for an XML node is to
select the specific node, such as the superuser or NewUser node
within the node shown above. Use XPath syntax similar to the following
to drill-down and select a specific node: 

 XML Node 

 XPath Syntax 

 /config/mgt-config/users/entry/permissions/role-based/superuser[text()='yes'] 

 /config/mgt-config/users/entry/permissions/role-based/custom/profile[text()='NewUser'] 

 Previous 

 PAN-OS XML API Error Codes 

 Next 

 PAN-OS XML API Request Types and Actions 

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

 Cloud Management for NGFWs 

 Cloud NGFW for AWS 

 Cloud NGFW for Azure 

 CN-Series 

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 Service Provider 

 VM-Series 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 AI-Powered ADEM 

 Prisma Access Monitoring and Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

 Cloud-Delivered Security Services 

 Advanced WildFire 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 Device Security 

 Enterprise DLP 

 SaaS Security 

 Network Security 

 Shared Policy for NGFWs and Prisma Access 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 PAN-OS 

 Next-Generation Firewall 

 Reference 

 API 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
