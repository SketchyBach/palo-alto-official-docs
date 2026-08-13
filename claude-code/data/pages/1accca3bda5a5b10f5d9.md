---
url: https://docs.paloaltonetworks.com/sd-wan/getting-started/initial-set-up-for-sd-wan
fetched_at: 2026-08-13T17:35:24Z
source: palo-alto-main
---

# Initial Set Up for SD-WAN Clear

Initial Set Up for SD-WAN 

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

 Initial Set Up for SD-WAN 

 Updated on 

 Tue Apr 07 02:29:53 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 SD-WAN Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Help 

 Select a Document 

 3.4 

 3.3 

 3.2 

 3.1 

 3.0 

 2.2 

 2.1 

 2.0 

 1.0 

 Release Notes 

 New Features 

 Updated on 

 Tue Apr 07 02:29:53 PDT 2026 

 Focus 

 Home 

 SD-WAN 

 Initial Set Up for SD-WAN 

 Download PDF 

 SD-WAN 

 Initial Set Up for SD-WAN 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 SD-WAN Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Help 

 Select a Document 

 3.4 

 3.3 

 3.2 

 3.1 

 3.0 

 2.2 

 2.1 

 2.0 

 1.0 

 Release Notes 

 New Features 

 Previous 

 SD-WAN Configuration Elements 

 Next 

 Add Your SD-WAN Firewalls as Managed Devices 

 Initial Set Up for SD-WAN 

 Prerequisite steps before you can begin configuring SD-WAN 
 deployment. 

 Where Can I Use This? What Do I Need? 

 NGFW 

 Advanced SD-WAN for NGFW 

 Before you can begin configuring your SD-WAN deployment, you
 must add your hub and branch firewalls as managed devices, and create the necessary
 templates and device group configurations to successfully push your SD-WAN configuration to SD-WAN firewalls. 

 To use a Panorama® management server to manage your firewalls, you need to enable a connection
 between the firewall and the Panorama management server. To strengthen your
 security posture when onboarding a new firewall, you must create a unique device
 registration authentication key on the Panorama management server for mutual
 authentication between the new firewall and the server on the first connection. A
 successful first connection requires that you add the Panorama IP address on
 each firewall the server will manage, add the serial number on the server for each
 firewall, and specify the device registration authentication key on both the server and
 the firewall. When you add a firewall as a managed device ,
 you can also associate the new firewall with a device group, template stack, Collector
 Group, and log collector during the initial deployment. Additionally, you have the
 option to automatically push the configuration to your newly added firewall when the
 firewall first connects to the Panorama server, which ensures that firewalls
 are immediately configured and ready to secure your network. 

 If you are adding a firewall to Panorama in a high availability (HA)
 configuration, the device registration authentication key is required only to add the
 firewall to the primary peer. Panorama in HA configuration synchronize the
 certificate authority (CA) certificate that allows the secondary peer to manage
 firewalls in the event of HA failover. 

 Create
 the predefined zones for the SD-WAN to forward the traffic.
 Create a network template with networking configuration objects
 that helps to easily setup firewall policy rules for managing traffic between different
 networks. 

 After adding firewalls as a managed device , you can group
 them into device groups . Be sure to assign both
 firewalls in an active/passive high availability (HA) configuration to the same device
 group so that Panorama will push the same policy rules and objects to those firewalls.
 PAN-OS doesn’t synchronize security rules across HA peers. To manage
 rules and objects at different administrative levels in your organization create a device group hierarchy . 

 Previous 

 SD-WAN Configuration Elements 

 Next 

 Add Your SD-WAN Firewalls as Managed Devices 

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

 IoT Security 

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

 Next-Generation Firewall 

 Getting Started 

 SD-WAN 

 English 

 Panorama 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
