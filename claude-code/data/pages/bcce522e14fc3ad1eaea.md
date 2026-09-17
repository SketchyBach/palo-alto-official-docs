---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-3.x/cortex-xdr-3.x-documentation/cortex-xdr-xql/functions/extract_url_registered_domain
fetched_at: 2026-09-16T08:44:22Z
source: cortex-platform
---

# extract_url_registered_domain | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

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

 extract_url_registered_domain 

 Learn more about the Cortex Query Language extract_url_registered_domain() function. 

 Syntax 

 Ask Copy 

 extract_url_registered_domain ("<URL>") 

 Description 

 The extract_url_registered_domain() function returns the registered domain or registerable domain, the public suffix plus one preceding label, of a URL. The function always returns a value in lowercase characters even if the URL provided contains uppercase characters. 

 Examples 

 Output examples when using the function 

 Returns paloaltonetworks.com from the complete URL: https://www.paloaltonetworks.com . 

 Ask Copy 

 extract_url_registered_domain ("https://www.paloaltonetworks.com") 

 Returns NULL for the URL: //user:password@a.b:80/path?query 

 Ask Copy 

 extract_url_registered_domain ("//user:password@a.b:80/path?query") 

 Returns example.co.uk in lowercase for the complete URL: www.Example.Co.UK , which includes uppercase characters. 

 Ask Copy 

 extract_url_registered_domain ("www.Example.Co.UK") 

 Returns paloaltonetworks.com for the following URL containing suffixes: https://www.test.paloaltonetworks.com/suffix/another_suffix 

 Ask Copy 

 extract_url_registered_domain ("https://www.test.paloaltonetworks.com/suffix/another_suffix") 

 Complete XQL query example 

 Returns one xdr_data record in the results table where the registered domain of the URL https://www.test.paloaltonetworks.com is listed in the REGISTERED_DOMAIN column as paloaltonetworks.com . 

 Ask Copy 

 dataset = xdr_data 
 | alter registered_domain = extract_url_registered_domain("https://www.test.paloaltonetworks.com") 
 | fields registered_domain 
 | limit 1 

 Previous extract_url_pub_suffix 

 Next first 

 Last updated 1 month ago 

 Was this helpful?
