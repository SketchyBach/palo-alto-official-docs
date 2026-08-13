---
url: https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-panorama-api/get-started-with-the-pan-os-rest-api/create-security-policy-rule-rest-api
fetched_at: 2026-08-13T17:11:41Z
source: palo-alto-main
---

# Create a Security Policy Rule (REST API) Clear

Create a Security Policy Rule (REST API) 

 Home 

 EN

 Location 

 Documentation Home 

 Palo Alto Networks 

 Support 

 Live Community 

 Knowledge Base 

 Strata Copilot

 PAN-OS® and Panorama™API Usage Guide 

 : 
 Create a Security Policy Rule (REST API) 

 Updated on 

 Jan 2, 2025 

 Focus 

 Download PDF 

 Filter

 Version 

 11.1 & Later 

 11.1 & Later 

 10.2 

 10.1 

 10.0 (EoL) 

 9.1 (EoL) 

 Expand all | Collapse all 

 About the PAN-OS API 

 PAN-OS XML API Components 

 Structure of a PAN-OS XML API Request 

 API Authentication and Security 

 XML and XPath 

 XPath Node Selection 

 PAN-OS API Authentication 

 Enable API Access 

 Get Your API Key 

 Generate an API Key Certificate 

 Authenticate Your API Requests 

 Get Started with the PAN-OS XML API 

 Make Your First API Call 

 Explore the API 

 Use the API Browser 

 Use the CLI to Find XML API Syntax 

 Use the Web Interface to Find XML API Syntax 

 PAN-OS XML API Error Codes 

 PAN-OS XML API Use Cases 

 Upgrade a Firewall to the Latest PAN-OS Version (API) 

 Show and Manage GlobalProtect Users (API) 

 Query a Firewall from Panorama (API) 

 Upgrade PAN-OS on Multiple HA Firewalls through Panorama (API) 

 Automatically Check for and Install Content Updates (API) 

 Enforce Policy using External Dynamic Lists and AutoFocus Artifacts (API) 

 Configure SAML 2.0 Authentication (API) 

 Quarantine Compromised Devices (API) 

 Manage Certificates (API) 

 PAN-OS XML API Request Types 

 PAN-OS XML API Request Types and Actions 

 Request Types 

 Configuration Actions 

 Actions for Modifying a Configuration 

 Actions for Reading a Configuration 

 Asynchronous and Synchronous Requests to the PAN-OS XML API 

 Configuration (API) 

 Get Active Configuration 

 Use XPath to Get Active Configuration 

 Use XPath to Get ARP Information 

 Get Candidate Configuration 

 Set Configuration 

 Edit Configuration 

 Delete Configuration 

 Rename Configuration 

 Clone Configuration 

 Move Configuration 

 Override Configuration 

 Multi-Move or Multi-Clone Configuration 

 Multi-config Request (API) 

 View Configuration Node Values for XPath 

 Commit Configuration (API) 

 Commit 

 Commit-All 

 Run Operational Mode Commands (API) 

 Get Reports (API) 

 Dynamic Reports 

 Predefined Reports 

 Custom Reports 

 Export Files (API) 

 Export Packet Captures 

 Export Application PCAPS 

 Export Threat, Filter, and Data Filtering PCAPs 

 Export Certificates and Keys 

 Export Technical Support Data 

 Import Files (API) 

 Importing Basics 

 Import Files 

 Retrieve Logs (API) 

 API Log Retrieval Parameters 

 Example: Use the API to Retrieve Traffic Logs 

 Apply User-ID Mapping and Populate Dynamic Groups (API) 

 Get Version Info (API) 

 Get Started with the PAN-OS REST API 

 PAN-OS REST API 

 Access the PAN-OS REST API 

 Resource Methods and Query Parameters (REST API) 

 PAN-OS REST API Request and Response Structure 

 PAN-OS REST API Error Codes 

 Work With Objects (REST API) 

 Create a Security Policy Rule (REST API) 

 Work with Policy Rules on Panorama (REST API) 

 Create a Tag (REST API) 

 Configure a Security Zone (REST API) 

 Configure an SD-WAN Interface (REST API) 

 Create an SD-WAN Policy Pre Rule (REST API) 

 Configure an Ethernet Interface (REST API) 

 Update a Virtual Router (REST API) 

 Work With Decryption (APIs) 

 Updated on 

 Jan 2, 2025 

 Focus 

 Home 

 PAN-OS 

 PAN-OS® and Panorama™API Usage Guide 

 Get Started with the PAN-OS REST API 

 Create a Security Policy Rule (REST API) 

 Download PDF 

 PAN-OS® and Panorama™API Usage Guide 

 Create a Security Policy Rule (REST API) 

 Table of Contents 

 Filter

 Version 

 11.1 & Later 

 11.1 & Later 

 10.2 

 10.1 

 10.0 (EoL) 

 9.1 (EoL) 

 Expand all | Collapse all 

 About the PAN-OS API 

 PAN-OS XML API Components 

 Structure of a PAN-OS XML API Request 

 API Authentication and Security 

 XML and XPath 

 XPath Node Selection 

 PAN-OS API Authentication 

 Enable API Access 

 Get Your API Key 

 Generate an API Key Certificate 

 Authenticate Your API Requests 

 Get Started with the PAN-OS XML API 

 Make Your First API Call 

 Explore the API 

 Use the API Browser 

 Use the CLI to Find XML API Syntax 

 Use the Web Interface to Find XML API Syntax 

 PAN-OS XML API Error Codes 

 PAN-OS XML API Use Cases 

 Upgrade a Firewall to the Latest PAN-OS Version (API) 

 Show and Manage GlobalProtect Users (API) 

 Query a Firewall from Panorama (API) 

 Upgrade PAN-OS on Multiple HA Firewalls through Panorama (API) 

 Automatically Check for and Install Content Updates (API) 

 Enforce Policy using External Dynamic Lists and AutoFocus Artifacts (API) 

 Configure SAML 2.0 Authentication (API) 

 Quarantine Compromised Devices (API) 

 Manage Certificates (API) 

 PAN-OS XML API Request Types 

 PAN-OS XML API Request Types and Actions 

 Request Types 

 Configuration Actions 

 Actions for Modifying a Configuration 

 Actions for Reading a Configuration 

 Asynchronous and Synchronous Requests to the PAN-OS XML API 

 Configuration (API) 

 Get Active Configuration 

 Use XPath to Get Active Configuration 

 Use XPath to Get ARP Information 

 Get Candidate Configuration 

 Set Configuration 

 Edit Configuration 

 Delete Configuration 

 Rename Configuration 

 Clone Configuration 

 Move Configuration 

 Override Configuration 

 Multi-Move or Multi-Clone Configuration 

 Multi-config Request (API) 

 View Configuration Node Values for XPath 

 Commit Configuration (API) 

 Commit 

 Commit-All 

 Run Operational Mode Commands (API) 

 Get Reports (API) 

 Dynamic Reports 

 Predefined Reports 

 Custom Reports 

 Export Files (API) 

 Export Packet Captures 

 Export Application PCAPS 

 Export Threat, Filter, and Data Filtering PCAPs 

 Export Certificates and Keys 

 Export Technical Support Data 

 Import Files (API) 

 Importing Basics 

 Import Files 

 Retrieve Logs (API) 

 API Log Retrieval Parameters 

 Example: Use the API to Retrieve Traffic Logs 

 Apply User-ID Mapping and Populate Dynamic Groups (API) 

 Get Version Info (API) 

 Get Started with the PAN-OS REST API 

 PAN-OS REST API 

 Access the PAN-OS REST API 

 Resource Methods and Query Parameters (REST API) 

 PAN-OS REST API Request and Response Structure 

 PAN-OS REST API Error Codes 

 Work With Objects (REST API) 

 Create a Security Policy Rule (REST API) 

 Work with Policy Rules on Panorama (REST API) 

 Create a Tag (REST API) 

 Configure a Security Zone (REST API) 

 Configure an SD-WAN Interface (REST API) 

 Create an SD-WAN Policy Pre Rule (REST API) 

 Configure an Ethernet Interface (REST API) 

 Update a Virtual Router (REST API) 

 Work With Decryption (APIs) 

 Create a Security Policy Rule (REST API) 

 The example in this section shows you how to
create and update a Security policy rule on the firewall. Use this
example to get familiar with the REST API and then make it work
with other policy types on the firewall. Access the REST API reference
documentation at https://<IP address or FQDN of the firewall or Panorama>/restapi-doc/ for
help with the resource URIs for the different objects and policies
and for help with the properties supported for each type of request.
For an overview, see PAN-OS REST API Request and Response Structure . 

 Create an Application
Object 

 Create a Security
Policy Rule 

 Reference an Address
Object in the Rule 

 Create
an Application Object 

 Make a POST request to create an
application object that allows you to allow browser-based applications
that belong to the category collaboration and subcategory email.
To make this application object named email-collaboration-apps available
across all virtual systems on a firewall, create the object at location=shared .
Use Palo Alto Networks Applipedia ,
the application database to view the attributes (Category, Subcategory,
Technology, Risk or Characteristic) that you can use to define the
object. You can also refer to https://<firewall_IP>/restapi-doc/#tag/objects-applications for details
on how to construct an application object. Here is an example. 

 curl -X POST \
 'https://10.2.1.4/restapi/v11.0/Objects/Applications?location=shared&name=email-collaboration-apps' \
 -H 'X-PAN-KEY: *******' \
 -d '{
 "entry": [
 {
 "@location": "shared",
 "@name": "email-collaboration-apps",
 "able-to-transfer-file": "yes",
 "category": "collaboration",
 "description": "apps we allow for collaboration",
 "risk": "2",
 "subcategory": "email",
 "technology": "browser-based"
 }
 ]
}' 

 You can now use this application
object in a Security policy rule. 

 Create
a Security Policy Rule 

 Before you start here, use the
XML API or any of the other management interfaces to set up interfaces
and zones on the firewall. 

 To create a Security policy rule,
make a POST request. In the following example, the API key is provided
as a custom header X-PAN-KEY instead of as query parameter. For
more details, see Access the PAN-OS REST API . The query
parameters include the name of the rule, location and vsys name location=vsys&vsys=<vsys_name>&name=<rule_name> .
And in the request body specify the same name, location, vsys name,
and includes additional properties for the Security policy rule
including the application object you created earlier. 

 curl -X POST \

 'https://10.2.1.4/restapi/v11.0/Policies/SecurityRules?location=vsys&vsys=vsys1&name=rule-example1' \
 -H 'X-PAN-KEY: *******' \
 -d '{
 "entry": [
 {
 "@location": "vsys",
 "@name": "rule-example1",
 "@vsys": "vsys1",
 "action": "allow",
 "application": {
 "member": [
 "email-collaboration-apps"
 ]
 },
 "category": {
 "member": [
 "any"
 ]
 },
 "destination": {
 "member": [
 "any"
 ]
 },
 "from": {
 "member": [
 "zone-edge1"
 ]
 },
 "source-hip": {
 "member": [
 "any"
 ]
 },
 "destination-hip": {
 "member": [
 "any"
 ]
 },
 "service": {
 "member": [
 "application-default"
 ]
 },
 "source": {
 "member": [
 "any"
 ]
 },
 "source-user": {
 "member": [
 "any"
 ]
 },
 "to": {
 "member": [
 "any"
 ]
 }
 }
 ]
}' 

 Instead of using
an application object, you can list applications by name as long
as the applications are included in the application content version
installed on the firewall. 

 "application": {
 "member": [
 "gmail",
 "linkedin",
 "sendgrid",
 "front"
 ]
}

 Reference
an Address Object in the Rule 

 To allow access to only
specific addresses in the source zone, you can include an address
object and restrict access to only those members in the source zone
with "source": {"member": ["web-servers-production"]} as shown
in the following example: 

 curl -X PUT \
 'https://10.2.1.4/restapi/v11.0/Policies/SecurityRules?location=vsys&name=rule-example1&vsys=vsys1' \
 -H 'X-PAN-KEY: *******' \
 -d '{
 "entry": [
 {
 "@location": "vsys",
 "@name": "rule-example1",
 "@vsys": "vsys1",
 "action": "allow",
 "application": {
 "member": [
 "email-collaboration-apps"
 ]
 },
 "category": {
 "member": [
 "any"
 ]
 },
 "destination": {
 "member": [
 "any"
 ]
 },
 "from": {
 "member": [
 "zone-edge1"
 ]
 },
 "source-hip": {
 "member": [
 "any"
 ]
 },
 "destination-hip": {
 "member": [
 "any"
 ]
 },
 "service": {
 "member": [
 "application-default"
 ]
 },
 "source": {
 "member": [
 "web-servers-production"
 ]
 },
 "source-user": {
 "member": [
 "any"
 ]
 },
 "to": {
 "member": [
 "any"
 ]
 }
 }
 ]
}' 

 If successful, the response
is 

 {"@status": "success","@code": "20","msg":"command succeeded"
 }
} 

 If the address object does not exist,
the response is as follows: 

 {"code": 3,"message": "Invalid Object","details": [
 {"@type": "CauseInfo","causes": [
 {"code": 12,"module": "panui_mgmt","description": "Invalid Object: rule-example1 -> source 'web-servers-production' is not an allowed keyword. rule-example1 -> source web-servers-production is an invalid ipv4/v6 address. rule-example1 -> source web-servers-production invalid range start IP. 
 rule-example1 -> source 'web-servers-production' is not a valid reference. rule-example1 -> source is invalid."
 }
 ]
 }
 ]
}

 Previous 

 Work With Objects (REST API) 

 Next 

 Work with Policy Rules on Panorama (REST API) 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
