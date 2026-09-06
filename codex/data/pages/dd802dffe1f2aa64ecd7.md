---
url: https://cortex-docs.paloaltonetworks.com/python-development-quick-start-guide/cortex-xsoar-python-development-quick-start-guide/script-code-snippets
fetched_at: 2026-09-06T10:50:56Z
source: cortex-platform
---

# Script Code Snippets | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Python Development Quick Start Guide 

 Cortex XSOAR Python Development Quick Start Guide 

 Script Code Snippets 

 Code snippets for common automation script actions. 

 The following code snippets perform common actions that you can modify as needed. 

 Basic Automation Template 

 This template can be used to create a new automation, replacing the standard boilerplate provided. 

 Ask Copy 

 def main(): 
 try: 
 except Exception as ex: 
 demisto.error(traceback.format_exc()) 
 return_error("Failed to execute command: " + str(ex)) 
 if __name__ in ("__main__", "__builtin__", "builtins"):     
 main() 

 Return Results to War Room and Incident Context 

 The Common Server Python return_results() function outputs data to both the War Room and incident context. A simple example is to display context data as Markdown in the War Room and update context. The Common Server Python functions tableToMarkdown() and CommandResults() are used to prepare the results and then pass them to return_results() . 

 Ask Copy 

 markDown = tableToMarkdown("Table Name", outputContext) 
 resultsOut = CommandResults( 
 readable_output = markDown, 
 outputs_prefix = "context.path", 
 outputs_key_field = "contextFieldName", 
 outputs = outputContext 
 ) 
 return_results(resultsOut) 

 Log Errors to Cortex XSOAR Server Log 

 The Demisto class provides the demisto.error() function that logs errors to the Cortex XSOAR server log. 

 Log Errors to the War Room 

 The Common Server Python return_error() function creates error entries in the War Room. 

 An exception string can be included in the message if using try/catch to handle exceptions. 

 Access Arguments 

 The Demisto class provides the demisto.args() function to retrieve arguments passed to an automation script, for example if a Cortex XSOAR playbook task calls the automation script. 

 To retrieve multiple arguments in a Python dictionary: 

 If only a single argument is required, access the argument directly with a key name: 

 Access Incident Objects 

 The demisto.incident() function returns a Python dictionary of the incident field values. 

 If only a single field is required, access the field directly with a key name. 

 Find, Set, and Create Indicators 

 The findIndicators command queries for indicators. 

 A request to the Cortex XSOAR API (required if applying tags) updates the indicator. 

 Get and Set Incident Fields 

 To get incident field values, the demisto.incident() function returns a dictionary of all fields or a single field. 

 To set the field value, the demisto.executeCommand() function passes a dictionary of field names and field values. 

 Get and Set Incident Custom Fields 

 Incidents may include custom fields created by the Cortex XSOAR user. These are contained within the incident object as a sub-dictionary. If there are multiple fields, use the demisto.incident() function with CustomFields as the key name. Individual custom field values can then be retrieved from the dictionary. 

 If only a single custom field is required: 

 To set a custom field, a Python dictionary object with a key name that matches the field name of the value is converted to a JSON string and the demisto.executeCommand() function is called. 

 Note 

 When setting custom fields use customFields , and when retrieving custom fields use CustomFields . 

 Get and Set Grid Fields 

 Grid fields display data tables. 

 Note 

 Column names must be the machine name (lowercase version of the display name) for the column or the data is ignored. 

 Get and Set Incident Context 

 To get a context value: 

 To set a context value, use the demisto.setContext() function: 

 Get and Set Lists 

 Lists are separate from incident fields and context, and store data for use by automations. Two common list actions are getting and setting values in the list. 

 Invoke the Cortex XSOAR REST API 

 The Cortex XSOAR REST API is available for automation tasks that require different access than what is provided through automation scripts and commands. See the API documentation for each endpoint to determine the parameters to include in the body of a request. 

 To invoke an API, specify the endpoint uri , in this case /incident, and provide the body of the request in a dictionary. The following sample creates an incident with the name "Incident Name”. 

 Previous Apply Tags to Indicators 

 Next Reference 

 Last updated 25 days ago 

 Was this helpful?
