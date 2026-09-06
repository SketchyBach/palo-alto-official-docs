---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/detect-investigate-and-respond-to-threats/investigation-and-response/response-actions/run-agent-scripts-on-an-endpoint
fetched_at: 2026-09-06T09:32:36Z
source: cortex-platform
---

# Run agent scripts on an endpoint | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSIAM 

 Cortex XSIAM Documentation 

 Detect, Investigate, and respond to threats 

 Investigation and response 

 Response actions 

 Cortex XSIAM 

 Run agent scripts on an endpoint 

 Run agent scripts to investigate, manage, and remediate endpoints from Cortex XSIAM. 

 For enhanced endpoint remediation and endpoint management, you can run Python 3.7 scripts on your endpoints directly from Cortex XSIAM. For commonly used actions, Cortex XSIAM provides out-of-the-box scripts. You can also write and upload your own Python scripts and code snippets into Cortex XSIAM for custom actions. Cortex XSIAM enables you to manage, run, and track the script execution on the endpoints, and store and display the execution results per endpoint. 

 To run scripts on an endpoint, you must have the following system requirements: 

 Endpoints running the Agent v7.1 and later. Since the agent uses its built-in capabilities and many available Python modules to execute the scripts, no additional setup is required on the endpoint. 

 Role in the hub with the following permissions to run and configure scripts: 

 Run Standard scripts 

 Run High-risk scripts 

 Script configuration (required to upload a new script, run a snippet, and edit an existing script) 

 Scripts (required to view the Scripts Library and the script execution results) 

 Running snippets requires both Run High-risk scripts and Script configuration permissions. Additionally, all scripts are executed as System User on the endpoint. 

 Manage scripts in the Scripts Library 

 Your scripts are available in the Action Center → Scripts Library , including out-of-the-box scripts and custom scripts. From the Scripts Library , you can view the script code and metadata, and perform the following actions from the right-click pivot menu: 

 Download script: Download the Python code file locally. 

 View/Download definitions file: View or download the script metadata. 

 Run: Run the selected script. Cortex XSIAM redirects you to the Action Center where the details of this script are populated in the new action fields. 

 Edit: Edit the script code or metadata. This option is not available for the out-of-the-box scripts. 

 The following table describes the default and optional fields that you can view in the Scripts Library . The fields are in alphabetical order. 

 Field 

 Description 

 Compatible OS 

 Operating systems with which the script is compatible. 

 Created By 

 User who created the script. For out-of-the-box scripts, the user name is Palo Alto Networks. 

 Description 

 Script description is an optional field that can be completed when creating, uploading, or editing a script. 

 Id 

 Unique ID assigned by Cortex XSIAM to identify the script. 

 Modification Date 

 Date and time in which the script or its attributes were last edited. 

 Name 

 Script name is a mandatory field that can be completed when creating, uploading, or editing a script. 

 Outcome 

 High-risk: Scripts that may potentially harm the endpoint. 

 Standard: Scripts that do not have a harmful impact on the endpoint. 

 Script FileSHA256 

 SHA256 of the code file. 

 Out-of-the-box scripts 

 Palo Alto Networks provides out-of-the-box scripts. You can view the scripts, download the script code and metadata, and duplicate the scripts, however you cannot edit the code or definitions of out-of-the-box scripts. 

 The following table lists the out-of-the-box scripts provided by Palo Alto Networks, in alphabetical order. New scripts are continuously uploaded into Cortex XSIAM through content updates, and are labeled New for a period of three days. 

 Script name 

 Description 

 delete_file 

 Delete a file on the endpoint according to the full path. 

 file_exists 

 Search for a specific file on the endpoint according to the full path. 

 get_process_list 

 List CPU and memory for all processes running on the endpoint. 

 list_directories 

 List all directories under a specific path on the endpoint. You can limit the number of levels you want to list. 

 process_kill_cpu 

 Set a minimum CPU value and kill all process on the endpoint that are using higher CPU. 

 process_kill_mem 

 Set a minimum RAM usage in bytes and kill all process on the endpoint that are using higher private memory. 

 process_kill_name 

 Kill all processes by a given name. 

 *registry_delete 

 (Windows) 

 Delete a Registry key or value on the endpoint. 

 *registry_get 

 (Windows) 

 Retrieve a Registry value from the endpoint. 

 *registry_set 

 (Windows) 

 Set a Registry value from the endpoint. 

 *Since all scripts are running under System context, you cannot perform any registry operations on user-specific hives (HKEY_CURRENT_USER of a specific user). 

 Upload your scripts 

 You can write and upload scripts to the Scripts Library . 

 Go to Action Center → Agent Script Library and select New Script . 

 Drag your script file into the window, or browse and select it. During upload, Cortex XSIAM parses the script to ensure you are using only supported Python modules. Click supported modules to view the supported modules list. If your script is using unsupported Python modules, or if your script is not using proper indentation, you will be required to fix it. You can use the editor to update your script directly in Cortex XSIAM. 

 Add metadata to your script. 

 You can enter the field definitions manually, or upload a definitions file to automatically enter the definitions. The definitions file must use exact script manifest format. To view the manifest format and create your own, see Create a script manifest. 

 Complete the following fields: 

 General: Specify the general script definitions including name and description, risk categorization, supported operating systems, and timeout in seconds. 

 Input: Set the starting execution point of your script code. To execute the script line by line, select Just run . Alternatively, to set a specific function in the code as the entry point, select Run by entry point . Select the function from the list, and specify for each function parameter its type. 

 script-upload-input.png 

 Output: If your script returns an output, specify the output type. Cortex XSIAM displays this information in the script results table. 

 Single parameter: If the script returns a single parameter, select the output type from the list and the output will be displayed as is. To detect the type automatically, select Auto Detect . 

 Dictionary: If the script returns multiple values, select Dictionary . By default, Cortex XSIAM displays the dictionary value as is in the script results table. 

 To improve the display of the script results table and enable filtering, you can assign user-friendly names and types to your dictionary keys. 

 script-upload-output2.png 

 To retrieve files from the endpoint, add the files_to_get key to the dictionary. This key includes an array of paths from which files will be retrieved from the endpoint. 

 When you are finished, create the new script. The script is uploaded to the Scripts Library . 

 Create a script manifest 

 You can create a script manifest to automatically enter file definitions for a script. For more information, see Step 2 in Upload your scripts. 

 The script manifest file that you upload into Cortex XSIAM has to be a single-line textual file, in the exact format explained below. If your file is structured differently, the manifest validation will fail and you will be required to fix the file. 

 Example 

 This is an example of the manifest file structure and content. 

 In this example, we are showing each parameter in a new line. However, when you create your file, you must remove any \n or \t characters. 

 Always use lowercase for variable names. 

 How to create a script manifest 

 Type the script name and description. 

 You can use letters and digits. Avoid the use of special characters. 

 Categorize the script. 

 If a script is potentially harmful, set it as High— Risk to limit the user roles that can run it. Otherwise, set it as Standard. 

 Assign the platform. 

 Enter the name of the operating system this script supports. The options are Windows, macOS, and Linux. If you need to define more than one, use a comma as a separator. 

 Set the script timeout. 

 Enter the number of seconds after which Cortex XSIAM agent halts the script execution on the endpoint. 

 Configure the script input and output. 

 To Run by entry point , you must specify the entry point name, and all input and output definitions. 

 The available parameter types are: 

 auto_detect 

 boolean 

 number 

 string 

 ip 

 number_list 

 string_list 

 ip_list 

 To set the script to Just run , leave both the Entry_point and Entry_point_definitions empty: 

 Example 

 Track script execution 

 When you run a script, you can see the script execution in the Action Center and track the script execution status. The Status indicates the action's progress, which includes the general action status and the breakdown by endpoints included in the action. The following table lists the possible status of a script execution action for each endpoint, in alphabetical order: 

 Status 

 Description 

 Aborted 

 The script execution action was aborted after it was already in progress on the endpoint. 

 Canceled 

 The script execution action was canceled before the agent pulled the request from the server. 

 Completed Successfully 

 The script was executed successfully on the endpoint with no exceptions. 

 Expired 

 The script execution actions expire after four days. After an action expires, the status of any remaining pending actions on endpoints changes to Expired and these endpoints will not receive the action. 

 Failed 

 A script can fail due to these reasons: 

 The agent failed to execute the script. 

 Exceptions occurred during the script execution. 

 In Progress 

 The agent pulled the script execution request. 

 Pending 

 The agent has not yet pulled the script execution request from the server. 

 Pending Abort 

 The agent is in the process of executing the script, and has not pulled the abort request from the server yet. 

 Timeout 

 The script execution reached its configured time out and the agent stopped the execution on the endpoint. 

 Open script in Interactive Mode 

 You can use Interactive Mode to dynamically track the script execution progress on all target endpoints and view the results as they are being received in real-time. Additionally, you can start executing more scripts on the same scope of target endpoints. 

 To initiate Interactive Mode for a script that is already running, in the Action Center , right-click the execution action of the relevant script and select Open in interactive mode . 

 Cancel or abort script execution 

 You can cancel or abort a script execution action for Pending and In Progress actions: 

 When the script execution action is Pending , the agent has not yet pulled the request from the Cortex XSIAM server. When you cancel a pending action, the server pulls back the request and updates the action status to Canceled . To cancel the action for all pending endpoints, go to the Action Center , right-click the action and Cancel for pending endpoints . Alternatively, to cancel a pending action for specific endpoints, go to Action Center → Additional data → Detailed Results , right-click the endpoint(s) and Cancel pending action . 

 When the script execution action is In Progress , the agent has begun running the script on the endpoint. When you abort an action that is in progress, the agent halts the script execution on the endpoint and updates the action status to Aborted . To abort the action for all In Progress endpoints and cancel the action for any Pending endpoints, go to the Action Center , right-click the action and Abort and cancel execution . Alternatively, to abort an in progress action for specific endpoints, go to Action Center → Additional data → Detailed Results , right-click the endpoints and Abort for endpoint in progress . 

 View script execution results 

 Cortex XSIAM logs all script execution actions, including the script results and the parameters specified when running the script. To view full details about the run, including returned values, right-click the script and select Additional data . 

 The script results are divided into the upper bar and the main view. The upper bar displays the script meta-data including the script name and entry point, the script execution action status, the parameter values used in this run and the target endpoints scope. You can also download the exact code used in this run as a py file. 

 The main view displays the script execution results as follows: 

 Main results view: Displays a table listing all target endpoints and their details. 

 In addition to the endpoint details (name, IP, domain, etc), the following table describes the default and additional optional fields that you can view per endpoint. The fields are in alphabetical order. 

 Field 

 Description 

 * Returned values 

 If your script returned values, the values are also listed in the additional data table according to your script output definitions. 

 Execution timestamp 

 Date and time the agent started the script execution on the endpoint. If the execution has not started yet, this field is empty. 

 Failed files 

 Number of files the agent failed to retrieve from the endpoint. 

 Retention date 

 Date after which the retrieved file will no longer be available for download. The value is 90 days from the execution date. 

 Retrieved files 

 Number of files that were successfully retrieved from the endpoint. 

 Status 

 See the list of statuses and their descriptions in Track script execution. 

 Standard output 

 The returned stdout 

 For each endpoint, you can right-click to download the script stdout , download retrieved files, and view returned exceptions. You can also Export to file to download the detailed results table in TSV format. 

 Aggregated results: A visualization of the script results. Cortex XSIAM automatically aggregates only results that have a small variety of values. To see how many of the script results were aggregated successfully, see the counts on the toggle (for example, aggregated results 4/5). You can filter the results to adjust the endpoints considered in the aggregation. You can also generate a PDF report of the aggregated results view. 

 Rerun a script 

 You can select a script execution action in the Action Center and rerun it. When you rerun a script, the same parameter values, target endpoints, and defined timeout are used, as defined in the previous run. However, you can make changes to the script before rerunning it. In addition, if the target endpoints in the original run were defined using a filter, the filter will be recalculated when you rerun the script. 

 Cortex XSIAM uses the current version of the script. If the script has been deleted or the supported operating system definition has been modified the since the previous run, you will not be able to rerun the script. 

 From the Action Center , right-click the script you want to rerun and select Rerun . 

 You are redirected to the final summary stage of the script execution action. 

 Run the script. 

 To run the script with the same parameters and on the same target endpoints as the previous run, click Done . To change any of the previous run definitions, navigate through the wizard and make the necessary changes. Then, click Done . The script execution action is added to the Action Center . 

 Troubleshoot script execution 

 To understand why a script returned Failed execution status, you can take the following actions: 

 Check script exceptions: If the script generated exceptions, you can view them to learn why the script execution failed. From the Action Center , right-click the Failed script and select Additional data . In the Script Results table, right-click an endpoint for which the script execution failed and select View exceptions . The agent executes scripts on Windows endpoints as a SYSTEM user, and on Mac and Linux endpoints as a root user. These context differences could cause differences in behavior, for instance when using environment variables. 

 Validate custom scripts: If a custom script that you uploaded failed, and the reason the script failed is still unclear from the exceptions or if the script did not generate any exceptions, try to identify whether it failed due to an error in Cortex XSIAM or an error in the script. To identify the error source, execute the script without the agent on the same endpoint with regular Python 3.7 installation. If the script execution is unsuccessful, you should fix your script. Otherwise, if the script was executed successfully with no errors, contact Customer Support. 

 Disable script execution 

 If you want to prevent Cortex XSIAM from running scripts on an agent, you can disable this capability during agent installation, or through Endpoint Administration. Disabling script execution is irreversible. If you want to re-enable this capability on the endpoint, you must reinstall the agent. For more information, see the Cortex XDR Agent Administrator’s Guide. 

 Disabling Script Execution does not take effect on scripts that are in progress. 

 Previous Pause endpoint protection 

 Next Remediate changes from malicious activity 

 Last updated 10 days ago 

 Was this helpful?
