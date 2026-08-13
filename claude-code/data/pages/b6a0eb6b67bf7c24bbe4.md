---
url: https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-overview/prisma-access-apis
fetched_at: 2026-08-13T17:25:12Z
source: palo-alto-main
---

# Prisma Access APIs Clear

Prisma Access APIs 

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

 Prisma Access APIs 

 Updated on 

 Mon Aug 10 14:01:14 PDT 2026 

 Focus 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deutsch (German) 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Access Docs 

 Release Notes 

 Select a Document 

 6.2 Preferred and Innovation 

 6.1 Preferred and Innovation 

 6.0 Preferred and Innovation 

 5.2 Preferred and Innovation 

 5.1 Preferred and Innovation 

 5.0 Preferred and Innovation 

 4.2 Preferred 

 4.1 Preferred 

 4.0 Preferred 

 3.2 Preferred and Innovation 

 Activation & Onboarding 

 Administration 

 Select a Document 

 4.0 & Later 

 Prisma Access China 

 Integrations 

 Incidents & Alerts 

 New Features 

 Updated on 

 Mon Aug 10 14:01:14 PDT 2026 

 Focus 

 Home 

 Prisma Access 

 Prisma Access Administration 

 Prisma Access Overview 

 Prisma Access APIs 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deutsch (German) 

 Prisma Access 

 Prisma Access APIs 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Access Docs 

 Release Notes 

 Select a Document 

 6.2 Preferred and Innovation 

 6.1 Preferred and Innovation 

 6.0 Preferred and Innovation 

 5.2 Preferred and Innovation 

 5.1 Preferred and Innovation 

 5.0 Preferred and Innovation 

 4.2 Preferred 

 4.1 Preferred 

 4.0 Preferred 

 3.2 Preferred and Innovation 

 Activation & Onboarding 

 Administration 

 Select a Document 

 4.0 & Later 

 Prisma Access China 

 Integrations 

 Incidents & Alerts 

 New Features 

 Previous 

 Prisma Access Infrastructure Management 

 Next 

 Prisma Access Insights APIs 

 Prisma Access APIs 

 Find the APIs to use with Prisma Access . 

 Where Can I Use This? What Do I Need? 

 Prisma Access (Managed by Strata Cloud Manager) 

 Prisma Access (Managed by Panorama) 

 Prisma Access license 

 APIs for Prisma Access (Managed by Strata Cloud Manager) 

 You can find more information about the APIs for Prisma Access (Managed by Strata Cloud Manager) on pan.dev , the site for Palo Alto Networks developer docs.
 Prisma Access (Managed by Strata Cloud Manager) uses these APIs for service onboarding, configuration, and
 operations. 

 APIs for Prisma Access (Managed by Panorama) 

 In addition to the XML APIs that are available for configuration and management in Panorama , there are XML APIs for the
 Cloud Services plugin that you can use to perform tasks specific to Prisma Access .
 Use these APIs through a third-party service, application, or script to automate
 configuration and reporting tasks for Prisma Access . 

 Access the Prisma Access (Managed by Panorama) API Using the Browser and Web Interface 

 To access the API using the browser, log in to the Panorama that manages Prisma
 Access with administrator privileges, then enter /api at the end
 of the URL. The URL changes to the XML API browser interface. 

 The Prisma Access APIs are located in the following XML Path Language (XPath) nodes
 in the XML tree: 

 Configuration Commands: XML API Configuration Commands devices entry[@name='localhost.localdomain'] plugins cloud_services 

 Operational Commands: XML API Operational Commands request plugins cloud_services prisma-access 

 As you navigate in the XML tree, Prisma Access populates the tree in the
 XML area. You can enter required values in the
 XML area and click Submit to
 process an XML request. For example, to request the onboarding status of a job,
 navigate to XML API Operational Commands request plugins cloud_services prisma-access job-status jobid , enter the Job id in the jobid field, enter
 the Service Type servicetype area, and click
 Submit to submit your request. 

 This XML only retrieves the onboarding status of a job. To retrieve the status of
 all commit operations, use the Prisma Access UI. 

 Prisma Access returns the output in XML format. 

 You can also use the web interface to find APIs in Panorama . 

 Use curl Commands to Retrieve Panorama Managed API Commands 

 If you prefer to use CLI to retrieve API command results, you can use APIs in
 conjunction with the API you use to retrieve
 public and infrastructure IP addresses for Prisma Access . To do so, use the
 following command: 

 Configuration Commands: 

 curl -k -X GET
 "https:// <panorama-ip-address> /api/?key= <api-key> &type=config&cmd= <api-parameters></api-parameters> 

 Operational Commands: 

 curl -k -X GET
 "https:// <panorama-ip-address> /api/?key= <api-key> &type=op&cmd= <api-parameters></api-parameters> 

 Where: 

 <panorama-ip-address> is the IP address of the Panorama
 that manages Prisma Access . 

 <api-key> is the API key retrieve ip addresses for
 Prisma Access ( Panorama Cloud Services Configuration Service Setup Generate API Key ). 

 <api-parameters> and
 </api-parameters> are the API parameters you use
 to retrieve the requested information from the API. 

 If you have a multi-tenant deployment, you add the name of the tenant for which you
 want to retrieve API information into the API. 

 For example, given a Prisma Access deployment that has the following parameters: 

 Panorama IP Address: 1.2.3.4 

 API key: 12345abcde 

 Tenant name: tenant-1 

 If you wanted to retrieve the number of active mobile users for that tenant, you
 would enter the following curl command: 

 curl -k -X GET
 "https://1.2.3.4/api/?key=12345abcde&type=op&cmd=<request><plugins><cloud_services><prisma-access><multi-tenant><tenant-name><entry
 name='tenant-1'></entry></tenant-name><remote-active-users-count/></multi-tenant></prisma-access></cloud_services></plugins></request>" 

 Use CLI Commands with Prisma Access (Managed by Panorama) 

 Prisma Access allows you to use CLI commands to retrieve Prisma Access 
 data. To access the CLI , establish a SSH connection
 using the IP address of the Panorama that manages Prisma Access . 

 The CLI uses the same modes and has the same behavior as PAN-OS
 commands, with the exception of entering the tenant name for multi-tenant
 deployments; you enter the tenant name using the tenant-name 
 tenant-name command. For example, given a tenant name of
 tenant-1 , enter the following command to retrieve to retrieve the active
 user count in a multi-tenant deployment: 

 admin-Panorama> request plugins cloud_services prisma-access multi-tenant remote-active-users-count tenant-name tenant-1 

pass
Current User Count: 253 

 Previous 

 Prisma Access Infrastructure Management 

 Next 

 Prisma Access Insights APIs 

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

 Hardware Reference 

 ION 1000 

 ION 1200 

 ION 1200-S 

 ION 2000 

 ION 3000 

 ION 3200 

 ION 5200 

 ION 7000 

 ION 9000 

 ION 9200 

 Hardware Quick Start Guides 

 ION 1200 

 ION 1200 4G 

 ION 1200 5G 

 ION 1200-S 

 ION 1200-S 4G 

 ION 1200-S 5G 

 ION 3200 

 ION 5200 

 ION 9200 

 Virtual ION Deployment 

 Virtual ION on AWS 

 Virtual ION on Azure 

 Virtual ION on GCP 

 Virtual ION on KVM for NFV 

 Virtual ION on OCI 

 Virtual ION on VMware 

 3rd Party Integrations 

 AWS Cloud-WAN Integration (GRE Connect) 

 AWS Cloud-WAN Integration (Tunnel-less Connect) 

 Checkpoint Integration 

 LiveAction Integration 

 Netskope Integration 

 Symantec Web Security Services Integration 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 4.1 Preferred 

 5.0 Preferred and Innovation 

 Administration 

 Prisma SASE 

 Prisma Access 

 Strata Cloud Manager 

 SASE 

 4.2 Preferred 

 5.1 Preferred and Innovation 

 5.0.1 Preferred and Innovation 

 Panorama 

 6.0 Preferred and Innovation 

 Prisma Access 

 4.0 Preferred 

 4.0 & Later 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
