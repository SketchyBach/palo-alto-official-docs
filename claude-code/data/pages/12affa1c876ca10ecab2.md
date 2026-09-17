---
url: https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/prisma-access-setup/dns-for-prisma-access.html
fetched_at: 2026-09-16T11:25:52Z
source: palo-alto-main
---

# DNS for Prisma Access Clear

Updated on 

 Sep 3, 2026 

 Focus 

 Home 

 Prisma Access 

 Prisma Access Administration 

 Prisma Access Setup 

 DNS for Prisma Access 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deutsch (German) 

 Prisma Access 

 DNS for Prisma Access 

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

 Prisma Access Zones 

 Next 

 High Availability for Prisma Access 

 DNS for Prisma Access 

 Learn about DNS for Prisma Access. 

 Where Can I Use This? What Do I Need? 

 Prisma Access (Managed by Strata Cloud Manager) 

 Prisma Access (Managed by Panorama) 

 Prisma Access license 

 Prisma Access allows you to specify DNS servers to resolve both domains that are internal to your
 organization and external domains. Do this to provide access to services on your
 corporate network—like LDAP and DNS servers—especially if you plan to set up service
 connections to provide access to these type of resources at HQ or in data centers.
 Prisma Access supports DNS resolution for mobile users- Global Protect and
 remote networks deployments . DNS queries for domains in the Internal Domain
 List are sent to your local DNS servers to ensure that resources are available to Prisma
 Access remote network users and mobile users. 

 These settings only apply for internal DNS resolution in the Prisma Access infrastructure. See the procedures in this section for more
 information. 

 Strata Cloud Manager 

 Panorama 

 DNS for Prisma Access ( Strata Cloud Manager ) 

 Enable Prisma Access to resolve both internal and public
domains. You can choose to use Prisma Access DNS or let Prisma Access 
leverage your organization’s DNS setup. 

 Here’s how to set up Prisma Access to resolve internal domains in the Prisma Access 
 infrastructure for mobile user deployments and remote network sites. 

 These settings only apply for internal DNS resolution in the
 Prisma Access infrastructure (for example, internal FQDNs that you use in
 policies). To specify internal DNS resolution for GlobalProtect
 mobile users, go to Configuration NGFW and Prisma Access Configuration Scope Prisma Access GlobalProtect Infrastructure Infrastructure Settings Resolve Internal Domains . 

 Select Configuration NGFW and Prisma Access Configuration Scope Prisma Access Prisma Access Infrastructure and Add Internal DNS Servers . 

 Enter the primary DNS server and secondary DNS server that Prisma Access should
 use to resolve the internal domain names. 

 Add the internal domain names to send to these DNS servers for
 resolution. 

 You can use a wildcard (*) in front of the domains in the domain list, for
 example *.acme.local or *.acme.com. 

 DNS for Prisma Access ( Panorama ) 

 Prisma Access allows you to specify DNS servers to resolve both domains that are internal
 to your organization and external domains. 

 Set up Prisma Access to resolve internal domains in the Prisma Access 
 infrastructure. 

 These settings only apply for internal DNS resolution in the Prisma Access 
 infrastructure (for example, internal FQDNs that you use in policies). To
 specify internal DNS resolution for GlobalProtect
 mobile users, go to Panorama Cloud Services Configuration Mobile Users—GlobalProtect Network Services Internal Domains . 

 Select Panorama Cloud Services Configuration Service Setup and click the gear icon to edit the Settings. 

 Select the Internal Domain List tab. 

 Add the Domain Names, Primary DNS, and Secondary DNS servers that you want Prisma Access to use to resolve your internal domain names. 

 You can use a wildcard (*) in front of the domains in the domain list; for
 example *.acme.local or *.acme.com. 

 Previous 

 Prisma Access Zones 

 Next 

 High Availability for Prisma Access
