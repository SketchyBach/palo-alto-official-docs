---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsoar-6-threat-intel-management-guides/6.12/configure-indicators/indicator-extraction
fetched_at: 2026-09-16T08:58:01Z
source: cortex-platform
---

# Indicator Extraction | 6.12 (EoL) | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Threat Intel Management Guides 

 6.12 (EoL) 

 Configure Indicators 

 Cortex XSOAR 6.12 Threat Intel Management EoL 

 Indicator Extraction 

 Extract and enrich indicators from incident fields in Cortex XSOAR 6.12. 

 Indicator extraction identifies indicators from different text sources in the system (such as War Room entries, email content, etc.), extracts them (usually based on regex) and creates indicators in Cortex XSOAR. After extraction, the indicator can be enriched. 

 Indicator enrichment takes the extracted indicator and provides detailed information about the indicator (from open ports to whois information, etc.). It provides a story about the indicator, based on an enrichment feed such as VirusTotal, IPinfo, etc. 

 In Cortex XSOAR, the indicator extraction feature extracts indicators from incident fields and enriches them using commands (such as the !url command), and scripts defined for the indicator type, such as urlscan.io , URLhaus . Provided the indicator extraction is enabled, you can configure the extraction logic according to the incident type and according to the associated field. 

 You can extract indicators when fetching incidents, when incident fields are updated, and in playbook tasks. You can also use commands like !extractIndicators , !enrichindicators , !ip , etc. 

 Note 

 Reputation commands, such as !ip and !domain , can only be used after you configure and enable a reputation integration instance, such as Virus Total and Whois. 

 As your system matures and you start ingesting more events with more integrations configured, you need to consider customizing your incident type, including how to extract indicators. 

 Caution 

 Extracting indicators can adversely affect system performance. We recommend that you define extraction settings for each incident type, as needed. 

 For example, for Malware you may want to extract all IP addresses, for Phishing you may only want to extract IP addresses from specific email headers. For attachments, you may want to disable indicator extraction to reduce external API usage and protect restricted data (the hash) from being sent. 

 Some content packs include a dashboard and widget that track API rate limit errors. You can use this information for troubleshooting and to make decisions about indicator enrichment. 

 Indicator Extraction Rules 

 You can create indicator extraction rules by using the following methods: 

 Incident Types 

 You can extract indicators from incident fields on creation of an incident and when a field changes. Indicator extraction rules are set out-of-the-box for content pack installed incident types. For example, in a Phishing incident type, by default, in the Destination IP field, IPv6 and IP indicators are extracted. For the Detection URL field, the URL indicator field is extracted, etc. 

 Provided the indicator extraction settings are enabled and depending on the rules set in the incident type, indicator extraction is automatic. For example, in a phishing incident, indicator extraction is set to extract the IP indicator (in the incident type). When the incident field updates, the IP indicator field is extracted automatically. In the War Room, you can check that the IP indicator field has been extracted by typing 1.1.1.1 . Cortex XSOAR recognizes the indicator as an IP indicator by matching it to the IP indicator’s regex. It then extracts and enriches the indicator using an integration that uses the IP command (such as, IPinfo). 

 Note 

 To edit content packs installed incident types including those propagated to a tenant in a multi-tenant environment, you need to detach them. Once detached, the incident type does not receive new content from Cortex XSOAR. If you want to receive content updates reattach the incident type. If you want to receive content updates and save the content, duplicate the incident type. For more information, see customize incident layouts . 

 Playbook Tasks 

 Commands : Run a command using the command line in Cortex XSOAR during an investigation. 

 Indicator Extraction Mode Options 

 Indicator extraction supports the following modes: 

 None 

 Inline 

 Out of band 

 Use system default 

 For detailed information about the modes and how to set them up, see Indicator Extraction Modes . 

 Indicator Scripts 

 When creating or editing an indicator type, you can add the following scripts: 

 Formatting Scripts 

 Enhancement Scripts 

 Reputation Scripts 

 During the indicator extraction flow, the order of execution is regex, formatting script, and reputation command, reputation script. Enhancement scripts are not part of the flow. 

 When running indicator extraction, using regex, the indicator uses a formatting script to transform the regex into a usable indicator for use in Cortex XSOAR in the War Room, reports, dashboards, etc. If indicator extraction has run, is turned off, or you have reached your API limit, if you have added an enhancement script to the indicator type, you can run an enhancement script. Reputation scripts enable you to change the reputation of the indicator. 

 Using Indicator Extraction in the CLI 

 You can run various commands in the CLI, such as !extractIndicators , !enrichindicators , !ip , ** !domain **and reputation script commands such as !URLReputation , !IPReputation . For more information, see Run Indicator Extraction in the CLI . 

 Note 

 Reputation commands, such as !ip and !domain , can only be used after you configure and enable a reputation integration instance, such as Virus Total and Whois. 

 Upgrade Cortex XSOAR 

 When upgrading from version 6.0.x and below: 

 By default, all incident types (from a content pack) are detached. 

 Indicator extraction is enabled for all incident fields, but if you have already selected an extraction mode, this is not affected. For example, if it is set to none there will be no extraction on incident creation. It is recommended to review the incident types, and select the required extraction rules. 

 The incident field change is set to none. 

 Troubleshoot Indicator Extraction 

 If indicators are not extracting, check whether the indicator mode is set to none. Even if you select the relevant incident fields and the indicators to extract, if the mode is set to none, indicators do not extract. 

 When creating new incident types, if you select Extract all indicators from all fields , all fields are extracted including the custom field. If you select Extract specific indicators by default , indicator extraction for the new custom field is set to none. 

 In a Multi-tenant environment, when installing a content pack in the Marketplace, the propagation labels enable the entire content pack to propagate to the tenant. For example, when installing the Content Pack (which includes an incident type) in the Marketplace, if the propagation label is set to all, it is propagated to the tenant. Even if you change the propagation label in the incident type, it has already been propagated. 

 The incident type labels can also propagate the incident type to additional tenants for which the content pack was not propagated. 

 If the incident type is not being updated in the tenant’s account, check whether the incident type is detached. If the tenant detaches the incident type, the changes are not updated from the Main Account. 

 Previous Add a Script in the Indicator Layout 

 Next Indicator Extraction Modes 

 Last updated 1 month ago 

 Was this helpful?
