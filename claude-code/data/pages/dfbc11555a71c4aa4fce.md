---
url: https://docs.paloaltonetworks.com/dns-security/release-notes/new-features-in-advanced-dns-security/new-features-in-december-2025
fetched_at: 2026-08-13T15:32:05Z
source: palo-alto-main
---

# New Features in December 2025 Clear

New Features in December 2025 

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

 New Features in December 2025 

 Updated on 

 Thu May 28 12:29:32 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Advanced DNS Security 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Release Notes 

 Updated on 

 Thu May 28 12:29:32 PDT 2026 

 Focus 

 Home 

 Advanced DNS Security Powered by Precision AI® 

 New Features in Advanced DNS Security 

 New Features in December 2025 

 Download PDF 

 Advanced DNS Security Powered by Precision AI® 

 New Features in December 2025 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Advanced DNS Security 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Release Notes 

 Previous 

 New Features in January 2026 

 Next 

 New Features in October 2025 

 New Features in December 2025 

 Review the new features and platform changes for Advanced DNS Security in December
 2025. 

 Automatic Subdomain Expansion for Advanced DNS Security Resolver EDLs 

 December 19, 2025 

 Managing comprehensive access control for domains often requires defining both the
 top-level domain and its subdomains to ensure complete coverage. This manual process
 can be time-consuming and increases the risk of security gaps if a specific
 subdomain is omitted. 

 You can now configure Advanced DNS Security Resolver external
 dynamic lists to automatically include all subdomains associated with a specific
 domain entry . When you enable this capability, the Advanced DNS Security
 Resolver treats a standard domain entry, such as example.com, as inclusive of all
 lower-level components (for example, *.example.com). This ensures that your security
 policies apply consistently across the entire domain hierarchy without requiring you
 to manually define wildcard entries. 

 This feature simplifies EDL domain management on your Advanced DNS Security Resolver;
 however, because the system generates an implicit wildcard entry for each domain,
 enabling this setting consumes two entries for every domain in the list. To
 accommodate for the increased entry count, the total domain entry limits (across all
 EDLs for a given tenant) have been increased. 

 Custom FQDN List Support For Advanced DNS Security Resolver 

 December 19, 2025 

 Security administrators often require precise and immediate control over domain
 resolution that extends beyond the default threat intelligence feeds and broad
 domain categories. Previously, when using the Advanced DNS Security Resolver ,
 you could only configure Fully Qualified Domain Names (FQDNs) to be explicitly set
 as 'allowable' domains with an association with a specific DNS Security profile.
 This limitation prevented the granular enforcement of diverse actions (like blocking
 or sinkholing) on custom domain lists unique to a network’s immediate threat posture
 or specific compliance needs. Additionally, replicating these FQDNs across multiple
 security profiles required manual re-entry, which could consume a significant amount
 of time. 

 The introduction of Custom Domain List Support for the Advanced DNS Security Resolver
 solves this critical challenge by providing administrators with control over
 security policy enforcement. This enhancement allows you to create and manage custom FQDN lists that
 are not tied to a DNS Security profile and apply explicit security actions to
 them. 

 You can now apply specific enforcement actions, including allow , block ,
 alert or sinkhole , to domains defined in your referable custom
 FQDN lists. This capability is essential for stopping communication with internal or
 custom-identified command-and-control (C2) domains, and other malicious domains, or
 ensuring strict adherence to unique organizational compliance lists. By defining
 explicit security actions for customized FQDN lists, you strengthen your first line
 of defense against sophisticated, DNS-based attacks. 

 Advanced DNS Security Resolver for Prisma Access Agent 

 December 08, 2025 

 Mobile Users with Prisma® Access Agents might need to disconnect the agent app due to
 various issues, such as connectivity or performance problems, customer site
 restrictions, or when accessing sanctioned applications directly. This creates
 security gaps due to the lack of security inspection for internet or Software as a
 Service (SaaS) traffic. Advanced DNS Security Resolver addresses this challenge by
 providing DNS security for Prisma Access Agent users whenever the user is
 disconnected from Prisma Access Agent, ensuring security protections remain in place
 at all times. 

 When you enable Advanced DNS Security Resolver for
 Prisma Access Agents, the agent routes DNS traffic to Palo Alto Networks DNS
 resolvers over HTTPS (DoH) whenever the primary tunnel connection is disconnected.
 The feature intercepts DNS queries and forwards them through encrypted connections,
 ensuring visibility and control over DNS requests even when users disconnect from
 the tunnel. The service supports user-authenticated modes, with long-lived device
 tokens valid for up to six months. 

 With this feature, forwarding of traffic to Advanced DNS Security Resolver relies on
 the same forwarding profiles the agent receives, giving you full control over what
 DNS traffic is resolved through Advanced DNS Security Resolver and what is allowed
 to go direct. The feature provides threat protection by blocking malicious domains
 using DNS Security for DNS requests, and user-specific, administrator-configured DNS
 Security policies you add to Advanced DNS Security Resolver. You can deploy Advanced
 DNS Security Resolver for Prisma Access Agent as a fallback mechanism that activates
 when primary tunnel connections are disrupted. 

 Previous 

 New Features in January 2026 

 Next 

 New Features in October 2025 

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

 Endpoints 

 GlobalProtect 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 Advanced DNS Security 

 Release Notes 

 Cloud-Delivered Security Services 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
