---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-on-prem/8.6/configure-cortex-xsoar/lists/transform-a-list-into-an-array
fetched_at: 2026-09-16T09:13:46Z
source: cortex-platform
---

# Transform a list into an array | 8.6 (EoL) | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 8 

 Cortex XSOAR 8 On-prem Documentation 

 8.6 (EoL) 

 Configure Cortex XSOAR 

 Lists 

 8.6 On-prem Cortex XSOAR EoL 

 Transform a list into an array 

 Transform lists into arrays in Cortex XSOAR On-prem 8.6 (EoL). 

 Create a transformer to split a list into an array, add or edit a task in a playbook, or map an instance. 

 Go to Playbooks and create or edit a playbook. 

 Select Create Task . 

 In the Choose script field, select the Set automation. 

 In the Key field, enter the key name. 

 In the value field, click {} 

 Add a transformer. 

 Click Filters And Transformers . 

 In the Get field, click {} . 

 Expand the Lists node and select a list to transform. 

 In Apply transformers on the field , click Add transformer . 

 Search for and select Split . 

 (Optional) In the delimiter field, type the delimiter used to separate the items in the string (default is ","). 

 Click Save . 

 Save the task and playbook. 

 For an example of using a transformer in a list, see Apply Transformers to Extracted Data . 

 Previous Use cases: JSON lists 

 Next Jobs 

 Last updated 2 months ago 

 Was this helpful?
