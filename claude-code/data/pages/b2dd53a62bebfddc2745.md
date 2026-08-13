---
url: https://docs.paloaltonetworks.com/vm-series/deployment/public-cloud/set-up-the-vm-series-firewall-on-oracle-cloud-infrastructure/oracle-cloud-infrastructure-logging
fetched_at: 2026-08-13T17:42:19Z
source: palo-alto-main
---

# Oracle Cloud Infrastructure Logging Clear

Oracle Cloud Infrastructure Logging 

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

 Oracle Cloud Infrastructure Logging 

 Updated on 

 Wed Jul 08 11:47:59 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 VM-Series Firewall Docs 

 Activation & Onboarding 

 Getting Started 

 Upgrade 

 Deployment 

 Select a Document 

 Public Cloud 

 Private Cloud 

 Updated on 

 Wed Jul 08 11:47:59 PDT 2026 

 Focus 

 Home 

 VM-Series 

 VM-Series Firewall on Oracle Cloud Infrastructure 

 Oracle Cloud Infrastructure Logging 

 Download PDF 

 VM-Series 

 Oracle Cloud Infrastructure Logging 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 VM-Series Firewall Docs 

 Activation & Onboarding 

 Getting Started 

 Upgrade 

 Deployment 

 Select a Document 

 Public Cloud 

 Private Cloud 

 Previous 

 Forward Metrics to Oracle Cloud Infrastructure 

 Next 

 Bootstrap the VM-Series Firewall on OCI 

 Oracle Cloud Infrastructure Logging 

 OCI Logging enables the PA-VM firewalls to stream logs such as traffic, threat, URL
 directly into an OCI Managed Kafka cluster. This integration bypasses standard syslog
 limitations to parse and safely forwards structured JSON log formats over secure mTLS
 connections. 

 Where Can I Use This? What Do I Need? 

 VM-Series 

 Prisma AIRS 

 OCI Network Firewall running PAN-OS® 11.2.13,
 12.1.8 and 12.2.2 onwards. 

 OCI Managed Kafka Cluster: Must be active
 with an accessible bootstrap endpoint operating on port
 9093. 

 Kafka Topics: It is recommended that you
 have the following three topics prior to setup: fw-traffic,
 fw-threat, and fw-url. 

 mTLS Certificates: A client certificate and
 private key bundle in PKCS12 format. 

 PA-VM Reachability & Certificate Import: 
 The PA-VM must be active, reachable, and have the following
 certificates imported: 

 Kafka-CA: The Kafka cluster CA certificate
 imported in PEM format as a standard
 certificate. 

 Kafka-Client-Cert: The client certificate +
 private key imported as a keypair . 

 Cloud-native enterprise environments deployed within Oracle Cloud
 Infrastructure (OCI) can now use OCI Logging that enables the PA-VM firewalls to
 stream traffic, threat, URL logs, and so on, directly into an OCI Managed Kafka cluster. 

 You can use OCI Logging to: 

 Centralize firewall log analytics directly into a managed OCI Kafka
 event stream. 

 Secure log transit using mutual TLS (mTLS) authentication. 

 Ensure strict adherence to structured log formats ($type
 $time_generated <json>) required by high-throughput SIEM and streaming
 parsers. 

 This integration relies on high-numbered, unprivileged syslog ports running
 locally on the PA-VM. PAN-OS forwarders send logs to localhost, where an internal engine
 intercepts, parses, formats, and safely pumps the data out to the designated Kafka
 topics. 

 The following are a few examples of the supported log types: 

 Log Type Syslog Port Kafka Topic Syslog Profile Server Name 

 traffic 5141 `fw-test` `syslog-kafka-traffic` `traffic` 

 threat 5142 `fw-threat` 

 `syslog-kafka-threat` 

 `threat` 

 url 5143 `fw-test2` `syslog-kafka-url` `url` 

 Configure OCI Logging 

 Configure Kafka logging servers. 
 Define a named Kafka server
 with its broker address, topic, partition key, and client certificate.

 Run this command once per Kafka destination. If you run the
 command again with the same server name, it updates the existing
 entry. 

 request plugins vm_series kafka-server server-name traffic kafka-broker <bootstrap>:9093 kafka-topic fw-traffic kafka-part-key 0 client-cert Kafka-Client-Cert
request plugins vm_series kafka-server server-name threat kafka-broker <bootstrap>:9093 kafka-topic fw-threat kafka-part-key 1 client-cert Kafka-Client-Cert
request plugins vm_series kafka-server server-name url kafka-broker <bootstrap>:9093 kafka-topic fw-url kafka-part-key 2 client-cert Kafka-Client-Cert

 Associate log types to syslog ports. 
 Map each log type you want to forward
 to the Kafka server and assign a syslog port for that log type. Run this
 command once per log type. You can reuse the same port across multiple
 log types on the same
 server. 

 request plugins vm_series kafka-server-log-type server-name traffic syslog-port 5141 type log-type traffic
request plugins vm_series kafka-server-log-type server-name threat syslog-port 5142 type log-type threat
request plugins vm_series kafka-server-log-type server-name url syslog-port 5143 type log-type url

 Configure PAN-OS syslog server profiles. 
 Enter configuration mode
 (configure) and direct the syslog profiles to point to the local input
 ports on 127.0.0.1 using standard BSD format over
 TCP. 

 set shared log-settings syslog syslog-kafka-traffic server syslog-kafka-traffic server 127.0.0.1 transport TCP port 5141 format BSD facility LOG_USER
set shared log-settings syslog syslog-kafka-threat server syslog-kafka-threat server 127.0.0.1 transport TCP port 5142 format BSD facility LOG_USER
set shared log-settings syslog syslog-kafka-url server syslog-kafka-url server 127.0.0.1 transport TCP port 5143 format BSD facility LOG_USER

 Crucial Apply Custom Log Format. 
 The syslog-pan parser expects a
 custom $type $time_generated <json> format. Standard PAN-OS BSD
 syslog CSV output will fail parsing, drop all records and leave your
 Kafka topics completely empty. Use the XML API to apply these specific
 XPaths and elements: 

 Traffic Format 
 XPath: 

 /config/shared/log-settings/syslog/entry[@name='syslog-kafka-traffic']/format 

 Element: 

 <traffic>\$type \$time_generated {"src_ip": "\$src", "sport":"\$sport", "dst_ip": "\$dst", "dport":"\$dport", "proto": "\$proto", "app": "\$app", "rule":"\$rule", "action": "\$action", "bytes_recv":"\$bytes_received", "bytes_sent":"\$bytes_sent", "pkts_received": "\$pkts_received", "pkts_sent":"\$pkts_sent", "start_time": "\$start", "elapsed_time": "\$elapsed", "repeat_count":"\$repeatcnt", "category":"\$category", "src country":"\$srcloc", "dst country":"\$dstloc", "session_end_reason": "\$session_end_reason", "xff_ip": "\$xff_ip"}</traffic> 

 Threat Format 
 XPath: 

 /config/shared/log-settings/syslog/entry[@name='syslog-kafka-threat']/format 

 Element: 

 <threat>\$type \$time_generated {"src_ip": "\$src", "sport":"\$sport", "dst":"\$dst", "dport":"\$dport", "proto": "\$proto", "app":"\$app", "rule":"\$rule", "action": "\$action", "threat_category": "\$thr_category", "sub_type": "\$subtype", "threat_content_name":"\$threatid", "severity": "\$severity", "direction": "\$direction", "repeatcnt":"\$repeatent", "data_filter_reason": "\$reason", "filetype": "\$filetype", "contentver": "\$contentver"}</threat> 

 URL Format 
 XPath: 

 /config/shared/log-settings/syslog/entry[@name='syslog-kafka-url']/format 

 Element: 

 <url>\$type \$time_generated {"src_ip":"\$src", "sport":"\$sport", "dst":"\$dst", "dport":"\$dport", "proto": "\$proto", "app":"\$app", "rule":"\$rule", "action": "\$action", "url_idx":"\$url_idx", "url_category_list": "\$url_category_list", "severity": "\$severity", "direction": "\$direction", "repeatent":"\$repeatent", "xff":"\$xff", "url_filename":"\$misc"}</url> 

 Configure log forwarding profile. 
 Route each individual log type to its
 corresponding newly created syslog profile. Run the following in
 configuration
 mode: 

 set shared log-settings profiles kafka-log-fwd match-list traffic-fwd filter "All Logs" log-type traffic send-syslog syslog-kafka-traffic
set shared log-settings profiles kafka-log-fwd match-list threat-fwd filter "All Logs" log-type threat send-syslog syslog-kafka-threat
set shared log-settings profiles kafka-log-fwd match-list url-fwd filter "All Logs" log-type url send-syslog syslog-kafka-url

 Attach log forwarding profile to security rules 
 Attach the forwarding
 profile to the specific security rules governing the traffic you intend
 to stream. Make sure log-end yes is verified to cleanly capture session
 termination traffic
 logs. 

 set rulebase security rules allow-interzone log-setting kafka-log-fwd
set rulebase security rules allow-interzone log-end yes

 Commit the configuration. 

 Verification and Health Check 

 To check Kafka server statuses: Execute the command: 

 show plugins vm_series kafka-servers (verify traffic,
 threat, and url outputs show correct brokers and cert profiles). 

 To check log port mapping: Execute the command: 

 show plugins vm_series kafka-server-log-type-mapping 
 (verify traffic points to 5141, threat to 5142, and url to 5143). 

 Check Pipeline Health 

 Validate the running states of your connections and streaming
 statistics: 

 Connectivity/mTLS Health: Run 

 debug plugins vm_series kafka config-status and confirm
 that it outputs: STATUS: All checks passed, mTLS OK, Private Key: Present on
 all 3 outputs . 

 Live Statistics: Run 

 debug plugins vm_series kafka statistics . Ensure
 traffic_logs_input > 0 after passing some ICMP traffic,
 Total Dropped: 0 , and the output status reads
 OK for all three log outputs (traffic_output,
 threat_output, url_output) . 

 Previous 

 Forward Metrics to Oracle Cloud Infrastructure 

 Next 

 Bootstrap the VM-Series Firewall on OCI 

 On This Page 

 Activation and Onboarding 

 Strata Cloud Manager 

 Next-Generation Firewalls 

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 VM-Series 

 Plugins 

 Cloud-Delivered Security Services 

 Advanced WildFire 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 AI Access Security 

 Device Security 

 Enterprise DLP 

 SaaS Security 

 Network Security 

 Shared Policy for NGFWs and Prisma Access 

 IPSec VPN 

 Security Policy 

 Quantum Security 

 Endpoints 

 GlobalProtect 

 Resources 

 All Release Notes 

 Compatibility Matrix 

 Experts Corner 

 VM-Series 

 Administration 

 Oracle Cloud Infrastructure 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
