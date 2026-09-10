---
url: https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cases-and-issues/investigation-and-response/automation/scripts/use-existing-scripts
fetched_at: 2026-09-06T10:05:25Z
source: cortex-platform
---

# Use existing scripts | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Cortex CLOUD Posture Management 

 Cases and issues 

 Investigation and response 

 Automation 

 Scripts 

 Cortex Cloud Posture 

 Use existing scripts 

 Find, review, and use existing scripts. 

 Using or modifying an existing script enables you to quickly leverage proven functionality and save significant time and effort developing a new script from scratch. 

 For example, you can use scripts from the Base and Common Scripts content packs that provide basic and reusable functions that can streamline your playbook development. 

 Common scripts 

 Filter and sort the table 

 Use the filter bar at the top of the Secrets table to narrow results by any filterable column. Common filtering strategies include: 

 By severity: Filter to Critical and High severity to focus on the most impactful secrets exposures 

 By secret type: Filter to a specific secret type (such as AWS Access Key) to scope remediation to a single credential category 

 By branch: Filter to the main or production branch to focus on secrets that affect production-bound code 

 By resolution status: Filter to New to identify untriaged secrets issues, or to In Progress to monitor active remediation 

 By secret validation: Filter to Valid or Privileged to identify confirmed active credentials that require immediate revocation 

 You can copy the script and add new functions/variables, or add your functions to the CommonUserServer script. You can also use your scripts to override the existing scripts in the CommonServer script. 

 CommonServerPython 

 The CommonServerPython script contains Python functions that can be used when writing your scripts and integrations. 

 The script contains over 400 functions, such as appendContext , vtCountPositives (which counts the number of detected URLs in the War Room entry), and datetime_to_string , (which converts a DateTime object into a string). 

 You can copy the script and add new functions/variables, or add your functions to the CommonServerUserPython script. You can also use your scripts to override the existing scripts in the CommonServerPython script. 

 CommonServerPowerShell 

 The CommonServerPowerShell script contains PowerShell arguments/functions that can be used when writing your scripts and integrations. 

 The script contains many arguments/functions, such as SetIntegrationContext , Write-HostToLog (which writes to the demisto.log), and ReturnOutputs (which returns results to the user more intuitively). 

 You can copy the script and add new arguments/functions or add your own to the CommonServerUserPowerShell script. You can also use your scripts to override the existing scripts in the CommonServerPowerShell script. 

 Navigate to Investigation & Response → Automation → Scripts and in the Scripts Library search for the script you want to use. 

 Use the free text in the search box to find an existing script. From the search drop-down, you can: 

 Perform a basic search by Basic (name and tag), Name , or Tag . 

 Perform an advanced search for specific words In Script or Everywhere (including the script name and tags). 

 You can search for an exact match of the script name by putting quotation marks around the search text. For example, searching for "AddKeyToList" returns the script with that name. You can search for more than one exact match by including the logical operator "or" in between your search texts in quotation marks. For example, searching for "AnalyzeTimestampIntervals" or "AddKeyToList" returns the two scripts with those names. Wildcards are not supported in free text search. 

 You can sort the scripts in the library alphabetically, by modified date, by system, or custom, and you can filter for disabled or deprecated scripts. 

 The Script Helper also provides a list of available alphabetically ordered commands and scripts. 

 Click Edit . If the script you want to use is locked, you first need to duplicate it. 

 If a script is installed from a content pack, by default, the script is locked, which means that it is not editable. 

 In the Agentic Assistant pane, start a conversation with the Automation Engineer agent to edit the script, or manually edit the script code and define the script settings. 

 For more information, see Accelerate script development using the Automation Engineer agent . For details about script settings, see Create a script . 

 Save the script version. 

 (Recommended) Validate your script. 

 Click Test . 

 In the Arguments section, provide values for any inputs your prompt requires. These inputs are used to simulate how the script will behave in a live playbook, or how the script registered as an Action and assigned to an Agent will run as part of an executed plan. 

 You can add input values manually. 

 Click Run . 

 The scripts are executed in the Playground. Review the output generated by the script to validate its behavior and ensure it produces the expected results. The output is typically a text summary or another structured format that you have defined. 

 In each run result, you can take the following actions: 

 Action 

 Description 

 Edit 

 Edit the entry, mark it as a note, preview it, or delete it. 

 Mark as note 

 Marks the entry as a note, which can help you understand why certain action was taken and assist future decisions. 

 When marked as a note, it is highlighted, so you can easily find it in the War Room or the Issue Overview tab. 

 View artifact in new tab 

 Opens a new tab for the artifact. 

 Add tags 

 Add any relevant tags to use that help you find relevant information. 

 (Optional) Click next to the Edit button and select Register new Action to register the script as an action and make it available for agents. For more information, see Manage actions . 

 Previous Access to scripts 

 Next Create a script 

 Last updated 5 days ago 

 Was this helpful?
