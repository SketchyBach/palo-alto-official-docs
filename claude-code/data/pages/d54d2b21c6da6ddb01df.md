---
url: https://docs.paloaltonetworks.com/cloud-ngfw-aws/administration/protect/cloud-ngfw-native-policy-management/security-profiles/setup-ingress-decryption
fetched_at: 2026-08-13T15:35:02Z
source: palo-alto-main
---

# Set Up Inbound Decryption on Cloud NGFW for AWS Clear

Set Up Inbound Decryption on Cloud NGFW for AWS 

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

 Set Up Inbound Decryption on Cloud NGFW for AWS 

 Updated on 

 May 19, 2026 

 Focus 

 Download PDF 

 English 

 日本語 (Japanese) 

 Français (French) 

 Deutsch (German) 

 Filter

 Expand All 
 | 
 Collapse All 

 Cloud NGFW for AWS Docs 

 Getting Started 

 Deployment 

 Administration 

 Reference 

 Release Notes 

 New Features 

 Updated on 

 May 19, 2026 

 Focus 

 Home 

 Cloud NGFW for AWS 

 Cloud NGFW for AWS Administration 

 Protect 

 Cloud NGFW Native Policy Management 

 Cloud NGFW for AWS Security Profiles 

 Set Up Inbound Decryption on Cloud NGFW for AWS 

 Download PDF 

 English 

 日本語 (Japanese) 

 Français (French) 

 Deutsch (German) 

 Cloud NGFW for AWS 

 Set Up Inbound Decryption on Cloud NGFW for AWS 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Cloud NGFW for AWS Docs 

 Getting Started 

 Deployment 

 Administration 

 Reference 

 Release Notes 

 New Features 

 Previous 

 Set Up Outbound Decryption on Cloud NGFW for AWS 

 Next 

 Cloud NGFW for AWS Rule Usage 

 Set Up Inbound Decryption on Cloud NGFW for AWS 

 Learn how to configure ingress decryption on Cloud NGFW for AWS. 

 Where Can I Use This? What Do I Need? 

 Cloud NGFW for AWS 

 Cloud NGFW subscription 

 Palo Alto Networks Customer Support Account (CSP) 

 AWS Marketplace account 

 User role (either tenant or administrator) 

 Cloud NGFW uses SSL Inbound Decryption to inspect and
 decrypt inbound SSL/TLS traffic from a client to a targeted network server (any
 server you have the certificate for and can import onto the firewall) and block
 suspicious sessions. The firewall acts as a proxy between the external client and
 the internal server and generates a new session key for each secure session. The
 firewall creates a secure session between the client and the firewall and another
 secure session between the firewall and the server to decrypt and inspect the
 traffic. However, Cloud NGFW keeps your traffic packet headers and payload intact,
 providing complete visibility of the source’s identity to your applications in your
 VPCs. 

 Your certificate and session keys are stored on
 the AWS secrets manager to perform SSL Inbound
 Inspection . The firewall validates that the certificate sent by the targeted server
 during the SSL/TLS handshake matches a certificate in your decryption policy rule.
 If there is a match, the firewall forwards the server's certificate to the client
 requesting server access and establishes a secure connection. 

 Select Rulestacks and select a previously created
 rulestack, which to apply the certificate. 

 Select Rules , then Create a new
 Security Rule for decryption. 

 Provide the following details under General . 
 Name —Name of the rule. 

 Description —A description for the rule. 

 Rule Priority —A unique priority for the
 rule. 

 Enabled —Enable the field to associate the
 rulestack with the rule. This field is enabled by default. 

 Define matching criteria for the Source and
 Destination IP address fields. 

 Configure Granular Controls . 
 Specify the Applications(App-ID) you want the
 rule to allow or block. 

 You can create TLS
 decryption rules with
 Applications(App-ID) — Any 
 or SSL — Match 
 only. 

 Specify a URL Category as the match criteria for
 the rule. 

 Specify the Protocol and Ports you want the rule
 to allow or block. 

 Specify the Action you want the firewall to take when
 the traffic matches one of the rules you created. 
 Allow —Allow traffic. 

 Deny —Block traffic and enforce the default
 Deny Action defined for the application that’s being
 denied. 

 Reset Server —Sends the TCP reset to the
 server-side device. 

 Reset Both —Sends a TCP reset to both client and
 server-side devices. 

 Under TLS Decryption , select
 Inbound and select an Inbound Inspection
 Certificate . 

 Create a certificate if you have not done so already. The Amazon
 Resource Name (ARN) of the secret must be used in the certificate ARN when
 creating the certificate object. 

 The certificate and private key are stored in the AWS Secrets Manager (ASM),
 and the application load balancer (ALB) uses these information to decrypt
 the traffic. The certificate need not be a CA certificate. If the
 certificate is a chain, use the leaf certificate and key. 

 PKCS8 is the supported certificate
 format. 

 Inbound decryption does not support self-signed
 certificates. 

 The decryption profile for TLS decryption is set to
 best practice Security policy. See decrypt traffic for full visibility and
 threat inspection for more information. 

 Click Enabled to enable logging. 

 Click Save . 

 Click Config Actions Deploy Configuration Commit to save the rule to the running configuration the firewall. 

 Previous 

 Set Up Outbound Decryption on Cloud NGFW for AWS 

 Next 

 Cloud NGFW for AWS Rule Usage 

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

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 Service Provider 

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

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Cloud NGFW for AWS 

 Administration 

 AWS 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
