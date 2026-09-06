---
url: https://cortex-docs.paloaltonetworks.com/xsoar-8-api/cortex-xsoar-8.x-apis/incidents
fetched_at: 2026-09-06T10:56:17Z
source: cortex-platform
---

# Incidents | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 API 

 Cortex XSOAR 

 XSOAR 8.x APIs 

 Cortex XSOAR 8.x APIs 

 Incidents 

 APIs for managing incidents 

 Create or update an incident 

 post https://api-yourfqdn /xsoar/public/v1/incident 

 Manually create a new Cortex XSOAR incident or update an existing one. 

 To update an existing incident, you must update the version parameter. For more information on updating the version parameter, see Optimistic locking and versioning. 

 To update incident custom fields, they must be in lowercase and without spaces. For example, "Scan IP" should be "scanip". To get the actual key name, you can go to Cortex XSOAR CLI and run /incident_add and look for the key that you would like to update. 

 Use createInvestigation: true to start the investigation process automatically upon creating the new incident. This will also run the appropriate playbook based on the incident type. 

 Header parameters 

 Authorization string Required 

 {api_key} 

 x-xdr-auth-id string Required 

 {api_key_id} 

 Body 

 application/json 

 closeNotes string Optional 

 Notes for closing the incident. 

 closeReason string Optional 

 The reason for closing the incident (select from existing predefined values). 

 closed string · date-time Optional 

 Use createInvestigation: true to start the investigation process automatically upon creating the new incident. This will also run the appropriate playbook based on the incident type. 
Use 'createInvestigation: false 

 createInvestigation boolean Optional 

 Use createInvestigation: true to start the investigation process automatically upon creating the new incident. This will also run the appropriate playbook based on the incident type. 

 customFields object Optional 

 Show properties 

 details string Optional 

 The details of the incident. 

 labels object · Label[] Optional 

 Labels related to incident - each label is composed of a type and value 

 Show properties 

 modified string · date-time Optional 

 Date modified. 

 name string Required 

 Incident name. 

 playbookId string Optional 

 The associated playbook for this incident. 

 rawJSON string Optional 

 reason string Optional 

 The reason an incident was closed. 

 severity number · double · max: 4 Optional 

 Severity is the incident severity 

 Example: 2 

 sla number · double Optional 

 SLAState is the incident SLA at closure time, in minutes. 

 status number · double · max: 2 Optional 

 IncidentStatus is the status of the incident 

 Example: 2 

 type string Optional 

 Incident type. 

 Example: Unclassified 

 Responses 

 200 

 Request processed successfully, but no incident was created. This can occur when conditions (for example, a pre-processing rule) prevent incident creation without generating an error. 

 201 

 Incident created successfully 

 application/json 

 400 

 Bad Request. 

 application/json 

 500 

 Internal server error. A unified status for API communication type errors. 

 application/json 

 post /xsoar/public/v1/incident 

 HTTP 

 Ask Copy 

 POST /xsoar/public/v1/incident HTTP/1.1 
 Host: api-yourfqdn 
 Authorization: text 
 x-xdr-auth-id: text 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 91 

 { 
 "details": "My test incident", 
 "name": "My test incident", 
 "severity": 2, 
 "type": "Unclassified" 
 } 

 200 

 Request processed successfully, but no incident was created. This can occur when conditions (for example, a pre-processing rule) prevent incident creation without generating an error. 

 No content 

 Create an incident from JSON 

 post https://api-yourfqdn /xsoar/public/v1/incident/json 

 Create a single incident from raw JSON. 

 Header parameters 

 authorization string Required 

 api_key 

 Example: DCdIeow0xm73EwnxjPza1tdHTfZQv2eH7bTKlTPkgBHLj8aSjFzjgTE9bQUK1DidlWLrnYRhaYQ4PCIyNrNJbMUC6DOWi8ANIn1JWpMTE2neGvoDIRsKUbj6pJ1z7Gmr 

 x-xdr-auth-id string Required 

 api_key_id 

 Example: 2841 

 Body 

 application/json 

 all boolean Optional 

 CustomFields object Optional 

 Show properties 

 overrideInvestigation boolean Optional 

 closeNotes string Optional 

 data object Optional 

 Show properties 

 columns string[] Optional 

 line string Optional 

 ids string[] Optional 

 force boolean Optional 

 originalIncidentId string Optional 

 closeReason string Optional 

 Responses 

 200 

 IncidentWrapper 

 application/json 

 IncidentWrapper is an extension of the Incident entity, which includes an additional field of changed-status for the web client 

 ShardID integer · int64 Optional 

 account string Optional 

 Account holds the tenant name so that slicing and dicing on the master can leverage bleve 

 activated string · date-time Optional 

 When was this activated 

 activatingingUserId string Optional 

 The user that activated this investigation 

 allRead boolean Optional 

 allReadWrite boolean Optional 

 attachment object · Attachment[] Optional 

 Attachments 

 Show properties 

 autime integer · int64 Optional 

 AlmostUniqueTime is an attempt to have a unique sortable ID for an incident 

 cacheVersn integer · int64 Optional 

 canvases string[] Optional 

 Canvases of the incident 

 category string Optional 

 Category 

 changeStatus string Optional 

 closeNotes string Optional 

 Notes for closing the incident 

 closeReason string Optional 

 The reason for closing the incident (select from existing predefined values) 

 closed string · date-time Optional 

 When was this closed 

 closingUserId string Optional 

 The user ID that closed this investigation 

 created string · date-time Optional 

 dbotCreatedBy string Optional 

 Who has created this event - relevant only for manual incidents 

 dbotCurrentDirtyFields string[] Optional 

 For mirroring, manage a list of current dirty fields so that we can send delta to outgoing integration 

 dbotDirtyFields string[] Optional 

 For mirroring, manage a list of dirty fields to not override them from the source of the incident 

 dbotMirrorDirection string Optional 

 DBotMirrorDirection of how to mirror the incident (in/out/both) 

 dbotMirrorId string Optional 

 DBotMirrorID of a remote system we are syncing with 

 dbotMirrorInstance string Optional 

 DBotMirrorInstance name of a mirror integration instance 

 dbotMirrorLastSync string · date-time Optional 

 The last time we synced this incident even if we did not update anything 

 dbotMirrorTags string[] Optional 

 The entry tags I want to sync to remote system 

 details string Optional 

 The details of the incident - reason, etc. 

 droppedCount integer · int64 Optional 

 DroppedCount ... 

 dueDate string · date-time Optional 

 SLA 

 feedBased boolean Optional 

 If this incident was triggered by a feed job 

 hasRole boolean Optional 

 Internal field to make queries on role faster 

 highlight object Optional 

 Show properties 

 id string Optional 

 indexName string Optional 

 insights integer · uint64 Optional 

 investigationId string Optional 

 Investigation that was opened as a result of the incoming event 

 isDebug boolean Optional 

 IsDebug ... 

 isPlayground boolean Optional 

 IsPlayGround 

 labels object · Label[] Optional 

 Labels related to incident - each label is composed of a type and value 

 Show properties 

 lastJobRunTime string · date-time Optional 

 If this incident was triggered by a job, this would be the time the previous job started 

 lastOpen string · date-time Optional 

 linkedCount integer · int64 Optional 

 LinkedCount ... 

 linkedIncidents string[] Optional 

 LinkedIncidents incidents that were marked as linked by user 

 modified string · date-time Optional 

 name string Optional 

 Incident Name - given by user 

 notifyTime string · date-time Optional 

 Incdicates when last this field was changed with a value that supposed to send a notification 

 numericId integer · int64 Optional 

 occurred string · date-time Optional 

 When this incident has really occurred 

 openDuration integer · int64 Optional 

 Duration incident was open 

 owner string Optional 

 The user who owns this incident 

 parent string Optional 

 Parent 

 phase string Optional 

 Phase 

 playbookId string Optional 

 The associated playbook for this incident 

 previousAllRead boolean Optional 

 previousAllReadWrite boolean Optional 

 previousRoles string[] Optional 

 Do not change this field manually 

 primaryTerm integer · int64 Optional 

 rawCategory string Optional 

 rawCloseReason string Optional 

 The reason for closing the incident (select from existing predefined values) 

 rawJSON string Optional 

 rawName string Optional 

 Incident RawName 

 rawPhase string Optional 

 RawPhase 

 rawType string Optional 

 Incident raw type 

 reason string Optional 

 The reason for the resolve 

 reminder string · date-time Optional 

 When if at all to send a reminder 

 roles string[] Optional 

 The role assigned to this investigation 

 runStatus string Optional 

 Run status of a job. 

 sequenceNumber integer · int64 Optional 

 severity number · double · max: 4 Optional 

 Severity is the incident severity 

 Example: 2 

 sizeInBytes integer · int64 Optional 

 sla number · double Optional 

 SLAState is the incident SLA at closure time, in minutes. 

 sortValues string[] Optional 

 sourceBrand string Optional 

 SourceBrand ... 

 sourceInstance string Optional 

 SourceInstance ... 

 status number · double · max: 2 Optional 

 IncidentStatus is the status of the incident 

 Example: 2 

 syncHash string Optional 

 todoTaskIds string[] Optional 

 ToDoTaskIDs list of to do task ids 

 type string Optional 

 Incident type 

 version integer · int64 Optional 

 xsoarHasReadOnlyRole boolean Optional 

 xsoarPreviousReadOnlyRoles string[] Optional 

 xsoarReadOnlyRoles string[] Optional 

 post /xsoar/public/v1/incident/json 

 HTTP 

 Ask Copy 

 POST /xsoar/public/v1/incident/json HTTP/1.1 
 Host: api-yourfqdn 
 authorization: DCdIeow0xm73EwnxjPza1tdHTfZQv2eH7bTKlTPkgBHLj8aSjFzjgTE9bQUK1DidlWLrnYRhaYQ4PCIyNrNJbMUC6DOWi8ANIn1JWpMTE2neGvoDIRsKUbj6pJ1z7Gmr 
 x-xdr-auth-id: 2841 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 223 

 { 
 "all": true, 
 "CustomFields": { 
 "key": "text" 
 }, 
 "overrideInvestigation": true, 
 "closeNotes": "text", 
 "data": { 
 "key": "text" 
 }, 
 "columns": [ 
 "text" 
 ], 
 "line": "text", 
 "ids": [ 
 "text" 
 ], 
 "force": true, 
 "originalIncidentId": "text", 
 "closeReason": "text" 
 } 

 200 

 IncidentWrapper 

 Ask Copy 

 { 
 "ShardID": 1, 
 "account": "text", 
 "activated": "2026-01-01T00:00:00.000Z", 
 "activatingingUserId": "text", 
 "allRead": true, 
 "allReadWrite": true, 
 "attachment": [ 
 { 
 "description": "text", 
 "isTempPath": true, 
 "name": "text", 
 "path": "text", 
 "showMediaFile": true, 
 "type": "text" 
 } 
 ], 
 "autime": 1, 
 "cacheVersn": 1, 
 "canvases": [ 
 "text" 
 ], 
 "category": "text", 
 "changeStatus": "text", 
 "closeNotes": "text", 
 "closeReason": "text", 
 "closed": "2026-01-01T00:00:00.000Z", 
 "closingUserId": "text", 
 "created": "2026-01-01T00:00:00.000Z", 
 "dbotCreatedBy": "text", 
 "dbotCurrentDirtyFields": [ 
 "text" 
 ], 
 "dbotDirtyFields": [ 
 "text" 
 ], 
 "dbotMirrorDirection": "text", 
 "dbotMirrorId": "text", 
 "dbotMirrorInstance": "text", 
 "dbotMirrorLastSync": "2026-01-01T00:00:00.000Z", 
 "dbotMirrorTags": [ 
 "text" 
 ], 
 "details": "text", 
 "droppedCount": 1, 
 "dueDate": "2026-01-01T00:00:00.000Z", 
 "feedBased": true, 
 "hasRole": true, 
 "highlight": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "id": "text", 
 "indexName": "text", 
 "insights": 1, 
 "investigationId": "text", 
 "isDebug": true, 
 "isPlayground": true, 
 "labels": [ 
 { 
 "type": "text", 
 "value": "text" 
 } 
 ], 
 "lastJobRunTime": "2026-01-01T00:00:00.000Z", 
 "lastOpen": "2026-01-01T00:00:00.000Z", 
 "linkedCount": 1, 
 "linkedIncidents": [ 
 "text" 
 ], 
 "modified": "2026-01-01T00:00:00.000Z", 
 "name": "text", 
 "notifyTime": "2026-01-01T00:00:00.000Z", 
 "numericId": 1, 
 "occurred": "2026-01-01T00:00:00.000Z", 
 "openDuration": 1, 
 "owner": "text", 
 "parent": "text", 
 "phase": "text", 
 "playbookId": "text", 
 "previousAllRead": true, 
 "previousAllReadWrite": true, 
 "previousRoles": [ 
 "text" 
 ], 
 "primaryTerm": 1, 
 "rawCategory": "text", 
 "rawCloseReason": "text", 
 "rawJSON": "text", 
 "rawName": "text", 
 "rawPhase": "text", 
 "rawType": "text", 
 "reason": "text", 
 "reminder": "2026-01-01T00:00:00.000Z", 
 "roles": [ 
 "text" 
 ], 
 "runStatus": "text", 
 "sequenceNumber": 1, 
 "severity": 2, 
 "sizeInBytes": 1, 
 "sla": 1, 
 "sortValues": [ 
 "text" 
 ], 
 "sourceBrand": "text", 
 "sourceInstance": "text", 
 "status": 2, 
 "syncHash": "text", 
 "todoTaskIds": [ 
 "text" 
 ], 
 "type": "text", 
 "version": 1, 
 "xsoarHasReadOnlyRole": true, 
 "xsoarPreviousReadOnlyRoles": [ 
 "text" 
 ], 
 "xsoarReadOnlyRoles": [ 
 "text" 
 ] 
 } 

 Search incidents by filter 

 post https://api-yourfqdn /xsoar/public/v1/incidents/search 

 Search incidents across all indices. You can filter by multiple options. 

 The maximum response size is 250 MB. If the response is larger than this, you will get an error response. 

 Note: This endpoint is not supported in multi-tenant environments. 

 Header parameters 

 authorization string Required 

 api_key 

 Example: DCdIeow0xm73EwnxjPza1tdHTfZQv2eH7bTKlTPkgBHLj8aSjFzjgTE9bQUK1DidlWLrnYRhaYQ4PCIyNrNJbMUC6DOWi8ANIn1JWpMTE2neGvoDIRsKUbj6pJ1z7Gmr 

 x-xdr-auth-id string Required 

 api_key_id 

 Example: 2841 

 Body 

 application/json 

 filter object · IncidentFilter Optional 

 IncidentFilter allows for very simple filtering. 

 Show properties 

 Responses 

 200 

 incidentSearchResponse 

 application/json 

 data object · Incident[] Optional 

 Note: CustomFields (an optional generic object type) is missing from the following definition. 

 Show properties 

 total integer Optional 

 post /xsoar/public/v1/incidents/search 

 HTTP 

 Ask Copy 

 POST /xsoar/public/v1/incidents/search HTTP/1.1 
 Host: api-yourfqdn 
 authorization: DCdIeow0xm73EwnxjPza1tdHTfZQv2eH7bTKlTPkgBHLj8aSjFzjgTE9bQUK1DidlWLrnYRhaYQ4PCIyNrNJbMUC6DOWi8ANIn1JWpMTE2neGvoDIRsKUbj6pJ1z7Gmr 
 x-xdr-auth-id: 2841 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 519 

 { 
 "filter": { 
 "andOp": true, 
 "category": [ 
 "text" 
 ], 
 "details": "text", 
 "files": [ 
 "text" 
 ], 
 "fromDate": "2026-01-01T00:00:00.000Z", 
 "id": [ 
 "text" 
 ], 
 "investigation": [ 
 "text" 
 ], 
 "level": [ 
 2 
 ], 
 "name": [ 
 "text" 
 ], 
 "notInvestigation": [ 
 "text" 
 ], 
 "page": 1, 
 "period": { 
 "by": "text", 
 "byFrom": "text", 
 "byTo": "text", 
 "field": "text", 
 "fromValue": "text", 
 "toValue": "text" 
 }, 
 "query": "text", 
 "reason": [ 
 "text" 
 ], 
 "size": 25, 
 "sort": [ 
 { 
 "asc": true, 
 "field": "text", 
 "fieldType": "text" 
 } 
 ], 
 "status": [ 
 2 
 ], 
 "timeFrame": 1, 
 "toDate": "2026-01-01T00:00:00.000Z", 
 "type": [ 
 "text" 
 ], 
 "urls": [ 
 "text" 
 ] 
 } 
 } 

 200 

 incidentSearchResponse 

 Ask Copy 

 { 
 "data": [ 
 { 
 "account": "text", 
 "activated": "2026-01-01T00:00:00.000Z", 
 "activatingingUserId": "text", 
 "allRead": true, 
 "allReadWrite": true, 
 "attachment": [ 
 { 
 "description": "text", 
 "isTempPath": true, 
 "name": "text", 
 "path": "text", 
 "showMediaFile": true, 
 "type": "text" 
 } 
 ], 
 "autime": 1682865388000000000, 
 "cacheVersn": 0, 
 "canvases": [ 
 "text" 
 ], 
 "category": "text", 
 "closeNotes": "text", 
 "closeReason": "text", 
 "closed": "2026-01-01T00:00:00.000Z", 
 "closingUserId": "text", 
 "created": "2026-01-01T00:00:00.000Z", 
 "dbotCreatedBy": "text", 
 "dbotCurrentDirtyFields": [ 
 "text" 
 ], 
 "dbotDirtyFields": [ 
 "text" 
 ], 
 "dbotMirrorDirection": "text", 
 "dbotMirrorId": "text", 
 "dbotMirrorInstance": "text", 
 "dbotMirrorLastSync": "2026-01-01T00:00:00.000Z", 
 "dbotMirrorTags": [ 
 "text" 
 ], 
 "details": "text", 
 "droppedCount": 0, 
 "dueDate": "2026-01-01T00:00:00.000Z", 
 "feedBased": true, 
 "hasRole": true, 
 "highlight": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "id": "text", 
 "investigationId": "text", 
 "isDebug": true, 
 "isPlayground": true, 
 "labels": [ 
 { 
 "type": "text", 
 "value": "text" 
 } 
 ], 
 "lastJobRunTime": "2026-01-01T00:00:00.000Z", 
 "lastOpen": "2026-01-01T00:00:00.000Z", 
 "linkedCount": 0, 
 "linkedIncidents": [ 
 "text" 
 ], 
 "modified": "2026-01-01T00:00:00.000Z", 
 "name": "text", 
 "notifyTime": "2026-01-01T00:00:00.000Z", 
 "numericId": 1, 
 "occurred": "2026-01-01T00:00:00.000Z", 
 "openDuration": 0, 
 "owner": "text", 
 "parent": "text", 
 "phase": "text", 
 "playbookId": "text", 
 "previousAllRead": true, 
 "previousAllReadWrite": true, 
 "previousRoles": [ 
 "text" 
 ], 
 "primaryTerm": 1, 
 "rawCategory": "text", 
 "rawCloseReason": "text", 
 "rawJSON": "text", 
 "rawName": "text", 
 "rawPhase": "text", 
 "rawType": "text", 
 "reason": "text", 
 "reminder": "2026-01-01T00:00:00.000Z", 
 "roles": [ 
 "text" 
 ], 
 "runStatus": "text", 
 "sequenceNumber": 1, 
 "severity": 2, 
 "sla": 1, 
 "sortValues": [ 
 "text" 
 ], 
 "sourceBrand": "text", 
 "sourceInstance": "text", 
 "status": 2, 
 "syncHash": "text", 
 "todoTaskIds": [ 
 "text" 
 ], 
 "type": "text", 
 "version": 0, 
 "xsoarHasReadOnlyRole": true, 
 "xsoarPreviousReadOnlyRoles": [ 
 "text" 
 ], 
 "xsoarReadOnlyRoles": [ 
 "text" 
 ] 
 } 
 ], 
 "total": 1 
 } 

 Create a new incident type 

 post https://api-yourfqdn /xsoar/public/v1/incidenttype 

 Create a new incident type. 

 Header parameters 

 authorization string Required 

 api_key 

 Example: DCdIeow0xm73EwnxjPza1tdHTfZQv2eH7bTKlTPkgBHLj8aSjFzjgTE9bQUK1DidlWLrnYRhaYQ4PCIyNrNJbMUC6DOWi8ANIn1JWpMTE2neGvoDIRsKUbj6pJ1z7Gmr 

 x-xdr-auth-id string Required 

 api_key_id 

 Example: 2841 

 Body 

 application/json 

 autorun boolean Optional 

 closureScript string Optional 

 extractSettings object · IncidentTypeExtractSettings Optional 

 Show properties 

 id string Optional 

 layout string Optional 

 name string Optional 

 playbookId string Optional 

 preProcessingScript string Optional 

 sla integer · int64 Optional 

 slaReminder integer · int64 Optional 

 color string Optional 

 Responses 

 200 

 IncidentType 

 application/json 

 autorun boolean Optional 

 cacheVersn integer · int64 Optional 

 closureScript string Optional 

 color string Optional 

 commitMessage string Optional 

 days integer · int64 Optional 

 daysR integer · int64 Optional 

 default boolean Optional 

 definitionId string Optional 

 detached boolean Optional 

 disabled boolean Optional 

 extractSettings object · IncidentTypeExtractSettings Optional 

 Show properties 

 fromServerVersion object · Version Optional 

 Version represents a version. 

 Show properties 

 highlight object Optional 

 Show properties 

 hours integer · int64 Optional 

 hoursR integer · int64 Optional 

 id string Optional 

 itemVersion object · Version Optional 

 Version represents a version. 

 Show properties 

 layout string Optional 

 locked boolean Optional 

 modified string · date-time Optional 

 name string Optional 

 numericId integer · int64 Optional 

 onChangeRepAlg number · double Optional 

 packID string Optional 

 packName string Optional 

 packPropagationLabels string[] Optional 

 playbookId string Optional 

 preProcessingScript string Optional 

 prevName string Optional 

 primaryTerm integer · int64 Optional 

 propagationLabels string[] Optional 

 readonly boolean Optional 

 remote boolean Optional 

 reputationCalc number · double Optional 

 sequenceNumber integer · int64 Optional 

 shouldCommit boolean Optional 

 sla integer · int64 Optional 

 slaReminder integer · int64 Optional 

 sortValues string[] Optional 

 syncHash string Optional 

 system boolean Optional 

 toServerVersion object · Version Optional 

 Version represents a version. 

 Show properties 

 vcShouldIgnore boolean Optional 

 vcShouldKeepItemLegacyProdMachine boolean Optional 

 version integer · int64 Optional 

 weeks integer · int64 Optional 

 weeksR integer · int64 Optional 

 post /xsoar/public/v1/incidenttype 

 HTTP 

 Ask Copy 

 POST /xsoar/public/v1/incidenttype HTTP/1.1 
 Host: api-yourfqdn 
 authorization: DCdIeow0xm73EwnxjPza1tdHTfZQv2eH7bTKlTPkgBHLj8aSjFzjgTE9bQUK1DidlWLrnYRhaYQ4PCIyNrNJbMUC6DOWi8ANIn1JWpMTE2neGvoDIRsKUbj6pJ1z7Gmr 
 x-xdr-auth-id: 2841 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 374 

 { 
 "autorun": true, 
 "closureScript": "text", 
 "extractSettings": { 
 "fieldCliNameToExtractSettings": { 
 "ANY_ADDITIONAL_PROPERTY": { 
 "extractAsIsIndicatorTypeId": "text", 
 "extractIndicatorTypesIDs": [ 
 "text" 
 ], 
 "isExtractingAllIndicatorTypes": true 
 } 
 }, 
 "mode": "text" 
 }, 
 "id": "text", 
 "layout": "text", 
 "name": "text", 
 "playbookId": "text", 
 "preProcessingScript": "text", 
 "sla": 1, 
 "slaReminder": 1, 
 "color": "text" 
 } 

 200 

 IncidentType 

 Ask Copy 

 { 
 "autorun": true, 
 "cacheVersn": 1, 
 "closureScript": "text", 
 "color": "text", 
 "commitMessage": "text", 
 "days": 1, 
 "daysR": 1, 
 "default": true, 
 "definitionId": "text", 
 "detached": true, 
 "disabled": true, 
 "extractSettings": { 
 "fieldCliNameToExtractSettings": { 
 "ANY_ADDITIONAL_PROPERTY": { 
 "extractAsIsIndicatorTypeId": "text", 
 "extractIndicatorTypesIDs": [ 
 "text" 
 ], 
 "isExtractingAllIndicatorTypes": true 
 } 
 }, 
 "mode": "text" 
 }, 
 "fromServerVersion": { 
 "Digits": [ 
 1 
 ], 
 "Label": "text" 
 }, 
 "highlight": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "hours": 1, 
 "hoursR": 1, 
 "id": "text", 
 "itemVersion": { 
 "Digits": [ 
 1 
 ], 
 "Label": "text" 
 }, 
 "layout": "text", 
 "locked": true, 
 "modified": "2026-01-01T00:00:00.000Z", 
 "name": "text", 
 "numericId": 1, 
 "onChangeRepAlg": 1, 
 "packID": "text", 
 "packName": "text", 
 "packPropagationLabels": [ 
 "text" 
 ], 
 "playbookId": "text", 
 "preProcessingScript": "text", 
 "prevName": "text", 
 "primaryTerm": 1, 
 "propagationLabels": [ 
 "text" 
 ], 
 "readonly": true, 
 "remote": true, 
 "reputationCalc": 1, 
 "sequenceNumber": 1, 
 "shouldCommit": true, 
 "sla": 1, 
 "slaReminder": 1, 
 "sortValues": [ 
 "text" 
 ], 
 "syncHash": "text", 
 "system": true, 
 "toServerVersion": { 
 "Digits": [ 
 1 
 ], 
 "Label": "text" 
 }, 
 "vcShouldIgnore": true, 
 "vcShouldKeepItemLegacyProdMachine": true, 
 "version": 1, 
 "weeks": 1, 
 "weeksR": 1 
 } 

 Close an incident 

 post https://api-yourfqdn /xsoar/public/v1/incident/close 

 Close the specified incident and optionally set a closing note. 

 Body 

 application/json 

 CustomFields object · CustomFields Optional 

 The keys should be the field's display name, all lowercase and without spaces. For example: Scan IP -> scanip
To get the actual key name you can also go to Cortex XSOAR CLI and run /incident_add and look for the key that you would like to update. 

 Show properties 

 id string Optional 

 closeNotes string Optional 

 Responses 

 200 

 OK 

 application/json 

 id string Optional 

 version integer Optional 

 cacheVersn integer Optional 

 modified string Optional 

 sizeInBytes integer Optional 

 dbotCreatedBy string Optional 

 CustomFields object · CustomFields Optional 

 The keys should be the field's display name, all lowercase and without spaces. For example: Scan IP -> scanip
To get the actual key name you can also go to Cortex XSOAR CLI and run /incident_add and look for the key that you would like to update. 

 Show properties 

 account string Optional 

 autime integer Optional 

 type string Optional 

 rawType string Optional 

 name string Optional 

 rawName string Optional 

 status integer Optional 

 custom_status string Optional 

 resolution_status string Optional 

 reason string Optional 

 created string Optional 

 occurred string Optional 

 closed string Optional 

 sla integer Optional 

 severity integer Optional 

 investigationId string Optional 

 labels object · Label[] Optional 

 Show properties 

 attachment any · nullable Optional 

 details string Optional 

 openDuration integer Optional 

 lastOpen string Optional 

 closingUserId string Optional 

 owner string Optional 

 activated string Optional 

 closeReason string Optional 

 rawCloseReason string Optional 

 closeNotes string Optional 

 playbookId string Optional 

 dueDate string Optional 

 reminder string Optional 

 runStatus string Optional 

 notifyTime string Optional 

 phase string Optional 

 rawPhase string Optional 

 isPlayground boolean Optional 

 rawJSON string Optional 

 parent string Optional 

 parentXDRIncident string Optional 

 retained boolean Optional 

 category string Optional 

 rawCategory string Optional 

 linkedIncidents any · nullable Optional 

 linkedCount integer Optional 

 droppedCount integer Optional 

 sourceInstance string Optional 

 sourceBrand string Optional 

 canvases any · nullable Optional 

 lastJobRunTime string Optional 

 feedBased boolean Optional 

 dbotMirrorId string Optional 

 dbotMirrorInstance string Optional 

 dbotMirrorDirection string Optional 

 dbotDirtyFields any · nullable Optional 

 dbotCurrentDirtyFields any · nullable Optional 

 dbotMirrorTags any · nullable Optional 

 dbotMirrorLastSync string Optional 

 isDebug boolean Optional 

 changeStatus string Optional 

 insights integer Optional 

 post /xsoar/public/v1/incident/close 

 HTTP 

 Ask Copy 

 POST /xsoar/public/v1/incident/close HTTP/1.1 
 Host: api-yourfqdn 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 68 

 { 
 "CustomFields": {}, 
 "id": "157447", 
 "closeNotes": "close_note_oAZROKPJ" 
 } 

 200 

 OK 

 Ask Copy 

 { 
 "id": "157447", 
 "version": 2, 
 "cacheVersn": 0, 
 "modified": "2024-02-21T12:58:29.813Z", 
 "sizeInBytes": 0, 
 "dbotCreatedBy": "user@company.com", 
 "CustomFields": { 
 "actionsoncampaignincidents": "Close", 
 "actionsonlowsimilarityincidents": "Add To Campaign", 
 "awsguarddutyconfidencescore": 0, 
 "bmcassignee": [ 
 {} 
 ], 
 "bmccustomer": [ 
 {} 
 ], 
 "bmcrequester": [ 
 {} 
 ], 
 "campaignemailsenderinstance": "rocket_gmail_instance_5p8iV9OZ", 
 "chronicleautoblockentities": "Yes", 
 "chronicleskipentityisolation": "Yes", 
 "cohesityheliosanomalystrength": 0, 
 "cohesityheliosclusterid": 0, 
 "containmentsla": { 
 "accumulatedPause": 0, 
 "breachTriggered": false, 
 "dueDate": "0001-01-01T00:00:00Z", 
 "endDate": "0001-01-01T00:00:00Z", 
 "lastPauseDate": "0001-01-01T00:00:00Z", 
 "runStatus": "idle", 
 "sla": 30, 
 "slaStatus": -1, 
 "startDate": "0001-01-01T00:00:00Z", 
 "totalDuration": 0 
 }, 
 "crowdstrikefalconbehaviourpatterndispositiondetails": [ 
 {}, 
 {}, 
 {} 
 ], 
 "cryptosimcategoryid": 0, 
 "cryptosimcorrelationid": 0, 
 "cryptosimpluginid": 0, 
 "datadogcloudsiem": [], 
 "datadogcloudsiemcustomerimpacted": false, 
 "datadogcloudsiemdetectandcreateduration": 0, 
 "datadogcloudsiemrepairtime": 0, 
 "datadogcloudsiemuserisservice": false, 
 "datadogcloudsiemuserverified": false, 
 "dataminrpulserelatedterms": [ 
 {}, 
 {}, 
 {} 
 ], 
 "dbotpredictionprobability": 0, 
 "decyfirdatadetails": [ 
 {}, 
 {}, 
 {} 
 ], 
 "detectionsla": { 
 "accumulatedPause": 0, 
 "breachTriggered": false, 
 "dueDate": "0001-01-01T00:00:00Z", 
 "endDate": "0001-01-01T00:00:00Z", 
 "lastPauseDate": "0001-01-01T00:00:00Z", 
 "runStatus": "idle", 
 "sla": 20, 
 "slaStatus": -1, 
 "startDate": "0001-01-01T00:00:00Z", 
 "totalDuration": 0 
 }, 
 "domaintoolsirisdetect": [ 
 {}, 
 {}, 
 {} 
 ], 
 "emaildeletefrombrand": "Unspecified", 
 "emaildeletetype": "soft", 
 "endpoint": [ 
 {} 
 ], 
 "externalid": "157447", 
 "extrahoprevealxdetectiondevices": [ 
 {}, 
 {}, 
 {} 
 ], 
 "extrahoprevealxmitretechniques": [ 
 {}, 
 {}, 
 {} 
 ], 
 "failedlogonevents": 0, 
 "filerelationships": [ 
 {}, 
 {}, 
 {} 
 ], 
 "fortisiemattacktactics": [ 
 {}, 
 {} 
 ], 
 "fortisiemevents": [ 
 {} 
 ], 
 "grafanapanelid": 0, 
 "incidentduration": { 
 "accumulatedPause": 0, 
 "breachTriggered": false, 
 "dueDate": "0001-01-01T00:00:00Z", 
 "endDate": "0001-01-01T00:00:00Z", 
 "lastPauseDate": "0001-01-01T00:00:00Z", 
 "runStatus": "idle", 
 "sla": 0, 
 "slaStatus": -1, 
 "startDate": "0001-01-01T00:00:00Z", 
 "totalDuration": 0 
 }, 
 "incidentrdpachehuntingstringssimilarity": [ 
 {}, 
 {}, 
 {} 
 ], 
 "incidentrdpcachehuntingstringsifter": [ 
 {}, 
 {}, 
 {} 
 ], 
 "inventasource": [ 
 {} 
 ], 
 "isactive": "true", 
 "isvpnipaddress": false, 
 "microsoftsentinelowner": [], 
 "numberoffoundrelatedalerts": 0, 
 "numberofrelatedincidents": 0, 
 "numberofsimilarfiles": 0, 
 "qintelqwatchexposures": [ 
 {}, 
 {}, 
 {} 
 ], 
 "remediationsla": { 
 "accumulatedPause": 0, 
 "breachTriggered": false, 
 "dueDate": "0001-01-01T00:00:00Z", 
 "endDate": "0001-01-01T00:00:00Z", 
 "lastPauseDate": "0001-01-01T00:00:00Z", 
 "runStatus": "idle", 
 "sla": 7200, 
 "slaStatus": -1, 
 "startDate": "0001-01-01T00:00:00Z", 
 "totalDuration": 0 
 }, 
 "riskiqautoexcludewhitelistedipaddress": "Yes", 
 "riskiqautowhitelistipaddress": "Yes", 
 "rocketfield02mxekkb": "option_f1kSTDSS", 
 "rocketfield0qietilt": [ 
 {} 
 ], 
 "rocketfield0yxt8qks": 0, 
 "rocketfield1m1nknsl": "rocket_kUrYJCYH", 
 "rocketfield2f1ram7u": false, 
 "rocketfield3d4otr42": [ 
 {} 
 ], 
 "rocketfield3degpevt": { 
 "accumulatedPause": 0, 
 "breachTriggered": false, 
 "dueDate": "0001-01-01T00:00:00Z", 
 "endDate": "0001-01-01T00:00:00Z", 
 "lastPauseDate": "0001-01-01T00:00:00Z", 
 "runStatus": "idle", 
 "sla": 1, 
 "slaStatus": -1, 
 "startDate": "0001-01-01T00:00:00Z", 
 "totalDuration": 0 
 }, 
 "rocketfield3rxb5har": { 
 "accumulatedPause": 0, 
 "breachTriggered": false, 
 "dueDate": "0001-01-01T00:00:00Z", 
 "endDate": "0001-01-01T00:00:00Z", 
 "lastPauseDate": "0001-01-01T00:00:00Z", 
 "runStatus": "idle", 
 "sla": 1, 
 "slaStatus": -1, 
 "startDate": "0001-01-01T00:00:00Z", 
 "totalDuration": 0 
 }, 
 "rocketfield3uuagwwt": "rocket_jvrHjnA7", 
 "rocketfield42q8ri0w": { 
 "accumulatedPause": 0, 
 "breachTriggered": false, 
 "dueDate": "0001-01-01T00:00:00Z", 
 "endDate": "0001-01-01T00:00:00Z", 
 "lastPauseDate": "0001-01-01T00:00:00Z", 
 "runStatus": "idle", 
 "sla": 1, 
 "slaStatus": -1, 
 "startDate": "0001-01-01T00:00:00Z", 
 "totalDuration": 0 
 }, 
 "rocketfield4ejubigq": 0, 
 "rocketfield4r4tiz6w": false, 
 "rocketfield6ipswid8": 0, 
 "rocketfield6mo51xzn": "rocket_2G5KQgOq", 
 "rocketfield7prumt0z": { 
 "accumulatedPause": 0, 
 "breachTriggered": false, 
 "dueDate": "0001-01-01T00:00:00Z", 
 "endDate": "0001-01-01T00:00:00Z", 
 "lastPauseDate": "0001-01-01T00:00:00Z", 
 "runStatus": "idle", 
 "sla": 1, 
 "slaStatus": -1, 
 "startDate": "0001-01-01T00:00:00Z", 
 "totalDuration": 0 
 }, 
 "rocketfield82dosswp": 0, 
 "rocketfield8wnmyyvc": "rocket_30PKbAUW", 
 "rocketfield9cxc2wvd": 0, 
 "rocketfield9xa0o3nq": "WZ3sR6", 
 "rocketfielda28fg0oj": { 
 "accumulatedPause": 0, 
 "breachTriggered": false, 
 "dueDate": "0001-01-01T00:00:00Z", 
 "endDate": "0001-01-01T00:00:00Z", 
 "lastPauseDate": "0001-01-01T00:00:00Z", 
 "runStatus": "idle", 
 "sla": 1, 
 "slaStatus": -1, 
 "startDate": "0001-01-01T00:00:00Z", 
 "totalDuration": 0 
 }, 
 "rocketfielda40b2sfg": 0, 
 "rocketfieldaax9wgte": [ 
 {} 
 ], 
 "rocketfieldaenrumcr": "Uo3MEg", 
 "rocketfieldbdvhqhgd": 0, 
 "rocketfieldbmhsqopn": { 
 "accumulatedPause": 0, 
 "breachTriggered": false, 
 "dueDate": "0001-01-01T00:00:00Z", 
 "endDate": "0001-01-01T00:00:00Z", 
 "lastPauseDate": "0001-01-01T00:00:00Z", 
 "runStatus": "idle", 
 "sla": 1, 
 "slaStatus": -1, 
 "startDate": "0001-01-01T00:00:00Z", 
 "totalDuration": 0 
 }, 
 "rocketfieldbp7q7pbn": 0, 
 "rocketfieldbtde7csg": 0, 
 "rocketfieldbtndlwtx": 0, 
 "rocketfieldbxvy7aci": { 
 "accumulatedPause": 0, 
 "breachTriggered": false, 
 "dueDate": "0001-01-01T00:00:00Z", 
 "endDate": "0001-01-01T00:00:00Z", 
 "lastPauseDate": "0001-01-01T00:00:00Z", 
 "runStatus": "idle", 
 "sla": 1, 
 "slaStatus": -1, 
 "startDate": "0001-01-01T00:00:00Z", 
 "totalDuration": 0 
 }, 
 "rocketfieldbzxrevrq": { 
 "accumulatedPause": 0, 
 "breachTriggered": false, 
 "dueDate": "0001-01-01T00:00:00Z", 
 "endDate": "0001-01-01T00:00:00Z", 
 "lastPauseDate": "0001-01-01T00:00:00Z", 
 "runStatus": "idle", 
 "sla": 1, 
 "slaStatus": -1, 
 "startDate": "0001-01-01T00:00:00Z", 
 "totalDuration": 0 
 }, 
 "rocketfieldc04gzmja": 0, 
 "rocketfieldcfdrg1gv": 0, 
 "rocketfieldcfzmni5r": { 
 "accumulatedPause": 0, 
 "breachTriggered": false, 
 "dueDate": "0001-01-01T00:00:00Z", 
 "endDate": "0001-01-01T00:00:00Z", 
 "lastPauseDate": "0001-01-01T00:00:00Z", 
 "runStatus": "idle", 
 "sla": 1, 
 "slaStatus": -1, 
 "startDate": "0001-01-01T00:00:00Z", 
 "totalDuration": 0 
 }, 
 "rocketfieldcjngz1hr": false, 
 "rocketfieldd9wodnig": false, 
 "rocketfielddiucwg95": 0, 
 "rocketfielddiwd4pdj": 0, 
 "rocketfielddpma6rxc": [ 
 {} 
 ], 
 "rocketfielddpydb2ts": "rocket_mCQCvo20", 
 "rocketfielde2kkcgrh": 0, 
 "rocketfieldeixka2g7": 0, 
 "rocketfieldeyincu1n": false, 
 "rocketfieldeyw5e4sm": 0, 
 "rocketfieldf0mrcm8q": [ 
 {} 
 ], 
 "rocketfieldf1zopnib": 0, 
 "rocketfieldfd8noctx": false, 
 "rocketfieldfvaoecwo": false, 
 "rocketfieldgcjnl61d": 0, 
 "rocketfieldgkraobgl": 0, 
 "rocketfieldh5kqjhzc": 0, 
 "rocketfieldhx9vm4pc": false, 
 "rocketfieldi3yadn4o": false, 
 "rocketfieldiuoszzbg": { 
 "accumulatedPause": 0, 
 "breachTriggered": false, 
 "dueDate": "0001-01-01T00:00:00Z", 
 "endDate": "0001-01-01T00:00:00Z", 
 "lastPauseDate": "0001-01-01T00:00:00Z", 
 "runStatus": "idle", 
 "sla": 1, 
 "slaStatus": -1, 
 "startDate": "0001-01-01T00:00:00Z", 
 "totalDuration": 0 
 }, 
 "rocketfieldivotdorp": "rocket_LfKMcWj5", 
 "rocketfieldj8zkfsym": [ 
 {} 
 ], 
 "rocketfieldjbpbuedw": { 
 "accumulatedPause": 0, 
 "breachTriggered": false, 
 "dueDate": "0001-01-01T00:00:00Z", 
 "endDate": "0001-01-01T00:00:00Z", 
 "lastPauseDate": "0001-01-01T00:00:00Z", 
 "runStatus": "idle", 
 "sla": 1, 
 "slaStatus": -1, 
 "startDate": "0001-01-01T00:00:00Z", 
 "totalDuration": 0 
 }, 
 "rocketfieldjiar3e0a": "rocket_12IRzenM", 
 "rocketfieldjj5vb0lk": 0, 
 "rocketfieldkethuvyk": { 
 "accumulatedPause": 0, 
 "breachTriggered": false, 
 "dueDate": "0001-01-01T00:00:00Z", 
 "endDate": "0001-01-01T00:00:00Z", 
 "lastPauseDate": "0001-01-01T00:00:00Z", 
 "runStatus": "idle", 
 "sla": 1, 
 "slaStatus": -1, 
 "startDate": "0001-01-01T00:00:00Z", 
 "totalDuration": 0 
 }, 
 "rocketfieldkpgyu158": [ 
 {} 
 ], 
 "rocketfieldkun3mu2u": false, 
 "rocketfieldl9vibxon": 0, 
 "rocketfieldlyefflpk": { 
 "accumulatedPause": 0, 
 "breachTriggered": false, 
 "dueDate": "0001-01-01T00:00:00Z", 
 "endDate": "0001-01-01T00:00:00Z", 
 "lastPauseDate": "0001-01-01T00:00:00Z", 
 "runStatus": "idle", 
 "sla": 1, 
 "slaStatus": -1, 
 "startDate": "0001-01-01T00:00:00Z", 
 "totalDuration": 0 
 }, 
 "rocketfieldmc5sbbxx": 0, 
 "rocketfieldmnuezx1q": "rocket_bU5TjVJf", 
 "rocketfieldmsxznc2y": 0, 
 "rocketfieldnlyjpp21": false, 
 "rocketfieldnqjoehxl": [ 
 {} 
 ], 
 "rocketfieldo1yxp4dy": [ 
 {} 
 ], 
 "rocketfieldo4zg2bva": { 
 "accumulatedPause": 0, 
 "breachTriggered": false, 
 "dueDate": "0001-01-01T00:00:00Z", 
 "endDate": "0001-01-01T00:00:00Z", 
 "lastPauseDate": "0001-01-01T00:00:00Z", 
 "runStatus": "idle", 
 "sla": 1, 
 "slaStatus": -1, 
 "startDate": "0001-01-01T00:00:00Z", 
 "totalDuration": 0 
 }, 
 "rocketfieldobcuclor": 0, 
 "rocketfieldohqjmx5w": false, 
 "rocketfieldoizbgs9u": 0, 
 "rocketfieldoobhwdtf": 0, 
 "rocketfieldooiszo3v": false, 
 "rocketfieldoq4ib3rq": { 
 "accumulatedPause": 0, 
 "breachTriggered": false, 
 "dueDate": "0001-01-01T00:00:00Z", 
 "endDate": "0001-01-01T00:00:00Z", 
 "lastPauseDate": "0001-01-01T00:00:00Z", 
 "runStatus": "idle", 
 "sla": 1, 
 "slaStatus": -1, 
 "startDate": "0001-01-01T00:00:00Z", 
 "totalDuration": 0 
 }, 
 "rocketfieldoupkddj1": { 
 "accumulatedPause": 0, 
 "breachTriggered": false, 
 "dueDate": "0001-01-01T00:00:00Z", 
 "endDate": "0001-01-01T00:00:00Z", 
 "lastPauseDate": "0001-01-01T00:00:00Z", 
 "runStatus": "idle", 
 "sla": 1, 
 "slaStatus": -1, 
 "startDate": "0001-01-01T00:00:00Z", 
 "totalDuration": 0 
 }, 
 "rocketfieldoz7n7gdi": false, 
 "rocketfieldphyivfgh": "rocket_vvOoi235", 
 "rocketfieldpn5nx1qc": 0, 
 "rocketfieldppnjqnl3": 0, 
 "rocketfieldpqkofav0": 0, 
 "rocketfieldpsjrp4kv": { 
 "accumulatedPause": 0, 
 "breachTriggered": false, 
 "dueDate": "0001-01-01T00:00:00Z", 
 "endDate": "0001-01-01T00:00:00Z", 
 "lastPauseDate": "0001-01-01T00:00:00Z", 
 "runStatus": "idle", 
 "sla": 1, 
 "slaStatus": -1, 
 "startDate": "0001-01-01T00:00:00Z", 
 "totalDuration": 0 
 }, 
 "rocketfieldptulavso": false, 
 "rocketfieldpufesh2i": { 
 "accumulatedPause": 0, 
 "breachTriggered": false, 
 "dueDate": "0001-01-01T00:00:00Z", 
 "endDate": "0001-01-01T00:00:00Z", 
 "lastPauseDate": "0001-01-01T00:00:00Z", 
 "runStatus": "idle", 
 "sla": 1, 
 "slaStatus": -1, 
 "startDate": "0001-01-01T00:00:00Z", 
 "totalDuration": 0 
 }, 
 "rocketfieldpx6wjuum": "rocket_5ryg2EXl", 
 "rocketfieldqbd6s83a": false, 
 "rocketfieldqe6qneof": false, 
 "rocketfieldqkco0yde": [ 
 {} 
 ], 
 "rocketfieldqku2kt7j": "rocket_8lraojiF", 
 "rocketfieldqp0o4lmh": "rocket_BlnkYAhj", 
 "rocketfieldqub0kxf8": { 
 "accumulatedPause": 0, 
 "breachTriggered": false, 
 "dueDate": "0001-01-01T00:00:00Z", 
 "endDate": "0001-01-01T00:00:00Z", 
 "lastPauseDate": "0001-01-01T00:00:00Z", 
 "runStatus": "idle", 
 "sla": 1, 
 "slaStatus": -1, 
 "startDate": "0001-01-01T00:00:00Z", 
 "totalDuration": 0 
 }, 
 "rocketfieldqyeq7xpv": "rocket_Sj6ZQfYt", 
 "rocketfieldrbxb2vfr": 0, 
 "rocketfieldrhbldnmx": 0, 
 "rocketfieldrqskwjv8": [ 
 {} 
 ], 
 "rocketfieldsbwfoqdv": { 
 "accumulatedPause": 0, 
 "breachTriggered": false, 
 "dueDate": "0001-01-01T00:00:00Z", 
 "endDate": "0001-01-01T00:00:00Z", 
 "lastPauseDate": "0001-01-01T00:00:00Z", 
 "runStatus": "idle", 
 "sla": 1, 
 "slaStatus": -1, 
 "startDate": "0001-01-01T00:00:00Z", 
 "totalDuration": 0 
 }, 
 "rocketfieldsiqptqqu": 0, 
 "rocketfieldstsfbljv": "option_2lPBa2b4", 
 "rocketfieldt5u0tvi2": 0, 
 "rocketfieldtb9lekl5": 0, 
 "rocketfieldtbazi7yi": false, 
 "rocketfieldthprm0ui": false, 
 "rocketfieldthtty9nn": false, 
 "rocketfieldtzpheljw": { 
 "accumulatedPause": 0, 
 "breachTriggered": false, 
 "dueDate": "0001-01-01T00:00:00Z", 
 "endDate": "0001-01-01T00:00:00Z", 
 "lastPauseDate": "0001-01-01T00:00:00Z", 
 "runStatus": "idle", 
 "sla": 1, 
 "slaStatus": -1, 
 "startDate": "0001-01-01T00:00:00Z", 
 "totalDuration": 0 
 }, 
 "rocketfieldua8dwttq": 0, 
 "rocketfieldudib0zul": "rocket_P0vSojZn", 
 "rocketfielduo7lgqj9": 0, 
 "rocketfieldurfk9syh": "OnushD", 
 "rocketfieldv2iglhei": "ATGQkF", 
 "rocketfieldvh1ydrmm": "option_PKIbNz9h", 
 "rocketfieldvi5jxbxt": 0, 
 "rocketfieldvsehzb8s": [ 
 {} 
 ], 
 "rocketfieldvx1mztgq": 0, 
 "rocketfieldwawulkzu": false, 
 "rocketfieldwl53df56": { 
 "accumulatedPause": 0, 
 "breachTriggered": false, 
 "dueDate": "0001-01-01T00:00:00Z", 
 "endDate": "0001-01-01T00:00:00Z", 
 "lastPauseDate": "0001-01-01T00:00:00Z", 
 "runStatus": "idle", 
 "sla": 1, 
 "slaStatus": -1, 
 "startDate": "0001-01-01T00:00:00Z", 
 "totalDuration": 0 
 }, 
 "rocketfieldwnzdgwsa": 0, 
 "rocketfieldwxyx6ugg": 0, 
 "rocketfieldwyw5iw48": "rocket_0xYBncbK", 
 "rocketfieldxf0uuduk": 0, 
 "rocketfieldxkevyilp": 0, 
 "rocketfieldxrbpjhnc": [ 
 {} 
 ], 
 "rocketfieldxsd42019": 0, 
 "rocketfieldxtmm8ix9": { 
 "accumulatedPause": 0, 
 "breachTriggered": false, 
 "dueDate": "0001-01-01T00:00:00Z", 
 "endDate": "0001-01-01T00:00:00Z", 
 "lastPauseDate": "0001-01-01T00:00:00Z", 
 "runStatus": "idle", 
 "sla": 1, 
 "slaStatus": -1, 
 "startDate": "0001-01-01T00:00:00Z", 
 "totalDuration": 0 
 }, 
 "rocketfieldxw7hsi6s": 0, 
 "rocketfieldxyqyxhpn": 0, 
 "rocketfieldyfutodrw": false, 
 "rocketfieldym2kvwjh": { 
 "accumulatedPause": 0, 
 "breachTriggered": false, 
 "dueDate": "0001-01-01T00:00:00Z", 
 "endDate": "0001-01-01T00:00:00Z", 
 "lastPauseDate": "0001-01-01T00:00:00Z", 
 "runStatus": "idle", 
 "sla": 1, 
 "slaStatus": -1, 
 "startDate": "0001-01-01T00:00:00Z", 
 "totalDuration": 0 
 }, 
 "rocketfieldzfml4ce0": false, 
 "rocketfieldzgsjduqe": "rocket_lTsQkUAH", 
 "rsametasevents": [], 
 "rsarawlogslist": [], 
 "saassecuritycategory": "no_reason", 
 "saassecurityremediationtype": "Remove public sharing", 
 "saassecurityremoveinheritedsharing": false, 
 "saassecuritystate": "open", 
 "saassecuritystatus": "open-new", 
 "securitypolicymatch": [ 
 {} 
 ], 
 "selectaction": "Close", 
 "servicenowbusinessimpact": "1 - Critical", 
 "servicenowcategory": "Inquiry / Help", 
 "servicenowimpact": "1 - High", 
 "servicenownotify": "Send Email", 
 "servicenowpriority": "1 - Critical", 
 "servicenowseverity": "1 - High", 
 "servicenowsircategory": "Confidential personal identity data exposure", 
 "servicenowsirstate": "New", 
 "servicenowstate": "1 - New", 
 "servicenowurgency": "1 - High", 
 "similarincidentsdbot": [ 
 {} 
 ], 
 "solarwindsacknowledged": false, 
 "solarwindsactivealertid": 0, 
 "solarwindsalertid": 0, 
 "solarwindsalertobjectid": 0, 
 "solarwindsalertrelatednodeid": 0, 
 "solarwindseventengineid": 0, 
 "solarwindseventid": 0, 
 "solarwindseventnetobjectid": 0, 
 "solarwindsinstancesiteid": 0, 
 "spycloudcompassdevicedata": [ 
 {}, 
 {}, 
 {} 
 ], 
 "suspiciousexecutions": [ 
 {}, 
 {}, 
 {} 
 ], 
 "testivan": false, 
 "thehiveflag": false, 
 "timetoassignment": { 
 "accumulatedPause": 0, 
 "breachTriggered": false, 
 "dueDate": "0001-01-01T00:00:00Z", 
 "endDate": "0001-01-01T00:00:00Z", 
 "lastPauseDate": "0001-01-01T00:00:00Z", 
 "runStatus": "idle", 
 "sla": 0, 
 "slaStatus": -1, 
 "startDate": "0001-01-01T00:00:00Z", 
 "totalDuration": 0 
 }, 
 "triagesla": { 
 "accumulatedPause": 0, 
 "breachTriggered": false, 
 "dueDate": "0001-01-01T00:00:00Z", 
 "endDate": "0001-01-01T00:00:00Z", 
 "lastPauseDate": "0001-01-01T00:00:00Z", 
 "runStatus": "idle", 
 "sla": 30, 
 "slaStatus": -1, 
 "startDate": "0001-01-01T00:00:00Z", 
 "totalDuration": 0 
 }, 
 "urlsslverification": [], 
 "xdralertsearchresults": [ 
 {}, 
 {}, 
 {} 
 ], 
 "xdrinvestigationresults": [ 
 {}, 
 {}, 
 {}, 
 { 
 "columnheader1": "" 
 }, 
 {}, 
 { 
 "columnheader1": "" 
 }, 
 {}, 
 {} 
 ], 
 "xdrstarred": false, 
 "xmcyberavgcomplexityscore": 0, 
 "xmcybersecurityscoretrend": 0, 
 "xpanseserviceclassifications": [ 
 {}, 
 {}, 
 {} 
 ], 
 "xpanseservicevalidation": [ 
 { 
 "columnheader1": "" 
 }, 
 {}, 
 {} 
 ] 
 }, 
 "account": "", 
 "autime": 1708507732380000000, 
 "type": "default_rocket_type", 
 "rawType": "default_rocket_type", 
 "name": "abc", 
 "rawName": "abc", 
 "status": 1, 
 "custom_status": "", 
 "resolution_status": "", 
 "reason": "", 
 "created": "2024-02-21T09:28:52.38Z", 
 "occurred": "2024-02-21T09:28:52.380846958Z", 
 "closed": "0001-01-01T00:00:00Z", 
 "sla": 0, 
 "severity": 0, 
 "investigationId": "157447", 
 "labels": [ 
 { 
 "value": "user@company.com", 
 "type": "Instance" 
 }, 
 { 
 "value": "Manual", 
 "type": "Brand" 
 } 
 ], 
 "attachment": null, 
 "details": "", 
 "openDuration": 11057, 
 "lastOpen": "2024-02-21T12:58:28.639333128Z", 
 "closingUserId": "", 
 "owner": "user@company.com", 
 "activated": "0001-01-01T00:00:00Z", 
 "closeReason": "", 
 "rawCloseReason": "", 
 "closeNotes": "close_note_oAZROKPJ", 
 "playbookId": "", 
 "dueDate": "0001-01-01T00:00:00Z", 
 "reminder": "0001-01-01T00:00:00Z", 
 "runStatus": "", 
 "notifyTime": "0001-01-01T00:00:00Z", 
 "phase": "", 
 "rawPhase": "", 
 "isPlayground": false, 
 "rawJSON": "", 
 "parent": "", 
 "parentXDRIncident": "", 
 "retained": false, 
 "category": "", 
 "rawCategory": "", 
 "linkedIncidents": null, 
 "linkedCount": 0, 
 "droppedCount": 0, 
 "sourceInstance": "user@company.com", 
 "sourceBrand": "Manual", 
 "canvases": null, 
 "lastJobRunTime": "0001-01-01T00:00:00Z", 
 "feedBased": false, 
 "dbotMirrorId": "", 
 "dbotMirrorInstance": "", 
 "dbotMirrorDirection": "", 
 "dbotDirtyFields": null, 
 "dbotCurrentDirtyFields": null, 
 "dbotMirrorTags": null, 
 "dbotMirrorLastSync": "0001-01-01T00:00:00Z", 
 "isDebug": false, 
 "changeStatus": "", 
 "insights": 0 
 } 

 Investigate an incident 

 post https://api-yourfqdn /xsoar/public/v1/incident/investigate 

 Open an investigation of an incident. Its status will change to Active and the remediation process will start. 

 Body 

 application/json 

 id string Optional 

 version integer Optional 

 Responses 

 200 

 OK 

 application/json 

 error null Optional 

 id string Optional 

 invPlaybook null Optional 

 investigation object Optional 

 Show properties 

 version integer Optional 

 post /xsoar/public/v1/incident/investigate 

 HTTP 

 Ask Copy 

 POST /xsoar/public/v1/incident/investigate HTTP/1.1 
 Host: api-yourfqdn 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 27 

 { 
 "id": "157448", 
 "version": 1 
 } 

 200 

 OK 

 Ask Copy 

 { 
 "error": null, 
 "id": "123456", 
 "invPlaybook": null, 
 "investigation": { 
 "cacheVersn": 0, 
 "category": "", 
 "closed": "0001-01-01T00:00:00Z", 
 "created": "2024-02-21T09:41:41.293Z", 
 "creatingUserId": "XSOARPAPIUser_3992", 
 "dbotCreatedBy": "user@company.com", 
 "details": "", 
 "entryUsers": [ 
 "user@company.com" 
 ], 
 "highPriority": false, 
 "id": "157448", 
 "isDebug": false, 
 "lastOpen": "0001-01-01T00:00:00Z", 
 "mirrorAutoClose": null, 
 "mirrorTypes": null, 
 "modified": "0001-01-01T00:00:00Z", 
 "name": "b", 
 "rawCategory": "", 
 "reason": null, 
 "runStatus": "", 
 "sizeInBytes": 0, 
 "slackMirrorAutoClose": false, 
 "slackMirrorType": "", 
 "status": 0, 
 "systems": null, 
 "tags": null, 
 "type": 0, 
 "users": [ 
 "user@company.com", 
 "" 
 ], 
 "version": 2 
 }, 
 "version": 1 
 } 

 Get a specific incident 

 get https://api-yourfqdn /xsoar/public/v1/incident/load/ {id} 

 Get the incident details of the specified incident ID. 

 Path parameters 

 id string Required Example: 162669 

 Header parameters 

 authorization string Required 

 api_key 

 Example: DCdIeow0xm73EwnxjPza1tdHTfZQv2eH7bTKlTPkgBHLj8aSjFzjgTE9bQUK1DidlWLrnYRhaYQ4PCIyNrNJbMUC6DOWi8ANIn1JWpMTE2neGvoDIRsKUbj6pJ1z7Gmr 

 x-xdr-auth-id string Required 

 api_key_id 

 Example: 2841 

 Responses 

 200 

 OK 

 application/json 

 Note: CustomFields (an optional generic object type) is missing from the following definition. 

 account string Optional 

 Account holds the tenant name so that slicing and dicing on the master can leverage bleve 

 activated string · date-time Optional 

 When was this activated 

 activatingingUserId string Optional 

 The user that activated this investigation 

 allRead boolean Optional 

 allReadWrite boolean Optional 

 attachment object · Attachment[] Optional 

 Attachments 

 Show properties 

 autime integer · int64 Optional 

 AlmostUniqueTime is an attempt to have a unique sortable ID for an incident 

 Example: 1682865388000000000 

 cacheVersn integer · int64 Optional Example: 0 

 canvases string[] Optional 

 Canvases of the incident 

 category string Optional 

 Category 

 closeNotes string Optional 

 Notes for closing the incident 

 closeReason string Optional 

 The reason for closing the incident (select from existing predefined values) 

 closed string · date-time Optional 

 When was this closed 

 closingUserId string Optional 

 The user ID that closed this investigation 

 created string · date-time Optional 

 When was this created 

 dbotCreatedBy string Optional 

 Who has created this event - relevant only for manual incidents 

 dbotCurrentDirtyFields string[] Optional 

 For mirroring, manage a list of current dirty fields so that we can send delta to outgoing integration 

 dbotDirtyFields string[] Optional 

 For mirroring, manage a list of dirty fields to not override them from the source of the incident 

 dbotMirrorDirection string Optional 

 DBotMirrorDirection of how to mirror the incident (in/out/both) 

 dbotMirrorId string Optional 

 DBotMirrorID of a remote system we are syncing with 

 dbotMirrorInstance string Optional 

 DBotMirrorInstance name of a mirror integration instance 

 dbotMirrorLastSync string · date-time Optional 

 The last time we synced this incident even if we did not update anything 

 dbotMirrorTags string[] Optional 

 The entry tags I want to sync to remote system 

 details string Optional 

 The details of the incident - reason, etc. 

 droppedCount integer · int64 Optional 

 DroppedCount ... 

 Example: 0 

 dueDate string · date-time Optional 

 SLA 

 feedBased boolean Optional 

 If this incident was triggered by a feed job 

 hasRole boolean Optional 

 Internal field to make queries on role faster 

 highlight object Optional 

 Show properties 

 id string Optional 

 investigationId string Optional 

 Investigation that was opened as a result of the incoming event 

 isDebug boolean Optional 

 IsDebug ... 

 isPlayground boolean Optional 

 IsPlayGround 

 labels object · Label[] Optional 

 Labels related to incident - each label is composed of a type and value 

 Show properties 

 lastJobRunTime string · date-time Optional 

 If this incident was triggered by a job, this would be the time the previous job started 

 lastOpen string · date-time Optional 

 linkedCount integer · int64 Optional 

 LinkedCount ... 

 Example: 0 

 linkedIncidents string[] Optional 

 LinkedIncidents incidents that were marked as linked by user 

 modified string · date-time Optional 

 name string Optional 

 Incident Name - given by user 

 notifyTime string · date-time Optional 

 Incdicates when last this field was changed with a value that supposed to send a notification 

 numericId integer · int64 Optional 

 occurred string · date-time Optional 

 When this incident has really occurred 

 openDuration integer · int64 Optional 

 Duration incident was open 

 Example: 0 

 owner string Optional 

 The user who owns this incident 

 parent string Optional 

 Parent 

 phase string Optional 

 Phase 

 playbookId string Optional 

 The associated playbook for this incident 

 previousAllRead boolean Optional 

 previousAllReadWrite boolean Optional 

 previousRoles string[] Optional 

 Do not change this field manually 

 primaryTerm integer · int64 Optional 

 rawCategory string Optional 

 rawCloseReason string Optional 

 The reason for closing the incident (select from existing predefined values) 

 rawJSON string Optional 

 rawName string Optional 

 Incident RawName 

 rawPhase string Optional 

 RawPhase 

 rawType string Optional 

 Incident raw type 

 reason string Optional 

 The reason for the resolve 

 reminder string · date-time Optional 

 When if at all to send a reminder 

 roles string[] Optional 

 The role assigned to this investigation 

 runStatus string Optional 

 Run status of a job. 

 sequenceNumber integer · int64 Optional 

 severity number · double · max: 4 Optional 

 Severity is the incident severity 

 Example: 2 

 sla number · double Optional 

 SLAState is the incident SLA at closure time, in minutes. 

 sortValues string[] Optional 

 sourceBrand string Optional 

 SourceBrand ... 

 sourceInstance string Optional 

 SourceInstance ... 

 status number · double · max: 2 Optional 

 IncidentStatus is the status of the incident 

 Example: 2 

 syncHash string Optional 

 todoTaskIds string[] Optional 

 ToDoTaskIDs list of to do task ids 

 type string Optional 

 Incident type 

 version integer · int64 Optional Example: 0 

 xsoarHasReadOnlyRole boolean Optional 

 xsoarPreviousReadOnlyRoles string[] Optional 

 xsoarReadOnlyRoles string[] Optional 

 get /xsoar/public/v1/incident/load/ {id} 

 HTTP 

 Ask Copy 

 GET /xsoar/public/v1/incident/load/{id} HTTP/1.1 
 Host: api-yourfqdn 
 authorization: DCdIeow0xm73EwnxjPza1tdHTfZQv2eH7bTKlTPkgBHLj8aSjFzjgTE9bQUK1DidlWLrnYRhaYQ4PCIyNrNJbMUC6DOWi8ANIn1JWpMTE2neGvoDIRsKUbj6pJ1z7Gmr 
 x-xdr-auth-id: 2841 
 Accept: */* 

 200 

 OK 

 Ask Copy 

 { 
 "id": "178768", 
 "version": 0, 
 "cacheVersn": 0, 
 "modified": "1970-01-01T00:00:00Z", 
 "sizeInBytes": 0, 
 "CustomFields": { 
 "bmcassignee": [ 
 {} 
 ], 
 "bmccustomer": [ 
 {} 
 ], 
 "bmcrequester": [ 
 {} 
 ], 
 "containmentsla": { 
 "accumulatedPause": 0, 
 "breachTriggered": false, 
 "dueDate": "0001-01-01T00:00:00Z", 
 "endDate": "0001-01-01T00:00:00Z", 
 "lastPauseDate": "0001-01-01T00:00:00Z", 
 "runStatus": "idle", 
 "sla": 30, 
 "slaStatus": -1, 
 "startDate": "0001-01-01T00:00:00Z", 
 "totalDuration": 0 
 }, 
 "crowdstrikefalconbehaviourpatterndispositiondetails": [ 
 {}, 
 {}, 
 {} 
 ], 
 "datadogcloudsiem": [ 
 {}, 
 {}, 
 {} 
 ], 
 "dataminrpulserelatedterms": [ 
 {}, 
 {}, 
 {} 
 ], 
 "decyfirdatadetails": [ 
 {}, 
 {}, 
 {} 
 ], 
 "detectionsla": { 
 "accumulatedPause": 0, 
 "breachTriggered": false, 
 "dueDate": "0001-01-01T00:00:00Z", 
 "endDate": "0001-01-01T00:00:00Z", 
 "lastPauseDate": "0001-01-01T00:00:00Z", 
 "runStatus": "idle", 
 "sla": 20, 
 "slaStatus": -1, 
 "startDate": "0001-01-01T00:00:00Z", 
 "totalDuration": 0 
 }, 
 "domaintoolsirisdetect": [ 
 {}, 
 {}, 
 {} 
 ], 
 "endpoint": [ 
 {} 
 ], 
 "externalid": "178768", 
 "extrahoprevealxdetectiondevices": [ 
 {}, 
 {}, 
 {} 
 ], 
 "extrahoprevealxmitretechniques": [ 
 {}, 
 {}, 
 {} 
 ], 
 "filerelationships": [ 
 {}, 
 {}, 
 {} 
 ], 
 "fortisiemattacktactics": [ 
 {}, 
 {} 
 ], 
 "fortisiemevents": [ 
 {} 
 ], 
 "incidentduration": { 
 "accumulatedPause": 0, 
 "breachTriggered": false, 
 "dueDate": "0001-01-01T00:00:00Z", 
 "endDate": "0001-01-01T00:00:00Z", 
 "lastPauseDate": "0001-01-01T00:00:00Z", 
 "runStatus": "idle", 
 "sla": 0, 
 "slaStatus": -1, 
 "startDate": "0001-01-01T00:00:00Z", 
 "totalDuration": 0 
 }, 
 "incidentrdpachehuntingstringssimilarity": [ 
 {}, 
 {}, 
 {} 
 ], 
 "incidentrdpcachehuntingstringsifter": [ 
 {}, 
 {}, 
 {} 
 ], 
 "inventasource": [ 
 {} 
 ], 
 "microsoftsentinelowner": [], 
 "qintelqwatchexposures": [ 
 {}, 
 {}, 
 {} 
 ], 
 "remediationsla": { 
 "accumulatedPause": 0, 
 "breachTriggered": false, 
 "dueDate": "0001-01-01T00:00:00Z", 
 "endDate": "0001-01-01T00:00:00Z", 
 "lastPauseDate": "0001-01-01T00:00:00Z", 
 "runStatus": "idle", 
 "sla": 7200, 
 "slaStatus": -1, 
 "startDate": "0001-01-01T00:00:00Z", 
 "totalDuration": 0 
 }, 
 "rsametasevents": [], 
 "rsarawlogslist": [], 
 "securitypolicymatch": [ 
 {} 
 ], 
 "similarincidentsdbot": [ 
 {} 
 ], 
 "spycloudcompassdevicedata": [ 
 {}, 
 {}, 
 {} 
 ], 
 "suspiciousexecutions": [ 
 {}, 
 {}, 
 {} 
 ], 
 "timetoassignment": { 
 "accumulatedPause": 0, 
 "breachTriggered": false, 
 "dueDate": "0001-01-01T00:00:00Z", 
 "endDate": "0001-01-01T00:00:00Z", 
 "lastPauseDate": "0001-01-01T00:00:00Z", 
 "runStatus": "idle", 
 "sla": 0, 
 "slaStatus": -1, 
 "startDate": "0001-01-01T00:00:00Z", 
 "totalDuration": 0 
 }, 
 "triagesla": { 
 "accumulatedPause": 0, 
 "breachTriggered": false, 
 "dueDate": "0001-01-01T00:00:00Z", 
 "endDate": "0001-01-01T00:00:00Z", 
 "lastPauseDate": "0001-01-01T00:00:00Z", 
 "runStatus": "idle", 
 "sla": 30, 
 "slaStatus": -1, 
 "startDate": "0001-01-01T00:00:00Z", 
 "totalDuration": 0 
 }, 
 "urlsslverification": [], 
 "xdralertsearchresults": [ 
 {}, 
 {}, 
 {} 
 ], 
 "xdrinvestigationresults": [ 
 {}, 
 {}, 
 {}, 
 { 
 "columnheader1": "" 
 }, 
 {}, 
 { 
 "columnheader1": "" 
 }, 
 {}, 
 {} 
 ], 
 "xpanseserviceclassifications": [ 
 {}, 
 {}, 
 {} 
 ], 
 "xpanseservicevalidation": [ 
 { 
 "columnheader1": "" 
 }, 
 {}, 
 {} 
 ] 
 }, 
 "account": "", 
 "autime": 1712843499584000000, 
 "type": "default_type", 
 "rawType": "default_type", 
 "name": "delete_integration_instance_ESEDFV0U", 
 "rawName": "delete_integration_instance_ESEDFV0U", 
 "status": 0, 
 "custom_status": "", 
 "resolution_status": "", 
 "reason": "", 
 "created": "2024-04-11T13:51:39.584Z", 
 "occurred": "2024-04-11T13:51:38.183347Z", 
 "closed": "0001-01-01T00:00:00Z", 
 "sla": 0, 
 "severity": 0, 
 "investigationId": "", 
 "labels": [ 
 { 
 "value": "Rocket Incident Generator", 
 "type": "Brand" 
 }, 
 { 
 "value": "delete_integration_instance_ESEDFV0U", 
 "type": "Instance" 
 }, 
 { 
 "value": "bar", 
 "type": "foo" 
 }, 
 { 
 "value": "{\"evidenceBoard\":\"https://fqdn.us.paloaltonetworks.com/EvidenceBoard/temp_a55ff05c-6e11-4544-86cf-f513687fc9fa\",\"investigation\":\"https://fqdn.us.paloaltonetworks.com/Details/temp_a55ff05c-6e11-4544-86cf-f513687fc9fa\",\"relatedIncidents\":\"https://fqdn.us.paloaltonetworks.com/Cluster/temp_a55ff05c-6e11-4544-86cf-f513687fc9fa\",\"server\":\"https://fqdn.us.paloaltonetworks.com\",\"warRoom\":\"https://fqdn.us.paloaltonetworks.com/WarRoom/temp_a55ff05c-6e11-4544-86cf-f513687fc9fa\",\"workPlan\":\"https://fqdn.us.paloaltonetworks.com/WorkPlan/temp_a55ff05c-6e11-4544-86cf-f513687fc9fa\"}", 
 "type": "demisto_url" 
 } 
 ], 
 "attachment": null, 
 "details": "{\"foo\": \"bar\", \"demisto_url\": {\"evidenceBoard\": \"https://fqdn.us.paloaltonetworks.com/EvidenceBoard/temp_a55ff05c-6e11-4544-86cf-f513687fc9fa\", \"investigation\": \"https://fqdn.us.paloaltonetworks.com/Details/temp_a55ff05c-6e11-4544-86cf-f513687fc9fa\", \"relatedIncidents\": \"https://fqdn.us.paloaltonetworks.com/Cluster/temp_a55ff05c-6e11-4544-86cf-f513687fc9fa\", \"server\": \"https://fqdn.us.paloaltonetworks.com\", \"warRoom\": \"https://fqdn.us.paloaltonetworks.com/WarRoom/temp_a55ff05c-6e11-4544-86cf-f513687fc9fa\", \"workPlan\": \"https://fqdn.us.paloaltonetworks.com/WorkPlan/temp_a55ff05c-6e11-4544-86cf-f513687fc9fa\"}}", 
 "openDuration": 0, 
 "lastOpen": "0001-01-01T00:00:00Z", 
 "closingUserId": "", 
 "owner": "", 
 "activated": "0001-01-01T00:00:00Z", 
 "closeReason": "", 
 "rawCloseReason": "", 
 "closeNotes": "", 
 "playbookId": "", 
 "dueDate": "0001-01-01T00:00:00Z", 
 "reminder": "0001-01-01T00:00:00Z", 
 "runStatus": "", 
 "notifyTime": "0001-01-01T00:00:00Z", 
 "phase": "", 
 "rawPhase": "", 
 "isPlayground": false, 
 "rawJSON": "", 
 "parent": "", 
 "parentXDRIncident": "", 
 "retained": false, 
 "category": "", 
 "rawCategory": "", 
 "linkedIncidents": null, 
 "linkedCount": 0, 
 "droppedCount": 0, 
 "sourceInstance": "delete_integration_instance_ESEDFV0U", 
 "sourceBrand": "Rocket Incident Generator", 
 "canvases": null, 
 "lastJobRunTime": "0001-01-01T00:00:00Z", 
 "feedBased": false, 
 "dbotMirrorId": "", 
 "dbotMirrorInstance": "", 
 "dbotMirrorDirection": "", 
 "dbotDirtyFields": null, 
 "dbotCurrentDirtyFields": null, 
 "dbotMirrorTags": null, 
 "dbotMirrorLastSync": "0001-01-01T00:00:00Z", 
 "isDebug": false 
 } 

 Batch export incidents to CSV 

 post https://api-yourfqdn /xsoar/public/v1/incident/batch/exportToCsv 

 Export a batch of incidents to a CSV file and receive the filename in response. You can then use Get incidents as a CSV file to download the CSV file. You can define the columns as well as filter the incidents to be included in the CSV file. 

 **Note: ** You can retrieve up to 10,000 incidents. 

 Header parameters 

 authorization string Required 

 api_key 

 Example: DCdIeow0xm73EwnxjPza1tdHTfZQv2eH7bTKlTPkgBHLj8aSjFzjgTE9bQUK1DidlWLrnYRhaYQ4PCIyNrNJbMUC6DOWi8ANIn1JWpMTE2neGvoDIRsKUbj6pJ1z7Gmr 

 x-xdr-auth-id string Required 

 api_key_id 

 Example: 2841 

 Body 

 application/json 

 CustomFields object Optional 

 Show properties 

 all boolean Optional 

 When all is true , all of the incidents are exported to CSV. 

 Note: When all : true , all settings relating to page size and number are ignored. 

 closeNotes string Optional 

 closeReason string Optional 

 columns string[] Optional 

 data object Optional 

 Show properties 

 filter object · IncidentFilter Optional 

 IncidentFilter allows for very simple filtering. 

 Show properties 

 force boolean Optional 

 ids string[] Optional 

 Specify the list of incident IDs to be included in the CSV file. 

 Note: When you choose to specify the IDs, all settings relating to page size and number are ignored. 

 line string Optional 

 originalIncidentId string Optional 

 overrideInvestigation boolean Optional 

 Responses 

 200 

 OK 

 application/json 

 filename string Optional 

 The CSV filename. Use this filename as the path header in /xsoar/public/v1/incidents/csv/{filename} . 

 Example: incidents_report_Thu_18_Apr_2024_10_06_04_UTC.csv 

 413 

 Limit exceeded. Output file exceeded limit. Exported incidents reach limit [10,000]. 

 application/json 

 post /xsoar/public/v1/incident/batch/exportToCsv 

 HTTP 

 Ask Copy 

 POST /xsoar/public/v1/incident/batch/exportToCsv HTTP/1.1 
 Host: api-yourfqdn 
 authorization: DCdIeow0xm73EwnxjPza1tdHTfZQv2eH7bTKlTPkgBHLj8aSjFzjgTE9bQUK1DidlWLrnYRhaYQ4PCIyNrNJbMUC6DOWi8ANIn1JWpMTE2neGvoDIRsKUbj6pJ1z7Gmr 
 x-xdr-auth-id: 2841 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 95 

 { 
 "all": true, 
 "columns": [ 
 "id", 
 "name", 
 "severity" 
 ], 
 "filter": { 
 "period": { 
 "by": "days", 
 "fromValue": 2 
 } 
 } 
 } 

 200 

 OK 

 Ask Copy 

 { 
 "filename": " incidents_report_Thu_18_Apr_2024_10_06_04_UTC.csv" 
 } 

 Get incidents as a CSV file 

 get https://api-yourfqdn /xsoar/public/v1/incident/csv/ {filename} 

 Download the incident details in a CSV file format after preparing it by calling the Batch export incidents to CSV API endpoint. The response of that call contains the prepared incident report filename with a timestamp. Use that filename as the path parameter in this API endpoint to download the file. 

 Note: To use cURL to run this command, add the -O curl command for downloading a file to the current folder, or -o /my_custom_location/my_custom_name.csv to customize the destination of the downloaded file. For example: 

 Ask Copy 

 curl "https://api-yourfqdn/xsoar/public/v1/incident/csv/incidents_report_Thu_18_Apr_2024_10_06_04_UTC.csv" 
 -H 'content-type: application/json' 
 -H 'accept: application/json' 
 -H "Authorization:$api_key" 
 -H "x-xdr-auth-id:$api_key_id" 
 -O 

 Path parameters 

 filename string Required 

 Filename of the CSV file outputted by the "Batch export incidents to CSV" API call 

 Example: incidents_report_Thu_18_Apr_2024_10_06_04_UTC.csv 

 Header parameters 

 authorization string Required 

 api_key 

 Example: DCdIeow0xm73EwnxjPza1tdHTfZQv2eH7bTKlTPkgBHLj8aSjFzjgTE9bQUK1DidlWLrnYRhaYQ4PCIyNrNJbMUC6DOWi8ANIn1JWpMTE2neGvoDIRsKUbj6pJ1z7Gmr 

 x-xdr-auth-id string Required 

 api_key_id 

 Example: 2841 

 Responses 

 200 

 OK 

 application/json 

 file string · binary Optional 

 get /xsoar/public/v1/incident/csv/ {filename} 

 HTTP 

 Ask Copy 

 GET /xsoar/public/v1/incident/csv/{filename} HTTP/1.1 
 Host: api-yourfqdn 
 authorization: DCdIeow0xm73EwnxjPza1tdHTfZQv2eH7bTKlTPkgBHLj8aSjFzjgTE9bQUK1DidlWLrnYRhaYQ4PCIyNrNJbMUC6DOWi8ANIn1JWpMTE2neGvoDIRsKUbj6pJ1z7Gmr 
 x-xdr-auth-id: 2841 
 Accept: */* 

 200 

 OK 

 Ask Copy 

 { 
 "file": "binary" 
 } 

 Update incidents in a batch 

 post https://api-yourfqdn /xsoar/public/v1/incident/batch 

 Update a batch of incidents. 

 To update custom fields, add CustomFields under the data parameter (the top-level CutomFields parameter is not used in this API). To update incident custom fields, make them lowercase and remove all spaces. For example: "Scan IP" -> "scanip". Alternatively, to get the actual key name, use the Cortex XSOAR CLI to run /incident_add and look for the key that you would like to update. 

 Header parameters 

 authorization string Required 

 api_key 

 Example: DCdIeow0xm73EwnxjPza1tdHTfZQv2eH7bTKlTPkgBHLj8aSjFzjgTE9bQUK1DidlWLrnYRhaYQ4PCIyNrNJbMUC6DOWi8ANIn1JWpMTE2neGvoDIRsKUbj6pJ1z7Gmr 

 x-xdr-auth-id string Required 

 api_key_id 

 Example: 2841 

 Body 

 application/json 

 CustomFields object Optional 

 Show properties 

 all boolean Optional 

 When all is true , all of the incidents are exported to CSV. 

 Note: When all : true , all settings relating to page size and number are ignored. 

 closeNotes string Optional 

 closeReason string Optional 

 columns string[] Optional 

 data object Optional 

 Show properties 

 filter object · IncidentFilter Optional 

 IncidentFilter allows for very simple filtering. 

 Show properties 

 force boolean Optional 

 ids string[] Optional 

 Specify the list of incident IDs to be included in the CSV file. 

 Note: When you choose to specify the IDs, all settings relating to page size and number are ignored. 

 line string Optional 

 originalIncidentId string Optional 

 overrideInvestigation boolean Optional 

 Responses 

 200 

 OK 

 application/json 

 IncidentSearchResponseWrapper is an extension for the IncidentSearchResponse type, which holds list of IncidentWrapper(s) 

 accountErrors string[] Optional 

 data object · IncidentWrapper[] Optional 

 in: body 

 Show properties 

 notUpdated integer · uint64 Optional 

 searchAfter string[] Optional 

 searchAfterElastic string[] Optional 

 searchBefore string[] Optional 

 searchBeforeElastic string[] Optional 

 total integer · int64 Optional 

 totalAccounts integer · int64 Optional 

 post /xsoar/public/v1/incident/batch 

 HTTP 

 Ask Copy 

 POST /xsoar/public/v1/incident/batch HTTP/1.1 
 Host: api-yourfqdn 
 authorization: DCdIeow0xm73EwnxjPza1tdHTfZQv2eH7bTKlTPkgBHLj8aSjFzjgTE9bQUK1DidlWLrnYRhaYQ4PCIyNrNJbMUC6DOWi8ANIn1JWpMTE2neGvoDIRsKUbj6pJ1z7Gmr 
 x-xdr-auth-id: 2841 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 188 

 { 
 "all": false, 
 "data": { 
 "severity": 3 
 }, 
 "filter": { 
 "page": 0, 
 "period": { 
 "by": "day", 
 "fromValue": 2 
 }, 
 "query": "-status:closed", 
 "size": 50, 
 "sort": [ 
 { 
 "asc": false, 
 "field": "id" 
 } 
 ] 
 }, 
 "ids": [ 
 "207460", 
 "207461" 
 ] 
 } 

 200 

 OK 

 Ask Copy 

 { 
 "total": 24, 
 "data": [ 
 { 
 "id": "207461", 
 "version": 1, 
 "cacheVersn": 0, 
 "modified": "2024-06-23T11:44:16.705Z", 
 "sizeInBytes": 0, 
 "sortValues": [ 
 "1" 
 ], 
 "dbotCreatedBy": "user@company.com", 
 "CustomFields": { 
 "bmcassignee": [ 
 {} 
 ], 
 "bmccustomer": [ 
 {} 
 ], 
 "bmcrequester": [ 
 {} 
 ], 
 "containmentsla": { 
 "accumulatedPause": 0, 
 "breachTriggered": false, 
 "dueDate": "0001-01-01T00:00:00Z", 
 "endDate": "0001-01-01T00:00:00Z", 
 "lastPauseDate": "0001-01-01T00:00:00Z", 
 "runStatus": "idle", 
 "sla": 30, 
 "slaStatus": -1, 
 "startDate": "0001-01-01T00:00:00Z", 
 "totalDuration": 0 
 }, 
 "crowdstrikefalconbehaviourpatterndispositiondetails": [ 
 {}, 
 {}, 
 {} 
 ], 
 "datadogcloudsiem": [ 
 {}, 
 {}, 
 {} 
 ], 
 "dataminrpulserelatedterms": [ 
 {}, 
 {}, 
 {} 
 ], 
 "decyfirdatadetails": [ 
 {}, 
 {}, 
 {} 
 ], 
 "detectionsla": { 
 "accumulatedPause": 0, 
 "breachTriggered": false, 
 "dueDate": "0001-01-01T00:00:00Z", 
 "endDate": "0001-01-01T00:00:00Z", 
 "lastPauseDate": "0001-01-01T00:00:00Z", 
 "runStatus": "idle", 
 "sla": 20, 
 "slaStatus": -1, 
 "startDate": "0001-01-01T00:00:00Z", 
 "totalDuration": 0 
 }, 
 "xpanseserviceclassifications": [ 
 {}, 
 {}, 
 {} 
 ], 
 "xpanseservicevalidation": [ 
 { 
 "columnheader1": "" 
 }, 
 {}, 
 {} 
 ] 
 }, 
 "account": "", 
 "autime": 1719143055300000000, 
 "type": "default_type", 
 "rawType": "default_type", 
 "name": "KxdcIbCA", 
 "rawName": "KxdcIbCA", 
 "status": 1, 
 "custom_status": "", 
 "resolution_status": "", 
 "reason": "", 
 "created": "2024-06-23T11:44:15.3Z", 
 "occurred": "2024-06-23T11:44:15.673434077Z", 
 "closed": "0001-01-01T00:00:00Z", 
 "sla": 0, 
 "severity": 1, 
 "investigationId": "207461", 
 "labels": [ 
 { 
 "value": "user@company.com", 
 "type": "Instance" 
 }, 
 { 
 "value": "Manual", 
 "type": "Brand" 
 } 
 ], 
 "attachment": "None", 
 "details": "", 
 "openDuration": 0, 
 "lastOpen": "0001-01-01T00:00:00Z", 
 "closingUserId": "", 
 "owner": "", 
 "activated": "0001-01-01T00:00:00Z", 
 "closeReason": "", 
 "rawCloseReason": "", 
 "closeNotes": "", 
 "playbookId": "", 
 "dueDate": "0001-01-01T00:00:00Z", 
 "reminder": "0001-01-01T00:00:00Z", 
 "runStatus": "", 
 "notifyTime": "0001-01-01T00:00:00Z", 
 "phase": "", 
 "rawPhase": "", 
 "isPlayground": false, 
 "rawJSON": "", 
 "parent": "", 
 "parentXDRIncident": "", 
 "retained": false, 
 "category": "", 
 "rawCategory": "", 
 "linkedIncidents": [], 
 "linkedCount": 0, 
 "droppedCount": 0, 
 "sourceInstance": "user@company.com", 
 "sourceBrand": "Manual", 
 "canvases": "None", 
 "lastJobRunTime": "0001-01-01T00:00:00Z", 
 "feedBased": false, 
 "dbotMirrorId": "", 
 "dbotMirrorInstance": "", 
 "dbotMirrorDirection": "", 
 "dbotDirtyFields": "None", 
 "dbotCurrentDirtyFields": "None", 
 "dbotMirrorTags": "None", 
 "dbotMirrorLastSync": "0001-01-01T00:00:00Z", 
 "isDebug": false, 
 "changeStatus": "", 
 "insights": 0 
 } 
 ], 
 "notUpdated": 0, 
 "searchAfter": "None", 
 "searchBefore": "None", 
 "searchAfterElastic": "None", 
 "searchBeforeElastic": "None", 
 "accountErrors": "None", 
 "totalAccounts": 0 
 } 

 Export an incident's history and workplan 

 get https://api-yourfqdn /xsoar/public/v1/performance/incident/export/ {incident_id} 

 Export the specified incident's history and workplan in a tar.gz file. Note that only playbook task entries are returned. 

 Path parameters 

 incident_id string Required 

 Incident ID 

 Header parameters 

 authorization string Required 

 api_key 

 Example: DCdIeow0xm73EwnxjPza1tdHTfZQv2eH7bTKlTPkgBHLj8aSjFzjgTE9bQUK1DidlWLrnYRhaYQ4PCIyNrNJbMUC6DOWi8ANIn1JWpMTE2neGvoDIRsKUbj6pJ1z7Gmr 

 x-xdr-auth-id string Required 

 api_key_id 

 Example: 2841 

 Responses 

 200 

 OK 

 application/json 

 filename string · binary Optional 

 A tar.gz file containing the JSON files with the incident's history. 

 get /xsoar/public/v1/performance/incident/export/ {incident_id} 

 HTTP 

 Ask Copy 

 GET /xsoar/public/v1/performance/incident/export/{incident_id} HTTP/1.1 
 Host: api-yourfqdn 
 authorization: DCdIeow0xm73EwnxjPza1tdHTfZQv2eH7bTKlTPkgBHLj8aSjFzjgTE9bQUK1DidlWLrnYRhaYQ4PCIyNrNJbMUC6DOWi8ANIn1JWpMTE2neGvoDIRsKUbj6pJ1z7Gmr 
 x-xdr-auth-id: 2841 
 Accept: */* 

 200 

 OK 

 Ask Copy 

 { 
 "filename": "binary" 
 } 

 Delete a batch of incidents 

 post https://api-yourfqdn /xsoar/public/v1/incident/batchDelete 

 Delete a batch of incidents. 

 Header parameters 

 Authorization string Required 

 {api_key} 

 x-xdr-auth-id string Required 

 {api_key_id} 

 Body 

 application/json 

 CustomFields object Optional 

 Show properties 

 all boolean Optional 

 When all is true , all of the incidents are exported to CSV. 

 Note: When all : true , all settings relating to page size and number are ignored. 

 closeNotes string Optional 

 closeReason string Optional 

 columns string[] Optional 

 data object Optional 

 Show properties 

 filter object · IncidentFilter Optional 

 IncidentFilter allows for very simple filtering. 

 Show properties 

 force boolean Optional 

 ids string[] Optional 

 Specify the list of incident IDs to be included in the CSV file. 

 Note: When you choose to specify the IDs, all settings relating to page size and number are ignored. 

 line string Optional 

 originalIncidentId string Optional 

 overrideInvestigation boolean Optional 

 Responses 

 200 

 OK 

 application/json 

 IncidentSearchResponseWrapper is an extension for the IncidentSearchResponse type, which holds list of IncidentWrapper(s) 

 accountErrors string[] Optional 

 data object · IncidentWrapper[] Optional 

 in: body 

 Show properties 

 notUpdated integer · uint64 Optional 

 searchAfter string[] Optional 

 searchAfterElastic string[] Optional 

 searchBefore string[] Optional 

 searchBeforeElastic string[] Optional 

 total integer · int64 Optional 

 totalAccounts integer · int64 Optional 

 post /xsoar/public/v1/incident/batchDelete 

 HTTP 

 Ask Copy 

 POST /xsoar/public/v1/incident/batchDelete HTTP/1.1 
 Host: api-yourfqdn 
 Authorization: text 
 x-xdr-auth-id: text 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 150 

 { 
 "all": false, 
 "filter": { 
 "page": 0, 
 "period": { 
 "by": "day", 
 "fromValue": 2 
 }, 
 "query": "", 
 "size": 50, 
 "sort": [ 
 { 
 "asc": false, 
 "field": "id" 
 } 
 ] 
 }, 
 "ids": [ 
 "12128", 
 "12129" 
 ] 
 } 

 200 

 OK 

 Ask Copy 

 { 
 "accountErrors": [ 
 "text" 
 ], 
 "data": [ 
 { 
 "ShardID": 1, 
 "account": "text", 
 "activated": "2026-01-01T00:00:00.000Z", 
 "activatingingUserId": "text", 
 "allRead": true, 
 "allReadWrite": true, 
 "attachment": [ 
 { 
 "description": "text", 
 "isTempPath": true, 
 "name": "text", 
 "path": "text", 
 "showMediaFile": true, 
 "type": "text" 
 } 
 ], 
 "autime": 1, 
 "cacheVersn": 1, 
 "canvases": [ 
 "text" 
 ], 
 "category": "text", 
 "changeStatus": "text", 
 "closeNotes": "text", 
 "closeReason": "text", 
 "closed": "2026-01-01T00:00:00.000Z", 
 "closingUserId": "text", 
 "created": "2026-01-01T00:00:00.000Z", 
 "dbotCreatedBy": "text", 
 "dbotCurrentDirtyFields": [ 
 "text" 
 ], 
 "dbotDirtyFields": [ 
 "text" 
 ], 
 "dbotMirrorDirection": "text", 
 "dbotMirrorId": "text", 
 "dbotMirrorInstance": "text", 
 "dbotMirrorLastSync": "2026-01-01T00:00:00.000Z", 
 "dbotMirrorTags": [ 
 "text" 
 ], 
 "details": "text", 
 "droppedCount": 1, 
 "dueDate": "2026-01-01T00:00:00.000Z", 
 "feedBased": true, 
 "hasRole": true, 
 "highlight": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "id": "text", 
 "indexName": "text", 
 "insights": 1, 
 "investigationId": "text", 
 "isDebug": true, 
 "isPlayground": true, 
 "labels": [ 
 { 
 "type": "text", 
 "value": "text" 
 } 
 ], 
 "lastJobRunTime": "2026-01-01T00:00:00.000Z", 
 "lastOpen": "2026-01-01T00:00:00.000Z", 
 "linkedCount": 1, 
 "linkedIncidents": [ 
 "text" 
 ], 
 "modified": "2026-01-01T00:00:00.000Z", 
 "name": "text", 
 "notifyTime": "2026-01-01T00:00:00.000Z", 
 "numericId": 1, 
 "occurred": "2026-01-01T00:00:00.000Z", 
 "openDuration": 1, 
 "owner": "text", 
 "parent": "text", 
 "phase": "text", 
 "playbookId": "text", 
 "previousAllRead": true, 
 "previousAllReadWrite": true, 
 "previousRoles": [ 
 "text" 
 ], 
 "primaryTerm": 1, 
 "rawCategory": "text", 
 "rawCloseReason": "text", 
 "rawJSON": "text", 
 "rawName": "text", 
 "rawPhase": "text", 
 "rawType": "text", 
 "reason": "text", 
 "reminder": "2026-01-01T00:00:00.000Z", 
 "roles": [ 
 "text" 
 ], 
 "runStatus": "text", 
 "sequenceNumber": 1, 
 "severity": 2, 
 "sizeInBytes": 1, 
 "sla": 1, 
 "sortValues": [ 
 "text" 
 ], 
 "sourceBrand": "text", 
 "sourceInstance": "text", 
 "status": 2, 
 "syncHash": "text", 
 "todoTaskIds": [ 
 "text" 
 ], 
 "type": "text", 
 "version": 1, 
 "xsoarHasReadOnlyRole": true, 
 "xsoarPreviousReadOnlyRoles": [ 
 "text" 
 ], 
 "xsoarReadOnlyRoles": [ 
 "text" 
 ] 
 } 
 ], 
 "notUpdated": 1, 
 "searchAfter": [ 
 "text" 
 ], 
 "searchAfterElastic": [ 
 "text" 
 ], 
 "searchBefore": [ 
 "text" 
 ], 
 "searchBeforeElastic": [ 
 "text" 
 ], 
 "total": 1, 
 "totalAccounts": 1 
 } 

 Upload a file to an incident 

 post https://api-yourfqdn /xsoar/public/v1/incident/upload/ {incident_id} 

 Add a file attachment to an incident. 

 Path parameters 

 incident_id string Required 

 Header parameters 

 Authorization string Required 

 {api_key} 

 x-xdr-auth-id string Required 

 {api_key_id} 

 Body 

 multipart/form-data 

 fileName string Optional 

 File name 

 fileComment string Optional 

 Comment to add to the file 

 field string Optional 

 Field name to hold the attachment details. If not specified, attachment is used. 

 showMediaFile boolean Optional 

 Whether to show media files. 

 last boolean Optional 

 If set to true , creates an investigation. This is used for uploading after creating an incident. 

 file string · binary Required 

 File 

 Responses 

 200 

 OK 

 application/json 

 IncidentWrapper is an extension of the Incident entity, which includes an additional field of changed-status for the web client 

 ShardID integer · int64 Optional 

 account string Optional 

 Account holds the tenant name so that slicing and dicing on the master can leverage bleve 

 activated string · date-time Optional 

 When was this activated 

 activatingingUserId string Optional 

 The user that activated this investigation 

 allRead boolean Optional 

 allReadWrite boolean Optional 

 attachment object · Attachment[] Optional 

 Attachments 

 Show properties 

 autime integer · int64 Optional 

 AlmostUniqueTime is an attempt to have a unique sortable ID for an incident 

 cacheVersn integer · int64 Optional 

 canvases string[] Optional 

 Canvases of the incident 

 category string Optional 

 Category 

 changeStatus string Optional 

 closeNotes string Optional 

 Notes for closing the incident 

 closeReason string Optional 

 The reason for closing the incident (select from existing predefined values) 

 closed string · date-time Optional 

 When was this closed 

 closingUserId string Optional 

 The user ID that closed this investigation 

 created string · date-time Optional 

 dbotCreatedBy string Optional 

 Who has created this event - relevant only for manual incidents 

 dbotCurrentDirtyFields string[] Optional 

 For mirroring, manage a list of current dirty fields so that we can send delta to outgoing integration 

 dbotDirtyFields string[] Optional 

 For mirroring, manage a list of dirty fields to not override them from the source of the incident 

 dbotMirrorDirection string Optional 

 DBotMirrorDirection of how to mirror the incident (in/out/both) 

 dbotMirrorId string Optional 

 DBotMirrorID of a remote system we are syncing with 

 dbotMirrorInstance string Optional 

 DBotMirrorInstance name of a mirror integration instance 

 dbotMirrorLastSync string · date-time Optional 

 The last time we synced this incident even if we did not update anything 

 dbotMirrorTags string[] Optional 

 The entry tags I want to sync to remote system 

 details string Optional 

 The details of the incident - reason, etc. 

 droppedCount integer · int64 Optional 

 DroppedCount ... 

 dueDate string · date-time Optional 

 SLA 

 feedBased boolean Optional 

 If this incident was triggered by a feed job 

 hasRole boolean Optional 

 Internal field to make queries on role faster 

 highlight object Optional 

 Show properties 

 id string Optional 

 indexName string Optional 

 insights integer · uint64 Optional 

 investigationId string Optional 

 Investigation that was opened as a result of the incoming event 

 isDebug boolean Optional 

 IsDebug ... 

 isPlayground boolean Optional 

 IsPlayGround 

 labels object · Label[] Optional 

 Labels related to incident - each label is composed of a type and value 

 Show properties 

 lastJobRunTime string · date-time Optional 

 If this incident was triggered by a job, this would be the time the previous job started 

 lastOpen string · date-time Optional 

 linkedCount integer · int64 Optional 

 LinkedCount ... 

 linkedIncidents string[] Optional 

 LinkedIncidents incidents that were marked as linked by user 

 modified string · date-time Optional 

 name string Optional 

 Incident Name - given by user 

 notifyTime string · date-time Optional 

 Incdicates when last this field was changed with a value that supposed to send a notification 

 numericId integer · int64 Optional 

 occurred string · date-time Optional 

 When this incident has really occurred 

 openDuration integer · int64 Optional 

 Duration incident was open 

 owner string Optional 

 The user who owns this incident 

 parent string Optional 

 Parent 

 phase string Optional 

 Phase 

 playbookId string Optional 

 The associated playbook for this incident 

 previousAllRead boolean Optional 

 previousAllReadWrite boolean Optional 

 previousRoles string[] Optional 

 Do not change this field manually 

 primaryTerm integer · int64 Optional 

 rawCategory string Optional 

 rawCloseReason string Optional 

 The reason for closing the incident (select from existing predefined values) 

 rawJSON string Optional 

 rawName string Optional 

 Incident RawName 

 rawPhase string Optional 

 RawPhase 

 rawType string Optional 

 Incident raw type 

 reason string Optional 

 The reason for the resolve 

 reminder string · date-time Optional 

 When if at all to send a reminder 

 roles string[] Optional 

 The role assigned to this investigation 

 runStatus string Optional 

 Run status of a job. 

 sequenceNumber integer · int64 Optional 

 severity number · double · max: 4 Optional 

 Severity is the incident severity 

 Example: 2 

 sizeInBytes integer · int64 Optional 

 sla number · double Optional 

 SLAState is the incident SLA at closure time, in minutes. 

 sortValues string[] Optional 

 sourceBrand string Optional 

 SourceBrand ... 

 sourceInstance string Optional 

 SourceInstance ... 

 status number · double · max: 2 Optional 

 IncidentStatus is the status of the incident 

 Example: 2 

 syncHash string Optional 

 todoTaskIds string[] Optional 

 ToDoTaskIDs list of to do task ids 

 type string Optional 

 Incident type 

 version integer · int64 Optional 

 xsoarHasReadOnlyRole boolean Optional 

 xsoarPreviousReadOnlyRoles string[] Optional 

 xsoarReadOnlyRoles string[] Optional 

 post /xsoar/public/v1/incident/upload/ {incident_id} 

 HTTP 

 Ask Copy 

 POST /xsoar/public/v1/incident/upload/{incident_id} HTTP/1.1 
 Host: api-yourfqdn 
 Authorization: text 
 x-xdr-auth-id: text 
 Content-Type: multipart/form-data 
 Accept: */* 
 Content-Length: 148 

 { 
 "fileName": "documentation.log", 
 "fileComment": "Some important comment", 
 "field": "string", 
 "showMediaFile": true, 
 "last": true, 
 "file": "documentation.log" 
 } 

 200 

 OK 

 Ask Copy 

 { 
 "id": "294018", 
 "version": -1, 
 "cacheVersn": 0, 
 "modified": "2025-04-27T09:43:07.284Z", 
 "sizeInBytes": 0, 
 "dbotCreatedBy": "user@company.com", 
 "CustomFields": { 
 "actionsoncampaignincidents": "Close", 
 "actionsonlowsimilarityincidents": "Add To Campaign", 
 "bmcassignee": [ 
 {} 
 ], 
 "bmccustomer": [ 
 {} 
 ], 
 "bmcrequester": [ 
 {} 
 ], 
 "chronicleautoblockentities": "Yes", 
 "chronicleskipentityisolation": "Yes", 
 "containmentsla": { 
 "accumulatedPause": 0, 
 "breachTriggered": false, 
 "dueDate": "0001-01-01T00:00:00Z", 
 "endDate": "0001-01-01T00:00:00Z", 
 "lastPauseDate": "0001-01-01T00:00:00Z", 
 "runStatus": "idle", 
 "sla": 30, 
 "slaStatus": -1, 
 "startDate": "0001-01-01T00:00:00Z", 
 "totalDuration": 0 
 }, 
 "crowdstrikefalconbehaviourpatterndispositiondetails": [ 
 {}, 
 {}, 
 {} 
 ], 
 "datadogcloudsiem": [ 
 {}, 
 {}, 
 {} 
 ], 
 "dataminrpulserelatedterms": [ 
 {}, 
 {}, 
 {} 
 ], 
 "dbotmirrordirection": "", 
 "decyfirdatadetails": [ 
 {}, 
 {}, 
 {} 
 ], 
 "detectionsla": { 
 "accumulatedPause": 0, 
 "breachTriggered": false, 
 "dueDate": "0001-01-01T00:00:00Z", 
 "endDate": "0001-01-01T00:00:00Z", 
 "lastPauseDate": "0001-01-01T00:00:00Z", 
 "runStatus": "idle", 
 "sla": 20, 
 "slaStatus": -1, 
 "startDate": "0001-01-01T00:00:00Z", 
 "totalDuration": 0 
 }, 
 "domaintoolsirisdetect": [ 
 {}, 
 {}, 
 {} 
 ], 
 "dsassets": [ 
 {}, 
 {}, 
 {} 
 ], 
 "dscomments": [ 
 {}, 
 {}, 
 {} 
 ], 
 "emaildeletefrombrand": "Unspecified", 
 "emaildeletetype": "soft", 
 "endpoint": [ 
 {} 
 ], 
 "externalid": "294018", 
 "extrahoprevealxdetectiondevices": [ 
 {}, 
 {}, 
 {} 
 ], 
 "extrahoprevealxmitretechniques": [ 
 {}, 
 {}, 
 {} 
 ], 
 "filerelationships": [ 
 {}, 
 {}, 
 {} 
 ], 
 "fortisiemattacktactics": [ 
 {}, 
 {} 
 ], 
 "fortisiemevents": [ 
 {} 
 ], 
 "incidentduration": { 
 "accumulatedPause": 0, 
 "breachTriggered": false, 
 "dueDate": "0001-01-01T00:00:00Z", 
 "endDate": "0001-01-01T00:00:00Z", 
 "lastPauseDate": "0001-01-01T00:00:00Z", 
 "runStatus": "idle", 
 "sla": 0, 
 "slaStatus": -1, 
 "startDate": "0001-01-01T00:00:00Z", 
 "totalDuration": 0 
 }, 
 "incidentrdpachehuntingstringssimilarity": [ 
 {}, 
 {}, 
 {} 
 ], 
 "incidentrdpcachehuntingstringsifter": [ 
 {}, 
 {}, 
 {} 
 ], 
 "inventasource": [ 
 {} 
 ], 
 "isactive": "true", 
 "microsoft365defendercomments": [ 
 {}, 
 {}, 
 {} 
 ], 
 "microsoftsentinelowner": [], 
 "qintelqwatchexposures": [ 
 {}, 
 {}, 
 {} 
 ], 
 "remediationsla": { 
 "accumulatedPause": 0, 
 "breachTriggered": false, 
 "dueDate": "0001-01-01T00:00:00Z", 
 "endDate": "0001-01-01T00:00:00Z", 
 "lastPauseDate": "0001-01-01T00:00:00Z", 
 "runStatus": "idle", 
 "sla": 7200, 
 "slaStatus": -1, 
 "startDate": "0001-01-01T00:00:00Z", 
 "totalDuration": 0 
 }, 
 "riskiqautoexcludewhitelistedipaddress": "Yes", 
 "riskiqautowhitelistipaddress": "Yes", 
 "rsametasevents": [], 
 "rsarawlogslist": [], 
 "saassecuritycategory": "no_reason", 
 "saassecurityremediationtype": "Remove public sharing", 
 "saassecuritystate": "open", 
 "saassecuritystatus": "open-new", 
 "securitypolicymatch": [ 
 {} 
 ], 
 "selectaction": "Close", 
 "servicenowbusinessimpact": "1 - Critical", 
 "servicenowcategory": "Inquiry / Help", 
 "servicenowimpact": "1 - High", 
 "servicenownotify": "Send Email", 
 "servicenowpriority": "1 - Critical", 
 "servicenowseverity": "1 - High", 
 "servicenowsircategory": "Confidential personal identity data exposure", 
 "servicenowsirstate": "New", 
 "servicenowstate": "1 - New", 
 "servicenowurgency": "1 - High", 
 "similarincidentsdbot": [ 
 {} 
 ], 
 "spycloudcompassdevicedata": [ 
 {}, 
 {}, 
 {} 
 ], 
 "suspiciousexecutions": [ 
 {}, 
 {}, 
 {} 
 ], 
 "timetoassignment": { 
 "accumulatedPause": 0, 
 "breachTriggered": false, 
 "dueDate": "0001-01-01T00:00:00Z", 
 "endDate": "0001-01-01T00:00:00Z", 
 "lastPauseDate": "0001-01-01T00:00:00Z", 
 "runStatus": "idle", 
 "sla": 0, 
 "slaStatus": -1, 
 "startDate": "0001-01-01T00:00:00Z", 
 "totalDuration": 0 
 }, 
 "triagesla": { 
 "accumulatedPause": 0, 
 "breachTriggered": false, 
 "dueDate": "0001-01-01T00:00:00Z", 
 "endDate": "0001-01-01T00:00:00Z", 
 "lastPauseDate": "0001-01-01T00:00:00Z", 
 "runStatus": "idle", 
 "sla": 30, 
 "slaStatus": -1, 
 "startDate": "0001-01-01T00:00:00Z", 
 "totalDuration": 0 
 }, 
 "urlsslverification": [], 
 "xdralertsearchresults": [ 
 {}, 
 {}, 
 {} 
 ], 
 "xdrinvestigationresults": [ 
 {}, 
 {}, 
 {}, 
 { 
 "columnheader1": "" 
 }, 
 {}, 
 { 
 "columnheader1": "" 
 }, 
 {}, 
 {} 
 ], 
 "xpanseserviceclassifications": [ 
 {}, 
 {}, 
 {} 
 ], 
 "xpanseservicevalidation": [ 
 { 
 "columnheader1": "" 
 }, 
 {}, 
 {} 
 ] 
 }, 
 "account": "", 
 "autime": 1745746984163000000, 
 "type": "default_type", 
 "rawType": "default_type", 
 "name": "VhAYsOwx", 
 "rawName": "VhAYsOwx", 
 "status": 1, 
 "custom_status": "", 
 "resolution_status": "", 
 "reason": "", 
 "created": "2025-04-27T09:43:04.163Z", 
 "occurred": "2025-04-27T09:43:04.551517754Z", 
 "closed": "0001-01-01T00:00:00Z", 
 "sla": 0, 
 "severity": 1, 
 "investigationId": "", 
 "labels": [ 
 { 
 "value": "user@company.com", 
 "type": "Instance" 
 }, 
 { 
 "value": "Manual", 
 "type": "Brand" 
 } 
 ], 
 "attachment": [ 
 { 
 "name": "TUdZ0Ddm.text", 
 "type": "text/plain", 
 "path": "294018_c1790a2c-61d7-4ac8-8329-8883d70dae50_TUdZ0Ddm.text", 
 "description": "", 
 "showMediaFile": false, 
 "isTempPath": false 
 } 
 ], 
 "details": "", 
 "openDuration": 0, 
 "lastOpen": "0001-01-01T00:00:00Z", 
 "closingUserId": "", 
 "owner": "", 
 "activated": "0001-01-01T00:00:00Z", 
 "closeReason": "", 
 "rawCloseReason": "", 
 "closeNotes": "", 
 "playbookId": "", 
 "dueDate": "0001-01-01T00:00:00Z", 
 "reminder": "0001-01-01T00:00:00Z", 
 "runStatus": "", 
 "notifyTime": "0001-01-01T00:00:00Z", 
 "phase": "", 
 "rawPhase": "", 
 "isPlayground": false, 
 "rawJSON": "", 
 "parent": "", 
 "parentXDRIncident": "", 
 "retained": false, 
 "exported": false, 
 "category": "", 
 "rawCategory": "", 
 "linkedIncidents": [], 
 "linkedCount": 0, 
 "droppedCount": 0, 
 "sourceInstance": "user@company.com", 
 "sourceBrand": "Manual", 
 "canvases": null, 
 "lastJobRunTime": "0001-01-01T00:00:00Z", 
 "feedBased": false, 
 "dbotMirrorId": "", 
 "dbotMirrorInstance": "", 
 "dbotMirrorDirection": "", 
 "dbotDirtyFields": null, 
 "dbotCurrentDirtyFields": null, 
 "dbotMirrorTags": null, 
 "dbotMirrorLastSync": "0001-01-01T00:00:00Z", 
 "isDebug": false, 
 "dedupID": "", 
 "haIntegrationEventID": "", 
 "haOriginalID": "", 
 "changeStatus": "", 
 "insights": 0 
 } 

 Previous Incident Fields 

 Next Indicators 

 Last updated 1 month ago 

 Was this helpful?
