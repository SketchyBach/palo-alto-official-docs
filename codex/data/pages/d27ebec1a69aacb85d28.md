---
url: https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-networking-admin/nat/configure-nat/create-a-source-nat-rule-with-persistent-dipp
fetched_at: 2026-08-13T17:11:08Z
source: palo-alto-main
---

# Create a Source NAT Rule with Persistent DIPP Clear

Create a Source NAT Rule with Persistent DIPP 

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

 Create a Source NAT Rule with Persistent DIPP 

 Updated on 

 Tue Aug 04 17:04:37 PDT 2026 

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

 Tue Aug 04 17:04:37 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 NAT 

 Configure NAT 

 Create a Source NAT Rule with Persistent DIPP 

 Download PDF 

 Next-Generation Firewall 

 Create a Source NAT Rule with Persistent DIPP 

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

 Translate Internal Client IP Addresses to Your Public IP Address (Source DIPP NAT) 

 Next 

 Enable Clients on the Internal Network to Access your Public Servers (Destination U-Turn NAT) 

 Create a Source NAT Rule with Persistent DIPP 

 Create a source NAT rule that uses persistent Dynamic IP and Port (DIPP). 

 Where Can I Use This? What Do I Need? 

 NGFW 

 One of these licenses for Strata Cloud Manager managed NGFWs: 

 Strata Cloud Manager Essentials 

 Strata Cloud Manager Pro 

 Beginning with PAN-OS 11.1.1 and later releases, you configure persistent
 DIPP in an individual NAT policy rule. 

 On the PA-7500 Series running PAN-OS
 12.1.8 and later, persistent DIPP NAT policy rules support a translated address pool
 of up to 32,768 IP addresses (/17 subnet) per rule in standalone mode and in
 active/passive HA. This expanded limit applies automatically after upgrade with no
 configuration changes required. C3 clustering (MLAG) does not support persistent
 DIPP at this scale in PAN-OS 12.1.8. 

 If your firewall is already configured with the DIPP or
 persistent DIPP NAT policy rules, then you must reboot the firewall after adding,
 deleting, or modifying the DIPP or persistent DIPP NAT policy rules. If your
 firewall does not have these policy rules configured, then you need not reboot after
 adding (new) NAT policy rules. 

 Persistent DIPP NAT rules operate with
 constrained resources and lack oversubscription capabilities. Therefore, configure
 these rules exclusively for persistent traffic to ensure optimal performance.

 Follow the below configuration guidelines when creating persistent DIPP NAT
 policy rule and port: 
 Identify the persistent traffic. 

 If you are not able to identify which traffic is persistence, perform
 the following: 
 Review the traffic logs to identify well-known
 non-persistent services. The common non-persistent traffic
 includes: 
 TCP ports: 443 (HTTPS), 20-22 (FTP/SSH), 80 (HTTP), 8080
 (HTTP alternate) 

 UDP ports: 443 (QUIC), 53 (DNS), and other ephemeral
 connections 

 Configure two identical NAT rules as follows: 
 In the first persistent DIPP NAT policy rule, populate
 service with above TCP or UDP
 applications. Optionally, you can also create additional service
 objects with Object Services . 

 In the second persistent DIPP NAT policy rule, leave
 service empty to capture all other
 traffic. 

 This approach ensures the second rule handles minimal traffic
 volume, since most connections utilize common application protocols
 covered by the first rule. 

 Both the rules can either share the
 same translated IP address pool, or use distinct IP address ranges
 based on your network requirements. 

 When you are using NAT for video or voice applications behind the firewall and you
 need to access STUN, create your policy rule using a translation type of persistent
 dynamic IP and port. 

 PAN-OS 

 Strata Cloud Manager 

 PAN-OS 

 For PAN-OS, create a source NAT rule that uses persistent DIPP. 

 For PAN-OS, follow this procedure to create a source NAT rule with persistent
 DIPP. 

 Create an address object for the external IP address you plan to use. 

 Select Objects Addresses and Add a
 Name and optional
 Description for the object. 

 Select IP Netmask from the
 Type and then enter the IP address of the
 external interface on the firewall, 203.0.113.100 in this example. 

 Click OK . 

 Although you don't have to
 use address objects in your policies, it is a best practice because
 it simplifies administration by allowing you to make updates in one
 place rather than having to update every policy where the address is
 referenced. 

 Create the NAT policy. 

 Select Policies NAT and click Add . 

 On the General tab, enter a descriptive
 Name for the policy. 

 ( Optional ) Enter a tag, which is a keyword or phrase that
 allows you to sort or filter policies. 

 For NAT Type , select ipv4 
 (default). 

 On the Original Packet tab, select the zone you
 created for your internal network in the Source
 Zone section (click Add and then
 select the zone) and the zone you created for the external network from
 the Destination Zone list. 

 On the Translated Packet tab, for
 Translation Type , select
 Persistent Dynamic IP And Port . 

 For Address Type , there are two choices. You
 could select Translated Address and then click
 Add . Select the address object you created or
 enter the translated source address. 

 An alternative Address Type is
 Interface Address , in which case the
 translated address will be the IP address of the interface. For this
 choice, you would select an Interface and
 optionally an IP Address if the interface has
 more than one IP address. 

 Click OK . 

 Commit your changes. 

 ( Optional ) Use operational CLI commands to view persistent DIPP
 information. 

 Access the CLI . 

 > 
 show running persistent-dipp-pool 

 > 
 show running persistent-dipp-client pool
 <nat-pool-index> 

 > 
 show running persistent-dipp-client-translation ip
 <client-ip-address> 

 Use the last two show commands at runtime to track
 persistent NAT resource usage by client IP address. 

 ( Optional ) Use configuration CLI commands to monitor persistent DIPP
 pool utilization. A syslog is generated if resource utilization exceeds the
 threshold you configured. 

 Access the CLI . 

 > 
 configure 

 # set deviceconfig setting
 session persistent-dipp-alert-enable <no|yes> 

 # set deviceconfig setting
 session persistent-dipp-alert-threshold <1-99> 

 # set deviceconfig setting
 session persistent-dipp-alert-interval <5-120> 

 Strata Cloud Manager 

 In Strata Cloud Manager, create a source NAT rule with persistent DIPP. 

 Strata Cloud Manager supports a source NAT rule that uses persistent DIPP . 

 In Strata Cloud Manager, select Configuration NGFW and Prisma Access. 

 Select Network Policies NAT 

 Add Rule and enter a Name for the
 source NAT policy rule. 

 Configure the original packet source zones and addresses, destination zone,
 interface, and addresses, and service. 

 For the translated packet, select Source Address Only or
 Both (source address and destination address). 

 For Translation Type, select Dynamic IP and Port . 

 Select Persistent NAT . 

 You can select Translated Address and then select the +
 to select the address object you created or enter the translated source address. 

 Alternatively, you can select Interface Address , in
 which case the translated address will be the IP address of the interface. For
 this choice, select an Interface and an
 IP address if the interface has more than one IP
 address. Or you could select Floating IP (and select an
 address object). 

 If you selected Both source and destination translation,
 continue by configuring the destination Translated
 Address and Translated Port . 

 Save the configuration. 

 Previous 

 Translate Internal Client IP Addresses to Your Public IP Address (Source DIPP NAT) 

 Next 

 Enable Clients on the Internal Network to Access your Public Servers (Destination U-Turn NAT) 

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

 Networking 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
