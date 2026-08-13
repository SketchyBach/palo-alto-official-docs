---
url: https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-advanced-deployments/dns-resolution-for-mobile-users-and-remote-networks/dns-resolution-for-remote-networks
fetched_at: 2026-08-13T17:24:29Z
source: palo-alto-main
---

# DNS Resolution for Remote Networks Clear

DNS Resolution for Remote Networks 

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

 DNS Resolution for Remote Networks 

 Updated on 

 Mon Aug 10 14:01:14 PDT 2026 

 Focus 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deutsch (German) 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Access Docs 

 Release Notes 

 Select a Document 

 6.2 Preferred and Innovation 

 6.1 Preferred and Innovation 

 6.0 Preferred and Innovation 

 5.2 Preferred and Innovation 

 5.1 Preferred and Innovation 

 5.0 Preferred and Innovation 

 4.2 Preferred 

 4.1 Preferred 

 4.0 Preferred 

 3.2 Preferred and Innovation 

 Activation & Onboarding 

 Administration 

 Select a Document 

 4.0 & Later 

 Prisma Access China 

 Integrations 

 Incidents & Alerts 

 New Features 

 Updated on 

 Mon Aug 10 14:01:14 PDT 2026 

 Focus 

 Home 

 Prisma Access 

 Prisma Access Administration 

 Prisma Access Advanced Deployments 

 DNS Resolution for Agent-Based and Remote Network Deployments 

 DNS Resolution for Remote Networks 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deutsch (German) 

 Prisma Access 

 DNS Resolution for Remote Networks 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Access Docs 

 Release Notes 

 Select a Document 

 6.2 Preferred and Innovation 

 6.1 Preferred and Innovation 

 6.0 Preferred and Innovation 

 5.2 Preferred and Innovation 

 5.1 Preferred and Innovation 

 5.0 Preferred and Innovation 

 4.2 Preferred 

 4.1 Preferred 

 4.0 Preferred 

 3.2 Preferred and Innovation 

 Activation & Onboarding 

 Administration 

 Select a Document 

 4.0 & Later 

 Prisma Access China 

 Integrations 

 Incidents & Alerts 

 New Features 

 Previous 

 DNS Resolution for Agent-Based Deployments 

 Next 

 How BGP Advertises Mobile User IP Address Pools for Service Connections and Remote Network Connections 

 DNS Resolution for Remote Networks 

 Learn about DNS resolution for Prisma Access Remote Network
deployments. 

 Where Can I Use
This? What Do I Need? 

 Prisma Access (Managed by Strata Cloud Manager) 

 Prisma Access (Managed by Panorama) 

 Prisma Access license 

 If you have an existing remote network deployment, you can continue
to use the DNS resolution methods that you already have in place,
or you can use Prisma Access to proxy the DNS request. Proxying
the DNS requests allows you to send DNS requests for public domains
to one server and send DNS request for internal domains to another
server. 

 The following figure shows a DNS request to a deployment where an internal DNS
 server is used to process requests for both internal and external domains. In this case,
 you don't need to use a remote network as DNS proxy. 

 In this example, the remote network IP address is 35.1.1.1 and the loopback IP address is
 10.172.37.1. Since Prisma Access does not proxy the requests, the source IP of the
 DNS request is 10.1.1.1 (the IP address of Client 1’s device in the remote network
 site). 

 If the DNS requests for internal domains being resolved by the DNS server in
 the headquarters or data center location, while requests for external domains are
 resolved using a third-party or public DNS server accessible through the internet, Prisma Access proxies the DNS request: 

 For DNS requests for internal domains, the source IP address is the
 loopback IP address (10.172.37.1 in this example). 

 For DNS requests for external domains, the source IP address is the
 service endpoint address of the remote network (35.1.1.1 in this example). 

 In order to use Prisma Access to proxy DNS requests for the clients in your remote network,
 you also need to configure the remote network DNS proxy IP address as the DNS server
 in your network configuration, which is outside of Prisma access. You can retrieve
 the Remote Network DNS IP Address from Configuration NGFW and Prisma Access Configuration Scope Prisma Access Prisma Access Infrastructure Remote Network DNS IP Address for Prisma Access (Managed by Strata Cloud Manager) deployments or Panorama Cloud Services Status Service Infrastructure Remote Network DNS Proxy IP Address for Prisma Access (Managed by Panorama) deployments. 

 In the following example, 172.1.255.254 is the remote network DNS proxy IP address
 that you configure as the DNS server to proxy DNS requests coming from Prisma Access
 remote network users. 

 Previous 

 DNS Resolution for Agent-Based Deployments 

 Next 

 How BGP Advertises Mobile User IP Address Pools for Service Connections and Remote Network Connections 

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

 Hardware Reference 

 ION 1000 

 ION 1200 

 ION 1200-S 

 ION 2000 

 ION 3000 

 ION 3200 

 ION 5200 

 ION 7000 

 ION 9000 

 ION 9200 

 Hardware Quick Start Guides 

 ION 1200 

 ION 1200 4G 

 ION 1200 5G 

 ION 1200-S 

 ION 1200-S 4G 

 ION 1200-S 5G 

 ION 3200 

 ION 5200 

 ION 9200 

 Virtual ION Deployment 

 Virtual ION on AWS 

 Virtual ION on Azure 

 Virtual ION on GCP 

 Virtual ION on KVM for NFV 

 Virtual ION on OCI 

 Virtual ION on VMware 

 3rd Party Integrations 

 AWS Cloud-WAN Integration (GRE Connect) 

 AWS Cloud-WAN Integration (Tunnel-less Connect) 

 Checkpoint Integration 

 LiveAction Integration 

 Netskope Integration 

 Symantec Web Security Services Integration 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 4.1 Preferred 

 5.0 Preferred and Innovation 

 Administration 

 Prisma SASE 

 Prisma Access 

 Strata Cloud Manager 

 SASE 

 4.2 Preferred 

 5.1 Preferred and Innovation 

 5.0.1 Preferred and Innovation 

 Panorama 

 6.0 Preferred and Innovation 

 Prisma Access 

 4.0 Preferred 

 4.0 & Later 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
