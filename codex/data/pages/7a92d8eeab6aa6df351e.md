---
url: https://docs.paloaltonetworks.com/ngfw/api/getting-started/explore-xmlapi/cli-xml-api-explore
fetched_at: 2026-08-13T16:40:51Z
source: palo-alto-main
---

# CLI Clear

CLI 

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

 CLI 

 Updated on 

 Thu Aug 28 13:33:18 PDT 2025 

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

 Thu Aug 28 13:33:18 PDT 2025 

 Focus 

 Home 

 Next-Generation Firewall 

 Getting Started with the PAN-OS XML API 

 Explore the XML API 

 CLI 

 Download PDF 

 Next-Generation Firewall 

 CLI 

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

 XML API Browser 

 Next 

 Structure of a PAN-OS XML API Request 

 CLI 

 Use an SSH client or terminal to access your firewall or Panorama CLI . 

 You can use the debug mode to see the underlying XML API requests used
 for the PAN-OS appliance. 

 Enter the following command to activate debug mode: 

 debug cli on 

 Running a CLI command, will give you the syntax for the XML API equivalent. For example
 the command, 

test url http://paloaltonetworks.com 

 Returns the
 following: 

 <request cmd="op" cookie="7581536015878829" uid="1206"><operations><test><url>http://paloaltonetworks.com</url></test></operations></request> 

 The first part of the query corresponds to the command type. With the response, you can
 formulate the corresponding XML call, like
 so: 

 https://<firewall>/api/?type=op&cmd=<test><url>http://paloaltonetworks.com</url></test>&key=<apikey>

 Depending on the CLI command, the XML tag values for cmd will
 vary. For example, here is a CLI command for showing firewall
 information: run show system info 

 The corresponding API call looks like this: 

 curl -X POST 'https://firewall/api?type=op&cmd=<show><system><info></info></system></show>&key=<apikey>" 

 Previous 

 XML API Browser 

 Next 

 Structure of a PAN-OS XML API Request 

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
