---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-on-prem/8.11/configure-cortex-xsoar/playbooks/customize-your-playbook/filter-and-transform-data/transformer-considerations-categories-and-built-in-transformers
fetched_at: 2026-09-16T08:54:40Z
source: cortex-platform
---

# Transformer considerations, categories, and built-in transformers | 8.11 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 8 

 Cortex XSOAR 8 On-prem Documentation 

 8.11 

 Configure Cortex XSOAR 

 Playbooks 

 Customize your playbook 

 Filter and transform data 

 Cortex XSOAR 8.11 On-prem 

 Transformer considerations, categories, and built-in transformers 

 Use transformers in Cortex XSOAR 8.11 On-prem. 

 You can use built-in transformers to define your transformer;, they are grouped by category. Before defining a transformer, consider the following. 

 Transformer considerations 

 Transformers try to cast the transformed value (and arguments) to the necessary type. Tasks will fail if casting has failed, for example {“some”: “object”} To upper case => Error . 

 Some transformers are applied on each item of the result. For example, a, b, c To upper case => A, B, C . 

 Some transformers operate on the entire list. For example, a, b, c count => 3 . 

 Some custom transformers are implemented as scripts with the transformer tag. You can find examples in the playbook automation task description. 

 Transformer categories and built-in transformers 

 When adding a transformer, clicking the default To upper case (String) field opens a search window showing the available built-in transformers. They are defined by category as follows. 

 Transformer category 

 Description 

 Built-in transformers 

 General 

 Generic transformers 

 FIXME_ACCORDION_PLACEHOLDER 

 String 

 String transformers 

 Note 

 To make regex case non-sensitive, use the (?i) prefix (for example (?i)yourRegexText . 

 FIXME_ACCORDION_PLACEHOLDER 

 Number 

 Number transformers 

 FIXME_ACCORDION_PLACEHOLDER 

 Date 

 Date transformers 

 FIXME_ACCORDION_PLACEHOLDERFIXME_ACCORDION_PLACEHOLDER 

 Previous Filter considerations, categories, and built-in filters 

 Next Extract indicators 

 Last updated 9 days ago 

 Was this helpful?
