---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/protect-your-endpoints/endpoint-dlp/cortex-data-loss-prevention-dlp-module-overview
fetched_at: 2026-08-13T15:14:40Z
source: cortex-platform
---

# Cortex Data Loss Prevention (DLP) module overview | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

Cortex Data Loss Prevention (DLP) module overview | Cortex Documentation Portal 

 ⌘ Ctrl k 

 Blog Support 
 More 

 Home 

 Products 

 Guides 

 Release Notes 

 API 

 Reference 

 AI Assistant 

 Good afternoon 
 I'm here to help you with the docs. 

 What is this page about? What should I read next? Can you give an example? 

 ⌘ Ctrl i 

 AI Based on your context 
 Send 

 Learn about Cortex XSIAM 

 Navigate the Cortex XSIAM docs 

 Get started with Cortex XSIAM 

 Agentic AI in Cortex XSIAM 

 Cortex XSIAM product licenses 

 In-product support ticket creation 

 Supported web browsers 

 Use the interface 

 Manage API keys 

 Onboard Cortex XSIAM 

 How to onboard Cortex XSIAM 

 Plan and prepare 

 Deployment steps 

 Post-deployment 

 Configure Cortex XSIAM 

 Learn how to configure Cortex XSIAM 

 Data management 

 Cortex XSIAM Data Sources and Connectors 

 Marketplace 

 Configure the Cortex Agentic Assistant 

 Cortex MCP server 

 Automations 

 Engines 

 Remote repository management 

 Customize cases and issues 

 XQL query management 

 Multi-Tenant 

 Managed Services configuration in Cortex 

 Protect your endpoints 

 Endpoint security 

 Endpoint DLP 

 Cortex Data Loss Prevention (DLP) module overview 

 Archive file classification 

 True-file type detection 

 Personas workflow for DLP 

 Best Practices 

 Configure DLP end-to-end 

 DLP status in all endpoints 

 Cortex DLP threat detection and issues 

 Detect, Investigate, and respond to threats 

 Monitor dashboards and reports 

 Investigation and response 

 Agentic Assistant chat 

 Asset management 

 Threat management 

 Attack surface management 

 Vulnerability management 

 Exposure management 

 Cortex Advanced Email Security 

 Identity Threat Detection and Response (ITDR) 

 Cloud Security 

 Monitor and track compliance adherence 

 Cloud security rules and policies 

 Cortex Cloud Data Classification 

 Cortex Data Security 

 Cloud Identity Security 

 Network exposure detection 

 Cortex Cloud SaaS Security 

 Cortex Cloud AI Security 

 Serverless function posture security 

 Cortex Cloud Application Security 

 Cloud workload policies and rules 

 Base image rules 

 Web and API Security (WAAS) 

 Serverless function runtime security 

 Reference and developer docs 

 Cortex XSIAM XQL 

 Graph Search 

 Cortex CLI 

 Role-Based Access Control 

 API documentation 

 Reference 

 Migrating to a new Broker VM image 

 Learn more about migrating to the latest broker VM image 

 Standalone Broker VM 

 Broker VM high availability cluster node 

 On this page 

 For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSIAM 

 Cortex XSIAM Documentation 

 Protect your endpoints 

 Endpoint DLP 

 Cortex Data Loss Prevention (DLP) module overview 

 Learn about Cortex Data Loss Prevention (DLP) module, which provides a solution to prevent sensitive data exfiltration. 

 Prerequisite 

 Endpoint DLP add-on license 

 Cortex agent 9.1 and above for Windows and macOS 

 The Cortex Data Loss Prevention (DLP) module provides a unified, flexible solution for preventing the exfiltration of sensitive data. It continuously enforces policies on endpoints (even offline) across web, local, and USB channels, protecting both on-premises and cloud environments. 

 After endpoint DLP is enabled, the DLP module is downloaded to all eligible endpoints. 

 This highlights Cortex's benefit of proactively safeguarding sensitive information. Future enhancements will include data-at-rest discovery, adaptive policies, and broader channel support. 

 Supported platforms and browsers 

 Supported platforms: 

 Windows: x64 (ARM CPU architecture not supported) 

 macOS 

 Supported browsers for the Cortex data security extension: Google Chrome and Microsoft Edge (Chrome Enterprise is not supported in MDM mode) 

 Either the endpoint must be joined to a domain, or the browser must be managed. 

 Supported file types and extensions 

 Windows/macOS supported file types and extensions 

 Category/application 

 Supported formats and extensions 

 Microsoft Office 

 doc, docx, dotx, ppsx, potx, ppt, pptx, xls, xlsx, xsltx 

 Microsoft Visio 

 vsd, vsdm, vsdx 

 iWork 

 key, numbers, pages 

 Standard documents 

 csv, pdf, rtf, txt, xps, oxps 

 Image files and storage 

 bmp, jpeg, jpg, png, tif, tiff 

 Source code/development (C-family) 

 c, cpp, cxx, c++, h, hpp, cs, m 

 Source code/development (scripting and programming) 

 cgi, jav, java, js, pl, ps1, py, r, rb, vbs 

 Source code/development (hardware and assembly) 

 asm, s, v, verilog, vh, vhd1, vlg 

 Archived and compressed files (supported from 9.3) 

 zip, 7z, rar, tar, gz, tar.bz2, tbz2, tar.bz, tbz, tar.xz, txz, tar.zst, tzst 

 *tgz - will not be supported in 9.3 

 Agent limitations 

 Supported platforms: Windows and macOS 

 Minimum agent version: 9.1.0 

 USB channel on Windows: 

 Before Windows 11 version 22H2, tracking is limited to files transferred to USB drives via File Explorer. 

 Archive file support: The system can scan up to 50 levels of nested archives. Content beyond this limit is not classified. 

 Supported file size: up to 300 MB (Cortex agent 9.3 and later). 

 Handwritten text: Detection of handwritten text is currently not supported. 

 Local applications: 

 On Windows, we only support WebView2-based applications such as WhatsApp, Microsoft Teams, and Zoom starting from agent version 9.2.0. 

 Use cases 

 Protecting personal information: Protects information like names, addresses, and credit card numbers to adhere to privacy policies (like GDPR or HIPAA). 

 Guarding company secrets: Prevents valuable designs, formulas, and business plans from falling into the wrong hands (like competitors). 

 Meeting legal rules: Helps businesses in specific industries (like healthcare or finance) follow strict laws about handling data. 

 Stopping leaks (accidental or intentional): Catches employees trying to email sensitive files to their accounts or upload them to unauthorized websites. It also helps prevent cybercriminals from stealing data. 

 Seeing and controlling data: Helps you locate all your important data and allows you to determine who can access it and how it can be utilized. 

 User roles and permissions 

 Cortex DLP now includes two new out-of-the-box roles: 

 Data security admin: Defines the policy and its key components, including applications. 

 Data security viewer: Reviews and analyzes DLP-related issues. 

 Refer to the Personas workflow for DLP for steps on how to create and manage endpoint DLP in your environment. 

 Verify that the user has the correct permissions in the linked role for access and configuration permissions to DLP capabilities. 

 Go to Settings → Configuration → Access Management → Roles . 

 Go to the relevant role, right-click and select Edit Role , and in the Components tab, verify under Data Security that the settings are configured to View/Edit . 

 Previous Endpoint DLP Next Archive file classification 

 Last updated 8 days ago 

 Was this helpful? 

 ‍ 

 Trust Center 

 ‍ 

 Privacy 

 ‍ 

 Terms of Use 

 ‍ 

 Legal 

 © 2026 Palo Alto Networks, Inc. All rights reserved. 

 Was this helpful?
