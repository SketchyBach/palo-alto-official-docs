---
url: https://docs.paloaltonetworks.com/advanced-ip-defense/getting-started/update-advanced-ip-defense-connectivity-settings
fetched_at: 2026-09-15T15:08:17Z
source: palo-alto-main
---

# Manage Advanced IP Defense Connectivity Settings Clear

Updated on 

 Aug 28, 2026 

 Focus 

 Home 

 Advanced IP Defense 

 Manage Advanced IP Defense Connectivity Settings 

 Download PDF 

 Advanced IP Defense 

 Manage Advanced IP Defense Connectivity Settings 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Advanced IP Defense Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Release Notes 

 New Features 

 Previous 

 Enable Role Based Access to Advanced IP Defense 

 Next 

 Create an Advanced IP Defense Profile 

 Manage Advanced IP Defense Connectivity Settings 

 Configure connectivity settings to ensure reliable communication between your firewall and Advanced IP Defense . 

 Where Can I Use
 This? What Do I Need? 

 NGFW (Managed by Strata Cloud Manager) 

 NGFW (Managed by PAN-OS or Panorama) 

 VM-Series 

 Advanced IP Defense license 

 PAN-OS 12.2.3 and later 

 Advanced IP Defense relies on continuous communication between the firewall and
 Advanced IP Defense to deliver real-time threat detection. The
 firewall sends two types of messages to the cloud: copies of DNS response IP-TTL pairs
 that Advanced IP Defense uses to build a per-tenant DNS state table, and Advanced IP Defense lookup requests that query IP attributes and direct-to-IP
 status for a given destination. Because these exchanges happen inline with traffic
 processing, connectivity reliability directly affects detection accuracy and user
 experience. 

 On a cache miss, the firewall allows the initial session to pass (fail-open) and
 asynchronously queries Advanced IP Defense for a verdict. The firewall does not
 hold or buffer packets while waiting for the cloud response. Once the verdict is
 returned, the local cache is populated and the policy is strictly enforced on all
 subsequent sessions matching that IP. If Advanced IP Defense becomes unreachable,
 the firewall reverts to fail-open to prevent a network outage. 

 The firewall caches IP attributes locally to reduce the volume of cloud lookups. The
 firewall only queries Advanced IP Defense on a cache miss—when it encounters
 an IP that isn't in the local cache or whose cached attributes have expired. 

 Strata Cloud Manager 

 PAN-OS & Panorama 

 Manage Advanced IP Defense Connectivity Settings in Strata Cloud Manager 

 Configure the Advanced IP Defense cloud endpoint and verify connectivity for your Strata Cloud Manager -managed firewalls. 

 Before configuring Advanced IP Defense connectivity, ensure: 

 Enforcement points can reach Advanced IP Defense endpoints on TCP 443.
 If firewalls are behind a proxy, configure proxy settings under Configuration Device Settings Services . 

 DNS servers are configured and can resolve Advanced IP Defense domain names. For the full list of domains, see Regional Service Domains . 

 The Advanced IP Defense connectivity settings control which cloud endpoint your
 managed firewalls use for real-time IP attribute lookups and direct-to-IP detection.
 Enforxement points communicate with Advanced IP Defense over TLS on port
 443. 

 Advanced IP Defense configuration management in Strata Cloud Manager is
 rolling out progressively and will be available in an upcoming release. Monitoring
 and logging capabilities (Activity Insights, Command Center, Threat Search, and log
 viewing) are available immediately. 

 Log in to Strata Cloud Manager . 

 Select Configuration NGFW and Prisma Access Security Services Advanced IP Defense . 

 Click the Settings tab. 

 Set the regional service domain FQDN. 

 By default, enforcement point uses the global anycast FQDN, which routes
 lookups to the nearest regional server. You can configure a specific
 regional FQDN for latency optimization or data residency requirements. 

 Click Save and Push your changes. 

 Manage Advanced IP Defense Connectivity Settings in PAN-OS and Panorama 

 Configure the Advanced IP Defense cloud endpoint and verify connectivity from your firewall. 

 Before configuring Advanced IP Defense connectivity, ensure: 

 Enforcement points can reach Advanced IP Defense endpoints on TCP 443.
 If your enforcement point is behind a proxy, configure proxy settings
 under Device Setup Services . 

 DNS servers are configured and can resolve Advanced IP Defense domain names. For the full list of domains, see Regional Service Domains . 

 The Advanced IP Defense connectivity settings control which cloud endpoint the
 enforcement point uses for real-time IP attribute lookups and direct-to-IP
 detection. The enforcement point communicates with Advanced IP Defense over TLS
 on TCP 443. 

 Log in to the PAN-OS web interface. 

 Select Device Setup Content-ID . 

 In the Advanced IP Defense Settings section, click the edit icon. 

 Set the AIPD Cloud Endpoint to a Regional Service Domains 
 FQDN. 

 By default, enforcement point uses the global anycast FQDN, which routes
 lookups to the nearest regional server. You can configure a specific
 regional FQDN for latency optimization or data residency requirements. 

 Click OK and Commit your changes. 

 Verify connectivity by running the following CLI command: 

 show ip-defense status 

 A successful response confirms that the enforcement point can reach Advanced IP Defense . Verify that Cloud connection 
 shows Connected and Last Result shows
 Good . 

 admin@PA-XXXX> show ip-defense status

Advanced IP Defense cloud
License: Valid
Configurations: Enabled
Current cloud server: api.prod.aipd.service.paloaltonetworks.com
Cloud connection: Connected
Last Result: Good ( 14 sec ago )
Allowlist Refresh: Interval 1800 sec ( Due 944 sec )
Last up time: 2026/08/21 15:22:39 to now
Last down time: N/A

Cookies Information :
Region state: Assigned
Region ID: us-central1
Region timestamp: 2026/08/21 15:22:39
TSG state: Assigned
TSG ID: 1234567890
TSG timestamp: 2026/08/21 15:22:39

Certificate Information :
Thermite : Available
Subject : CN = 00XXXXXXXXXXX, O = Palo Alto Networks, L = Santa Clara, ST = CA, C = US
Issuer : CN = USC-Client-Issuing-CA2-G5, O = Palo-Alto-Networks-Inc., C = US
CA : no
Not-valid-before : Aug 17 23:03:01 2026 GMT
Not-valid-after : Nov 15 23:03:00 2026 GMT 

 Previous 

 Enable Role Based Access to Advanced IP Defense 

 Next 

 Create an Advanced IP Defense Profile
