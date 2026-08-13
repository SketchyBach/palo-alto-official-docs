---
url: https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/decryption/troubleshoot-and-monitor-decryption/decryption-troubleshooting-workflow-examples/troubleshoot-revoked-certificates
fetched_at: 2026-08-13T17:08:57Z
source: palo-alto-main
---

# Troubleshoot Revoked Certificates Clear

Troubleshoot Revoked Certificates 

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

 Troubleshoot Revoked Certificates 

 Updated on 

 Mar 13, 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Network Security Docs 

 Security Policy 

 IPsec VPN 

 Decryption 

 Device-ID 

 Quantum Security 

 Quality of Service 

 Updated on 

 Mar 13, 2026 

 Focus 

 Home 

 Network Security 

 Troubleshoot Decryption 

 Troubleshoot Revoked Certificates 

 Download PDF 

 Network Security 

 Troubleshoot Revoked Certificates 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Network Security Docs 

 Security Policy 

 IPsec VPN 

 Decryption 

 Device-ID 

 Quantum Security 

 Quality of Service 

 Previous 

 Troubleshoot Expired Certificates 

 Next 

 Device-ID Overview 

 Troubleshoot Revoked Certificates 

 Find sites that have revoked certificates so you can make informed decisions about
 allowed traffic. 

 Where Can I Use
 This? What Do I Need? 

 All NGFW deployments, including those funded
 by software NGFW
 credits 

 All Prisma Access deployments 

 No separate license required for decryption when using NGFWs or
 Prisma Access . 

 Note: The features and capabilities available to you in
 Strata Cloud Manager depend on your active license(s) . 

 A revoked certificate is no longer valid. It may indicate that there are
 security issues with a site and that the certificate is not trustworthy, although
 there are also benign reasons why a certificate may be revoked. 

 Don’t trust revoked certificates; enable certificate revocation
 checking to deny access to sites with revoked certificates. 

 To drop
 sessions with revoked certificates and troubleshoot revoked certificates, enable
 certificate revocation checking. If you don’t enable certificate revocation checking, the NGFW
 doesn’t check for revoked certificates and you won’t know if a site has a revoked
 certificate. 

 Strata Cloud Manager 

 PAN-OS & Panorama 

 Troubleshoot Revoked Certificates ( Strata Cloud Manager ) 

 Before you begin this task, enable certificate revocation checks using OCSP
 and CRL if you haven't already. 

 Filter the decryption logs for certificate revocation errors. 

 Select Log
 Viewer , and then select
 Firewall/Decryption . 

 In the search field, enter the following query: Error
 Message = ‘OCSP/CRL check: certificate revoked’ . 

 ( Optional ) Double-check the certificate expiration date at the Qualys
 SSL Labs site. 

 Enter the hostname of the server ( Server Name
 Identification column of the decryption log) in the
 Hostname field and Submit 
 it to view certificate information for the host. 

 Troubleshoot Revoked Certificates ( PAN-OS ) 

 Enable certificate revocation checking if you haven’t already enabled it. 

 Go to Device Setup Session Decryption Settings . 

 Enable both OCSP and CRL certificate checking. 

 If you Block sessions on certificate status check
 timeout in the Forward Proxy Decryption profile and
 are concerned that 5 seconds is not enough time and may result in
 too many sessions blocked by timeouts, set the Receive
 Timeout (sec) to a longer amount of time. 

 Filter the Decryption log ( Monitor Logs Decryption ) to find certificate revocation errors using the query
 (error eq ‘OCSP/CRL check: certificate
 revoked’) . 

 ( Optional ) Double-check the certificate expiration date at the Qualys
 SSL Labs site. 

 Enter the hostname of the server ( Server Name
 Identification column of the Decryption log) in the
 Hostname field and Submit 
 it to view certificate information for the host. 

 Previous 

 Troubleshoot Expired Certificates 

 Next 

 Device-ID Overview 

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

 Decryption 

 Network Security 

 PAN-OS 

 Next-Generation Firewall 

 Decryption 

 English 

 Strata Cloud Manager 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
