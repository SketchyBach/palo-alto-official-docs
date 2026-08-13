---
url: https://docs.paloaltonetworks.com/ngfw/administration/monitoring/configure-log-forwarding/configure-log-forwarding-pan-os
fetched_at: 2026-08-13T16:40:09Z
source: palo-alto-main
---

# Configure Log Forwarding (PAN-OS) Clear

Configure Log Forwarding (PAN-OS) 

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

 Configure Log Forwarding (PAN-OS) 

 Updated on 

 Aug 3, 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Generation Firewall Docs 

 Getting Started 

 Administration 

 Networking 

 Quick Start 

 Reference 

 Incidents & Alerts 

 Release Notes 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 11.0 (EoL) 

 PAN-OS 10.2 

 PAN-OS 10.1 (EoL) 

 PAN-OS 10.0 (EoL) 

 PAN-OS 9.1 (EoL) 

 PAN-OS 9.0 (EoL) 

 PAN-OS 8.1 (EoL) 

 Help 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 10.2 

 PAN-OS 10.1 

 New Features 

 Updated on 

 Aug 3, 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 Monitoring 

 Configure Log Forwarding 

 Configure Log Forwarding (PAN-OS) 

 Download PDF 

 Next-Generation Firewall 

 Configure Log Forwarding (PAN-OS) 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Generation Firewall Docs 

 Getting Started 

 Administration 

 Networking 

 Quick Start 

 Reference 

 Incidents & Alerts 

 Release Notes 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 11.0 (EoL) 

 PAN-OS 10.2 

 PAN-OS 10.1 (EoL) 

 PAN-OS 10.0 (EoL) 

 PAN-OS 9.1 (EoL) 

 PAN-OS 9.0 (EoL) 

 PAN-OS 8.1 (EoL) 

 Help 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 10.2 

 PAN-OS 10.1 

 New Features 

 Configure Log Forwarding (PAN-OS) 

 Configure log forwarding for PAN-OS. 

 10.1 and 10.2 

 11.1 and
 later 

 Configure Log Forwarding PAN-OS 10.1 10.2 

 Centralize multi-firewall monitoring: forward logs to Panorama or external services.
 Firewalls convert formats, filter, handle logs (max 4096 bytes), and risk crash with
 unsupported fields. 

 Configure a server profile for each external service that will receive log
 information. 

 You can use separate profiles to send different sets of logs, filtered by
 log attributes, to a different server. To increase availability, define
 multiple servers in a single profile. 

 Configure one or more of the following server profiles: 

 ( Required for SMTP over TLS ) If you have not already done so,
 create a certificate profile 
 for the email server. 

 To enable the SNMP manager (trap server) to interpret firewall traps,
 you must load the Palo Alto Networks Supported MIBs into
 the SNMP manager and, if necessary, compile them. For details, refer to
 your SNMP management software documentation. 

 If the syslog server requires client authentication, you must also configure-syslog-monitoring.html#id43889746-3f0f-40aa-bfbe-8a77b8ce7532_id6dde9e7b-bf0e-4a24-bcd5-fc9b8af8f294 

 Configure an HTTP server profile (see Forward Logs to an HTTP/S Destination ). 

 Log forwarding to an HTTP server is designed for log forwarding
 at low frequencies and is not recommend for deployments with a
 high volume of log forwarding. You may experience log loss when
 forwarding to an HTTP server if your deployment generate a high
 volume of logs that need to be forwarded. 

 Create a Log Forwarding profile. 

 The profile defines the destinations for Traffic, Threat, WildFire
 Submission, URL Filtering, Data Filtering, Tunnel and Authentication
 logs. 

 Select Objects Log Forwarding and Add a profile. 

 Enter a Name to identify the profile. 

 If you want the firewall to automatically assign the profile to new
 security rules and zones, enter default . If
 you don’t want a default profile, or you want to override an
 existing default profile, enter a Name that
 will help you identify the profile when assigning it to security
 rules and zones. 

 If no log forwarding profile named default 
 exists, the profile selection is set to
 None by default in new security rules
 ( Log Forwarding field) and new
 security zones ( Log Setting field),
 although you can change the selection. 

 Add one or more match list
 profiles . 

 The profiles specify log query filters, forwarding destinations, and
 automatic actions such as tagging. For each match list profile: 

 Enter a Name to identify the
 profile. 

 Select the Log Type . 

 In the Filter drop-down, select
 Filter Builder . Specify the
 following and then Add each
 query: 

 Connector logic (and/or) 

 Log Attribute 

 Operator to define inclusion
 or exclusion logic 

 Attribute Value for the query
 to match 

 Select Panorama if you want to forward
 logs to Log Collectors or the Panorama management
 server. 

 For each type of external service that you use for monitoring
 (SNMP, Email, Syslog, and HTTP), Add 
 one or more server profiles. 

 ( Optional, GlobalProtect Only ) If you are using a log
 forwarding profile with a security policy to automatically quarantine a
 device using GlobalProtect, select
 Quarantine in the Built-in
 Actions area. 

 Click OK to save the Log Forwarding
 profile. 

 Assign the Log Forwarding profile to policy rules and network zones. 

 Security, Authentication, and DoS Protection rules support log forwarding. In
 this example, you assign the profile to a Security rule. 

 Perform the following steps for each rule that you want to trigger log
 forwarding: 

 Select Policies Security and edit the rule. 

 Select Actions and select the Log
 Forwarding profile you created. 

 Set the Profile Type to
 Profiles or Group , and
 then select the security profiles or
 Group Profile required to trigger log
 generation and forwarding for: 

 Threat logs—Traffic must match any security profile assigned
 to the rule. 

 WildFire Submission logs—Traffic must match a WildFire Analysis profile 
 assigned to the rule. 

 For Traffic logs, select Log At Session Start 
 and/or Log At Session End . 

 Log At Session Start consumes more resources
 than logging only at the session end. In most cases, you only
 Log At Session End . Enable both
 Log At Session Start and Log
 At Session End only for troubleshooting, for
 long-lived tunnel sessions such as GRE tunnels (you can't see these
 sessions in the ACC unless you log at the start of the session), and
 to gain visibility into Operational Technology/Industrial Control
 Systems (OT/ICS) sessions, which are also long-lived sessions. 

 Click OK to save the rule. 

 Configure the destinations for System, Configuration, Correlation,
 GlobalProtect, HIP Match, and User-ID logs. 

 Panorama generates Correlation logs based on the firewall logs it
 receives, rather than aggregating Correlation logs from firewalls. 

 Select Device Log Settings . 

 For each log type that the firewall will forward, see Step Add one
 or more match list profiles. 

 ( PA-7000 Series firewalls with Log Cards only ) Configure a log card
 interface to perform log forwarding. 

 As of PAN-OS 10.1, you can no longer forward system logs and other
 Management plane logs using the Management interface or service routes.
 The only way to forward system logs from a PA-7000 Series firewall with
 a LFC running PAN-OS 10.1 or later is by configuring a log card
 interface 

 Select Network Interfaces Ethernet and click Add Interface . 

 Select the Slot and Interface
 Name . 

 Set the Interface Type to Log
 Card . 

 Enter the IP Address , Default
 Gateway , and ( for IPv4 only )
 Netmask . 

 Select Advanced and specify the Link
 Speed , Link Duplex , and
 Link State . 

 These fields default to auto , which
 specifies that the firewall automatically determines the values
 based on the connection. However, the minimum recommended
 Link Speed for any connection is
 1000 (Mbps). 

 Click OK to save your changes. 

 ( PA-5450 firewall only ) Configure a log interface to perform log
 forwarding. 

 This step is not required if you are forwarding logs to a Panorama or Strata Logging Service using the management interface. The
 management interface handles log forwarding by default and does not
 require the log interface to be configured. 

 ( PAN-OS 10.2.0 and 10.2.1 ) The management interface handles
 log forwarding by default unless you configure a specific service
 route for log forwarding. 

 ( PAN-OS 10.2.2 and later releases ) The management interface
 handles log forwarding by default unless you configure the log
 interface or a specific service route for log forwarding. If a log
 interface is configured and committed, all internal logging, Strata Logging Service , SNMP, HTTP, and Syslog will be
 forwarded by the log interface. 

 Ensure that the log interface you are configuring is not in the same
 subnetwork as the management interface. Configuring both interfaces in
 the same subnetwork can cause connectivity issues and result in the
 wrong interface being used for log forwarding. 

 LOG-1 and LOG-2 are bundled as a single logical interface called
 bond1 . Bond1 uses LACP (link aggregation
 control protocol) as IEEE 802.3ad. Set the Mode 
 for LACP status queries to Active and the
 Transmission Rate for LACP query and response
 exchanges to Slow . 

 Select Device Setup Management . 

 Select the settings gear on the top menu bar of Log
 Interface . 

 Fill in the IP Address ,
 Netmask , and Default
 Gateway fields. 

 If your network uses IPv6, fill in the IPv6
 Address and IPv6 Default
 Gateway fields instead. 

 When the log interface is configured with an IP address,
 communication between the firewall and Panorama automatically
 switches from being handled by the management interface
 (default) to the log interface. 

 Specify the Link Speed , Link
 Duplex , and Link State . These
 fields default to auto , which specifies that the
 firewall automatically determines the values based on the
 connection. 

 Click OK to save your changes. 

 Commit and verify your changes. 

 Commit your changes. 

 Verify the log destinations you configured are receiving firewall
 logs: 

 Panorama—If the firewall forwards logs to a Panorama virtual
 appliance in Panorama mode or to an M-Series appliance, you
 must configure a Collector Group 
 before Panorama will receive the logs. You can then verify log forwarding . 

 Email server—Verify that the specified recipients are
 receiving logs as email notifications. 

 Syslog server—Refer to your syslog server documentation to
 verify it’s receiving logs as syslog messages. 

 SNMP manager— Use an SNMP Manager to Explore MIBs and Objects to verify it’s receiving logs as
 SNMP traps. 

 HTTP server— Forward Logs to an HTTP/S Destination . 

 Configure Log Forwarding PAN-OS 11.1 

 Forward logs to Panorama or external services. Firewalls convert formats, filter,
 handle logs, and risk crash with unsupported fields. 

 Configure a server profile for each external service that will receive log
 information. 

 You can use separate profiles to send different sets of logs, filtered by
 log attributes, to a different server. To increase availability, define
 multiple servers in a single profile. 

 Configure one or more of the following server profiles: 

 ( Required for SMTP over TLS ) If you have not already done so,
 create a certificate profile 
 for the email server. 

 To enable the SNMP manager (trap server) to interpret firewall traps,
 you must load the Palo Alto Networks Supported MIBs into
 the SNMP manager and, if necessary, compile them. For details, refer to
 your SNMP management software documentation. 

 If the syslog server requires client authentication, you must also configure-syslog-monitoring.html#id43889746-3f0f-40aa-bfbe-8a77b8ce7532_id6dde9e7b-bf0e-4a24-bcd5-fc9b8af8f294 

 Configure an HTTP server profile (see Forward Logs to an HTTP/S Destination ). 

 Log forwarding to an HTTP server is designed for log forwarding
 at low frequencies and is not recommend for deployments with a
 high volume of log forwarding. You may experience log loss when
 forwarding to an HTTP server if your deployment generate a high
 volume of logs that need to be forwarded. 

 Create a Log Forwarding profile. 

 The profile defines the destinations for Traffic, Threat, WildFire
 Submission, URL Filtering, Data Filtering, Tunnel and Authentication
 logs. 

 Select Objects Log Forwarding and Add a profile. 

 Enter a Name to identify the profile. 

 If you want the firewall to automatically assign the profile to new
 security rules and zones, enter default . If
 you don’t want a default profile, or you want to override an
 existing default profile, enter a Name that
 will help you identify the profile when assigning it to security
 rules and zones. 

 If no log forwarding profile named default 
 exists, the profile selection is set to
 None by default in new security rules
 ( Log Forwarding field) and new
 security zones ( Log Setting field),
 although you can change the selection. 

 Add one or more match list
 profiles . 

 The profiles specify log query filters, forwarding destinations, and
 automatic actions such as tagging. For each match list profile: 

 Enter a Name to identify the
 profile. 

 Select the Log Type . 

 In the Filter drop-down, select
 Filter Builder . Specify the
 following and then Add each
 query: 

 Connector logic (and/or) 

 Log Attribute 

 Operator to define inclusion
 or exclusion logic 

 Attribute Value for the query
 to match 

 Select Panorama if you want to forward
 logs to Log Collectors or the Panorama management
 server. 

 For each type of external service that you use for monitoring
 (SNMP, Email, Syslog, and HTTP), Add 
 one or more server profiles. 

 ( Optional, GlobalProtect Only ) If you are using a log
 forwarding profile with a security policy to automatically quarantine a
 device using GlobalProtect, select
 Quarantine in the Built-in
 Actions area. 

 Click OK to save the Log Forwarding
 profile. 

 Assign the Log Forwarding profile to policy rules and network zones. 

 Security, Authentication, and DoS Protection rules support log forwarding. In
 this example, you assign the profile to a Security rule. 

 Perform the following steps for each rule that you want to trigger log
 forwarding: 

 Select Policies Security and edit the rule. 

 Select Actions and select the Log
 Forwarding profile you created. 

 Set the Profile Type to
 Profiles or Group , and
 then select the security profiles or
 Group Profile required to trigger log
 generation and forwarding for: 

 Threat logs—Traffic must match any security profile assigned
 to the rule. 

 WildFire Submission logs—Traffic must match a WildFire Analysis profile 
 assigned to the rule. 

 For Traffic logs, select Log At Session Start 
 and/or Log At Session End . 

 Log At Session Start consumes more resources
 than logging only at the session end. In most cases, you only
 Log At Session End . Enable both
 Log At Session Start and Log
 At Session End only for troubleshooting, for
 long-lived tunnel sessions such as GRE tunnels (you can't see these
 sessions in the ACC unless you log at the start of the session), and
 to gain visibility into Operational Technology/Industrial Control
 Systems (OT/ICS) sessions, which are also long-lived sessions. 

 Click OK to save the rule. 

 Configure the destinations for System, Configuration, Correlation,
 GlobalProtect, HIP Match, and User-ID logs. 

 Panorama generates Correlation logs based on the firewall logs it
 receives, rather than aggregating Correlation logs from firewalls. 

 Select Device Log Settings . 

 For each log type that the firewall will forward, see Step Add one
 or more match list profiles. 

 ( PA-7500 Series firewall only ) Configure a log interface to perform
 log forwarding. 

 Management Plane logs are forwarded through the
 management interface to a log collector such as Panorama or Cortex Data
 Lake. Data plane logs are forwarded through the log ports on the PA-7500
 Management Processing Card (MPC). 

 LOG-1 and LOG-2 are bundled as a single logical
 interface called bond1 . When connecting both log
 ports, use the Ethernet port channel on the switch. 

 This step is not required if you are storing Data Plane logs locally,
 which can be configured by enabling demo mode. To enable demo mode, you
 must first add and enable a logging drive 
 in the PA-7500 Management Processing Card (MPC). 

 After the logging drive is enabled, log in to the CLI and enter 

 admin@pa-7500> debug log-receiver mp demo_mode set dp <data plane number> slot <DPC slot number> duration <in minutes> 

 For the data plane and DPC slot number, refer to the chassis slot
 numbering on the PA-7500 front panel . 

 To view the current duration of demo mode, enter 

 admin@pa-7500> debug log-receiver mp demo_mode show 

 To turn off demo mode, enter the following command and set the duration
 to 0 . 

 admin@pa-7500> debug log-receiver mp demo_mode set dp <data plane number> slot <DPC slot number> duration <in minutes> 

 Select Device Setup Management . 

 Select the settings gear on the top menu bar of Log
 Interface . 

 Fill in the IP Address ,
 Netmask , and Default
 Gateway fields. 

 If your network uses IPv6, fill in the IPv6
 Address and IPv6 Default
 Gateway fields instead. 

 The log interface can be configured with
 either an IPv4 address or an IPv6 address; it cannot have both an
 IPv4 address and IPv6 address at the same time. 

 Specify the Link Speed , Link
 Duplex , and Link State . These
 fields default to auto , which specifies that the
 firewall automatically determines the values based on the
 connection. 

 Click OK to save your changes. 

 ( PA-7000 Series firewalls with Log Cards only ) Configure a log card
 interface to perform log forwarding. 

 As of PAN-OS 10.1, you can no longer forward system logs and other
 Management plane logs using the Management interface or service routes.
 The only way to forward system logs from a PA-7000 Series firewall with
 a LFC running PAN-OS 10.1 or later is by configuring a log card
 interface 

 Select Network Interfaces Ethernet and click Add Interface . 

 Select the Slot and Interface
 Name . 

 Set the Interface Type to Log
 Card . 

 Enter the IP Address , Default
 Gateway , and ( for IPv4 only )
 Netmask . 

 Select Advanced and specify the Link
 Speed , Link Duplex , and
 Link State . 

 These fields default to auto , which
 specifies that the firewall automatically determines the values
 based on the connection. However, the minimum recommended
 Link Speed for any connection is
 1000 (Mbps). 

 Click OK to save your changes. 

 ( PA-5450 firewall only ) Configure a log interface to perform log
 forwarding. 

 This step is not required if you are forwarding logs to a Panorama or Strata Logging Service using the management interface. The
 management interface handles log forwarding by default and does not
 require the log interface to be configured. 

 ( PAN-OS 10.2.0 and 10.2.1 ) The management interface handles
 log forwarding by default unless you configure a specific service
 route for log forwarding. 

 ( PAN-OS 10.2.2 and later releases ) The management interface
 handles log forwarding by default unless you configure the log
 interface or a specific service route for log forwarding. If a log
 interface is configured and committed, all internal logging, Strata Logging Service , SNMP, HTTP, and Syslog will be
 forwarded by the log interface. 

 Ensure that the log interface you are configuring is not in the same
 subnetwork as the management interface. Configuring both interfaces in
 the same subnetwork can cause connectivity issues and result in the
 wrong interface being used for log forwarding. 

 LOG-1 and LOG-2 are bundled as a single logical interface called
 bond1 . Bond1 uses LACP (link aggregation
 control protocol) as IEEE 802.3ad. Set the Mode 
 for LACP status queries to Active and the
 Transmission Rate for LACP query and response
 exchanges to Slow . 

 Select Device Setup Management . 

 Select the settings gear on the top menu bar of Log
 Interface . 

 Fill in the IP Address ,
 Netmask , and Default
 Gateway fields. 

 If your network uses IPv6, fill in the IPv6
 Address and IPv6 Default
 Gateway fields instead. 

 When the log interface is configured with an IP address,
 communication between the firewall and Panorama automatically
 switches from being handled by the management interface
 (default) to the log interface. 

 Specify the Link Speed , Link
 Duplex , and Link State . These
 fields default to auto , which specifies that the
 firewall automatically determines the values based on the
 connection. 

 Click OK to save your changes. 

 Commit and verify your changes. 

 Commit your changes. 

 Verify the log destinations you configured are receiving firewall
 logs: 

 Panorama—If the firewall forwards logs to a Panorama virtual
 appliance in Panorama mode or to an M-Series appliance, you
 must configure a Collector Group 
 before Panorama will receive the logs. You can then verify log forwarding . 

 Email server—Verify that the specified recipients are
 receiving logs as email notifications. 

 Syslog server—Refer to your syslog server documentation to
 verify it’s receiving logs as syslog messages. 

 SNMP manager— Use an SNMP Manager to Explore MIBs and Objects to verify it’s receiving logs as
 SNMP traps. 

 HTTP server— Forward Logs to an HTTP/S Destination . 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Activate a License or Product 

 Cloud Identity Engine 

 Strata Logging Service 

 Device Associations 

 Hub 

 Identity and Access Management 

 Tenant Management 

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

 Network Security 

 Shared Policy for NGFWs and Prisma Access 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Network Security 

 PAN-OS 

 Next-Generation Firewall 

 Administration 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
