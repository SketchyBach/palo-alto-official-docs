---
url: https://docs.paloaltonetworks.com/ai-runtime-security/activation-and-onboarding/ai-runtime-security-api-intercept-overview/configure-openai-codex-integration
fetched_at: 2026-08-13T14:02:57Z
source: ai-security
---

# Configure OpenAI Codex Integration Clear

Configure OpenAI Codex Integration 

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

 Configure OpenAI Codex Integration 

 Updated on 

 Tue Aug 11 09:28:58 PDT 2026 

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

 Tue Aug 11 09:28:58 PDT 2026 

 Focus 

 Home 

 Prisma AIRS 

 Activation & Onboarding 

 Prisma AIRS AI Runtime: API Intercept Overview 

 Configure OpenAI Codex Integration 

 Download PDF 

 Prisma AIRS 

 Configure OpenAI Codex Integration 

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

 Integrate Anthropic Inference Hooks 

 Next 

 Prisma AIRS MCP Server for Centralized AI Agent Security 

 Configure OpenAI Codex Integration 

 Learn about Prisma AIRS integration with OpenAI Codex. 

 Where Can I Use This? What Do I Need? 

 Prisma AIRS AI Runtime Security in
 AWS 

 Prisma AIRS AI Runtime Firewall Prerequisites and Limitations 

 Prisma AIRS Runtime API integrates natively with OpenAI Codex Enterprise to
 enforce real-time threat prevention and Data Loss Prevention (DLP) across every
 developer prompt in your organization. Inspection happens at the platform level;
 developers experience no workflow changes, plugin installs, or latency. 

 When Prisma AIRS detects a threat, it sends a block verdict to OpenAI Codex
 before the prompt reaches the destination model or any connected MCP server. 

 Prerequisites 

 OpenAI Codex Enterprise account with admin access 

 Prisma AIRS management (via Strata Cloud Manager) access with
 permission to generate API credentials 

 To configure OpenAI Codex integration: 

 Retrieve your Prisma AIRS credentials: 

 Log into Strata Cloud Manager
 (SCM) . 

 Click AI Security > AI Runtime > API Applications : 

 Click Manage in the upper right portion of
 the AI Applications page: 

 Select API Keys . 

 In the Manage API Keys screen, click
 Add New Application/API Key . 

 Follow the onboarding work flow to generate a new API Key and endpoint
 URL. Copy both values; you'll use this information to configure the
 OpenAI Codex. 

 Configure the OpenAI Codex: 

 Sign in to the OpenAI Codex Enterprise admin dashboard. 

 Locate the security or API integration settings. 

 Paste the Prisma AIRS API key and endpoint URL into the designated
 fields. 

 Save the configuration. 

 Activate org-wide scanning in the OpenAI Codex Enterprise admin dashboard. 

 Once saved, all users in Codes across your OpenAI organization are
 automatically routed through the Prisma AIRS Runtime API for real-time
 inspection. No additional action is required. 

 What Gets Inspected 
 Prisma AIRS scans every developer prompt before
 it reaches the model, covering two threat vectors: 

 Data Loss
 Prevention 

 Data Loss Prevention (DLP) Examples 

 Secrets and credentials API keys, passwords, tokens, private keys 

 PII and financial data Personal identifiers, regulated data patterns 

 Proprietary code and IP Internal architecture, trade secrets, custom pattern
 rules 

 Threat and Malicious Code Detection 

 Threat Type Description 

 Malicious code patterns Obfuscated scripts, dangerous command executions, known
 exploit patterns 

 Malicious URLs Phishing domains or unverified links embedded in
 prompts 

 Prompt manipulation attacks Adversarial inputs designed to bypass controls or alter
 model behavior 

 How it Works 

 Prisma AIRS operates as an inline security
 layer between the developer and the destination model: 

 The developer submits a prompt in OpenAI Codex. 

 The prompt is routed to the Prisma AIRS Runtime API for
 inspection. 

 If clean — the prompt is forwarded to the model as
 normal. 

 If a threat is detected — a block verdict is returned and
 the prompt is stopped before reaching the model or any MCP
 server. 

 Developers see no difference in their normal
 workflow. Security teams receive centralized logs and policy enforcement
 across the entire engineering organization. 

 Audit &
 Visibility 

 Because inspection occurs at the administrative API
 layer, security teams gain: 

 Centralized policy enforcement — consistent rules applied
 across all users and sessions 

 Audit-ready logging — full visibility into blocked and
 allowed traffic 

 No per-developer configuration — governance is org-wide
 from a single control point 

 Previous 

 Integrate Anthropic Inference Hooks 

 Next 

 Prisma AIRS MCP Server for Centralized AI Agent Security 

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

 Activation & Onboarding 

 Prisma AIRS 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
