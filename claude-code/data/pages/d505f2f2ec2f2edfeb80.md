---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam-developer-guide/cortex-xsiam-development-guide/integrations-and-scripts/developing/context-standards
fetched_at: 2026-09-16T09:04:48Z
source: cortex-platform
---

# Context standards | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Developer Docs 

 Cortex XSIAM Developer Guide 

 Cortex XSIAM Development Guide 

 Integrations and scripts 

 Developing 

 Context standards 

 Cortex XSIAM standards for structuring incident context data. 

 Cortex XSIAM organizes incident data in a tree of objects called the incident context. Any integration commands or scripts that run add data into the context at a predefined location. This also applies to commands that run within playbook execution. 

 The context stores the results from every integration command and every automation script that runs. It is a JSON storage for each incident. Whether you run an integration command from the CLI or from a playbook task, the output result is stored into the JSON context in the incident or the playground. For example, a command like !whois query="cnn.com" returns the data and store the results into the context. 

 When building new integrations the entry context should be returned according to this standard in addition to the vendor specific context. 

 The structure should be: 

 Ask Copy 

   { 
  "Object": { 
    ... 
  }, 
  "Vendor": { 
    "Object": { 
      ... 
    } 
  } 

 } 

 Some standard objects are mandatory and enforced in the code, and some are recommended . 

 Mandatory Cortex XSIAM context standards 

 There are standard context schema used for the system indicators and the DBot Score object. You do not need to manually output this in your code, instead, use the builtin classes as described in context use cases . 

 File 

 The following is the format for a File. File here refers to the file indicator or a binary file that could potentially be malicious, and might be checked for reputation or sent to a sandbox. 

 In YAML 

 IP 

 The following is the format for an IP entity: 

 In YAML 

 Endpoint 

 The following is the format for an Endpoint: 

 In YAML 

 Email Object 

 The following is the format for an Email Object: 

 In YAML 

 Domain 

 The following is the format for a Domain. Please note that for WHOIS, the entity is a dictionary nested for the key "WHOIS". 

 In YAML 

 URL 

 The following is the format for a URL entity: 

 In YAML 

 CVE 

 The following is the format for a CVE: 

 In YAML 

 Rule 

 The following is the format for a Rule: 

 In YAML: 

 DBot Score 

 The following is the format for a DBot Score entry: 

 In YAML 

 Certificate 

 The following is the format for an X509 certificate: 

 In YAML 

 Recommended Cortex XSIAM context standards 

 The following are examples of how each entity should be formed in the entry context. 

 Ticket 

 In YAML 

 Account 

 In YAML 

 Registry Key 

 In YAML 

 Event 

 In YAML 

 Service 

 In YAML 

 Process 

 In YAML 

 Previous Context and outputs 

 Next Generic commands 

 Last updated 19 days ago 

 Was this helpful?
