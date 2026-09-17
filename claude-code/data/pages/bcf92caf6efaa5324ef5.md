---
url: https://docs.paloaltonetworks.com/content/techdocs/en_US/pan-os/9-1/pan-os-panorama-api/get-started-with-the-pan-os-rest-api.html
fetched_at: 2026-09-16T13:53:56Z
source: palo-alto-main
---

# Get Started with the PAN-OS REST API Clear

Updated on 

 Wed Aug 21 13:48:19 PDT 2024 

 Focus 

 Home 

 PAN-OS 

 PAN-OS® and Panorama™ API Guide 

 Get Started with the PAN-OS REST API 

 Download PDF 

 PAN-OS® and Panorama™ API Guide 

 Get Started with the PAN-OS REST API 

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

 Get Started with the PAN-OS REST API 

 To use the PAN-OS® and Panorama™ REST API, first use
your administrative credentials to get an API key. You can then
use the API key to make API requests. 

 PAN-OS REST API 

 Access the PAN-OS REST API 

 Resource Methods and Query Parameters (REST API) 

 PAN-OS REST API Request and Response Structure 

 PAN-OS REST API Error Codes 

 Work With Objects (REST API) 

 Create a Security Policy Rule (REST API) 

 Work with Policy Rules on Panorama (REST API) 

 Create a Tag (REST
API) 

 Configure a Security
Zone (REST API) 

 Configure a Virtual
SD-WAN Interface (REST API) 

 Create an SD-WAN Policy
Pre Rule (REST API) 

 The PAN-OS REST API covers a subset of the firewall and Panorama
functions, and you’ll need to use the XML API to complete the configuration
and commit your changes. 

 The API requests in this guide use cURL commands . However, you
can make API requests with other tools such as Postman or a RESTClient .
By default, PAN-OS uses a self-signed certificate, so you will need
to use the -k parameter with cURL requests. Alternatively, you can replace the self-signed certificate with
one from a trusted certificate authority. If you have an internal
certificate authority, generate your own certificate and install
it on the firewall. 

 Previous 

 Get Version Info (API) 

 Next 

 PAN-OS REST API
