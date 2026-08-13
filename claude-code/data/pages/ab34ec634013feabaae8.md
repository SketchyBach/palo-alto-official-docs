---
url: https://docs.paloaltonetworks.com/strata-cloud-manager/new-features/by-date/strata-cloud-manager/february-2024#3cfaf63c8948ef3ae3c609248e1a70ad
fetched_at: 2026-08-13T17:38:24Z
source: palo-alto-main
---

# New Features - Strata Cloud Manager - February 2024 Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear

New Features - Strata Cloud Manager - February 2024 

 Home 

 EN

 Location 

 Documentation Home 

 Palo Alto Networks 

 Support 

 Live Community 

 Knowledge Base 

 Strata Copilot

 Filter

 Expand All 
 | 
 Collapse All 

 Strata Cloud Manager Docs 

 Activation & Onboarding 

 Subscription & Tenant Management 

 Getting Started 

 AIOps 

 Release Notes 

 New Features 

 Focus 

 Home 

 Strata Cloud Manager 

 New Features - Strata Cloud Manager - February 2024 

 AIOps for NGFW: DIMM Memory Failure Alert 

 Release Date: February 2024 
 | 
 Last Updated: June 2026 

 Introducing the DIMM Memory Failure alert that detects errors in the Dual In-Line Memory Module (DIMM) component within devices. The DIMM, a hardware component, stores, and accesses data in the firewall's Random Access Memory (RAM). This memory module influences the firewall's performance, allowing it to process network traffic rapidly and execute security tasks. The firewall's processes encounter issues accessing a specific memory location when an error related to this component occurs, indicating a memory failure.: 

 Supported on AIOps for NGFW Free and Strata Cloud Manager with AIOps for NGFW Premium license. 

 Strata Cloud Manager

 AIOPs

 February 2024

 AIOps for NGFW: Delayed Telemetry Alert 

 Release Date: February 2024 
 | 
 Last Updated: June 2026 

 Introducing the Delayed Telemetry alert, which actively identifies instances when Strata Cloud Manager detects a problem with receiving or processing telemetry from a device. If telemetry is missing for 6 hours, Strata Cloud Manager issues a medium severity alert. If this absence persists for more than 72 hours, Strata Cloud Manager elevates the alert severity to critical. 

 Upon the resumption of telemetry data processing, Strata Cloud Manager automatically closes the delayed telemetry alerts. If you remove a device, Strata Cloud Manager deletes all associated data, including delayed alerts. Additionally, Strata Cloud Manager displays an orange or red hourglass icon next to hostnames, providing quick visual cues to identify devices with potential telemetry issues. 

 Supported on AIOps for NGFW Free and Strata Cloud Manager with AIOps for NGFW Premium license. 

 Strata Cloud Manager

 AIOPs

 February 2024

 AIOps for NGFW: Logging Drive Failure Alert 

 Release Date: February 2024 
 | 
 Last Updated: June 2026 

 Introducing the Logging Drive Failure alert that detects a failure in the logging drive by monitoring the firewall's disk status. This failure in the drive could potentially result in data loss, impair logging and monitoring capabilities, and activate a failover in the case of a high availability (HA) pair. 

 Supported on AIOps for NGFW Free and Strata Cloud Manager with AIOps for NGFW Premium license. 

 Strata Cloud Manager

 AIOPs

 February 2024

 Configuration Snippet Cloning 

 Release Date: February 2024 
 | 
 Last Updated: May 2026 

 When you need to create similar configuration snippets with slight variations, manually rebuilding each snippet from scratch wastes valuable time and increases the risk of configuration errors. This challenge becomes particularly frustrating when you want to use an existing snippet as a foundation for new deployments or when adapting proven configurations for different network segments. 

 You can now clone existing snippets in Strata Cloud Manager , allowing you to use any preexisting snippet as a template for new configurations. This cloning capability eliminates the need to configure completely new objects when you want to create variations of existing snippets. 

 Snippets are configuration objects, or groups of configuration objects, that you can associate with your folders, firewalls, and Prisma® Access deployments onboarded to Strata Cloud Manager. You use them to standardize configurations, enabling you to push changes quickly to multiple areas simultaneously. Snippets help you manage common configurations centrally for consistent security enforcement across NGFW and Prisma Access deployments. 

 Snippets are classified in two ways: Predefined and Custom. Predefined snippets are available to all Strata Cloud Manager users and help you quickly get your new firewalls and deployments up and running with best practice configurations. Custom snippets are any snippets that administrators create. 

 When you clone a snippet, the system creates an independent copy that is not associated with any devices, folders, or deployments. This allows you to customize the cloned snippet freely without having to disassociate it from existing resources before you begin making modifications. 

 Strata Cloud Manager

 Management

 February 2024

 Strata Cloud Manager

 Management

 February 2024

 GlobalProtect Portal and Gateway for Cloud Managed NGFWs 

 Release Date: February 2024 
 | 
 Last Updated: May 2026 

 Use GlobalProtect 
 Whether checking email from home or updating corporate documents from an airport, the majority of today's employees work outside the physical corporate boundaries. This workforce mobility increases productivity and flexibility while simultaneously introducing significant security risks. Every time users leave the building with their laptops or smart phones, they are bypassing the corporate firewall and associated policies that are designed to protect both the user and the network. GlobalProtect ® solves the security challenges introduced by roaming users by extending the network security policy that you're enforcing within the physical perimeter to all users, no matter where they are located. 

 You can now use GlobalProtect with cloud-managed NGFWs to secure your mobile workforce. Enable your cloud-managed NGFWs as GlobalProtect gateways and portals, in order to provide flexible, secure remote access to users everywhere. 

 GlobalProtect

 February 2024

 Strata Cloud Manager

 Management

 February 2024

 Strata Cloud Manager

 Management

 February 2024

 New Prisma Access Cloud Management Location 

 Release Date: February 2024 
 | 
 Last Updated: May 2026 

 Prisma Access Cloud Management can now be deployed in the India region . 

 Prisma Access

 February 2024

 6.0 Preferred and Innovation

 Strata Cloud Manager

 Management

 February 2024

 Strata Cloud Manager

 Management

 February 2024

 Policy Analyzer 

 Release Date: February 2024 
 | 
 Last Updated: May 2026 

 Time-sensitive security policy changes carry the high risk of introducing errors, misconfigurations, or conflicts into the rulebase, requiring slow and complex manual audit processes. Policy integrity is difficult to maintain at scale, leading to decreased performance and potential security gaps. Strata Cloud Manager introduces Policy Analyzer, enabling administrators to optimize time and resources when implementing any change request. Policy Analyzer provides immediate, automated analysis of the security rulebase to ensure policy updates meet defined intent and technical requirements. It proactively checks for anomalies, such as Shadows, Redundancies, Generalizations, Correlations, and Consolidations, that otherwise require labor-intensive manual checking. By identifying conflicting or duplicate rules before deployment, Policy Analyzer streamlines change management, reduces the risk of misconfiguration, and ensures the continued performance and integrity of your network security posture. 

 Strata Cloud Manager

 Management

 February 2024

 Strata Cloud Manager

 Management

 February 2024

 Private Key Export in Certificate Management 

 Release Date: February 2024 
 | 
 Last Updated: May 2026 

 You can centrally manage the certificates you use to secure communication across your network. 

 You can now export the private key from Strata Cloud Manager for a self-signed certificate. However, the export of private keys for an externally signed certificate is restricted. The supported export formats are as follows: 

 Base64 Encoded Certificate (PEM) —This is the default format. It's the most common and has the broadest support on the internet. Export Private Key if you want the exported file to include the private key. 

 Encrypted Private Key and Certificate (PKCS12) —This format is more secure than PEM but isn't as common or as broadly supported. The exported file will automatically include the private key. 

 Binary Encoded Certificate (DER) —More operating system types support this format than the others. You can't export the private key in this format. 

 Strata Cloud Manager

 Management

 February 2024

 Strata Cloud Manager

 Management

 February 2024

 Security Checks 

 Release Date: February 2024 
 | 
 Last Updated: May 2026 

 Security administrators rely on predefined best practice checks that align with industry standards, such as CIS (Center for Internet Security) and NIST (National Institute of Standards and Technology). However, the rigidity of applying these checks globally often forces you to manually bypass or ignore critical security findings for specific operational exceptions, risking compliance and increasing administrative overhead. 

 Strata Cloud Manager now addresses this by supporting real-time inline check exemptions. Exemptions allow you to restrict where security checks are applied within your deployment, rather than requiring you to disable the checks entirely. This capability ensures you maintain a robust global security posture while flexibly accommodating specific organizational needs. Additionally, essential check information is now delivered in a consolidated, contextual view, simplifying your configuration evaluation workflow and allowing you to balance security enforcement with operational efficiency. 

 Strata Cloud Manager

 AIOPs

 February 2024

 Strata Cloud Manager

 Management

 February 2024

 Traceability and Control of Post-Quantum Cryptography in Decryption 

 Release Date: February 2024 
 | 
 Last Updated: May 2026 

 Today, post-quantum cryptography (PQC) algorithms and hybrid PQC algorithms (classical and PQC algorithms combined) are accessible through open-source libraries and integrated into web browsers and other technologies. Traffic encrypted by PQC or hybrid PQC algorithms cannot be decrypted yet, making these algorithms vulnerable to misuse. To address these concerns, Palo Alto Networks firewalls now detect, block, and log the use of PQC and hybrid PQC algorithms in TLSv1.3 sessions. 

 Your decryption policy rules determine if the firewall detects, blocks, and logs PQC and hybrid PQC algorithms. If SSL/TLS traffic matches an SSL Forward Proxy or SSL Inbound Inspection decryption policy rule, the firewall prevents negotiation with PQC, hybrid PQC, and other unsupported algorithms. Specifically, the firewall removes these algorithms from the ClientHello, forcing the client to negotiate with classical algorithms. This enables continuous decryption and threat identification through deep packet inspection. If the client strictly negotiates PQC or hybrid PQC algorithms, the firewall drops the session. The decryption log entry for dropped sessions shows the error message: "client only supports post-quantum algorithms”. 

 If SSL/TLS traffic matches a “no-decrypt” decryption policy rule or does not match any decryption policy rules, the firewall allows the negotiation of PQC or hybrid PQC algorithms. In these cases, the firewall generates a decryption log only if the traffic matches a "no-decrypt" decryption policy rule. 

 Additionally, new threat signatures offer visibility into the use of PQC and hybrid PQC algorithms in your network. These signatures monitor ServerHello responses and alert you when PQC-based SSL/TLS sessions are successfully negotiated. A Threat Prevention license is required to receive alerts. 

 PAN-OS

 February 2024

 11.1

 Strata Cloud Manager

 Management

 February 2024

 Strata Cloud Manager

 Network Visibility

 February 2024

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

 Experts Corner 

 Solutions Docs from Product Experts 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
