---
url: https://docs.paloaltonetworks.com/advanced-url-filtering/administration/pan-db-private-cloud-overview/set-up-pan-db-private-cloud/configure-firewalls-to-access-pan-db-private-cloud
fetched_at: 2026-08-13T15:19:21Z
source: palo-alto-main
---

# Configure Firewalls to Access the PAN-DB Private Cloud Clear

Configure Firewalls to Access the PAN-DB Private Cloud 

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

 Configure Firewalls to Access the PAN-DB Private Cloud 

 Updated on 

 Thu Jul 30 16:45:14 PDT 2026 

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

 Advanced URL Filtering 

 Administration 

 Updated on 

 Thu Jul 30 16:45:14 PDT 2026 

 Focus 

 Home 

 Advanced URL Filtering 

 PAN-DB Private Cloud 

 Set Up PAN-DB Private Cloud 

 Configure Firewalls to Access the PAN-DB Private Cloud 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Advanced URL Filtering 

 Configure Firewalls to Access the PAN-DB Private Cloud 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Advanced URL Filtering 

 Administration 

 Previous 

 Configure the PAN-DB Private Cloud 

 Next 

 Configure Authentication with Custom Certificates on the PAN-DB Private Cloud 

 Configure Firewalls to Access the PAN-DB Private Cloud 

 Follow these steps to configure firewall access to the
PAN-DB private cloud servers from your CLI or the firewall’s web
interface. 

 Where can I use
this? What do I need? 

 NGFW (Managed by PAN-OS or Panorama) 

 Advanced URL
 Filtering license (or a legacy URL filtering
 license) 

 Note: Legacy URL filtering licenses are
 discontinued, but active legacy licenses are still
 supported. 

 When using the PAN-DB public cloud, each firewall accesses the PAN-DB servers in the AWS cloud to
 download the list of eligible servers to which it can connect for URL lookups. With
 the PAN-DB private cloud, you must configure the firewalls with a (static) list of
 your PAN-DB private cloud servers that will be used for URL lookups. The list can
 contain up to 20 entries; IPv4 addresses, IPv6 addresses, and FQDNs are supported.
 Each entry on the list— IP address or FQDN—must be assigned to the management port
 or eth1 of the PAN-DB server. 

 From the PAN-OS CLI , add
a list of static PAN-DB private cloud servers used for URL lookups. 

 Use the following CLI command to add the IP addresses of the private PAN-DB servers: 

 > configure 

 # set deviceconfig setting pan-url-db cloud-static-list <IP addresses> 

 Alternatively, in the web interface for each firewall, select Device Setup Content-ID , edit the URL Filtering section, and then enter the
 IP addresses or FQDNs of the PAN-DB servers. The list must be
 comma-separated. 

 To delete the entries for the private PAN-DB servers, use the following CLI command: 

 # delete deviceconfig setting pan-url-db cloud-static-list <IP addresses> 

 Deleting the list of private PAN-DB servers triggers a reelection process on the firewall. The
 firewall first checks for the list of PAN-DB private cloud servers
 and when it can't find one, the firewall accesses the PAN-DB servers
 in the AWS cloud to download the list of eligible servers to which
 it can connect. 

 Enter # commit to save your changes. 

 To verify that the change is effective, use the following
CLI command on the firewall: 

 > show url-cloud status 
Cloud status: Up 
URL database version: 20150417-220 

 Previous 

 Configure the PAN-DB Private Cloud 

 Next 

 Configure Authentication with Custom Certificates on the PAN-DB Private Cloud 

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

 IPSec VPN 

 Security Policy 

 Quantum Security 

 Endpoints 

 GlobalProtect 

 Remote Browser Isolation 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 11.0 

 10.1 

 Network Security 

 PAN-OS 

 10.2 

 11.1 

 Cloud-Delivered Security Services 

 URL Filtering 

 Administration 

 9.1 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
