---
url: https://docs.paloaltonetworks.com/strata-logging-service/log-reference/network-logs/network-url-log/network-url-syslog-fields
fetched_at: 2026-08-13T17:40:37Z
source: palo-alto-main
---

# URL Syslog Default Field Order Clear

URL Syslog Default Field Order 

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

 URL Syslog Default Field Order 

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

 URL 

 URL Syslog Default Field Order 

 Download PDF 

 Strata Logging Service 

 URL Syslog Default Field Order 

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

 URL 

 Next 

 URL CEF Fields 

 URL Syslog Default Field Order 

 Example URL log in Syslog:

 Oct 13 20:56:15 gke-standard-cluster-2-pool-1-6ea9f13a-fnid 394 <142>1 2020-10-13T20:56:15.519Z stream-logfwd20-156653024-10121421-eq28-harness-16kn logforwarder - panwlogs - Palo Alto Networks,​firewall,​013201004706,​PA-5220,​22229,​2019-07-03T00:05:03.000000Z,​-2021464963,​3,​THREAT,​1,​url,​xxx.xx.x.xx,​00000000000000000000ffff0a365c38,​57085,​xxx.xx.x.xx,​00000000000000000000ffff0a65023e,​8080,​6,​tcp,​,​PA-5220,​0,​client to server,​sjccbovw01p:8080,​1,​,​1,​get,​\"\u001B\t\u0003 hL\"\"Z}u\u0015\",​sjccbovw01p:8080/BOE/portal/1606170029/InfoView/DataLoader?notification=true&usercurrenttime=2019-7-2%2017:4&usertimezoneoffset=-7:00,​https%253A%252F%252Fconsole.cloud.google.com%252Fdataflow%252FjobsDetail%252Flocations%252Fus-central1%252Fjobs%252F2019-08-09_20_00_42-9931281171472243776%253Fproject%253Drepl-prd1-eu%2526organizationId%253D992524860932,​1,​https,​80,​console.cloud.google.com,​/dataflow/jobsDetail/locations/us-central1/jobs/2019-08-09_20_00_42-9931281171472243776,​\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,​ like Gecko) Chrome/xxx.xx.x.xx Safari/537.36\",​,​1,​Informational,​Informational,​,​0,​0,​10077,​private-ip-addresses,​,​4,​alert,​-6917529027641081856,​web-browsing,​general-internet,​3\r\n4\r\n5\r\n6\r\n8,​\" Ezajw*{\u0000}`\",​12,​0,​0,​0,​,​xxx.xx.x.xx-xxx.xx.x.xx,​,​,​\"e y@i\u0003AQ\u0011\u0011c'H\r \",​,​false,​true,​tap,​,​ethernet,​1181132783616,​0,​0,​ethernet,​1,​19,​false,​false,​false,​false,​test,​\")\nq\u0010~\u0016C\u001F\",​0,​xxx.xx.x.xx,​00000000000000000000ffff00000000,​0,​xxx.xx.x.xx,​00000000000000000000ffff00000000,​8080,​ethernet,​1181132783616,​0,​0,​ethernet,​1,​19,​0,​\"WkuL0\n,​[Cr\",​1,​4,​dg-log-policy,​,​false,​6708774908183291111,​4189227,​,​xxx.xx.x.xx-xxx.xx.x.xx,​R9/k!`>\u0017:TN,​,​internet-utility,​browser-based,​2019-08-15T03:05:54.000000Z,​tap,​0,​N/A,​tunneled-app,​0,​xxx.xx.x.xx,​1,​vsys1,​\"\r\u0007\u001F+#c\bw\",​-1004264700,​,​1093632,​false,​false,​true,​false,​false,​false,​true,​false,​false,​false,​false,​false,​false,​false,​false,​false,​false,​,​\"eef3\u001A\u0012\\ozM\u0015>\u000E\u0003\",​,​\"S/!]\u000B\u0017\"\"r38\",​,​\"p<[<L\t(,​\",​,​,​,​,​,​,​,​\"\tm\u0004Pq<\u00066uJq\n\",​ujm@\u000Ek*Ggl6,​,​,​,​;H;jyv\\\u0016\u0000S,​,​,​,​\"j6u7^ ,​\u0015\b\u0016S~\u000E&\",​,​,​\":\u0018\r\u0006\u0016*-y\u0002OQN\",​,​\"\u0000#ROK4e \r\u0004DD\u0000\",​1551419174186411220,​,​,​-537061822,​,​^ \u0002@nRq\u001DxZ!w,​;nTVmp=H\u001CCQ\u0000O,​,​,​,​,​,​,​ 

 The following identifies the default field order for filters 

 migrated from an earlier version of the log forwarding application. 

 For log filters created after that migration, you specify the field order when you

 create a log filter 

 by specifying the columns you want to receive.

 The fields are identified in the default order that they appear in each log
 line.

 HEADER, log_time , log_source_id , log_type.​value , sub_type.​value , config_version.​value , time_generated , source_ip.​value , dest_ip.​value , nat_source.​value , nat_dest.​value , rule_matched , source_user , dest_user , app , vsys , from_zone , to_zone , inbound_if.​value , outbound_if.​value , log_set , EMPTY, session_id , count_of_repeats , source_port , dest_port , nat_source_port , nat_dest_port , flags, protocol.​value , action.​value , uri , EMPTY, url_category.​value , vendor_severity.​value , direction_of_attack.​value , sequence_no , action_flags, source_location , dest_location , EMPTY, content_type , pcap_id , EMPTY, EMPTY, url_idx , user_agent , EMPTY, xff , referer , EMPTY, EMPTY, EMPTY, EMPTY, dg_hier_level_1 , dg_hier_level_2 , dg_hier_level_3 , dg_hier_level_4 , vsys_name , log_source_name , EMPTY, source_uuid , dest_uuid , http_method.​value , tunnelid_imsi , monitor_tag_imei , parent_session_id , parent_start_time , tunnel.​value , inline_ml_verdict.​value , content_version , sig_flags , EMPTY, EMPTY, http_headers , url_category_list , rule_matched_uuid , http2_connection , dynusergroup_name , xff_ip.​value , source_device_category , source_device_profile , source_device_model , source_device_vendor , source_device_osfamily , source_device_osversion , source_device_host , source_device_mac , dest_device_category , dest_device_profile , dest_device_model , dest_device_vendor , dest_device_osfamily , dest_device_osversion , dest_device_host , dest_device_mac , container_id , pod_namespace , pod_name , source_edl , dest_edl , gp_host_id , endpoint_serial_number , domain_edl, source_dynamic_address_group , dest_dynamic_address_group , partial_hash, time_generated_high_res , EMPTY, EMPTY, nssai_network_slice_type.​value 

 Previous 

 URL 

 Next 

 URL CEF Fields 

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
