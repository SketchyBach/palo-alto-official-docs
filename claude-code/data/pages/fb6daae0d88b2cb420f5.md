---
url: https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/decryption/troubleshoot-and-monitor-decryption/decryption-troubleshooting-workflow-examples/troubleshoot-revoked-certificates
fetched_at: 2026-09-16T07:38:40Z
source: palo-alto-main
---

# Troubleshoot Revoked Certificates Clear

Updated on 

 Fri Mar 13 14:52:24 PDT 2026 

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
