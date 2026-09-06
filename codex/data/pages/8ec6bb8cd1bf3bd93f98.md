---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-on-prem/8.14/investigate-and-respond-to-threats/threat-intel-management/indicator-configuration/customize-indicator-types-fields-and-layouts/create-an-indicator-field
fetched_at: 2026-09-06T10:25:52Z
source: cortex-platform
---

# Create an indicator field |  8.14 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 8 

 Cortex XSOAR 8 On-prem Documentation 

 8.14 

 Investigate and Respond to Threats 

 Threat Intel Management 

 Indicator configuration 

 Customize indicator types, fields, and layouts 

 Cortex XSOAR 8.14 On-prem 

 Create an indicator field 

 Create custom indicator fields in Cortex XSOAR 8.14 On-prem. 

 Create an indicator field 

 Indicator fields are used to add specific indicator information to incidents. When you create an indicator field, you can associate the field to a specific indicator type or all indicator types. You can then map the custom field to the relevant indicator type. You can also add an indicator field trigger script. 

 Note 

 Cortex XSOAR IOC fields are based on the STIX 2.1 specifications. For more information, see Indicator field structure . 

 Field types 

 Field type 

 Description 

 Boolean 

 Checkbox 

 Date picker 

 Adds the date to the field. 

 Grid (table) 

 Include an interactive, editable grid as a field type for selected indicator types or all indicator types. 

 To see how to create a grid field and to use a script, see Add an indicator field trigger script to an indicator field . 

 When you select Grid (table) you can format the table and determine if the user can add rows. 

 HTML 

 Create and view HTML content, which can be used in any type of indicator. 

 Note 

 The following HTML tags are not permitted: blockquote , del , dd , div , dl , dt , fieldset , form , h1 , h2 , h3 , h4 , h5 , h6 , hr , iframe , ins , li , math , noscript , ol , pre , p , script , style , table , ul , address , article , aside , canvas , details , dialog , figcaption , figure , footer , header , hgroup , main , nav , output , progress , section , video . 

 The following CSS tags are not permitted: background-color , text-align , font-size , font-family , font-weight , color , line-height , border-style , border , page-break-inside , tablelayout , padding , background-size , display , padding-top , padding-right , padding-bottom , padding-left , text-size-adjust , break-inside , word-break , width , height , -ms-text-size-adjust , -webkit-text-size-adjust . 

 Long text 

 Long text is analyzed and tokenized, and entries are indexed as individual words, enabling you to perform advanced searches and use wildcards. 

 Long text fields can't be sorted and used in graphical dashboard widgets. 

 While editing a long text field, pressing enter will create a new line (case is insensitive). 

 Add a placeholder, if required. 

 Markdown 

 Add markdown formatted text as a template, which will be displayed to users in the field after the indicator is created. Markdown lets you add basic formatting to text to provide a better end-user experience. 

 Multi select/Array 

 Select the following options: 

 Multi-select from a prefilled (static) list 

 An empty array field for the user to add one or more values as a comma-separated list 

 Add a placeholder, if required. 

 Number 

 Can contain any number. Default is 0. 

 Role 

 The role assigned to the indicator. Determines which users (by role) can view the indicator. 

 Short text 

 Short text is treated as a single unit of text and is not indexed by word. Advanced search, including wildcards, is not supported. 

 Short text fields are case-sensitive by default but can be changed to case-insensitive when creating the field. 

 While editing a short text field, pressing enter will save the change. 

 Maximum length 60,000 characters 

 Recommended use is one-word entries, such as username and email address. 

 Select a placeholder, if required. 

 Single select 

 Select a value from a list of options. Add comma-separated values. 

 Tags 

 Accepts a single tag or a comma-separated list, not case-sensitive. 

 Add a placeholder, if required. 

 URL 

 Add a URL when completing the field. 

 User 

 A user in Cortex XSOAR. 

 How to create a field 

 Select Settings & Info → Settings → Object Setup → Indicators → Fields → New Field . 

 Select the relevant field type. 

 Complete the following fields (if relevant): 

 Parameter 

 Description 

 Mandatory 

 If selected, this field is mandatory when used in a form. 

 Field Name 

 A meaningful display name for the field. After you type a name, you will see below the field that the Machine name is automatically populated. The field’s machine name is applicable for searching and the CLI. 

 Tooltip 

 An optional tooltip for the field. 

 In the Basic Settings tab, define the values (according to the selected field type). 

 In the Attributes tab define the following: 

 Field 

 Description 

 Script to run when field value changes 

 The script dynamically changes the field value when script conditions are met. For a script to be available, it must have the field-change-triggered-indicator tag when defining the script. For more information, see Indicator field trigger scripts . 

 Add to all indicator types 

 This option is selected by default, which means this field is available to use in all indicator types. Clear the checkbox to associate this field with a subset of indicator types. 

 Make data available for search 

 The values for this field can be returned in searches. 

 Save the field. 

 Ask Copy 

 If you subsequently edit the field, you can optionally select **Don't show in the indicators layout**. If you select this, the indicator field does not appear in the layout but the data is displayed in the context data. 

 7. (Optional) Add a custom field to a section in the indicator layout. 

 Ask Copy 

 If you select **Don't show in the indicators layout**, the field will not appear in the layout. 

 8. (Optional) In the indicator type, map custom indicator fields, so an indicator field is automatically updated, without the analyst having to manually change it. 

 Previous Map custom indicator fields 

 Next Indicator fields structure 

 Last updated 4 hours ago 

 Was this helpful?
