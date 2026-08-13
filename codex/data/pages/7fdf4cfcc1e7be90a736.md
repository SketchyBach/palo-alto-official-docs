---
url: https://docs.paloaltonetworks.com/cloud-ngfw-aws/administration/protect/cloud-ngfw-native-policy-management/x-forwarded-for
fetched_at: 2026-08-13T15:30:52Z
source: palo-alto-main
---

# X-Forwarded-For on Cloud NGFW for AWS Clear

X-Forwarded-For on Cloud NGFW for AWS 

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

 X-Forwarded-For on Cloud NGFW for AWS 

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

 X-Forwarded-For on Cloud NGFW for AWS 

 Download PDF 

 English 

 日本語 (Japanese) 

 Français (French) 

 Deutsch (German) 

 Cloud NGFW for AWS 

 X-Forwarded-For on Cloud NGFW for AWS 

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

 Rulestacks and Rules on Cloud NGFW for AWS 

 Next 

 Create a Prefix List on Cloud NGFW for AWS 

 X-Forwarded-For on Cloud NGFW for AWS 

 Learn how ingress traffic to your applications passes through AWS load balancers or
 proxy servers before it reaches the NGFW. 

 Where Can I Use This? What Do I Need? 

 Cloud NGFW for AWS 

 Cloud NGFW subscription 

 Palo Alto Networks Customer Support Account (CSP) 

 AWS Marketplace account 

 User role (either tenant or administrator) 

 The ingress traffic to your applications might pass through AWS load balancers or proxy
 servers before it reaches the NGFW. Because these devices intercept traffic between the
 source and destination, the NGFW sees the IP address of the load balancer or proxy
 server instead of the IP address of the source. These devices add the X-Forwarded-For
 (XFF) header to HTTP requests and add the actual IPv4 or IPv6 address of the client
 accessing your application. 

 Traffic to your applications might have passed more than one proxy server before it
 reaches the NGFW. The XFF request header might contain multiple IP addresses that are
 separated by commas. NGFW always uses the most recently added address in the XFF header
 to enforce policy. 

 When configuring the rulestack , you can enable
 Cloud NGFW to use the source IP address in an XFF HTTP header field to enforce security
 policy. 

 Previous 

 Rulestacks and Rules on Cloud NGFW for AWS 

 Next 

 Create a Prefix List on Cloud NGFW for AWS 

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
