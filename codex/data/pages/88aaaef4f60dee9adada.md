---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-administrator-guide/6.13/customize-cortex-xsoar/customize-and-configure-cortex-xsoar/indicators/indicator-customization/indicator-types/indicator-type-profile
fetched_at: 2026-09-06T10:45:33Z
source: cortex-platform
---

# Indicator Type Profile | 6.13 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Administrator Guides 

 6.13 

 Customize Cortex XSOAR 

 Customize and Configure Cortex XSOAR 

 Indicators 

 Indicator Customization 

 Indicator Types 

 Cortex XSOAR 6.13 

 Indicator Type Profile 

 Configure indicator type profile settings. 

 Each indicator type has its own 'profile' that allows Cortex XSOAR to recognize it across the platform. Add the following fields, when you edit or Create an Indicator Type . 

 Field 

 Description 

 Name 

 A meaningful name for the indicator type. 

 Regex 

 The regular expression (regex) by which to identify indicators for this indicator type. 

 Formatting Script 

 Modifies how the indicator displays in Cortex XSOAR. 

 Formatting scripts must be tagged indicator-format in order to appear in the dropdown for the indicator type. 

 Reputation Commands 

 Calculates the reputation of indicators of this type. The verdict (reputation) is only associated with the specific indicator on which it’s run (not the indicator type). The command returns the reputation of the indicator as an entry with entry context and in some cases also returns context values that can be mapped to the custom fields of the indicator. The results of the reputation command do not print to the war room in the indicator extraction flow. 

 Layout 

 Select the Indicator layout . 

 Reputation Scripts 

 The output of the reputation script is a verdict score, which is used as the basis for the indicator verdict. Reputation scripts must be tagged reputation in order to appear in the dropdown for the indicator type. 

 The results of reputation scripts do not print to the war room in the extraction flow. 

 Enhancement Scripts 

 The enhancement script is not part of the indicator extraction flow, and are run manually on the indicator type. For example, domain reputation, email reputation, parse email files, etc. 

 After indicators are identified, you can go to the indicator quick view, click the Actions button and run an enhancement script directly on an indicator. In order for these scripts to be available in the drop-down menu, they need the enhancement tag. 

 When you run an enhancement script, it is the equivalent of running the script at the CLI in the War Room. The script can write to context, return an entry, etc. 

 Exclude these integrations for the reputation command 

 Integrations to exclude when calculating the verdict, evaluating, and enriching indicators of this indicator type. Excluding an integration here prevents it from triggering during automated enrichment processes such as indicator extraction, the enrichIndicators command, or the Enrich button. This setting does not prevent the integration from running if you explicitly execute its command (for example, !url or !ip ). 

 Tip 

 To control which integrations run when explicitly executing a command (and not during enrichment), add the using-brand argument to specify only the integrations you want to use. 

 For example: 

 !url url="https://www.google.com" using-brand="AutoFocus V2,VirusTotal" 

 Indicator Expiration Method 

 The method by which to expire indicators of this type. The expiration method that you select is the default expiration method for indicators of this indicator type. 

 The expiration can also be assigned when configuring a feed integration instance, which overrides the default method. 

 Never Expire: indicators of this type never expire. 

 Time Interval: indicators of this type expire after the specified number of days or hours. 

 Context path for verdict value (Advanced) 

 When an indicator is extracted, the entry data from the command is mapped to the incident context. This path defines where in context the data is mapped. 

 Context value of verdict (Advanced) 

 The value of this field defines the actual data that is mapped to the context path. 

 Cache expiration in minutes (Advanced) 

 The amount of time (in minutes) after which the cache for indicators of this type expire. The default is 4,320 minutes (three days). The cache enables you to limit API requests by only updating indicators after a specific time period has passed. The cache cannot be cleared manually. 

 Note 

 Indicator cache expiration rules only apply to automatic enrichment, triggered by the enrichIndicators command. If you run reputation commands, such as !ip , the commands will execute and the indicator will be updated if there is new information, even if the cache has not expired. 

 Previous Create an Indicator Type 

 Next Map Custom Indicator Fields 

 Last updated 3 days ago 

 Was this helpful?
