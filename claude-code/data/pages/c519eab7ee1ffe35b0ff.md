---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-5.x-rn/release-information/features-introduced-in-2025-xdr-4x/november-2025/feature-enhancements
fetched_at: 2026-09-06T10:52:54Z
source: cortex-platform
---

# Feature Enhancements | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Release Notes 

 Cortex XDR 

 Cortex XDR 5.x 

 Release Information 

 Features Introduced in 2025 

 November 2025 

 Feature Enhancements 

 General 

 Feature 

 Description 

 AgentiX AI Agent Workforce 

 Cortex Agentic Assistant: Go beyond rigid playbooks and command autonomous agents based on over 1.2 billion real-world playbook executions and governed by robust guardrails, to dynamically plan, reason and take action to solve any security challenge. For more information, see Cortex Agentic Assistant . 

 Cortex Agentic Assistant is included in Cortex XDR with a Cloud Runtime Security or Cloud Posture Security license, and is available in supported regions. 

 Expanded Asset Group scoping 

 Scope-Based Access Control (SBAC) has been enhanced to provide more granular control over your access policies. You can now define Asset Groups that include the Business Application Names attribute for scoping definitions. 

 API 

 Feature 

 Description 

 User and role APIs 

 These new APIs enable you to manage user roles, update API keys, and add or remove role and scope assignments for users, which gives greater flexibility to automate and scale your user management workflows. 

 Automations 

 Feature 

 Description 

 Install content from Marketplace 

 You can now browse and install content packs directly from Marketplace, which provides improved visibility into all available content. This allows you to easily discover and install the right content packs to fit your specific security workflows. 

 Dismiss alerts for non-configured playbook components 

 When setting up playbooks, you can now dismiss alerts for components you don't need, such as specific sub-playbooks, scripts, and commands. Alerts can be dismissed in both system and custom playbooks, and you do not need to edit or duplicate a system playbook to dismiss an alert. This enables you to reduce visual noise, making it easier to focus on the tasks that require configuration. 

 Unique task logos 

 Boost clarity and quickly distinguish between integration commands, custom scripts, and system actions with playbooks that display unique logos and content pack indicators. 

 Streamlined playbook development with drag-and-drop functionality 

 Streamline your playbook development by using drag-and-drop to build automation flows. This enables you to create and organize your playbooks faster by simply dragging tasks from the side panel directly onto the canvas. 

 AI Script Generator 

 Generate high-quality Python scripts quickly and efficiently with the AI Script Generator. It's built-in testing panel lets you validate and refine the code generated from natural language, ensuring accuracy and significantly reducing the time spent on manual development. 

 Choose an integration instance for Quick Actions 

 When running a Quick Action on demand or as part of an automation rule, you can now select a specific integration instance to use, enabling a more efficient and targeted response. 

 Automation Exclusion Center enhancements 

 The automation exclusion center now allows for more dynamic and flexible policies: 

 Hard user remediation and soft user remediation automation exclusion policies can now reference asset groups. User accounts are automatically categorized into asset groups, eliminating the need for manual list updates and ensuring that automation exclusion policies remain up-to-date. 

 Reference multiple lists and asset groups in the same policy, providing maximum flexibility. 

 New role permissions enable you to allow non-admin users the ability to view or edit policies in the Automation Exclusion Center. Admins can delegate policy management to non-admin users without granting full admin-level system access, giving admins more time to focus on other critical responsibilities. 

 Automation Exclusion policy overrides provide greater control and responsiveness. You can now permit policy overrides on specific automation exclusion policies, enabling analysts to run commands on critical assets as needed. You can also configure policies without overrides, providing a balance of security and operational flexibility. 

 With RBAC for lists, you can now define one or more roles that can view or edit a list, mitigating the risk of unauthorized or accidental changes to lists of critical assets. 

 New condition-based policies offer more versatility and precision for enforcing automation exclusions. You can now use lists with dynamic matching operators, such as starts with, ends with, and doesn’t include. Dynamic matching operators allow you to apply automation exclusion policies to entire naming patterns, such as regional endpoints or internal domains, simplifying management and improving coverage. 

 Broker VM 

 Version 29.0.71 (reboot required) 

 For more information on maintenance releases, see Maintenance releases 

 Feature 

 Description 

 Enhanced error visibility and auditing for additional Broker VM applets 

 Gain better insight into application, connectivity, and processing errors for the FTP Collector, Netflow Collector, Network Mapper, and Apache Kafka collector applets running on Broker VMs. Error messages are displayed on Apps of Broker VMs and Clusters, and applet status changes are logged in the collection_auditing dataset, enabling detailed investigations through XQL queries. 

 Broker VM support for Spain’s Esquema Nacional de Seguridad (ENS) National Security Framework 

 The Broker VM has been updated to comply with Spain’s Esquema Nacional de Seguridad (ENS) National Security Framework. You must enable the option Only use recommended cipher suites to meet the ENS regulation. This new setting is located in the Advanced Settings section, which you can access when configuring the Broker VM using its URL. 

 Enhanced Database Collector 

 The Database Collector applet now has a new Storage Method option, which offers more control over how the data is handled: 

 Append: This method adds new data to an existing dataset as this worked previously by default. 

 Replace: This new method is only available for Snapshot datasets and overwrites the entire dataset with the newly collected data. This is necessary when the data that needs to be collected from the database is static data or reference data, such as a list of computers, IP addresses, or a list of users. 

 Cortex Query Language (XQL) 

 Feature 

 Description 

 Enhanced XQL query monitoring and governance 

 Introducing significant updates to XQL query management that deliver a more responsive, holistic, and powerful Query Center experience. Key enhancements: 

 Improved performance: Experience faster and more responsive page load and filtering times in the Query Center. 

 Real-time tracking and management: Get full visibility into active queries across your tenant, with the power to instantly cancel running queries. 

 Expanded query coverage: Monitor queries from all XQL query sources, including Dashboards with XQL widgets, Correlation rules, BIOC rules, and more. 

 Administrator governance: Prevent resource strain and optimize tenant performance by setting query limits for all users. 

 New default query limit: To prevent long-running queries and ensure optimal tenant performance, queries will automatically stop after 60 minutes. (This value can be overridden using the max_runtime_minutes command.) 

 Updated query retention: Query retention is now aligned with issue retention. 

 Lookup datasets enhancement 

 Cortex XDR has implemented a fix to improve lookup dataset queries and provide better flexibility in managing your data. Now, when you create or add data to a lookup dataset using the target stage, the _time field won't be included by default unless you explicitly add it with the fields stage. 

 Detection rules 

 Feature 

 Description 

 New and improved Analytics tags 

 New analytics suites: 

 EDR Windows Disguised Processes: A novel analytics detection suite designed to detect Windows process masquerading techniques and their diverse sub-techniques, such as common process name impersonation and renaming of legitimate system utilities by attackers. The suite achieves this through its comprehensive analytic capabilities, featuring dynamic baselines and anomaly scoring. 

 EDR Linux Credential Grabbing: A behavior-based analytics detection suite to identify uncommon access to sensitive files that are frequently targeted for credential discovery. The suite monitors processes interacting with files such as SSH private keys, password and group files, shell history, and other configuration artifacts commonly used to store credentials. By analyzing access patterns across environments, the detector suite highlights rare or anomalous behavior, helping uncover otherwise unnoticed credential-harvesting activity. 

 EDR macOS Generic Persistence: An innovative analytics detection suite tailored to the macOS domain to detect unusual activities to secure persistent foothold and execution in macOS endpoints. This suite highlights abused persistence mechanisms and support the hunt for novel persistence techniques, commonly leveraged by macOS infostealers and APTs. 

 Microsoft Teams Analytics: An advanced analytics suite for detecting attack attempts within Microsoft Teams. The suite uncovers a broad range of different sub-techniques, such as phishing, malicious link sharing in chats, unauthorized policy modification, malicious application installation, and data collection. The suite uses dynamic baselines and anomaly scoring to provide comprehensive analytics, identifying abnormal user and communication patterns. 

 Improved analytics tags: 

 DLL Hijacking Analytics: We've expanded and improved our coverage for DLL Hijacking techniques. Using advanced analytic capabilities, we significantly enhanced detection logic for important threats, including Microsoft process hijacking and DLL sideloading. 

 Email Security 

 Feature 

 Description 

 New Advanced Email Security response engine 

 A lightweight, real-time remediation engine enabling automated, policy-driven actions to quickly respond to email threats before they manifest. All remediation actions initiated by automatic policies are tracked in the Remediation Action Center, where you can review the emails and actions taken. 

 This feature requires an Email Security Module add-on. 

 Endpoint Security 

 Feature 

 Description 

 File examination on-load for macOS 

 Detect and prevent execution of malicious Mach-O files when loaded on macOS-based endpoints, using this new Cortex XDR agent capability. 

 Child Process Protection for Linux 

 Cortex XDR introduces an additional prevention module for Linux (in KM mode) that examines the relations between parent and child processes to detect suspicious relations. This module provides improved detection and protection coverage capabilities. 

 CaaS distribution 

 Cortex XDR now supports Google Kubernetes Engine (GKE) Autopilot. 

 External Data Ingestion and Management 

 Feature 

 Description 

 Unified integration error notifications 

 Instead of being inundated with multiple notifications, all data collector errors are now grouped into a single notification. This new, non-dismissible notification alerts all users to data source integration errors. 

 Investigation and response 

 Feature 

 Description 

 Cortex MCP Server 

 This feature is currently in Beta . 

 The Cortex MCP Server enables seamless integration between Cortex XDR and your preferred Large Language Model (LLM) applications. Built on the Model Context Protocol (MCP), a new standard for connecting AI models with external tools, it allows you to leverage Cortex XDR’s powerful capabilities directly through natural language. Use the built-in tools to manage cases, handle issues, and conduct investigations, with the flexibility to create, customize, and fine-tune tools to fit specific use cases and workflows. 

 XDR Collectors 

 XDR Collectors 1.5.1: Windows 1.5.1.2048 and Linux 1.5.1.1950 

 XDR Collectors 1.4.3: Windows 1.4.3.1686 

 For more information on maintenance releases, see Maintenance releases 

 Feature 

 Description 

 Enhanced visibility and auditing of XDR Collectors 

 Cortex XDR now provides enhanced error visibility and auditing for XDR Collectors. This enables you to quickly identify and resolve application, connectivity, and processing errors, simplifying troubleshooting and ensuring your critical workflows remain uninterrupted. 

 Previous Release Highlights 

 Next Changed Features 

 Last updated 16 days ago 

 Was this helpful?
