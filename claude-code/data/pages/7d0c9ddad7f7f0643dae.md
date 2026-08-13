---
url: https://docs.paloaltonetworks.com/pan-os/10-1/pan-os-panorama-api/get-started-with-the-pan-os-rest-api/work-with-address-objects-rest-api
fetched_at: 2026-08-13T17:03:16Z
source: palo-alto-main
---

# Work With Objects (REST API) Clear

Work With Objects (REST API) 

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

 Work With Objects (REST API) 

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

 PAN-OS REST API Use Cases 

 Work With Objects (REST API) 

 Download PDF 

 Next-Generation Firewall 

 Work With Objects (REST API) 

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

 PAN-OS REST API Use Cases 

 Next 

 Create a Security Policy Rule (REST API) 

 Work With Objects (REST API) 

 Objects are elements that you use within policy
 rules. The firewalls and Panorama support a large number of objects
 such as tags, address objects, log forwarding profiles, and security
 profiles. 

 The examples in this section show you how to perform
 CRUD operations with an address object. You can use this example
 to work with other objects of the firewall. Access the REST API
 reference documentation at https://<IP address or FQDN of the firewall or Panorama>/restapi-doc/ for
 help with the resource URIs for different objects and the structure
 of the request. For an overview, see
 PAN-OS REST API Request and Response Structure . 

 Create an Address
 Object 

 Edit an Address
 Object 

 Rename an Address
 Object 

 Delete an Address
 Object 

 Get Address Objects 

 Create a Tag 

 Create
 an Address Object 

 Make a POST request to create an address
 object. In the request, the query parameters must include the name
 and the location on where you want to create the object. And in
 the request body include the same name, location and other properties
 to define the object. For example: 

 curl -X POST \
 'https://10.2.1.4/restapi/v11.0/Objects/Addresses?location=shared&name=web-servers-production' \
 -H 'X-PAN-KEY: ********' \
 -d '{
 "entry": [
 {
 "@location": "shared",
 "@name": "web-servers-production",
 "description": "what is this for?",
 "fqdn": "docs.paloaltonetworks.com",
 "tag": {
 "member": [
 "blue"
 ]
 }
 }
 ]
}' 

 Edit
 an Address Object 

 Make a PUT request and include the name
 and location of the object as query parameters. Include the same
 location and name in the request body and define the properties
 of the object you’d like to change. In the following example, you
 are modifying the description and adding a new tag called red to
 the address object. If the tag does not already exist, you must
 first create the tag before you can reference it in the address
 object. 

 curl -X PUT \
 'https://10.2.1.4/restapi/v11.0/Objects/Addresses?location=shared&name=web-servers-production' \
 -H 'X-PAN-KEY: ********' \
 -d '{
 "entry": [
 {
 "@location": "shared",
 "@name": "web-servers-production",
 "description": "publish servers",
 "fqdn": "docs.paloaltonetworks.com",
 "tag": {
 "member": [
 "blue",
 "red"
 ]
 }
 }
 ]
}' 

 The response is 

 {
 "@code": "20",
 "@status": "success",
 "msg": "command succeeded"
} 

 Rename
 an Address Object 

 When renaming an object, make a POST
 request with the following query parameters—name of the object name=<name> ,
 l ocation=<location> , and the new name newname=<name> .
 The following example renames web-servers-production to web-server-publish. 

 curl -X POST \
 'https://10.5.196.4/restapi/v11.0/Objects/Addresses:rename?location=shared&name=web-servers-production&newname=web-server-publish' \
 -H 'X-PAN-KEY: ********' 

 Delete
 an Address Object 

 Make a DELETE request and include the
 name and the location of the object as query parameters. For example: 

 curl -X DELETE \
 'https://10.2.1.4/restapi/v11.0/Objects/Addresses?location=shared&name=web-server-production' \
 -H 'X-PAN-KEY: ********' 

 Get
 Address Objects 

 Make a GET request to retrieve a list
 of all address objects within a specified location. For example,
 the following query reads all address objects in vsys1 which is
 indicated with location=vsys&vsys=vsys1 in
 the query parameter. 

 curl -X GET \
 'https://10.2.1.4/restapi/v11.0/Objects/Addresses?location=vsys&vsys=vsys1' \
 -H 'X-PAN-KEY: ********' 

 And the response includes the list of address
 objects that are configured on vsys1 on the firewall. 

 {
 "@code": "19",
 "@status": "success",
 "result": {
 "@count": "3",
 "@total-count": "3",
 "entry": [
 {
 "@location": "vsys",
 "@name": "fqdn1",
 "@vsys": "vsys1",
 "fqdn": "www.test.com"
 },
 {
 "@location": "vsys",
 "@name": "Peer1",
 "@vsys": "vsys1",
 "ip-netmask": "172.0.0.1/24"
 },
 {
 "@location": "vsys",
 "@name": "Peer2renamed",
 "@oldname": "Peer2",
 "@vsys": "vsys1",
 "ip-netmask": "200.0.0.1/24"
 }
 ]
 }
}

 Create a Tag 

 Tags allow you to group objects using keywords or phrases. Use tags to identify the
 purpose of a rule or configuration object and to help you better organize your
 rulebase. To ensure that policy rules are properly tagged. You must create a tag
 before you can assign it as a group tag on a rule. 

 Link tags are tags that enable you use to identify groups of physical interfaces
 specifically for an SD-WAN configuration on Panorama™. Some examples of link tags
 are Low Cost Paths, General Access, Private HQ, and Backup. The following is an
 example of a REST API request to create a link tag. 

 curl -X POST 'https://<Panorama>/restapi/v11.1/objects/tags?location=device-group&device-group=SD-WAN_Branch&name=Low-Cost-Paths'
 -H 'X-PAN-KEY: <your key>
 -d '{
 "entry": {
 "@name": "Low-Cost-Paths”,
 “comments”: “Groups two low cost broadband links and a backup link”
 }
 }' 

 Previous 

 PAN-OS REST API Use Cases 

 Next 

 Create a Security Policy Rule (REST API) 

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
