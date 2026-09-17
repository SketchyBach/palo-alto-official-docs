---
url: https://docs.paloaltonetworks.com/pan-os/9-1/pan-os-panorama-api/pan-os-xml-api-request-types/configuration-api/view-configuration-node-values-for-xpath
fetched_at: 2026-09-16T11:04:50Z
source: palo-alto-main
---

# View Configuration Node Values for XPath Clear

Updated on 

 Aug 21, 2024 

 Focus 

 Home 

 PAN-OS 

 PAN-OS® and Panorama™ API Guide 

 PAN-OS
XML API Request Types 

 Configuration
(API) 

 View Configuration Node Values for XPath 

 Download PDF 

 PAN-OS® and Panorama™ API Guide 

 View Configuration Node Values for XPath 

 Table of Contents 

 Filter

 Version 

 9.1 (EoL) 

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

 Get Started with the PAN-OS XML API 

 Enable API Access 

 Get Your API Key 

 Make Your First API Call 

 Authenticate Your API Requests 

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

 End-of-Life (EoL)

 View Configuration Node Values for XPath 

 Use
 action=complete action
 along with an XPath to see possible values that are available with
 the XPath node.

 View the possible values, such as network interfaces,
 for multi-vsys firewalls, use the following command: 

 curl -X POST 'https://firewall/api?type=config&action=complete&xpath=/config/devices/entry[@name='localhost.localdomain']/vsys&key=apikey" 

 Confirm that the XML response for the request looks like
 the following: 

 <response status="success" code="19">
 <completions>
 <completion value="vsys1" vxpath="/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']" current="yes" help-string="vsys1"/>
 </completions>
</response>

 Previous 

 Multi-Move or Multi-Clone Configuration 

 Next 

 Commit Configuration (API)
