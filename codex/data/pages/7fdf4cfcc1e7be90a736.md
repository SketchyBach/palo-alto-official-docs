---
url: https://docs.paloaltonetworks.com/cloud-ngfw-aws/administration/protect/cloud-ngfw-native-policy-management/x-forwarded-for
fetched_at: 2026-09-15T15:09:11Z
source: palo-alto-main
---

# X-Forwarded-For on Cloud NGFW for AWS Clear

Updated on 

 Wed Aug 19 05:21:24 PDT 2026 

 Focus 

 Home 

 Cloud NGFW for AWS 

 Cloud NGFW for AWS Administration 

 Protect 

 Cloud NGFW Native Policy Management 

 X-Forwarded-For on Cloud NGFW for AWS 

 Download PDF 

 English 

 日本語 (Japanese) 

 Français (French) 

 Deutsch (German) 

 Cloud NGFW for AWS 

 X-Forwarded-For on Cloud NGFW for AWS 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Cloud NGFW for AWS Docs 

 Getting Started 

 Deployment 

 Administration 

 Reference 

 Release Notes 

 New Features 

 Previous 

 Rulestacks and Rules on Cloud NGFW for AWS 

 Next 

 Create a Prefix List on Cloud NGFW for AWS 

 X-Forwarded-For on Cloud NGFW for AWS 

 Learn how ingress traffic to your applications passes through AWS load balancers or
 proxy servers before it reaches the NGFW. 

 Where Can I Use This? What Do I Need? 

 Cloud NGFW for AWS 

 Cloud NGFW subscription 

 Palo Alto Networks Customer Support Account (CSP) 

 AWS Marketplace account 

 User role (either tenant or administrator) 

 The ingress traffic to your applications might pass through AWS load balancers or proxy
 servers before it reaches the NGFW. Because these devices intercept traffic between the
 source and destination, the NGFW sees the IP address of the load balancer or proxy
 server instead of the IP address of the source. These devices add the X-Forwarded-For
 (XFF) header to HTTP requests and add the actual IPv4 or IPv6 address of the client
 accessing your application. 

 Traffic to your applications might have passed more than one proxy server before it
 reaches the NGFW. The XFF request header might contain multiple IP addresses that are
 separated by commas. NGFW always uses the most recently added address in the XFF header
 to enforce policy. 

 When configuring the rulestack , you can enable
 Cloud NGFW to use the source IP address in an XFF HTTP header field to enforce security
 policy. 

 Previous 

 Rulestacks and Rules on Cloud NGFW for AWS 

 Next 

 Create a Prefix List on Cloud NGFW for AWS
