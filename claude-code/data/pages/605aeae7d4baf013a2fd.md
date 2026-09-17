---
url: https://docs.paloaltonetworks.com/pan-os/9-1/pan-os-admin/networking/service-routes.html
fetched_at: 2026-09-16T10:52:51Z
source: palo-alto-main
---

# Service Routes Clear

Updated on 

 Jul 22, 2025 

 Focus 

 Home 

 PAN-OS 

 Networking 

 Service Routes 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Service Routes 

 Table of Contents 

 Filter

 End-of-Life (EoL)

 Previous 

 Virtual Routers 

 Next 

 Static Routes 

 Service Routes 

 The firewall uses the management (MGT) interface
by default to access external services, such as DNS servers, external
authentication servers, Palo Alto Networks services such as software,
URL updates, licenses and AutoFocus. An alternative to using the
MGT interface is to configure a data port (a regular interface)
to access these services. The path from the interface to the service
on a server is known as a service route . The service
packets exit the firewall on the port assigned for the external
service and the server sends its response to the configured source
interface and source IP address. 

 When set to default
settings, certain services (such as External Dynamic Lists and URL
updates) use service route settings that are inherited by a parent
service (in this case, Palo Alto Networks Services) if it is explicitly
configured with an interface. If the defaults are not used, Palo
Alto Networks recommends configuring each of the services that you
use with an interface to ensure that the proper service route is used. 

 You
can configure service routes globally for the firewall (shown in
the following task) or Customize
Service Routes for a Virtual System on a firewall enabled
for multiple virtual systems so that you have the flexibility to
use interfaces associated with a virtual system. Any virtual system
that does not have a service route configured for a particular service
inherits the interface and IP address that are set globally for
that service. 

 For firewalls in a high availability (HA) 
 configuration, the service route configuration is synchronized across the HA peers.
 For firewalls in an active/passive high
 availability (HA) , the service route you configured to leverage an
 external service or for log forwarding sees activity only on the
 active HA peer while the
 passive HA peer sees no activity if you configured
 an Ethernet interface as the Source Interface . For example,
 you configure a service route with Ethernet 1/3 as the source interface to forward
 logs to Cortex Data Lake. In this scenario, all logs are forwarded from the
 active HA peer but no logs, including the system
 and configuration logs, are forwarded from the passive 
 HA peer. However, if you configure the MGT interface as the service route
 Source Interface , activity occurs on both the
 active and passive HA
 peers. 

 The following procedure enables you to change
the interface the firewall uses to send requests to external services. 

 Customize service routes. 

 Select Device Setup Services Global (omit
Global on a firewall without multiple virtual system capability),
and in the Services Features section, click Service Route
Configuration . 

 Select Customize and
do one of the following to create a service route: 

 For a predefined service: 

 Select IPv4 or IPv6 and
click the link for the service for which you want customize the
service route. 

 To easily use the same source address for
multiple services, select the checkbox for the services, click Set
Selected Routes , and proceed to the next step. 

 To limit the list for Source Address, select a Source
Interface ; then select a Source Address (from
that interface) as the service route. An Address Object can also
be referenced as a Source Address if it is already configured on
the selected interface. Selecting Any Source
Interface makes all IP addresses on all interfaces available in
the Source Address list from which you select an address. Selecting Use
default causes the firewall to use the management interface
for the service route, unless the packet destination IP address
matches the configured Destination IP address, in which case the
source IP address is set to the Source Address configured
for the Destination . Selecting MGT causes
the firewall to use the MGT interface for the service route, regardless
of any destination service route. 

 The Service Route
Source Address does not inherit configuration changes from the referenced
interface and vice versa. Modification of an Interface IP Address
to a different IP address or Address Object will not update a corresponding
Service Route Source Address. This may lead to commit failure and
require you to update the Service Route(s) to a valid Source Address
value. 

 Click OK to save the setting. 

 Repeat this step if you want to specify both an IPv4 and
IPv6 address for a service. 

 For a destination service route: 

 Select Destination and Add a Destination IP
address. In this case, if a packet arrives with a destination IP
address that matches this configured Destination address,
then the source IP address of the packet will be set to the Source
Address configured in the next step. 

 To limit the list for Source Address, select a Source
Interface ; then select a Source Address (from
that interface) as the service route. Selecting Any Source
Interface makes all IP addresses on all interfaces available in
the Source Address list from which you select an address. Selecting MGT causes
the firewall to use the MGT interface for the service route. 

 Click OK to save the setting. 

 Repeat the prior steps for each service route you
want to customize. 

 Click OK to save the service
route configuration. 

 Commit. 

 Click Commit . 

 Previous 

 Virtual Routers 

 Next 

 Static Routes
