---
url: https://docs.paloaltonetworks.com/openconfig/1-3/openconfig-admin/openconfig-models/vlan/manage-vlans
fetched_at: 2026-08-13T16:57:38Z
source: palo-alto-main
---

# Manage VLANs Clear

Manage VLANs 

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
 Manage VLANs 

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

 1.0 

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

 VLAN 

 Manage VLANs 

 Download PDF 

 PAN-OS OpenConfig Administrator’s Guide 

 Manage VLANs 

 Table of Contents 

 Filter

 Version 

 1.3 

 1.3 

 1.2 

 1.1 

 1.0 

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

 Manage VLANs 

 Examples of how to use the VLAN OpenConfig model with
 PAN-OS. 

 Adding Layer 2 Interfaces to a VLAN 

 The
 example below shows a gNMI call that adds ethernet1/6 to VLANs 15
 and 16 and VLAN 17 for untagged ethernet frames. 

 gnmic
 set -a 10.1.1.1:9339 -u username -p password --skip-verify --replace-path /interfaces/interface[name=ethernet1/6]/ethernet/switched-vlan
 --replace-file vlan1.json -e JSON_IETF --timeout 300s 

 Below
 is the contents of the JSON file used to add the interface to the
 VLAN. 

 {
 "trunk-vlans": [15,16],
 "native-vlan": 17
 }

 The plugin returns the following response after
 a successful update: 

 {
 "timestamp": 1618446078899330350,
 "time": "2021-04-14T17:21:18.89933035-07:00",
 "results": [
 {
 "operation": "REPLACE",
 "path": "interfaces/interface[name=ethernet1/7]/ethernet/switched-vlan"
 }
 ]
 }

 PAN-OS's
 OpenConfig behavior automatically adds the interface to the specified
 VLANs, tags the interfaces, sets the interfaces in Layer2 mode,
 and adds the interfaces to the default_l2 security zone. 

 The
 image below shows how the interfaces appear in the VLAN tab. 

 To add another
 interface to the same VLANs you can send the same request for another
 interface. The example below adds ethernet1/7. 

 gnmic
 set -a 10.1.1.1:9339 -u username -p password --skip-verify --debug
 --replace-path /interfaces/interface[name=ethernet1/7]/ethernet/switched-vlan
 --replace-file vlan1.json -e JSON_IETF --timeout 300s 

 {
 "trunk-vlans": [15,16],
 "native-vlan": 17
 }

 The image below shows that the ethernet1/7 is
 added to the same native VLANs and trunk VLANs as ethernet1/6. 

 Adding a Routed VLAN Interface 

 The gNMI
 call below shows how you can create a routed VLAN interface and
 add it to VLAN 17. 

 gnmic set -a 10.1.1.1:9339 -u username
 -p password --skip-verify --debug --update /interfaces/interface[name=vlan.17]/routed-vlan/config/vlan:::int:::17
 -e JSON_IETF 

 Retrieving VLANs 

 Since the VLAN model
 augments the interface model, each of the VLANs appears when you
 do a get call to the /interfaces path. The snippet below shows that
 the only one with a VLAN type is l3ipvlan is the routed VLAN. 

 {
 "config": {
 "description": "",
 "enabled": true,
 "loopback-mode": false,
 "name": "ethernet1/7",
 "tpid": "openconfig-vlan-types:TPID_0X8100",
 "type": "iana-if-type:ethernetCsmacd"
 },
 "openconfig-if-ethernet:ethernet": {
 "config": {
 "auto-negotiate": true,
 "port-speed": "openconfig-if-ethernet:SPEED_UNKNOWN"
 },
 "openconfig-vlan:switched-vlan": {
 "config": {
 "native-vlan": 17,
 "trunk-vlans": [
 15,
 16
 ]
 }
 }
 },
 "openconfig-interfaces:name": "ethernet1/7"
 },
 {
 "config": {
 "description": "",
 "enabled": true,
 "loopback-mode": false,
 "name": "vlan.17",
 "type": "iana-if-type:l3ipvlan"
 },
 "openconfig-interfaces:name": "vlan.17",
 "openconfig-vlan:routed-vlan": {
 "config": {
 "vlan": 17
 },
 "openconfig-if-ip:ipv4": {
 "config": {
 "dhcp-client": false,
 "mtu": 1500
 }
 },
 "openconfig-if-ip:ipv6": {
 "config": {
 "dup-addr-detect-transmits": 0,
 "enabled": false
 },
 "router-advertisement": {
 "config": {
 "interval": 600,
 "lifetime": 1800,
 "suppress": true
 }
 }
 }

 Previous 

 VLAN Behavior 

 Next 

 Telemetry Streaming 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
