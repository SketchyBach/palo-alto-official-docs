---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-administrator-guide/6.14/customize-cortex-xsoar/customize-and-configure-cortex-xsoar/lists/set-the-list-separator-character
fetched_at: 2026-09-06T10:41:54Z
source: cortex-platform
---

# Set the List Separator Character | 6.14 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Administrator Guides 

 6.14 

 Customize Cortex XSOAR 

 Customize and Configure Cortex XSOAR 

 Lists 

 Cortex XSOAR 6.14 

 Set the List Separator Character 

 Set the list separator character in Cortex XSOAR 6.14. The default is a comma. 

 When you create a list, the data is a just a string of items. The items in a list are distinguished from one another using a separator. The default separator is a comma. 

 You can set a custom separator globally (all lists) or for individual lists. The custom list separator can only be a single character, for example a single semicolon (;) or a single colon (:). If you set the separator as multi-character, the default separator will be applied. 

 If you set a global list separator and custom separator for an individual list, the separator set for the individual list overrides the global list separator. 

 After setting a new separator, the separators in existing lists are not updated and are not treated as separators anymore. You can use the Replace transformer to modify an existing list and replace all instances of the previous separator with the new separator. 

 Go to Settings → About → Troubleshooting . 

 In the Server Configuration section, click Add Server Configuration . 

 Add the necessary key and value. 

 Type 

 Key 

 Value 

 Global 

 list.separator 

 Single-character separator. For example “;”. 

 List 

 list.< listName >.separator 

 Single-character separator. For example “;”. 

 Previous Create a List 

 Next Transform a List into an Array 

 Last updated 4 days ago 

 Was this helpful?
