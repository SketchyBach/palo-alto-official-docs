---
url: https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/prisma-access-mobile-users/mobile-users-globalprotect.html
fetched_at: 2026-09-16T09:37:26Z
source: palo-alto-main
---

# Mobile Users: GlobalProtect Clear

Updated on 

 Sep 3, 2026 

 Focus 

 Home 

 Prisma Access 

 Prisma Access Administration 

 Prisma Access Mobile Users 

 Mobile Users: GlobalProtect 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deutsch (German) 

 Prisma Access 

 Mobile Users: GlobalProtect 

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

 Prisma Access Mobile Users 

 Next 

 Planning Checklist for GlobalProtect on Prisma Access 

 Mobile Users: GlobalProtect 

 Where Can I Use
This? What Do I Need? 

 Prisma Access (Managed by Strata Cloud Manager) 

 Prisma Access (Managed by Panorama) 

 Prisma Access license 

 GlobalProtect allows you to protect mobile users by installing
the GlobalProtect app on their
endpoints and configuring GlobalProtect settings in Prisma Access .
GlobalProtect allows you to secure mobile users’ access to all applications,
ports, and protocols, and to get consistent security whether the
user is inside or outside your network. 

 When you secure mobile users using GlobalProtect, you will need
 to define the settings to configure the portal and gateways in
the cloud. For example, you will define a portal hostname, set up
the IP address pool for your mobile users, and configure DNS settings
for your internal domains. You may be able to leverage using existing
configurations for some of the required settings, such as what authentication
profile to use to authenticate mobile users. If you already have
a template with your authentication profiles, certificates, certificate
profiles, and server profiles, you can add that template to the
predefined template stack during onboarding to simplify the setup
process. 

 In addition, if you want your mobile users to be able to connect
to your remote network locations, or if you have mobile users in
different geographical areas who need direct access to each other’s
endpoints, you must configure at least one service connection
with placeholder values , even if you don’t plan to use the
connection to provide access to your data center or HQ locations.
The reason this is required is because, while all remote network
locations are fully meshed, Prisma Access gateways (also known as locations )
connect to the service connection in a hub-and-spoke architecture
to provide access to the internal networks in your Prisma Access 
infrastructure. 

 Planning Checklist for GlobalProtect on Prisma Access 

 Set Up GlobalProtect Mobile Users 

 GlobalProtect — Customize Tunnel Settings 

 Ticket Request to Disable GlobalProtect (Strata Cloud Manager) 

 Monitor GlobalProtect Mobile Users 

 IP Address Pools for a GlobalProtect Mobile Users Deployment 

 How the GlobalProtect App Selects Prisma Access Locations for Mobile Users 

 Add Mobile User Egress IP Addresses to Your Allow Lists 

 GlobalProtect App Upgrades 

 Integrate Prisma Access with On-Premises GlobalProtect Gateways 

 Previous 

 Prisma Access Mobile Users 

 Next 

 Planning Checklist for GlobalProtect on Prisma Access
