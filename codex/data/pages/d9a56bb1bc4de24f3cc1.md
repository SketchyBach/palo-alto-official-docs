---
url: https://docs.paloaltonetworks.com/content/techdocs/en_US/pan-os/10-0/pan-os-cli-quick-start/use-the-cli/view-settings-and-statistics.html
fetched_at: 2026-09-16T10:42:33Z
source: palo-alto-main
---

# View Settings and Statistics Clear

Updated on 

 Mon Aug 28 18:33:05 PDT 2023 

 Focus 

 Home 

 PAN-OS 

 PAN-OS CLI Quick Start 

 Use
the CLI 

 View Settings and Statistics 

 Download PDF 

 PAN-OS CLI Quick Start 

 View Settings and Statistics 

 Table of Contents 

 Filter

 Version 

 10.0 (EoL) 

 11.1 & Later 

 10.2 

 10.1 

 10.0 (EoL) 

 9.1 (EoL) 

 Expand all | Collapse all 

 Get Started with the CLI 

 Access the CLI 

 Verify SSH Connection to Firewall 

 Refresh SSH Keys and Configure Key Options for Management Interface Connection 

 Give Administrators Access to the CLI 

 Administrative Privileges 

 Set Up a Firewall Administrative Account and Assign CLI Privileges 

 Set Up a Panorama Administrative Account and Assign CLI Privileges 

 Change CLI Modes 

 Navigate the CLI 

 Find a Command 

 View the Entire Command Hierarchy 

 Find a Specific Command Using a Keyword Search 

 Get Help on Command Syntax 

 Get Help on a Command 

 Interpret the Command Help 

 Customize the CLI 

 Use the CLI 

 View Settings and Statistics 

 Modify the Configuration 

 Commit Configuration Changes 

 Test the Configuration 

 Test the Authentication Configuration 

 Test Policy Matches 

 Load Configurations 

 Load Configuration Settings from a Text File 

 Load a Partial Configuration 

 Xpath Location Formats Determined by Device Configuration 

 Load a Partial Configuration into Another Configuration Using Xpath Values 

 Use Secure Copy to Import and Export Files 

 Export a Saved Configuration from One Firewall and Import it into Another 

 Export and Import a Complete Log Database (logdb) 

 CLI Jump Start 

 CLI Cheat Sheets 

 CLI Cheat Sheet: Device Management 

 CLI Cheat Sheet: User-ID 

 CLI Cheat Sheet: HA 

 CLI Cheat Sheet: Networking 

 CLI Cheat Sheet: VSYS 

 CLI Cheat Sheet: Panorama 

 CLI Changes in PAN-OS 10.0 

 Load Commands Changed in PAN-OS 10.0 

 Load Commands Removed in PAN-OS 10.0 

 Revert Commands Changed in PANOS-10.0 

 Set Commands Introduced in PAN-OS 10.0 

 Set Commands Changed in PAN-OS 10.0 

 Set Commands Removed in PAN-OS 10.0 

 Show Commands Introduced in PAN-OS 10.0 

 Show Commands Removed in PAN-OS 10.0 

 End-of-Life (EoL)

 View Settings and Statistics 

 Use show commands to view configuration
settings and statistics about the performance of the firewall or
Panorama and about the traffic and threats identified on the firewall.
You can use show commands in both Operational
and Configure mode. For example, the show system info command
shows information about the device itself: 

 admin@PA-850> show system info 

hostname: PA-850
ip-address: 10.10.10.23
public-ip-address: unknown
netmask: 255.255.255.0
default-gateway: 10.10.10.1
ip-assignment: static
ipv6-address: unknown
ipv6-link-local-address: fe80::d6f4:beff:febe:ba00/64
ipv6-default-gateway:
mac-address: d4:f4:be:be:ba:00
time: Tue Feb 12 08:40:09 2019
uptime: 6 days, 11:51:18
family: 800
model: PA-850
serial: 011901000300
cloud-mode: non-cloud
sw-version: 9.0.0-c300
global-protect-client-package-version: 0.0.0
app-version: 8114-5254
app-release-date: 2019/01/16 15:14:11 PST
av-version: 2860-3370
av-release-date: 2019/01/16 10:05:59 PST
threat-version: 8114-5254
threat-release-date: 2019/01/16 15:14:11 PST
wf-private-version: 0
wf-private-release-date: unknown
url-db: paloaltonetworks
wildfire-version: 314895-317564
wildfire-release-date: 2019/01/16 18:20:09 PST
url-filtering-version: 20190201.20201
global-protect-datafile-version: unknown
global-protect-datafile-release-date: unknown
global-protect-clientless-vpn-version: 0
global-protect-clientless-vpn-release-date:
logdb-version: 9.0.10
platform-family: 800
vpn-disable-mode: off
multi-vsys: off
operational-mode: normal

admin@PA-3220> 

 The show session info command shows details
about the sessions running through the Palo Alto Networks device. 

 admin@PA-850> show session info 

 target-dp: *.dp0
 --------------------------------------------------------------------------------
 Number of sessions supported: 196606
 Number of allocated sessions: 0
 Number of active TCP sessions: 0
 Number of active UDP sessions: 0
 Number of active ICMP sessions: 0
 Number of active GTPc sessions: 0
 Number of active GTPu sessions: 0
 Number of pending GTPu sessions: 0
 Number of active BCAST sessions: 0
 Number of active MCAST sessions: 0
 Number of active predict sessions: 0
 Number of active SCTP sessions: 0
 Number of active SCTP associations: 0
 Session table utilization: 0%
 Number of sessions created since bootup: 5044051
 Packet rate: 0/s
 Throughput: 0 kbps
 New connection establish rate: 0 cps
 --------------------------------------------------------------------------------
 Session timeout
 TCP default timeout: 3600 secs
 TCP session timeout before SYN-ACK received: 5 secs
 TCP session timeout before 3-way handshaking: 10 secs
 TCP half-closed session timeout: 120 secs
 TCP session timeout in TIME_WAIT: 15 secs
 TCP session delayed ack timeout: 250 millisecs
 TCP session timeout for unverified RST: 30 secs
 UDP default timeout: 30 secs
 ICMP default timeout: 6 secs
 SCTP default timeout: 3600 secs
 SCTP timeout before INIT-ACK received: 5 secs
 SCTP timeout before COOKIE received: 60 secs
 SCTP timeout before SHUTDOWN received: 30 secs
 other IP default timeout: 30 secs
 Captive Portal session timeout: 30 secs
 Session timeout in discard state:
 TCP: 90 secs, UDP: 60 secs, SCTP: 60 secs, other IP protocols: 60 secs
 --------------------------------------------------------------------------------
 Session accelerated aging: True
 Accelerated aging threshold: 80% of utilization
 Scaling factor: 2 X
 --------------------------------------------------------------------------------
 Session setup
 TCP - reject non-SYN first packet: True
 Hardware session offloading: True
 Hardware UDP session offloading: True
 IPv6 firewalling: True
 Strict TCP/IP checksum: True
 Strict TCP RST sequence: True
 Reject TCP small initial window: False
 ICMP Unreachable Packet Rate: 200 pps
 --------------------------------------------------------------------------------
 Application trickling scan parameters:
 Timeout to determine application trickling: 10 secs
 Resource utilization threshold to start scan: 80%
 Scan scaling factor over regular aging: 8
 --------------------------------------------------------------------------------
 Session behavior when resource limit is reached: drop
 --------------------------------------------------------------------------------
 Pcap token bucket rate : 10485760
 --------------------------------------------------------------------------------
 Max pending queued mcast packets per session : 0
 -------------------------------------------------------------------------------- 

 Previous 

 Use the CLI 

 Next 

 Modify the Configuration
