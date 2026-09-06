---
url: https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/cases-and-issues/investigation-and-response/automation/playbooks/build-your-playbook/add-objects-from-the-task-library/add-commands-and-scripts
fetched_at: 2026-09-06T09:55:45Z
source: cortex-platform
---

# Add commands and scripts | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Cortex CLOUD Runtime Security 

 Cases and issues 

 Investigation and response 

 Automation 

 Playbooks 

 Build your playbook 

 Add objects from the Task Library 

 Add commands and scripts 

 Add command and script tasks to a playbook. 

 Adding commands and scripts to playbooks enables automating repetitive tasks and executing custom actions to enhance efficiency and streamline workflow processes. 

 If you want to add a script that is not yet adopted, Cortex Cloud automatically installs the content pack containing the script. If the script requires an integration instance, you are prompted to configure one. 

 From the Task Library pane, click Commands & Scripts . 

 Search for a specific script, or click an integration from the list. 

 If you click an integration, it expands to show all the scripts it includes.

 If you require a custom script, use the Agentic Assistant with the Automation Engineer agent to leverage the Cortex Agentic built-in LLM to quickly and efficiently generate functional Python scripts from natural language prompts. For more information, see Create a script . 

 Hover over the script you want and drag it onto the playbook editor. The Task Details pane opens. 

 A green check mark next to the script indicates the script is adopted and the integration instance containing the script is configured. 

 You are notified if any relevant integration instances require updates. Once installed, you are prompted to configure integration instance settings. 

 If the content pack containing the script you want is not installed, it will automatically install. You then configure an integration instance, if required, by clicking Create an instance now. 

 If the script belongs to multiple content packs, select from a drop down list which one to install. 

 If you add the script and it requires an integration instance, Cortex Cloud indicates you need to set up an integration to run the script. 

 If you do not have permission to download the script, contact your administrator for help. You can also filter by "show only configured" to show scripts you can use. 

 In the integration instance settings pane, enter values for the settings fields. 

 Click Save & Exit for the integration instance. 

 Select the Task Type the script will be based on, either Standard Task or Conditional Task . 

 Standard task: Use a Standard task when you want to perform a manual or automated action as part of a workflow, for example, when an analyst needs to confirm information or escalate a case. 

 Conditional task: Use a Conditional task to validate conditions based on values or parameters and take appropriate direction in the playbook workflow. 

 Configure the script or command settings as follows. 

 Tab 

 Details 

 Inputs 

 Each script has its own set of input arguments (or none). You can set each argument to a specific value (by typing directly on the line under the argument name), or you can click the curly brackets to define a source field to populate the argument. 

 Outputs 

 Each script has its own set of output arguments (or none). 

 Mapping 

 Map the output from a playbook task directly to an issue field. 

 The value for an output key populates the specified field per issue. This is a good alternative to using a task with the setIssue command. 

 The output value is dynamic and is derived from the context at the time that the task is processed. As a result, parallel tasks that are based on the same output may return inconsistent results. 

 In the Mapping tab, click Add custom output mapping . 

 Under Outputs , select the context output to map to an issue field. Click the curly brackets to see a list of the output parameters available from the script. 

 Under Field to fill, select the field that you want to populate with the output. 

 Click Save . 

 Advanced 

 Includes the following fields. 

 Register as case timeline record : If enabled, the results of the task execution appear as a record in the case timeline. If enabled, you must enter a Record name. You have the option of adding an Effective time , Description , Tags , and marking the record as evidence and adding an evidence comment.
NOTE: Only enter an Effective time if you want the same exact time recorded every time the playbook task executes. 

 Using : Choose which integration instance will execute the command, or leave empty to use all integration instances. 

 Extend context : Append the extracted results of the action to the context. For example, "newContextKey1=path1::newContextKey2=path2" returns "[path1:'aaa',path2: 'bbb', newContexKey1: 'aaa',newContextKey2:'bbb']" 

 Ignore outputs: If set to true, will not store outputs into the context (besides the extended outputs). 

 Execution timeout (seconds): Sets the command execution timeout in seconds. 

 Indicator Extraction mode: Choose when to extract indicators: 

 Use system default: This is the default setting. 

 None: Do not perform indicator extraction 

 Inline: Before other playbook tasks 

 Out of band: While other tasks are running 

 Mark results as note 

 Run without a worker 

 Skip this branch if this script/playbook is unavailable 

 Quiet Mode : When in quiet mode, tasks do not display inputs and outputs or extract indicators. Errors and warnings are still documented. You can turn quiet mode on or off at the task or playbook level. 

 Details 

 Includes the following fields. 

 Tag the result with : Add a tag to the task result. You can use the tag to filter entries in the War Room. 

 Task description (Markdown supported) : Provide a description of what this task does. You can enter objects from the context data in the description. For example, in a communication task, you can use the recipient’s email address. The value for the object is based on what appears in the context every time the task runs. 

 On Error 

 Includes the following fields. 

 Number of retries : How many times the task should retry running if there is an error. Default is 0. 

 Retry interval (seconds) : How long to wait between retries. Default is 30 seconds. 

 The maximum retry interval is 800 seconds (13.3 minutes). If you enter a value greater than 800 seconds, the retry interval will be limited to 800 seconds. 

 Error handling : How the task should behave if there is an error while running the script. Options are: 

 Stop 

 Continue 

 Continue on error path(s) 

 This option configures the task to handle potential errors that may occur when executing the current task's script. 

 Click OK. 

 Connect the task you added by dragging and dropping a wire. 

 Previous Add objects from the Task Library 

 Next Add sub-playbooks 

 Last updated 7 days ago 

 Was this helpful?
