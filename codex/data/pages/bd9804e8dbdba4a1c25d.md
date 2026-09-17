---
url: https://docs.paloaltonetworks.com/enterprise-dlp/getting-started/configure-icap-forwarding
fetched_at: 2026-09-15T15:10:26Z
source: palo-alto-main
---

# Configure ICAP Forwarding Clear

Updated on 

 Sep 4, 2026 

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

 Configure Internet Content Adaptation Protocol (ICAP) forwarding to integrate your
 existing on-premises third-party DLP solutions with Enterprise Data Loss Prevention (E-DLP) . 

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

 Configure Internet Content Adaptation Protocol (ICAP) forwarding to integrate your
 existing on-premises third-party DLP solutions with Enterprise Data Loss Prevention (E-DLP) . In
 some sectors such as finance, you might need to maintain your legacy DLP systems
 while simultaneously adopting new cloud security strategies. By integrating ICAP
 with Enterprise DLP , you can configure Enterprise DLP to forward inspected
 files to your on-premises ICAP server for further inspection while still leveraging
 the advanced inline ML-based detections offered by Enterprise DLP . This one-way
 integration ensures all files that Enterprise DLP actively scans and that match
 your inline policy criteria are transmitted to your configured ICAP server, enabling
 your existing DLP solution to perform its analysis. Concurrently, Enterprise DLP conducts its own inspection and policy rule enforcement, providing comprehensive
 data protection. 

 NGFW and Prisma Access Tenants — Enterprise DLP 
 forwards a file to your ICAP server once per unique file hash. Files with
 cached inspection results do not trigger an additional ICAP forward. Enterprise DLP retains inspection history for 90 days for files that
 generated a DLP incident . 

 SaaS Security — Enterprise DLP forwards a file to your
 ICAP server for every file forwarded to Enterprise DLP , including files
 that return a cached inspection result. 

 Enterprise DLP generates an audit log for the initial ICAP forwarding
 configuration and when you modify an existing ICAP forwarding configuration. Enterprise DLP does not generate an audit log when you test the connectivity
 between Enterprise DLP and your ICAP server. 

 Enterprise DLP does not support ICAP forwarding for Email DLP or Endpoint
 DLP. 

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
 source forwarded to Enterprise DLP 

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

 Log in to Strata Cloud Manager . 

 You configure ICAP forwarding for your enforcement points on Strata Cloud Manager regardless of whether they are managed on Strata Cloud Manager or a Panorama® management server . 

 Select Configuration Data Loss Prevention Settings ICAP and toggle Disabled to enable ICAP for
 your Enterprise DLP tenant. 

 For Type , choose the type of ICAP connection you're
 using ( ICAP or ICAPS ). 

 The primary difference between the ICAP and
 ICAPS protocols is that ICAPS uses SSL/TLS
 encryption to secure communication between Enterprise DLP and your ICAP
 server, while ICAP does not. 

 For Server REQMOD URL , enter the URL of your ICAP
 server that accepts ICAP requests for your on-premises third-party DLP
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

 For Server Certificate , drag and drop or click
 Browse File to upload a signed certificate authority
 (CA) certificate to enable authentication and communication between Enterprise DLP and your ICAP server. 

 Enterprise DLP supports CA certificates in
 PEM format. 

 Enterprise DLP requires a CA certificate for
 ICAPS connections. 

 Test the connection between Enterprise DLP and your
 ICAP server. 

 Enterprise DLP requires you test the connection between Enterprise DLP and ICAP server before you can save your ICAP forwarding
 configuration. The connectivity test must be
 Success to Save your
 ICAP forwarding configuration. 

 Success — Enterprise DLP 
 successfully connected to your ICAP server. 

 Failed — Enterprise DLP 
 couldn't connect to your ICAP server due to one of the following
 reasons. 

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
