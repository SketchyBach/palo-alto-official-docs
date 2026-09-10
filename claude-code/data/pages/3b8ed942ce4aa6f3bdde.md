---
url: https://docs.paloaltonetworks.com/ai-runtime-security/administration/api-intercept-create-configure-security-profile/ai-agent-security-low-no-code
fetched_at: 2026-09-06T11:17:11Z
source: ai-security
---

# AI Agent Security for Low-Code/No-Code Platforms Clear

Updated on 

 Mon Aug 24 04:41:52 PDT 2026 

 Focus 

 Home 

 Prisma AIRS 

 Administration 

 Defend: Create and Configure API Security Profile 

 AI Agent Security for Low-Code/No-Code Platforms 

 Download PDF 

 Prisma AIRS 

 AI Agent Security for Low-Code/No-Code Platforms 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma AIRS Docs 

 Activation & Onboarding 

 Administration 

 AI Supply Chain Security 

 AI Red Teaming 

 Release Notes 

 New Features 

 Previous 

 Managing Customer Encryption Keys 

 Next 

 Monitor: Threat Logs and AI Security Logs 

 AI Agent Security for Low-Code/No-Code Platforms 

 Secure your AI agents running on low-code or no-code platforms 

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

 If you enable AI Agent Protection without configuring an AI Agent
 framework in your application definition, then the AI Agent
 detection service only enables model-based protections and not
 pattern-based. 

 Review the API scan logs for any agent-related
 threats identified by fields such as Agent framework, Agent final verdict,
 prompt Agent verdict, and prompt Agent action. 

 See the Prisma AIRS 
 Scan APIs to detect agent-specific
 threats in the scan prompt and response. 

 Previous 

 Managing Customer Encryption Keys 

 Next 

 Monitor: Threat Logs and AI Security Logs
