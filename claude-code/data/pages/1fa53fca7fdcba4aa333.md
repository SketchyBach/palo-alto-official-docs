---
url: https://docs.paloaltonetworks.com/openconfig/1-3/openconfig-admin/openconfig-models/ospf-version-2/manage-ospf-version-2
fetched_at: 2026-08-13T16:57:33Z
source: palo-alto-main
---

# Manage OSPF Version 2 Clear

Manage OSPF Version 2 

 Home 

 EN

 Location 

 Documentation Home 

 Palo Alto Networks 

 Support 

 Live Community 

 Knowledge Base 

 Strata Copilot

 PAN-OS OpenConfig Administrator’s Guide 

 : 
 Manage OSPF Version 2 

 Updated on 

 Tue Feb 11 16:28:28 PST 2025 

 Focus 

 Download PDF 

 Filter

 Version 

 1.3 

 1.3 

 1.2 

 1.1 

 Expand all | Collapse all 

 Getting Started 

 About PAN-OS OpenConfig Support 

 PAN-OS OpenConfig Model Support 

 Install the OpenConfig Plugin 

 PAN-OS OpenConfig Wildcard Support 

 PAN-OS OpenConfig Bundling Support 

 OpenConfig Models 

 BGP 

 BGP Behavior 

 Manage BGP Routes 

 Firewall Zones 

 Firewall Zones Behavior 

 Manage Firewall Zones 

 High Availabilty 

 High Availability Behavior 

 Manage High Availability 

 Interfaces 

 Interfaces Behavior 

 Manage Interfaces 

 LACP 

 LACP Behavior 

 Manage LACP 

 LLDP 

 LLDP Behavior 

 Manage LLDP 

 Local Routes 

 Local Routes Behavior 

 Manage Local Routes 

 Network Instances 

 Network Instances Behavior 

 Manage Network Instances 

 OSPF Version 2 

 OSPF Version 2 Behavior 

 Manage OSPF Version 2 

 Platform 

 Platform Behavior 

 Manage Platform 

 Routing Policy 

 Routing Policy Behavior 

 Manage Routing Policies 

 System 

 System Behavior 

 Manage System 

 VLAN 

 VLAN Behavior 

 Manage VLANs 

 Telemetry Streaming 

 OpenConfig Telemetry on PAN-OS 

 Updated on 

 Tue Feb 11 16:28:28 PST 2025 

 Focus 

 Home 

 OpenConfig 

 PAN-OS OpenConfig Administrator’s Guide 

 OpenConfig Models 

 OSPF Version 2 

 Manage OSPF Version 2 

 Download PDF 

 PAN-OS OpenConfig Administrator’s Guide 

 Manage OSPF Version 2 

 Table of Contents 

 Filter

 Version 

 1.3 

 1.3 

 1.2 

 1.1 

 Expand all | Collapse all 

 Getting Started 

 About PAN-OS OpenConfig Support 

 PAN-OS OpenConfig Model Support 

 Install the OpenConfig Plugin 

 PAN-OS OpenConfig Wildcard Support 

 PAN-OS OpenConfig Bundling Support 

 OpenConfig Models 

 BGP 

 BGP Behavior 

 Manage BGP Routes 

 Firewall Zones 

 Firewall Zones Behavior 

 Manage Firewall Zones 

 High Availabilty 

 High Availability Behavior 

 Manage High Availability 

 Interfaces 

 Interfaces Behavior 

 Manage Interfaces 

 LACP 

 LACP Behavior 

 Manage LACP 

 LLDP 

 LLDP Behavior 

 Manage LLDP 

 Local Routes 

 Local Routes Behavior 

 Manage Local Routes 

 Network Instances 

 Network Instances Behavior 

 Manage Network Instances 

 OSPF Version 2 

 OSPF Version 2 Behavior 

 Manage OSPF Version 2 

 Platform 

 Platform Behavior 

 Manage Platform 

 Routing Policy 

 Routing Policy Behavior 

 Manage Routing Policies 

 System 

 System Behavior 

 Manage System 

 VLAN 

 VLAN Behavior 

 Manage VLANs 

 Telemetry Streaming 

 OpenConfig Telemetry on PAN-OS 

 Manage OSPF Version 2 

 How to automate OSPF Version 2 settings on PAN-OS with OpenConfig models. 

 PAN-OS supports the openconfig-ospfv2
model which enables you to manage OSPF Version 2 settings on a virtual
router from your client. 

 Enable OSPF 

 The following command enables
OSPF and sets the router-id: 

 gnmic set --update "/network-instances/network-instance[name=demo_vr]/protocols/protocol[name=ospfv2]/config/enabled:::bool:::true" --update "/network-instances/network-instance[name=demo_vr]/protocols/protocol[name=ospfv2]/ospfv2/global/config/router-id:::string:::1.1.1.1" 

 A
successful response returns: 

{
 "results": [
 {
 "operation": "UPDATE",
 "path": "network-instances/network-instance[name=openconfig-test]/protocols/protocol[name=ospfv2]/config/enabled"
 },
 {
 "operation": "UPDATE",
 "path": "network-instances/network-instance[name=openconfig-test]/protocols/protocol[name=ospfv2]/ospfv2/global/config/router-id"
 }
 ],
 "time": "2021-06-18T15:23:11.754703221-07:00",
 "timestamp": 1624054991754703221
}

 To follow the rest of the examples, add interfaces
ethernet1/4 & ethernet1/4.1 a to virtual-router. See Manage Network Instances for more
examples. 

 Setting OSPF Options 

 The following command
enables graceful-restart and helper-mode. 

 gnmic set --log --update-path "/network-instances/network-instance[name=demo_vr]/protocols/protocol[name=ospfv2]/ospfv2/global/graceful-restart/config" --update-file "graceful_restart.json" 

 The
following is the contents of graceful-restart.json: 

 { "enabled": true, "helper-only": true} 

 A
successful response returns: 

{
 "results": [
 {
 "operation": "UPDATE",
 "path": "network-instances/network-instance[name=openconfig-test]/protocols/protocol[name=ospfv2]/ospfv2/global/graceful-restart/config"
 }
 ]
}

 The image below shows the checked Enable
Graceful Restart and Enable Helper Mode after
the commands. 

 The
following command sets the default-metric: 

 gnmic set --log --update "/network-instances/network-instance[name=demo_vr]/protocols/protocol[name=ospfv2]/config/default-metric:::int:::116" 

 A
successful response returns: 

{
 "results": [
 {
 "operation": "UPDATE",
 "path": "network-instances/network-instance[name=openconfig-test]/protocols/protocol[name=ospfv2]/config/default-metric"
 }
 ]
}

 The following command sets the LSA-generation
and SPF delays: 

 gnmic set --log --update "/network-instances/network-instance[name=demo_vr]/protocols/protocol[name=ospfv2]/ospfv2/global/timers/spf/config/initial-delay:::int:::3" --update "/network-instances/network-instance[name=demo_vr]/protocols/protocol[name=ospfv2]/ospfv2/global/timers/lsa-generation/config/initial-delay:::int:::4" 

 A
successful response returns: 

{
 "results": [
 {
 "operation": "UPDATE",
 "path": "network-instances/network-instance[name=openconfig-test]/protocols/protocol[name=ospfv2]/ospfv2/global/timers/spf/config/initial-delay"
 },
 {
 "operation": "UPDATE",
 "path": "network-instances/network-instance[name=openconfig-test]/protocols/protocol[name=ospfv2]/ospfv2/global/timers/lsa-generation/config/initial-delay"
 }
 ]
}

 Creating an Area 

 The following command
creates an area and adds interfaces ethernet1/4 and ethernet1/4.1: 

 gnmic set --log --update-path "/network-instances/network-instance[name=demo_vr]/protocols/protocol[name=ospfv2]/ospfv2/areas/area[identifier=0.0.0.0]/interfaces" --update-file "/Users/pbadhan/oc/ospf/add_interface_to_area.json" 

 The
following is the contents of the add_interface_to_area.json file: 

{
 "interface": [
 {
 "config": {
 "id": "ethernet1/4",
 "network-type": "NON_BROADCAST_NETWORK"
 },
 "id": "ethernet1/4",
 "interface-ref": {
 "config": {
 "interface": "ethernet1/4"
 }
 }
 },
 {
 "config": {
 "id": "ethernet1/4.1",
 "network-type": "NON_BROADCAST_NETWORK"
 },
 "id": "ethernet1/4.1",
 "interface-ref": {
 "config": {
 "interface": "ethernet1/4",
 "subinterface": 1
 }
 }
 }
 ]
}

 The default values for network type are
broadcast. 

 A successful response returns: 

{
 "results": [
 {
 "operation": "UPDATE",
 "path": "network-instances/network-instance[name=openconfig-test]/protocols/protocol[name=ospfv2]/ospfv2/areas/area[identifier=0.0.0.0]/interfaces"
 }
 ]
}

 Configuring Neighbors and Virtual Links 

 The
following command adds a neighbor with router-id 1.1.1.10 to interface
ethernet1/4.1: 

 gnmic set --log --update "/network-instances/network-instance[name=demo_vr]/protocols/protocol[name=ospfv2]/ospfv2/areas/area[identifier=0.0.0.0]/interfaces/interface[id=ethernet1/4.1]/neighbors/neighbor[router-id=1.1.1.10]/config/router-id:::string:::1.1.1.10" 

 A
successful response returns: 

{
 "results": [
 {
 "operation": "UPDATE",
 "path": "network-instances/network-instance[name=openconfig-test]/protocols/protocol[name=ospfv2]/ospfv2/areas/area[identifier=0.0.0.0]/interfaces/interface[id=ethernet1/4.1]/neighbors/neighbor[router-id=1.1.1.10]/config/router-id"
 }
 ]
}

 The
following command configures a virtual link to the 1.1.1.1 area. 

 set --log --update "/network-instances/network-instance[name=demo_vr]/protocols/protocol[name=ospfv2]/ospfv2/areas/area[identifier=1.1.1.1]/virtual-links/virtual-link[remote-router-id=2.2.2.2]/config/remote-router-id:::string:::2.2.2.2" 

 A
successful response returns: 

{
 "results": [
 {
 "operation": "UPDATE",
 "path": "/network-instances/network-instance[name=demo_vr]/protocols/protocol[name=ospfv2]/ospfv2/areas/area[identifier=1.1.1.1]/virtual-links/virtual-link[remote-router-id=2.2.2.2]/config/remote-router-id:::string:::2.2.2.2"
 }
 ]
}

 Retrieving OSPF Settings 

 The following
command retrieves the settings and shows all of the relevant updates
that were set using the configuration above. 

 gnmic -a firewall:9339 -e JSON_IETF set --update --path /network-instances/network-instance[name=openconfig-test]

 PAN-OS only enables you to retrieve settings
for OSPFv2 from the network instance level. 

 Previous 

 OSPF Version 2 Behavior 

 Next 

 Platform 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
