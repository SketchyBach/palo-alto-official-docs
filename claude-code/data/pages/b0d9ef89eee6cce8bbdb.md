---
url: https://docs.paloaltonetworks.com/ai-runtime-security/administration/discover-your-cloud-resources/ai-traffic-network-risk-analysis
fetched_at: 2026-08-13T14:03:20Z
source: ai-security
---

# Analyze Risk in Network Traffic Clear

Analyze Risk in Network Traffic 

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

 Analyze Risk in Network Traffic 

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

 Discover Your Cloud Resources 

 Analyze Risk in Network Traffic 

 Download PDF 

 Prisma AIRS 

 Analyze Risk in Network Traffic 

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

 Discover Your Cloud Resources 

 Next 

 View You VPCs, VNets, and Applications with the Cloud Asset Map 

 Analyze Risk in Network Traffic 

 Analyze the unprotected cloud assets and the traffic flow between them. 

 Where Can I Use This? What Do I Need? 

 Cloud Asset Discovery in Strata Cloud Manager 

 Onboard and Activate a
 Cloud Account in Strata Cloud Manager 

 Analyze network traffic patterns, identify security threats, and understand
 protection coverage across your cloud infrastructure. This comprehensive view
 displays assets protected by Prisma AIRS AI Runtime firewall
 and VM-Series firewalls, including virtual machines, containers, and
 serverless workloads. 

 Use this risk analysis to prioritize your security deployments by focusing on the
 highest-risk assets first. 

 Deploy Prisma AIRS AI Runtime firewall or VM-Series to protect critical applications and vulnerable workloads
 based on their threat exposure and business impact. 

 Workload Protection Overview : Prisma AIRS AI
 Runtime firewall protects AI applications, AI models, and cloud-native applications,
 while VM-Series firewalls secure traditional enterprise applications,
 legacy workloads, and network infrastructure. 

 Log in to Strata Cloud Manager . 

 Navigate to AI Security AI Runtime Firewall . 

 Select the Operational view to analyze the bidirectional communication
 flows between users to applications, applications to the AI model, applications
 to the internet, and applications to applications. 

 Select the Security view to assess the threat landscape and deploy AI
 network intercepts as needed. 

 Risk Assessment and Prioritization 

 Use the network traffic analysis to evaluate security risks across your AI
 infrastructure and determine where to deploy Prisma AIRS AI
 Runtime firewall or VM-Series firewall. The risk analysis provides
 three complementary views to help you understand your risk landscape and make
 informed deployment decisions. 
 The following views help you to: 
 Identify high-risk assets that need immediate firewall
 deployment 

 Understand traffic patterns to configure appropriate protection
 policies 

 Prioritize your security efforts based on actual risk
 exposure 
 Review each view to understand your complete AI security posture
 management, then use the findings to deploy Prisma AIRS 
 AI Runtime firewall or VM-Series firewall protection where it will
 have the greatest impact on reducing your overall risk. 

 Models View 

 Assess east-west network traffic flow between applications and AI models.
 Deploy Prisma AIRS firewall for exposed model endpoints
 that communicate across network segments. 
 Configure AI model protection and
 AI data protection policies in your AI security profile, including prompt
 injection detection and toxic content filtering, then push the security
 policy rules to Prisma AIRS AI Runtime firewall to
 secure model inference traffic and prevent unauthorized
 access. 

 In the Operational view, click the MODELS protections icon. The
 model discovery helps you to: 

 See which applications communicate with which AI
 models. 

 Identify AI models receiving traffic from protected and
 unprotected apps. 

 View protection status, model name, and traffic
 statistics (requests, responses, protected traffic) when
 hovering over an AI model. 

 Identify and prioritize the security threats. 

 Summarize alerted model threats, such as prompt injection,
 malicious URLs, and sensitive data leakage. 

 Click on each application and model to assess how each maps and
 communicates with other assets in your network architecture. 

 Select Add Protection ("+" icon) and place Prisma AIRS firewall between AI models and
 applications. 
 Refer to Deploy Prisma AIRS AI Runtime, VM-Series, and CNGFW Firewalls for your cloud
 provider's workflow. 

 Internet View 

 Assess outbound network traffic flow from user
 applications to internet destinations. Deploy Prisma AIRS 
 AI Runtime firewall or VM-Series immediately for internet-facing
 AI applications. Configure AI application protection in your AI security
 profile, then push the security policy rules to the firewalls. Set up threat
 monitoring for all AI services receiving traffic from external
 sources. 

 Hover over and click the INTERNET protection icon to
 identify: 

 Internet-facing applications. 

 Protected and unprotected apps in your cloud
 environment. 

 Safe and unsafe internet destinations reached by the
 apps. 

 Security threats in the network flow between apps and
 the internet. 

 Threat details by clicking on each app. 

 Hover over an internet destination URL to see the IP addresses of the
 top 5 URLs accessing that destination. 

 Select Add Protection ("+" icon) and place Prisma AIRS firewall or VM-Series 
 between the internet and applications. 
 Refer to Deploy Prisma AIRS AI Runtime, VM-Series, and CNGFW Firewalls for your cloud
 provider's workflow. 

 Users View 

 Assess inbound network traffic from external
 applications to internal user applications. Deploy Prisma AIRS firewall or VM-Series 
 immediately to secure the exposed application endpoints receiving external
 traffic. Configure an AI security policy by enabling AI application protections,
 then push the security policy rule to your deployed firewall to prevent
 malicious attacks and unauthorized data access. 

 Hover over and click the USERS protection icon to: 

 Highlight unprotected traffic flows. 

 Identify the protected and unprotected apps. 

 Determine threat actors, suspicious users, and benign
 users. 

 View application threat details by clicking on each
 application. 

 Select Add Protection ("+" icon) and place Prisma AIRS firewall between users and
 applications. 
 Refer to Deploy Prisma AIRS AI Runtime, VM-Series, and CNGFW Firewalls for your cloud
 provider's workflow. 

 Application Threats Breakdown 

 Assess application threats discovery shows the
 discovered threats from both Prisma AIRS AI Runtime firewall
 and VM-Series firewall. 

 Select the Security view on the Strata Cloud Manager 
 dashboard. 

 Click on the Apps icon. This view will: 

 Group application threats under Applications , Cloud
 Providers , and Application Assets . 

 Classify applications as protected or unprotected applications,
 including metadata such as Application Asset IP address,
 Cloud Networks , Region, Cloud Provider , and
 Tags used to categorize the apps. 

 Drill down to see the network traffic flows between Apps →
 Models, Users → Apps, and Apps → Internet. 

 The application details include: 

 Firewall Serial Number : Displays the unique identifier for
 each firewall protecting your applications. 

 Firewall Type : Identifies whether protection is provided by
 Prisma AIRS AI Runtime firewall or VM-Series . 
 Network Traffic Flow Paths:
 Shows traffic flows and indicates which firewall platform
 inspects each application 

 Select Application Breakdown to view applications grouped by your
 cloud workloads, such as VMs and Pods (including containerized environments,
 Clusters, VMs, and Serverless architectures). 

 This breakdown shows applications scoped in the
 "Application definition" during Cloud account onboarding in Strata
 Cloud Manager . 

 Select the Cloud Providers tab to view the application threat
 breakdown by the cloud provider. 

 When reviewing the Application breakdown section
 on the Applications page, you might observe that the sum of VM and Pod
 applications doesn't always equal the total number of applications
 displayed at the top of the page. This is because some applications are
 categorized as both VM and Pod types, leading to their inclusion in both
 respective counts within the breakdown. 
 However, the total
 application count prominently displayed remains accurate,
 representing the unique number of applications across all types,
 without any double-counting. 

 Select the Application Assets view to analyze the threat breakdown
 based on traffic generated from interactions between endpoints and
 applications. 

 For Azure, the feature discovers Function Apps and identifies associated
 outbound IP addresses. On AWS, it discovers Lambda functions and their
 linked Elastic Network Interfaces (ENIs). This information allows you to
 understand which serverless assets are exposed to the internet versus
 which are contained within protected networks. 

 Previous 

 Discover Your Cloud Resources 

 Next 

 View You VPCs, VNets, and Applications with the Cloud Asset Map 

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
