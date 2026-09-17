---
url: https://docs.paloaltonetworks.com/advanced-threat-prevention/custom-signatures/dns-req-section
fetched_at: 2026-09-16T08:20:17Z
source: palo-alto-main
---

# dns-req-section Clear

Updated on 

 Thu Sep 03 18:17:31 PDT 2026 

 Focus 

 Home 

 Advanced Threat Prevention Powered by Precision AI® 

 dns-req-section 

 Download PDF 

 Advanced Threat Prevention Powered by Precision AI® 

 dns-req-section 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Advanced Threat Prevention 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Custom Application IDs and Signatures 

 Reference 

 dns-req-section 

 Where Can I Use
 This? What Do I Need? 

 Prisma Access (Managed by Panorama or Strata Cloud Manager) 

 NGFW (Managed by Panorama or Strata Cloud Manager) 

 VM-Series 

 CN-Series 

 Advanced Threat Prevention (for enhanced feature
 support) or Threat Prevention License 

 This context matches the DNS questions of a DNS query
so that patterns can be written against one or more domains in a
given DNS query. 

 Additional Details 

 This context
is a direct pattern match against the format of a DNS query, so
patterns must adhere to the DNS question structure. A recommended
approach to create a DNS pattern is to capture the DNS request with
Wireshark and copy the DNS Request field (make sure to remove the
ending period in the request). 

 Context Capture 

 This example illustrates
how to build a signature for a DNS query for the domain www.thebayareagamers.com. 

 The
Wireshark representation of the above table. Everything highlighted
yellow and blue is provided by this context. The blue section is
where the hexadecimal string is pulled from for the above table.
