---
url: https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/prisma-access-advanced-deployments/mobile-user-globalprotect-advanced-deployments/sinkhole-ipv6-traffic-from-mobile-users/set-up-an-ipv6-sinkhole-on-the-on-premises-gateway.html
fetched_at: 2026-09-16T11:36:49Z
source: palo-alto-main
---

# Set Up an IPv6 Sinkhole On the On-Premises Gateway Clear

Updated on 

 Sep 3, 2026 

 Focus 

 Home 

 Prisma Access 

 Prisma Access Administration 

 Prisma Access Advanced Deployments 

 Prisma Access Mobile Users—GlobalProtect Advanced Deployments 

 Sinkhole IPv6 Traffic in Mobile Users—GlobalProtect Deployments 

 Set Up an IPv6 Sinkhole On the On-Premises Gateway 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deutsch (German) 

 Prisma Access 

 Set Up an IPv6 Sinkhole On the On-Premises Gateway 

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

 Configure GlobalProtect to Disable Direct Access to the Local Network 

 Next 

 Redistribute HIP Information with Prisma Access 

 Set Up an IPv6 Sinkhole On the On-Premises Gateway 

 Set up an IPv6 sinkhole for a Prisma Access GlobalProtect
mobile users deployment. 

 Where Can I Use
 This? What Do I Need? 

 Prisma Access (Managed by Panorama) 

 Prisma Access 
 license 

 If you have a hybrid deployment that uses next-generation
firewalls configured as gateways with Prisma Access , perform the
following task on the on-premises gateway to drop the IPv6 traffic. 

 Add
IPv6 IP pools to your GlobalProtect agent configuration. 

 Select Network GlobalProtect Gateways . 

 Select an existing GlobalProtect gateway or Add a
new one. 

 Select Agent Client Settings . 

 Select the agent configuration to modify or Add a
new one. 

 Select IP Pools ; then, Add an
IPv6 pool to assign to the virtual network adapter on the endpoints
that connect to the GlobalProtect gateway uses for mobile network
traffic and click OK . 

 Enable IPv6 on the interface. 

 Select Device Interface Tunnel and
select the tunnel Interface that you use
for the mobile user’s traffic. 

 Select IPv6 ; then, select Enable
IPv6 on the interface . 

 Add a security policy to set a TCP reset action that
will terminate sessions with IPv6 source traffic that matches the
IP pools you configured in Step 1 . 

 Select Policies Security and Add a
new security policy. 

 Set the Source Address in the
rule to match the IP pools you configured in Step 1 . 

 Select Actions ; then, select
an Action Setting of Reset Client and
click OK . 

 Commit your changes. 

 ( Optional ) Perform this task on all the gateway
firewalls in your deployment. 

 Previous 

 Configure GlobalProtect to Disable Direct Access to the Local Network 

 Next 

 Redistribute HIP Information with Prisma Access
