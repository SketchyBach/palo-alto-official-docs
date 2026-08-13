---
url: https://docs.paloaltonetworks.com/iot/administration/detect-iot-device-vulnerabilities/virtual-patching-overview
fetched_at: 2026-08-13T16:36:16Z
source: palo-alto-main
---

# Virtual Patching with Device Security Clear

Virtual Patching with Device Security 

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

 Virtual Patching with Device Security 

 Updated on 

 Jul 30, 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Device Security Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Enterprise Administration 

 Integrations 

 Release Notes 

 Best Practice 

 New Features 

 Updated on 

 Jul 30, 2026 

 Focus 

 Home 

 Device Security 

 Device Security Administration Guide 

 IoT Device Vulnerability Detection 

 Virtual Patching with Device Security 

 Download PDF 

 Device Security 

 Virtual Patching with Device Security 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Device Security Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Enterprise Administration 

 Integrations 

 Release Notes 

 Best Practice 

 New Features 

 Previous 

 Create Compensating Controls 

 Next 

 Apply a Virtual Patch to Risky Assets 

 Virtual Patching with Device Security 

 Virtual patching provides network-level protection for OT and 
 IoT devices that cannot be easily patched due to operational 
 constraints.

 Where Can I Use This? What Do I Need? 

 Device Security (Managed by Strata Cloud Manager) 

 One of the following subscriptions: 

 Device Security subscription

 Precision AI bundle subscription

 Device Security X subscription

 Virtual patching provides the capability to mitigate risks in OT 
 and IoT environments where operational constraints make it 
 difficult to patch devices. With virtual patching, you can deploy 
 network-level protections through your next-generation firewall 
 rather than applying patches directly to the vulnerable devices. 
 Virtual patching maps CVEs to existing threat signatures. From 
 there, you can review the vulnerability and create security 
 policies that block malicious traffic targeting the 
 vulnerability.

 Some OT and IoT environments face significant patching challenges 
 due to a variety of factors. Legacy systems often lack vendor 
 support for updates, critical infrastructure requires extended 
 maintenance windows that conflict with security timelines, long 
 operating periods extend the time between maintenance windows, or 
 updates may require long recertification cycles. Virtual patching 
 addresses these issues by providing the ability to prevent the 
 exploitation of vulnerabilities at the network level.

 Virtual patching integrates asset discovery, risk assessment, and 
 automated policy deployment features within Device Security . 
 You can identify vulnerable devices, assess their risk levels, and 
 receive guided recommendations for deploying compensating controls. 
 Device Security verifies that appropriate threat signatures 
 exist for specific vulnerabilities and helps you create 
 least-privilege security policies with vulnerability protection 
 profiles. When you deploy these policies, you can extend the 
 operational life of legacy systems while meeting regulatory 
 compliance that requires documented risk mitigations.

 To use Virtual Patching effectively in Strata Cloud Manager , you 
 need NGFW deployments with the latest Advanced Threat Protection 
 version, a Device Security license, and Strata Cloud Manager 
 for policy management.

 When using Panorama for NGFW management, you can do Virtual Patching by attaching
 the Vulnerability Protection Profile to the 
 Security policy rules in Panorama. In this case, 
 Device Security provides asset visibility, vulnerability 
 identification, and threat signature mapping, while Panorama 
 provides the policy management and enforcement 
 capabilities.

 View the Virtual Patching Vulnerability Information 

 In Device Security in Strata Cloud Manager , you can see 
 which vulnerabilities have virtual patching options available 
 on the Assets Inventory page. In the 
 top section, click View More in the 
 Risk Score widget to expand the list of Top Priority 
 Vulnerabilities identified in your network. This list adjusts 
 as you drill down into particular device types and 
 categories.

 Each identified vulnerability in the list represents the impact 
 of that vulnerability on a particular device profile. The same 
 vulnerability may appear multiple times with a different 
 number of impacted assets if the vulnerability affects 
 multiple device profiles.

 For each top priority vulnerability, a chip next to the CVE ID 
 indicates if the vulnerability has a 
 Threat Signature 
 available, a patch identified, or both. Clicking on a 
 vulnerability displays details about it:

 Summary – A short description of 
 the vulnerability, with a link to the 
 Vulnerability Details page .

 Mitigate the vulnerability risk – 
 Recommendations to mitigate the vulnerability risk. This 
 can include patch information, if available, virtual 
 patching when a threat signature can be used, or 
 recommendations to reduce the attack surface via 
 zero-trust Security policies rules if no patch or threat 
 signature is available.

 Identified Risky Assets – A table 
 of the risky assets impacted by the vulnerability.

 The Identified Risky Assets table lets you see all impacted 
 devices that share the same profile. The table only includes 
 critical, high, and medium risk devices. Use the table to help 
 determine how widespread a vulnerability is, and how virtual 
 patching may reduce the risk score for individual devices as 
 well as for the device profile.

 Previous 

 Create Compensating Controls 

 Next 

 Apply a Virtual Patch to Risky Assets 

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

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 Service Provider 

 VM-Series 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 Device Security 

 Administration 

 Cloud-Delivered Security Services 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
