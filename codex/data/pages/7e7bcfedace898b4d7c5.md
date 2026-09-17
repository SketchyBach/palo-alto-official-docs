---
url: https://cortex-docs.paloaltonetworks.com/xql-command-reference-guide/readme/functions/bitwise_xor
fetched_at: 2026-09-16T09:04:53Z
source: cortex-platform
---

# bitwise_xor | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 XQL 

 XQL Command Reference Guide 

 Cortex XQL Command Reference 

 Functions 

 bitwise_xor 

 Use the bitwise_xor() function to perform a bitwise exclusive OR (XOR) operation between two integer values. 

 Syntax 

 Ask Copy 

 bitwise_xor ( < left_clause > , < right_clause > ) 

 Parameters 

 Name 

 Type 

 Required 

 Description 

 left_clause 

 integer 

 Yes 

 The first integer value or field on which to perform the bitwise XOR. 

 right_clause 

 integer 

 Yes 

 The second integer value or field to XOR against the first value. 

 Returns 

 The bitwise_xor() function returns an integer representing the result of the bitwise exclusive OR operation between the two input parameters. 

 Usage notes 

 The function performs a bitwise XOR ( ^ ) operation, comparing each bit of the first operand to the corresponding bit of the second operand. If the bits are different, the corresponding result bit is set to 1; if the bits are the same, it is set to 0. 

 Both parameters must be integers. Passing a string value will result in a validation error. 

 This function is commonly used to toggle specific bit flags, detect differences between two bitmask fields, or perform simple obfuscation. 

 The XOR operation is its own inverse: applying bitwise_xor() twice with the same value returns the original value (for example, bitwise_xor(bitwise_xor(a, b), b) equals a ). 

 The function is typically used within the alter or filter stages to create computed fields or filter events based on bitwise conditions. 

 Examples 

 Example 1: Toggle a specific bit flag in an integer field 

 Goal : Toggle bit 2 (value 4) in the event_type field. If the bit is set, it will be cleared; if it is cleared, it will be set. 

 XQL code : 

 Explanation : This query performs a bitwise XOR between event_type and 4 (binary 100 ). For a value of 7 (binary 111 ), bit 2 is cleared, resulting in 3 (binary 011 ). For a value of 3 (binary 011 ), bit 2 is set, resulting in 7 (binary 111 ). 

 Output : 

 event_id 

 event_type 

 toggled_type 

 101 

 7 

 3 

 102 

 3 

 7 

 103 

 5 

 1 

 Example 2: Detect differences between two bitmask fields 

 Goal : Identify which bits differ between two integer fields by computing their XOR. 

 XQL code : 

 Explanation : This query computes the XOR of permission_before and permission_after . The result contains 1-bits only in positions where the two fields differ. For values 7 (binary 111 ) and 5 (binary 101 ), the result is 2 (binary 010 ), indicating bit 1 changed. 

 Output : 

 event_id 

 permission_before 

 permission_after 

 diff_bits 

 101 

 7 

 5 

 2 

 102 

 3 

 3 

 0 

 103 

 12 

 9 

 5 

 Example 3: Filter events where specific bits changed 

 Goal : Filter for events where at least one of the lower 4 bits changed between two status fields. 

 XQL code : 

 Explanation : This query first computes the XOR of status_before and status_after to find all differing bits, then uses bitwise_and() with 15 (binary 1111 ) to isolate the lower 4 bits. Only events where at least one of the lower 4 bits changed pass the filter. 

 Output : 

 event_id 

 status_before 

 status_after 

 changed_bits 

 101 

 7 

 5 

 2 

 103 

 12 

 9 

 5 

 106 

 15 

 0 

 15 

 Related articles 

 Stages : alter , config , filter , fields , limit 

 Functions : bitwise_and , bitwise_or , bitwise_sleft , bitwise_sright , to_integer 

 Previous bitwise_sright 

 Next cbrt 

 Last updated 3 months ago 

 Was this helpful?
