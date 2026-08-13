---
url: https://docs.paloaltonetworks.com/enterprise-dlp/getting-started/configure-icap-forwarding
fetched_at: 2026-08-13T15:32:23Z
source: palo-alto-main
---

# Configure ICAP Forwarding Clear

Configure ICAP Forwarding 

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

 Configure ICAP Forwarding 

 Updated on 

 Tue Aug 04 16:01:43 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Enterprise DLP Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Reference 

 Release Notes 

 New Features by OS Version 

 New Features by Month 

 Updated on 

 Tue Aug 04 16:01:43 PDT 2026 

 Focus 

 Home 

 Enterprise DLP 

 Configure ICAP Forwarding 

 Download PDF 

 Enterprise DLP 

 Configure ICAP Forwarding 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Enterprise DLP Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Reference 

 Release Notes 

 New Features by OS Version 

 New Features by Month 

 Previous 

 Configure Syslog Forwarding for Enterprise DLP 

 Next 

 Edit the Structured Data Settings 

 Configure ICAP Forwarding 

 Configure Internet Content Adaption Protocol (ICAP) forwarding to integrate your
 existing on-premises third party DLP solutions with Enterprise Data Loss Prevention (E-DLP) . 

 On May 7, 2025 , Palo Alto Networks is introducing new Evidence Storage and Syslog Forwarding service IP
 addresses to improve performance and expand availability for these services
 globally. 

 You must allow these new service IP addresses on your network
 to avoid disruptions for these services. Review the Enterprise DLP 
 Release Notes for more
 information. 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by Panorama or Strata Cloud Manager) 

 Prisma Access (Managed by Panorama or Strata Cloud Manager) 

 Prisma Browser 

 Enterprise Data Loss Prevention (E-DLP) license 

 Review the Supported
 Platforms for details on the required license
 for each enforcement point. 

 Or any of the following licenses that include the Enterprise DLP license 

 Prisma Access CASB license 

 Next-Generation
CASB for Prisma Access and NGFW (CASB-X) license 

 Data Security license 

Configure Internet Content Adaptation Protocol (ICAP) forwarding to integrate
 your existing on-premises third party DLP solutions with Enterprise Data Loss Prevention (E-DLP) . In
 some sectors such as finance, you might need to maintain your legacy DLP systems while
 simultaneously adopting new cloud security strategies. By integrating ICAP with Enterprise DLP , you can configure Enterprise DLP to forward inspected files to
 your on-premises ICAP server for further inspection while still leveraging the advanced
 inline ML-based detections offered by Enterprise DLP . This one-way integration
 ensures all files matching your inline Enterprise DLP match criteria are
 transmitted to your configured ICAP server, enabling your existing DLP solution to
 perform its analysis. Concurrently, Enterprise DLP conducts its own inspection and
 policy rule enforcement, providing comprehensive data protection. 
 Enterprise DLP 
 generates an audit log for the initial ICAP forwarding
 configuration and when you modify an existing ICAP forwarding configuration. Enterprise DLP does not generate an audit log when you test the connectivity
 between Enterprise DLP and your ICAP server. 

 Enterprise DLP supports ICAP forwarding for inline inspection for traffic
 forwarded from NGFW and Prisma Access tenants (Managed by Panorama or Strata Cloud Manager ). 

 Enterprise DLP does not support ICAP forwarding for Email DLP, Endpoint DLP,
 or SaaS Security traffic. 

 Forwarded ICAP Field Descriptions 

 Field 

 Output 

 X-Client-IP 

 ( Default )
 0.0.0.0 

 X-Server-IP 

 ( Default )
 0.0.0.0 

 X-Subscriber-ID username of the traffic
 source forward to Enterprise DLP 

 X-Authenticated-User 

 PANW-DLP-API://<username> 

 <username> is the traffic
 source forwarded to Enterprise DLP 

 UserAgent 

 toolarium
 ICAP-Client/<client-version> 

 <client-version> is the
 Palo Alto Networks ICAP client version 

 apiVersion 

 Toolarium API version 

 requestSource 

 ( Default ) file 

 Indicates that Enterprise DLP is forwarding a file
 to your ICAP server 

 resourceName 

 Can display the forwarded file name or URL, or be empty

 Log in to 
 Strata Cloud Manager . 

 You configure ICAP forwarding for your enforcement points on Strata Cloud Manager regardless of whether they are managed on Strata Cloud Manager or a Panorama® management server . 

 Select Configuration Data Loss Prevention Settings ICAP and toggle the Disabled radio button to
 enable ICAP for your Enterprise DLP tenant. 

 Select the Type of ICAP connection you're using
 ( ICAP or ICAPS ). 

 The primary difference between the ICAP and
 ICAPS protocols is that ICAPS uses SSL/TLS
 encryption to secure communication between Enterprise DLP and your ICAP
 server, while ICAP does not. 

 For the Server REQMOD URL , enter the URL of your ICAP
 server that accepts ICAP requests for your on-premises third party DLP
 solution. 

 Your ICAP server URL can also include the port number your ICAP server uses
 for communication. If you don't enter a port number in the server URL, Enterprise DLP uses port 1344 for
 unsecured ICAP connections and port
 11344 for secured
 ICAPS connections. 

 Common formats for ICAP and ICAPS server URLs: 

 ICAP — icap://<Domain or
 IP>:<port>/<servicepath> 

 ICAPS — icaps://<Domain or
 IP>:<port>/<servicepath> 

 For the Server Certificate , drag and drop or click
 Browse File to upload a signed certificate authority
 (CA) certificate to enable authentication and communication between Enterprise DLP and ICAP server. 

 Enterprise DLP supports CA certificates in
 PEM format. 

 Enterprise DLP requires you upload a CA certificate for
 ICAP connections. 

 Test the connection between Enterprise DLP and your
 ICAP server. 

 Enterprise DLP requires you test the connection between Enterprise DLP and ICAP server before you can save your ICAP forwarding
 configuration. The connectivity test must be
 Success to Save your
 ICAP forwarding configuration. 

 Success — Enterprise DLP 
 successfully connected to your ICAP server. 

 Failed — Enterprise DLP 
 couldn't successfully connect to your ICAP server due one of the
 following reasons. 

 You configured the ICAP server network information
 incorrectly. Review your ICAP server URL, port, and server
 certificate to confirm you entered the correct information.
 Test the connectivity again after
 your review. 

 You entered your ICAP server configuration correctly but Enterprise DLP couldn't connect to your ICAP server due
 to an internal issue. Test the
 connectivity again. 

 Save your ICAP forwarding configuration. 

 Previous 

 Configure Syslog Forwarding for Enterprise DLP 

 Next 

 Edit the Structured Data Settings 

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

 SaaS Security 

 Endpoints 

 GlobalProtect 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Getting Started 

 Cloud-Delivered Security Services 

 Data Filtering 

 Enterprise DLP 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
