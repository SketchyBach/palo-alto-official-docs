---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam-rn/cortex-xsiam-release-information/features-introduced-in-2025-xsiam/july-2025/feature-enhancements
fetched_at: 2026-09-06T10:52:45Z
source: cortex-platform
---

# Feature Enhancements | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Release Notes 

 Cortex XSIAM 

 Cortex XSIAM 

 Cortex XSIAM Release Information 

 Features Introduced in 2025 

 July 2025 

 Feature Enhancements 

 The Cortex XSIAM 3.2 release includes the following enhancements: 

 General 

 Feature 

 Description 

 Export filter JSON from the UI to ease writing API calls 

 Cortex public APIs require a proprietary JSON filter object for filtering assets, asset groups, policies, and other entities. To simplify API integration, you can now define your desired filter directly in the UI and export the exact JSON object for use in your API calls. This saves time and streamlines development. 

 Vulnerability Management Dashboard Enhancements 

 Reduce risks faster with actionable intelligence and new visualizations on the Vulnerability Management dashboard. Enhancements include filtering by asset group, a new widget for emerging vulnerabilities, and count of open issues by duration. 

 Investigation and response 

 Feature 

 Description 

 Cortex Command center updates 

 (Requires the Cortex XSIAM Premium license) 

 The latest Cortex Command Center updates enhance your ability to achieve comprehensive visibility across your cloud and enterprise assets. You can now: 

 Monitor data ingestion over the last 24 hours. 

 View open issues by asset class or provider to identify patterns and prioritize response. 

 Monitor the number of assets protected by the Cortex Agent to ensure complete coverage. 

 ITDR Issues and Insights Navigation 

 A new navigation entry for ITDR Issues and Insights enables you to quickly review all ITDR-related issues, including INFO, at a glance, with filtering, sorting, and other options. 

 Unified Identity Inventory 

 A unified inventory for identities features dedicated sections for investigating each domain: cloud, enterprise, and code. 

 Graph Search 

 Feature 

 Enhancement 

 Graph Search enhancements (Beta) 

 (Requires the Cortex XSIAM Premium license or the Cortex Cloud Posture Management add-on) 

 Graph Search now enables customers to: 

 Investigate real-time activity and identify critical events, such as access to sensitive information typically contained in a Storage Bucket, which generate issues and cases. This is now possible by the 100 most recent runtime events added to the graph results. 

 Track assets with internet exposure that could be targeted for external surface attacks, and the exposure path is also available. 

 Detection rules 

 Feature 

 Description 

 New and improved Analytics tags 

 New analytics suites: 

 EDR Windows C2 Analytics: An innovative analytics detection suite that provides visibility into C2 and exfiltration traffic using our novel approach that fuses EDR process context and network-based features. This approach uncovers a broad range of attacks, from overt malicious communications to those involving seemingly benign implants or remote hosts. 

 EDR Linux Shell Analytics: A new, advanced Analytics-based generic detection suite that detects abnormal Linux shell executions, surfacing unknown exploits, stealthy backdoors, and post-exploitation activities. It also highlights attacker tools and powerful system commands run in unfamiliar contexts. 

 EDR MacOS Shell Analytics: A novel analytics-based detection suite tailored to the macOS domain that detects unusual spawned macOS shells. It uncovers unknown exploits, stealthy backdoors, and the uncommon AppleScript and information-gathering activities commonly leveraged by macOS infostealers. 

 Improved analytics tags: 

 NDR Lateral Movement Analytics: Upgrade to our network-based lateral movement detection suite, focusing on richer application logging for deeper protocol-based context. The suite's enhanced behavior-based analytics now provide earlier, more precise lateral movement detection, including SSH and improved Windows-native protocols. 

 EDR macOS AppleScript Analytics: Expanding our AppleScript attacks coverage by introducing visibility into module events.This enhancement extends our detection of suspicious AppleScript executions to trigger alerts also on executables loading AppleScript dynamic libraries (dylibs) for potential malicious use. 

 External Data Ingestion and Management 

 Feature 

 Description 

 OCI support 

 Gain visibility, compliance, and governance over assets and configurations in Oracle Cloud Infrastructure (OCI) environments. 

 VNET flow log support for Azure Network Watcher 

 Azure Network Watcher now supports VNET flow logs. 

 XDR Collectors 

 XDR Collectors 1.5.0: Windows 1.5.0.1733 and Linux 1.5.0.1695 

 XDR Collectors 1.4.3: Windows 1.4.3.1686 

 For more information on maintenance releases, see Maintenance releases 

 Feature 

 Description 

 XDR Collectors 1.5.0 and 1.4.3 

 This release includes performance improvements and bug fixes. 

 Broker VM 

 Version 28.0.96 (reboot required) 

 For more information on maintenance releases, see Maintenance releases 

 Deprecation of Broker VM Pathfinder applet 

 The Broker VM Pathfinder applet is now deprecated. 

 From this release, the Pathfinder applet can no longer be activated in new tenants or existing tenants that have never implemented this applet before. 

 If this applet has been implemented in your tenant, it will remain available until January 25, 2026, which is the official deprecation date. To ensure complete coverage and protection, we recommend deploying XDR Agents on all endpoints by this date. 

 Migration guidance and deployment resources for XDR Agents are available here . 

 For questions or transition support, contact your Customer Support team . 

 Feature 

 Description 

 New Network Scanner Broker VM applet 

 (Requires the Cortex XSIAM Premium, Cortex XSIAM Enterprise, or Cortex XSIAM NG-SIEM license) 

 Cortex Network Scanner is a powerful tool for internal network security. It efficiently identifies assets and assesses vulnerabilities using a variety of techniques, including remote and authenticated local checks. 

 Broker VM applet configurations preserved when deactivated 

 Cortex XSIAM now provides the ability to maintain the Broker VM applet configurations whenever an applet is deactivated. This ensures that whenever the applet is reactivated the saved configuration is restored. 

 Enhanced error visibility and auditing for additional Broker VM applets 

 Gain better insight into application, connectivity, and processing errors for the File and DB collector applets running on Broker VMs. Error messages are displayed on Apps of Broker VMs and Clusters, and applet status changes are logged in the collection_auditing dataset, enabling detailed investigations through XQL queries. 

 Broker VM applets license enforcement 

 License enforcement for the Broker VM applets has been enhanced to ensure that only applets aligned with the purchased product and licensed capabilities are available for activation and use. 

 Cortex Query Language (XQL) 

 Feature 

 Description 

 New XQL IP functions 

 Cortex Query Language (XQL) now supports new functions for IP manipulations. These functions verify whether an input is a valid IPv4/IPv6 address and if the IPv4/IPv6 address is a known private IP. 

 Automations 

 Feature 

 Description 

 Streamlined cloud automation configuration 

 (Requires a Cortex XSIAM Premium, Cortex XSIAM Enterprise, or Cortex XSIAM NG SIEM license) 

 Simplify adopting cloud automation capabilities by integrating automation instance management directly into the cloud onboarding process for AWS, GCP, and Azure. Now, all automation setup configurations are integrated into Terraform, providing seamless enablement and visibility into instance health. 

 Automation Exclusion Center 

 Configure centralized automation exclusion policies to define which assets, such as users and endpoints, should be excluded from automated remediation. Use these policies to protect critical assets and ensure remediation actions are applied only to assets that are not explicitly excluded. 

 Automation menu navigation improvement 

 The Automation Rules menu item has been moved from Case Configuration to the Automation section of the main navigation, providing a streamlined user experience for automation configuration. 

 API 

 Feature 

 Description 

 Cases and Issues public APIs 

 (Requires a Cortex XSIAM Premium, Cortex XSIAM Enterprise, or Cortex XSIAM NG SIEM license) 

 New public APIs are now available for managing cases and issues, providing capabilities to list and update cases, access related issues, assets, and artifacts, and to list, update, and create issues. This enables you to streamline and automate operations externally. 

 Create Distributions API now supports Kubernetes installations 

 (Requires a Cortex XSIAM Premium, or Cortex XSIAM Enterprise license) 

 The Create Distributions API now supports Kubernetes installations, helping you automate and streamline the deployment of the agent in Kubernetes environments. 

 Identity Security Access Table Data API 

 Facilitate advanced integrations, reporting, and analytics with the introduction of the CIEM Access Table Data API. It enables the retrieval of detailed access information using filters, with access details similar to the UI. 

 Unified Asset Inventory APIs 

 Gain comprehensive API access to all your on-premises and cloud asset information. We've introduced new APIs for retrieving asset data from the Unified Asset Inventory, complete with powerful filtering capabilities. This provides flexible and precise access to your asset data. 

 APIs for managing API keys 

 Gain more granular control and efficiency over your API keys. We've introduced new public API endpoints to get, create, and delete API keys, including the ability to delete API keys in bulk. This streamlines key management and enhances your security posture. 

 Streamlined automation with new Application Security APIs 

 (Requires a Cortex XSIAM Premium license) 

 Enhance your security operations and automation using our new Application Security public APIs. They allow for the programmatic management of data sources, rules, policies, and scans, helping you optimize and streamline your application security workflows. 

 API Security 

 Feature 

 Description 

 Cortex API security enhancements 

 Cortex API security is enhanced with the following new capabilities: 

 Boost your security and get a clearer picture of your API landscape with enhanced security scanning. By classifying API endpoints and their sub-types (like login, and checkout), you'll better understand each API's scope and sensitivity. This deeper insight paves the way for better detection of future threats and vulnerabilities, all while optimizing sensitive data protection. 

 Beyond just observing live traffic, Cortex Cloud can automatically identify and extract API specifications from your AWS and Azure API gateway, proactively scanning them for misconfigurations and vulnerabilities, which gives you a more complete and secure inventory of all your API endpoints. Cortex also creates API endpoints from the specifications, which enables Cortex to uncover shadow APIs. 

 Security coverage expands with the new integration option, F5 BIG-IP LTM. 

 For better risk assessment and more effective remediation, Cortex expands its API security visibility by showing the gateways, workloads, and specifications related to the same endpoints, giving you a broader context of the API endpoint. 

 Deep insights into the data profiles and patterns observed in your API endpoints' traffic can now be achieved with the integration of DSPM's unified, cross-platform data sensitivity scanning engine. 

 Attack Surface Management 

 Requires the ASM add-on. 

 Feature 

 Description 

 Emerging Vulnerabilities 

 The Emerging Vulnerabilities is a curated list of emergent and global threat events. Powered by a dedicated team of security researchers, it consolidates detailed, crucial information about each threat and the potential impact on your organization. The Emerging Vulnerabilities page enables you to research emerging vulnerabilities, assess the impact, and build a remediation plan—all in one place. 

 Global Lookup 

 Global Lookup enables you to enter any IP address or domain and view 7 days of internet scan data, including registration information, related certificates, services seen, and more. Global Lookup is available directly in the product, eliminating the need to use external tools, to enable faster investigations and provide clarity on indicator ownership. 

 New post-compromise detections 

 Expand detection coverage for Ransomware activity, Cryptojacking, and Webshells to deliver an additional layer of defense and identify ongoing attacks and potential lateral movement by attackers. 

 Dynamic Protocol Detection for 65k Ports 

 Now all 65k IPv4 ports will undergo dynamic port protocol detection, resulting in improved service discovery. This will be released by the end of July for all customers. 

 New Attack Surface Rules 

 (Requires a Cortex XSIAM Premium, Cortex XSIAM Enterprise, or Cortex XSIAM NG SIEM license) 

 New Attack Surface Rules identify internet-facing applications that leak full or partial credential information. 

 IPv6 Support for ASM in Cortex XSIAM 

 (Requires a Cortex XSIAM Premium, Cortex XSIAM Enterprise, or Cortex XSIAM NG SIEM license) 

 ASM in Cortex XSIAM now supports IPv6, expanding your ability to discover and protect your attack surface. This enhancement means IPv6 services will generate findings and issues, and IPv6 assets will be included in your inventory. 

 Digital Risk Protection 

 Brand risk support is now available for ASM. There are two new attack surface rules to enable leaked credential and brand risk domain discovery. 

 Gateway 

 Feature 

 Description 

 Improved user record management 

 Only users with at least one role or user group assigned are saved to Cortex Gateway, ensuring that the Gateway contains only relevant user data. This enhances data security and system efficiency. 

 Cloud Runtime Security 

 Feature 

 Description 

 Container Registry Scanning via Broker VM 

 (Requires a Cortex XSIAM Premium, Cortex XSIAM Enterprise, or Cortex XSIAM NG SIEM license) 

 Securely scan self-hosted container registries in on-prem or private clouds without exposing them to external access. 

 Previous Release Highlights 

 Next Changed features 

 Last updated 16 days ago 

 Was this helpful?
