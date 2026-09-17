---
url: https://cortex-docs.paloaltonetworks.com/cortex-agentix/configure-cortex-agentix/automations/playbooks/build-your-playbook/customize-your-playbook/extract-indicators
fetched_at: 2026-09-16T08:51:02Z
source: cortex-platform
---

# Extract Indicators | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex AgentiX 

 Cortex AgentiX Documentation 

 Configure Cortex AgentiX 

 Automations 

 Playbooks 

 Build your playbook 

 Customize your playbook 

 Cortex AgentiX 

 Extract Indicators 

 Extract indicators from playbook data to enrich investigations in Cortex AgentiX. 

 In Cortex AgentiX, the indicator extraction feature extracts indicators from issue fields and enriches them using commands and scripts. 

 For more information about indicator extraction, see Extract and enrich an indicator . 

 How to set up indicator extraction in a playbook task 

 Select the playbook where you want to add indicator extraction, and click Edit. 

 In the playbook, click a task to open the Task Details pane. 

 Click the Advanced tab. 

 For Indicator Extraction mode, select the mode you want to use (default is none). 

 Click OK. 

 The following scenario shows how indicator extraction is used in the Process Email - Generic v2 playbook to extract and enrich a very specific group of indicators. 

 This playbook parses the headers in the original email used in a phishing attack. It is important to parse the original email used in the phishing attack and not the email that was forwarded to ensure that you only extract the email headers from the malicious email and not the one your organization uses to report phishing attacks. 

 Navigate to the Playbooks page and search for the Process Email - Generic v2 playbook. 

 Click and select either Duplicate (create a copy of the playbook to edit) or Edit Playbook (detach the playbook). 

 Open the Add original email details to context task, and for the Script drop down, change the script from Set to ParseEmailFilesV2. 

 Under the Outputs tab, you can see all of the different data that the task extracts. 

 xsiam-playbook-extract-indicators.png 

 Click the Advanced tab and set Indicator Extraction mode to Inline . This ensures all the outputs are processed before the playbook moves ahead to the next task. 

 Open the Display email information in layout - Email.Headers task. This task receives the data from the saved attachment tasks and sets the various data points to context. 

 Click the Advanced tab and set Indicator Extraction mode to None , because the indicators were already extracted earlier in the Extract email artifacts and attachments task and there is no need to extract them again. 

 Indicator extraction modes 

 Indicator extraction supports the following modes: 

 None: Indicators are not extracted automatically. Use this option when you do not want to further evaluate the indicators. 

 Inline: Indicators are extracted within the context that indicator extraction runs (synchronously). The findings are added to the context data. For example, if indicator extraction for a playbook task is inline, extraction occurs before the next playbook tasks run. 

 This configuration may delay playbook execution (issue creation). 

 While indicator creation is asynchronous, indicator extraction and enrichment are run synchronously. Data is placed into the issue context and is available via the context for subsequent tasks. 

 Out of band: Indicators are extracted in parallel (asynchronously) to other actions. The extracted data will be available within the issue, however, it is not available for immediate use in task inputs or outputs because the information is not available in real-time. 

 When using out of band, the extracted indicators do not appear in the context. If you want the extracted indicators to appear select inline. 

 If system-wide indicator extraction is enabled, indicators are extracted according to the following rules: 

 Issue creation - inline 

 Issue field change - inline 

 Tasks - none, can be overridden on a per task basis 

 CLI - out of band, but can be overridden on a per-command basis 

 Troubleshoot indicator extraction 

 If indicators are not extracted, check whether the indicator mode is set to none. Even if you select the relevant issue fields and the indicators to extract, if the mode is set to none, indicators do not extract. 

 Previous Extend context 

 Next Update issue fields with playbook tasks 

 Last updated 1 month ago 

 Was this helpful?
