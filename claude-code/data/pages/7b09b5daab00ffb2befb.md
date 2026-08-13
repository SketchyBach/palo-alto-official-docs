---
url: https://docs.paloaltonetworks.com/openconfig/2-0/openconfig-admin/pan-os-models/pan-os-openconfig-pcap
fetched_at: 2026-08-13T16:57:52Z
source: palo-alto-main
---

# PAN-OS OpenConfig PCAP Clear

PAN-OS OpenConfig PCAP 

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
 PAN-OS OpenConfig PCAP 

 Updated on 

 Wed Jan 29 11:45:21 PST 2025 

 Focus 

 Download PDF 

 Filter

 Version 

 2.0 

 2.0 

 2.0 & Later 

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

 PAN-OS Models 

 PAN-OS OpenConfig PCAP 

 Download PDF 

 PAN-OS OpenConfig Administrator’s Guide 

 PAN-OS OpenConfig PCAP 

 Table of Contents 

 Filter

 Version 

 2.0 

 2.0 

 2.0 & Later 

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

 PAN-OS OpenConfig PCAP 

 PAN-OS OpenConfig PCAP model support. 

 About the PAN-OS PCAP Model 

 Review the YANG model before using the pan-os pcap
 model, familiarize yourself with supported paths. 

 For more information about taking a custom packet capture on PAN-OS, view the Administrator's Guide . After capturing
 youre desired packets, you can then use a network packet analyzer to review
 information provided by your capture. 

 When using the PCAP model, you can use several custom filters defined in
 the YANG model such as: 
 Source IP Address 

 Source Port 

 Destination IP Address 

 Destination Port 

 Network Protocol 

 You can further filter your results by capping the limit on the PCAP results with
 filters such as: 
 File Size 

 Packet Captured Count 

 Duration 

 For the PCAP model, data_push_url custom endpoint is required. You
 can then use the your endpoint to further process conditions and use the other
 available config models to manipulate your PAN-OS firewall configuration. 

 Only one PCAP job can be running at a time. You can define
 the time for the capture to run using the leaf nodes provided in the data
 model. 

 Using the PAN-OS PCAP Model 

 The following query retrieves a packet capture: 

gnmic -a IP:9339 -u USER -p PASSWORD --mode ONCE subscribe -e json_ietf --skip-verify --path /pan/pcap/config[filter1_destination_port=5353][filter1_destination_port=67][file_size=100][duration=120] 

 The following is an example response following a successful packet
 capture: 

{
 "source": "10.0.0.1:9339",
 "subscription-name": "default-1683208591",
 "timestamp": 1683208595000000000,
 "time": "2023-05-04T06:56:35-07:00",
 "updates": [
 {
 "Path": "/pan/pcap/config",
 "values": {
 "/pan/pcap/config": {
 "code": 200,
 "message": "dial-in: pcap job is done. file name: <snip>.pcap"
 }
 }
 }
 ]
} 

 Previous 

 PAN-OS OpenConfig Config 

 Next 

 PAN-OS OpenConfig XML API 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
