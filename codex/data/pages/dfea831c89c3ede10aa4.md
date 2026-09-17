---
url: https://docs.paloaltonetworks.com/content/techdocs/en_US/prisma-access/administration/prisma-access-advanced-deployments/service-connection-advanced-deployments/use-traffic-forwarding-rules-with-service-connections/configure-zone-mapping-and-security-policies-for-dedicated-connections.html
fetched_at: 2026-09-16T11:36:47Z
source: palo-alto-main
---

# Configure Zone Mapping and Security Policies for Traffic
Steering Dedicated Connections Clear

Updated on 

 Thu Sep 03 12:12:03 PDT 2026 

 Focus 

 Home 

 Prisma Access 

 Prisma Access Administration 

 Prisma Access Advanced Deployments 

 Prisma Access Service Connection Advanced Deployments 

 Use Traffic Steering to Forward Internet-Bound Traffic to
Service Connections 

 Configure Zone Mapping and Security Policies for Traffic
Steering Dedicated Connections 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deutsch (German) 

 Prisma Access 

 Configure Zone Mapping and Security Policies for Traffic
Steering Dedicated Connections 

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

 Prisma Access Traffic Steering Rule Guidelines 

 Next 

 Configure Traffic Steering in Prisma Access 

 Configure Zone Mapping and Security Policies for Traffic
Steering Dedicated Connections 

 Configure zone mapping and create security policies for
dedicated connections for Prisma Access traffic steering. 

 Where Can I Use
 This? What Do I Need? 

 Prisma Access (Managed by Panorama) 

 Prisma Access 
 license 

 If you create a target that uses a dedicated service
connection, the zone for the dedicated service connection changes from Trust to Untrust (non-dedicated
service connection targets do not change their zones). Since you
cannot create zones or configure zone mapping for service connections,
you make zone mapping and security policy changes
for dedicated service connections to the mobile users and device
groups instead. Complete the following steps to configure zone mapping
for dedicated connections. 

 These steps show a sample
configuration; you can tailor this example to suit your deployment. 

 Select Network Zones . 

 Select the correct Template from
the drop-down list (either Mobile_User_Template for
mobile users or Remote_Network_Template for
remote networks). 

 If you have a mobile user and a remote network deployment,
you need to perform these steps twice; once in the Mobile_User_Template and
once in the Remote_Network_Template . 

 Add two zones for your trusted
and untrusted zones. 

 This example creates two zones called Trust and Untrust . 

 Create default policies for the zones you created. 

 Select Policies Security Post Rules . 

 Select the correct Device Group from
the drop-down list (either Mobile_User_Device_Group for
remote networks or Remote_Network_Device_Group for
mobile users). 

 If you have a mobile user and remote network deployment,
you need to perform these steps twice; once in the Mobile_User_Device_Group and
once in the Remote_Network_Device_Group . 

 Add a default policy to use
for Trust zone-to-Trust zone traffic. 

 This policy allows Any traffic to
pass for all Source , User , Destination , Application ,
and Service/URL Category traffic. 

 Add a default policy to use
for Trust zone-to-Untrust zone traffic, using the same parameters
you used for the Trust-to-Trust policy. 

 When complete, you have two security policies, one for
Trust-to-Trust traffic and one for Trust-to-Untrust traffic. 

 Define zone mapping for the remote networks, mobile users,
or both, as required for your deployment. 

 Set the zone mapping for the remote networks,
mobile users, or both. 

 For mobile users, select Panorama Cloud Services Configuration Mobile Users . 

 For remote networks, select Panorama Cloud Services Configuration Remote Networks . 

 Click the gear icon next to Zone Mapping to
edit the settings. 

 Set the Zone Mapping for your
deployment, moving the zone for trusted traffic to the Trusted
Zones and the zone for untrusted traffic to the Untrusted
Zones ; then, click OK . 

 Previous 

 Prisma Access Traffic Steering Rule Guidelines 

 Next 

 Configure Traffic Steering in Prisma Access
