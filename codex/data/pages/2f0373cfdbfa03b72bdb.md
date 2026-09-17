---
url: https://docs.paloaltonetworks.com/content/techdocs/en_US/pan-os/9-1/pan-os-panorama-api/get-started-with-the-pan-os-xml-api/authenticate-your-api-requests.html
fetched_at: 2026-09-16T13:53:49Z
source: palo-alto-main
---

# Authenticate Your API Requests Clear

Updated on 

 Aug 21, 2024 

 Focus 

 Home 

 PAN-OS 

 PAN-OS® and Panorama™ API Guide 

 Get Started with the PAN-OS XML API 

 Authenticate Your API Requests 

 Download PDF 

 PAN-OS® and Panorama™ API Guide 

 Authenticate Your API Requests 

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

 Authenticate Your API Requests 

 Authenticate your API Requests for PAN-OS firewalls. 

 Palo Alto Networks encourages you to authenticate
your API requests by including a basic authentication token in the
header of your requests. The basic authentication header can be
used to authenticate both XML and REST API requests. 

 Convert your user name and password to Base64
format. 

 Example: username:password converts to
dXNlcm5hbWU6cGFzc3dvcmQ= 

 When making a request to the firewall, include the base64
converted token in the header preceded by Authorization:
Basic 

 Example: 

 curl -X POST 'https://firewall/api/?&type=config&action=get&xpath=/config/devices/entry[@name=%27localhost.localdomain%27]/network/interface/ethernet' -H 'Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=' 

 Include the header in each of the subsequent requests
to the firewall. 

 Previous 

 Make Your First API Call 

 Next 

 Explore the API
