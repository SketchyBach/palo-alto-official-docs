---
url: https://cortex-docs.paloaltonetworks.com/cortex-agentix/detect-investigate-and-respond-to-threats/threat-intel-management/get-started-with-threat-intel-management/indicator-lifecycle
fetched_at: 2026-09-06T10:19:33Z
source: cortex-platform
---

# Indicator lifecycle | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex AgentiX 

 Cortex AgentiX Documentation 

 Detect, Investigate, and Respond to Threats 

 Threat Intel Management 

 Get started with Threat Intel Management 

 Cortex AgentiX 

 Indicator lifecycle 

 Track indicators through their lifecycle in Cortex AgentiX. 

 Indicators are text-based artifacts associated with issues, such as IP addresses, URLs, and email addresses, and are an essential part of the case management and remediation process. They help correlate issues, create hunting operations, and enable you to easily analyze cases and reduce Mean Time to Response (MTTR). 

 The following diagram explains the indicator lifecycle in Cortex AgentiX. 

 indictaor-lifecycle.png 

 Step 

 Details 

 1. Identify the indicator type and value 

 Cortex AgentiX analyzes the text-based artifact and if it matches the indicator type profile. The indicator value is extracted, based on the indicator profile definition. Indicator extraction identifies indicators from various sources within Cortex AgentiX, such as email headers, IP addresses, email addresses, and file hashes in file attachments. For more information about indicator extraction, see Indicator extraction . 

 You can create or customize existing indicator types and fields for your use case. For more information, see Customize indicator fields and types . 

 2. Formatting and validation 

 Formatting and validation of the indicator are done using a formatting script that validates the data that represents the indicator's value and determines how we want the data to appear in Cortex AgentiX. For example, the URL indicator type uses the FormatURL script, which defangs URLs. For more information, see Formatting scripts . 

 3. Create or update an indicator 

 If the indicator is not known to Cortex AgentiX, an indicator is created or you can create your own. If already known, it is updated with any new data including last seen dates. If the indicator is in an expired state but new data is received, it changes to active status. 

 4. Gather reputation and enrichment information 

 You can run reputation commands and enhancement script commands on indicator values. You need to set them to run in the indicator type. The enhancement script also runs on the indicator type. Both determine the indicator's verdict. For more information, see Enhancement scripts . 

 When a reputation command/enhancement script is run, the verdict gets added to the issue context, when attached to an issue. Generally, the information is found under the Dbot Score key, the specific Indicator type, and specific vendor information. 

 Note 

 To run enhancement scripts and reputation commands, you must configure a relevant enrichment integration, such as VirusTotal, IPinfo v2, etc. 

 5. Reputation scripts 

 Reputation scripts can be used if you want to override existing reputation commands with custom logic. For those indicator types without reputation commands, a custom reputation script can be applied. Use it to customize verdicts and DBotScore context entry. For more information, see Reputation scripts . 

 6. Map indicator fields 

 After your indicator is enriched, you can map fields. Some indicator fields are automatically mapped by Cortex AgentiX to contain the relevant values. The default settings can be changed for each indicator type. You can create and associate any custom fields with indicators. For more information, see Indicator classification and mapping . 

 7. Expiration 

 Many indicators have expiration dates as threats are dynamic. IP addresses may change, systems may be fixed, etc. When configuring an indicator type, you can set it never to expire or after a time interval. For more information, see Configure indicator expiration . 

 Tip 

 We recommend defining your policy for handling expired indicators. 

 Previous Indicator concepts 

 Next Indicator configuration 

 Last updated 10 days ago 

 Was this helpful?
