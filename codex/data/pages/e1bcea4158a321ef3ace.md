---
url: https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/user-id/deploy-user-id-in-a-large-scale-network/insert-username-in-http-headers
fetched_at: 2026-08-13T17:05:21Z
source: palo-alto-main
---

# Insert Username in HTTP Headers Clear

Insert Username in HTTP Headers 

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

 Insert Username in HTTP Headers 

 Updated on 

 Mon Aug 03 13:41:44 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Generation Firewall Docs 

 Getting Started 

 Administration 

 Networking 

 Quick Start 

 Reference 

 Incidents & Alerts 

 Release Notes 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 11.0 (EoL) 

 PAN-OS 10.2 

 PAN-OS 10.1 (EoL) 

 PAN-OS 10.0 (EoL) 

 PAN-OS 9.1 (EoL) 

 PAN-OS 9.0 (EoL) 

 PAN-OS 8.1 (EoL) 

 Help 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 10.2 

 PAN-OS 10.1 

 New Features 

 Updated on 

 Mon Aug 03 13:41:44 PDT 2026 

 Focus 

 Home 

 Next-Generation Firewall 

 User-ID 

 Deploy User-ID in a Large-Scale Network 

 Insert Username in HTTP Headers 

 Download PDF 

 Next-Generation Firewall 

 Insert Username in HTTP Headers 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Generation Firewall Docs 

 Getting Started 

 Administration 

 Networking 

 Quick Start 

 Reference 

 Incidents & Alerts 

 Release Notes 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 11.0 (EoL) 

 PAN-OS 10.2 

 PAN-OS 10.1 (EoL) 

 PAN-OS 10.0 (EoL) 

 PAN-OS 9.1 (EoL) 

 PAN-OS 9.0 (EoL) 

 PAN-OS 8.1 (EoL) 

 Help 

 Select a Document 

 PAN-OS 12.2 

 PAN-OS 12.1 

 PAN-OS 11.2 

 PAN-OS 11.1 

 PAN-OS 10.2 

 PAN-OS 10.1 

 New Features 

 Previous 

 Configure User-ID for Numerous Mapping Information Sources 

 Next 

 Redistribute Data and Authentication Timestamps 

 Insert Username in HTTP Headers 

 Configure the firewall to include the domain and username
in the traffic headers to allow other appliances to receive user
identification information. 

 When you configure a secondary enforcement
appliance with your Palo Alto Networks firewall to enforce user-based policy,
the secondary appliance may not have the IP address-to-username
mapping from the firewall. Transmitting user information to downstream
appliances may require deployment of additional appliances such
as proxies or negatively impact the user’s experience (for example, users
having to log in multiple times). By sharing the user's identity
in the HTTP headers, you can enforce user-based policy without negatively impacting
the user's experience or deploying additional infrastructure. 

 When
you configure this feature, apply the URL profile to your Security
policy, and commit your changes, the firewall: 

 Populates
the user and domain values with the format of the primary username in the
group mapping for the source user. 

 Encodes this information using Base64. 

 Adds the Base64-encoded header to the payload. 

 Routes the traffic to the downstream appliance. 

 If
you want to include the username and domain only when the user accesses
specific domains, configure a domain list and the firewall inserts
the header only when a domain in the list matches the Host header
of the HTTP request. 

 To share user information with downstream
appliances, you must first enable User-ID and configure group mapping . 

 To
include the username and domain in the header, the firewall requires
the IP address-to-username mapping for the user. If the user is
not mapped, the firewall inserts unknown in
Base64 encoding for both the domain and username in the header. 

 To
include the username and domain in headers for HTTPS traffic, you
must first create a decryption profile to
decrypt HTTPS traffic. 

 This feature supports forward-proxy
decryption traffic. 

 Create or edit a URL
Filtering Profile . 

 The firewall does not insert headers if the action for
the URL filtering profile is block for the
domain. 

 Create or edit an HTTP header insertion
entry using predefined types. 

 You can define up to five headers for each profile. 

 Select Dynamic Fields as the header Type . 

 Add the Domains where
you want insert headers. When the user accesses a domain in the
list, the firewall inserts the specified header. 

 Add a new Header or
select X-Authenticated-User to edit it. 

 Select a header Value format (either ($domain)\($user) or WinNT://($domain)/($user) )
or enter your own format using the ($domain) and ($user) dynamic
tokens (for example, ($user)@($domain) for
UserPrincipalName). 

 Do not use the same dynamic token (either ($user) or ($domain) )
more than once per value. 

 Each value can be up to 512 characters.
The firewall populates the ($user) and ($domain) dynamic
tokens using the primary username in the group mapping profile.
For example: 

 If the primary username is the sAMAccountName,
the value for ($user) is the sAMAccountName
and the value for ($domain) is the NetBios
domain name. 

 If the primary username is the UserPrincipalName, the ($user) the
user account name (prefix) and the ($domain) is
the Domain Name System (DNS) name. 

 (Optional) Select Log to enable
logging for the header insertion. 

 Apply the URL filtering profile to the security policy
rule for HTTP or HTTPS traffic. 

 Select OK twice to confirm the
HTTP header configuration. 

 Commit your changes. 

 Verify the firewall includes the username and domain
in the HTTP headers. 

 Use the show user user-ids all command
to verify the group mapping is correct. 

 Use the show counter global name ctd_header_insert command
to view the number of HTTP headers inserted by the firewall. 

 If you configured logging in Step 7, check the logs for the inserted
Base64 encoded payload (for example, corpexample\testuser would
appear in the logs as Y29ycGV4YW1wbGVcdGVzdHVzZXI= ). 

 Previous 

 Configure User-ID for Numerous Mapping Information Sources 

 Next 

 Redistribute Data and Authentication Timestamps 

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

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Network Security 

 PAN-OS 

 Next-Generation Firewall 

 Administration 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
