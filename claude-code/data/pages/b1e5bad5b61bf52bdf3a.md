---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam-developer-guide/cortex-xsiam-development-guide/integrations-and-scripts/advanced-topics/event-collector-integrations
fetched_at: 2026-09-16T09:04:51Z
source: cortex-platform
---

# Event collector integrations | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Developer Docs 

 Cortex XSIAM Developer Guide 

 Cortex XSIAM Development Guide 

 Integrations and scripts 

 Advanced topics 

 Event collector integrations 

 Develop event collector integrations to fetch events and logs from external products to Cortex XSIAM. 

 Event collector integrations enable fetching events and logs from external products, for example from OKTA and Jira . They are developed the same as other integrations, with a few extra configuration parameters and APIs. 

 Create a Cortex XSIAM event collector integration 

 To create an event collector integration use the demisto-sdk init --xsiam command. This creates a new content pack with all necessary Cortex XSIAM content items. The event collector integration can be found at Packs/Integrations/${VENDOR_NAME}EventCollector . 

 Event collector integration naming conventions 

 Event collector integration names ( id , name , and display fields) should end with EventCollector so users can easily understand what the integration is used for. 

 Required event collector YAML keys 

 Use the demisto-sdk init --xsiam command to automatically generate the necessary integration YAML configuration keys for an event collector. If you create the YAML manually, verify the following keys are set: 

 isfetchevents key in the integration YAML file to indicate the integration is an event collector integration. 

 Must have the fromversion: 6.8.0 field. 

 The marketplaces key set with the -marketplacev2 value. This ensures that the event collector is only available for installation on Cortex XSIAM. 

 Event collector YAML example 

 Ask Copy 

 script: 
  isfetchevents: true 
 fromversion: 6.8.0 
 marketplaces: 
 - marketplacev2 

 Configure Collect section parameters 

 For event collector integration instance settings, the event collector related parameters should be organized in one section by adding the Collect key to each relevant parameter in the integration YAML file: 

 For example, since the first_fetch and fetch_limit are event collector related parameters, add them to the Collect section: 

 In the integration instance modal, it looks like this: 

 Event collector integration commands 

 Every event collector integration supports at least three commands: 

 fetch-events - This command initiates a fetch events request to specific external product endpoint(s) using the relevant chosen parameters, and sends the fetched events to the Cortex XSIAM dataset. If the integration instance setting is configured to Fetch events , then this command is executed at the specified Events Fetch Interval . By default, it runs every minute to retrieve and import events into Cortex XSIAM. 

 When creating an event collector integration with the demisto-sdk init --xsiam command, the Packs/Integrations/${VENDOR_NAME}EventCollector/${VENDOR_NAME}EventCollector.yml file includes the key script.isfetchevents: true , which indicates that the integration can fetch events. 

 test-module - This command runs when the Test button is clicked in the integration instance settings configuration. 

 <product-prefix>-get-events - This command fetches a limited number of events from the external source and displays them in the War Room. Replace <product-prefix> with the name of the product or vendor source providing the events. For example, for an event collector integration for Microsoft Intune, the command might be called msintune-get-events . 

 In the Packs/Integrations/${VENDOR_NAME}EventCollector/${VENDOR_NAME}EventCollector.yml file under the script.commands path, the SDK by default provides a hello-world-get-events command. This command is used primarily for debugging to retrieve the events that the fetch-events command would run. It includes an optional argument, should_push_events , that has the same functionality as fetch-events when set to true . 

 Send events with send_events_to_xsiam 

 Call the send_events_to_xsiam() function from CommonServerPython when the fetch-events command is executed. 

 This command expects the following arguments: 

 events The events to send to the Cortex XSIAM tenant. Should consist of one of the following: 

 List of strings or dictionaries where each string or dictionary represents an event. 

 String containing raw events separated by new lines. 

 vendor (string): The vendor represented by the event collector integration. 

 product (string): The specific product integrated in the event collector integration. 

 data_format (string) - Should only be included if the events parameter contains a string in the leef or cef format. Otherwise the data_format is set automatically. 

 Example: main() function from an event collector integration: 

 This example assumes the events are not in cef or leef formats, therefore the data_format argument is not used. 

 Important 

 The send_events_to_xsiam() function should only be used with a system integration. For custom data ingestion needs, use the HTTP Log Collector or contact support to request an official integration. 

 Always pass events to the send_events_to_xsiam() function, even if no events were fetched, because the send_events_to_xsiam() function also updates the UI for the number of events fetched, which could also be 0. Empty data will not be sent to the database. 

 Only call demisto.setLastRun after calling send_events_to_xsiam() . 

 For more info on the send_events_to_xsiam() function, see the API reference . 

 Send event data with multiple types 

 If within fetch-events different API endpoints are called, then events may consist of multiple types with different structures. In this case, call send_events_to_xsiam() with an aggregated list of events from both endpoints. For example, for detections: List[Dict[str, Any]] and audits: List[Dict[str, Any]] , send them as: 

 For more details, see https://xsoar.pan.dev/docs/reference/api/common-server-python#send_events_to_xsiam . 

 Configure the first event collection run 

 When an integration runs for the first time, the last run time is not in the integration context. To set up the first run properly, use an if statement with a time that is specified in the integration settings. 

 It is best practice to specify in the integration settings how far back in time to fetch events for the first run. 

 Configure event queries and parameters 

 Queries and parameters are configurable parameters in the integration settings that enable filtering events. For example, to import only certain event types into Cortex XSIAM, you need to query the API for only that specific event type. 

 The following example uses the First Run if statement and query . 

 Create event collector parsing rules 

 When developing an event collector integration, you can implement parsing rules in the event collector code. 

 The most common parsing rule is the _time system property, which indicates the event time from the remote system. For example, using the following events: 

 The created event property is a str representation of a timestamp (without milliseconds). However, the _time system property expects the result to be an str in format %Y-%m-%dT%H:%M:%S.000Z . Transform it using the timestamp_to_datestring function from CommonServerPython : 

 To ensure the parsing rule has been applied and is working as expected, run an XQL query to compare the _time and created fields: 

 View collected event data in Cortex XSIAM 

 After events are received by Cortex XSIAM, they are stored in a dataset in the structure of <vendor>_<product>_raw. If it's the first time fetching events, this dataset will be created. For more information about dataset management, see Dataset management . 

 To see the events sent by the send_events_to_xsiam() function in your Cortex XSIAM instance: 

 Go to the left toolbar and navigate to Incident response → Investigation → Query Builder . 

 Click the XQL button. 

 In the query builder box, type a query to search for the events you want to view. For example, to view all events type the following and then click Run . 

 You should see the events sent by your integration in the table of results. 

 Previous Fetching credentials 

 Next Feed Integrations 

 Last updated 20 days ago 

 Was this helpful?
