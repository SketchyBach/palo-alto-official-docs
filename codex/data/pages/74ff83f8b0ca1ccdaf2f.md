---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-administrator-guide/6.12/configure-cortex-xsoar/customize-and-configure-cortex-xsoar/indicators/indicator-extraction/run-indicator-extraction-in-the-cli
fetched_at: 2026-09-06T10:48:52Z
source: cortex-platform
---

# Run Indicator Extraction in the CLI | 6.12 (EoL) | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Administrator Guides 

 6.12 (EoL) 

 Configure Cortex XSOAR 

 Customize and Configure Cortex XSOAR 

 Indicators 

 Indicator Extraction 

 Cortex XSOAR 6.12 EoL 

 Run Indicator Extraction in the CLI 

 Run indicator extraction from the CLI in Cortex XSOAR 6.12. 

 In the CLI you can run the following commands to extract and enrich indicators: 

 extractIndicators 

 enrichIndicators 

 Reputation commands 

 extractIndicators command 

 If you want to extract indicators from non-War-Room-entry sources (such as extracting from files), use the !extractIndicators command from the CLI. The command does not create indicators but extracts them only. Use the command to do the following: 

 Validate regex: Test a specific string to see if the relevant indicators are extracted correctly, such as a URL. 

 In a playbook or automation. The command extracts indicators in a playbook or automation non-war-room-source, and potentially also creates and enriches them (if required). 

 You can extract from the following: 

 A specified entry (an entry ID) 

 Investigation (Investigation ID) 

 Text 

 File path 

 For example, type !extractIndicators text="some text 1.1.1.1 something" auto-extract=inline 

 The entry text contains the text of the indicators, which is extracted and enriched. 

 You can also extract indicators by adding the auto-extract parameter with the script and the mode for which you are setting it up. For example, !ReadFile entryId=826@101 auto-extract=inline . 

 Usually, when using the CLI, you want to disable indicator extraction. For example, if you return internal/private data to the War Room, and you do not want it to be extracted and enriched in third-party services, add auto-extract=none to your CLI command. 

 You can enrich indicators by doing the following: 

 enrichIndicators command 

 The enrichIndicators command is usually used when you want to batch enrich indicators. This command works on existing indicators only (it does not create them on its own). When running the command, the relevant enrichment command is triggered (such as !ip ), which is based on the indicator type that is found. The data is saved to context and to the indicator. 

 Note 

 Triggering enrichment on a substantial amount of indicators can take time (since it's activating all enrichment integrations per indicator) and can result in performance degradation. 

 Reputation commands (such as !ip ) 

 This command can work on existing and non-existing indicators. If extraction is on, the data is saved both to the indicator and the incident's context. If not, then just to the context because the mapping flow is always triggered in enrichment commands. The default configuration is set to none in playbook tasks for extraction. 

 The indicator does not need to exist to run the reputation command, as the command uses a third-party threat intel integration, such as IPinfo. 

 You can also click the Enrich indicator button in the indicator layout. 

 Note 

 Reputation commands, such as !ip and !domain , can only be used after you configure and enable a reputation integration instance, such as Virus Total and Whois. 

 Previous Create Indicator Extraction Rules for an Incident Type 

 Next Create Indicator Extract Rules for a Playbook Task 

 Last updated 1 month ago 

 Was this helpful?
