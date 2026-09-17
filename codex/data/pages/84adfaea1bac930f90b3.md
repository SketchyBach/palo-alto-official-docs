---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/administration/prisma-sd-wan-sites-and-devices/prisma-sd-wan-ports-and-interfaces/virtual--interface/add-and-configure-a-virtual-interface
fetched_at: 2026-09-16T07:47:48Z
source: strata-and-sase
---

# Add and Configure a Virtual Interface Clear

Updated on 

 Mon Aug 24 08:54:44 PDT 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Prisma SD-WAN Administrator’s Guide 

 Prisma SD-WAN Sites and Devices 

 Prisma SD-WAN Ports and Interfaces 

 Virtual Interface 

 Add and Configure a Virtual Interface 

 Download PDF 

 Prisma SD-WAN 

 Add and Configure a Virtual Interface 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma SD-WAN Docs 

 Activation & Onboarding 

 Administration 

 CloudBlades 

 Select a Document 

 CloudBlade Integrations 

 CloudBlades Integration with Prisma Access 

 Deployment 

 Incidents & Alerts 

 Reference 

 Release Notes 

 Select a Document 

 ION 6.8 

 ION 6.6 

 ION 6.5 

 ION 6.4 

 ION 6.3 

 ION 6.1 

 ION 5.6 

 Prisma SD-WAN Controller 

 Prisma SD-WAN On-Premises Controller 

 Prisma SD-WAN CloudBlades 

 Prisma Access CloudBlade Cloud Managed 

 Prisma Access CloudBlade Panorama Managed 

 New Features 

 Previous 

 Virtual Interface 

 Next 

 Prisma SD-WAN Standard VPN 

 Add and Configure a Virtual Interface 

 Learn to add and configure a virtual interface. The interfaces can be either controller
 ports or non-controller ports. 

 Where Can I Use
 This? What Do I Need? 

 Prisma SD-WAN (Managed by Strata Cloud Manager ) 

 Prisma SD-WAN 

 A virtual interface refers to a software-based interface that emulates a physical
 one, used for a variety of logical networking purposes such as VLAN subinterfaces,
 loopback interfaces, or interfaces in virtual wire mode. It differs from a port
 channel, which is a configuration that bundles multiple physical Ethernet ports into
 a single logical interface for increased bandwidth and redundancy. 

 Select Configuration Prisma SD-WAN ION Devices Claimed , select the device you want to configure and then select a port
 on the device to configure for HA. 

 On the device's interface configuration page, select the Interfaces + Add Interface to add a virtual interface. 

 In the General section, 

 Enter a Name and (Optional) 
 Description , and add Tags 
 for the port channel interface. 

 For Admin Up , select No 
 or Yes to administratively bring down the
 interface or bring up the interface. 

 An interface will not be operational if Admin
 Up is No . 

 Admin Up must be
 Yes for a virtual interface with
 controller ports. 

 Admin Up can be
 Yes or No for
 a virtual interface with non-controller ports. 

 In the Network Setting section, 

 For Virtual Interface Members, select a maximum of two interfaces from
 the drop-down. 

 The interfaces can be either controller ports or non-controller
 ports. A combination of controller and non-controller ports is not
 allowed. Configuring the second controller port provides port-level
 and cable-level redundancy. 

 For Use These Ports For , select an appropriate
 option from the drop-down. 

 For controller ports, the option can be None. 

 For non-controller ports, the available options are: LAN,
 Internet, and Private WAN. 

 For Security Zone , select a device to bind. 

 For IPv4 Configuration , select
 DHCP or Static . 

 If the IP address dynamically assigned, select
 DHCP . 

 If the IP address is fixed and specified manually, select
 Static . If you select
 Static , specify the IP
 Address/Mask , Default
 Gateway , and DNS
 server(s) . 

 Select Enable IPv6 On This Interface to
 configure IPv6. 

 For IPv6 Configuration , select AutoConf or
 Static . 

 Autoconf (automatic
 interface configuration) indicates the Global IP address is derived
 using stateless address autoconfiguration (SLAAC). 

 Choose Static if the IP address is fixed and
 is manually assigned. Additionally specify the IPv6
 Address/Mask , Default Gateway
 (IPv6) , and DNS
 server(s)(IPv6) . 

 IPv6 configuration is available for Private WAN and Internet
 ports. 

 For Scope , select Global 
 or Local . 

 When Global is selected, the IP addresses
 advertised into the Prisma SD-WAN Fabric. 

 When Local is selected the IP addresses
 are not advertised into the Prisma SD-WAN 
 Fabric. 

 For Circuit Label , select the circuit label that
 corresponds to the connection for this site. 

 A circuit label cannot be attached to a virtual interface composed of
 two controller ports. 

 If DHCP Relay functions are required, select
 DHCP . Change Add DHCP
 Relay from No to
 Yes . 

 Create Virtual Interface to complete
the configuration. 

 Related CLIs 

 config interface 

 ping 

 ping6 

 debug bounce interface 

 debug bw test src interface 

 ssh interface 

 tcp dump 

 tcp ping 

 trace route 

 inspect interface stats 

 inspect wan paths 

 dump cgnx infra status 

 dump cgnx infra status live 

 dump cgnx infra status store 

 dump interface config 

 dump interface status 

 dump interface status interface
 details 

 dump interface status interface module 

 dump wan interface config 

 dump wan interface summary 

 Previous 

 Virtual Interface 

 Next 

 Prisma SD-WAN Standard VPN
