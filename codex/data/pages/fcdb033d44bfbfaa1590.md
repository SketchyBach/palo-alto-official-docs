---
url: https://docs.paloaltonetworks.com/pan-os/10-1/pan-os-admin/zone-protection-and-dos-protection/dos-protection-against-flooding-of-new-sessions/end-a-single-session-dos-attack
fetched_at: 2026-08-13T17:02:13Z
source: palo-alto-main
---

# End a Single Session DoS Attack Clear

End a Single Session DoS Attack 

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

 End a Single Session DoS Attack 

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

 Zone Protection and DoS Protection 

 DoS Protection Against Flooding of New Sessions 

 End a Single Session DoS Attack 

 Download PDF 

 Next-Generation Firewall 

 End a Single Session DoS Attack 

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

 Configure DoS Protection Against Flooding of New Sessions 

 Next 

 Identify Sessions That Use Too Much of the On-Chip Packet Descriptor 

 End a Single Session DoS Attack 

 Use DoS protection policy rules and Security policy rules to block single session DoS
 attacks. 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by PAN-OS or Panorama) 

 No prerequisites needed 

 To mitigate a single-session DoS attack, you
would still Configure
DoS Protection Against Flooding of New Sessions in advance.
At some point after you configure the feature, a session might be
established before you realize a DoS attack (from the IP address
of that session) is underway. When you see a single-session DoS
attack, perform the following task to end the session, so that subsequent connection
attempts from that IP address trigger the DoS protection against
flooding of new sessions. 

 Identify the source IP address that is causing
the attack. 

 For example, use the firewall Packet Capture feature with
a destination filter to collect a sample of the traffic going to
the destination IP address. Alternatively, use the ACC to filter
on destination address to view the activity to the target host being
attacked. 

 Create a DoS Protection policy rule that will block the
attacker’s IP address after the attack thresholds are exceeded. 

 Create a Security policy rule to deny the source IP address
and its attack traffic. 

 End any existing attacks from the attacking source IP
address by executing the clear session all filter source <ip-address> operational
command. 

 Alternatively, if you know the session ID, you can execute
the clear session id <value> command
to end that session only. 

 If you use the clear session all filter source <ip-address> command,
all sessions matching the source IP address are discarded, which
can include both good and bad sessions. 

 After you end
the existing attack session, any subsequent attempts to form an
attack session are blocked by the Security policy. The DoS Protection
policy counts all connection attempts toward the thresholds. When
the Max Rate threshold is exceeded, the source IP address is blocked
for the Block Duration, as described in Multiple-Session DoS Attack . 

 Previous 

 Configure DoS Protection Against Flooding of New Sessions 

 Next 

 Identify Sessions That Use Too Much of the On-Chip Packet Descriptor 

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
