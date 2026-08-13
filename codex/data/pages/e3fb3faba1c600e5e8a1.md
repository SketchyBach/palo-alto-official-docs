---
url: https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/policy/policy-types
fetched_at: 2026-08-13T17:09:56Z
source: palo-alto-main
---

# Policy Types Clear

Policy Types 

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

 Policy Types 

 Updated on 

 Aug 11, 2025 

 Focus 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 한국어 (Korean) 

 Filter

 Updated on 

 Aug 11, 2025 

 Focus 

 Home 

 PAN-OS 

 Policy 

 Policy Types 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 한국어 (Korean) 

 Policy Types 

 Table of Contents 

 Filter

 Previous 

 Policy 

 Next 

 Security Policy 

 Policy Types 

 The Palo Alto Networks next-generation firewall supports
a variety of policy types that work together to safely enable applications
on your network. 

 Make sure you understand that in policy rules, the set of IPv4
addresses is treated as a subset of the set of IPv6 addresses, as
described in Policy . 

 For all policy types, when you Enforce Policy Rule Description, Tag, and Audit Comment , you can use
the audit comment archive to view how a policy rule changed over
time. The archive, which includes the audit comment history and
the configuration logs, enables you to compare configuration versions
and review who created or modified and why. 

 Policy Type 

 Description 

 Security 

 Determine whether to block or allow a session
based on traffic attributes such as the source and destination security
zone, the source and destination IP address, the application, user,
and the service. For more details, see Security
Policy . 

 NAT 

 Instruct the firewall which packets need
translation and how to do the translation. The firewall supports
both source address and/or port translation and destination address
and/or port translation. For details, see NAT . 

 QoS 

 Identify traffic requiring QoS treatment (either preferential treatment or bandwidth-limiting)
 using a defined parameter or multiple parameters and assign it a
 class. For more details, see Quality of Service . 

 Policy Based Forwarding 

 Identify traffic that should use a different
egress interface than the one that would normally be used based
on the routing table. For more details, see Policy-Based
Forwarding . 

 Decryption 

 Identify encrypted traffic that you want to inspect for visibility, control, and granular
 security. For more details, see Decryption . 

 Application Override 

 Identify sessions that you want to bypass
App-ID layer 7 processing and threat inspection. Traffic that matches
an application override policy forces the firewall to handle the
session as a stateful inspection firewall at layer 4. Only use Application
Override when you must and in the most highly trusted environments
where you can apply the principle of least privilege strictly. For
more details, see Application Override . 

 Authentication 

 Identify traffic that requires users to
authenticate. For more details, see Authentication
Policy . 

 DoS Protection 

 Identify potential denial-of-service (DoS)
attacks and take protective action in response to rule matches.
For more details, see DoS
Protection Profiles . 

 Previous 

 Policy 

 Next 

 Security Policy 

 On This Page 

 PAN-OS 

 Next-Generation Firewall 

 Policy 

 11.1 

 Network Security 

 11.1 & Later 

 Administration 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
