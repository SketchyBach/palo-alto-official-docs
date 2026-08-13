---
url: https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/monitoring/snmp-monitoring-and-traps/enable-snmp-services-for-firewall-secured-network-elements
fetched_at: 2026-08-13T17:09:26Z
source: palo-alto-main
---

# Enable
SNMP Services for Firewall-Secured Network Elements Clear

Enable
SNMP Services for Firewall-Secured Network Elements 

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

 Enable
SNMP Services for Firewall-Secured Network Elements 

 Updated on 

 Mon Aug 03 13:41:44 PDT 2026 

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

 Mon Aug 03 13:41:44 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 Monitoring 

 SNMP
Monitoring and Traps 

 Enable
SNMP Services for Firewall-Secured Network Elements 

 Download PDF 

 Next-Generation Firewall 

 Enable
SNMP Services for Firewall-Secured Network Elements 

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

 Identify the OID for a System Statistic or Trap 

 Next 

 Monitor Statistics Using SNMP 

 Enable
SNMP Services for Firewall-Secured Network Elements 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by PAN-OS or Panorama) 

 Support license 

 ( Panorama ) Device management license 

 If you will use Simple Network Management
Protocol (SNMP) to monitor or manage network elements (for example,
switches and routers) that are within the security zones of Palo
Alto Networks firewalls, you must create a security rule that allows SNMP
services for those elements. 

 You don’t need a security
rule to enable SNMP monitoring of Palo Alto Networks firewalls,
Panorama, or WF-500 appliances. For details, see Monitor Statistics Using SNMP . 

 Create an application group. 

 Select Objects Application Group and click Add . 

 Enter a Name to identify the
application group. 

 Click Add , type snmp ,
and select snmp and snmp-trap from
the drop-down. 

 Click OK to save the application
group. 

 Create a security rule to allow SNMP services. 

 Select Policies Security and click Add . 

 In the General tab, enter a Name for
the rule. 

 In the Source and Destination tabs,
click Add and enter a Source Zone and
a Destination Zone for the traffic. 

 In the Applications tab, click Add ,
type the name of the applications group you just created, and select
it from the drop-down. 

 In the Actions tab, verify
that the Action is set to Allow ,
and then click OK and Commit . 

 Previous 

 Identify the OID for a System Statistic or Trap 

 Next 

 Monitor Statistics Using SNMP 

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

 Administration 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
