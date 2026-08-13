---
url: https://docs.paloaltonetworks.com/ai-runtime-security/administration/agent-discovery/protect-agents-using-api-intercept
fetched_at: 2026-08-13T14:04:39Z
source: ai-security
---

# View and Protect Agents Using API Intercept Clear

View and Protect Agents Using API Intercept 

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

 View and Protect Agents Using API Intercept 

 Updated on 

 Aug 10, 2026 

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

 Aug 10, 2026 

 Focus 

 Home 

 Prisma AIRS 

 Administration 

 Agent Discovery 

 View and Protect Agents Using API Intercept 

 Download PDF 

 Prisma AIRS 

 View and Protect Agents Using API Intercept 

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

 Setup AI Agent Discovery 

 Next 

 AI Agent Discovery Limitations 

 View and Protect Agents Using API Intercept 

 Learn how to view and protect agents using API Intercept in Prisma AIRS. 

 Where Can I Use This? What Do I Need? 

 Prisma AIRS AI Runtime Security 

 Prisma AIRS AI Runtime:
 Network Intercept Prerequisites and Limitations

 AI Agent Discovery allows you to discover agents from an onboarded cloud account and
 secure them using the AI Runtime API Intercept workflow. With the API intercept
 workflow, you protect applications using REST APIs by embedding Security-as-Code
 directly into source code. 

 The APIs protect your AI models, applications, and datasets by programmatically
 scanning prompts and models for threats, enabling robust protection across public
 and private models with model-agnostic functionality. Its model-agnostic design
 ensures seamless integration with any AI model, regardless of its architecture or
 framework. This enables consistent security across diverse AI models without any
 model-specific customization. For more information, see the API Intercept Overview page . 

 Before using Strata Cloud Manager to view and configure enterprise agents for AI
 Agent Discovery you need to Onboard and activate Prisma AIRS AI
 Runtime API intercept;during this process, when you click + 
 in the Agent Details page an API security profile is
 created. 

 This process allows you to
 activate an AUTH key to retrieve an API key and the sample code template you can
 embed in your application to detect threats. Once you've onboarded and activated
 API Intercept you can enforce security policy rules. After onboarding you can
 use AI Agent Discovery for your enterprise AI agents. 

 Use Strata Cloud Manager to View and Configure Enterprise Agents 

 To view and configure Enterprise Agents using Strata Cloud Manager: 

 Log into Strata Cloud Manager (SCM) . 

 In SCM, select AI Security > AI Agent Security > Enterprise
 Agents . 

 The All Agents page appears. You can use
 this page to view models, tools and knowledge bases. With this page, you
 can: 

 View all the Enterprise Agents that have been
 onboarded. 

 View details for each Enterprise Agent; point your cursor
 to the agent for additional information: 

 Filter the view based on a specific time frame (for example, past 24
 hours). 

 Manage APIs . With this
 option, you can manage added agents, added API keys, added security
 profiles, or manage custom topics. 

 View potential threats. 

 If an agent has a deployment profile that has not been activated you can
 activate it. Select the agent, then click the + icon
 to display the Activate Deployment Profile . 

 When you click
 + to activate a deployment profile, existing
 profiles appear; if you select a profile you can go through the process
 of creating a new security profile. You can use an unexpired API key for
 a cloud provider to protect the agent belonging to the provider. 

 In the Onboard API Account page, select the radio
 button next to the profile, then click Next : 

 After you activate the deployment profile, you
 can create a security profile if one hasn't been configured. Refer to
 this page for more information.

 In the Create Security Profile page: 

 Enter a Security Profile Name . 

 Select the AI Model Protection options you
 want to use. 

 Click Create Profile . 

 In the Add Application (Agent) page: 

 Enter an Application Name . 

 Select the Cloud Provider . This field
 represents the cloud where the AI application is running. 

 Select the Environment where the AI
 application is running. For example, PROD, Staging, or QA. 

 Select the AI Agent Framework ; this field is
 associated with the Cloud Provider. For example, if you selected AWS
 as the Cloud Provider, this field will be set to AWS Agent
 Builder. 

 Select the Deployment Profile . 

 Configure the Security Profile ; you can use
 this option to link to an existing security profile, or choose which
 profile to use in your app code. Use the slider to link or unlink
 the profile. 

 Click Next . 

 In the Input API Details page: 

 Enter the API Key Name . This field represents
 the name of the API key associated with the previously created AI
 application. 

 Select the appropriate Rotation to set the
 rotation frequency of the created API key. 

 Click the Generate API key. 

 After you generate the API key you
 can integrate the AIRS API into your application. Refer to the API reference documentation 
 for more information. 

 When AI agents exist in the unprotected state they are displayed in
 the All Agents dashboard: 

 If you select an AI agent in the unprotected state , you can use the
 dashboard to activate it (see Step 3 above): 

 When an AI agent exists in the protected state it is displayed in
 the All Agents dashboard. This view illustrates the
 protected threats and associated models, tools and knowledge bases: 

 When AI agents exist in both the protected and unprotected 
 state, the All Agents dashboard changes to show the status of both
 agents: 

 Important Considerations When Using the Prisma AIRS AI Runtime API 

 In addition to using Strata Cloud Manager to configure elements of AI Agent
 Discovery, you can also leverage the Prisma AIRS AI Runtime API to help discover
 and protect applications using REST APIs. Refer to the API reference documentation for more
 information. 

 There are a few important things to consider when using APIs for Agent
 Discovery: 
 An API key created for one cloud account cannot be used in another cloud
 account. 

 There are agent metadata requirements for: 
 AWS: all 3 agent metadata fields are required. 

 Azure: only the agent_id field is
 required. 

 Previous 

 Setup AI Agent Discovery 

 Next 

 AI Agent Discovery Limitations 

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

 Administration 

 Prisma AIRS 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
