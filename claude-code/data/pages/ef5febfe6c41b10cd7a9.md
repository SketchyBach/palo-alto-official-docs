---
url: https://docs.paloaltonetworks.com/network-security/security-policy/administration/security-profiles/ai-security-profile
fetched_at: 2026-08-12T14:07:59Z
source: strata-and-sase
---

# Security Profile: AI Security Clear

Security Profile: AI Security 

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

 Security Profile: AI Security 

 Updated on 

 Aug 5, 2026 

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

 Aug 5, 2026 

 Focus 

 Home 

 Network Security 

 Network Security: Security Policy 

 Security Profiles 

 Security Profile: AI Security 

 Download PDF 

 Network Security 

 Security Profile: AI Security 

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

 Security Profile Groups 

 Next 

 Security Profile: WildFire® Analysis 

 Security Profile: AI Security 

 The page helps you to create an AI security profile in Strata Cloud Manager . 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by Strata Cloud Manager) 

 Prisma AIRS AI Runtime Security 

 Prisma AIRS AI Runtime
 Licenses 

 Deploy Prisma AIRS : Network intercept
 managed by Strata Cloud Manager or Panorama 

 This page helps you to create an AI security profile and associate this
 profile with a security policy to monitor the AI traffic passing through the Prisma AIRS AI Runtime: Network intercept. 

 An AI security profile protects AI traffic and is only available for Prisma AIRS : Network intercept firewalls. 

 The AI security profile helps you to configure specific protections to
 protect your cloud network architecture. This profile can only be configured from
 Strata Cloud Manager and Panorama . See AI Runtime Security: Network intercept for details. 

 The Prisma AIRS : Network intercept monitors the AI
 and non-AI traffic against AI security policy rules and reduces the security risks
 that surface during interactions with AI models. 

 An AI security profile helps you to configure: 
 AI application protection with protections like AI URL
 categorization 

 AI model protection to protect your AI models against threats such
 as prompt injections 

 AI data protection to protect against for example; sensitive data leakage to
 and from AI models 

 To create an AI security profile: 

 Log in to Strata Cloud Manager . 

 Go to Manage > Configuration > NGFW and Prisma Access > Security
 Services > AI Security . 

 The AI security profile will be available at the
 folder/snippet/device level for all devices. 

 Select the Configuration Scope as Global or limit it to your AI
 security profile. 

 Select AI Security and Add Profile . 

 Enter a Name and a Description . 

 Add Model Group for customized protections including AI application
 protection, AI data protection, and AI model protection. See Create Model Groups for Customized
 Protections . 

 Set the Max Inline Latency for AI Security detection runtime latency (#
 milliseconds) for traffic that hits a specific AI security profile. 

 Select Save to create the profile. 

 In the Profile Usage section, you can see the profile groups to which
 this AI security profile is currently attached. You have the option to add this
 security profile to additional profile groups, clone a profile group, or remove
 the security profile from any existing profile group. This section also details
 the security policy rules associated with the AI security profile. 

 Next, set up security rules and link the AI security profile to enforce these
 protections on the traffic. 

 Previous 

 Security Profile Groups 

 Next 

 Security Profile: WildFire® Analysis 

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

 Network Security 

 Security Policy 

 Strata Cloud Manager 

 Security Policy 

 Prisma AIRS 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
