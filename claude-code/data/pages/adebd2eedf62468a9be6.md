---
url: https://docs.paloaltonetworks.com/prisma-access/administration/application-security
fetched_at: 2026-08-13T17:24:08Z
source: palo-alto-main
---

# App Security Clear

App Security 

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

 App Security 

 Updated on 

 Mon Aug 10 14:01:14 PDT 2026 

 Focus 

 Download PDF 

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

 App Security 

 Download PDF 

 Prisma Access 

 App Security 

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

 Create Common Policies for App Acceleration and Private App Security 

 Next 

 Enable App Security (Strata Cloud Manager) 

 App Security 

 Learn about the App Security distributed cloud service 

 Where Can I Use This? What Do I Need? 

 Prisma Access (Managed by Strata Cloud Manager) 

 Prisma Access (Managed by Panorama) 

 Prisma Access
 license 

 Minimum dataplane PAN-OS 11.2.7 or later 

 Private App Security add-on license 

 App Security is a distributed cloud service that adds a dedicated layer of protection
 against application-specific attacks, enabling security teams to consolidate
 traditional, standalone WAF solutions into a unified platform alongside their existing
 SASE and NGFW components. 

 The threat landscape facing enterprise applications has never been more complex or
 fast-moving. Several converging trends are driving the need for a modern, integrated
 approach: 

 Dissolving perimeters. The widespread adoption of remote work and Bring Your Own
 Device (BYOD) has eliminated the traditional network boundary. Private and internal
 systems, which may lack the latest security patches yet house critical business
 data, face the same exposure as public-facing applications. Effective protection
 must be uniform across all corporate applications, regardless of where access
 originates. 

 Continuous change. Organizations are constantly deploying new applications, updating
 existing ones, and migrating between hosting environments. A capable app security
 solution must automatically discover, adapt, and scale alongside these changes with
 little to no manual intervention. 

 AI-accelerated attacks. The rapid democratization of AI tooling means that even
 unsophisticated attackers can now quickly build exploits for newly disclosed
 vulnerabilities, run broad automated scans, and execute complex logic attacks at low
 cost and effort. 

 Point-solution sprawl. Security architectures built from isolated, use-case-specific
 tools create fragmented postures, high management overhead, and slower incident
 response. 

 App Security provides comprehensive protection for web applications and APIs through
 native integration with the Palo Alto Networks Strata portfolio, managed entirely within
 Strata Cloud Manager. Beyond core WAF capabilities such as OWASP Top 10 protection, DDoS
 rate limiting, geo-fencing, and customizable policies, App Security offers several key
 advantages: 

 Unified posture across Public and Private Apps. App Security enforces consistent
 controls for both enterprise public-facing and private applications, applying true
 Zero Trust principles by treating all traffic uniformly regardless of source or use
 case. 

 Instant, zero-touch protection for Private Apps. For private applications, App
 Security is built directly into Prisma SASE. Activating the feature immediately
 extends protection without additional deployments, and auto-discovers and covers any
 number of on-premises or in-cloud applications as they come online. 

 Continuous, proactive threat coverage. App Security receives automatic updates as
 new vulnerabilities are discovered, delivering immediate protection against emerging
 exploits and acting as a critical barrier while applications await patching. 

 Simplified consolidation. App Security offers a compelling path to consolidating
 your web application protection layer —from frictionless onboarding as a Prisma
 Access add-on, to centralized management in Strata Cloud Manager, to a unified log
 repository in SLS. 

 Uses Cases and Deployment Options 

 App Security is a cloud-delivered, auto-scaling service that protects both private
 and public enterprise applications. It relies on inspection nodes collocated with
 global Prisma Access compute locations. 

 App Security Protects Private Applications 

 App Security is an add-on to Prisma Access. Once activated, it automatically
 discovers any internal domains receiving traffic through Prisma Access and adds
 them to an application inventory. From there, administrators can select which
 applications to protect and configure the appropriate App Security policies for
 each. 

 Because private application traffic is already carried and inspected by Prisma
 Access, enabling App Security requires no additional deployments or traffic
 rerouting. Policies are enforced transparently within the existing flow. 

 App Security policies are evaluated after the standard Prisma Access Security
 policies, and they apply only to traffic destined for private applications that
 has already been permitted by those policies. 

 App Security Protects Public Applications 

 App Security supports enterprises that deploy and manage applications accessible
 over the public Internet, delivering the same web application protections
 against threats originating from arbitrary public IPs. 

 Unlike the private application use case, Prisma Access is not in the traffic path
 here. Instead, application traffic is directed to the App Security stack through
 a reverse proxy, using custom CNAME records in the DNS resolver for each
 protected domain. After App Security policies inspect the traffic, it is
 forwarded to the origin server where the application is hosted. 

 The following sections walk through all configuration steps for enabling App
 Security protections on Enterprise Applications. At a high level, policy
 definitions and visibility dashboards are shared across both use cases. The main
 difference between private and public application support lies in how the
 application itself is defined. 

 Previous 

 Create Common Policies for App Acceleration and Private App Security 

 Next 

 Enable App Security (Strata Cloud Manager) 

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

 6.2 Preferred and Innovation 

 SASE 

 Administration 

 Prisma Access 

 Prisma SASE 

 Prisma Access 

 Panorama 

 Strata Cloud Manager 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
