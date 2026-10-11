---
url: https://docs.paloaltonetworks.com/ai-runtime-security/administration/api-intercept-create-configure-security-profile/ai-agent-security-low-no-code
fetched_at: 2026-10-11T09:52:27Z
source: ai-security
---

# AI Agent Security for Low-Code/No-Code Platforms Clear

Updated on 

 Aug 13, 2026 

 Focus 

 Home 

 Prisma AIRS 

 AI Agent Identity 

 SaaS Agent Security Overview 

 AI Agent Security for Low-Code/No-Code Platforms 

 Download PDF 

 Prisma AIRS 

 AI Agent Security for Low-Code/No-Code Platforms 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma AIRS 

 Getting Started 

 Activation & Onboarding 

 AI Inventory 

 AI Red Teaming 

 AI Supply Chain Security 

 AI Runtime Security 

 AI Gateway 

 AI Agent Identity 

 Release Notes 

 New Features 

 Previous 

 Onboard SaaS Agents for AI Agent Discovery 

 Next 

 Prisma AIRS MCP Server for Centralized AI Agent Security 

 AI Agent Security for Low-Code/No-Code Platforms 

 Secure AI agents on low-code and no-code platforms against prompt injection and unauthorized actions using Prisma AIRS AI Runtime Security. 

 Where Can I Use This? What Do I Need? 

 AI Agent Security 

 Create and Associate a
 Deployment Profile for Prisma AIRS AI Runtime: API
 Intercept 

 Prisma AIRS detects and prevents malicious exploitation
 of AI agents deployed on no-code/low-code platforms, protecting against unauthorized
 actions and system manipulation. 
 The AI Agent security provides model-based and
 pattern-based detection services. 

 AI agents could be deployed on
 no-code/low-code platforms like AWS Agent Builder, GCP Agent Builder, Microsoft
 Copilot Studio, and Azure AI Agent Builder. 

 The feature secures your
 AI Agents using a prompt injection detection service against threat vectors such
 as: 
 Function schema extraction : Leaks when asking questions about
 available tools/schema. 

 Direct function invocation : Involves leakage of tool names; the
 attacker asks the agent to invoke the tool directly. 

 Memory manipulation : includes directly modifying long-term memory
 when incorporating predefined schema tags. 

 AI Agent Security Components : 
 AI Agent framework : The framework in which your cloud workloads
 run. 

 AI Agent protection : Update API security profile to activate
 agent-specific threat detection. When enabled, the system will inspect API
 calls for signs of function schema extraction, direct function invocation,
 and memory manipulation attempts. 

 To secure your AI agents, 

 Configure a Prisma AIRS API security profile by
 defining applications and configuring an AI agent
 framework . 

 Enable AI Agent Protection in your API security profile . 

 If you enable AI Agent Protection without configuring
 an AI Agent framework in your application definition,
 the AI Agent detection service enables only model-based protections, not
 pattern-based. 

 Review the API scan logs for any agent-related
 threats identified by fields such as Agent framework, Agent final verdict,
 prompt Agent verdict, and prompt Agent action. 

 See the Prisma AIRS 
 Scan APIs to detect agent-specific
 threats in the scan prompt and response. 

 Previous 

 Onboard SaaS Agents for AI Agent Discovery 

 Next 

 Prisma AIRS MCP Server for Centralized AI Agent Security
