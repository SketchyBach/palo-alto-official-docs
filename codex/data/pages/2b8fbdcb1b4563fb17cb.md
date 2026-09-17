---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-on-prem/8.12/learn-about-cortex-xsoar/cortex-xsoar-use-cases
fetched_at: 2026-09-16T08:53:53Z
source: cortex-platform
---

# Cortex XSOAR use cases | 8.12 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 8 

 Cortex XSOAR 8 On-prem Documentation 

 8.12 

 Learn about Cortex XSOAR 

 Cortex XSOAR 8.12 On-prem 

 Cortex XSOAR use cases 

 Explore recommended SOC automation use cases in Cortex XSOAR 8.12 On-prem. 

 How Automation Makes Life Easier in the SOC 

 Accelerate incident response : Replacing low-level manual tasks with automations, security automation can shave off large chunks from incident response times while improving accuracy and analyst satisfaction. 

 Standardize and scale processes : Through stepwise, replicable workflows, security automation can help standardize incident enrichment and response processes that increase the baseline quality of response and is primed for scale. 

 Unify security infrastructures : A SOAR platform like Cortex XSOAR can act as a connective fabric that runs through hitherto disparate security products, providing analysts with a central console from which to action incident response. 

 Increase analyst productivity : Since low-level tasks are automated, and processes are standardized, analysts can spend their time in more important decision-making and charting future security improvements rather than getting mired in grunt work. 

 Leverage existing investments : By automating repeatable actions and minimizing console switching, security orchestration enables teams to coordinate among multiple products easily and extract more value out of existing security investments. 

 Streamline incident handling : By applying automation to incident ticket management via integrations with key ITSM vendors such as ServiceNow, Jira, and Remedy, as well as communication tools such as Slack, security teams can speed up incident handling and closure. Incidents can also be distributed automatically to the respective stakeholders based on predefined incident types. 

 Improve overall security posture : The sum of all aforementioned benefits is an overall improvement of the organization’s security posture and a corresponding reduction in security and business risk. 

 The following examples demonstrate how to automate repetitive tasks and streamline your security incident response processes for maximum efficiency. These are tried and tested automation use cases that have been leveraged by our own Palo Alto Networks SOC, ITOps, and our customers to gain operational efficiencies and scale. 

 Phishing response 

 Phishing emails are pernicious and one of the most frequent, easily executable, and harmful security attacks organizations still face today. Responding to a phishing email involves switching between multiple screens to coordinate a response, including responding to end users. These tasks can easily take around 45 minutes of your time per incident. 

 In Cortex XSOAR phishing playbooks can help you execute repeatable tasks at machine speed, identify false positives, and prime your operations for standardized phishing responses at scale. More importantly, the quick identification and resolution of false positives gives you more time to deal with genuine phishing attacks and prevents them from slipping through the cracks. Cortex XSOAR has machine learning intelligence built in, allowing you to “train” the phishing engine to recognize future phishing attacks. 

 Workflow Automating phishing response 

 Engage 

 Cortex XSOAR can ingest suspected phishing emails as incidents from various detection sources such as SIEMs, EDRs, email security, or phishing services. If you aggregate all suspected phishing emails in a common mailbox, these emails can be ingested as incidents via a mail listener integration. 

 When the email is ingested, a playbook is triggered, going through the steps to automate enrichment and response. To keep end users updated, the playbook sends an automated email to the affected user and lets them know the suspected phishing email is being investigated. 

 Triage 

 In the triage process, the playbook can perform extraction and enrichment of indicators of compromise (IoC) extraction. 

 By investigating the email, such as title, email address, and attachments, the playbook assigns incident severity by cross-referencing these details against external threat databases. Following this, the playbook extracts IoCs from the email and checks for any reputational red flags from threat intelligence tools that your team uses. 

 When enrichment is finished, the playbook checks if any malicious indicators are found. Based on this check, different response branches can arise. 

 Respond 

 Different playbook branches execute depending on whether malicious indicators were detected in the suspected phishing email. 

 If malicious indicators are detected, the playbook sends an email to the affected user with further instructions. The playbook also scans all organizational mailboxes/endpoints to identify other instances of that email and deletes all instances to avoid further damage. Finally, the playbook adds the malicious IoCs to block lists/watchlists on the SOC’s other tools. If no malicious indicators are detected, there are still precautions to be taken before confirming that the email is harmless. The playbook checks if there are any attachments in the email that can be sent for detonation in a sandbox. 

 Threat intel analyses are then presented in an incident war room for the analyst to do a final check. Once the analyst is satisfied that the email isn’t malicious, the playbook sends an email to the affected user apprising them of the false alarm. The incident ticket is marked closed. 

 You easily eliminate 10 or more steps your security team has to touch, saving them hours responding to phishing alerts. 

 For more information, see the Phishing content pack. 

 Malware investigation and response 

 Determining if alerts for unknown activity from your endpoint security tools are malicious often involves coordinating between multiple security tools. It’s a cross-referencing nightmare with multiple consoles open simultaneously and valuable time spent performing repetitive data collection tasks. Decreasing the investigation and response time means less dwell time for malicious activity to wreak havoc in your network. 

 Automation playbooks can unify processes across SIEMs and endpoint tools in a single workflow, performing repetitive steps before bringing analysts in for important decision-making and investigative activities. 

 Workflow automating malware investigation and response 

 Query 

 An incoming endpoint security alert triggers a series of playbooks that automatically query for evidence of malice, such as: 

 Is there evidence of an attempted lateral movement? 

 Is there evidence of persistence? Did the process create any scheduled jobs? Did it write to the registry? Was Autorun updated? 

 Is the file digitally signed? 

 How did the file get onto the machine? 

 What is the process execution chain? 

 What triggered the execution of the file? 

 Was the network traffic blocked at the firewall? 

 The findings are presented in the incident for an analyst review, eliminating the need to manually collect and piece the evidence together. 

 Triage 

 Detonating suspicious files in sandboxes for malware analysis is an ever-present and important investigative step during incident response. However, it’s taxing for security analysts to coordinate across consoles while executing this repetitive task because malware analysis tools are isolated from other security products. Transferring results from one console to another for documentation is time-consuming and increases the chances of errors. 

 In this scenario, playbooks can be run concurrently to automate the file detonation process as an isolated workflow or with other enrichment activities. Playbooks can parse through the results of the sandbox detonation and be configured to run specific queries against the EDR tool. As playbooks document the result of all actions on a central console, the need for manual post-incident documentation is also eliminated. 

 Another aspect of malware analysis involves gathering forensic data, such as all the processes running on a machine, which can be automated. During an investigation, it is critical to understand what is happening on the endpoint when the alert is detected. Sometimes it can be minutes or even hours before an analyst looks at a detected alert, at which point the state of the endpoint is likely different, which makes the re-creation of what happened more challenging. These playbooks can communicate continuously with the same endpoint tools to run queries on processes, network connections, browser history, etc. to track incident status. 

 Respond 

 If the file is malicious, the playbook updates relevant watchlists/block lists with that information. From here, the playbook can branch into other actions such as quarantining infected endpoints, killing malicious processes, removing infected files, opening tickets, and reconciling data from third-party threat feeds. 

 After the queries have been run, the playbook updates the endpoint tool database with new indicator information, so repeat offenses are eliminated. 

 For more information, see the Malware Investigation and Response content pack. 

 Zero-day threat response 

 Zero-day threats and ransomware breaches are constantly in the news, such as SolarWinds SUNBURST, HAFNIUM Microsoft zero-day exploit, Nobelium threat actor, Kaseya supply chain ransomware attack, and Log4j vulnerability. 

 Every time a critical vulnerability is reported, it’s an all-hands-on-deck effort to ensure that your organization is not exposed to the potential exploits of the vulnerability. Your executive team likely has heard it in the news and needs an assessment of exposure for the organization. Speed is essential if potential malicious activity is detected. 

 Automation can help you quickly process, collect, hunt for indicators, and perform quick response actions upon finding IoCs. 

 Workflow automating zero-day threat response 

 Engage and Triage 

 In the case of a breach alert, the process of retrieving and discovering associated IoCs is as repetitive as it is important. Your analysts risk getting mired in this work while the attack continues to manifest. Isolated security tools result in a struggle to reconcile threat data across platforms to get an overall understanding of malicious activity and spread. 

 By running this playbook at the outset of incident response, your team can query endpoints, firewalls, and other incidents in seconds, avoiding wasted time that can be used towards locking down defenses. 

 Respond 

 The playbook executes initial response actions based on indicator malice. For example, the playbook can block indicators, isolate, or quarantine infected hosts, or feed malicious indicators back into threat intelligence databases and tool watchlists to avoid future attacks using the same indicators. 

 We provide specific rapid breach response playbooks for high-profile breaches to help you speed up your investigation efforts. For more information, see the Rapid Breach Response content pack. 

 Remote user access provisioning 

 Remote work has become the norm, and your business is increasingly moving to the cloud, which has increased the threat exposure and attack surface your team has to account for. 

 Automation can play a role in many areas, including aiding investigations into unsuccessful login attempts and other access violations, monitoring the health of VPNs, and updating dynamic allow/deny IP domain lists to ensure business continuity. 

 Threat Intel Management 

 As you ingest alerts, you can automatically enrich them with the latest threat intel from your feeds. This gives you context for how external and emerging threats are impacting your environment and also helps you quickly hone in on critical threats. 

 Proactive blocking of threats 

 The indicators collected from many different threat feeds need to be aggregated, normalized, scored, and prioritized before they can be pushed to enforcement points. A threat intel platform can automate these feed management functions, ensuring that your external dynamic lists (EDLs) are always up to date per the latest threats. 

 Continuous incident enrichment 

 As you investigate incidents, you need threat intel context on associated indicators. Curated threat intelligence, such as those from Unit 42 Intel threat research that comes packaged with the Threat Intel Management (TIM) module, helps you automate indicator enrichment, giving your analysts early warning and rich context into emerging threats in the wild that might be impacting your network. 

 Generating Weekly OSINT (Open Source Intelligence) and Other Threat Reports 

 Your threat intel team produces and disseminates threat intelligence reports to various business units/stakeholders to keep them up to date on the latest threats targeting their industry. Most intelligence is still shared via unstructured formats such as email and blogs, so your threat analysts may go through hours of manual work aggregating and digging for known malware families, curated news, and industry-specific threats, as well as providing analyses on why each threat is relevant to the business. Cortex XSOAR TIM provides automated workflows and a central repository for intelligence analysts to create, collaborate, and share curated intelligence reports with stakeholders. 

 External threat landscape modeling 

 Threat intelligence teams need to understand the details of attacks and how their organizations may be vulnerable. The intel team builds profiles of threat actors, identifying if there are related attacks and which techniques and tools the threat actor used. This information is shared with stakeholders, including security operations and leadership. 

 MITRE ATT&CK mapping 

 The MITRE ATT&CK framework was created to organize the real-world industry observations of threat actors into a standardized language of tactics, techniques, and procedures (TTPs) to help organizations share information and recommendations, which can be used to harden security programs. 

 Given the breadth and depth of the framework, understanding, consuming, and mapping the tactics and techniques within the MITRE ATT&CK framework into reliable and usable remediation steps can be a complicated and time-consuming task. 

 The set of playbooks in the MITRE ATT&CK - Courses of Action content pack helps you automatically map your incident response to MITRE ATT&CK techniques and sub-techniques in an organized and automated manner, which ensures your organization not only blocks specific reported IoCs but also takes a more holistic approach to preventing future attacks. With Cortex XSOAR, you can leverage prebuilt automation playbooks to cross-reference every incident with the tactics and techniques of the MITRE ATT&CK framework. 

 This content pack provides manual or automated remediation of MITRE ATT&CK techniques and kill chain. Security analysts choose the techniques relevant to their security program and run the prebuilt playbooks that leverage expert remediation workflows. This can be found in the built-in MITRE ATT&CK dashboard. 

 Cloud security incident response 

 In cloud security, there are many infrastructures and products to deal with. The security of your cloud is often a shared responsibility between you, your cloud service provider, and other teams. Cloud SecOps teams report that cloud security incidents are treated on a case-by-case basis, and the remediation process is high-touch and manual. There is often no correlation between cloud platforms and on-premises security. 

 Cortex XSOAR can unify processes across multi-cloud and on-premises security infrastructures, providing your security teams with a single console to execute the incident response. We also integrate with cloud-based identity management tools, enabling role-based and keyless deployment of services without the need for credential management. 

 Cloud threat detection 

 With the move towards digital currency and the acceptance of cryptocurrency for financial transactions, cryptojacking isn't declining anytime soon. 

 For example, you may automate a response to a cryptomining alert. Cortex XSOAR can ingest cloud security alerts from AWS, Google Cloud, Microsoft Azure, or Cortex Cloud to fully or partially automate incident response. 

 Extract 

 The playbook extracts indicators (IPs, URLs, hashes, and so on) from the incident data. It can also open a ticket for the incident. 

 Enrich 

 The playbook enriches indicators with reputation data from threat intelligence tools that the SOC uses. It also enriches the ingested data with additional context from SIEMs and other non-cloud-based event management tools to identify the full extent of the suspected attack. The playbook checks if the indicators are identified as malicious. 

 Respond 

 The playbook obtains the instance and security group details and security group details, takes volume snapshots, and creates a tag for the EC2 instance to be isolated. These steps are classic digital incident response and forensics actions, but carried out in the cloud. What we are doing is moving the EC2 instance into a separate virtual PC (VPC) as we would on a virtual LAN (VLAN) in the on-premises world, getting a list of running processes, analyzing the results, and also sending an email to the analyst for review. 

 If the indicators are not identified as malicious, the playbook can ask a security analyst to review the information and verify that it’s not dangerous before closing the incident as a false positive. 

 Automation cuts analyst time and increases responses by eliminating manual tasks, inter-team coordination, and security product changes. Also, you can enforce standard operating procedures across different teams for cloud security incident response. Other automation use cases include automating incident response for common cloud security incidents like password and security group misconfigurations, access key compromises, unpatched vulnerabilities, and unusual activity like port scans/port sweeps. View more automation content packs in Marketplace . 

 Vulnerability Management 

 Vulnerability management is a strategically important process that covers both the proactive and reactive aspects of security operations. Since vulnerability management encompasses all computing and internet-facing assets, security teams often grapple unsuccessfully with correlating data across environments, spending too much time unifying context and not enough time remediating the vulnerability. 

 Security orchestration playbooks can automate enrichment and context addition for vulnerabilities before passing them to the appropriate teams for patch remediation. This maintains a balance between automated and manual processes by ensuring that analyst time is not spent executing repetitive tasks but on making critical decisions and drawing inferences. 

 Extract 

 The playbook ingests asset and vulnerability information from a vulnerability management tool such as Tenable or Qualys. The related information from the incident is extracted, and related indicators are created and enriched. 

 The playbook then enriches endpoint and CVE data through relevant tools. It also adds custom fields to the incident if the newly gathered data requires them. 

 To provide the analyst with a richer vulnerability context, the playbook queries the vulnerability management tool for any diagnoses, consequences, and remediations tied to the vulnerability. If any vulnerability context is found, it’s added to the incident data. Based on the gathered context, the playbook then calculates the severity of the incident. 

 Remediate 

 Playbooks can also use vulnerabilities to inform threat priority and initiate the patching process. Response actions can be taken by playbooks, including: 

 Checking if assets (IP, domain, or certificate) associated with the issue are excluded in the exclusions list and closing the incident automatically. 

 Enriching indicators and calculating the severity of the issue. 

 Adding associated assets (IP, domain, or certificate) to the exclusions list. 

 Tagging associated assets and updating the status of the issue. 

 The playbook now hands over control to the security analyst for manual investigation and remediation of the vulnerability. 

 Attack surface management 

 Vulnerability scanners are great for monitoring your known assets, but what about your unknown assets? To uncover these blind spots, your organization needs an automated attack surface management (ASM) solution like Cortex Xpanse that continuously discovers and monitors the entirety of IPv4 space to provide a complete and accurate inventory of your global internet-facing assets and misconfigurations. 

 Together with Cortex XSOAR, Xpanse enables you to automate the identification and remediation of web-facing exposures to reduce your mean time to detect and respond (MTTD and MTTR). 

 The integration enables the fetching and mirroring of Xpanse issues into Cortex XSOAR incidents as well as the ingestion of indicators (IPs, domains, and certificates), referring to the corporate network perimeter as discovered by Xpanse. Leveraging both technologies, your security team can respond to asset vulnerabilities and incidents with automated orchestration playbooks. You can trigger scans to enrich incidents and automatically generate tickets for on-premises and cloud assets. 

 Discover 

 Scan the internet and accurately attribute unknown assets using multiple sources to reduce false positives and map your full attack surface. 

 Enrich 

 Use automated playbooks to enrich incidents using Xpanse asset information and threat intelligence indicators, helping you reduce MTTD and MTTR across your cloud native, hybrid, and on-premises environments. 

 Remediate 

 Improve your team’s efficiency with a host of integrations and prebuilt scripts to automate attack surface management. For more details, see the Cortex Xpanse content pack. 

 Network operations automation 

 In this use case, we will pivot from the SOC to the NOC. A flexible and scalable SOAR platform can be applied to any workflow or process, and our own Palo Alto Networks operations teams are using Cortex XSOAR internally to automate their manual processes. 

 One area where we have seen great benefits is network operations, where manual but necessary tasks are a time burden for the ITOps and NetOps teams. 

 Manual Firewall Device Onboarding and Upgrades 

 It’s a tedious and manual process to upgrade and validate all firewalls distributed across your network. There is significant time investment needed in the process where your team needs to download the firewall update, install, reboot, and verify that the upgrade was successful. For enterprises with over 100 firewalls distributed across their organization, this process is not scalable and is done infrequently. 

 “We manage about 450 firewalls. It takes us two hours to upgrade each firewall. We can only do a few at a time to ensure everything upgrades correctly.” – Insurance industry customer 

 With Cortex XSOAR, you can onboard and upgrade all your devices within the environment and automatically verify upgrade status. There is still time required to download and reboot the system, but your NetOps team no longer has to “babysit” the process. Snapshots of the configuration can be captured to enable rollbacks if necessary. Once the upgrade is complete, verification steps can be performed to ensure the firewall is functioning properly. 

 There are many more automation use cases that can be deployed to streamline network operations, from policy and rule change management to monitoring network health and outages, but your NetOps teams will derive great efficiency benefits just from starting their automation journey with this key use case. 

 Previous Cortex XSOAR architecture 

 Next Understand Cortex XSOAR licenses 

 Last updated 1 month ago 

 Was this helpful?
