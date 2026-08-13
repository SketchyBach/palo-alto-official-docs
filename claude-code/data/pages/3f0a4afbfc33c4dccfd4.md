---
url: https://docs.paloaltonetworks.com/ngfw/networking/about-auto-vpn/refresh-a-pre-shared-key
fetched_at: 2026-08-13T16:53:40Z
source: palo-alto-main
---

# Refresh a Pre-Shared Key Clear

Refresh a Pre-Shared Key 

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

 Refresh a Pre-Shared Key 

 Updated on 

 Tue Aug 04 17:04:37 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Generation Firewall Docs 

 Getting Started 

 Administration 

 Networking 

 Quick Start 

 Reference 

 Incidents & Alerts 

 Release Notes 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 11.0 (EoL) 

 PAN-OS 10.2 

 PAN-OS 10.1 (EoL) 

 PAN-OS 10.0 (EoL) 

 PAN-OS 9.1 (EoL) 

 PAN-OS 9.0 (EoL) 

 PAN-OS 8.1 (EoL) 

 Help 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 10.2 

 PAN-OS 10.1 

 New Features 

 Updated on 

 Tue Aug 04 17:04:37 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 Auto VPN 

 Refresh a Pre-Shared Key 

 Download PDF 

 Next-Generation Firewall 

 Refresh a Pre-Shared Key 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Generation Firewall Docs 

 Getting Started 

 Administration 

 Networking 

 Quick Start 

 Reference 

 Incidents & Alerts 

 Release Notes 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 11.0 (EoL) 

 PAN-OS 10.2 

 PAN-OS 10.1 (EoL) 

 PAN-OS 10.0 (EoL) 

 PAN-OS 9.1 (EoL) 

 PAN-OS 9.0 (EoL) 

 PAN-OS 8.1 (EoL) 

 Help 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 10.2 

 PAN-OS 10.1 

 New Features 

 Previous 

 Configure Auto VPN 

 Next 

 Fail Open 

 Refresh a Pre-Shared Key 

 Refresh the Pre-Shared Key for an Auto VPN cluster on Strata Cloud Manager . 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by Strata Cloud Manager 

 One of these licenses: 

 Strata Cloud Manager Essentials 

 Strata Cloud Manager Pro 

 Auto
 VPN allows you to configure secure connectivity between your managed
 firewalls using SD-WAN. Peers in the VPN cluster use a pre-shared key to mutually
 authenticate each other. To strengthen your security posture, Palo Alto Networks
 recommends refreshing the pre-shared keys used for authenticating VPN tunnels for
 existing VPN clusters periodically to ensure your VPN tunnels are not
 compromised. 

 Refreshing the pre-shared key may cause a temporary service disruption. To avoid
 impact to your business, Palo Alto Networks recommends scheduling a maintenance
 window to ensure you can resolve and service disruption issues outsides of
 business hours. 

 Log in to Strata Cloud Manager . 

 Configure Auto VPN . 

 Select Manage Configuration NGFW and Prisma Access Overview Configuration NGFW and Prisma Access Setup and select the Global configuration
 scope. 

 Select Global Settings Auto VPN VPN Clusters Auto VPN VPN Clusters . 

 Locate the VPN cluster for which you want to refresh the pre-shared key. 

 In the Pre-Shared Key Generated Data column, click
 Refresh Key . 
 A new Config Push to Redresh the Pre-Shared Key is
 displayed. 

 Check Acknowledge the possible service disruption . 

 You are prompted that refreshing the pre-shared key may cause a service
 disruption as the new pre-shared key generates a new security association
 (SA) for all SD-WAN firewalls in the VPN cluster. You must acknowledge the
 possibility of a service disruption due to refreshing the pre-shared key to
 continue. 

 Push . 

 Previous 

 Configure Auto VPN 

 Next 

 Fail Open 

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

 PAN-OS 

 Next-Generation Firewall 

 Networking 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
