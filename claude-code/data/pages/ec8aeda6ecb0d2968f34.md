---
url: https://docs.paloaltonetworks.com/network-security/security-policy/administration/objects/external-dynamic-lists/enforce-policy-on-an-external-dynamic-list
fetched_at: 2026-08-13T16:38:30Z
source: palo-alto-main
---

# Enforce Policy on an External Dynamic List Clear

Enforce Policy on an External Dynamic List 

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

 Enforce Policy on an External Dynamic List 

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

 Enforce Policy on an External Dynamic List 

 Download PDF 

 Network Security 

 Enforce Policy on an External Dynamic List 

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

 View External Dynamic List Entries 

 Next 

 Find External Dynamic Lists That Failed Authentication 

 Enforce Policy on an External Dynamic List 

 Learn how to block or allow traffic based on IP addresses or URLs in an external
 dynamic list, or use a dynamic domain list with a DNS sinkhole to prevent access to
 malicious domains. 

 Where Can I Use
 This? What Do I Need? 

 NGFW (Cloud Managed) 

 NGFW (PAN-OS & Panorama Managed) 

 Prisma Access (Managed by Strata Cloud Manager) 

 Prisma Access (Managed by Panorama) 

 Check for any license or role requirements for the products you're using. 

 External Dynamic Lists allow you to dynamically update security rules based on real-time threat intelligence obtained from external sources. This
 dynamic integration ensures that your configuration remains updated with the latest
 threat indicators, allowing for a proactive and effective response to emerging
 cyberthreats. 

 To get started, you'll need to configure and external dynamic list. This
 involves providing essential information such as the external dynamic list's URL,
 type (IPv4, IPv6, domain, etc.), and any necessary authentication credentials. Your
 configuration regularly fetches and updates this information to stay current with
 the evolving threat landscape. 

 Once you've configured your external dynamic list, you can integrate it
 into your security rules. Your configuration references your external dynamic
 list in relevant rule conditions, and uses the external threat indicators to match
 traffic. For example, an external dynamic list containing malicious IP addresses can
 be referenced in a security rule to block traffic originating from or
 destined to those addresses. 

 It’s important for your configuration to be able to dynamically update and
 enforce security rules based on the contents of the external dynamic list.
 This ability significantly enhances your configuration's efficacy in detecting and
 preventing potential threats by applying up to date threat intelligence from trusted
 sources. 

 Regular monitoring and maintenance are crucial aspects of this process.
 Routinely review the external dynamic list configuration, validate its accuracy and
 relevance, and fine-tune security rules based on the intelligence gathered.
 Adjustments might include modifying rules to block or allow traffic based on the
 latest threat indicators or updating the external dynamic list to align with
 changing security needs. 

 Leveraging an external dynamic list to enforce Security policy represents a
 proactive and agile approach to cybersecurity. It allows you to adapt swiftly to
 evolving threats, fortifying your network defenses and ensuring a robust security
 posture. 

 Follow these steps to block or allow traffic based on IP addresses or URLs in an
 external dynamic list, or use a dynamic domain list with a DNS sinkhole to prevent
 access to malicious domains. 

 Strata Cloud Manager 

 PAN-OS & Panorama 

 Enforce Policy on an External Dynamic List (Strata Cloud Manager) 

 Block or allow traffic based on IP addresses or URLs in an external dynamic list, or
 use a dynamic domain list with a DNS sinkhole to prevent access to malicious domains. 

 Block or allow traffic based on IP addresses or URLs in an external dynamic list, or
 use a dynamic domain list with a DNS sinkhole to prevent access to malicious
 domains. 

 Tips for enforcing policy with external dynamic lists: 

 Search for a domain, IP address, or URL that belongs to one or more external
 dynamic lists is used in policy. This is useful for determining which
 external dynamic list (referenced in a Security rule) is causing a certain
 domain, IP address, or URL to be blocked or allowed. 

 Configure DNS sinkholing for a custom list of
 domains . 

 Use an External Dynamic List in a URL
 Filtering Profile . 

 Use an External Dynamic List of Type URL as Match Criteria in a Security
 Security Rule. 

 Select Configuration NGFW and Prisma Access Security Services Security Policy . 

 Select Add Rule and enter a descriptive
 Name for the rule. 

 In SOURCE , select a
 Zone . 

 In DESTINATION , select a
 Zone . 

 In URL CATEGORY / TENANT RESTRICTION , select the
 appropriate external dynamic list from the URL Category list. 

 In Actions , set the
 Action setting to
 Allow or Deny . 

 Select Save . 

 Verify whether entries in the external dynamic list were ignored or
 skipped. 

 Test that the policy action is enforced. 

 View External Dynamic List
 Entries for the URL list, and attempt to access a
 URL from the list. 

 Verify that the action you defined is enforced. 

 Monitor activity. Select Incidents & Alerts Log Viewer Firewall/URL to access the detailed log view. 

 Use an IP External Dynamic List or Predefined IP External Dynamic List as a
 Source or Destination Address Object in a Security Rule. 

 This capability is useful if you deploy new servers and want to allow access
 to the newly deployed servers without requiring a commit. 

 Select Configuration NGFW and Prisma Access Security Services Security Policy . 

 Select Add Rule and give the rule a descriptive
 Name . 

 In SOURCE and
 DESTINATION , set the external dynamic list to be
 used as the SOURCE and
 DESTINATION addresses. 

 In APPLICATION / SERVICE , make sure the
 Service is set to Application
 Default . 

 In Actions set the Action
 setting to Allow or
 Deny . 

 Create separate external dynamic lists if you want to specify
 allow and deny actions for specific IP addresses. 

 Leave all the other options at the default values. 

 Select Save to save the changes. 

 Test that the policy action is enforced. 

 View External Dynamic List
 Entries for the external dynamic list, and
 attempt to access an IP address from the list. 

 Verify that the action you defined is enforced. 

 Select Incidents & Alerts Log Viewer Firewall/Traffic and view the log entry for the session. 

 Use a Predefined URL External Dynamic List to exclude benign domains that
 applications use for background traffic from Authentication policy.

 When you select the panw-auth-portal-exclude-list EDL
 type, you can easily exclude from Authentication policy enforcement the domains
 that many applications use for background traffic, such as updates and other
 trusted services. This ensures that the necessary traffic for these services is
 not blocked and application maintenance is not interrupted. 

 Select Configuration NGFW and Prisma Access Identity Services Authentication Authentication Rules Add Rule . 

 In Services and URLs , select the Predefined URL
 EDL as the URL Category . 

 In Action , select Do Not
 Authenticate . 

 Select Save . 

 Move the rule to the top so that it's the first
 rule in the policy. 

 Enforce Policy on an External Dynamic List (PAN-OS & Panorama) 

 Learn how to block or allow traffic based on IP addresses or URLs in an external
 dynamic list, or use a dynamic domain list with a DNS sinkhole to prevent access to
 malicious domains. 

 Block or allow traffic based on IP addresses or URLs in an external dynamic list, or
 use a dynamic domain list with a DNS sinkhole to prevent access to malicious
 domains. 

 Tips for enforcing policy on the firewall with external dynamic lists: 

 When viewing external dynamic lists on the firewall ( Objects External Dynamic Lists ), click List Capacities to compare how
 many IP addresses, domains, and URLs are currently used in policy with the
 total number of entries that the firewall supports for each list type. 

 Use Global Find to Search the Firewall or
 Panorama Management Server for a domain, IP address, or URL that
 belongs to one or more external dynamic lists is used in policy. This is
 useful for determining which external dynamic list (referenced in a Security
 policy rule) is causing the firewall to block or allow a certain domain, IP
 address, or URL. 

 Use the directional controls at the bottom of the page to change the
 evaluation order of EDLs. This allows you to or order the lists to make
 sure the most important entries in an EDL are committed before capacity
 limits are reached. 

 You can only change the EDL order when Group By
 Type is deselected. 

 Configure DNS sinkholing for a custom list of
 domains . 

 Use an External Dynamic List in a URL
 Filtering Profile . 

 Use an External Dynamic List of Type URL as Match Criteria in a Security
 Security Rule. 

 Select Policies Security . 

 Click Add and enter a descriptive
 Name for the rule. 

 In the Source tab, select the Source
 Zone . 

 In the Destination tab, select the
 Destination Zone . 

 In the Service/URL Category tab, click
 Add to select the appropriate external
 dynamic list from the URL Category list. 

 In the Actions tab, set the Action
 Setting to Allow or
 Deny . 

 Click OK and
 Commit . 

 Verify whether entries in the external dynamic list were ignored or
 skipped. 

 Use the following CLI command on a firewall to review the details for
 a list. 

 request
system external-list show type <domain | ip | url> name_of_list 

 For example: 

 request system
external-list show type url EBL_ISAC_Alert_List 

 Test that the policy action is enforced. 

 View External Dynamic List
 Entries for the URL list, and attempt to access a
 URL from the list. 

 Verify that the action you defined is enforced. 

 To monitor the activity on the firewall: 

 Select ACC and add a URL
 Domain as a global filter to view the Network
 Activity and Blocked Activity for the URL you
 accessed. 

 Select Monitor Logs URL Filtering to access the detailed log view. 

 Use an IP External Dynamic List or Predefined IP External Dynamic List as a
 Source or Destination Address Object in a Security Rule. 

 This capability is useful if you deploy new servers and want to allow access
 to the newly deployed servers without requiring a firewall commit. 

 Select Policies Security . 

 Click Add and give the rule a descriptive
 Name . 

 In the Source/Destination tabs, set the external
 dynamic list to be used as the Source/Destination
 Address (es). 

 In the Service/ URL Category tab, make sure the
 Service is set to
 application-default . 

 In the Actions tab, set the Action Setting to
 Allow or Deny . 

 Create separate external dynamic lists if you want to specify
 allow and deny actions for specific IP addresses. 

 Leave all the other options at the default values. 

 Click OK to save the changes. 

 Commit the changes. 

 Test that the policy action is enforced. 

 View External Dynamic List
 Entries for the external dynamic list, and
 attempt to access an IP address from the list. 

 Verify that the action you defined is enforced. 

 Select Monitor Logs Traffic and view the log entry for the session. 

 To verify the security rule that matches a flow, select Device Troubleshooting , and execute a Security Policy Match
 test: 

 Use a Predefined URL External Dynamic List to exclude benign domains that
 applications use for background traffic from Authentication policy.

 When you select the panw-auth-portal-exclude-list EDL
 type, you can easily exclude from Authentication policy enforcement the domains
 that many applications use for background traffic, such as updates and other
 trusted services. This ensures that the firewall does not block the necessary
 traffic for these services and application maintenance is not interrupted. 

 Select Policies Authentication . 

 On the Service/URL Category tab, select the
 Predefined URL EDL as the URL Category . 

 On the Actions tab, select
 default-no-captive-portal as the
 Authentication Enforcement . 

 Click OK . 

 Move the rule to the top so that it's the first
 rule in the policy. 

 Commit your changes. 

 Previous 

 View External Dynamic List Entries 

 Next 

 Find External Dynamic Lists That Failed Authentication 

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
