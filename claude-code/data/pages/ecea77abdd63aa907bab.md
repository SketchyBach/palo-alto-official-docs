---
url: https://docs.paloaltonetworks.com/ai-runtime-security/ai-red-teaming/identify-ai-system-risks-with-ai-red-teaming/get-started-with-prisma-airs-ai-red-teaming/targets/third-party-registration-and-integration
fetched_at: 2026-08-13T14:06:25Z
source: ai-security
---

# Third-party Registration and Integration Clear

Third-party Registration and Integration 

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

 Third-party Registration and Integration 

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

 Third-party Registration and Integration 

 Download PDF 

 Prisma AIRS 

 Third-party Registration and Integration 

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

 View Target 

 Next 

 Register Application on Microsoft Entra for AI Red Teaming 

 Third-party Registration and Integration 

 Register AI Red Teaming as a trusted application in a third-party identity provider
 to authenticate and run security scans against protected APIs and AI agents. 

 Where Can I Use This? What Do I Need? 

 Prisma AIRS (AI Red Teaming) 

 Prisma AIRS AI Red Teaming License 

 Prisma AIRS AI Red Teaming Deployment Profile 

 ( For Entra ID scenarios ) An Azure account with an
 active subscription 

 ( For Entra ID scenarios ) Admin access to Microsoft
 Entra ID (to grant application permissions) 

 ( For n8n ) An active n8n instance (cloud
 or self-hosted) with a published workflow and production webhook
 URL 

 Many AI systems and agents restrict access behind authentication layers. To run security
 scans against these protected targets, AI Red Teaming must authenticate as a trusted
 client before it can send attack payloads. Depending on the target, this means
 registering AI Red Teaming as an application in a third-party identity provider, or
 configuring webhook-level credentials that the target's endpoint validates on each
 request. 

 Supported Authentication Scenarios 

 AI Red Teaming supports authentication for the following third-party integration
 scenarios: 

 OAuth 2.0 client credentials flow : Use this when your target is a REST
 API or streaming endpoint protected by Azure Entra ID. This flow is designed for
 server-to-server, fully automated authentication. AI Red Teaming uses the
 client_credentials grant type to fetch and cache access
 tokens throughout the scan without requiring a user to be present. Token refresh
 is handled automatically. 

 Microsoft Copilot Studio : Use this when your target is a Microsoft
 Copilot Studio agent. This scenario uses a one-time delegated authentication
 flow where you log in through Microsoft once to authorize AI Red Teaming. This
 generates a refresh token valid for 90 days that AI Red Teaming uses to
 authenticate for subsequent scans. 

 n8n : Use this when your target is an AI agent built in
 n8n. n8n agents expose an authenticated webhook URL that AI Red Teaming calls
 directly. No identity provider registration is required. Authentication uses
 either a custom HTTP header ( Header Auth ) or standard
 credentials ( Basic Auth ) configured on the n8n Webhook
 node. 

 Scenario Target Type Auth Mechanism User Interaction Required 

 OAuth 2.0 client credentials REST APIs or streaming endpoints protected by Entra ID client_credentials grant None (fully automated) 

 Microsoft Copilot Studio Copilot Studio agents authorization_code grant (one-time) Required once for initial authorization 

 n8n n8n workflow agents (Agent target type) Header Auth or Basic Auth on the n8n Webhook node None (fully automated) 

 What Registration Enables 

 For both Microsoft Entra ID scenarios, you register AI Red Teaming as an application
 in Microsoft Entra ID. The registration process differs depending on your
 target: 

 ( For OAuth 2.0 ) Configure Application permissions (not Delegated) and
 skip the redirect URI. AI Red Teaming authenticates using its own identity and
 does not require a user sign-in during scanning. Admin consent is required to
 activate the Application permissions. 

 ( For Microsoft Copilot Studio ) Configure Delegated permissions with
 the CopilotStudio.Copilots.Invoke scope and add a redirect
 URI. The redirect URI receives the authorization code after your one-time login,
 which AI Red Teaming exchanges for a refresh token. 

 After registration, AI Red Teaming handles the full token lifecycle automatically,
 including token fetching, caching, and refresh, so scans run uninterrupted without
 manual intervention. To register your application and configure authentication,
 follow the steps in Register Application on Microsoft Entra for AI Red
 Teaming . For supported grant types, token lifecycle management, and scope
 configuration details, see Azure Entra ID and AI Red Teaming OAuth 2.0
 Integration . 

 n8n Integration 

 n8n is a workflow automation platform for building AI agents. An n8n agent typically
 chains a Webhook trigger node, an AI model node, and a Respond to Webhook node. AI
 Red Teaming connects to the agent through its published webhook URL, sending attack
 prompts as HTTP POST requests and reading the AI model's responses. 

 n8n integration does not require application registration with an identity provider.
 You configure authentication directly on the n8n Webhook node and provide the same
 credentials when creating the target in AI Red Teaming. The n8n connection method
 supports REST and streaming response modes, single-turn and multi-turn
 conversations, and multimodal file attacks against n8n agents. To configure an n8n
 agent as a target, follow the steps in n8n Connection Method . For
 authentication options, response modes, multi-turn behavior, and file attack
 details, see n8n and AI Red Teaming Integration . 

 Previous 

 View Target 

 Next 

 Register Application on Microsoft Entra for AI Red Teaming 

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
