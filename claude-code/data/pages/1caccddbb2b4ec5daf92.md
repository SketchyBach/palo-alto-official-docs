---
url: https://docs.paloaltonetworks.com/ngfw/administration/virtual-systems/customize-service-routes-for-a-virtual-system
fetched_at: 2026-09-16T07:26:06Z
source: palo-alto-main
---

# Customize Service Routes for a Virtual
System Clear

Updated on 

 Mon Aug 31 04:46:16 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 Virtual Systems 

 Customize Service Routes for a Virtual
System 

 Download PDF 

 Next-Generation Firewall 

 Customize Service Routes for a Virtual
System 

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

 Configure a Shared Gateway 

 Next 

 Configure a PA-7000 Series Firewall for Logging Per Virtual System 

 Customize Service Routes for a Virtual
System 

 Learn how to setup service routes to support virtual systems. 

 Where Can I Use This? What Do I Need? 

 NGFW 

 Virtual
 Systems license for any virtual systems beyond
 the base number supported by each NGFW series. 

 One of the following licenses when using Strata Cloud
 Manager: 
 Strata Cloud Manager Pro 

 Strata Cloud Manager Essentials 

 Virtual System support on Strata Cloud
 Manager is available on request. Contact your account team to
 enable the feature. 

 When a firewall is enabled for multiple virtual systems,
the virtual systems inherit the global service and service route settings.
For example, the firewall can use a shared email server to originate
email alerts to all virtual systems. In some scenarios, you’d want
to create different service routes for each virtual system. 

 One use case for configuring service routes at the virtual system
level is if you are an ISP who needs to support multiple individual
tenants on a single Palo Alto Networks firewall. Each tenant requires
custom service routes to access service such as DNS, Kerberos, LDAP,
NetFlow, RADIUS, TACACS+, Multi-Factor Authentication, email, SNMP
trap, syslog, HTTP, User-ID Agent, VM Monitor, and Panorama (deployment
of content and software updates). Another use case is an IT organization
that wants to provide full autonomy to groups that set servers for
services. Each group can have a virtual system and define its own
service routes. 

 You can select a virtual router for a service route in
a virtual system; you cannot select the egress interface. After
you select the virtual router and the firewall sends the packet
from the virtual router, the firewall selects the egress interface
based on the destination IP address. Therefore, if a virtual system
has multiple virtual routers, packets to all of the servers for
a service must egress out of only one virtual router. A packet with
an interface source address may egress a different interface, but
the return traffic would be on the interface that has the source
IP address, creating asymmetric traffic. 

 When you enable Multi Virtual System Capability, any virtual system that does not
 have specific service routes configured inherits the global service and service
 route settings for the firewall. You can instead configure a virtual system to use a
 different service route, as described in the following workflow. 

 A firewall with multiple virtual systems must have interfaces and subinterfaces with
 non-overlapping IP addresses. A per-virtual system service route for SNMP traps or
 for Kerberos is for IPv4 only. 

 The service route for a service strictly follows how you configured the server
 profile for the service: 

 If you define a server profile ( Device Server Profiles ) for the Shared location, the firewall uses the global service
 route for that service. 

 If you define a server profile for a specific virtual system, the firewall uses
 the virtual system-specific service route for that service. 

 If you define a server profile for a specific virtual system but the virtual
 system-specific service route for that service is not configured, the firewall
 uses the global service route for that service. 

 The firewall supports syslog forwarding on a virtual system basis. When multiple
 virtual systems on a firewall are connecting to a syslog server using SSL
 transport, the firewall can generate only one certificate for secure
 communication. The firewall does not support each virtual system having its own
 certificate. 

 Customize service routes for a virtual system. 

 Select Device Setup Services Virtual Systems , and select the virtual system you want to
 configure. 

 Click the Service Route Configuration 
 link. 

 Select one: 

 Inherit Global Service Route
 Configuration —Causes the virtual system to
 inherit the global service route settings relevant to a
 virtual system. If you choose this option, skip the step to
 customize. 

 Customize —Allows you to specify a
 source address for each service. 

 If you chose Customize , select the
 IPv4 or IPv6 tab,
 depending on what type of addressing the server offering the service
 uses. You can specify both IPv4 and IPv6 addresses for a service. Click
 on a service. (Only services that are relevant to a virtual system are
 available.) 

 To easily use the same source address for multiple services,
 select the checkbox for the services, click Set
 Selected Routes , and continue. 

 To limit the list for Source Address, select a
 Source Interface , then select a
 Source Address (from that interface) as the service route.
 Selecting Any Source Interface makes
 all IP addresses on all interfaces for the virtual system
 available in the Source Address list from which you select
 an address. You can select Inherit Global
 Setting . 

 Source Address will indicate
 Inherited if you selected
 Inherit Global Setting for the
 Source Interface or it will
 indicate the source address you selected. If you selected
 Any for Source
 Interface , select an IP address or enter an
 IP address (using the IPv4 or IPv6 format that matches the
 tab you chose) to specify the source address that will be
 used in packets sent to the external service. 

 If you modify an address object and the IP family type
 (IPv4/IPv6) changes, a Commit is
 required to update the service route family to use. 

 Click OK . 

 Repeat the prior steps to configure source addresses for other external
 services. 

 Click OK . 

 Commit your changes. 

 Click Commit and OK . 

 If you are configuring per-virtual system service routes for logging services
 for a PA-7000 Series firewall, continue to the task Configure a
 PA-7000 Series Firewall for Logging Per Virtual System . 

 Previous 

 Configure a Shared Gateway 

 Next 

 Configure a PA-7000 Series Firewall for Logging Per Virtual System
