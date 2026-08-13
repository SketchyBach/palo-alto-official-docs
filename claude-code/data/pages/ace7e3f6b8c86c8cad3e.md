---
url: https://docs.paloaltonetworks.com/network-security/decryption/administration/troubleshooting-decryption/troubleshoot-version-errors
fetched_at: 2026-08-13T16:38:13Z
source: palo-alto-main
---

# Troubleshoot Version Errors Clear

Troubleshoot Version Errors 

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

 Troubleshoot Version Errors 

 Updated on 

 Fri Mar 13 14:52:24 PDT 2026 

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

 Fri Mar 13 14:52:24 PDT 2026 

 Focus 

 Home 

 Network Security 

 Troubleshoot Decryption 

 Troubleshoot Version Errors 

 Download PDF 

 Network Security 

 Troubleshoot Version Errors 

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

 Identify Weak Protocols and Cipher Suites 

 Next 

 Troubleshoot Unsupported Cipher Suites 

 Troubleshoot Version Errors 

 Identify and fix version errors in various ways. 

 Where Can I Use
 This? What Do I Need? 

 Prisma Access (Managed by Panorama) 

 NGFW (Managed by PAN-OS or Panorama) 

 For Prisma Access (Managed by Panorama) : 

 A Prisma Access
 license 

 Cloud Services
 plugin for Panorama 

 If you're using a NGFW (Managed by PAN-OS or Panorama) ,
 no other requirements. 

 Version errors arise when there are mismatches between the TLS protocol versions that
 the client and server use or between the TLS protocol versions that the client and
 the Decryption profile applied to the traffic use. The error messages includes
 bitmask values that identify the supported client and Decryption profile versions.
 You can use these values to identify the cipher the client tried to use and the
 cipher values that the Decryption profile supports. The CLI command to convert
 version error bitmasks is: debug dataplane show ssl-decrypt
 bitmask-version <bitmask-value> . For more information and
 remediation, see Decryption Log Errors and Error Indexes . 

 Key Steps for Converting Bitmask Values and Turning Them Into Something
 Useful 

 Filter the Decryption logs for version errors using a query. 

 Plug the bitmask value into the appropriate CLI command to identify the
 protocol versions that caused the error. 

 Use the cipher information to update the Decryption profile if you want to
 allow access to the site in question. 

 Identify version errors in the decryption logs. 

 Select Monitor Logs Decryption . 

 Filter decryption logs using the following queries: 

 To find all instances where the error is related to protocol
 versions : (err_index eq
 Version) . The highlighted values are bitmask
 values. 

 Error Index = Version 

 To find all instances where the protocol versions supported
 by the client and in the Decryption profile attached to the
 policy rule don't match: (error contains ‘Client
 and decrypt profile mismatch’) . 

 Error contains 'client and decrypt profile version
 mismatch' 

 You can filter decryption logs in many ways. 

 For example, to see only TLSv1.3 version errors, specify the error index and
 the TLS version you're looking for in the query as follows:
 (err_index eq Version) and (tls_version eq
 TLS1.3) . 

 To find all decryption sessions that experienced the same error, click an
 error message to add it to the query and remove the original query, for
 example: 

 The hexadecimal codes or bitmasks identify the exact version that the client
 supports and the exact version that the Decryption profile supports. 

 Log in to the CLI to look up the
 bitmask values. 

 To identify the TLS versions that a bitmask corresponds to, use the
 debug dataplane show ssl-decrypt bitmask-version
 < bitmask-value > CLI
 command. 

 Example screens of this lookup: 

 Example 1 (first screenshot) 

 The version errors in the first screenshot (the same errors for all
 three sessions) show an issue with a client and Decryption profile
 mismatch. The version supported by the client is represented by the
 0x08 bitmask and the version
 supported in the Decryption profile bitmask is
 0x70 . 

 admin@vm1> debug dataplane show ssl-decrypt bitmask-version 0x08 
 TLSv1.0 

 This output shows that the client supports only TLSv1.0. 

 admin@vm1> debug dataplane show ssl-decrypt bitmask-version 0x70 
 TLSv1.1 
 TSLv1.2 
 TLSv1.3 

 This output shows that the Decryption profile supports
 TLSv1.1, TLSv1.2, and TLSv1.3, but not TLSv1.0. Now you know
 the issue is that the client only supports an older version
 of the TLS protocol and the Decryption profile attached to
 the decryption policy rule that controls the traffic does
 not allow TLSv1.0 traffic. 

 Example 2 (third screenshot) 

 The version error in the second screenshot shows a different issue: a
 client and server version mismatch. The error indicates the
 supported client bitmask as 0x20 : 

 admin@vm1> debug dataplane show ssl-decrypt bitmask-version 0x20 
 TLSv1.2 

 The output shows that the client supports only TLSv1.2, which means
 that the server doesn't support this version. The server might only
 support TLSv1.3 or it might support only TLSv1.1 or lower (less
 secure protocols). 

 Decide what action to take. 

 How you fix this error depends on the TLS versions supported by the client
 and server and your business needs. 

 Evaluate if you need access to the server for business or another
 important purpose. 

 Confirm the TLS versions that the server supports. You can use
 Wireshark or another packet analysis tool to find out which TLS
 versions the server supports. 

 You could update the client or server to support a stronger
 version. 

 If the client only supports a weaker TLS version, and cannot 
 support a more secure protocol, as in Example 1, you can: 

 Let the NGFW continue to block the traffic. 

 ( Not Recommended ) Update the Decryption
 profile to allow certain TLS traffic. Continue to step
 4 . This option allows traffic of a specific TLS
 version when it matches the decryption policy rules that the
 profile is attached to, which is why it's not
 recommended. 

 Don't allow access to all
 servers that use less secure TLS versions. Create more
 specific rules for cases like this. 

 This may be a good course of action
 in a case like Example 2, where the server supports a more
 secure TLS protocol than the client. Then, you'd be updating
 the client so that it accepts a more secure TLS version,
 which is good for security. 

 ( Most Secure option ) Configure a Decryption
 profile that allows the weaker TLS version, but apply
 it to a decryption policy rule 
 for the particular server that controls the sites, user, device,
 or source address (and to any similar users, devices, or source
 addresses so that one policy rule and profile control all of
 this traffic) that must use this server. 

 Identify and modify the Decryption profile associated with the policy rule that
 controls the session traffic. 

 Identify the decryption policy rule that control the session
 traffic. 

 Check the Policy Name column in the log
 (or click the magnifying glass 

 next to a Decryption log entry to
 see the information in the General section of the Detailed Log
 View). 

 Select Policies Decryption . Then, select the policy rule with the Policy
 Name above. In the examples, the policy rule is Big
 Brother. 

 Identify the Decryption profile. 
 Select the Options tab. Decryption
 profile displays the name of the Decryption
 profile. 

 Edit the protocol versions supported in the Decryption profile. 

 Select Objects Decryption Decryption Profile , and select the appropriate Decryption
 profile. 

 Select SSL Decryption SSL Protocol Settings , and then select the Min
 Version and Max
 Version that you need. 

 Click OK . 

 Commit your changes. 

 Previous 

 Identify Weak Protocols and Cipher Suites 

 Next 

 Troubleshoot Unsupported Cipher Suites 

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
