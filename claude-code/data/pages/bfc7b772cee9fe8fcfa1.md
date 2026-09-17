---
url: https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/policy/policy-based-forwarding/pbf
fetched_at: 2026-09-16T07:39:27Z
source: palo-alto-main
---

# PBF Clear

Updated on 

 Aug 11, 2025 

 Focus 

 Home 

 PAN-OS 

 Policy 

 Policy-Based
Forwarding 

 PBF 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 한국어 (Korean) 

 PBF 

 Table of Contents 

 Filter

 Previous 

 Policy-Based Forwarding 

 Next 

 Egress Path and Symmetric Return 

 PBF 

 PBF rules allow traffic to take an alternative path
from the next hop specified in the route table, and are typically
used to specify an egress interface for security or performance
reasons. Let's say your company has two links between the corporate office
and the branch office: a cheaper internet link and a more expensive
leased line. The leased line is a high-bandwidth, low-latency link.
For enhanced security, you can use PBF to send applications that
aren’t encrypted traffic, such as FTP traffic, over the private
leased line and all other traffic over the internet link. Or, for
performance, you can choose to route business-critical applications
over the leased line while sending all other traffic, such as web
browsing, over the cheaper link. 

 Egress Path and Symmetric Return 

 Path Monitoring for PBF 

 Service Versus Applications in PBF 

 Previous 

 Policy-Based Forwarding 

 Next 

 Egress Path and Symmetric Return
