---
url: https://docs.paloaltonetworks.com/iot/integration/vulnerability-scanning/integrate-iot-security-with-tenable/set-up-tenable-for-integration
fetched_at: 2026-08-13T16:37:30Z
source: palo-alto-main
---

# Set up Tenable Vulnerability Management for Integration Clear

Set up Tenable Vulnerability Management for Integration 

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

 Set up Tenable Vulnerability Management for Integration 

 Updated on 

 Thu May 14 09:23:33 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Device Security Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Enterprise Administration 

 Integrations 

 Release Notes 

 Best Practice 

 New Features 

 Updated on 

 Thu May 14 09:23:33 PDT 2026 

 Focus 

 Home 

 Device Security 

 Device Security Integration Guide 

 Vulnerability Scanning 

 Integrate Device Security with Tenable Vulnerability Management 

 Set up Tenable Vulnerability Management for Integration 

 Download PDF 

 Device Security 

 Set up Tenable Vulnerability Management for Integration 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Device Security Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Enterprise Administration 

 Integrations 

 Release Notes 

 Best Practice 

 New Features 

 Previous 

 Integrate Device Security with Tenable Vulnerability Management 

 Next 

 Set up Device Security and XSOAR for Tenable Vulnerability Management Integration 

 Set up Tenable Vulnerability Management for Integration 

 Set up Tenable Vulnerability Management for integration with Device Security through
 Cortex XSOAR . 

 Where Can I Use This? What Do I Need? 

 Device Security (Managed by Strata Cloud Manager) 

 (Legacy) IoT Security (Standalone portal) 

 One of the following subscriptions: 

 Device Security subscription for an advanced
 Device Security product (Enterprise Plus,
 Industrial OT, or Medical)

 Device Security X subscription

 One of the following Cortex XSOAR setups:

 A free, cohosted, limited-featured
 Cortex XSOAR instance

 A full-featured Cortex XSOAR server

 Before integrating Device Security with Tenable Vulnerability Management (formerly known as
 Tenable.io), make sure you have a working Tenable Vulnerability Management setup.
 It’s assumed that you’ve already installed
a Tenable Nessus vulnerability scanner on your network so that it
 can reach the hosts you intend to scan, made a Tenable Vulnerability Management account,
and associated the scanner with your account. 

 After completing
those steps, you must generate two API keys that will allow Cortex XSOAR to access the Tenable API and then copy and paste them into
your XSOAR integration instance configuration. 

 Generate two API keys. 

 Log in to your Tenable Vulnerability Management account. 

 To generate the two API keys you need, click Settings My Account API Keys Generate . 

 A
warning appears that explains how generating API keys will invalidate
any existing keys and unauthorize applications currently using them. 

 To continue, click Generate . 

 The
two API keys appear on the page: 

 Access Key :
This key authenticates Cortex XSOAR and Tenable.io to each other
and permits XSOAR to access Tenable API resources. 

 Secret
Key : This key encrypts and decrypts communications between
Tenable.io and Cortex XSOAR . 

 Record the two API keys. 

 Because Tenable only displays the keys immediately after
generating them, do not navigate away from this page until you have
copied the text strings for both keys, pasted them into a text file,
and saved the file in a secure location. You will enter these when
configuring the Tenable integration instance in Cortex XSOAR . 

 Previous 

 Integrate Device Security with Tenable Vulnerability Management 

 Next 

 Set up Device Security and XSOAR for Tenable Vulnerability Management Integration 

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

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 Service Provider 

 VM-Series 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 Device Security 

 Cloud-Delivered Security Services 

 Integrations 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
