---
url: https://docs.paloaltonetworks.com/panorama/administration/manage-firewalls
fetched_at: 2026-08-13T17:17:37Z
source: palo-alto-main
---

# Manage Firewalls with Panorama Clear

Manage Firewalls with Panorama 

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

 Manage Firewalls with Panorama 

 Updated on 

 Thu Jul 30 16:22:01 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Panorama Docs 

 Getting Started 

 Administration 

 New Features 

 Updated on 

 Thu Jul 30 16:22:01 PDT 2026 

 Focus 

 Home 

 Panorama 

 Manage Firewalls with Panorama 

 Download PDF 

 Panorama 

 Manage Firewalls with Panorama 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Panorama Docs 

 Getting Started 

 Administration 

 New Features 

 Previous 

 Change Certificates 

 Next 

 Add a Firewall as a Managed Device 

 Manage Firewalls with Panorama 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by Panorama) 

 Device Management License 

 Panorama superuser role 

 To use the Panorama™ management server for managing Palo Alto Networks firewalls, you must add
 the firewalls as managed devices and then assign them to device groups and to templates
 or template stacks. The following tasks best suit a first-time firewall deployment.
 Templates and template stacks are utilized to define and administer the common base
 network and device configurations that enable firewalls to operate seamlessly on the
 network. Meanwhile, device groups allow administrators to organize firewalls logically
 to centrally manage globally shared and local policy rules, control the precedence of
 inherited objects, and maintain a structured rule hierarchy. Managing firewalls involves
 a variety of deployment options, including setting up Zero Touch Provisioning (ZTP) to
 automate and simplify the onboarding of new branch firewalls directly from the internet
 after connecting to the ZTP service. 

 Administrators can also seamlessly transition existing locally-managed firewalls to
 Panorama management by importing their configurations, or change devices between
 Panorama management and cloud management as deployment needs evolve. 

 Panorama also provides robust device monitoring capabilities, allowing administrators to
 track device health metrics—such as session counts, data plane CPU utilization, logging
 rates, and environmental performance—and identify devices that deviate from baseline
 operational ranges. Furthermore, administrators can monitor policy rule usage to
 evaluate whether rules continue to match traffic enforcement needs, enabling the
 identification and cleanup of unused rules to reduce security risks. 

 To view the Objects and Policies tabs
on the Panorama web interface, you must first create at least one
device group. To view the Network and Device tabs,
you must create at least one template. These tabs contain the options
by which you configure and manage the firewalls on your network. 

 Before proceeding, review Plan Your Panorama Deployment to understand
 the deployment options 

 Previous 

 Change Certificates 

 Next 

 Add a Firewall as a Managed Device 

 On This Page 

 Activation and Onboarding 

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

 Panorama 

 Service Provider 

 VM-Series 

 Plugins 

 SASE 

 Prisma Access 

 Prisma SASE Multitenant Platform 

 AI-Powered ADEM 

 Prisma Access Monitoring & Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

 Cloud-Delivered Security Services 

 Advanced WildFire 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 AI Access Security 

 Device Security 

 Enterprise DLP 

 SaaS Security 

 Network Security 

 Shared Policy for NGFWs and Prisma Access 

 IPSec VPN 

 Security Policy 

 Quantum Security 

 Endpoints 

 GlobalProtect 

 Remote Browser Isolation 

 Prisma Access Agent 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 FedRAMP 

 Prisma SASE for FedRAMP 

 Autonomous DEM for FedRAMP 

 Prisma SD-WAN Experts Corner 

 Network Policy 

 QoS Whitepaper 

 Security Architecture Whitepaper 

 External Antennas for ION-C Series 

 Dynamic Path Selection 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Resources 

 All Products A - Z 

 All Release Notes 

 Compatibility Matrix 

 Experts Corner 

 Network Security Platform 

 Security Policy 

 Decryption 

 Device-ID 

 IPSec VPN 

 Quality of Service 

 Quantum Security 

 11.1 & Later 

 Next-Generation Firewall 

 Administration 

 Panorama 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
