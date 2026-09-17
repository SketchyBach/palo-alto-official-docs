---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/cloud-security/overview/personas-workflow
fetched_at: 2026-09-16T08:37:09Z
source: cortex-platform
---

# Personas workflow | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSIAM 

 Cortex XSIAM Documentation 

 Cloud Security 

 Web and API Security (WAAS) 

 Personas workflow 

 Cortex XSIAM API security responsibilities and workflows for SOC analysts, security practitioners, and workload owners. 

 The workflow outlines the responsibilities of each persona to detect, assess, protect, and secure the API assets across the organization, focusing on the main API security elements: 

 Visibility 

 Posture Management & Risk Profiling 

 Threat Detection & Response 

 SOC analyst 

 Responsibility : Real-time threat detection & response 

 The SOC analyst is the key to identifying and investigating API vulnerabilities and attacks within an organization. 

 Steps : 

 Visibility : Reviews the Cases & Issues module for new attacks. 

 Investigate : Select a case or an issue, analyze involved APIs and their context, analyze request/response details, and distinguish normal from malicious activity. 

 To conduct a deeper investigation to eliminate or contain the threat, investigate the security issue 

 Decide and Act : Determine if it's a true attack. If so, initiate an immediate response (often outside the UI) and flag for fixes. Close the case in the UI. 

 Security practitioner 

 Responsibility : Proactive posture management & risk reduction 

 The security practitioner uses the UI for continuous risk assessment and orchestration of remediation. 

 Steps : 

 Overview of API landscape : In the API Security Management dashboard, review emerging threats and understand the overall security of the API landscape. 

 Analyze APIs and Risks : Navigate to API endpoints to view all APIs, their risk factors (e.g., internet exposure, sensitive data, authentication/encryption status), and posture issues. Drill down for details. 

 Manage OpenAPI Specifications : Access the OpenAPI specification files. Review findings on the specification file itself (misconfigurations) and verify API traffic conformance to its specification. 

 Assign Remediation : Consolidate all findings, group them by application owner, and distribute tasks (via email/tickets with timelines) for fixes (code, gateway, specification updates). 

 Workload owner 

 Responsibility : Application security accountability 

 The workload owner acts on security tasks, primarily outside the UI. 

 Steps : 

 Receive Tasks : Get detailed security tasks and timelines from the security practitioner. 

 Implement Fixes : Apply necessary fixes to application code, API configurations, or OpenAPI specifications. 

 Ensure Compliance : Bring their APIs and assets into alignment with security standards. 

 Previous Web and API Security (WAAS) 

 Next Secure your API landscape 

 Last updated 1 month ago 

 Was this helpful?
