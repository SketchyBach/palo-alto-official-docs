---
url: https://docs.paloaltonetworks.com/dns-security/administration/configure-dns-security/configure-lookup-timeout
fetched_at: 2026-08-13T15:31:55Z
source: palo-alto-main
---

# Configure Lookup Timeout Clear

Configure Lookup Timeout 

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

 Configure Lookup Timeout 

 Updated on 

 Thu Jul 30 19:02:25 PDT 2026 

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

 Advanced DNS Security 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Release Notes 

 Updated on 

 Thu Jul 30 19:02:25 PDT 2026 

 Focus 

 Home 

 Advanced DNS Security Powered by Precision AI® 

 Configure DNS Security Subscription Services 

 Configure Lookup Timeout 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Advanced DNS Security Powered by Precision AI® 

 Configure Lookup Timeout 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Advanced DNS Security 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Release Notes 

 Previous 

 Test Connectivity to the DNS Security Cloud Services 

 Next 

 Configure No DNS UDP Discard 

 Configure Lookup Timeout 

 Adjust DNS timeout settings to match average latency. If the NGFW cannot retrieve a
 signature verdict within the allotted time, it will pass the DNS request through without
 inspection. 

 Where Can I Use
 This? What Do I Need? 

 NGFW (Managed by Strata Cloud Manager) 

 NGFW (Managed by PAN-OS or Panorama) 

 VM-Series 

 CN-Series 

 Advanced DNS Security License (for enhanced feature
 support) or DNS Security License 

 Advanced Threat Prevention or Threat Prevention
 License 

 DNS Security 

 If the firewall is unable to retrieve a signature verdict in the allotted time
 due to connectivity issues, the request, including all subsequent DNS responses,
 are passed through. You can check the average latency to verify that requests
 fall within the configured period. If the average latency exceeds the configured
 period, consider updating the setting to a value that is higher than the average
 latency to prevent requests from timing out. 

 In the CLI, issue the following command to view the average latency. 

 show dns-proxy dns-signature
counters 

 The default timeout is 100 milliseconds. 

 Scroll down through the output to the latency section under the Signature
 query API heading and verify that the average latency falls within the
 defined timeout period. This latency indicates the amount of time it takes,
 on average, to retrieve a signature verdict from the DNS security service.
 Additional latency statistics for various latency periods can be found below
 the averages. 

 Signature query API:
 .
 .
 .
 [latency ] :
 max 1870 (ms) min 16(ms) avg 27(ms)
 50 or less : 47246
 100 or less : 113
 200 or less : 25
 400 or less : 15
 else : 21 

 If the average latency is consistency above the default timeout value, you
 can raise the setting so that the requests fall within a given period.
 Select Device > Content-ID and update the
 Realtime Signature Lookup setting. 

 Commit the changes. 

 Advanced DNS Security 

 View the record of round trip times (in milliseconds) for Advanced DNS
 Security requests using the following debug CLI command. These are
 distributed into latency brackets from 0ms to 450ms. You can use this to
 determine the ideal max latency setting for your NGFW. 

 admin@PA-VM debug dataplane show ctd feature-forward stats 

 In the response output, navigate to the section
 PAN_CTDF_DETECT_SERVICE_ADNS . 

 PAN_CTDF_DETECT_SERVICE_ADNS
cli_timeout: 1
req_total: 2
req_timed_out: 0
Hold:
adns rtt>=0ms: 0
adns rtt>=50ms: 2
adns rtt>=100ms: 0
adns rtt>=150ms: 0
adns rtt>=200ms: 0
adns rtt>=250ms: 0
adns rtt>=300ms: 0
adns rtt>=350ms: 0
adns rtt>=400ms: 0
adns rtt>=450ms: 0 

 Configure the maximum Advanced DNS signature lookup timeout setting. When
 this value is exceeded, the DNS response passes through without performing
 analysis using Advanced DNS Security. DNS signatures (and their associated
 policies) that are delivered through regular content updates or are part of
 configured EDLs (external dynamic lists) or DNS exceptions are still
 applied. 

 Select Device Setup Content-ID Advanced DNS Security . 

 Specify an updated maximum Advanced DNS signature lookup timeout
 setting in milliseconds. The default is 100ms and is the recommended
 setting. 

 Click OK to confirm your changes. 

 Alternatively, you can use the following CLI command to configure the
 Advanced DNS Security timeout value. You can set a value of 100-15,000ms
 in 100ms increments. The default value is 100ms and is the recommended
 setting. 

 admin@PA-VM# set deviceconfig setting adns-setting max-latency <timeout_value_in_milliseconds>

 For example: 

 admin@PA-VM# set deviceconfig setting adns-setting max-latency 500 

 You can check the current timeout configuration using the following CLI
 command (refer to the max-latency entry of the
 output). 

 admin@PA-VM show config pushed-template 
...
 }
 deviceconfig {
 setting {
 dns {
 dns-cloud-server dns.service.paloaltonetworks.com;
 }
 adns-setting {
 max-latency 100; 
 }
 }
 }
... 

 Previous 

 Test Connectivity to the DNS Security Cloud Services 

 Next 

 Configure No DNS UDP Discard 

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

 Endpoints 

 GlobalProtect 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 11.0 

 10.1 

 10.2 

 Administration 

 Prisma Access 

 9.1 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
