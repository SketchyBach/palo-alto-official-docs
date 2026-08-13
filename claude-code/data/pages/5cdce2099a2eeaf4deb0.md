---
url: https://docs.paloaltonetworks.com/ai-runtime-security/ai-red-teaming/identify-ai-system-risks-with-ai-red-teaming/get-started-with-prisma-airs-ai-red-teaming/targets/custom-target-adapters/attach-a-custom-target-adapter-to-a-target
fetched_at: 2026-08-13T14:06:12Z
source: ai-security
---

# Attach a Custom Target Adapter to a Target Clear

Attach a Custom Target Adapter to a Target 

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

 Attach a Custom Target Adapter to a Target 

 Updated on 

 Fri Jul 24 03:07:12 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma AIRS Docs 

 Activation & Onboarding 

 Administration 

 AI Model Security 

 AI Red Teaming 

 Release Notes 

 New Features 

 Updated on 

 Fri Jul 24 03:07:12 PDT 2026 

 Focus 

 Home 

 Prisma AIRS 

 AI Red Teaming 

 Identify AI System Risks with AI Red Teaming 

 Get Started with Prisma AIRS AI Red Teaming 

 Targets 

 Custom Target Adapters 

 Attach a Custom Target Adapter to a Target 

 Download PDF 

 Prisma AIRS 

 Attach a Custom Target Adapter to a Target 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma AIRS Docs 

 Activation & Onboarding 

 Administration 

 AI Model Security 

 AI Red Teaming 

 Release Notes 

 New Features 

 Previous 

 Test and Validate a Custom Target Adapter 

 Next 

 Troubleshoot a Custom Target Adapter 

 Attach a Custom Target Adapter to a Target 

 After activating a custom target adapter, attach it to one or more targets by
 selecting Custom Adapter as the connection method and configuring the channel and optional
 overrides. 

 Where Can I Use This? What Do I Need? 

 Prisma AIRS (AI Red Teaming) 

 AI Red Teaming License 

 Network Channel
 client v1.4.0 or later 

 Adapter sidecar
 enabled 

 Before attaching a custom adapter to a target, complete the following: 

 Set up prerequisites —The Network Channel
 Helm chart must be at v1.4.0 or later, the adapter sidecar must be enabled, and
 a Network Channel must exist for the target's network. 

 An active Network Channel is required to host and
 execute adapter code. 

 Build the Custom Adapter Code/Script —Write and test
 your Python adapter functions before uploading. 

 Test and activate the adapter —The adapter
 must be active in the Custom Adapters list before it can be selected here. 

 You can point multiple targets at the same custom target
 adapter, each with its own overrides and channel. When you update and reactivate a
 shared adapter, every target using it picks up the change on its next scan. You do
 not need to edit each target individually. Scans in progress use the adapter version
 that was active when the scan started. Changes take effect from the next scan
 onward. 

 Attaching the adapter to a target is the final step in the custom adapter setup. For
 an overview of the complete workflow, see Custom Target Adapters . 

 In the AI Red Teaming, create a new target or open an existing target for
 editing. 

 After specifying Target Details , set the
 Connection Method to Custom
 Adapter . 

 Configure Endpoint Accessibility . This field indicates
 if your endpoint is Public or
 Private (secured within a private network). 

 Select IP Allowlist . To establish a successful
 connection, certain IP addresses must be allowed by your firewall. These
 IP addresses are region-specific, so you should allow the specific IP
 addresses shown in the tooltip within your interface. 

 Select Network Channels to configure private
 channels for endpoint connectivity. If a network channel was previously
 configured, it appears as an option in a drop-down menu. 

 Network channel is required for both private
 endpoint accessibility and custom adapter code execution. Therefore
 the network channel you select for endpoint accessibility in this
 step, is automatically selected for custom adapter in the next
 step. 

 Configure Custom Adapter. 

 In Custom Adapter , select the adapter you
 activated. 

 In Network Channel , select the channel for this
 target's network. 

 ( Optional ) Configure per-target value overrides. 
 In the Variable Overrides section, enter any
 variable or secret
 values that should replace the adapter's defaults for this
 specific target. For example, a different base_url for
 a staging environment or a different api_key for
 another account. Values you do not override fall back to the adapter's
 defaults at scan time. 

 ( Optional ) Enable Supports
 Multi-Turn . 
 Multi-turn support is disabled by default. Enable it only if your
 target supports multi-turn conversations and your adapter handles them.
 Enabling this setting allows scans to run multi-turn attacks against the
 target. 

 ( Optional ) Select Next: Advanced
 Configurations . 

 Enter the Successful Connection Message (test message) that the
 AI Red Teaming validation system sends to your adapter when you run
 Validate Target . 

 Configure the endpoint Rate Limits . Enter the
 maximum number of allowed requests per minute for this endpoint. 

 Enable Guardrails/Content Filters . These fields
 are used for output guardrails or content filters applicable on the
 target endpoint. 

 Specify the Error code for Guardrails or
 Content Filters . This field represents
 the error code your system uses when a response is
 prevented by filters or safeguards. 

 Provide a Sample Exception
 JSON . 

 Select Validate Target . 

 Only after a target is successfully validated, you
 can add target background information. 

 ( Mandatory ) Configure Target Background . 

 AI Red Teaming collects and organizes the Target background
 information about your target endpoint. Target background encompasses
 mandatory elements such as, industry classification, use case definition,
 and competitive landscape analysis, along with optional documentation
 uploads including company policy documents and other relevant materials. 

 Target background information is mandatory for all
 the target types. 

 Add Industry information. 

 Add Use Case , that is specific role of the
 target such as customer service or additional comments. 

 ( Optional ) Select Add Competitor to add
 the list of Competitors . 

 Enable Agentic Profiling. 
 Agentic Profiling in AI Red Teaming helps gather all relevant
 context about a target endpoint such as its business use case,
 background, key capabilities, technical architecture and other critical
 information. This is carried out by an autonomous agent probing the
 target endpoint with the right prompts. All information gathered through
 this exercise is presented as the Target's profile and is used
 downstream in AI Red Teaming Scans using the Agent. 

 Select Submit . 

 The target is now connected through the adapter and is available for scanning . 

 Previous 

 Test and Validate a Custom Target Adapter 

 Next 

 Troubleshoot a Custom Target Adapter 

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

 CN-Series 

 Firewalls 

 VM-Series 

 Cloud-Delivered Security Services 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 Enterprise DLP 

 Network Security 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 AI Red Teaming 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
