---
url: https://docs.paloaltonetworks.com/openconfig/1-3/openconfig-admin/openconfig-models/lldp/manage-lldp
fetched_at: 2026-08-13T16:57:28Z
source: palo-alto-main
---

# Manage LLDP Clear

Manage LLDP 

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
 Manage LLDP 

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

 LLDP 

 Manage LLDP 

 Download PDF 

 PAN-OS OpenConfig Administrator’s Guide 

 Manage LLDP 

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

 Manage LLDP 

 Getting started using openconfig-lldp data model. 

 Review the
 LLDP YANG deviation file before
 using the openconfig-lldp model to familiarize yourself with supported
 paths.

 Globally Enable LLDP 

 The example shows
 a gNMI call that globally enables LLDP: 

 gnmic -a 10.1.1.1
 --port 9339 -u admin -p password --skip-verify -e JSON_IETF --timeout
 300s set --update /lldp/enabled:::bool:::true 

 A successful
 update request returns: 

 Set Response:
 {
 "timestamp": 1619041389507147469,
 "time": "2021-04-21T14:43:09.507147469-07:00",
 "results": [
 {
 "operation": "UPDATE",
 "path": "lldp/enabled"
 }
 ]
 } 

 Enable LLDP for Aggregate Interface 

 This
 example shows a gNMI call that enables an individual aggregate ethernet
 interface. 

 gnmic -a 10.1.1.1 --port 9339 -u admin -p
 password --skip-verify -e JSON_IETF --timeout 300s set --update /lldp/interfaces/interface[name=ae1]/enabled:::bool:::true 

 A
 successful update request returns: 

 {
 "timestamp": 1619041489486221608,
 "time": "2021-04-21T14:44:49.486221608-07:00",
 "results": [
 {
 "operation": "UPDATE",
 "path": "lldp/interfaces/interface[name=ae1]/enabled"
 }
 ]
 }

 Retrieving LLDP Configuration 

 You can
 retrieve LLDP state information and global configuration information
 by using the following command: 

 gnmic -a 10.1.1.1 --port
 9339 -u admin -p password --skip-verify -e JSON_IETF --timeout 300s
 get --path /lldp/ 

 [
 {
 "timestamp": 1619040961585845211,
 "time": "2021-04-21T14:36:01.585845211-07:00",
 "updates": [
 {
 "Path": "lldp",
 "values": {
 "lldp": {
 "config": {
 "enabled": false,
 "hello-timer": "30"
 },
 "openconfig-lldp:interfaces": {
 "interface": [
 {
 "config": {
 "enabled": true,
 "name": "ae1"
 },
 "name": "ae1",
 "state": {
 "counters": {
 "frame-discard": "0",
 "frame-error-in": "0",
 "frame-error-out": "0",
 "frame-in": "0",
 "frame-out": "0",
 "tlv-discard": "0"
 },
 "enabled": true,
 "name": "ae1"
 }
 }, Truncated 

 Previous 

 LLDP Behavior 

 Next 

 Local Routes 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
