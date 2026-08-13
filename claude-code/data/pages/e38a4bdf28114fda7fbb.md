---
url: https://docs.paloaltonetworks.com/pan-os/10-1/pan-os-admin/policy/use-an-external-dynamic-list-in-policy/view-external-dynamic-list-entries
fetched_at: 2026-08-13T17:01:28Z
source: palo-alto-main
---

# View External Dynamic List Entries Clear

View External Dynamic List Entries 

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

 View External Dynamic List Entries 

 Updated on 

 Aug 5, 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Network Security Docs 

 Security Policy 

 IPsec VPN 

 Decryption 

 Device-ID 

 Quantum Security 

 Quality of Service 

 Updated on 

 Aug 5, 2026 

 Focus 

 Home 

 Network Security 

 Network Security: Security Policy 

 Policy Objects 

 Policy Object: External Dynamic Lists 

 View External Dynamic List Entries 

 Download PDF 

 Network Security 

 View External Dynamic List Entries 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Network Security Docs 

 Security Policy 

 IPsec VPN 

 Decryption 

 Device-ID 

 Quantum Security 

 Quality of Service 

 Previous 

 Retrieve an External Dynamic List from the Web Server 

 Next 

 Enforce Policy on an External Dynamic List 

 View External Dynamic List Entries 

 View the contents of an external dynamic list to check if it contains certain IP
 addresses, domains, or URLs. 

 Where Can I Use
 This? What Do I Need? 

 NGFW (Cloud Managed) 

 NGFW (PAN-OS & Panorama Managed) 

 Prisma Access (Managed by Strata Cloud Manager) 

 Prisma Access (Managed by Panorama) 

 Check for any license or role requirements for the products you're using. 

 It's a good idea to look at your external dynamic list (EDL) entries to
 assess the information present in these lists. Viewing external dynamic list entries
 gives you insights into the threat intelligence being used for Security policy
 enforcement, and helps you maintain an up to date and robust security posture. 

 To access and view entries within an external dynamic list, navigate to the
 Objects tab and select External Dynamic
 Lists . Here, you can see a list of all configured external dynamic
 lists. Select a specific external dynamic list to view the entries it contains. 

 External dynamic list entries typically comprise IP addresses, URLs, domain
 names, or other indicators of compromise, depending on the type of external dynamic
 list configured. Your configuration periodically fetches updates from the specified
 URL associated with the external dynamic list, ensuring that the entries remain
 current and reflect the latest threat intelligence. 

 To delve deeper into the entries within an external dynamic list, you can
 review the contents directly from the external dynamic list configuration. This
 might involve inspecting the external dynamic list's source file, which you can
 access by clicking on the URL associated with the external dynamic list. The
 contents of the external dynamic list source file provide a comprehensive view of
 the listed indicators and their details. 

 Regular monitoring of these entries is vital to ensure the effectiveness of
 your configuration's threat prevention capabilities. Review the entries
 periodically, cross-reference them with known threat databases, and validate their
 relevance to your organization's security posture. 

 Before you Enforce Policy on an External
 Dynamic List , view the contents of an external dynamic list to check if
 it contains certain IP addresses, domains, or URLs. The entries displayed are based
 on the version of the external dynamic list that was most recently retrieved. 

 Follow these steps to view the contents of an external dynamic list to check if it
 contains certain IP addresses, domains, or URLs. 

 Strata Cloud Manager 

 PAN-OS & Panorama 

 View External Dynamic List Entries (Strata Cloud Manager) 

 View the contents of an external dynamic list to check if it contains certain IP
 addresses, domains, or URLs. 

 Select Configuration NGFW and Prisma Access Objects External Dynamic Lists . 

 Select the external dynamic list you want to view. 

 Check the List Entries and
 Exceptions and view the objects that were retrieved
 from the list. 

 The list might be empty if: 

 The EDL has not yet been applied to a Security rule. To apply
 an EDL to a Security rule and populate the EDL, see Enforce Policy on an External Dynamic List . 

 The external dynamic list has not yet been retrieved. To force the
 retrieval of an external dynamic list immediately, Retrieve an External Dynamic List from the Web
 Server . 

 Enter an IP address, domain, or URL (depending on the type of list) in the
 search field to check if it’s in the list. Exclude entries from an external
 dynamic list based on which IP addresses, domains, and URLs you need to block or
 allow. 

 Exclude Entries from an External Dynamic List 

 As you view the entries of an external dynamic list, you can exclude up to 100
 entries from the list. The ability to exclude entries from an external dynamic
 list gives you the option to enforce policy on some (but not all) of the entries
 in a list. This is helpful if you cannot edit the contents of an external
 dynamic list (such as the Palo Alto Networks High-Risk IP Addresses feed)
 because it comes from a third-party source. 

 Follow these steps to exclude entries from an external dynamic list to enforce
 policy on some (but not all) of the entries in a list. 

 View External Dynamic List
 Entries . 

 Select up to 100 entries to manually exclude from the list or manually add
 a list exception. 

 You cannot save your changes to the external dynamic list if you
 have duplicate entries in the Manual Exceptions list. To
 identify duplicate entries, look for entries with a red
 underline. 

 A manual exception must match a list entry exactly. Additionally,
 you cannot exclude a specific IP address from within an IP
 address range. To exclude a specific IP address from an IP
 address range, you must add each IP address in the range as a
 list entry and then exclude the desired IP address. 

 Exclusion of an individual IP address from an IP address range is
 not supported. 

 Save your changes. 

 ( Optional ) Enforce Policy on an
 External Dynamic List . 

 View External Dynamic List Entries (PAN-OS & Panorama) 

 View the contents of an external dynamic list directly on the firewall to check if it
 contains certain IP addresses, domains, or URLs. 

 Select Objects External Dynamic Lists . 

 Click the external dynamic list you want to view. 

 Click List Entries and Exceptions and view the objects
 that the firewall retrieved from the list. 

 The list might be empty if: 

 The EDL has not yet been applied to a Security rule. To apply
 an EDL to a Security rule and populate the EDL, see Enforce Policy on an External Dynamic List . 

 The firewall has not yet retrieved the external dynamic list. To
 force the firewall to retrieve an external dynamic list immediately,
 Retrieve an External Dynamic List from the Web
 Server . 

 The firewall is unable to access the server that hosts the external
 dynamic list. Click Test Source URL to verify
 that the firewall can connect to the server. 

 Enter an IP address, domain, or URL (depending on the type of list) in the
 filter field and Apply Filter ( 

 ) to
 check if it’s in the list. Exclude entries from an external dynamic list based
 on which IP addresses, domains, and URLs you need to block or allow. 

 Exclude Entries from an External Dynamic List 

 As you view the entries of an external dynamic list, you can exclude up to 100
 entries from the list. The ability to exclude entries from an external dynamic
 list gives you the option to enforce policy on some (but not all) of the entries
 in a list. This is helpful if you cannot edit the contents of an external
 dynamic list (such as the Palo Alto Networks High-Risk IP Addresses feed)
 because it comes from a third-party source. 

 Follow these steps to exclude entries from an external dynamic list to enforce
 policy on some (but not all) of the entries in a list. 

 View External Dynamic List
 Entries . 

 Select up to 100 entries to manually exclude from the list or manually add
 a list exception. 

 You cannot save your changes to the external dynamic list if you
 have duplicate entries in the Manual Exceptions list. To
 identify duplicate entries, look for entries with a red
 underline. 

 A manual exception must match a list entry exactly. Additionally,
 you cannot exclude a specific IP address from within an IP
 address range. To exclude a specific IP address from an IP
 address range, you must add each IP address in the range as a
 list entry and then exclude the desired IP address. 

 Exclusion of an individual IP address from an IP address range is
 not supported. 

 Save your changes. 

 ( Optional ) Enforce Policy on an
 External Dynamic List . 

 Previous 

 Retrieve an External Dynamic List from the Web Server 

 Next 

 Enforce Policy on an External Dynamic List 

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

 Security Policy 

 Prisma Access 

 Panorama 

 Strata Cloud Manager 

 Security Policy 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
