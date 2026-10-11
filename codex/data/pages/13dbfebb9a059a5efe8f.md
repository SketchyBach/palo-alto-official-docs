---
url: https://docs.paloaltonetworks.com/ai-runtime-security/administration/detect-and-alert-on-malicious-traffic/detect-and-prevent-ai-network-security-threats
fetched_at: 2026-10-11T09:52:15Z
source: ai-security
---

# Explore OWASP Coverage in Prisma AIRS AI Runtime: Network Intercept Clear

Updated on 

 Thu Oct 01 08:11:56 PDT 2026 

 Focus 

 Home 

 Prisma AIRS 

 AI Runtime Security 

 AIRS API 

 Explore OWASP Coverage in Prisma AIRS AI Runtime: Network Intercept 

 Download PDF 

 Prisma AIRS 

 Explore OWASP Coverage in Prisma AIRS AI Runtime: Network Intercept 

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

 Integrate Microsoft Foundry 

 Next 

 AIRS VM Firewall 

 Explore OWASP Coverage in Prisma AIRS AI Runtime: Network Intercept 

 Detect and secure AI network security threats. 

 Where Can I Use This? What Do I Need? 

 Prisma AIRS 

 Deploy AI
 Runtime Security instance 

Use the Prisma AIRS : Network intercept to detect
 malicious threats and secure your environment against OWASP top 10 
 LLM Applications threats. 
 In this section, you will create an AI security profile , attach it to a
 security profile group, and then add this profile group to a security policy rule to
 enforce a custom policy for all the security profiles in the group. 

 Licensing Capacity Limit: Limited to processing up to 10K
 AI transactions per day per vCPU of AI network intercept. 

 Log in to Strata Cloud Manager . 

 Select Manage Configuration NGFW and Prisma
 Access . 

 From the top menu, select Security Services AI Security . 

 Select Add Profile . 

 Enter a Name and a Description . 

 Select Add Model Group and configure the following
 protections: 

 AI applications security to protect against malicious URLs. 

 AI model protections to protect against Prompt Injections. 

 AI data protection to prevent data leakage to and from AI models. Import
 one of the predefined or custom Enterprise DLP profiles. 

 The URL security feature inspects both AI
 model input and output for URLs, categorizing each detected URL. You can set
 a default action for URLs and define exceptions. For example, set the
 default action to "Allow" and block specific categories like "Malware" and
 "Grayware." 

 See Create Model Groups in Strata Cloud Manager for detailed steps. 

 Select Manage Configuration NGFW and Prisma Access Security Services Profile Groups Add Profile Group and
 add the AI security profile to this group. See Security Profile Groups . 

 Create a Security Policy Rule 
 to detect the OWASP top 10 LLM Applications threats such as Prompt Injection and
 Data Leaks. 

 In the Profile Group tab, select and add the
 AI Security profile group that you configured earlier. 

 Select Incidents & Alerts Log Viewer . 

 Select Firewall/AI Security . 

 Review the logs to see the traffic blocked according to your AI Security
 profile name. 

 Analyze log entries for `ai-model-protection`, `ai-data-protection`, and
 `ai-application-protection`. 

 Previous 

 Integrate Microsoft Foundry 

 Next 

 AIRS VM Firewall
