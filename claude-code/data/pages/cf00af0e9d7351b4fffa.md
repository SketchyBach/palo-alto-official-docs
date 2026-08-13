---
url: https://docs.paloaltonetworks.com/advanced-threat-prevention/custom-signatures-reference/custom-signature-contexts/context-qualifiers
fetched_at: 2026-08-13T15:17:41Z
source: palo-alto-main
---

# Context Qualifiers Clear

Context Qualifiers 

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

 Context Qualifiers 

 Updated on 

 Wed Jun 10 20:25:53 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Advanced Threat Prevention 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Custom Application IDs and Threat Signatures 

 Reference 

 Release Notes 

 Updated on 

 Wed Jun 10 20:25:53 PDT 2026 

 Focus 

 Home 

 Advanced Threat Prevention Powered by Precision AI® 

 Custom Signature Contexts 

 Context Qualifiers 

 Download PDF 

 Advanced Threat Prevention Powered by Precision AI® 

 Context Qualifiers 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Advanced Threat Prevention 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Custom Application IDs and Threat Signatures 

 Reference 

 Release Notes 

 Previous 

 panav-rsp-zip-compression-ratio 

 Next 

 New Features in Advanced Threat Prevention 

 Context Qualifiers 

 Add context qualifiers with custom signatures to limit
match conditions and reduce false positives. 

 Where Can I Use
 This? What Do I Need? 

 Prisma Access (Managed by Panorama or Strata Cloud Manager) 

 NGFW (Managed by Panorama or Strata Cloud Manager) 

 VM-Series 

 CN-Series 

 Advanced Threat Prevention (for enhanced feature
 support) or Threat Prevention License 

 Qualifiers lessen the chance of false positives by restricting
the locations where the firewall can find a given pattern. In other
words, a signature matches only when the firewall detects the pattern
inside a specific qualifier, which corresponds to a specific context.
For example, you might use the http-method qualifier to specify
that a http-req-uri-path pattern matters when found inside a HTTP
GET method. 

 FTP Command Qualifiers 

 FTP Vendor ID Qualifiers 

 HTTP Header Field
Qualifiers 

 HTTP Method Qualifiers 

 IMAP Command Qualifiers 

 RTSP Method Qualifiers 

 SMTP Method Qualifiers 

 FTP
Command Qualifiers 

 FTP command qualifiers can be added
to custom signatures that use FTP-related contexts to limit a match
condition to specific FTP commands. 

 ABOR ACCT ALLO APPE AUTH CDUP CWD 

 DELE EHLO ERPT HELO LIST MDTM MKD 

 MODE NLIST OPTS PASS PASV PBSZ PORT 

 PWD QUIT REIN REST RETR RMD RNFR 

 RNTO SITE SIZE SMNT STAT STOR STOU 

 STRU SYST TEST TYPE UNKNOWN-COMMAND UNLOCK USER 

 XCRC XMD5 XSHA1 

 FTP
Vendor ID Qualifiers 

 FTP vendor ID qualifiers can be added
to custom signatures that use FTP-related contexts to limit a match
condition to specific FTP clients. 

 CEASERFTP EASY_FILE_SHARING_FTP FILE_COPA_FTP FREEFTPD MICROSOFTFTP NETTERM 

 PROFTPD SERV_U UNKNOWN_FTP_SERVER VSFTPD WARFTPD WS_FTP 

 WUFTP 

 HTTP
Header Field Qualifiers 

 HTTP header field qualifiers can
be added to custom signatures that use HTTP-related contexts to
limit a match condition to HTTP headers that have specific values
for select header fields. 

 ACCEPT_LANGUAGE AUTHORIZATION CONTENT_ENCODING CONTENT_LENGTH CONTENT_TYPE HOST 

 IF_MOD_SINCE SUBSCRIBE_HDR TRANSFER_ENCODING UNKNOWN_HDR X_FORWARD_FOR 

 HTTP
Method Qualifiers 

 HTTP method qualifiers can be added
to custom signatures that use HTTP-related contexts to limit a match
condition to HTTP headers that use specific HTTP methods. 

 BCOPY BDELETE BITS_POST BMOVE BPROPFIND BROPPATCH CCM_POST 

 CONNECT COPY DELETE GET HEAD LINK LOCK 

 MCKCOL MOVE NOTIFY OPTIONS POLL POST PROPFIND 

 PROPPATCH PROXY_SUCCESS PUT RPC_CONNECT SEARCH SMS_POST SOURCE 

 SUBSCRIBE TRACE TRACK UNKNOWN_METHOD UNLINK UNLOCK UNSUBSCRIBE 

 IMAP
Command Qualifiers 

 IMAP command qualifiers can be added
to custom signatures that use IMAP-related contexts to limit a match
condition to specific IMAP commands. 

 APPEND AUTHENTICATE CAPABILITY CHECK CLOSE COPY CREATE 

 DELETE EXAMINE EXPUNGE FETCH FIND IDLE LIST 

 LOGIN LSUB NOOP RENAME SEARCH SELECT STARTTLS 

 STATUS SUBSCRIBE UNKNOWN_COMMAND UNSUBSCRIBE 

 RTSP
Method Qualifiers 

 RTSP method qualifiers can be added
to custom signatures that use RTSP-related contexts to limit a match
condition to specific RTSP methods. 

 ANNOUNCES DESCRIBE GET_PARAMETER OPTIONS PAUSE 

 PLAY RECORD REDIRECT SET_PARAMETER SETUP 

 SETUP_PARAMETER TEAR_DOWN UNKNOWN_METHOD 

 SMTP
Method Qualifiers 

 SMTP method qualifiers can be added
to custom signatures that use SMTP-related contexts to limit a match
condition to specific SMTP methods. 

 AUTH BDAT DATA EHLO HELO MAIL QUIT 

 RCPT RSET SAML SEND SOML STARTTLS UNKNOWN_CMD 

 USER VRFY XEXCH50 XEXPS XLINK2STATE XTELLMAIL 

 Previous 

 panav-rsp-zip-compression-ratio 

 Next 

 New Features in Advanced Threat Prevention 

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

 Endpoints 

 GlobalProtect 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 Reference 

 Custom Signatures 

 Advanced Threat Prevention 

 Threat Prevention 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
