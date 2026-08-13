---
url: https://docs.paloaltonetworks.com/best-practices/security-policy-best-practices/security-policy-best-practices/maintain-security-policy-best-practices
fetched_at: 2026-08-13T15:33:02Z
source: palo-alto-main
---

# Maintain Security Policy Best Practices Clear

Maintain Security Policy Best Practices 

 Home 

 EN

 Location 

 Documentation Home 

 Palo Alto Networks 

 Support 

 Live Community 

 Knowledge Base 

 Strata Copilot

 Security Policy Best Practices 

 : 
 Maintain Security Policy Best Practices 

 Updated on 

 Apr 4, 2024 

 Focus 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Filter

 Expand all | Collapse all 

 Security Policy Best Practices 

 Plan Security Policy Best Practices 

 Deploy Security Policy Best Practices 

 Security Policy Rule Best Practices 

 Security Policy Rulebase Best Practices 

 Policy Optimizer Best Practices 

 App-ID Cloud Engine Best Practices 

 Policy Recommendation Best Practices 

 Maintain Security Policy Best Practices 

 Updated on 

 Apr 4, 2024 

 Focus 

 Home 

 Best Practices 

 Security Policy Best Practices 

 Security Policy Best Practices 

 Maintain Security Policy Best Practices 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Security Policy Best Practices 

 Maintain Security Policy Best Practices 

 Table of Contents 

 Filter

 Expand all | Collapse all 

 Security Policy Best Practices 

 Plan Security Policy Best Practices 

 Deploy Security Policy Best Practices 

 Security Policy Rule Best Practices 

 Security Policy Rulebase Best Practices 

 Policy Optimizer Best Practices 

 App-ID Cloud Engine Best Practices 

 Policy Recommendation Best Practices 

 Maintain Security Policy Best Practices 

 Maintain Security Policy Best Practices 

 Maintain your best practices Security policy deployment in PAN-OS and Prisma Access . 

 After you plan and deploy Security policy best practices, maintain your best
 practice deployment as your network and its applications, users, devices, and
 infrastructure change. 

 Keep all security subscriptions current to avoid gaps in coverage. 

 Keep up with Applications and Threats content updates and follow best practices for Applications and Threats
 content updates . 

 Review Release notes for the latest features,
 changes to default behavior, issues, etc. 

 Create daily, weekly, monthly (and any other period you need) maintenance
 checklists. 

 Security policy deployment maintenance is a recursive task because new
 applications, users, and IoT devices are continuously added to and deleted
 from your environment as things change over time. For example, checklists
 can include: 

 Evaluating Applications and Threats content updates. 

 Using Policy Optimizer for managing applications. 

 Reviewing IoT and SaaS policy recommendations and updates. The
 posture of IoT devices may change over time and SaaS applications
 used may change over time or need to be treated differently and
 require updating. Keep sanctioned/tolerated/unsanctioned tags for
 applications updated. 

 Setting times to run Security posture
 analysis tools . 

 Reviewing behavior changes and issues documented in the release
 notes. 

 Reviewing Security policy rules to see if you can tighten them or if
 they are no longer needed. 

 Maintain App-ID in Security policy: 

 Review new and modified content-delivered App-IDs and adjust rules as
 necessary. 

 As you add new applications to your network, include them in
 specific, granular policy rules. Use tags and application filters to
 automate adding sanctioned applications, including new App-ID Cloud
 Engine applications, to rules. 

 When your company stops using an application, remove it from allow
 rules to prevent unauthorized use. 

 Regularly review the applications your Security policy rules
 allow. 

 Maintain User-ID in Security policy: 

 As you add new users to your network, add them to the appropriate
 user groups to control their access and include them in policy, or
 add them directly to rules if they belong to no group. 

 As users leave the company or as their contracts end, remove them
 from user groups to prevent access. Remove individuals from rules if
 they weren't added as part of a group. 

 Continue to follow best practices for user group
 mapping and best practices for dynamic user
 groups (DUGs) as you add and remove users from groups and
 policy rules. 

 Maintain and update Security profiles and profile groups as your network and
 goals evolve. When you add new allow rules, ensure that they have the
 appropriate Security profiles attached. 

 Update Log Forwarding as needed as for new rules and applications: 

 Apply an appropriate Log Forwarding profile to every new Security
 policy rule or use a default Log Forwarding profile to automatically
 apply a Log Forwarding profile to new rules. If you use a default
 profile, check the rule to ensure that the default profile is
 appropriate and if not, replace it with an appropriate profile. 

 Periodically review what you’re logging and what you’re not logging and
 how you’re logging it. Ensure that you’re logging the traffic you want
 to log and logging all the information you want to log for Security
 Operating Center (SOC) operations. 

 Update log forwarding profiles as administrators join and leave the
 company. 

 As new applications come into your network, update Log Forwarding to
 accommodate them. 

 Use security posture analysis tools to check your best practices
 deployment: 

 In PAN-OS and Prisma Access , use Strata Cloud Manager to
 check Security policy as you create it. 

 Periodically run the Strata Cloud Manager on-demand Best Practices
 Assessment (BPA) to measure progress toward a best
 practices deployment. 

 Run the Security Lifecyle review
 (SLR) quarterly to get a better view into your
 network. 

 Use firewall tools to check activity and adjust Security policy as
 needed. 

 Use log information in PAN-OS (also applies to
 Panorama Managed
Prisma Access ) and Strata Cloud Manager Managed Prisma Access to
 investigate and monitor traffic. 

 Use the Application Command Center 
 to see graphical summaries of applications, users, threats, URLs,
 and content that traverses your network. 

 Use App Scope reports to help
 understand changes in application usage and user activity, bandwidth
 usage, and network threats. 

 Create Custom reports to view the
 exact data you want to investigate. 

 Check Policy Optimizer regularly to examine the
 rulebase and find and fix unused rules, over-provisioned rules, and rules with
 unused applications. Add checking Policy Optimizer to your regularly scheduled
 maintenance. 

 Use SecOps tools and services to monitor your entire security posture
 proactively, help prevent threats, and investigate issues: 

 Cortex XSIAM combines SOC
 analytics for proactive monitoring with SIEM capabilities. 

 Cortex XSOAR provides
 comprehensive security orchestration, automation, and
 response,including response playbooks, for comprehensive threat
 intelligence management and real-time collaboration. 

 Cortex XDR provides an
 extended detection and response platform that monitors and manages
 cloud, network, and endpoint events and data. 

 SOC Services such as
 SecOps Prevention Posture Assessment, optimization, and learning
 workshops. 

 The following resources provide more information about Palo Alto Networks
 platforms, features, and support: 

 The Security Best Practices
 Documentation Portal contains standalone books such as
 IoT Security Best
 Practices , Administrative Access Best
 Practices , and Decryption Best Practices ,
 and links to best practices topics in various administrator's
 guides. 

 Administrator's Guides: 

 PAN-OS Administrator's
 Guide 

 Prisma Access ( Panorama Managed
Prisma Access and
 Strata Cloud Manager Managed Prisma Access ) 

 SaaS Security
 Administrator’s Guide 

 IoT Security
 Administrator's Guide 

 Documentation Portals: 

 Cloud Delivered Security
 Services (CDSS) documentation portal 

 Cloud Identity Engine
 (CIE) documentation portal 

 GlobalProtect
 documentation portal 

 Palo Alto Networks
 Customer Support Portal 

 Monitor Your IoT Security
 Deployment Using Best Practices 

 IoT Security Solution
 Structure (summary of how the IoT Security solution
 works) 

 SaaS Security on ( Panorama Managed
Prisma Access and Strata Cloud Manager Managed Prisma Access ) 

 Troubleshoot issues on SaaS
 Security Inline 

 Previous 

 Policy Recommendation Best Practices 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
