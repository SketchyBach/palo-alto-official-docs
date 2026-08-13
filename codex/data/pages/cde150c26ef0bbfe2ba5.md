---
url: https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/zone-protection-and-dos-protection/dos-protection-against-flooding-of-new-sessions/multiple-session-dos-attack
fetched_at: 2026-08-13T17:05:35Z
source: palo-alto-main
---

# Multiple-Session DoS Attack Clear

Multiple-Session DoS Attack 

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

 Multiple-Session DoS Attack 

 Updated on 

 Mon Aug 03 13:41:44 PDT 2026 

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

 Mon Aug 03 13:41:44 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 Zone Protection and DoS Protection 

 DoS Protection Against Flooding of New Sessions 

 Multiple-Session DoS Attack 

 Download PDF 

 Next-Generation Firewall 

 Multiple-Session DoS Attack 

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

 Previous 

 DoS Protection Against Flooding of New Sessions 

 Next 

 Single-Session DoS Attack 

 Multiple-Session DoS Attack 

 Learn about protecting your zone from larger scale and multiple-session DoS
 attacks. 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by PAN-OS or Panorama) 

 No prerequisites needed 

 Configure
DoS Protection Against Flooding of New Sessions by configuring
a DoS Protection policy rule, which determines the criteria that,
when matched by incoming packets, trigger the Protect action.
The DoS Protection profile counts each new connection toward the Alarm
Rate, Activate Rate, and Max Rate thresholds. When the incoming
new connections per second exceed the Activate Rate, the firewall
takes the action specified in the DoS Protection profile. 

 The following figure and table describe how the Security policy
rules, DoS Protection policy rules and profile work together in
an example. 

 Sequence
of Events as Firewall Quarantines an IP Address 

 In this example, an attacker launches a
DoS attack at a rate of 10,000 new connections per second to UDP
port 53. The attacker also sends 10 new connections per second to
HTTP port 80. 

 The new connections match criteria in the
DoS Protection policy rule, such as a source zone or interface,
source IP address, destination zone or interface, destination IP
address, or a service, among other settings. In this example, the
policy rule specifies UDP. 

 The DoS Protection policy rule
also specifies the Protect action and Classified ,
two settings that dynamically put the DoS Protection profile settings
into effect. The DoS Protection profile specifies that a Max Rate
of 3000 packets per second is allowed. When incoming packets match
the DoS Protection policy rule, new connections per second are counted toward
the Alert , Activate ,
and Max Rate thresholds. 

 You
can also use a Security policy rule to block all traffic from the
source IP address if you deem that address to be malicious all the
time. 

 The 10,000 new connections per second exceed
the Max Rate threshold. When all of the following
occur: 

 the threshold is exceeded, 

 a Block Duration is specified, and 

 Classified is set to include source
IP address, 

 the firewall puts the offending source
IP address on the block list. 

 An IP address on the block list is in quarantine,
meaning all traffic from that IP address is blocked. The firewall
blocks the offending source IP address before additional attack
packets reach the Security policy. 

 The following figure describes in more detail what happens after
an IP address that matches the DoS Protection policy rule is put
on the block list. It also describes the Block Duration timer. 

 Every one second, the firewall allows the IP address to come
off the block list so that the firewall can test the traffic patterns
and determine if the attack is ongoing. The firewall takes the following
action: 

 During this one-second test period, the firewall allows
packets that don’t match the DoS Protection policy criteria (HTTP
traffic in this example) through the DoS Protection policy rules
to the Security policy for validation. Very few packets, if any,
have time to get through because the first attack packet that the
firewall receives after the IP address is let off the block list
will match the DoS Protection policy criteria, quickly causing the
IP address to be placed back on the block list for another second.
The firewall repeats this test each second until the attack stops. 

 The firewall blocks all attack traffic from going past the
DoS Protection policy rules (the address remains on the block list)
until the Block Duration expires. 

 The 1-second checks illustrated in the preceding figure
occur on firewall models that have multiple dataplane CPUs and a
hardware network processor. All single dataplane systems or systems without
a hardware network processor perform this mitigation in software
and use a 5-second interval. 

 When the attack stops, the firewall does not put the IP address
back on the block list. The firewall allows non-attack traffic to
proceed through the DoS Protection policy rules to the Security
policy rules for evaluation. You must configure a Security policy
rule to allow or deny traffic because without one, an implicit Deny
rule denies all traffic. 

 The block list is based on a source zone and source address combination.
This behavior allows duplicate IP addresses to exist as long as
they are in different zones belonging to separate virtual routers. 

 The Block Duration setting in a DoS Protection profile specifies
how long the firewall blocks the [offending] packets that match
a DoS Protection policy rule. The attack traffic remains blocked
until the Block Duration expires, after which the attack traffic
must again exceed the Max Rate threshold to be blocked again. 

 If the attacker uses multiple sessions or bots that initiate
multiple attack sessions, the sessions count toward the thresholds
in the DoS Protection profile without a Security policy deny or
drop rule in place. Hence, a single-session attack requires a Security
policy deny or drop rule in order for each packet to count toward
the thresholds; a multiple-session attack does not. 

 Therefore, the DoS protection against flooding of new sessions
allows the firewall to efficiently defend against a source IP address
while attack traffic is ongoing and to permit non-attack traffic
to pass as soon as the attack stops. Putting the offending IP address
on the block list allows the DoS protection functionality to take
advantage of the block list, which is designed to quarantine all
activity from that source IP address, such as packets with a different
application. Quarantining the IP address from all activity protects
against a modern attacker who attempts a rotating application attack,
in which the attacker simply changes applications to start a new
attack or uses a combination of different attacks in a hybrid DoS
attack. You can monitor blocked IP addresses to
view the block list, remove entries from it, and get additional information
about an IP address on the block list. 

 Beginning with PAN-OS 7.0.2, it is a change in behavior
that the firewall places the attacking source IP address on the
block list. When the attack stops, non-attack traffic is allowed
to proceed to Security policy enforcement. The attack traffic that
matched the DoS Protection profile and DoS Protection policy rules
remains blocked until the Block Duration expires. 

 Previous 

 DoS Protection Against Flooding of New Sessions 

 Next 

 Single-Session DoS Attack 

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
