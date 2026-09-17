---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-administrator-guide/6.13/learn-about-cortex-xsoar/get-started-in-cortex-xsoar/use-the-command-line-interface
fetched_at: 2026-09-16T08:56:36Z
source: cortex-platform
---

# Use the Command Line Interface | 6.13 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Administrator Guides 

 6.13 

 Learn about Cortex XSOAR 

 Get Started in Cortex XSOAR 

 Cortex XSOAR 6.13 

 Use the Command Line Interface 

 Cortex XSOAR 6.13 enables you to run system commands, integration commands, automations, and more, from an integrated CLI. 

 Cortex XSOAR enables you to run system commands, integration commands, automations, and more, from an integrated command line interface (CLI). With the CLI’s auto-complete feature, you can easily find relevant commands, scripts, and arguments. The CLI is available throughout Cortex XSOAR, with the exception of the Marketplace and while editing Playbooks. 

 Note 

 When entering a command in the CLI, you can use the up/down arrow buttons to do a reverse history search for previous commands with the same prefix. 

 You can run various commands in the CLI, by typing the following: 

 ! : Integration commands, automations, and built-in commands. For example, add evidence, assign an analyst, etc. 

 / : System commands/operations. For example, add notes, close an investigation, etc. 

 @ : User tagging. Send notifications to administrators, teams, analysts, etc. 

 Example: 

 To run the print script with a value of hello and the key a from the context: 

 !Print value="hello ${a}" 

 To explicitly use the following characters, place them within single or double quotes. An escape character \ is not required. 

 &&, ||, !, {, }, [, ], (, ), ~, *, ? 

 To explicitly use the following characters, place them within single or double quotes and use an escape character \ . 

 ** \, \n, \t, \r, ", ^, :, **comma, and space 

 When writing a query or complex text in the CLI, we strongly recommend enclosing your text with the backtick (`) character. Text within the backticks does not require you to escape single quotation marks ('), double quotation marks ('') or backslashes (\. 

 Examples: 

 To run the searchIncidentv2 script with query of all myfield that equals "this is a test" using escape characters: 

 !SearchIncidentsV2 query="myfield:\"this is a test\"" 

 To run the same query using backticks: 

 !SearchIncidentsV2 query=`myfield:"this is a test"` 

 To run the Python command returning Hello World using escape characters: 

 !py script="demisto.results(\"hello world\")" 

 To run the Python command returning Hello World using backticks: 

 !py script=`demisto.results("hello world")` 

 Note 

 (Multi-tenant) - The CLI is not available from the main account in a multi-tenant deployment. You can, however, run commands across multiple tenants from the main account. 

 Common Arguments 

 The following common arguments are available for every script run from the CLI. 

 Argument Name 

 Description 

 auto-extract 

 Decides whether/when to extract indicators. 

 Possible values: 

 inline - Extract indicators within the indicator extraction run context (synchronously). 

 outOfBand - Extract indicators in parallel (asynchronously) to other actions. 

 none - Do not extract indicators (recommended for scripts with large outputs when indicator extraction is not required). 

 execution-password 

 Supplies a password to run a password protected automation. 

 execution-timeout 

 Defines how long a command waits in seconds before it times out. 

 extend-context 

 Select which information from the raw JSON you want to add to the context data. 

 For a single value: contextKey=RawJsonOutputPath 

 For multiple values: contextKey1=RawJsonOutputPath1::contextKey2=RawJsonOutputPath2 

 ignore-outputs 

 Possible values: true or false . If set to true , will not store outputs into the context (besides extended context). 

 raw-response 

 Possible values: true or false . If set to true , returns the raw JSON result from the script. 

 retry-count 

 Determines how many times the script attempts to run before generating an error. 

 retry-interval 

 Determines the wait time (in seconds) between each execution of the script. 

 using 

 Selects which integration instance runs the command. 

 using-brand 

 Selects which integration runs the command. If the selected integration has multiple instances, the script may run multiple times. Use the using argument to select a single integration instance. 

 using-category 

 Selects which category of integrations runs the command. If the selected category includes multiple integration instances, the script may run multiple times. Use the using argument to select a single integration instance. 

 Previous API Keys 

 Next Common Arguments 

 Last updated 12 days ago 

 Was this helpful?
