---
url: https://docs.paloaltonetworks.com/cloud-ngfw-aws/administration/protect/cloud-ngfw-native-policy-management
fetched_at: 2026-08-13T15:30:46Z
source: palo-alto-main
---

# Cloud NGFW Native Policy Management Clear

Cloud NGFW Native Policy Management 

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

 Cloud NGFW Native Policy Management 

 Updated on 

 Tue May 19 03:36:42 PDT 2026 

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

 Tue May 19 03:36:42 PDT 2026 

 Focus 

 Home 

 Cloud NGFW for AWS 

 Cloud NGFW for AWS Administration 

 Protect 

 Cloud NGFW Native Policy Management 

 Download PDF 

 English 

 日本語 (Japanese) 

 Français (French) 

 Deutsch (German) 

 Cloud NGFW for AWS 

 Cloud NGFW Native Policy Management 

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

 Cloud NGFW for AWS Enterprise Data Loss Prevention (E-DLP) Integration 

 Next 

 Rulestacks and Rules on Cloud NGFW for AWS 

 Cloud NGFW Native Policy Management 

 Learn about Cloud NGFW for AWS native policy management. 

 Where Can I Use This? What Do I Need? 

 Cloud NGFW for AWS 

 Cloud NGFW subscription 

 Palo Alto Networks Customer Support Account (CSP) 

 AWS Marketplace account 

 User role (either tenant or administrator) 

 On Cloud NGFW, you define Security policy rules and group those rules together in a
 rulestack. 

 While Security policy rules enable you to allow or block traffic on your
 network, Security Profiles help you define an allow but scan rule,
 which scans allowed applications for threats, such as malware, spyware, and DDoS
 attacks. When traffic matches the allow rule defined in the Security
 policy rule, the Security Profiles attached to the rule are applied for further content
 inspection rules such as antivirus checks and data filtering. 

 Security Profiles are not used in the match criteria of a traffic flow. The
 Security Profile is applied to scan traffic after the Security policy rule allows the
 application or category. 

 The firewall provides default Security Profiles that you can use out of the box
 to begin protecting your network from threats. See Set Up a Basic Security Policy for information
 on using the default profiles in your Security policy rule. 

 For recommendations on the best practice settings for Security Profiles, review
 the best practices for creating security
 profiles . 

 You can add Security Profiles that are commonly applied together to Create a Security Profile Group ; this set of
 profiles are treated as a unit and added to Security policy rules in one step (or
 included in Security policy rules by default, if you choose to set up a default Security
 Profile Group). 

 Security profiles provide fundamental
 protections by scanning traffic that you allow on the network for threats. Security
 Profiles provide a full suite of coordinated threat prevention tools that block
 peer-to-peer command and control (C2) application traffic, dangerous file types,
 attempts to exploit vulnerabilities, and antivirus signatures, and also identify new and
 unknown malware. 

 It takes relatively little effort to apply Security Profiles because Palo Alto
 Networks provides predefined profiles that you can simply add to Security policy allow
 rules. Customizing Security Profiles is easy because you can clone a predefined profile
 and then edit it. You can also create a Security Profile from scratch on the firewall or
 on Panorama. 

 To detect known and unknown threats in your network traffic, attach Security
 Profiles to all Security policy rules that allow traffic on the network, so that the
 firewall inspects all allowed traffic. The firewall applies Security Profiles to traffic
 that matches the Security policy allow rule, scans traffic in accordance with the
 Security Profile settings, and then takes appropriate actions to protect the network.
 The recommendations for best practice Security Profiles apply to all four of the data
 center traffic flows except as noted. 

 Download content updates automatically and install
 them as soon as possible so that you have the latest threat prevention signatures
 and content (antivirus, antispyware, vulnerabilities, malware, etc.) on the firewall
 and block the latest threats. 

 Previous 

 Cloud NGFW for AWS Enterprise Data Loss Prevention (E-DLP) Integration 

 Next 

 Rulestacks and Rules on Cloud NGFW for AWS 

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
