---
url: https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-mobile-users/mobile-users-explicit-proxy
fetched_at: 2026-08-13T17:24:52Z
source: palo-alto-main
---

# Mobile Users: Explicit Proxy Clear

Mobile Users: Explicit Proxy 

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

 Mobile Users: Explicit Proxy 

 Updated on 

 Aug 10, 2026 

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

 Aug 10, 2026 

 Focus 

 Home 

 Prisma Access 

 Prisma Access Administration 

 Prisma Access Mobile Users 

 Mobile Users: Explicit Proxy 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deutsch (German) 

 Prisma Access 

 Mobile Users: Explicit Proxy 

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

 Setting Priority for Prisma Access and On-Premises Gateways 

 Next 

 Explicit Proxy Configuration Guidelines 

 Mobile Users: Explicit Proxy 

 Set up your Mobile Users (Explicit Proxy) environment. 

 Where Can I Use
This? What Do I Need? 

 Prisma Access (Managed by Strata Cloud Manager) 

 Prisma Access (Managed by Panorama) 

 Prisma Access license 

 Prisma Access by Palo Alto Networks, is a security service edge (SSE) solution
 that delivers best-in-class cloud SWG functionality, including advanced URL filtering,
 SSL decryption, SaaS application control, and advanced threat prevention. Prisma Access 
 operationalizes next-generation security deployments with a pervasive and always-on
 cloud-native infrastructure entirely managed by Palo Alto Networks. Mobile users and
 remote sites can securely access the internet and SaaS applications according to
 corporate policies. Prisma Access offers flexible connectivity options: PAC Files,
 Agent, Agentless, and Site-to-Site IPSEC to ensure any legacy or alternative cloud proxy
 architectures can move to Prisma Access with minimal networking changes. 

 Explicit Proxy 

 Prisma Access provides a complete cloud Secure Web Gateway (SWG) capability, including an
 Explicit Proxy connection method based in the cloud. If your organization’s existing
 network already uses explicit proxies and deploys PAC files on your client endpoints,
 you can smoothly migrate from legacy proxy-based SWG solutions to Prisma Access to
 secure mobile users’ outbound internet traffic. You can also use an Explicit Proxy if
 you need to use a proxy for compliance purposes. Explicit proxy uses the Mobile User
 license. 

 If you use multiple PAC files to define how to
 direct web traffic for different users or systems, Prisma Access gives you the
 ability to associate those PAC files with Forwarding Profiles so that you can use
 several PAC files at once. Futhermore, instead of authoring a PAC file at all,
 Forwarding Profiles enable you to configure simple forwarding rules to define the
 direction of your web traffic. 

 Supported Locations 

 Explicit
 Proxy with the GlobalProtect App 
 GlobalProtect in Proxy Mode 

 GlobalProtect in Tunnel and Proxy Mode 

 Explicit Proxy
 with PAC Files 
 Set Up
 with SAML 

 Set Up with Kerberos 

 Forwarding Profiles 
 Multiple PAC File
 Support 

 Forwarding Rules 

 Forwarding Profiles with
 GlobalProtect 

 Prisma Access Explicit Proxy Features 

 Feature Description 

 App-ID Continuously classifies all applications regardless of port,
 TLS/SSL encryption, or technique used by an attacker to evade detection.
 Unlike legacy solutions that depend on Layers 3 and 4 as the first layers of
 control before application classification is applied, Prisma Access applies
 App-ID along with other Layer 7 controls, such as User-ID. 

 User-ID Integrates with a wide range of user identity repositories so
 that your policies follow your users and groups regardless of their
 location. 

 SSL Decryption Inspects and applies policy to TLS/SSL-encrypted traffic. For
 privacy and regulatory compliance, you can enable or disable decryption
 flexibly based on URL, source, destination, user, user group, and
 port. 

 AI/ML-Based Detection Delivers inline, signatureless attack detection and zero-day
 exploit prevention. Prisma Access adapts and provides instantaneous
 real-time protection vs. scheduled updates. It prevents up to 95% of unknown
 threats instantly, with less than 10-second signature delivery, resulting in
 a 99.5% reduction in infected systems. 

 DNS Security Applies real-time protections and inline machine learning to
 disrupt C2 callback and other attacks that use DNS. Natively integrated into
 Prisma Access , Advanced DNS Security provides automated protections,
 preventing attackers from bypassing security measures, and eliminates the
 need for independent tools or changes to DNS routing. 

 Advanced URL Filtering Superior protection against web-based threats, such as
 phishing, malware, and C2, that combines powerful database protections with
 an ML-powered web security engine that categorizes and blocks new malicious
 URLs in real time. Industry-leading phishing protection tackles the most
 common causes of breaches, letting you take back control of your web traffic
 through fine-grained controls and policy settings that automate security
 actions based on users, risk ratings, and content categories. 

 Advanced Threat Prevention 

 Stop zero-day threats, known exploits, malware, spyware, and
 malicious command and control (C2) with industry-leading threat prevention.
 Prevent 60% more unknown injection attacks and 48% more highly evasive C2
 traffic than traditional intrusion prevention systems. 

 Advanced WildFire 

 Ensure files are safe by automatically preventing known,
 unknown, and highly evasive malware 60X faster with the industry’s largest
 threat intelligence and malware prevention engine. 

 NG-CASB* Gain proactive SaaS visibility, protection against
 misconfigurations, and real-time data protection for best-in-class SaaS
 security. 

 Data Loss Prevention (DLP)* Includes a set of tools and processes that allow you to protect
 sensitive information against unauthorized access, misuse, extraction, or
 sharing. DLP on Prisma Access enables you to enforce data security policies
 and prevent the loss of sensitive data across mobile users and remote
 networks. 

 Remote Browser Isolation Support Through CloudBlades, integrates with third-party RBI clouds by
 leveraging existing NGFW URL categorization and URL rewrite features to
 forward select/all internet-bound traffic to the RBI cloud. This capability
 provides a seamless user experience while forwarding certain traffic
 (unknown or high-risk categories) to RBI for additional inspection while the
 remaining traffic can be inspected by Prisma Access and egress directly to
 the internet. 

 Reporting 

 Includes, as a standard, a detailed, customizable SaaS
 application usage report that provides insight into all SaaS
 traffic—sanctioned and unsanctioned—on your network. You can also create
 custom reports based on your needs and easily schedule, download, and share
 them with others in your organization. 

 User Authentication 

 Supports all existing PAN-OS authentication methods, including
 Kerberos, RADIUS, SAML, LDAP, client certificates, and a local user
 database. With PAC only, supports Kerberos and SAML. 

 Site-to-Site IPsec VPN Supports site-to-site tunnels over IPv4 and IKEv1/IKEv2 to
 ensure compatibility. For multiple connection sites, ECMP routing can
 provide additional redundancy and cost efficiency by balancing sessions over
 available internet connections. 

 Logging Shows overall traffic, application, user, threat, URL, and data
 filter logging to facilitate organization of data via the cloud-based Strata Logging Service . 

 Forwarding Profiles Enables the use of multiple PAC files for different user groups or
 systems. Also supports the creation of forwarding rules for defining the
 direction of web traffic to provide a simpler alternative to creating
 and maintaining a PAC file. 

 * Requires an add-on license. 

 For a detailed description of product features and capabilities, please refer
 to the Prisma Access datasheet . 

 Previous 

 Setting Priority for Prisma Access and On-Premises Gateways 

 Next 

 Explicit Proxy Configuration Guidelines 

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

 Explicit Proxy 

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
