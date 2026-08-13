---
url: https://docs.paloaltonetworks.com/strata-logging-service/log-reference/network-logs/network-decryption-log/network-decryption-syslog-fields
fetched_at: 2026-08-13T17:40:19Z
source: palo-alto-main
---

# Decryption Syslog Default Field Order Clear

Decryption Syslog Default Field Order 

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

 Decryption Syslog Default Field Order 

 Updated on 

 Fri Jul 03 02:04:39 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Strata Logging Service Docs 

 Activation & Onboarding 

 Administration 

 Release Notes 

 Log Reference 

 New Features 

 Updated on 

 Fri Jul 03 02:04:39 PDT 2026 

 Focus 

 Home 

 Strata Logging Service 

 Strata Logging Service Log Reference 

 Network Logs 

 Decryption 

 Decryption Syslog Default Field Order 

 Download PDF 

 Strata Logging Service 

 Decryption Syslog Default Field Order 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Strata Logging Service Docs 

 Activation & Onboarding 

 Administration 

 Release Notes 

 Log Reference 

 New Features 

 Previous 

 Decryption 

 Next 

 Decryption CEF Fields 

 Decryption Syslog Default Field Order 

 Example Decryption log in Syslog:

 Oct 13 01:11:28 gke-standard-cluster-2-pool-1-6ea9f13a-moqf 1124 <142>1 2020-10-13T01:11:28.247Z stream-logfwd20-156653024-10121421-eq28-harness-16kn logforwarder - panwlogs - 1,​2020-10-13T01:11:23.000000Z,​007051000113358,​,​DECRYPTION,​10.0,​2020-10-13T01:11:05.000000Z,​xxx.xx.x.xx,​xxx.xx.x.xx,​xxx.xx.x.xx,​xxx.xx.x.xx,​deny-attackers,​00000000000000000000ffff05050505,​paloaltonetwork\xxxxx,​mcafee-endpoint-encryption,​vsys1,​ethernet4Zone-test3,​datacenter,​,​,​rs-logging,​2020-10-13T01:11:05.000000Z,​999250,​1,​28790,​18368,​31621,​27853,​3072,​tcp,​allow,​GRE,​,​,​,​,​85c1488d-5bbd-42e7-8f28-a19256972c32,​unknown,​unknown,​TLS1.3,​ECDHE,​AES_128_GCM,​SHA256,​,​sect409k1,​None,​Untrusted,​Uninspected,​Broker,​14ff0117d825393ebcad2bbfb94bc282da926a7a,​6263d82e0ec3d57c209151526dc1240cc19ec2e685fbae4c81f394e9819a7699,​1602551466,​1605143466,​V2,​192,​23,​32,​32,​21,​64,​CN = MGMT-GROUP-MGMT-CA,​CN = Thawte Premium Server CA1,​CN = Thawte Premium Server CA1,​devop-host.panw.local,​,​1873cc5c-0d31,​pns_default,​pan-dp-77754f4,​,​,​,​,​2020-10-13T01:11:06.359000Z,​H-Phone,​h-profile,​Pro,​Huawei,​Mate 10,​Android v6.1,​pan-411,​264754728121,​H-Phone,​h-profile,​ANE-LX3,​Huawei,​P20 Lite,​Android v7.1,​pan-431,​496310767571,​111291,​-9223372036854775808 

 The following identifies the default field order for filters 

 migrated from an earlier version of the log forwarding application. 

 For log filters created after that migration, you specify the field order when you

 create a log filter 

 by specifying the columns you want to receive.

 The fields are identified in the default order that they appear in each log
 line.

 HEADER, log_time , log_source_id , log_type.​value , sub_type.​value , config_version.​value , time_generated , source_ip.​value , dest_ip.​value , nat_source.​value , nat_dest.​value , rule_matched , source_user , dest_user , app , vsys , from_zone , to_zone , inbound_if.​value , outbound_if.​value , log_set , time_received_mp , session_id , count_of_repeats , source_port , dest_port , nat_source_port , nat_dest_port , flags, protocol.​value , action.​value , tunnel.​value , EMPTY, EMPTY, source_uuid , dest_uuid , rule_matched_uuid , client_to_firewall.​value , firewall_to_client.​value , tls_version.​value , tls_keyxchange.​value , tls_enc_algorithm.​value , tls_auth.​value , policy_name , elliptic_curve.​value , error_index.​value , root_status.​value , chain_status.​value , proxy_type.​value , cert_serial , fingerprint , not_before , not_after , certificate_version.​value , certificate_size , cn_len , issuer_len , root_cn_len , sni_len , cert_flags , cn , issuer_cn , root_cn , sni , error_message , container_id , pod_namespace , pod_name , source_edl , dest_edl , source_dynamic_address_group , dest_dynamic_address_group , time_generated_high_res , source_device_category , source_device_profile , source_device_model , source_device_vendor , source_device_osfamily , source_device_osversion , source_device_host , source_device_mac , dest_device_category , dest_device_profile , dest_device_model , dest_device_vendor , dest_device_osfamily , dest_device_osversion , dest_device_host , dest_device_mac , sequence_no , action_flags 

 Previous 

 Decryption 

 Next 

 Decryption CEF Fields 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Activate a License or Product 

 Identity and Access Management 

 Next-Generation Firewalls 

 AIOps for NGFW 

 Cloud Management for NGFWs 

 Cloud NGFW for AWS 

 Cloud NGFW for Azure 

 CN-Series 

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 Service Provider 

 VM-Series 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 AI-Powered ADEM 

 Prisma Access Monitoring and Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

 Cloud-Delivered Security Services 

 Advanced WildFire 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 Device Security 

 Enterprise DLP 

 SaaS Security 

 Endpoints 

 GlobalProtect 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Security Operations 

 Log Reference 

 Strata Logging Service 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
