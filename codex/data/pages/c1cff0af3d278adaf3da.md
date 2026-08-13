---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/cortex-xsiam-data-sources/palo-alto-networks-integrations/next-generation-firewall/ingest-next-generation-firewall-logs-using-the-syslog-collector
fetched_at: 2026-08-13T15:02:30Z
source: cortex-platform
---

# Ingest Next-Generation Firewall logs using the Syslog collector | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

Ingest Next-Generation Firewall logs using the Syslog collector | Cortex Documentation Portal 

 ⌘ Ctrl k 

 Blog Support 
 More 

 Home 

 Products 

 Guides 

 Release Notes 

 API 

 Reference 

 AI Assistant 

 Good afternoon 
 I'm here to help you with the docs. 

 What is this page about? What should I read next? Can you give an example? 

 ⌘ Ctrl i 

 AI Based on your context 
 Send 

 Learn about Cortex XSIAM 

 Navigate the Cortex XSIAM docs 

 Get started with Cortex XSIAM 

 Agentic AI in Cortex XSIAM 

 Cortex XSIAM product licenses 

 In-product support ticket creation 

 Supported web browsers 

 Use the interface 

 Manage API keys 

 Onboard Cortex XSIAM 

 How to onboard Cortex XSIAM 

 Plan and prepare 

 Deployment steps 

 Post-deployment 

 Configure Cortex XSIAM 

 Learn how to configure Cortex XSIAM 

 Data management 

 Cortex XSIAM Data Sources and Connectors 

 What are Cortex XSIAM data sources and connectors? 

 Complete data source and connector catalog 

 Vendor-specific data sources and connectors 

 Connectors 

 Standard data sources 

 Cloud service provider (CSP) onboarding 

 Generic on-premise data collectors 

 Palo Alto Networks integrations 

 Cloud Next-Generation Firewall 

 Next-Generation Firewall 

 Ingest data from Next-Generation Firewall 

 Ingest Next-Generation Firewall logs using the Syslog collector 

 Panorama 

 Prisma Access 

 Prisma Access Browser 

 Ingest detection data from Strata Logging Service 

 IoT Security 

 Cortex Attack Surface Management 

 Cortex Automation Developer Tools 

 Cortex Data Lake 

 Cortex Internals 

 Cortex XDR 

 Enterprise DLP 

 Palo Alto Networks Cortex 

 PAN PSIRT Advisories 

 Prisma Cloud Compute 

 Prisma Cloud CSPM 

 SaaS Security (Aperture) 

 Threat Vault 

 WildFire Cloud 

 Log type filtering 

 Collecting URL and File log types 

 Cloud Posture and Runtime Security data sources 

 External alerts using External Issue Mapping 

 Administration and troubleshooting 

 Marketplace 

 Configure the Cortex Agentic Assistant 

 Cortex MCP server 

 Automations 

 Engines 

 Remote repository management 

 Customize cases and issues 

 XQL query management 

 Multi-Tenant 

 Managed Services configuration in Cortex 

 Protect your endpoints 

 Endpoint security 

 Endpoint DLP 

 Detect, Investigate, and respond to threats 

 Monitor dashboards and reports 

 Investigation and response 

 Agentic Assistant chat 

 Asset management 

 Threat management 

 Attack surface management 

 Vulnerability management 

 Exposure management 

 Cortex Advanced Email Security 

 Identity Threat Detection and Response (ITDR) 

 Cloud Security 

 Monitor and track compliance adherence 

 Cloud security rules and policies 

 Cortex Cloud Data Classification 

 Cortex Data Security 

 Cloud Identity Security 

 Network exposure detection 

 Cortex Cloud SaaS Security 

 Cortex Cloud AI Security 

 Serverless function posture security 

 Cortex Cloud Application Security 

 Cloud workload policies and rules 

 Base image rules 

 Web and API Security (WAAS) 

 Serverless function runtime security 

 Reference and developer docs 

 Cortex XSIAM XQL 

 Graph Search 

 Cortex CLI 

 Role-Based Access Control 

 API documentation 

 Reference 

 Migrating to a new Broker VM image 

 Learn more about migrating to the latest broker VM image 

 Standalone Broker VM 

 Broker VM high availability cluster node 

 On this page 

 For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSIAM 

 Cortex XSIAM Documentation 

 Configure Cortex XSIAM 

 Cortex XSIAM Data Sources and Connectors 

 Palo Alto Networks integrations 

 Next-Generation Firewall 

 Ingest Next-Generation Firewall logs using the Syslog collector 

 Use the Syslog collector to ingest Next-Generation Firewall (NGFW) logs in CEF format. This method is useful when your firewalls are located in a different region, or bandwidth issues are encountered due to large log size. When possible, we recommend that you ingest NGFW logs using the dedicated Next-Generation Firewall data collector instead of the Syslog collector. 

 Note 

 In the following procedure, general information is provided for NGFW and Panorama. For detailed instructions, consult the documentation for your specific devices and Panorama version, to ensure that you have configured log forwarding correctly for all the log types that you would like to forward to Cortex XSIAM. The following steps only cover configuration of the custom log schema (CEF) for a given syslog server. They do not replace the administrator guide’s configuration coverage of log forwarding. 

 For tenants where customers have integrated directly with Strata Logging Service, the configured integrations, such as Next-Generation Firewall and Prisma Access, can be migrated to Cortex XSIAM in either of the following ways before the license expires: 

 Configure the firewall/Panorama for log forwarding to Cortex XSIAM 

 To configure the device to include its IP address in the header of Syslog messages, select Panorama/Device → Setup → Management , click the Edit icon in the Logging and Reporting Settings section, and navigate to the Log Export and Reporting tab. 

 From the Syslog HOSTNAME Format menu, select ipv4-address or ipv6-address , and click OK . 

 Select Device → Server Profiles → Syslog , and click Add . 

 Enter a server profile Name and Location ( Location refers to a virtual system, if the device is enabled for virtual systems). 

 On the Servers tab of the Syslog Server Profiles window, click Add, and enter the following information for the Syslog server: 

 Name 

 Syslog Server (IP address) 

 Transport , Port (default 514 for UDP) 

 Facility (default LOG_USER) 

 Select the Custom Log Format tab and click configure the log formats as follows: 

 Note 

 To avoid the possible effects of line formatting, do not copy/paste the message formats directly into the PAN-OS web interface. Instead, paste into a text editor, remove any carriage return or line feed characters, and then copy and paste into the web interface. 

 Note 

 From version 10.0 and later, the log format documented for log types (Traffic, Threat, and URL) exceeds the maximum supported 2048 characters in the Custom Log Format tab on the firewall and Panorama. Select the CEF keys and values to limit the number of characters to 2048, as per your requirements. 

 Log Type 

 Custom Format 

 Traffic 

 CEF:0|PANW|NGFW_CEF|$sender_sw_version|$subtype|$type|1| __firewall_type=firewall.traffic __timestamp=$start __tz=$high_res_timestamp log_type=$type subtype=$subtype log_time=$cef-formatted-receive_time time_generated=$cef-formatted-time_generated log_source_id=$serial log_source_name=$device_name sequence_no=$seqno source_ip=$src dest_ip=$dst source_port=$sport dest_port=$dport nat_source=$natsrc nat_dest=$natdst nat_source_port=$natsport nat_dest_port=$natdport protocol=$proto action=$action source_user=$srcuser dest_user=$dstuser xff_ip=$xff_ip app=$app app_category=$category_of_app app_sub_category=$subcategory_of_app rule_matched=$rule rule_matched_uuid=$rule_uuid severity=1 vsys=$vsys vsys_name=$vsys_name from_zone=$from to_zone=$to inbound_if=$inbound_if outbound_if=$outbound_if session_id=$sessionid source_device_category=$src_category source_device_profile=$src_profile source_device_model=$src_model source_device_vendor=$src_vendor source_device_osfamily=$src_osfamily source_device_osversion=$src_osversion source_device_mac=$src_mac dest_device_category=$dst_category dest_device_profile=$dst_profile dest_device_model=$dst_model dest_device_vendor=$dst_vendor dest_device_osfamily=$dst_osfamily dest_device_osversion=$dst_osversion dest_device_mac=$dst_mac bytes_sent=$bytes_sent bytes_received=$bytes_received packets_received=$pkts_received packets_sent=$pkts_sent total_time_elapsed=$elapsed session_end_reason=$session_end_reason url_category=$category 

 Threat 

 CEF:0|PANW|NGFW_CEF|$sender_sw_version|$threatid|$type|$number-of-severity| __firewall_type=firewall.threat __timestamp=$cef-formatted-time_generated __tz=$high_res_timestamp log_type=$type subtype=$subtype log_time=$cef-formatted-receive_time time_generated=$cef-formatted-time_generated log_source_id=$serial log_source_name=$device_name sequence_no=$seqno source_ip=$src dest_ip=$dst source_port=$sport dest_port=$dport nat_source=$natsrc nat_dest=$natdst nat_source_port=$natsport nat_dest_port=$natdport protocol=$proto action=$action source_user=$srcuser dest_user=$dstuser xff=$xff xff_ip=$xff_ip app=$app app_category=$category_of_app app_sub_category=$subcategory_of_app rule_matched=$rule rule_matched_uuid=$rule_uuid severity=$number-of-severity vsys=$vsys vsys_name=$vsys_name from_zone=$from to_zone=$to inbound_if=$inbound_if outbound_if=$outbound_if session_id=$sessionid source_device_category=$src_category source_device_profile=$src_profile source_device_model=$src_model source_device_vendor=$src_vendor source_device_osfamily=$src_osfamily source_device_osversion=$src_osversion source_device_mac=$src_mac dest_device_category=$dst_category dest_device_profile=$dst_profile dest_device_model=$dst_model dest_device_vendor=$dst_vendor dest_device_osfamily=$dst_osfamily dest_device_osversion=$dst_osversion dest_device_mac=$dst_mac misc=$misc threat_id=$threatid threat_name=$threat_name threat_category=$thr_category direction=$direction user_agent=$user_agent 

 URL 

 CEF:0|PANW|NGFW_CEF|$sender_sw_version|$subtype|$type|$number-of-severity| __firewall_type=firewall.url __timestamp=$cef-formatted-time_generated __tz=$high_res_timestamp log_type=$type subtype=$subtype log_time=$cef-formatted-receive_time time_generated=$cef-formatted-time_generated log_source_id=$serial log_source_name=$device_name sequence_no=$seqno source_ip=$src dest_ip=$dst source_port=$sport dest_port=$dport nat_source=$natsrc nat_dest=$natdst nat_source_port=$natsport nat_dest_port=$natdport protocol=$proto action=$action source_user=$srcuser dest_user=$dstuser xff=$xff xff_ip=$xff_ip app=$app app_category=$category_of_app app_sub_category=$subcategory_of_app rule_matched=$rule rule_matched_uuid=$rule_uuid severity=$number-of-severity vsys=$vsys vsys_name=$vsys_name from_zone=$from to_zone=$to inbound_if=$inbound_if outbound_if=$outbound_if session_id=$sessionid source_device_category=$src_category source_device_profile=$src_profile source_device_model=$src_model source_device_vendor=$src_vendor source_device_osfamily=$src_osfamily source_device_osversion=$src_osversion source_device_mac=$src_mac dest_device_category=$dst_category dest_device_profile=$dst_profile dest_device_model=$dst_model dest_device_vendor=$dst_vendor dest_device_osfamily=$dst_osfamily dest_device_osversion=$dst_osversion dest_device_mac=$dst_mac uri=$misc threat_id=$threatid threat_name=$threat_name threat_category=$thr_category direction=$direction user_agent=$user_agent url_category=$category url_category_list=$url_category_list content_type=$contenttype http_method=$http_method http_headers=$http_headers http2_connection=$http2_connection referer=$referer pcap_id=$pcap_id 

 File Data 

 CEF:0|PANW|NGFW_CEF|$sender_sw_version|$threatid|$type|$number-of-severity| __firewall_type=firewall.filedata __timestamp=$cef-formatted-time_generated __tz=$high_res_timestamp log_type=$type subtype=$subtype log_time=$cef-formatted-receive_time time_generated=$cef-formatted-time_generated log_source_id=$serial log_source_name=$device_name sequence_no=$seqno source_ip=$src dest_ip=$dst source_port=$sport dest_port=$dport nat_source=$natsrc nat_dest=$natdst nat_source_port=$natsport nat_dest_port=$natdport protocol=$proto action=$action source_user=$srcuser dest_user=$dstuser xff=$xff xff_ip=$xff_ip app=$app app_category=$category_of_app app_sub_category=$subcategory_of_app rule_matched=$rule rule_matched_uuid=$rule_uuid severity=$number-of-severity vsys=$vsys vsys_name=$vsys_name from_zone=$from to_zone=$to inbound_if=$inbound_if outbound_if=$outbound_if session_id=$sessionid source_device_category=$src_category source_device_profile=$src_profile source_device_model=$src_model source_device_vendor=$src_vendor source_device_osfamily=$src_osfamily source_device_osversion=$src_osversion source_device_mac=$src_mac dest_device_category=$dst_category dest_device_profile=$dst_profile dest_device_model=$dst_model dest_device_vendor=$dst_vendor dest_device_osfamily=$dst_osfamily dest_device_osversion=$dst_osversion dest_device_mac=$dst_mac misc=$misc threat_id=$threatid threat_name=$threat_name threat_category=$thr_category direction=$direction user_agent=$user_agent file_url=$file_url filedigest=$filedigest filetype=$filetype pcap_id=$pcap_id 

 Configure Escaping characters as follows: 

 Escaped Characters: \ 

 Escape Character: \ 

 Syslog_settings_NGFW_log_collection.png 

 Configure Syslog collection 

 Set up a Syslog collector for the logs, as explained in Activate Syslog Collector . In Task 4, ensure that you set Format to CEF. 

 Previous Ingest data from Next-Generation Firewall Next Panorama 

 Last updated 17 days ago 

 Was this helpful? 

 ‍ 

 Trust Center 

 ‍ 

 Privacy 

 ‍ 

 Terms of Use 

 ‍ 

 Legal 

 © 2026 Palo Alto Networks, Inc. All rights reserved. 

 Was this helpful?
