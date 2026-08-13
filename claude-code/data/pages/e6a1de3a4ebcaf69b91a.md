---
url: https://docs.paloaltonetworks.com/ngfw/help/11-2/policies/policies-network-packet-broker/network-packet-broker-application-service-traffic-tab
fetched_at: 2026-08-13T16:48:57Z
source: palo-alto-main
---

# Network Packet Broker Application/Service/Traffic Tab Clear

Network Packet Broker Application/Service/Traffic Tab 

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

 Network Packet Broker Application/Service/Traffic Tab 

 Updated on 

 Thu Jun 25 17:41:47 PDT 2026 

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

 Thu Jun 25 17:41:47 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 Policies 

 Policies > Network Packet Broker 

 Network Packet Broker Application/Service/Traffic Tab 

 Download PDF 

 Next-Generation Firewall 

 Network Packet Broker Application/Service/Traffic Tab 

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

 Network Packet Broker Destination Tab 

 Next 

 Network Packet Broker Path Selection Tab 

 Network Packet Broker Application/Service/Traffic Tab 

 Select the Application/Service/Traffic tab
to define the type of traffic, the applications, and the services
to forward to a Network Packet Broker security chain. You can forward
any combination of decrypted TLS, non-decrypted TLS, and non-TLS
traffic to a security chain. 

 Field 

 Description 

 Traffic Type 

 Select the traffic type or traffic types
to forward to the security chain. You can select one, some, or all
of the traffic types in one rule: 

 Forward
TLS(Decrypted) Traffic —(Default) Forwards decrypted
TLS traffic to the security chain specified by the Packet Broker
profile attached to the Network Packet Broker policy. 

 Forward TLS(Non-Decrypted) Traffic —Forwards
undecrypted TLS traffic to the security chain specified by the Packet
Broker profile attached to the Network Packet Broker policy. 

 Forward Non-TLS Traffic —Forwards cleartext
(non-TLS) traffic to the security chain specified by the Packet
Broker profile attached to the Network Packet Broker policy. 

 Application 

 Add specific applications
for the Network Packet Broker policy rule. If an application has
multiple functions, you can select the container application or
individual functional applications. If you select the container
application, all functional applications are included and the application
definition is automatically updated as future functional apps are
added to the container app. 

 Service 

 Select the services that you want to limit
to specific TCP or UDP port numbers. Choose one of the following
from the drop-down: 

 any —(Default)
The selected applications are forwarded on any protocol or port. 

 application-default —The selected applications
are forwarded only if they are on their default ports as defined
by Palo Alto Networks®. (Applications that run on non-standard ports
and protocols, if unintentional, can be a sign of undesired application
behavior and usage, and if intentional, can be a sign of malicious
behavior. However, internal custom applications may use non-standard
ports and require exceptions.) 

 Select — Add an
existing service or choose Service or Service Group to
specify a new entry. (Or select Objects
> Services and Objects
> Service Groups ). 

 Previous 

 Network Packet Broker Destination Tab 

 Next 

 Network Packet Broker Path Selection Tab 

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

 11.2 

 Help 

 Panorama 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
