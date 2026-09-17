---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/logging/appsec-pan-8
fetched_at: 2026-09-16T09:09:17Z
source: cortex-platform
---

# Security policies missing descriptions in Palo Alto Networks devices misconfiguration detected in co | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Logging 

 Security policies missing descriptions in Palo Alto Networks devices misconfiguration detected in co 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_PAN_8 

 Category - Subcategory 

 Public Exposure - Ingress Controls 

 Provider 

 OTHER 

 Severity 

 LOW 

 Framework 

 Ansible 

 Impact 

 This rule ensures that all security policies in Palo Alto Networks devices have a populated 'description' field. Descriptions are essential for providing context and understanding the purpose of each security rule, facilitating easier management and auditing of security policies. This check verifies that the description attribute in panos_security_rule resources is not empty, promoting better documentation and clarity in security rule definitions. 

 How to Fix 

 Palo Alto Networks 

 Resource: panos_security_rule 

 Attribute: description 

 To mitigate this issue, ensure that every panos_security_rule resource contains a descriptive description attribute. This description should offer clear and concise information about the rule’s purpose, facilitating effective management and documentation of security policies. 

 Secure Code Example: 

 Ask Copy 

 - name : Example 
 tasks : 
 - name : Example 
 paloaltonetworks.panos.panos_security_rule : 
 ... 
 + description : " Block traffic from untrusted zones to critical servers " 

 In this example, including meaningful descriptions in your security rules clarity and manageability of your security policies. 

 Previous The --audit-log-maxsize argument is not set appropriately misconfiguration detected in code 

 Next Log Forwarding Profile not selected for a Palo Alto Networks device security policy rule misconfigur 

 Last updated 1 month ago 

 Was this helpful?
