---
url: https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/policy/use-an-external-dynamic-list-in-policy/formatting-guidelines-for-an-external-dynamic-list/domain-list
fetched_at: 2026-08-13T17:10:02Z
source: palo-alto-main
---

# Domain List Clear

Domain List 

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

 Domain List 

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

 Formatting Guidelines for an External Dynamic List 

 Domain List 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 한국어 (Korean) 

 Domain List 

 Table of Contents 

 Filter

 Previous 

 IP Address List 

 Next 

 URL List 

 Domain List 

 You can use placeholder characters in domain lists to
configure a single entry to match against multiple website subdomains,
pages, including entire top-level domains, as well as matches to
specific web pages. 

 Follow these guidelines when creating domain list entries: 

 Enter each domain name in a new line; URLs or IP addresses
are not supported in this list. 

 Do not prefix the domain name with the protocol, http://
or https://. 

 You can use an asterisk (*) to indicate a wildcard value. 

 You can use a caret (^) to indicate an exact match value. 

 The following characters are considered token separators:
. / ? & = ; + 

 Every string separated by one or two of
these characters is a token. Use wildcard characters as token placeholders,
indicating that a specific token can contain any value. 

 Wildcard characters must be the only character within a token;
however, an entry can contain multiple wildcards. 

 Each domain entry can be up to 255 characters in length. 

 When to use the asterisk (*) wildcard: 

 Use an asterisk (*) wildcard to indicate one or multiple variable
subdomains. For example, to specify enforcement for Palo Alto Network’s
website regardless of the domain extension used, which might be
one or two subdomains depending on location, you would add the entry: *.paloaltonetworks.com .
This entry would match to both docs.paloaltonetworks.com and support.paloaltonetworks.com. 

 You can also use this wildcard to indicate entire top-level domains.
For example, to specify enforcement of a TLD named .work, you would
add the entry *.work . This matches all websites
ending with .work. 

 The (*) wildcard can only be prepended in domain entries. 

 Asterisk (*) examples 

 EDL Domain List Entry Matching Sites 

 *.company.com 

 eng.tools.company.com 

 support.tools.company.com 

 tools.company.com 

 docs.company.com 

 *.click 

 all websites ending with a top-level domain
of .click. 

 When to use a caret (^) character: 

 Use carets (^) to indicate an exact match of a subdomain. For
example, ^paloaltonetworks.com matches only
paloaltonetworks.com. This entry does not match to any other site. 

 Caret (^) examples 

 EDL Domain List Entry Matching Site 

 ^company.com 

 company.com 

 ^eng.company.com 

 eng.company.com 

 Previous 

 IP Address List 

 Next 

 URL List 

 On This Page 

 PAN-OS 

 Next-Generation Firewall 

 Policy 

 11.1 

 Network Security 

 11.1 & Later 

 Administration 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
