---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-on-prem/8.10/multi-tenant/multi-tenant/onboard-cortex-xsoar-multi-tenant/step-5.-install-and-configure-content
fetched_at: 2026-09-16T08:55:20Z
source: cortex-platform
---

# Step 5. Install and configure content | 8.10 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 8 

 Cortex XSOAR 8 On-prem Documentation 

 8.10 

 Multi-Tenant 

 Multi-tenant 

 Onboard Cortex XSOAR multi-tenant 

 Cortex XSOAR 8.10 On-prem 

 Step 5. Install and configure content 

 Install content for multi-tenant deployments in Cortex XSOAR 8.10 On-prem. 

 In Cortex XSOAR, content includes the following: 

 Content 

 Description 

 Integrations 

 Third-party tools and services that the Cortex XSOAR platform works with to orchestrate and automate SOC operations. You can trigger events from these integrations that become incidents in Cortex XSOAR. After the incidents are created, you can run playbooks on these incidents to enrich them with information from other products in your system. 

 Playbooks 

 You can automate many security processes, including handling investigations and managing tickets and security responses that were previously handled manually. Playbooks enable you to organize and document security monitoring, orchestration, and response activities. When an incident is ingested, if a playbook runs, an incident is created. 

 Dashboards, reports, and widgets 

 Dashboards and reports consist of visualized data powered by fully customizable widgets, which enable you to analyze data from inside or outside Cortex XSOAR in different formats such as graphs, pie charts, or text. Reports allow you to share similar data outside of Cortex XSOAR via email. Reports can be scheduled to run at a specific time to capture data where the start/end time is important. 

 Classifiers and mappers 

 Classification determines the type of incident/indicator that is created for events ingested from a specific integration. You create a classifier and define that classifier in an integration. Mappers map the fields from your third-party integration to the fields that you defined in your incident/indicator layouts. 

 Incident types, fields, and layouts 

 All incidents that are ingested into Cortex XSOAR are assigned an incident type when they are classified. Each incident type has a unique set of data that is relevant to that specific incident type. Fields and layouts ensure that you see relevant information that is relevant to the incident type. 

 Indicator types, fields. and layouts 

 Indicators are categorized by indicator type, which determines the indicator layout and fields that are displayed and which scripts are run on indicators of that type. 

 Scripts 

 Perform a specific action, and are comprised of commands associated with an integration. Write scripts in either Python or JavaScript. Scripts are used as part of tasks, which are used in playbooks and commands in the War Room. 

 Content is organized into content packs to support specific security orchestration use cases, which are either preinstalled or downloaded from Marketplace. Content packs are created by Palo Alto Networks, technology partners, contributors, and customers. 

 After downloading and installing content packs, you can then start customizing the content to suit your use case. For example, although Cortex XSOAR comes with a Mail Sender integration already configured, you may want to set up your Mail Sender integration, such as EWS. 

 Further information 

 To install content packs, see Install content packs . 

 To set up your use case using the deployment wizard, see Set up your use case with the Deployment Wizard . 

 Marketplace, see Cortex Marketplace . 

 For Post-deployment steps, see Post deployment . 

 Previous Step 4. Set up users and roles 

 Next Child tenant management 

 Last updated 9 days ago 

 Was this helpful?
