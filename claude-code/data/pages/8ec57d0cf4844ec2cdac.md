---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-on-prem/8.5/investigate-and-respond-to-threats/threat-intel-management/indicator-configuration/customize-indicator-types-fields-and-layouts/create-an-indicator-type
fetched_at: 2026-09-16T09:14:31Z
source: cortex-platform
---

# Create an indicator type | 8.5 (EoL) | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 8 

 Cortex XSOAR 8 On-prem Documentation 

 8.5 (EoL) 

 Investigate and Respond to Threats 

 Threat Intel Management 

 Indicator configuration 

 Customize indicator types, fields, and layouts 

 Cortex XSOAR 8.5 On-prem EoL 

 Create an indicator type 

 Documentation for Cortex XSOAR On-prem 8.5 (EoL). 

 Indicators are categorized by indicator type, which determines the indicator layout and fields that are displayed and which scripts are run on indicators of that type. Cortex XSOAR includes several out-of-the-box indicator types, such as: 

 IP Address 

 Domain 

 URL 

 File 

 For more information about file indicators and how to configure the file hash, see File indicators . 

 When you create a new indicator type, you define its properties, including whether and how to format the indicator data and how the verdict is calculated. 

 Go to Settings & Info → Settings → Object Setup → Indicators → Types . 

 Click New . 

 In the Settings tab, add the required indicator profile, such as name and Regex. 

 For more information, see Indicator type profile . 

 In the Custom Fields tab, map the fields, as required. 

 For more information, see Map custom indicator fields . 

 See this video for an example of creating a custom indicator type: Indicators and Enrichment . 

 Create a company email indicator type 

 The following example describes how to create a new indicator type to manage employee emails, for example, for resource management or inside threat investigation. 

 Create a new indicator type for the employee email addresses that contain the “our_company.com” company domain. 

 Under Settings & Info → Settings → Object Setup → Indicators → Types → New , in the Settings tab, define the following. 

 Name: Company email 

 Regex: .*?@our_company.com (simplified to capture all the email addresses using the our_company.com domain). 

 Reputation command: Not relevant for this example, since we don't want any external enrichment. 

 Formatting script: If more formatting is needed, you can use a formatting script to edit the saved value. 

 Reputation script: If needed, you can create a reputation script to affect the DBot score given to the new custom indicator. 

 In the Custom Fields tab, map custom fields for the new indicator type. 

 You can map fields returned using an integration such as Active Directory to obtain more data about the actual user to whom the email belongs. You can also collect data using integrations such as Okta (MFA, SSO), SIEM, and email security. Fields such as Username , Full name , and various groups the user is part of as well as other identifiers, are returned to context and mapped into the indicator using the custom fields. 

 use-case-custom-indicator-type-mapping.png 

 Note 

 If you miss mapping any field, you can create additional new indicator fields and either relate them to all indicator types, or relate them only to the new indicator type (recommended). 

 Design a custom layout for the new indicator type. 

 You can use the Dynamic section in the indicator layout to run Python scripts and return results from within the layout itself. 

 Previous Customize indicator types, fields, and layouts 

 Next Indicator type profile 

 Last updated 1 month ago 

 Was this helpful?
