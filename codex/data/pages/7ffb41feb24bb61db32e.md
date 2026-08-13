---
url: https://docs.paloaltonetworks.com/globalprotect/new-features/by-version/globalprotect/6-2#a6d4af51899698812b1b52e1a13ab0d5
fetched_at: 2026-08-13T16:32:57Z
source: palo-alto-main
---

# New Features - GlobalProtect - 6.2 Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear Clear

New Features - GlobalProtect - 6.2 

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

 GlobalProtect Docs 

 Getting Started 

 Activation & Onboarding 

 Administration 

 User Guide 

 Select a Document 

 6.3 

 6.2 

 6.1 

 6.0 

 Release Notes 

 Select a Document 

 6.3 

 6.2 

 6.1 

 6.0 

 New Features 

 Focus 

 Home 

 GlobalProtect 

 New Features - GlobalProtect - 6.2 

 CIE (SAML) Authentication using Embedded Web-view 

 Release Date: May 2024 
 | 
 Last Updated: May 2026 

 Enterprises often require strict security compliance controls that necessitate periodic user verification, even when existing SAML tokens remain valid. Previously, users reconnecting the GlobalProtect app with Cloud Identity Engine (CIE) authentication were not prompted to re-enter their credentials, which created potential security gaps and compliance challenges. This enhancement introduces support for CIE (SAML) authentication using an embedded web-view , eliminating the need for complex pre-deployment configuration. Crucially, this feature now supports force authentication. You can now configure the GlobalProtect® app to prompt end users to reauthenticate whenever they reconnect, ensuring stricter access control and helping your organization achieve stringent security compliance goals. This functionality works even if the underlying SAML token has not yet expired. 

 Available in PAN-OS 11.2.0 and later releases. 

 GlobalProtect

 Core

 May 2024

 6.2

 GlobalProtect

 GlobalProtect App

 May 2024

 6.2

 CLI Support to Connect to the GlobalProtect App with SAML Authentication 

 Release Date: September 2024 
 | 
 Last Updated: June 2026 

 You can now use the command-line interface (CLI) to initiate, manage, and terminate SAML-authenticated sessions on Linux, giving you a command-line workflow for connection management without requiring you to interact with the full desktop application. 

 Previously, establishing a GlobalProtect connection with SAML authentication on Linux required using the GUI application throughout the entire process. There was no way to initiate or control connections from the command line, making it difficult to integrate GlobalProtect into scripted or automated workflows. 

 With this update, you use the GlobalProtect app CLI to start and manage connections. When SAML authentication is required, your default browser opens to complete the authentication step — after which the authenticated session is fully managed through the CLI. This lets you script connection setup and teardown while GlobalProtect handles the browser-based authentication handoff automatically. 

 This functionality is available starting with the GlobalProtect app for Linux version 6.2.1 and is supported on Fedora, Ubuntu, and Red Hat Enterprise Linux. 

 GlobalProtect

 GlobalProtect App

 September 2024

 6.2

 GlobalProtect

 Management

 September 2024

 6.2

 Strict Certificate Check for GlobalProtect App Connections 

 Release Date: August 2026 
 | 
 Last Updated: August 2026 

 Without a way to centrally enforce certificate validation, endpoints could potentially connect to portals or gateways presenting untrusted certificates, leaving them exposed to man-in-the-middle attacks. Fixing this required updating settings on each endpoint individually. 

 You can now enforce certificate validation for Windows and macOS endpoints directly from the portal agent configuration. Endpoints that receive this setting will only connect to portals and gateways presenting certificates signed by a trusted CA — no per-device changes required. 

 You can configure this alongside other portal agent settings in Customize the GlobalProtect App . 

 GlobalProtect

 GlobalProtect App

 August 2026

 6.2

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

 Virtual ION on KVM for NFV 

 Virtual ION on OCI 

 Virtual ION on VMware 

 3rd Party Integrations 

 AWS Cloud-WAN Integration (GRE Connect) 

 AWS Cloud-WAN Integration (Tunnel-less Connect) 

 Checkpoint Integration 

 LiveAction Integration 

 Netskope Integration 

 Symantec Web Security Services Integration 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
