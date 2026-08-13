---
url: https://docs.paloaltonetworks.com/advanced-wildfire/wildfire-appliance/use-the-wildfire-appliance-cli/wildfire-appliance-configuration-mode-command-reference/set-deviceconfig-high-availability
fetched_at: 2026-08-13T15:21:13Z
source: palo-alto-main
---

# set deviceconfig high-availability Clear

set deviceconfig high-availability 

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

 set deviceconfig high-availability 

 Updated on 

 Mon Mar 02 18:41:58 PST 2026 

 Focus 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Filter

 Expand All 
 | 
 Collapse All 

 Advanced WildFire 

 Administration 

 Appliance 

 Updated on 

 Mon Mar 02 18:41:58 PST 2026 

 Focus 

 Home 

 Advanced WildFire Powered by Precision AI™ 

 Use the WildFire Appliance CLI 

 WildFire Appliance Configuration Mode Command Reference 

 set deviceconfig high-availability 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Advanced WildFire Powered by Precision AI™ 

 set deviceconfig high-availability 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Advanced WildFire 

 Administration 

 Appliance 

 Previous 

 set deviceconfig cluster 

 Next 

 set deviceconfig setting management 

 set deviceconfig high-availability 

 Description 

 Configure Wildfire
appliance cluster high-availability (HA) settings. 

 Hierarchy Location 

 set deviceconfig 

 Syntax 

 high-availability { 
enabled {no | yes}; 
election-option { 
preemptive {no | yes}; 
priority {primary | secondary}; 
timers { 
advanced {heartbeat interval <value> | hello-interval <value> | 
preemption-hold-time <value> | promotion-hold-time <value>} 
aggressive; 
recommended; 
} 
} 
interface { 
ha1 { 
peer-ip-address <ip-address>; 
port {eth2 | eth3 | management}; 
encryption enabled {no | yes}; 
} 
ha1-backup { 
peer-ip-address <ip-address>; 
port {eth2 | eth3 | management}; 
} 
} 
} 

 Options 

 + enabled —
Enable HA on both controller nodes to provide fault tolerance for
the cluster. Each WildFire appliance cluster should have two controller
nodes configured as an HA pair. 

 > election-option —
Configure the preemptive, priority, and timer HA option values. 

 +
preemptive — Election option to enable the passive
HA peer (the controller backup node) to preempt the active HA peer
(the primary controller node) based on the HA priority setting.
For example, if the primary controller node goes down, the secondary
(passive) controller node takes over cluster control. When the primary
controller node comes back up, if you do not configure preemption, the
secondary controller continues to control the cluster and the primary
controller acts as the controller backup node. However, if you configure
preemption on both HA peers, then when the primary controller comes
back up, it preempts the secondary controller by taking back control
of the cluster. The secondary controller resumes its former role
as the controller backup node. You must configure the preemptive
setting on both of the HA peers for preemption to work. 

 +
priority — Election option to configure the preemption
priority of each controller in the HA pair. Configure preemption
on both members of the HA controller pair. 

 >
timers — Configure the timers for HA election options.
The WildFire appliance provides two pre-configured timer options
( aggressive and recommended settings),
or you can configure each timer individually. The Advanced timers
enable you to configure values individually: 

 The heartbeat-interval sets
the time in milliseconds to send heartbeat pings. The range of values
is 1000-60,000 ms, with a default value of 2000 ms. 

 The hello-interval sets the
time in milliseconds to send Hello messages. The range of values
is 8000-60,000 ms, with a default value of 8000 ms. 

 The preemption-hold-time sets
the time in minutes to remain in passive (controller backup) mode before
preempting the active (primary) controller node. The range of values
is 1-60 minutes, with a default value of 1 minute. 

 The promtion-hold-time sets
the time in milliseconds to change state from passive (controller backup)
to active (primary) state. The range of values is 0-60,000 ms, with
a default value of 2000 ms. 

 > interface —
Configure HA interface settings for the primary ( ha1 )
and backup ( ha1-backup ) control link
interfaces. The control link interfaces enable the HA controller
pair to remain synchronized and prepared to failover in case the
primary controller node goes down. Configuring both the ha1 interface
and the ha1-backup interface provides
redundant connectivity between controllers in case of a link failure.
Set: 

 The peer-ip-address .
For each interface, configure the IP address of the HA peer. The ha1 interface
peer is the ha1 interface IP address
on the other controller node in the HA pair. The ha1-backup interface
peer is the ha1-backup interface IP address
on the other controller node in the HA pair. 

 The port . On each controller
node, configure the port to use for the ha1 interface
and the port to use for the ha-backup interface.
You can use eth2 , eth3 ,
or the management port (eth0) for the
HA control link interfaces. You cannot use the Analysis Environment
Network interface (eth1) as an ha1 or ha1-backup control
link interface. Use the same interface on both HA peers as the ha1 interface,
and use the same interface (but not the ha1 interface)
on both HA peers as the ha1-backup interface.
For example, configure eth3 as the ha1 interface
on both controller nodes and configure the management interface as
the ha1-backup interface on both controller
nodes. 

 Sample Output 

 admin@wf-500(active-controller)# show deviceconfig high-availability 
high-availability { 
election-option { 
priority primary; 
} 
enabled no; 
interface { 
ha1 { 
peer-ip-address 10.10.10.150; 
port eth2 
} 
ha1-backup { 
peer-ip-address 10.10.10.160; 
port management 
} 
} 
} 

 Required Privilege Level 

 superuser, deviceadmin 

 Previous 

 set deviceconfig cluster 

 Next 

 set deviceconfig setting management 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Activate a License or Product 

 Strata Logging Service 

 Device Associations 

 Hub 

 Identity and Access Management 

 Tenant Management 

 Next-Generation Firewalls 

 AIOps for NGFW 

 Cloud Management for NGFWs 

 Firewalls 

 PAN-OS 

 Panorama 

 VM-Series 

 SASE 

 Prisma Access 

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

 Security Policy 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 CLI 

 10.1 

 11.0 

 Network Security 

 PAN-OS 

 10.2 

 WF-500-B Appliance 

 Advanced Wildfire 

 WF-500 Appliance 

 Appliance 

 9.1 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
