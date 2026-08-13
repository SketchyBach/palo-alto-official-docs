---
url: https://docs.paloaltonetworks.com/openconfig/2-0/openconfig-admin/openconfig-models/lldp
fetched_at: 2026-08-13T16:57:46Z
source: palo-alto-main
---

# LLDP Clear

LLDP 

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
 LLDP 

 Updated on 

 Jan 29, 2025 

 Focus 

 Download PDF 

 Filter

 Version 

 2.0 

 2.0 

 2.0 & Later 

 1.3 

 1.2 

 1.1 

 1.0 

 Expand all | Collapse all 

 Getting Started 

 PAN-OS OpenConfig Model Support 

 PAN-OS OpenConfig Dial-Out Support 

 Install the OpenConfig Plugin 

 PAN-OS OpenConfig Wildcard Support 

 PAN-OS OpenConfig Bundling Support 

 Telemetry Streaming 

 OpenConfig Models 

 BGP Usage and Behavior 

 Firewall Zones Usage and Behavior 

 Interfaces 

 High Availabilty 

 LACP 

 LLDP 

 Local Routes 

 Network Instances 

 OSPF Version 2 

 Platform 

 Routing Policy 

 System 

 VLAN 

 PAN-OS Models 

 PAN-OS OpenConfig Logging 

 PAN-OS OpenConfig Config 

 PAN-OS OpenConfig PCAP 

 PAN-OS OpenConfig XML API 

 PAN-OS OpenConfig File Upload 

 Updated on 

 Jan 29, 2025 

 Focus 

 Home 

 OpenConfig 

 PAN-OS OpenConfig Administrator’s Guide 

 OpenConfig Models 

 LLDP 

 Download PDF 

 PAN-OS OpenConfig Administrator’s Guide 

 LLDP 

 Table of Contents 

 Filter

 Version 

 2.0 

 2.0 

 2.0 & Later 

 1.3 

 1.2 

 1.1 

 1.0 

 Expand all | Collapse all 

 Getting Started 

 PAN-OS OpenConfig Model Support 

 PAN-OS OpenConfig Dial-Out Support 

 Install the OpenConfig Plugin 

 PAN-OS OpenConfig Wildcard Support 

 PAN-OS OpenConfig Bundling Support 

 Telemetry Streaming 

 OpenConfig Models 

 BGP Usage and Behavior 

 Firewall Zones Usage and Behavior 

 Interfaces 

 High Availabilty 

 LACP 

 LLDP 

 Local Routes 

 Network Instances 

 OSPF Version 2 

 Platform 

 Routing Policy 

 System 

 VLAN 

 PAN-OS Models 

 PAN-OS OpenConfig Logging 

 PAN-OS OpenConfig Config 

 PAN-OS OpenConfig PCAP 

 PAN-OS OpenConfig XML API 

 PAN-OS OpenConfig File Upload 

 LLDP 

 Getting started with LLDP model using PAN-OS OpenConfig
plugin. 

 Review the deviation file before using the
 openconfig-lldp model to familiarize yourself with supported paths. 

 When using the LLDP model with PAN-OS firewalls: 

 Doing a Get on the lldp/interfaces path retrieves all consolidated information
 for the aggregated ethernet interface members and other interfaces. 

 You can direct gNMI calls to aggregate ethernet interfaces, but not to specific
 members of the aggregate interface. 

 When an interface has LLDP disabled, the interface counters are shown as all
 zeros. 

 Deleting an LLDP configuration will set the /lldp/config/enabled value back to
 false. 

 lldp/state/hello-timer is the transit interval in PAN-OS. 

 Below is the matching of counter from OpenConfig to PAN-OS at the
 lldp/interfaces/interface/state/counters level: 

 OpenConfig fields PAN-OS field 

 frame-in Total Received 

 frame-out Total Transmitted 

 frame-error-in Errors 

 frame-discard Errors 

 tlv-discard Dropped TLV 

 frame-error-out Dropped Transmit 

 Review the LLDP YANG deviation file before using the
 openconfig-lldp model to familiarize yourself with supported paths. 

 Globally Enable LLDP 

 The example shows a gNMI call that globally enables LLDP: 

 gnmic -a 10.1.1.1
 --port 9339 -u admin -p password --skip-verify -e JSON_IETF --timeout
 300s set --update /lldp/enabled:::bool:::true 

 A successful update request returns: 

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

 This example shows a gNMI call that enables an individual aggregate ethernet
 interface. 

 gnmic -a 10.1.1.1 --port 9339 -u admin -p
 password --skip-verify -e JSON_IETF --timeout 300s set --update /lldp/interfaces/interface[name=ae1]/enabled:::bool:::true 

 A successful update request returns: 

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

 You can retrieve LLDP state information and global configuration information by using
 the following command: 

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

 LACP 

 Next 

 Local Routes 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
