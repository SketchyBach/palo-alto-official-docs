---
url: https://cortex-docs.paloaltonetworks.com/xql-command-reference-guide/readme/functions/arraycreate
fetched_at: 2026-09-06T10:58:20Z
source: cortex-platform
---

# arraycreate | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 XQL 

 XQL Command Reference Guide 

 Cortex XQL Command Reference 

 Functions 

 arraycreate 

 Use the arraycreate() function to return a new array based on the given parameters defined for its elements. 

 Syntax 

 Ask Copy 

 arraycreate ( " <array_element1> " , " <array_element2> " ,...) 

 Parameters 

 Name 

 Type 

 Required 

 Description 

 <array_element> 

 string, integer, float, boolean 

 Yes 

 The values to include as elements in the new array. Must be enclosed in quotes if they are string literals. 

 Returns 

 The arraycreate() function returns a single, new array containing the specified elements. 

 Usage notes 

 All elements within the array created by arraycreate() must be of the same data type. 

 The function returns the data types exactly as entered and doesn't implicitly convert string representations of numeric or boolean values. For example, "123" remains a string "123" within the array, and isn't converted to a number. 

 If all elements are NULL , the output is an empty array with no elements. 

 Examples 

 Example 1: Creating an array of string literals 

 Goal : Define a new array containing only direct string values. 

 XQL code : 

 Explanation : For each record in sample_xql_raw , a new field named custom_tags is created. This field contains an array with two string elements: "alert" and "investigation_needed" . 

 Output : 

 EVENT_ID 

 CUSTOM_TAGS 

 101 

 ["alert", "investigation_needed"] 

 102 

 ["alert", "investigation_needed"] 

 103 

 ["alert", "investigation_needed"] 

 Example 2: Creating an array with literals representing different data types (as strings) 

 Goal : Handle different types of literal values, specifically strings, numbers, and booleans, by treating them as string parameters. 

 XQL code : 

 Explanation : A mixed_info array is generated for each record. The query demonstrates that arraycreate() can incorporate various literal values into a single array, with all elements being treated as strings, adhering to the rule that all elements must be of the same data type. 

 Output : 

 EVENT_ID 

 MIXED_INFO 

 101 

 ["version_1.0", "123", "true", "45.67"] 

 102 

 ["version_1.0", "123", "true", "45.67"] 

 103 

 ["version_1.0", "123", "true", "45.67"] 

 Example 3: Creating an array by combining literals with existing field values 

 Goal : Dynamically build an array by including both static literal values and values from existing fields in each record. 

 XQL code : 

 Explanation : The to_string() function is used to convert the event_id (numeric) and is_successful (boolean) fields into strings, allowing them to be combined with the event_description (string) into a new array called event_summary . Each row will have a unique event_summary array reflecting its own event_id , event_description , and is_successful status. 

 Output : 

 EVENT_ID 

 EVENT_DESCRIPTION 

 IS_SUCCESSFUL 

 EVENT_SUMMARY 

 101 

 "User login successful" 

 true 

 ["101", "User login successful", "true"] 

 102 

 "File access attempt" 

 false 

 ["102", "File access attempt", "false"] 

 103 

 "Network connection established" 

 true 

 ["103", "Network connection established", "true"] 

 Example 4: Creating an array with derived values from JSON extraction 

 Goal : Incorporate values that are the result of other XQL functions, specifically json_extract_scalar() for extracting data from JSON fields. 

 XQL code : 

 Explanation : status_code is created by extracting the code field from simple_json_data . user_name is created by extracting the user.name field from nested_json_data . extracted_details then combines these two (potentially NULL) string values into a new array. If all the input elements are NULL, then the output is an empty array. 

 Output : 

 EVENT_ID 

 SIMPLE_JSON_DATA 

 NESTED_JSON_DATA 

 EXTRACTED_DETAILS 

 101 

 {"status": "ok", "code": 200} 

 {"user": {"id": "U1", "name": "Alice"}, ...} 

 ["200", "Alice"] 

 102 

 {"status": "fail", "error": "access_denied"} 

 {"process": {"name": "cmd.exe", "pid": 1234}, ...} 

 [] 

 103 

 {"connection_id": "CONN-001", "protocol": "TCP"} 

 {"source": {"ip": "172.16.0.1", "port": 5000}, ...} 

 [] 

 Related articles 

 Stages : alter 

 Functions : arrayconcat , to_string , json_extract_scalar 

 Datasets : xdr_data 

 Previous arrayconcat 

 Next arraydistinct 

 Last updated 2 months ago 

 Was this helpful?
