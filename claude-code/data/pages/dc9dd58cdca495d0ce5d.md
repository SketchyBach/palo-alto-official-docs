---
url: https://docs.paloaltonetworks.com/advanced-ip-defense/getting-started/update-advanced-ip-defense-connectivity-settings
fetched_at: 2026-08-13T15:23:36Z
source: palo-alto-main
---

# Edit Advanced IP Defense Connectivity Settings Clear

Edit Advanced IP Defense Connectivity Settings 

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

 Edit Advanced IP Defense Connectivity Settings 

 Updated on 

 May 22, 2026 

 Focus 

 Download PDF 

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

 Updated on 

 May 22, 2026 

 Focus 

 Home 

 Advanced IP Defense 

 Edit Advanced IP Defense Connectivity Settings 

 Download PDF 

 Advanced IP Defense 

 Edit Advanced IP Defense Connectivity Settings 

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

 Edit Advanced IP Defense Connectivity Settings 

 Configure connectivity settings to ensure reliable communication between your firewall and the Advanced IP Defense cloud service. 

 Where Can I Use This? What Do I Need? 

 PAN-OS 12.2 and later 

 Strata Cloud Manager 

 Advanced IP Defense license 

 Admin access to firewall or Strata Cloud Manager 

 Network connectivity to Advanced IP Defense cloud service endpoints 

 Advanced IP Defense relies on continuous communication between the firewall and the Advanced IP Defense cloud service to deliver real-time threat detection. The firewall sends two types of messages to the cloud: copies of DNS response IP-TTL pairs that the Advanced IP Defense cloud service uses to build a per-tenant DNS state table, and Advanced IP Defense lookup requests that query IP attributes and direct-to-IP status for a given destination. Because these exchanges happen inline with traffic processing, connectivity reliability directly affects detection accuracy and user experience. 

 On a cache miss, the firewall allows the initial session to pass (fail-open) and asynchronously queries the Advanced IP Defense cloud service for a verdict. The firewall does not hold or buffer packets while waiting for the cloud response. Once the verdict is returned, the local cache is populated and the policy is strictly enforced on all subsequent sessions matching that IP. If the Advanced IP Defense cloud service becomes unreachable, the firewall reverts to fail-open to prevent a network outage. 

 The firewall caches IP attributes locally to reduce the volume of cloud lookups. The firewall only queries the Advanced IP Defense cloud service on a cache miss—when it encounters an IP that isn't in the local cache or whose cached attributes have expired. 

 The firewall also periodically pulls updated allowlist files from the cloud to pre-populate known-safe entries locally. This pull occurs at regular intervals and delivers two per-tenant files: one for the Advanced IP Defense allowlist and one for the direct-to-IP allowlist. If the firewall can't reach the cloud endpoint, it continues to use the most recent cached version of the allowlists. When the firewall reaches its maximum DNS cache capacity, it fails open on direct-to-IP detection and doesn't take action on direct-to-IP traffic until capacity is available. 

 Strata Cloud Manager 

 PAN-OS 

 Edit Advanced IP Defense Connectivity Settings in Strata Cloud Manager 

 Configure Strata Cloud Manager connectivity settings to enable communication with the Advanced IP Defense cloud service for real-time IP attribute lookups and direct-to-IP detection. 

 Strata Cloud Manager manages connectivity settings for cloud-managed firewalls and Prisma Access deployments. Connectivity settings control how your cloud-managed infrastructure communicates with the Advanced IP Defense cloud service. Proper connectivity configuration ensures optimal performance and reliability of Advanced IP Defense threat detection across your cloud-managed environment. 

 Use the credentials associated with your Palo Alto Networks support account and
 log in to the Strata Cloud Manager on the hub . 

 Access the Advanced IP Defense connectivity settings in Strata Cloud Manager . 

 Select Configuration Device Settings Cloud Services to access connectivity settings for cloud-based security services. 

 Verify Advanced IP Defense cloud service connectivity status. 

 The cloud-managed infrastructure uses an asynchronous fail-open model for cloud lookups. On a cache miss, traffic is allowed to pass and the system queries the Advanced IP Defense cloud service asynchronously. Once the verdict is returned, the local cache is populated and the policy is enforced on subsequent sessions. If the Advanced IP Defense cloud service becomes unreachable, the system fails open to prevent a network outage. 

 Ensure that network connectivity to the Advanced IP Defense cloud service endpoints on port 443 is stable. Verify DNS servers are configured and can resolve Advanced IP Defense cloud service domain names. 

 (Optional) Configure proxy server settings for cloud connectivity. 

 If your cloud-managed infrastructure is deployed behind a proxy server or in an environment that requires proxy authentication, you must configure proxy settings to enable communication with the Advanced IP Defense cloud service. 

 Select Configuration Device Settings Services and configure the proxy server settings: 

 Enter the proxy server IP address or FQDN 

 Specify the proxy server port number 

 Enter proxy authentication credentials if required 

 Enable the option to use proxy for inline cloud services 

 The proxy server password must contain a minimum of six characters. 

 Verify network connectivity to Advanced IP Defense cloud service endpoints. 

 Ensure that your cloud-managed infrastructure has network connectivity to the Advanced IP Defense cloud service endpoints. The infrastructure must be able to reach the Advanced IP Defense cloud service on port 443 (HTTPS) for secure communication. 

 You can verify connectivity by: 

 Checking network routing to ensure traffic to Advanced IP Defense cloud service endpoints is not blocked 

 Verifying that security policies allow outbound HTTPS traffic to Advanced IP Defense cloud service IPs 

 Confirming that any proxy servers or firewalls between your infrastructure and the internet allow traffic to the Advanced IP Defense cloud service 

 Configure DNS resolution for Advanced IP Defense cloud service endpoints. 

 The cloud-managed infrastructure must be able to resolve the Advanced IP Defense cloud service domain names to IP addresses. Ensure that your infrastructure has access to DNS servers that can resolve these domain names. 

 Select Configuration Device Settings Services and verify that DNS servers are configured. You can specify primary and secondary DNS servers to ensure redundancy. 

 Test connectivity to the Advanced IP Defense cloud service. 

 After configuring connectivity settings, test the connection to verify that the cloud-managed infrastructure can reach the Advanced IP Defense cloud service. 

 Select Configuration Device Settings Services and click Test Connectivity to verify that the infrastructure can successfully communicate with the Advanced IP Defense cloud service. A successful test confirms that your connectivity settings are correct. 

 Monitor Advanced IP Defense cloud service connectivity status. 

 After enabling Advanced IP Defense , monitor the connectivity status to ensure the cloud-managed infrastructure maintains a stable connection to the Advanced IP Defense cloud service. 

 Select Monitor System Cloud Services to view the status of Advanced IP Defense cloud service connections. Check for any connectivity errors or warnings that may indicate network issues. 

 Commit your changes. 

 Click Commit to apply the connectivity settings to your Strata Cloud Manager configuration. 

 Edit Advanced IP Defense Connectivity Settings in PAN-OS and Panorama 

 Configure PAN-OS and Panorama connectivity settings to enable communication with the Advanced IP Defense cloud service for real-time IP attribute lookups and direct-to-IP detection. 

 PAN-OS and Panorama manage connectivity settings for on-premises firewalls and Panorama -managed deployments. Connectivity settings control how your firewall or Panorama communicates with the Advanced IP Defense cloud service. Proper connectivity configuration ensures optimal performance and reliability of Advanced IP Defense threat detection across your on-premises infrastructure. 

 Log in to the 

 Access the Advanced IP Defense connectivity settings. 

 In PAN-OS or Panorama , select Device Setup Content-ID to access the global connectivity settings for cloud-based security services. 

 Verify Advanced IP Defense cloud service connectivity status. 

 The firewall uses an asynchronous fail-open model for cloud lookups. On a cache miss, the firewall allows the initial session and queries the Advanced IP Defense cloud service asynchronously. Once the verdict is returned, the local cache is populated and the policy is enforced on subsequent sessions. If the Advanced IP Defense cloud service becomes unreachable, the firewall fails open to prevent a network outage. 

 Ensure that network connectivity to the Advanced IP Defense cloud service endpoints on port 443 is stable. Verify DNS servers are configured and can resolve Advanced IP Defense cloud service domain names. 

 (Optional) Configure proxy server settings for cloud connectivity. 

 If your firewall is deployed behind a proxy server or in an environment that requires proxy authentication, you must configure proxy settings to enable communication with the Advanced IP Defense cloud service. 

 Select Device Setup Services and configure the proxy server settings: 

 Enter the proxy server IP address or FQDN 

 Specify the proxy server port number 

 Enter proxy authentication credentials if required 

 Enable the option to use proxy for inline cloud services 

 The proxy server password must contain a minimum of six characters. 

 Verify network connectivity to Advanced IP Defense cloud service endpoints. 

 Ensure that your firewall has network connectivity to the Advanced IP Defense cloud service endpoints. The firewall must be able to reach the Advanced IP Defense cloud service on port 443 (HTTPS) for secure communication. 

 You can verify connectivity by: 

 Checking firewall routing to ensure traffic to Advanced IP Defense cloud service endpoints is not blocked 

 Verifying that security policies allow outbound HTTPS traffic to Advanced IP Defense cloud service IPs 

 Confirming that any proxy servers or firewalls between your firewall and the internet allow traffic to the Advanced IP Defense cloud service 

 Configure DNS resolution for Advanced IP Defense cloud service endpoints. 

 The firewall must be able to resolve the Advanced IP Defense cloud service domain names to IP addresses. Ensure that your firewall has access to DNS servers that can resolve these domain names. 

 Select Device Setup Services and verify that DNS servers are configured. You can specify primary and secondary DNS servers to ensure redundancy. 

 Test connectivity to the Advanced IP Defense cloud service. 

 After configuring connectivity settings, test the connection to verify that the firewall can reach the Advanced IP Defense cloud service. 

 Select Device Setup Services and click Test Connectivity to verify that the firewall can successfully communicate with the Advanced IP Defense cloud service. A successful test confirms that your connectivity settings are correct. 

 Monitor Advanced IP Defense cloud service connectivity status. 

 After enabling Advanced IP Defense , monitor the connectivity status to ensure the firewall maintains a stable connection to the Advanced IP Defense cloud service. 

 Select Monitor System Cloud Services to view the status of Advanced IP Defense cloud service connections. Check for any connectivity errors or warnings that may indicate network issues. 

 Commit your changes. 

 Click Commit to apply the connectivity settings to your firewall. 

 Previous 

 Enable Role Based Access to Advanced IP Defense 

 Next 

 Create an Advanced IP Defense Profile 

 On This Page 

 Activation and Onboarding 

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

 Panorama 

 Service Provider 

 VM-Series 

 Plugins 

 SASE 

 Prisma Access 

 Prisma SASE Multitenant Platform 

 AI-Powered ADEM 

 Prisma Access Monitoring & Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

 Cloud-Delivered Security Services 

 Advanced WildFire 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 AI Access Security 

 Device Security 

 Enterprise DLP 

 SaaS Security 

 Network Security 

 Shared Policy for NGFWs and Prisma Access 

 IPSec VPN 

 Security Policy 

 Quantum Security 

 Endpoints 

 GlobalProtect 

 Remote Browser Isolation 

 Prisma Access Agent 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 FedRAMP 

 Prisma SASE for FedRAMP 

 Autonomous DEM for FedRAMP 

 Hardware Reference 

 ION 1000 

 ION 1200 

 ION 1200-S 

 ION 2000 

 ION 3000 

 ION 3200 

 ION 5200 

 ION 7000 

 ION 9000 

 ION 9200 

 Hardware Quick Start Guides 

 ION 1200 

 ION 1200 4G 

 ION 1200 5G 

 ION 1200-S 

 ION 1200-S 4G 

 ION 1200-S 5G 

 ION 3200 

 ION 5200 

 ION 9200 

 Virtual ION Deployment 

 Virtual ION on AWS 

 Virtual ION on Azure 

 Virtual ION on GCP 

 Virtual ION on Alibaba Cloud 

 Virtual ION on KVM for NFV 

 Virtual ION on Dell PowerEdge 

 Virtual ION on OCI 

 Virtual ION on VMware 

 Virtual ION on Megaport Virtual Edge 

 3rd Party Integrations 

 AWS Cloud-WAN Integration (GRE Connect) 

 AWS Cloud-WAN Integration (Tunnel-less Connect) 

 Checkpoint Integration 

 LiveAction Integration 

 Netskope Integration 

 Symantec Web Security Services Integration 

 Prisma SD-WAN Experts Corner 

 Network Policy 

 QoS Whitepaper 

 Security Architecture Whitepaper 

 External Antennas for ION-C Series 

 Dynamic Path Selection 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Resources 

 All Products A - Z 

 All Release Notes 

 Compatibility Matrix 

 Experts Corner 

 Network Security Platform 

 Security Policy 

 Decryption 

 Device-ID 

 IPSec VPN 

 Quality of Service 

 Quantum Security 

 Advanced IP Defense 

 Getting Started 

 Cloud-Delivered Security Services 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
