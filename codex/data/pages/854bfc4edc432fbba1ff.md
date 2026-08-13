---
url: https://docs.paloaltonetworks.com/openconfig/2-0/openconfig-admin/openconfig-models/high-availabilty
fetched_at: 2026-08-13T16:57:45Z
source: palo-alto-main
---

# High Availabilty Clear

High Availabilty 

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
 High Availabilty 

 Updated on 

 Wed Jan 29 11:45:21 PST 2025 

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

 Wed Jan 29 11:45:21 PST 2025 

 Focus 

 Home 

 OpenConfig 

 PAN-OS OpenConfig Administrator’s Guide 

 OpenConfig Models 

 High Availabilty 

 Download PDF 

 PAN-OS OpenConfig Administrator’s Guide 

 High Availabilty 

 Table of Contents 

 Filter

 Version 

 2.0 

 2.0 

 2.0 & Later 

 1.3 

 1.2 

 1.1 

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

 High Availabilty 

 Learn about the high availability concept, including using openconfig-hagroups model with the PAN-OS OpenConfig plugin. 

 Review the deviation file before using the
 openconfig-hagroups model to familiarize yourself with supported paths. 

 When using the openconfig-hagroups model: 

 Only active-passive mode is supported. 

 Preemptive Hold Time is defined in milliseconds. 

 LinkMonitorEnable is enabled by default. 

 ApPassingLinkState is set to auto by default. 

 Configure HA Settings 

 The following command updates various high availability settings on the
 firewall: 

gnmic -a firewall:9339 -e JSON_IETF set --update-path "/" --update-file highavailability.json

 Only the interfaces of type HA are currently supported
 with this model. 

 {
 "ha-groups": {
 "ha-group": [
 {
 "id": 1,
 "config": {
 "id": 1,
 "ha-enabled": true,
 "ha-mode": "ACTIVE_PASSIVE"
 },
 "control-link": {
 "config": {
 "control-link-interface": "ethernet1/7",
 "control-link-ipv4": "192.168.1.16/31",
 "control-link-peer-ipv4": "192.168.1.17/31"
 }
 },
 "data-link": {
 "data-link-interface": "ethernet1/16",
 "data-link-ipv4": "192.168.1.20/31"
 }
 }
 ]
 }
} 

 A successful update returns the following output: 

Set Response:
{
 "timestamp": 1625780831682622866,
 "time": "2021-07-08T14:47:11.682622866-07:00",
 "results": [
 {
 "operation": "UPDATE"
 }
 ]
}

 The UI displays the following after updating the HA settings. 

 Retrieve HA Settings 

 The following command retrieves the HA Settings currently available on the firewall. 

 gnmic -a firewall:9339 -e JSON_IETF get --path "/ha-groups/ha-group"

 After sending the file above, the output returns the following: 

Timestamp": 1625864679870214721,
 "time": "2021-07-09T14:04:39.870214721-07:00",
 "updates": [
 {
 "Path": "ha-groups",
 "values": {
 "ha-groups": {
 "ha-group": [
 {
 "config": {
 "global-health-policy": "ANY",
 "ha-config-sync": false,
 "ha-enabled": true,
 "ha-mode": "ACTIVE_PASSIVE",
 "ha-msg-encryption": false,
 "ha-session-sync": false,
 "hello-interval": 8000,
 "id": 1,
 "preempt": false,
 "preempt-hold-timer": 60000
 },
 "control-link": {
 "config": {
 "control-link-interface": "ethernet1/7",
 "control-link-ipv4": "192.168.1.16/31",
 "control-link-peer-ipv4": "192.168.1.17/31"
 },
 "state": {
 "control-link-interface": "ethernet1/7",
 "control-link-ipv4": "192.168.1.16/31",
 "control-link-peer-ipv4": "192.168.1.17/31"
 }
 },
 "data-link": {
 "config": {
 "data-link-interface": "ethernet1/16",
 "data-link-ipv4": "192.168.1.20/31"
 },
 "state": {
 "data-link-interface": "ethernet1/16",
 "data-link-ipv4": "192.168.1.20/31"
 }
 },
 "id": 1,
 "state": {
 "global-health-policy": "ANY",
 "global-health-status": "DOWN",
 "ha-config-sync": false,
 "ha-enabled": true,
 "ha-mode": "ACTIVE_PASSIVE",
 "ha-msg-encryption": false,
 "ha-session-sync": false,
 "ha-state": "ACTIVE",
 "ha-state-last-change": "83787",
 "hello-interval": 8000,
 "id": 1,
 "preempt": false,
 "preempt-hold-timer": 60000
 }
 }
 ]
 }
 }
 }
 ]
 }
]

 Delete HA Settings 

 The following command deletes the HA settings previously set on the firewall. 

gnmic -a firewall:9339 -e JSON_IETF delete --path "ha-groups"

 Previous 

 Interfaces 

 Next 

 LACP 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
