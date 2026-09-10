---
url: https://cortex-docs.paloaltonetworks.com/python-development-quick-start-guide/cortex-xsoar-python-development-quick-start-guide/development-tools-and-resources
fetched_at: 2026-09-06T10:50:56Z
source: cortex-platform
---

# Development Tools and Resources | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Python Development Quick Start Guide 

 Cortex XSOAR Python Development Quick Start Guide 

 Development Tools and Resources 

 Development tools include Demisto class, Common Server Python class, Common Scripts content pack, Cortex XSOAR IDE and script helper, and more. 

 Cortex XSOAR provides the following tools and resources to develop Python scripts. 

 Demisto Class 

 The Demisto class is a standard Python class available to all automations and integrations and provides a large number of functions, a few of which are not available in integrations. 

 Some typical functions are: 

 demisto.args() 

 demisto.incident() 

 demisto.context() 

 demisto.indicator() 

 demisto.executeCommand() 

 Common Server Python 

 The Common Server Python functions are automatically available to any automation. Common Server Python functions sit above the Demisto Class and provide simpler APIs. 

 Some typical functions are: 

 CommandResults() 

 return_results() 

 return_warning() 

 return_error() 

 Common Server User Python 

 Like Common Server Python, Common Server User Python is available to every automation. By default, it is blank. Users add common code to share with automations they create. You can override the functions in Common Server Python by creating ones with the same name in Common Server User Python. Functions created in Common Server User Python do not appear in the script helper in the Cortex XSOAR console IDE. 

 Common Scripts Content Pack 

 The Common Script content pack contains over 250 common scripts that are used for automated tasks in playbooks. 

 Demisto Python Client 

 The Demisto Python client is a Python library for the Demisto API for creating remote applications not executed by Cortex XSOAR. A Demisto client class is instantiated providing methods that access Cortex XSOAR REST API endpoints. 

 Cortex XSOAR Console IDE and Script Helper 

 The integrated IDE within the Cortex XSOAR console supports authoring scripts and integrations. It enables inserting code snippets into a script and provides basic how to descriptions of many of the functions. 

 Generic Webhook Integration 

 The Generic Webhook integration creates incidents by posting HTTPS requests to the webhook endpoint. Download the Generic Webhooks content pack from the Marketplace. Configure an integration instance to listen for requests to the Cortex XSOAR server. 

 https://<xsoar server>/instance/execute/webhook 

 Or if a non-standard HTTPS port, for example 8000, is configured in the integration instance: 

 https://<xsoar server>:8000 

 REST API 

 Scripts and the Cortex XSOAR console access the Cortex XSOAR server via its REST API. For the current list of API endpoints on your server, see the https://<xsoar server>/api URL or the API Reference Guide . This list changes with Cortex XSOAR builds and releases. 

 Demisto SDK 

 The Demisto SDK is a Python library that validates Cortex XSOAR entities being developed and assists interaction between your development environment and Cortex XSOAR. Commands are available to package content for inclusion in the Cortex XSOAR server and to release content to Marketplace. 

 Cortex XSOAR Extension for Visual Studio Code 

 Visual Studio Code and the Cortex XSOAR extension are used for creating and publishing custom content packs for the Marketplace. It is installed along with the Demisto SDK, and a local clone of the GitHub demisto content repository is created. Docker is used for executing Python code linting tools against Python code. Creating mock functions of the Demisto class enables local debugging in Visual Studio Code. For authoring automations and simple integrations as part of Cortex XSOAR playbooks, using the XSOAR IDE in the Cortex XSOAR console with the Script Helper is a simpler approach. 

 Troubleshooting 

 Cortex XSOAR provides development debugging and diagnostics tools. For additional information, see the Troubleshooting Guide . 

 Cortex XSOAR Playbook Debugging 

 When developing a playbook, you can use the playbook debugger for testing. 

 Commands entered on the Cortex XSOAR command line can have the debug-mode=true argument added: 

 <XSOAR command> <command arguments> debug-mode=true 

 In the incident’s War Room or the Cortex XSOAR playground entry, there is a Download link with detailed logging from the command. 

 For details on the debugger, see Debug a Playbook . 

 Cortex XSOAR Automation Diagnostics 

 Diagnostic outputs from Cortex XSOAR scripts can be sent to an incident’s War Room or during testing in the playground using Demisto Class or Common Server Python functions: 

 CommandResults() 

 return_results() 

 return_warning() 

 return_error() 

 LOG() 

 LOG.print_log() 

 Cortex XSOAR Server Logs 

 In the Cortex XSOAR console Settings → About → Troubleshooting , set Log Level to Debug . On the Cortex XSOAR server, the server and other logs are found at /var/log/demisto/server.log . 

 Cortex XSOAR Integration Instance Logs 

 In the Cortex XSOAR console Settings → Integrations → Instances , you can enable integration instance debug logging by setting Log Level: Debug . The integration log file is found at /var/log/demisto/integration.log . 

 Cortex XSOAR Log Bundle 

 In the Cortex XSOAR console Settings → About → Troubleshooting , select the Download Logs link to download the Cortex XSOAR log bundle for review. 

 Previous Cortex XSOAR Script Development Process 

 Next Cortex XSOAR Automation Scripts 

 Last updated 25 days ago 

 Was this helpful?
