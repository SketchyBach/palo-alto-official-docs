---
url: https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/policy/use-an-external-dynamic-list-in-policy/built-in-edls
fetched_at: 2026-08-13T17:10:00Z
source: palo-alto-main
---

# Built-in External Dynamic Lists Clear

Built-in External Dynamic Lists 

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

 Built-in External Dynamic Lists 

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

 Use an External Dynamic List in Policy 

 Built-in External Dynamic Lists 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 한국어 (Korean) 

 Built-in External Dynamic Lists 

 Table of Contents 

 Filter

 Previous 

 URL List 

 Next 

 Configure the Firewall to Access an External Dynamic List 

 Built-in External Dynamic Lists 

 With an active Threat Prevention license, Palo Alto
Networks provides built-in IP address EDLs that you can use to protect
against malicious hosts. 

 Palo Alto Networks Bulletproof IP Addresses —Contains
IP addresses provided by bulletproof hosting providers. Because
bulletproof hosting providers place few, if any, restrictions on
content, attackers frequently use these services to host and distribute
malicious, illegal, and unethical material. 

 Palo Alto Networks High-Risk IP Addresses —Contains
malicious IP addresses from threat advisories issued by trusted
third-party organizations. Palo Alto Networks compiles the list of
threat advisories, but does not have direct evidence of the maliciousness
of the IP addresses. 

 Palo Alto Networks Known Malicious IP Addresses —Contains
IP addresses that are verified malicious based on WildFire analysis,
Unit 42 research, and data gathered from telemetry ( share threat intelligence with
Palo Alto Networks ). Attackers use these IP addresses almost
exclusively to distribute malware, initiate command-and-control
activity, and launch attacks. 

 Palo Alto Networks Tor Exit IP Addresses —Contains
IP addresses supplied by multiple providers and validated with Palo
Alto Networks threat intelligence data as active Tor exit nodes.
Traffic from Tor exit nodes can serve a legitimate purpose, however,
is disproportionately associated with malicious activity, especially
in enterprise environments. 

 The firewall receives updates for these feeds in content updates,
allowing the firewall to automatically enforce policy based on the
latest threat intelligence from Palo Alto Networks. You cannot modify
the contents of the built-in lists. Use them as-is (see Enforce
Policy on an External Dynamic List ), or create a custom external
dynamic list that uses one of the lists as a source (see Configure
the Firewall to Access an External Dynamic List ) and exclude entries from the list as needed. 

 Previous 

 URL List 

 Next 

 Configure the Firewall to Access an External Dynamic List 

 On This Page 

 PAN-OS 

 Next-Generation Firewall 

 Policy 

 11.1 

 Network Security 

 11.1 & Later 

 Administration 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
