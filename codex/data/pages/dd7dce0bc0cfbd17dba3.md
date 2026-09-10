---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-on-prem/8.7/configure-cortex-xsoar/playbooks/debug-your-playbook/troubleshoot-playbook-performance
fetched_at: 2026-09-06T11:27:14Z
source: cortex-platform
---

# Troubleshoot playbook performance | 8.7 (EoL) | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 8 

 Cortex XSOAR 8 On-prem Documentation 

 8.7 (EoL) 

 Configure Cortex XSOAR 

 Playbooks 

 Debug your playbook 

 Cortex XSOAR 8.7 On-prem EoL 

 Troubleshoot playbook performance 

 Troubleshoot playbook performance in Cortex XSOAR On-prem 8.7 (EoL). 

 You can analyze playbook metadata such as tasks input and output, the amount of storage each task input/output uses, and the type of task. This is useful when troubleshooting your custom playbook if your system has slowed down and is using high CPU usage, memory, or storage (disk space). 

 After an incident has been assigned to a playbook you can analyze it to see its tasks inputs/outputs storage. You can filter the data according to the KB used in each task input/output. 

 From the Incidents page, in the Incident War Room , run the following command in the CLI. 

 !getInvPlaybookMetaData incidentId= <incident ID> `` ``minSize= <size of the data you want to return in KB. Default is 10> 

 Example 21. 

 To view the playbook metadata that is used in incident number 964, in the CLI type !getInvPlaybookMetaData incidentid=”964” minSize=”0”!getInvPlaybookMetaData incidentid=”964” minSize=”0”. 

 Previous Debug your playbook 

 Next Manage playbook content 

 Last updated 4 days ago 

 Was this helpful?
