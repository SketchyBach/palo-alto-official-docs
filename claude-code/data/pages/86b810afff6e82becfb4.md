---
url: https://docs.paloaltonetworks.com/saas-agent-security/administration/respond-to-security-recommendations/risk-recommendations
fetched_at: 2026-08-13T17:32:36Z
source: palo-alto-main
---

# Risk Recommendations Clear

Risk Recommendations 

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

 Risk Recommendations 

 Updated on 

 Mon Jun 01 16:05:41 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 SaaS Agent Security Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Release Notes 

 New Features 

 Updated on 

 Mon Jun 01 16:05:41 PDT 2026 

 Focus 

 Home 

 SaaS Agent Security 

 Respond to Risk Recommendations 

 Risk Recommendations 

 Download PDF 

 SaaS Agent Security 

 Risk Recommendations 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 SaaS Agent Security Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Release Notes 

 New Features 

 Previous 

 Respond to Risk Recommendations 

 Next 

 Risk Severity Calculations 

 Risk Recommendations 

 Learn about the types of risks that SaaS Agent Security can detect in your
 agentic platforms and the agents that they host. 

 Where Can I Use This? What Do I Need? 

 Strata Cloud Manager 

 SaaS Agent Security license 

 Or any of the following licenses that include the SaaS Agent Security license: 

 CASB-X 

 CASB-PA 

 SaaS Security Posture Management license 

 SaaS Agent Security runs regular scans of the agentic platforms that you have
 onboarded. These scans detect risks in the platforms and in the agents that they host.
 These detected risks appear in the Recommendations panel of the SaaS Agent Security dashboard, with information about the platform instances
 and agents where the risks were detected. 

 Each risk type has a severity level to communicate its potential impact and to guide your
 prioritization of remediation efforts. 

 Critical: Identifies risks that, if exploited, could lead to a catastrophic
 event, such as a large-scale data breach or complete system compromise. You should
 address these risks immediately. 

 High: Identifies risks that, if exploited, could lead to a significant data
 breach. This risk level also includes significant monitoring and visibility gaps,
 such as SaaS Agent Security failing to connect to an agent platform or an
 agent operating without an audit trail. 

 Medium: Identifies risks that compromise an agent's security posture.
 These risks are a priority but are not considered an emergency. This risk level
 also includes moderate monitoring gaps, such as a connected application that
 requires onboarding to enable scans. 

 Low: Identifies operational issues that do not pose a security threat.
 However, these risks could point to underlying problems that should be addressed as
 part of routine maintenance. 

 Threat Description Severity 

 Agent with No Authentication Detected 

 SaaS Agent Security detected an agent for which no
 authentication mechanism was configured. This lack of authentication
 is a critical vulnerability, because it leaves the agent, and
 potentially the applications it connects to, exposed to unauthorized
 access and manipulation. 

 For example, when building a scheduling agent that connects to your
 organization's calendar application, an agent developer might fail
 to have the agent explicitly ask for authentication. This
 misconfiguration could expose users' calendars to bad actors. 

 If SaaS Agent Security detects this risk, immediate action
 is required. Implement robust authentication protocols for the
 agent. Ensure that all agents are configured with appropriate
 authentication mechanisms to secure their operations and prevent
 unauthorized access. 

 Critical 

 Agent Identified with Excessive Permissions 

 SaaS Agent Security detected an agent that has elevated
 permissions to a connected application. SaaS Agent Security detects this threat by identifying agents that were granted
 excessive permissions to a connected application, such as broad
 administrative read and write capabilities within the application. 

 For example, an administrator might have granted the application
 account these excessive permissions as a shortcut to avoid setting
 up granular permissions. 

 When an AI agent has elevated permissions to even a single
 application, it creates a significant security risk. An attacker
 could use the agent to gain control of the connected application and
 exfiltrate its data. The attacker could potentially use the
 connected application as the starting point for a lateral movement
 attack. 

 If SaaS Agent Security detects this risk, we strongly
 recommend reviewing the agent's permissons and revoking any
 permissions that are unnecessary. Grant the agent only the
 permissions it needs to complete its function. 

 High 

 Agent without Delegated Permission 

 SaaS Agent Security detected an agent that is accessing a
 connected application without inheriting or impersonating the
 permissions of the user who is interacting with the agent. In this
 case, the agent might instead inherit permissions from a Non-Human
 Identity (NHI), such as the service account, API key, or OAuth
 application, that it used to connect to the application. As a
 result, the human users of the agent might have indirect access to
 resources they typically wouldn't be authorized to access. 

 If SaaS Agent Security detects this risk, we strongly
 recommend that you re-architect the agent to use delegated
 permission. 

 High 

 Dormant Agent Detected 

 SaaS Agent Security detected an agent that has shown no
 activity for over 30 days. Specifically, the agent has not had any
 chat interactions within the last month. 

 A dormant agent represents an unnecessary security risk because,
 although it is not being used, it might still have active tokens or
 permissions to connected applications or knowledge bases. If the
 agent becomes compromised, its inactivity might delay detection of
 malicious use. 

 For example, an agent developer might have created an agent for a
 specialize purpose and created a service account for it to connect
 to an application. The developer leaves the company, and, although
 the agent is not being used, it still has permissions to the
 connected application. 

 You should review the identified dormant agent to determine if it's
 needed. If the agent is no longer needed, you should deactivate or
 remove it to reduce potential attack surfaces. 

 Medium 

 Agent Access to Sensitive Knowledge Bases 

 SaaS Agent Security detected an agent with access to
 knowledge bases that contain sensitive information. This access
 could result in exposure of the sensitive information. This could be
 an inadvertent disclosure in response to a benign prompt, or it
 could be the result of a deliberate prompt injection attack. 

 You should conduct an immediate review of the agent's access
 permissions to the sensitive knowledge bases. Ensure that the agent
 has access only to the specific information it requires for its
 designated functions. 

 High 

 Missing Application Onboarding 

 SaaS Agent Security detected an agent that has one or more
 connected applications that were not onboarded into SaaS Security Posture Management (SSPM). As a result, SSPM is not scanning these
 application instances for security posture vulnerabilities. To gain
 additional insights into the agent's connected applications, onboard them into
 SSPM . 

 Medium 

 Invalid Credentials Detected 

 Due to invalid credentials, SaaS Agent Security 
 could not access an agentic platform or could not access certain
 connected applications for an agent. The credentials might be
 invalid for a number of reasons, such as an expired token, revoked
 access, or changed credentials. 

 Failure to access an agentic platform prevents
 platform-level visibility into the agents and the applications they
 support. Failure to access an agent's connected application prevents
 SSPM from scanning the application instance for security posture
 vulnerabilities. 

 You should ensure the credentials are valid. For an agentic platform,
 re-authenticate to SaaS Agent Security . For an
 agent-connected application, re-authenticate to
 SSPM . 

 High 

 Health Degradation Detected During Scanning 

 During scanning, SaaS Agent Security detected
 health-degradation errors. These errors, such as rate limiting or
 400/500 errors from the applications the agents interact with, often
 point to underlying network or service stability problems. 

 SaaS Agent Security may have detected the health
 degradation for an agentic platform, or for a agent connected
 application. 

 To ensure stable and reliable scanning operations, investigate the
 root cause of the health degradation. This may involve examining
 network connectivity, API rate limits on the application side, or
 the health of the agents' connected applications and knowledge
 bases. 

 Low 

 Agent with No Auditability Detected 

 SaaS Agent Security detected an agent with write
 permissions operating without audit logging enabled. This creates a
 critical visibility gap, making it impossible to trace potentially
 malicious or erroneous actions, which severely hinders incident
 response and forensic investigations. 

 To maintain a clear and comprehensive audit trail, enable audit
 logging for the identified agent immediately. Ensure that all agent
 activities, especially those involving data modification or
 configuration changes, are captured in immutable logs. 

 High 

 Agent with No Data Masking Enabled 

 SaaS Agent Security detected an agent that
 handles or logs data without masking sensitive information. This
 exposes Personally Identifiable Information (PII), credentials, or
 other confidential data in plain text, which increases the risk of a
 data breach. A lack of data masking can lead to serious violations
 of data privacy regulations, such as GDPR (General Data Protection
 Regulation), HIPAA (Health Insurance Portability and Accountability
 Act), and CCPA (California Consumer Privacy Act). 

 To prevent the exposure of sensitive information, configure and
 enable data masking for the identified agent. Review agent logs and
 outputs to ensure that sensitive data types are properly redacted or
 obscured, protecting sensitive information from unauthorized
 exposure. 

 High 

 Agent Using Weak Authentication Detected 

 SaaS Agent Security detected an agent that is
 using a deprecated and insecure authentication method, such as Basic
 Auth or OAuth 1.0. These protocols are vulnerable to credential
 theft through interception, posing a direct threat to the agent and
 the systems it connects to. 

 To protect credentials and prevent unauthorized access, you should
 immediately upgrade the authentication protocol for the identified
 agent. Migrate to a secure standard, such as OAuth 2.0 or SAML. 

 Medium 

 Agent with Malicious System Prompt Detected 

 SaaS Agent Security detected an agent with a malicious
 system prompt. This indicates that the agent's core instructions
 were deliberately crafted to perform harmful actions, bypass safety
 controls, or exfiltrate data. This could be the result of an insider
 threat or a compromised development process. 

 Immediately contain the threat by disabling the identified agent.
 Launch an investigation to determine the origin and intent of the
 malicious prompt. Review access logs and author details, and
 investigate other agents created by the same author. 

 Critical 

 Malicious User Prompt Detected 

 SaaS Agent Security detected an active attempt by
 a user to compromise an agent by injecting a malicious prompt. This
 attempt was intended to manipulate the agent into violating its
 operational or safety policies. 

 This detection is based on the chat transcript history for the past
 30 days 

 Review the conversation logs associated with this event to understand
 the context and nature of the attack. Analyze the agent's responses
 to determine if the attack was successful in bypassing security
 policies or eliciting unintended behavior. Based on the findings,
 consider suspending the user's access and use the insights to
 enhance prompt validation rules or refine the agent's underlying
 guardrails. 

 High 

 Previous 

 Respond to Risk Recommendations 

 Next 

 Risk Severity Calculations 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Activate a License or Product 

 Cloud Identity Engine 

 Strata Logging Service 

 Device Associations 

 Identity and Access Management 

 Tenant Management 

 Next-Generation Firewalls 

 Cloud Management for NGFWs 

 Cloud NGFW for AWS 

 Cloud NGFW for Azure 

 CN-Series 

 Firewalls 

 PAN-OS 

 VM-Series 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 AI-Powered ADEM 

 Prisma Access Monitoring and Visibility 

 Next-Generation CASB 

 Cloud-Delivered Security Services 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 Device Security 

 Enterprise DLP 

 SaaS Security 

 Experts Corner 

 Solutions Docs from Product Experts 

 Administration 

 Cloud-Delivered Security Services 

 SaaS Agent Security 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
