---
url: https://docs.paloaltonetworks.com/cloud-ngfw-aws/administration/deploy-and-configure
fetched_at: 2026-08-13T15:30:36Z
source: palo-alto-main
---

# Deploy Clear

Deploy 

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

 Deploy 

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

 Deploy 

 Download PDF 

 English 

 日本語 (Japanese) 

 Français (French) 

 Deutsch (German) 

 Cloud NGFW for AWS 

 Deploy 

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

 Usage Explorer 

 Next 

 Deploy in Cloud NGFW Console 

 Deploy 

 Learn about the different options for deploying and managing Cloud NGFW for
 AWS. 

 Where Can I Use This? What Do I Need? 

 Cloud NGFW for AWS 

 Cloud NGFW subscription 

 Palo Alto Networks Customer Support Account (CSP) 

 AWS Marketplace account 

 User role (either tenant or administrator) 

 Cloud NGFW for AWS offers multiple options for deploying NGFW resources and managing
 Security policy rules. 

 NGFW Deployment and Management 

 Native NGFW Deployment —When you subscribe to Cloud NGFW via AWS
 Marketplace, you procure a tenant. You can then deploy Cloud NGFW resources
 for your VPCs with a few clicks on the Cloud NGFW
 Console or using APIs . These resources come with
 built-in resilience, scalability, and lifecycle management. You can also use
 infrastructure as code tools such as Cloud
 Formation or Terraform for creating these resources. Once created, you can
 author Security policy rules for these Cloud NGFW resources using Native
 policy management (rulestacks) or using Panorama policy management (device
 groups). 

 AWS Firewall Manager Deployment —If you currently use AWS Firewall
 Manager to manage security groups, or other network security features across
 your AWS organization, You can use the same AWS Firewall Manager to deploy
 NGFWs into multiple accounts and VPCs throughout an AWS organization. You
 can use the AWS Console , AWS APIs , or Cloud Formation to author the
 Firewall Manager policy configuration that deploys and manages all Cloud
 NGFW settings. 

 AWS Firewall Manager also manages the endpoint subnets, route tables, and
 gateway load-balancer endpoints within the VPC where the Cloud NGFW resource
 is deployed. When you use AWS Firewall Manager, the Cloud NGFW resource uses
 global rulestacks in your Cloud NGFW tenant for the security settings and
 rules. If you have not previously configured a global rulestack in your
 tenant (using Panorama policy management), AWS Firewall Manager redirects
 you to the Cloud NGFW console to create and manage the global rulestack
 using native policy management. 

 Security Policy Management 

 Native policy Management— You can manage Security policy rules on the
 Cloud NGFW resources by authoring Rulestacks natively using the Cloud NGFW Console or APIs . You can also use
 infrastructure as code tools such as Cloud Formation or Terraform for creating these
 rulestacks. A rulestack defines the advanced access control (App-ID, URL
 Filtering) and threat prevention behavior of the NGFW. A rulestack includes
 a set of security rules and the associated objects and Security Profiles. 

 Panorama policy Management —You can link your Cloud NGFW tenant with a
 Panorama appliance to author and manage policy rules for your Cloud NGFW
 resources. You can use Panorama Console , APIs , or Terraform to author these Security
 policy rules on the Cloud device groups. The policy you author in the
 Panorama Cloud device group manifests as global rulestacks in your Cloud
 NGFW tenant. 

 Strata Cloud Manager policy Management —Strata Cloud Manager provides
 unified management for your entire network security deployment, which allows
 you to easily manage your Palo Alto Networks security infrastructure from a
 single, streamlined web interface. With this interface you gain
 comprehensive visibility into users, branch sites, applications, and threats
 across all network security enforcement points. This functionality provides
 actionable insights, better security, and easy troubleshooting and problem
 resolution. 

 Previous 

 Usage Explorer 

 Next 

 Deploy in Cloud NGFW Console 

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
