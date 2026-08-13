---
url: https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-panorama-api/get-started-with-the-pan-os-rest-api/pan-os-rest-api-error-codes
fetched_at: 2026-08-13T17:11:42Z
source: palo-alto-main
---

# PAN-OS REST API Error Codes Clear

PAN-OS REST API Error Codes 

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
 PAN-OS REST API Error Codes 

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

 PAN-OS REST API Error Codes 

 Download PDF 

 PAN-OS® and Panorama™API Usage Guide 

 PAN-OS REST API Error Codes 

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

 PAN-OS REST API Error Codes 

 PAN-OS and Panorama REST API error code descriptions 

 The possible REST API feature-specific
error response codes and their descriptions are as follows: 

 Error Code Description 

 1 The operation was canceled, typically by the
caller. 

 2 Unknown internal server error. 

 3 Bad request. The caller specified an invalid
parameter. 

 4 Gateway timeout. A firewall or Panorama module
timed out before a backend operation completed. 

 5 Not found. The requested entity was not found. 

 6 Conflict. The entity that the caller attempted
to create already exists. 

 7 Forbidden. The caller does not have permission
to execute the specified operation. 

 16 Unauthorized. The request does not have valid
authentication credentials to perform the operation. 

 8 Resource exhausted. Some resource has been
exhausted. 

 9 Failed precondition. The operation was rejected
because the system is not in a state required for the execution
of the operation. 

 10 Aborted because of conflict. A typical cause
is a concurrency issue. 

 11 Out of range. The operation was attempted past
a valid range. And example is reaching an end-of-file. 

 12 Not implemented. The operation is disabled,
not implemented, or not supported. 

 13 Internal server error. An unexpected and potentially
serious internal error occurred. 

 14 Service unavailable. The service is temporarily
unavailable. 

 15 Internal server error. Unrecoverable data loss
or data corruption occurred. 

 Previous 

 PAN-OS REST API Request and Response Structure 

 Next 

 Work With Objects (REST API) 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
