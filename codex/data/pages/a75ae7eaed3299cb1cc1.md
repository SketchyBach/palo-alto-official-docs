---
url: https://docs.paloaltonetworks.com/network-security/security-policy/administration/objects/external-dynamic-lists/configure-the-firewall-to-access-an-external-dynamic-list-from-the-edl-hosting-service/create-an-external-dynamic-list-using-the-edl-hosting-service-cloud-management
fetched_at: 2026-09-16T12:58:12Z
source: palo-alto-main
---

# Create an External Dynamic List Using the EDL Hosting Service (Strata Cloud
        Manager) Clear

Updated on 

 Fri Aug 07 10:46:39 PDT 2026 

 Focus 

 Home 

 Network Security 

 Network Security: Security Policy 

 Policy Objects 

 Policy Object: External Dynamic Lists 

 Configure your Environment to Access an External Dynamic List from the EDL Hosting
 Service 

 Create an External Dynamic List Using the EDL Hosting Service (Strata Cloud
 Manager) 

 Download PDF 

 Network Security 

 Create an External Dynamic List Using the EDL Hosting Service (Strata Cloud
 Manager) 

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

 Create an External Dynamic List Using the EDL Hosting Service (Strata Cloud
 Manager) 

 Leveraging a Feed URL as the source in an EDL allows for dynamic enforcement of SaaS
 application traffic without the need for you to host and maintain your own EDL source. 

 Visit the EDL Hosting Service and identify the
 Feed URL for your SaaS application. 

 Review the Microsoft 365 documentation for
 more information which Feed URL is best for your use case. Additionally,
 consider the SaaS application and location of users accessing the SaaS
 application when identifying a Feed URL to. For example, if you have a
 branch in Germany that only needs to access Exchange Online, select a Feed
 URL from the Service Area: Exchange Online for
 Germany . 

 For a policy-based forwarding policy
 rule, use an IP-based Feed URL. 

 ( Best Practices ) Create a certificate profile to authenticate the EDL
 Hosting Service. 

 Download the GlobalSign Root R1
 certificate . 

 Convert the GlobalSign Root R1 Certificate to PEM Format . 

 Import the GlobalSign Root R1 certificate. 

 Select Configuration NGFW and Prisma Access Objects Certificate Management Custom Certificates and Import a new
 custom certificate. 

 Enter a descriptive Certificate
 Name . 

 For the Certificate File , select
 Browse and select the certificate
 you converted in the previous step. 

 For the Format , select
 Base64 Encoded Certificate
 (PEM) . 

 Select Save . 

 Create a certificate authority (CA) certificate profile. 

 Select Configuration NGFW and Prisma Access Objects Certificate Management Certificate Profiles and Add Profile . 

 Enter a descriptive Name . 

 For the CA Certificates ,
 Add the certificate you imported
 in the previous step. 

 Select Save . 

 Select Push Config . 

 Create an EDL using a Feed URL from the EDL Hosting Service. 

 Select Configuration NGFW and Prisma Access Objects External Dynamic Lists and Add External Dynamic
 List . 

 Enter a descriptive Name for the EDL. 

 Select the EDL Type . 

 For an IP-based EDL, select IP
 List . 

 For a URL-based EDL, select URL
 List . 

 ( Optional ) Enter a Description for the
 EDL 

 Enter the Feed URL as the EDL Source . 

 Enforce all endpoints within a specific Feed URL. Adding an
 excluding a specific endpoint from a Feed URL can cause
 connectivity issues to the SaaS application. 

 ( Best Practices ) Select the Certificate
 Profile you created in the previous step. 

 Specify the frequency your environment should Check for
 updates to match the update frequency of the Feed
 URL. 

 For example, if the Feed URL is updated daily by Palo Alto Networks
 then configure the EDL to check for updates
 Daily . 

 Palo Alto Networks displays the update frequency for each Feed URL in
 the EDL Hosting Service . Feed
 URLs are automatically updated with any new endpoints. 

 Select Save . 

 Enforce Policy on an External Dynamic List . 

 When you enforce policy on an EDL from the EDL Hosting Service where the EDL
 is the source, be specific when configuring which users have access to the
 SaaS application to avoid over-provisioning access to the application. 

 Leverage App-ID alongside EDLs in a
 security rule for additional strict enforcement of SaaS application
 traffic.
