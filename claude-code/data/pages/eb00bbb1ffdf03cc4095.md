---
url: https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-networking-admin/nat/configure-nat/translate-internal-client-ip-addresses-to-your-public-ip-address-source-dipp-nat
fetched_at: 2026-08-13T17:11:09Z
source: palo-alto-main
---

# Translate Internal Client IP Addresses to Your Public IP
Address (Source DIPP NAT) Clear

Translate Internal Client IP Addresses to Your Public IP
Address (Source DIPP NAT) 

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

 Translate Internal Client IP Addresses to Your Public IP
Address (Source DIPP NAT) 

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

 Translate Internal Client IP Addresses to Your Public IP
Address (Source DIPP NAT) 

 Download PDF 

 Next-Generation Firewall 

 Translate Internal Client IP Addresses to Your Public IP
Address (Source DIPP NAT) 

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

 Configure NAT 

 Next 

 Create a Source NAT Rule with Persistent DIPP 

 Translate Internal Client IP Addresses to Your Public IP
Address (Source DIPP NAT) 

 Configure source DIPP NAT to translate internal client IP addresses to your public IP
 address. 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by PAN-OS or Panorama) 

 When a client on your internal network sends a request, the source address in the
 packet contains the IP address for the client on your internal network. If you use
 private IP address ranges internally, the packets from the client will not be able
 to be routed on the internet unless you translate the source IP address in the
 packets leaving the network into a publicly routable address. 

 On the firewall you can do this by configuring a source NAT policy that translates
 the source address (and optionally the port) into a public address. One way to do
 this is to translate the source address for all packets to the egress interface on
 your firewall, as shown in the following procedure. 

 On the PA-7500 Series
 running PAN-OS 12.1.8 and later, a single DIPP NAT policy rule supports a translated
 address pool of up to 32,768 IP addresses (/17 subnet), enabling you to consolidate
 what would otherwise require up to 128 separate NAT rules into a single policy. This
 expanded per-policy capacity takes effect automatically after upgrade and requires
 no additional configuration. The system-wide maximum for DIPP NAT translated IP
 addresses on the PA-7500 is also 32,768. If you later downgrade from PAN-OS 12.1.8,
 the downgrade is blocked when any single DIPP NAT policy rule contains more than 256
 translated IP addresses, and the following message is displayed: 
 Downgrading from PAN-OS 12.1.8 is not allowed if a DIPP NAT policy has a number
 of translated IP addresses configured that exceeds the maximum capacity of 256
 translated IP addresses per DIPP NAT policy. Reduce the number of DIPP NAT IP
 addresses in the policy, commit, and then retry the downgrade. 

 This task covers regular DIPP, and this task also includes
 the step to enable persistent NAT for DIPP in PAN-OS 11.1.0 and earlier releases.
 To enable persistent NAT for DIPP in
 PAN-OS 11.1.1 and later releases, Create a Source NAT Rule with Persistent DIPP . 

 Create an address object for the external IP address
you plan to use. 

 Select Objects Addresses and Add a Name and
optional Description for the object. 

 Select IP Netmask from the Type and
then enter the IP address of the external interface on the firewall,
203.0.113.100 in this example. 

 Click OK . 

 Although you do not have to use address objects in your policies, it is a best
 practice because it simplifies administration by allowing you to
 make updates in one place rather than having to update every policy
 where the address is referenced. 

 Create the NAT policy. 

 Select Policies NAT and click Add . 

 On the General tab, enter a
descriptive Name for the policy. 

 ( Optional ) Enter a tag, which is a keyword
or phrase that allows you to sort or filter policies. 

 For NAT Type , select ipv4 (default). 

 On the Original Packet tab,
select the zone you created for your internal network in the Source Zone section
(click Add and then select the zone) and
the zone you created for the external network from the Destination
Zone list. 

 On the Translated Packet tab,
select Dynamic IP And Port from the Translation Type list
in the Source Address Translation section of the screen. 

 For Address Type , there are
two choices. You could select Translated Address and
then click Add . Select the address object
you just created. 

 An alternative Address Type is Interface
Address , in which case the translated address will be
the IP address of the interface. For this choice, you would select
an Interface and optionally an IP Address if
the interface has more than one IP address. 

 Click OK . 

 Commit your changes. 

 Click Commit . 

 ( PAN-OS 11.1.0 and earlier releases ) Enable persistent NAT for DIPP.
 (Skip this step for regular DIPP.) 

 Access the CLI . 

 > set system setting
 persistent-dipp enable yes 

 > request restart
 system 

 If you have HA configured, repeat this step on the other HA peer. 

 ( Optional ) Verify the translation. 

 Use the show session all command
to view the session table, where you can verify the source IP address and
port and the corresponding translated IP address and port. 

 Use the show session id <id_number> to
view more details about a session. 

 If you configured Dynamic IP NAT, use the show counter global filter aspect session severity drop | match nat command
to see if any sessions failed due to NAT IP allocation. If all of
the addresses in the Dynamic IP NAT pool are allocated when a new
connection is supposed to be translated, the packet will be dropped. 

 Previous 

 Configure NAT 

 Next 

 Create a Source NAT Rule with Persistent DIPP 

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
