---
url: https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/policy/use-an-external-dynamic-list-in-policy/external-dynamic-list
fetched_at: 2026-08-13T17:10:01Z
source: palo-alto-main
---

# External Dynamic List Clear

External Dynamic List 

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

 External Dynamic List 

 Updated on 

 Mon Aug 11 16:31:23 PDT 2025 

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

 Mon Aug 11 16:31:23 PDT 2025 

 Focus 

 Home 

 PAN-OS 

 Policy 

 Use an External Dynamic List in Policy 

 External Dynamic List 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 한국어 (Korean) 

 External Dynamic List 

 Table of Contents 

 Filter

 Previous 

 Use an External Dynamic List in Policy 

 Next 

 Formatting Guidelines for an External Dynamic List 

 External Dynamic List 

 An External Dynamic List is a text file that is hosted
on an external web server so that the firewall can import objects—IP
addresses, URLs, domains, International Mobile Equipment Identities
(IMEIs), International Mobile Subscriber Identities (IMSIs)—included
in the list and enforce policy. To enforce Security policy on the
entries included in the external dynamic list, you must reference
the list in a supported policy rule or profile. When multiple lists are
referenced, you can prioritize the order of evaluation to make sure
the most important EDLs are committed before capacity limits are
reached. As you modify the list, the firewall dynamically imports
the list at the configured interval and enforces policy without
the need to make a configuration change or a commit on the firewall.
If the web server is unreachable, the firewall uses the last successfully
retrieved list for enforcing policy until the connection is restored
with the web server. In cases where authentication to the EDL fails,
the security policy stops enforcing the EDL. To retrieve the external
dynamic list, the firewall uses the interface configured with the Palo
Alto Networks Services service route. 

 The firewall retains the last successfully retrieved EDL and
continues operating with the most current EDL information until
connection is restored with the server hosting the EDL if: 

 You upgrade or downgrade the firewall 

 You reboot the firewall, management plane, or data plane 

 The server hosting the EDL becomes unreachable 

 The following warning is displayed when the firewall is unable
to connect or otherwise fetch the most current EDL information from
the server. 

 Unable to fetch external list. Using old copy for refresh. 

 The firewall supports these types of external dynamic lists: 

 Predefined IP Address —A predefined IP address
list is a type of IP address list that refers to the built-in, dynamic
IP lists with fixed or “predefined” contents. These Built-In External Dynamic
Lists —for bulletproof hosting providers, known malicious,
and high-risk IP addresses—are automatically added to your firewall
if you have an active Threat Prevention license. A predefined IP
address list can also refer to an EDL that uses one of the built-in
lists as a source. Because you can’t modify the contents of a predefined
list, you can use a predefined list as a source for a different
EDL if you want to add or exclude list entries. 

 Predefined URL List —This type of external
dynamic list contains pre-populated URLs that applications use for
background services, such as updates or Certificate Revocation List
(CRL) checks, that the firewall can safely exclude from Authentication
policy. Palo Alto Networks revises and maintains this type of external dynamic
list, which is also known as an Authentication Portal Exclude List,
through content updates. 

 IP Address —The firewall typically enforces policy
for a source or destination IP address that is defined as a static
object on the firewall (see Enforce
Policy on an External Dynamic List ) If you need agility in
enforcing policy for a list of source or destination IP addresses
that emerge ad hoc, you can use an external dynamic list of type
IP address as a source or destination address object in policy rules,
and configure the firewall to deny or allow access to the IP addresses
(IPv4 and IPv6 address, IP range and IP subnets) included in the
list. You can also use an IP address EDL in the source or destination
of an SD-WAN policy rule. The firewall treats an external dynamic
list of type IP address as an address object; all the IP addresses
included in a list are handled as one address object. 

 Domain —This type of external dynamic list allows you
to import custom domain names into the firewall to enforce policy
using an Anti-Spyware profile or SD-WAN policy rule. An EDL in an
Anti-Spyware profile is very useful if you subscribe to third-party
threat intelligence feeds and want to protect your network from
new sources of threat or malware as soon as you learn of a malicious
domain. For each domain you include in the external dynamic list,
the firewall creates a custom DNS-based spyware signature so that
you can enable DNS sinkholing. The DNS-based spyware signature is
of type spyware with medium severity and each signature is named Custom Malicious DNS Query <domain name> .
You can also specify the firewall to include the subdomains of a
specifed domain. For example, if your domain list includes paloaltonetworks.com,
all lower level components of the domain name (e.g., *.paloaltonetworks.com)
will also be included as part of the list. When this setting is
enabled, each domain in a given list requires an additional entry,
effectively doubling the number of entries used by the list. For
details on configuring domain lists, see configure DNS sinkholing for
a custom list of domains . 

 URL —This type of external dynamic list gives you the
agility to protect your network from new sources of threat or malware.
The firewall handles an external dynamic list with URLs like a custom
URL category and you can use this list in two ways: 

 As
a match criterion in Security policy rules, Decryption policy rules, and
QoS policy rules to allow, deny, decrypt, not decrypt, or allocate
bandwidth for the URLs in the custom category. 

 In a URL Filtering profile where you can define more granular
actions, such as continue, alert, or override, before you attach
the profile to a Security policy rule (see Use an External Dynamic List
in a URL Filtering Profile ). 

 Equipment Identity —You can reference an external dynamic
list of IoT devices defined by International Mobile Equipment Identities
(IMEIs) in a Security policy rule that controls traffic for equipment
connected to a 5G or 4G network. Refer to the Mobile Network Infrastructure
Getting Started for information about configuring Equipment ID security
on supported firewall models. 

 Subscriber Identity —You can reference an external
dynamic list of International Mobile Subscriber Identities (IMSIs)
in a Security policy rule that controls traffic for subscribers
connected to a 5G or 4G network. Refer to the Mobile Network Infrastructure
Getting Started for information about configuring Subscriber ID
security on supported firewall models. 

 On each firewall model, you can add up to a maximum of 30 custom
EDLs with unique sources that can be used to enforce policy .
The external dynamic list limit is not applicable to Panorama. When
using Panorama to manage a firewall that is enabled for multiple virtual
systems, if you exceed the limit for the firewall, a commit error
displays on Panorama. A source is a URL that includes the IP address
or hostname, the path, and the filename for the external dynamic
list. The firewall matches the URL (complete string) to determine
whether a source is unique. 

 While the firewall does not impose a limit on the number of lists
of a specific type, the following limits are enforced: 

 IP address—The PA-3200 Series, PA-5200 Series, and the PA-7000 Series firewalls support a
 maximum of 150,000 total IP addresses; all other models support a maximum of
 50,000 total IP addresses. No limits are enforced for the number of IP addresses
 per list. When the maximum supported IP address limit is reached on the
 firewall, the firewall generates a syslog message. The IP addresses in
 predefined IP address lists do not count toward the limit. 

 URL and domain—The maximum number of URLs and domains supported
varies by model. No limits are enforced for the number of URL or
domain entries per list. Refer to the following table for specifics
on your model: 

 Model 
 URL List Entry Limits Domain List Entry Limits 

 PA-5200 Series, PA-5400 Series, PA-7000 Series (upgraded
with the PA-7000 20GXM NPC, PA-7000 20GQXM NPC, or the PA-7000 100G
NPC). 

 PA-7000 appliances with mixed NPCs only support the standard
capacities. 

 250,000 4,000,000 

 VM-500, VM-700 

 100,000 
 2,000,000 

 PA-400 Series (excepting the PA-410), PA-850,
PA-820, PA-3200 Series, PA-3400 Series 

 100,000 
 1,000,000 

 PA-7000 Series (and appliances upgraded
with the PA-7000 20GQ NPC or the PA-7000 20G NPC), VM-300 

 100,000 
 500,000 

 PA-220, PA-410, VM-50, VM-50 (Lite), VM-100, VM-1000-HV 

 50,000 
 50,000 

 For EDL capacities for IMSI and IMEI, see the 5G Equipment ID and Subscriber ID
 Security in the Mobile Network Infrastructure Getting
 Started guide. 

 List entries only count toward the firewall limits if they belong
to an external dynamic list that is referenced in policy. 

 When parsing the list, the firewall skips entries
that do not match the list type, and ignores entries that exceed
the maximum number supported for the model. To ensure that the entries
do not exceed the limit, check the number of entries currently used
in policy. Select Objects External Dynamic Lists and
click List Capacities . 

 An external dynamic list must contain entries. If you want
to stop using the list, remove the reference from the policy rule
or profile instead leaving the list blank. If the list does not
contain any entries, the firewall fails to refresh the list and
continues to use the last information it retrieved. 

 As a best practice, Palo Alto Networks recommends using shared
EDLs when multiple virtual systems are used. Using individual EDLs
with duplicate entries for each virtual system uses more memory,
which might over-utilize firewall resources. 

 EDL entry counts on firewalls operating multi-virtual systems
take additional factors into account (such as DAGs, number of virtual
systems, rules bases) to generate a more accurate capacity consumption
listing. This might result in a discrepancy in capacity usage after
upgrading from PAN-OS 8.x releases. 

 Depending on the features enabled on the firewall, memory
usage limits might be exceeded before EDL capacity limits are met
due to memory allocation updates. As a best practice, Palo Alto
Networks recommends reviewing EDL capacities and, when necessary,
removing or consolidating EDLs into shared lists to minimize memory usage. 

 Previous 

 Use an External Dynamic List in Policy 

 Next 

 Formatting Guidelines for an External Dynamic List 

 On This Page 

 PAN-OS 

 Next-Generation Firewall 

 Policy 

 11.1 

 Network Security 

 11.1 & Later 

 Administration 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
