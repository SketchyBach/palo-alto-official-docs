---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-3.x/cortex-xdr-3.x-documentation/cortex-xdr-xql/functions/json_extract_scalar
fetched_at: 2026-09-16T08:44:22Z
source: cortex-platform
---

# json_extract_scalar | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

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

 json_extract_scalar 

 Learn more about the Cortex Query Language json_extract_scalar() function. 

 Important 

 Before using this JSON function, it's important that you understand how Cortex XDR treats a JSON in the Cortex Query Language. For more information, see JSON functions . 

 Syntax 

 Regular Syntax 

 Ask Copy 

 json_extract_scalar(<json_object_formatted_string>, <field_path>) 

 When a field in the <json_path> contains characters, such as a dot (.) or colon (:), use the syntax: 

 Ask Copy 

 json_extract_scalar(<json_object_formatted_string>, "['<json_field>']") 

 Syntactic Sugar Format 

 To make it easier for you to write your XQL queries, you can also use the following syntactic sugar format: 

 Ask Copy 

 <json_object_formatted_string> -> <field_path> 

 When a field in the <json_path> contains characters, such as a dot (.) or colon (:), use the syntax: 

 Ask Copy 

 <json_object_formatted_string> -> ["<json_field>"] 

 Description 

 The json_extract_scalar() function accepts a string representing a JSON object, and it retrieves the value from the identified field as a string. This function always returns a string. If the JSON field is an object or array, it will return a null value. To retrieve an XQL-native datatype, use an appropriate function, such as to_float or to_integer . If the input string does not represent a JSON object, this function fails to parse. To convert a string field to a JSON object, use the to_json_string function. 

 Important 

 JSON field names are case sensitive, so the key to field pairing must be identical in an XQL query for results to be found. For example, if a field value is "TIMESTAMP" and your query is defined to look for "timestamp", no results will be found. 

 Examples 

 Return the storage_device_drive_type value from the action_file_device_info field, and return the record if it is 1. 

 There are two ways that you can build this query either with a filter using an XQL-native datatype or string. 

 Option A - Filter using an XQL-native datatype 

 Option B - Filter using a string 

 Using Syntactic Sugar Format 

 The same example above with a syntactic sugar format. 

 Previous json_extract_array 

 Next json_extract_scalar_array 

 Last updated 1 month ago 

 Was this helpful?
