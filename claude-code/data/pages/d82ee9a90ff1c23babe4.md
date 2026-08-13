---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/ion-cli-reference/use-cli-commands/inspect-commands/inspect-flow-internal
fetched_at: 2026-08-13T17:30:53Z
source: palo-alto-main
---

# inspect flow internal Clear

inspect flow internal 

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

 inspect flow internal 

 Updated on 

 Tue Jun 02 09:34:24 PDT 2026 

 Focus 

 Download PDF 

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

 Updated on 

 Tue Jun 02 09:34:24 PDT 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Use CLI Commands 

 Inspect Commands 

 inspect flow internal 

 Download PDF 

 Prisma SD-WAN 

 inspect flow internal 

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

 inspect flow detail 

 Next 

 inspect interface stats 

 inspect flow internal 

 Use the inspect flow internal command
to display the details of flows that match the input filter. It
displays existing flows and their path, along with information on
applications and attached interfaces. 

 Command 

 inspect flow internal (srcv4= src-ipv4 | dstv4=dst-ipv4 | srcport=src-port | dstport=dst-port | prot-nm=(udp | tcp | icmp) | prot-no= 0 - 255) 

 Options 

 srcv4 Enter the source IP address. 

 dstv4 Enter the destination IP address. 

 srcport Enter the source port. 

 dstport Enter the destination port. 

 prot-nm Tab to select UDP, TCP, or ICMP. 

 prot-no Enter a protocol number ranging from 0 - 255. 

 Command Notes 

 Role Super, Read Only 

 Related Commands — 

 Introduced in Release 5.0.3 

 Example 

 inspect flow internal
 FLOW DETAILS :
 app_id : 16150106802370049
 app_idle_timeout : 20
 app_iface_cookie : 0
 attached_iface_1 : 
 type: FC_DP_IFACE_LAN 
 name: ethr3 
 vlan_id: 0 
 alt_vlan_id: 0 
 signature: 0xdeadcafe (-559035650) 
 dp_fid: 39 
 cookie: 0 
 policy_action 
 tos: 0 
 out_port_name: bwc_out_1 
 push_vlan_id: 0 
 queue_id: 2097187 
 idle_timeout: 20 
 insert_flow: 1 
 policy_action_flags: 0 
 cookie: 0 
 nw_src: 0.0.0.0 
 nw_dst: 0.0.0.0 
 src_eth_addr: 00:00:00:00:00:00, 
 dst_eth_addr: 00:00:00:00:00:00,
 attached_iface_2 : 
 type: FC_DP_IFACE_WAN 
 name: tnl-1 
 vlan_id: 0 
 alt_vlan_id: 0 
 signature: 0xdeadcafe (-559035650) 
 dp_fid: 43 
 cookie: 0 
 policy_action 
 tos: 0 
 out_port_name: bwc_in_1 
 push_vlan_id: 0 
 queue_id: 2097187 
 idle_timeout: 20 
 insert_flow: 1 
 policy_action_flags: 0 
 cookie: 2 
 nw_src: 0.0.0.0 
 nw_dst: 0.0.0.0 
 src_eth_addr: 00:00:00:00:00:00, 
 dst_eth_addr: 00:00:00:00:00:00,
 byte_count : 0
 cookie : 4
 detected_app_count : 0
 dport : 0
 dropped_cookie : 0
 dscp : --
 dst : 192.168.20.100
 dst_vlan_id : 0
 expire_time : 430123
 flow_count : 4
 flow_drop_reason : not dropped
 flow_type : NORMAL
 id : 35
 idle_timeout : 20
 iface_count : 4
 lan2_type : lan-unknown
 lan_type : spoke-lan
 ln_id : 16200275524390210
 loopback_to_edge_fid : 0
 meta_packet_count : 1
 mp_vlan_id : 0
 nat_nw_src : 0
 nctx_id : 0
 net_dpf_id : 0
 net_nctx_id : 0
 net_policy_name : Rule 1
 net_spf_id : 0
 other_pkt_count : 2
 other_sec_state_valid : 1
 packet_count : 0
 path_type : lan_to_public_vpn
 prefix_iface_cookie : 0
 prefix_mask : 827453603864
 prev_flow_path_type : unknown_flow_path
 prev_flow_type : NORMAL
 pri_dpf_id : 0
 pri_nctx_id : 0
 pri_policy_name : icmp-ping-Policy
 pri_spf_id : 0
 priority : 2
 protocol : 1
 refcnt : 2
 security_policy : 
 sec_stack_id : 16242998621490011 
 sec_app_count : 1 
 sec_app : 
 sec_rule_index : 0 
 sec_action : ALLOW 
 sec_result_count : 1 
 sec_result : 
 sec_src_id : 16200275524390210 
 sec_dst_id : 100 
 sec_src_zone_id : 16200471619100074 
 sec_dst_zone_id : 16204672468290016 
 sec_action : ALLOW 
 sec_rule_id : 16246315738930189 
 sec_rule_num : 1 
 sec_rule_app_count : 0
 set_flags : is_src_lan is_src_origis_lan_to_wan is_eps is_dst_wan is_dst_server is_fast_path is_matured_flow is_icmp_req_orig is_icmp_ping_app bwc_enabled non_port_scanning app_detection_done update_stats
 sport : 8
 src : 192.168.7.100
 src_vlan_id : 0
 start_time : 2021-08-11 01:21:02
 state : ESTABLISHED
 term_app_id : 16150106802370049
 traffic_typ : xact
 tuple : 192.168.7.100 > 192.168.20.100: icmp,
 update_priority : 0
 wan2_type : wan-unknown
 wan_path_change_count : 0
 wan_path_id : 16261257799450062
 wan_type : public-vpn-wan 

 Previous 

 inspect flow detail 

 Next 

 inspect interface stats 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Activate a License or Product 

 Cloud Identity Engine 

 Hub 

 Identity and Access Management 

 Tenant Management 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 AI-Powered ADEM 

 Prisma Access Monitoring and Visibility 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 FedRAMP 

 Prisma SASE for FedRAMP 

 Hardware Reference 

 ION 1000 

 ION 1200 

 ION 1200-S 

 ION 2000 

 ION 3000 

 ION 3200 and ION 3200H 

 ION 5200 

 ION 7000 

 ION 9000 

 ION 9200 

 Hardware Quick Start Guides 

 ION 1200 

 ION 1200 4G 

 ION 1200 5G 

 ION 1200-S 

 ION 1200-S 4G 

 ION 1200-S 5G 

 ION 3200 

 ION 3200H 

 ION 3200H 5G 

 ION 5200 

 ION 9200 

 Virtual ION Deployment 

 Virtual ION on AWS 

 Virtual ION on Azure 

 Virtual ION on GCP 

 Virtual ION on Alibaba Cloud 

 Virtual ION on KVM for NFV 

 Virtual ION on OCI 

 Virtual ION on VMware 

 Virtual ION on Megaport Virtual Edge 

 Virtual ION on Dell PowerEdge 

 Prisma SD-WAN Integration 

 AWS Cloud-WAN Integration (GRE Connect) 

 AWS Cloud-WAN Integration (Tunnel-less Connect) 

 Checkpoint Integration 

 LiveAction Integration 

 Netskope Integration 

 Symantec Web Security Services Integration 

 Prisma SD-WAN Experts Corner 

 Network Policy 

 QoS Whitepaper 

 Security Architecture Whitepaper 

 External Antennas for ION-C Series 

 Dynamic Path Selection 

 Best Practices 

 Best Practices Library 

 Resources 

 All Products A - Z 

 Compatibility Matrix 

 SASE 

 CLI 

 Reference 

 Prisma SASE 

 Prisma SD-WAN ION CLI Reference 

 Prisma SD-WAN 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
