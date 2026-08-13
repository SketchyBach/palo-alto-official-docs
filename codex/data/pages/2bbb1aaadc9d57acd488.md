---
url: https://docs.paloaltonetworks.com/ngfw/help/11-2/globalprotect/network-globalprotect-gateways/globalprotect-gateways-agent-tab/network-services-tab
fetched_at: 2026-08-13T16:47:35Z
source: palo-alto-main
---

# Network Services Tab Clear

Network Services Tab 

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

 Network Services Tab 

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

 GlobalProtect 

 Network > GlobalProtect > Gateways 

 GlobalProtect Gateways Agent Tab 

 Network Services Tab 

 Download PDF 

 Next-Generation Firewall 

 Network Services Tab 

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

 Client IP Pool Tab 

 Next 

 Connection Settings Tab 

 Network Services Tab 

 Network GlobalProtect Gateways <gateway-config> Agent <agent-config> Network Services 

 Select the Network Services tab to configure
DNS settings that will are assigned to the virtual network adapter
on the endpoint when the GlobalProtect app establishes a tunnel
with the gateway. 

 Network Services options are available only if you have
enable tunnel mode and define a tunnel interface on the Tunnel
Settings Tab . 

 GlobalProtect Gateway
Client Network Services Configuration Settings 

 Description 

 Inheritance Source 

 Select a source to propagate DNS server
and other settings from the selected DHCP client or PPPoE client
interface into the GlobalProtect apps’ configuration. With this
setting, all client network configurations, such as DNS servers
and WINS servers, are inherited from the configuration of the interface
selected in the Inheritance Source. 

 Check inheritance source status 

 Click Inheritance Source to see the server
settings that are currently assigned to the client interfaces. 

 Primary DNS 

 Secondary DNS 

 Enter the IP addresses of the primary and
secondary servers that provide DNS to the clients. 

 Primary WINS 

 Secondary WINS 

 Enter the IP addresses of the primary and
secondary servers that provide Windows Internet Naming Service (WINS)
to the endpoints. 

 Inherit DNS Suffixes 

 Select this option to inherit the DNS suffixes
from the inheritance source. 

 DNS Suffix 

 Add a suffix that
the endpoint should use locally when an unqualified hostname, which
it cannot resolve, is entered. You can enter multiple suffixes (up
to 100) by separating each suffix with a comma. 

 Previous 

 Client IP Pool Tab 

 Next 

 Connection Settings Tab 

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
