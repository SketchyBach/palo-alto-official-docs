---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-3.x/cortex-xdr-3.x-documentation/cortex-xdr-xql/functions/object_create
fetched_at: 2026-09-16T08:44:23Z
source: cortex-platform
---

# object_create | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR 

 Cortex XDR 3.x Documentation 

 Cortex XDR 3.x Documentation 

 Cortex XDR XQL 

 Functions 

 Cortex XDR 3.x 

 object_create 

 Learn more about the Cortex Query Language object_create() function. 

 Syntax 

 Ask Copy 

 object_create ("<key1>", "<value1>", "<key2>", "<value2>",...) 

 Description 

 The object_create() function returns an object based on the given parameters defined for the key and value pairs. Accepts n > 1 even number of parameters. 

 Example 

 Returns a final object to a field called a that contains the key and value pair {“2”:“password”} , where the "password" value is comprised by joining 2 values together. 

 Ask Copy 

 dataset = xdr_data 
 | alter a = object_create("2", concat("pass", "word")) 
 | fields a 

 Previous object_merge 

 Next parse_epoch 

 Last updated 1 month ago 

 Was this helpful?
