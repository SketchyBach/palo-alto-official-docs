---
url: https://docs.paloaltonetworks.com/prisma-access/administration/ztna-connector-in-prisma-access/active-directory-domain-services-support-with-ztna-connector
fetched_at: 2026-08-13T17:25:40Z
source: palo-alto-main
---

# Active Directory Domain Services Support with ZTNA Connector Clear

Active Directory Domain Services Support with ZTNA Connector 

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

 Active Directory Domain Services Support with ZTNA Connector 

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

 Prisma Access ZTNA Connector 

 Active Directory Domain Services Support with ZTNA Connector 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deutsch (German) 

 Prisma Access 

 Active Directory Domain Services Support with ZTNA Connector 

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

 ZTNA Connector Application Tags 

 Next 

 Delete Connector IP Blocks 

 Active Directory Domain Services Support with ZTNA Connector 

 Learn how Prisma Access ZTNA Connector provides support for Microsoft Active
 Directory Domain Services using DNS SRV resolution and data center IP addresses. 

 Where Can I Use This? What Do I Need? 

 Prisma Access (Managed by Strata Cloud Manager) 

 Prisma Access version 6.0 

 Prisma Access licenses include 10 connectors, 10,000
 FQDNs, and 1024 IP subnets. A minimum version of Prisma Access 5.2 is required to get 10,000 FQDNs. This
 functionality is provided for the purpose of trying out ZTNA
 Connectors in your environment. 

 The Private App add-on license
 includes 200 ZTNA Connectors, 10,000 FQDNs, and 1024 IP subnet
 functionality. 

 Microsoft Active Directory Domain Services (AD DS) relies on a two-phase DNS resolution
 process that requires special handling in Prisma Access ZTNA
 deployments. When a Microsoft client joins a domain, it first makes a DNS SRV query to
 identify domain controllers offering specific services, followed by Connectionless
 Lightweight Directory Access Protocol (CLDAP) queries to locate the optimal domain
 controller in the user's AD site. 

 Prisma Access ZTNA Connector now provides enhanced support for AD DS
 environments through two key capabilities. First, it supports end-to-end DNS SRV
 resolution, enabling users to discover domain controllers and their services. Second, it
 provides a Use Data Center IP feature for application targets that prevents
 destination network address translation (DNAT) to domain controllers required by
 Microsoft's AD architecture. 

 In traditional ZTNA deployments, application targets are assigned Prisma
 Access anycast IP addresses, and traffic undergoes DNAT. However, AD services
 might not function correctly over DNAT. The Use Data Center IP feature addresses
 this by treating the domain controller's actual data center IP address as the fabric IP
 address, eliminating the need for DNAT in the connection path. 

 To successfully implement ZTNA Connector for AD environments: 
 Understand your AD network design. 

 Co-locate ZTNA Connector groups in those sites within AD site subnets close to
 AD resources. 

 Configure the DNS servers for the ZTNA Connectors. The DNS servers need to
 provide DNS resolutions for both public PANW cloud services FQDNs and also
 private data center Microsoft AD FQDNs, particularly for 1-arm and 2-arm
 configurations. 

 ZTNA Connector requires access to
 DNS servers for resolving public DNS to connect to PANW cloud controllers
 and private DNS for Microsoft AD. In 1-arm configurations, the DNS server
 (typically a domain controller) must resolve both public and private FQDNs.
 In 2-arm configurations, port 1 DNS server resolves public FQDNs, while port
 2 DNS server (the domain controller) resolves private Microsoft AD
 resources. 

 Map wildcard and/or FQDN ZTNA Connector application targets to the domain names
 within the sites domain controllers. 

 ZTNA Connector also includes wildcard and FQDN application target port settings for
 Microsoft AD services, such as DNS, Kerberos, LDAP, SMB, and others, saving you time
 during configuration while enabling customization as needed. 

 ZTNA Connectors forwards the SRV request to the domain controllers. The
 response to the DNS SRV query from the domain controllers is forwarded back to the
 Microsoft Windows client. With this information, the Microsoft client is able to join
 the AD domain. 

 You need to use the domain controller's data center IP address when
 communicating with the domain controllers. 

 Configuring Application Targets 

 When configuring the application targets: 
 Review the ZTNA Connector Requirements and Guidelines . 

 Configure ZTNA Connector. 

 Go to Configuration Wildcard Targets and Create Wildcard Target . 

 Add a unique Name , assign a Connector
 Group , and add a domain in Wildcard . 

 If you're adding a wildcard target or an FQDN target to access a Microsoft AD
 data center, Enable Microsoft AD Firewall Ports to
 prepopulate TCP and UDP ports required for AD, and then
 Confirm . 

 If you are adding a wildcard target or an FQDN target to access a Microsoft AD
 data center, enable Keep Data Center IP Address , and then
 Confirm . 

 For Microsoft AD networks, it's essential to utilize this
 option. Microsoft client must communicate (without involving DNAT
 translation of the domain controller's IP address) with the domain
 controllers using the native data center IP address of the domain
 controller within the network. If the application is compatible with DNS
 proxy and DNAT translation, this option isn't necessary. 

 When you enable Keep Data Center IP
 Address , the applications don't get an IP address from the
 application pool. The original IP address of the application that the ZTNA
 Connector resolves, will be advertised in the Prisma Access
 Infrastructure. 

 For FQDN applications learned from
 Keep Data Center IP Address wildcards or manually
 added FQDNs set as Keep Data Center IP Address 
 targets, the IP address displayed in the application table indicates the
 specific data center IP address. 

 Previous 

 ZTNA Connector Application Tags 

 Next 

 Delete Connector IP Blocks 

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

 SASE 

 4.1 Preferred 

 Strata Cloud Manager 

 5.1 Preferred and Innovation 

 Panorama 

 6.0 Preferred and Innovation 

 ZTNA Connector 

 5.0 Preferred and Innovation 

 Administration 

 Prisma Access 

 Prisma Access 

 Prisma SASE 

 Strata Cloud Manager 

 4.0 & Later 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
