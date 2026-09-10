---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-on-prem/8.6/configure-cortex-xsoar/incident-configuration/classification-and-mapping
fetched_at: 2026-09-06T11:23:01Z
source: cortex-platform
---

# Classification and mapping | 8.6 (EoL) | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 8 

 Cortex XSOAR 8 On-prem Documentation 

 8.6 (EoL) 

 Configure Cortex XSOAR 

 Incident configuration 

 8.6 On-prem Cortex XSOAR EoL 

 Classification and mapping 

 Classify and map integration instances in Cortex XSOAR On-prem 8.6 (EoL). 

 The classification and mapping feature enables you to take events and event information ingested from integrations, classify the event as an incident type, and map event information to incident fields in Cortex XSOAR. 

 Note 

 Classifiers and mappers can be created with or without association to a specific integration instance and can be assigned to multiple instances. An integration can only have a classifier or only a mapper. 

 When creating a classifier and mapper, you can contribute them to the Marketplace. 

 For more information about classification and mapping, see the following video: Classification and Mapping . 

 Classification 

 Classification determines the type of incident that is created for events ingested from a specific integration. For example, Cortex XSOAR might generate alerts from Cortex Traps which you would classify either as a dedicated Traps, Authentication, or Malware incident type. 

 By classifying the events as different incident types, you can process them with different playbooks in the incident type, which is suited to their respective requirements. 

 You have the following options for classification: 

 You can hard code every alert fetched from the integration to a specific incident type, by selecting the incident type in the integration instance settings. This is useful where you want all alerts classified to a single type, such as phishing and have the same playbook execute on the same incident. 

 Most integrations produce a variety of alerts that you may want to send to separate incident types, which may use different playbook/response processes. Create an incident classifier to route alerts from the integration to incident types in Cortex XSOAR. After you create a classifier, add the classifier to an integration. For more information, see Create an incident classifier . 

 Note 

 To hard code an incident type or select a classifier in an integration instance, you may need to select Fetches incidents in the integration instance settings. 

 Some content packs include classifiers, which have incident types already classified. For example, the Cortex XDR Incident Handler - Classifier classifies events such as FirstSSOAccess and RDPBruteForce as Cortex XDR Incident types in Cortex XSOAR. 

 Mapping 

 Mapping enables you to map important information from incoming alerts into incident fields for use in playbooks and in layouts, so analysts can view the information when investigating an incident. 

 Some content packs include mappers, which have fields already mapped. For example, the XDR - Incoming Mapper includes fields such as Hostnames , LastMirroedInTime , and Occurred are already mapped. To create a mapper, see Create an incident mapper . 

 Mappers enable you to do the following: 

 When building playbooks, incidents are much easier to use and allow you to take different actions based on those fields within a playbook. 

 Most field types become searchable. For example, if you map the source username to a field, you can query that field with other incidents with the same source username. It is easier to correlate, deduplicate, query, and report. 

 Easily add fields to layouts for display and review by the analyst. 

 Perform indicator extraction based on the incident type and its fields. Extract specific indicators from specific fields. 

 Mirror content in Cortex XSOAR with third-party integrations. This enables you to make changes to an incident in Cortex XSOAR and have that change be reflected in the case managed by the integration. For example, if you are using a case management system such as JIRA or Salesforce, you can close an incident in Cortex XSOAR and have that reflected automatically. 

 Note 

 The integration must support pulling the integration schema for mirroring to work. 

 Using JSON files 

 When creating a classifier or mapper you can use the following: 

 Integration instance: The instance needs to be configured and enabled. 

 Select a schema: When supported by the integration, this pulls all of the integration fields from the database. 

 Upload a JSON file: If you can't pull samples or the samples do not retrieve sufficient data, upload a formatted JSON file. 

 The JSON file needs to be in an array of dictionaries, with each alert in its own dictionary. For example: 

 Previous Incident layout customization 

 Next Create an incident classifier 

 Last updated 1 month ago 

 Was this helpful?
