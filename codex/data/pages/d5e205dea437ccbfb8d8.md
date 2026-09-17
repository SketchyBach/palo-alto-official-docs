---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-api/cortex-xsoar-6.x-apis/scripts
fetched_at: 2026-09-16T09:04:08Z
source: cortex-platform
---

# Scripts | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 API 

 Cortex XSOAR 

 XSOAR 6.x APIs 

 Cortex XSOAR 6.x APIs 

 Scripts 

 APIs for managing scripts (automations) 

 Create or update automation 

 post https://hostname /automation 

 Create or update a given automation. 

 Authorizations 

 api_key 

 Authorization string Required 

 Body 

 application/json 

 filter object · GenericStringFilter Optional 

 GenericStringFilter is a general filter that will fetch entities using the Query value 

 Show properties 

 savePassword boolean Optional 

 script object · AutomationScript Optional 

 AutomationScript represents a script that will run on the system 

 Show properties 

 Responses 

 200 

 The saved automation. 

 application/json 

 pythonEnabled boolean Optional 

 scripts object · ScriptAPI ...[] Optional 

 Show properties 

 selectedScript object Optional 

 Show properties 

 suggestions string[] Optional 

 post /automation 

 HTTP 

 Ask Copy 

 POST /automation HTTP/1.1 
 Host: hostname 
 Authorization: YOUR_API_KEY 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 2329 

 { 
 "filter": { 
 "Cache": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "ignoreWorkers": true, 
 "page": 1, 
 "query": "text", 
 "searchAfter": [ 
 "text" 
 ], 
 "searchAfterElastic": [ 
 "text" 
 ], 
 "searchAfterMap": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "searchAfterMapOrder": { 
 "ANY_ADDITIONAL_PROPERTY": 1 
 }, 
 "searchBefore": [ 
 "text" 
 ], 
 "searchBeforeElastic": [ 
 "text" 
 ], 
 "size": 1, 
 "sort": [ 
 { 
 "asc": true, 
 "field": "text", 
 "fieldType": "text" 
 } 
 ] 
 }, 
 "savePassword": true, 
 "script": { 
 "MainEngineInfo": { 
 "engine": "text", 
 "engineGroup": "text" 
 }, 
 "allRead": true, 
 "allReadWrite": true, 
 "arguments": [ 
 { 
 "auto": "text", 
 "default": true, 
 "defaultValue": "text", 
 "deprecated": true, 
 "description": "text", 
 "hidden": true, 
 "isArray": true, 
 "name": "text", 
 "predefined": [ 
 "text" 
 ], 
 "required": true, 
 "secret": true, 
 "type": "text" 
 } 
 ], 
 "cacheVersn": 1, 
 "comment": "text", 
 "commitMessage": "text", 
 "contextKeys": [ 
 "text" 
 ], 
 "created": "2026-01-01T00:00:00.000Z", 
 "dbotCreatedBy": "text", 
 "definitionId": "text", 
 "dependsOn": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "deprecated": true, 
 "detached": true, 
 "dockerImage": "text", 
 "enabled": true, 
 "engine": "text", 
 "engineGroup": "text", 
 "fromServerVersion": { 
 "Digits": [ 
 1 
 ], 
 "Label": "text" 
 }, 
 "hasRole": true, 
 "hidden": true, 
 "highlight": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "id": "text", 
 "important": [ 
 { 
 "contextPath": "text", 
 "description": "text", 
 "related": "text" 
 } 
 ], 
 "indexName": "text", 
 "itemVersion": { 
 "Digits": [ 
 1 
 ], 
 "Label": "text" 
 }, 
 "locked": true, 
 "modified": "2026-01-01T00:00:00.000Z", 
 "name": "text", 
 "numericId": 1, 
 "outputs": [ 
 { 
 "contentPath": "text", 
 "contextPath": "text", 
 "description": {}, 
 "type": "text" 
 } 
 ], 
 "packID": "text", 
 "packName": "text", 
 "packPropagationLabels": [ 
 "text" 
 ], 
 "polling": true, 
 "prevName": "text", 
 "previousAllRead": true, 
 "previousAllReadWrite": true, 
 "previousRoles": [ 
 "text" 
 ], 
 "primaryTerm": 1, 
 "private": true, 
 "propagationLabels": [ 
 "text" 
 ], 
 "pswd": "text", 
 "rawTags": [ 
 "text" 
 ], 
 "remote": true, 
 "roles": [ 
 "text" 
 ], 
 "runAs": "text", 
 "runOnce": true, 
 "script": "text", 
 "scriptTarget": 1, 
 "searchableName": "text", 
 "sensitive": true, 
 "sequenceNumber": 1, 
 "shouldCommit": true, 
 "sizeInBytes": 1, 
 "sortValues": [ 
 "text" 
 ], 
 "sourceScripID": "text", 
 "subtype": "text", 
 "syncHash": "text", 
 "system": true, 
 "tags": [ 
 "text" 
 ], 
 "timeout": 1, 
 "toServerVersion": { 
 "Digits": [ 
 1 
 ], 
 "Label": "text" 
 }, 
 "type": "text", 
 "user": "text", 
 "vcShouldIgnore": true, 
 "vcShouldKeepItemLegacyProdMachine": true, 
 "version": 1, 
 "visualScript": "text", 
 "xsoarHasReadOnlyRole": true, 
 "xsoarPreviousReadOnlyRoles": [ 
 "text" 
 ], 
 "xsoarReadOnlyRoles": [ 
 "text" 
 ] 
 } 
 } 

 application/json 

 200 

 The saved automation. 

 Ask Copy 

 { 
 "pythonEnabled": true, 
 "scripts": [ 
 { 
 "arguments": [ 
 { 
 "auto": "text", 
 "default": true, 
 "defaultValue": "text", 
 "deprecated": true, 
 "description": "text", 
 "hidden": true, 
 "isArray": true, 
 "name": "text", 
 "predefined": [ 
 "text" 
 ], 
 "required": true, 
 "secret": true, 
 "type": "text" 
 } 
 ], 
 "comment": "text", 
 "contextKeys": [ 
 "text" 
 ], 
 "dependsOn": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "deprecated": true, 
 "detached": true, 
 "dockerImage": "text", 
 "enabled": true, 
 "hidden": true, 
 "id": "text", 
 "locked": true, 
 "modified": "2026-01-01T00:00:00.000Z", 
 "name": "text", 
 "outputs": [ 
 { 
 "contentPath": "text", 
 "contextPath": "text", 
 "description": {}, 
 "type": "text" 
 } 
 ], 
 "permitted": true, 
 "polling": true, 
 "propagationLabels": [ 
 "text" 
 ], 
 "roles": [ 
 "text" 
 ], 
 "runAs": "text", 
 "scriptTarget": 1, 
 "system": true, 
 "tags": [ 
 "text" 
 ], 
 "type": "text", 
 "user": "text", 
 "version": 1 
 } 
 ], 
 "selectedScript": { 
 "ANY_ADDITIONAL_PROPERTY": {} 
 }, 
 "suggestions": [ 
 "text" 
 ] 
 } 

 Copy automation 

 post https://hostname /automation/copy 

 Copy given automation 

 Authorizations 

 api_key 

 Authorization string Required 

 Body 

 application/json 

 filter object · GenericStringFilter Optional 

 GenericStringFilter is a general filter that will fetch entities using the Query value 

 Show properties 

 savePassword boolean Optional 

 script object · AutomationScript Optional 

 AutomationScript represents a script that will run on the system 

 Show properties 

 Responses 

 200 

 The saved automation. 

 application/json 

 pythonEnabled boolean Optional 

 scripts object · ScriptAPI ...[] Optional 

 Show properties 

 selectedScript object Optional 

 Show properties 

 suggestions string[] Optional 

 post /automation/copy 

 HTTP 

 Ask Copy 

 POST /automation/copy HTTP/1.1 
 Host: hostname 
 Authorization: YOUR_API_KEY 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 2329 

 { 
 "filter": { 
 "Cache": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "ignoreWorkers": true, 
 "page": 1, 
 "query": "text", 
 "searchAfter": [ 
 "text" 
 ], 
 "searchAfterElastic": [ 
 "text" 
 ], 
 "searchAfterMap": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "searchAfterMapOrder": { 
 "ANY_ADDITIONAL_PROPERTY": 1 
 }, 
 "searchBefore": [ 
 "text" 
 ], 
 "searchBeforeElastic": [ 
 "text" 
 ], 
 "size": 1, 
 "sort": [ 
 { 
 "asc": true, 
 "field": "text", 
 "fieldType": "text" 
 } 
 ] 
 }, 
 "savePassword": true, 
 "script": { 
 "MainEngineInfo": { 
 "engine": "text", 
 "engineGroup": "text" 
 }, 
 "allRead": true, 
 "allReadWrite": true, 
 "arguments": [ 
 { 
 "auto": "text", 
 "default": true, 
 "defaultValue": "text", 
 "deprecated": true, 
 "description": "text", 
 "hidden": true, 
 "isArray": true, 
 "name": "text", 
 "predefined": [ 
 "text" 
 ], 
 "required": true, 
 "secret": true, 
 "type": "text" 
 } 
 ], 
 "cacheVersn": 1, 
 "comment": "text", 
 "commitMessage": "text", 
 "contextKeys": [ 
 "text" 
 ], 
 "created": "2026-01-01T00:00:00.000Z", 
 "dbotCreatedBy": "text", 
 "definitionId": "text", 
 "dependsOn": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "deprecated": true, 
 "detached": true, 
 "dockerImage": "text", 
 "enabled": true, 
 "engine": "text", 
 "engineGroup": "text", 
 "fromServerVersion": { 
 "Digits": [ 
 1 
 ], 
 "Label": "text" 
 }, 
 "hasRole": true, 
 "hidden": true, 
 "highlight": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "id": "text", 
 "important": [ 
 { 
 "contextPath": "text", 
 "description": "text", 
 "related": "text" 
 } 
 ], 
 "indexName": "text", 
 "itemVersion": { 
 "Digits": [ 
 1 
 ], 
 "Label": "text" 
 }, 
 "locked": true, 
 "modified": "2026-01-01T00:00:00.000Z", 
 "name": "text", 
 "numericId": 1, 
 "outputs": [ 
 { 
 "contentPath": "text", 
 "contextPath": "text", 
 "description": {}, 
 "type": "text" 
 } 
 ], 
 "packID": "text", 
 "packName": "text", 
 "packPropagationLabels": [ 
 "text" 
 ], 
 "polling": true, 
 "prevName": "text", 
 "previousAllRead": true, 
 "previousAllReadWrite": true, 
 "previousRoles": [ 
 "text" 
 ], 
 "primaryTerm": 1, 
 "private": true, 
 "propagationLabels": [ 
 "text" 
 ], 
 "pswd": "text", 
 "rawTags": [ 
 "text" 
 ], 
 "remote": true, 
 "roles": [ 
 "text" 
 ], 
 "runAs": "text", 
 "runOnce": true, 
 "script": "text", 
 "scriptTarget": 1, 
 "searchableName": "text", 
 "sensitive": true, 
 "sequenceNumber": 1, 
 "shouldCommit": true, 
 "sizeInBytes": 1, 
 "sortValues": [ 
 "text" 
 ], 
 "sourceScripID": "text", 
 "subtype": "text", 
 "syncHash": "text", 
 "system": true, 
 "tags": [ 
 "text" 
 ], 
 "timeout": 1, 
 "toServerVersion": { 
 "Digits": [ 
 1 
 ], 
 "Label": "text" 
 }, 
 "type": "text", 
 "user": "text", 
 "vcShouldIgnore": true, 
 "vcShouldKeepItemLegacyProdMachine": true, 
 "version": 1, 
 "visualScript": "text", 
 "xsoarHasReadOnlyRole": true, 
 "xsoarPreviousReadOnlyRoles": [ 
 "text" 
 ], 
 "xsoarReadOnlyRoles": [ 
 "text" 
 ] 
 } 
 } 

 application/json 

 200 

 The saved automation. 

 Ask Copy 

 { 
 "pythonEnabled": true, 
 "scripts": [ 
 { 
 "arguments": [ 
 { 
 "auto": "text", 
 "default": true, 
 "defaultValue": "text", 
 "deprecated": true, 
 "description": "text", 
 "hidden": true, 
 "isArray": true, 
 "name": "text", 
 "predefined": [ 
 "text" 
 ], 
 "required": true, 
 "secret": true, 
 "type": "text" 
 } 
 ], 
 "comment": "text", 
 "contextKeys": [ 
 "text" 
 ], 
 "dependsOn": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "deprecated": true, 
 "detached": true, 
 "dockerImage": "text", 
 "enabled": true, 
 "hidden": true, 
 "id": "text", 
 "locked": true, 
 "modified": "2026-01-01T00:00:00.000Z", 
 "name": "text", 
 "outputs": [ 
 { 
 "contentPath": "text", 
 "contextPath": "text", 
 "description": {}, 
 "type": "text" 
 } 
 ], 
 "permitted": true, 
 "polling": true, 
 "propagationLabels": [ 
 "text" 
 ], 
 "roles": [ 
 "text" 
 ], 
 "runAs": "text", 
 "scriptTarget": 1, 
 "system": true, 
 "tags": [ 
 "text" 
 ], 
 "type": "text", 
 "user": "text", 
 "version": 1 
 } 
 ], 
 "selectedScript": { 
 "ANY_ADDITIONAL_PROPERTY": {} 
 }, 
 "suggestions": [ 
 "text" 
 ] 
 } 

 Delete existing automation 

 post https://hostname /automation/delete 

 Delete a given automation from the system. 

 Authorizations 

 api_key 

 Authorization string Required 

 Body 

 application/json 

 filter object · GenericStringFilter Optional 

 GenericStringFilter is a general filter that will fetch entities using the Query value 

 Show properties 

 savePassword boolean Optional 

 script object · AutomationScript Optional 

 AutomationScript represents a script that will run on the system 

 Show properties 

 Responses 

 200 

 automation deleted 

 No content 

 post /automation/delete 

 HTTP 

 Ask Copy 

 POST /automation/delete HTTP/1.1 
 Host: hostname 
 Authorization: YOUR_API_KEY 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 2329 

 { 
 "filter": { 
 "Cache": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "ignoreWorkers": true, 
 "page": 1, 
 "query": "text", 
 "searchAfter": [ 
 "text" 
 ], 
 "searchAfterElastic": [ 
 "text" 
 ], 
 "searchAfterMap": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "searchAfterMapOrder": { 
 "ANY_ADDITIONAL_PROPERTY": 1 
 }, 
 "searchBefore": [ 
 "text" 
 ], 
 "searchBeforeElastic": [ 
 "text" 
 ], 
 "size": 1, 
 "sort": [ 
 { 
 "asc": true, 
 "field": "text", 
 "fieldType": "text" 
 } 
 ] 
 }, 
 "savePassword": true, 
 "script": { 
 "MainEngineInfo": { 
 "engine": "text", 
 "engineGroup": "text" 
 }, 
 "allRead": true, 
 "allReadWrite": true, 
 "arguments": [ 
 { 
 "auto": "text", 
 "default": true, 
 "defaultValue": "text", 
 "deprecated": true, 
 "description": "text", 
 "hidden": true, 
 "isArray": true, 
 "name": "text", 
 "predefined": [ 
 "text" 
 ], 
 "required": true, 
 "secret": true, 
 "type": "text" 
 } 
 ], 
 "cacheVersn": 1, 
 "comment": "text", 
 "commitMessage": "text", 
 "contextKeys": [ 
 "text" 
 ], 
 "created": "2026-01-01T00:00:00.000Z", 
 "dbotCreatedBy": "text", 
 "definitionId": "text", 
 "dependsOn": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "deprecated": true, 
 "detached": true, 
 "dockerImage": "text", 
 "enabled": true, 
 "engine": "text", 
 "engineGroup": "text", 
 "fromServerVersion": { 
 "Digits": [ 
 1 
 ], 
 "Label": "text" 
 }, 
 "hasRole": true, 
 "hidden": true, 
 "highlight": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "id": "text", 
 "important": [ 
 { 
 "contextPath": "text", 
 "description": "text", 
 "related": "text" 
 } 
 ], 
 "indexName": "text", 
 "itemVersion": { 
 "Digits": [ 
 1 
 ], 
 "Label": "text" 
 }, 
 "locked": true, 
 "modified": "2026-01-01T00:00:00.000Z", 
 "name": "text", 
 "numericId": 1, 
 "outputs": [ 
 { 
 "contentPath": "text", 
 "contextPath": "text", 
 "description": {}, 
 "type": "text" 
 } 
 ], 
 "packID": "text", 
 "packName": "text", 
 "packPropagationLabels": [ 
 "text" 
 ], 
 "polling": true, 
 "prevName": "text", 
 "previousAllRead": true, 
 "previousAllReadWrite": true, 
 "previousRoles": [ 
 "text" 
 ], 
 "primaryTerm": 1, 
 "private": true, 
 "propagationLabels": [ 
 "text" 
 ], 
 "pswd": "text", 
 "rawTags": [ 
 "text" 
 ], 
 "remote": true, 
 "roles": [ 
 "text" 
 ], 
 "runAs": "text", 
 "runOnce": true, 
 "script": "text", 
 "scriptTarget": 1, 
 "searchableName": "text", 
 "sensitive": true, 
 "sequenceNumber": 1, 
 "shouldCommit": true, 
 "sizeInBytes": 1, 
 "sortValues": [ 
 "text" 
 ], 
 "sourceScripID": "text", 
 "subtype": "text", 
 "syncHash": "text", 
 "system": true, 
 "tags": [ 
 "text" 
 ], 
 "timeout": 1, 
 "toServerVersion": { 
 "Digits": [ 
 1 
 ], 
 "Label": "text" 
 }, 
 "type": "text", 
 "user": "text", 
 "vcShouldIgnore": true, 
 "vcShouldKeepItemLegacyProdMachine": true, 
 "version": 1, 
 "visualScript": "text", 
 "xsoarHasReadOnlyRole": true, 
 "xsoarPreviousReadOnlyRoles": [ 
 "text" 
 ], 
 "xsoarReadOnlyRoles": [ 
 "text" 
 ] 
 } 
 } 

 application/json 

 200 

 automation deleted 

 No content 

 Import an automation 

 post https://hostname /automation/import 

 Import an automation to Cortex XSOAR 

 Authorizations 

 api_key 

 Authorization string Required 

 Body 

 multipart/form-data 

 file string Optional 

 file 

 Responses 

 200 

 The saved automation 

 application/json 

 AutomationScript represents a script that will run on the system 

 MainEngineInfo object · EngineInfo ... Optional 

 Show properties 

 allRead boolean Optional 

 allReadWrite boolean Optional 

 arguments object · Argument[] Optional 

 Argument to a module command 

 Show properties 

 cacheVersn integer · int64 Optional 

 comment string Optional 

 commitMessage string Optional 

 contextKeys string[] Optional 

 created string · date-time Optional 

 dbotCreatedBy string Optional 

 Who has created this event - relevant only for manual incidents 

 definitionId string Optional 

 dependsOn object Optional 

 This fields indicates which commands this script depends on 

 Show properties 

 deprecated boolean Optional 

 detached boolean Optional 

 dockerImage string Optional 

 enabled boolean Optional 

 engine string Optional 

 Engine that will run the script 

 engineGroup string Optional 

 EngineGroup that will run the script 

 fromServerVersion object · Version represents a version. Optional 

 Show properties 

 hasRole boolean Optional 

 Internal field to make queries on role faster 

 hidden boolean Optional 

 highlight object Optional 

 Show properties 

 id string Optional 

 important object · Important[] Optional 

 Important The important outputs of a given command 

 Show properties 

 indexName string Optional 

 itemVersion object · Version represents a version. Optional 

 Show properties 

 locked boolean Optional 

 modified string · date-time Optional 

 name string Optional 

 numericId integer · int64 Optional 

 outputs object · Output[] Optional 

 Output of a module command 

 Show properties 

 packID string Optional 

 packName string Optional 

 packPropagationLabels string[] Optional 

 polling boolean Optional 

 prevName string Optional 

 previousAllRead boolean Optional 

 previousAllReadWrite boolean Optional 

 previousRoles string[] Optional 

 Do not change this field manually 

 primaryTerm integer · int64 Optional 

 private boolean Optional 

 propagationLabels string[] Optional 

 pswd string Optional 

 rawTags string[] Optional 

 remote boolean Optional 

 roles string[] Optional 

 The role assigned to this investigation 

 runAs string Optional 

 runOnce boolean Optional 

 script string Optional 

 scriptTarget integer · int64 Optional 

 ScriptTarget represents the module where this script should run 

 searchableName string Optional 

 sensitive boolean Optional 

 sequenceNumber integer · int64 Optional 

 shouldCommit boolean Optional 

 sizeInBytes integer · int64 Optional 

 sortValues string[] Optional 

 sourceScripID string Optional 

 subtype string Optional 

 ScriptSubType holds the script type version 

 syncHash string Optional 

 system boolean Optional 

 tags string[] Optional 

 timeout integer · int64 Optional 

 A Duration represents the elapsed time between two instants
as an int64 nanosecond count. The representation limits the
largest representable duration to approximately 290 years. 

 toServerVersion object · Version represents a version. Optional 

 Show properties 

 type string Optional 

 ScriptType holds the type of a script 

 user string Optional 

 vcShouldIgnore boolean Optional 

 vcShouldKeepItemLegacyProdMachine boolean Optional 

 version integer · int64 Optional 

 visualScript string Optional 

 xsoarHasReadOnlyRole boolean Optional 

 xsoarPreviousReadOnlyRoles string[] Optional 

 xsoarReadOnlyRoles string[] Optional 

 post /automation/import 

 HTTP 

 Ask Copy 

 POST /automation/import HTTP/1.1 
 Host: hostname 
 Authorization: YOUR_API_KEY 
 Content-Type: multipart/form-data 
 Accept: */* 
 Content-Length: 15 

 { 
 "file": "text" 
 } 

 200 

 The saved automation 

 Ask Copy 

 { 
 "MainEngineInfo": { 
 "engine": "text", 
 "engineGroup": "text" 
 }, 
 "allRead": true, 
 "allReadWrite": true, 
 "arguments": [ 
 { 
 "auto": "text", 
 "default": true, 
 "defaultValue": "text", 
 "deprecated": true, 
 "description": "text", 
 "hidden": true, 
 "isArray": true, 
 "name": "text", 
 "predefined": [ 
 "text" 
 ], 
 "required": true, 
 "secret": true, 
 "type": "text" 
 } 
 ], 
 "cacheVersn": 1, 
 "comment": "text", 
 "commitMessage": "text", 
 "contextKeys": [ 
 "text" 
 ], 
 "created": "2026-01-01T00:00:00.000Z", 
 "dbotCreatedBy": "text", 
 "definitionId": "text", 
 "dependsOn": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "deprecated": true, 
 "detached": true, 
 "dockerImage": "text", 
 "enabled": true, 
 "engine": "text", 
 "engineGroup": "text", 
 "fromServerVersion": { 
 "Digits": [ 
 1 
 ], 
 "Label": "text" 
 }, 
 "hasRole": true, 
 "hidden": true, 
 "highlight": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "id": "text", 
 "important": [ 
 { 
 "contextPath": "text", 
 "description": "text", 
 "related": "text" 
 } 
 ], 
 "indexName": "text", 
 "itemVersion": { 
 "Digits": [ 
 1 
 ], 
 "Label": "text" 
 }, 
 "locked": true, 
 "modified": "2026-01-01T00:00:00.000Z", 
 "name": "text", 
 "numericId": 1, 
 "outputs": [ 
 { 
 "contentPath": "text", 
 "contextPath": "text", 
 "description": {}, 
 "type": "text" 
 } 
 ], 
 "packID": "text", 
 "packName": "text", 
 "packPropagationLabels": [ 
 "text" 
 ], 
 "polling": true, 
 "prevName": "text", 
 "previousAllRead": true, 
 "previousAllReadWrite": true, 
 "previousRoles": [ 
 "text" 
 ], 
 "primaryTerm": 1, 
 "private": true, 
 "propagationLabels": [ 
 "text" 
 ], 
 "pswd": "text", 
 "rawTags": [ 
 "text" 
 ], 
 "remote": true, 
 "roles": [ 
 "text" 
 ], 
 "runAs": "text", 
 "runOnce": true, 
 "script": "text", 
 "scriptTarget": 1, 
 "searchableName": "text", 
 "sensitive": true, 
 "sequenceNumber": 1, 
 "shouldCommit": true, 
 "sizeInBytes": 1, 
 "sortValues": [ 
 "text" 
 ], 
 "sourceScripID": "text", 
 "subtype": "text", 
 "syncHash": "text", 
 "system": true, 
 "tags": [ 
 "text" 
 ], 
 "timeout": 1, 
 "toServerVersion": { 
 "Digits": [ 
 1 
 ], 
 "Label": "text" 
 }, 
 "type": "text", 
 "user": "text", 
 "vcShouldIgnore": true, 
 "vcShouldKeepItemLegacyProdMachine": true, 
 "version": 1, 
 "visualScript": "text", 
 "xsoarHasReadOnlyRole": true, 
 "xsoarPreviousReadOnlyRoles": [ 
 "text" 
 ], 
 "xsoarReadOnlyRoles": [ 
 "text" 
 ] 
 } 

 Search Automation (aka scripts) 

 post https://hostname /automation/search 

 Search Automation by filter 

 Authorizations 

 api_key 

 Authorization string Required 

 Body 

 application/json 

 automationScriptFilter is a general filter that fetches entities using a query string query using the Query value 

 Cache object Optional 

 Cache of join functions 

 Show properties 

 ignoreWorkers boolean Optional 

 Do not use workers mechanism while searching bleve 

 page integer · int64 Optional 

 0-based page 

 query string Optional 

 searchAfter string[] Optional 

 Efficient next page, pass max sort value from previous page 

 searchAfterElastic string[] Optional 

 Efficient next page, pass max ES sort value from previous page 

 searchAfterMap object Optional 

 Map accounts search after values - stores next page sort values per account.
There is no need to store searchBeforeMap as [current page searchBefore] equals to [prev page searchAfter]
More, there is no way to generate correct searchBefore from current page as some tenants may not appear at all.
The map is relevant in proxy mode and used by tenants, each tenant extracts the searchAfter keys from the map. 

 Show properties 

 searchAfterMapOrder object Optional 

 Show properties 

 searchBefore string[] Optional 

 Efficient prev page, pass min sort value from next page 

 searchBeforeElastic string[] Optional 

 Efficient prev page, pass min ES sort value from next page 

 size integer · int64 Optional 

 Size is limited to 1000, if not passed it defaults to 0, and no results will return 

 sort object · Order[] Optional 

 The sort order 

 Show properties 

 stripContext boolean Optional 

 Responses 

 200 

 automationScriptResult 

 application/json 

 pythonEnabled boolean Optional 

 scripts object · ScriptAPI ...[] Optional 

 Show properties 

 selectedScript object Optional 

 Show properties 

 suggestions string[] Optional 

 post /automation/search 

 HTTP 

 Ask Copy 

 POST /automation/search HTTP/1.1 
 Host: hostname 
 Authorization: YOUR_API_KEY 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 390 

 { 
 "Cache": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "ignoreWorkers": true, 
 "page": 1, 
 "query": "text", 
 "searchAfter": [ 
 "text" 
 ], 
 "searchAfterElastic": [ 
 "text" 
 ], 
 "searchAfterMap": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "searchAfterMapOrder": { 
 "ANY_ADDITIONAL_PROPERTY": 1 
 }, 
 "searchBefore": [ 
 "text" 
 ], 
 "searchBeforeElastic": [ 
 "text" 
 ], 
 "size": 1, 
 "sort": [ 
 { 
 "asc": true, 
 "field": "text", 
 "fieldType": "text" 
 } 
 ], 
 "stripContext": true 
 } 

 application/json 

 200 

 automationScriptResult 

 Ask Copy 

 { 
 "pythonEnabled": true, 
 "scripts": [ 
 { 
 "arguments": [ 
 { 
 "auto": "text", 
 "default": true, 
 "defaultValue": "text", 
 "deprecated": true, 
 "description": "text", 
 "hidden": true, 
 "isArray": true, 
 "name": "text", 
 "predefined": [ 
 "text" 
 ], 
 "required": true, 
 "secret": true, 
 "type": "text" 
 } 
 ], 
 "comment": "text", 
 "contextKeys": [ 
 "text" 
 ], 
 "dependsOn": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "deprecated": true, 
 "detached": true, 
 "dockerImage": "text", 
 "enabled": true, 
 "hidden": true, 
 "id": "text", 
 "locked": true, 
 "modified": "2026-01-01T00:00:00.000Z", 
 "name": "text", 
 "outputs": [ 
 { 
 "contentPath": "text", 
 "contextPath": "text", 
 "description": {}, 
 "type": "text" 
 } 
 ], 
 "permitted": true, 
 "polling": true, 
 "propagationLabels": [ 
 "text" 
 ], 
 "roles": [ 
 "text" 
 ], 
 "runAs": "text", 
 "scriptTarget": 1, 
 "system": true, 
 "tags": [ 
 "text" 
 ], 
 "type": "text", 
 "user": "text", 
 "version": 1 
 } 
 ], 
 "selectedScript": { 
 "ANY_ADDITIONAL_PROPERTY": {} 
 }, 
 "suggestions": [ 
 "text" 
 ] 
 } 

 Previous Reports 

 Next System Management 

 Last updated 1 month ago 

 Was this helpful?
