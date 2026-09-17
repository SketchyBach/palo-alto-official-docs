---
url: https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/saas-security/saas-security/saas-ai-agent-security/onboard-saas-ai-agents/onboard-cursor-enterprise
fetched_at: 2026-09-16T08:47:55Z
source: cortex-platform
---

# Onboard Cursor Enterprise | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Cortex CLOUD Posture Management 

 SAAS SECURITY 

 SaaS Security 

 SaaS AI Agent Security 

 Onboard SaaS AI Agents 

 Cortex Cloud Posture 

 Onboard Cursor Enterprise 

 Connect Cursor Enterprise in Cortex Cloud Posture Management SaaS AI Agent Security for visibility and control across your AI ecosystem. 

 Cursor Enterprise is the secure, scalable version of Cursor, an AI-powered code editor built on VS Code. It is designed for large organizations needing advanced features like SSO, audit logs, usage analytics, and data privacy controls to manage AI-assisted software development for complex codebases. It provides features such as IP allowlisting, team management, centralized security, and compliance tools (GDPR, CCPA, SOC 2) to meet enterprise security and governance needs, allowing teams to build faster and more efficiently. 

 Important : Due to Cursor Enterprise API restrictions, any discovery for Tools and Knowledge Bases is limited to the last 30 days. If you want to increase this duration, contact Technical Support. 

 Create an Admin API Key in Cursor Enterprise. 

 Go to the Cursor Enterprise dashboard and select Settings > API Keys > New API Key. 

 Copy the generated Admin API Key and keep it handy for the onboarding steps. 

 Onboard Cursor Enterprise to Cortex. 

 Log in to Cortex. 

 Select Settings > Data Sources and Integrations > Add New . You can use the Search bar to find the Cursor connector. 

 Click on the Cursor tile and select Add Another Instance . 

 On the Capabilities page, provide an Instance Name and select Agent Security scanning capability. 

 On the Connections page, provide your Instance URL and enter your API Key to initiate the authentication flow. 

 Once AISPM validates the credentials and permissions, the onboarding process is complete. 

 Validation and Scanning: Cortex establishes the connection and validates the credentials and permissions. After successful validation, you will see a confirmation message. The amount of time Cortex takes to scan varies based on the amount of data it is required to scan. At a minimum, it takes at least one hour to scan and display data in the AISPM dashboard. 

 Previous Onboard ChatGPT Enterprise 

 Next Onboard Gemini Enterprise 

 Last updated 2 days ago 

 Was this helpful?
