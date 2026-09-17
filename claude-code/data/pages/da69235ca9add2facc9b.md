---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-api/cortex-xsoar-6.x-apis/indicators
fetched_at: 2026-09-16T09:04:09Z
source: cortex-platform
---

# Indicators | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 API 

 Cortex XSOAR 

 XSOAR 6.x APIs 

 Cortex XSOAR 6.x APIs 

 Indicators 

 APIs for managing indicators 

 Create Indicator 

 post https://hostname /indicator/create 

 Create an indicator entity To update indicator custom fields you should lowercase them and remove all spaces. For example: Scan IP -> scanip 

 Authorizations 

 api_key 

 Authorization string Required 

 Body 

 application/json 

 entryId string Optional 

 indicator object · IocObject Optional 

 IocObject - represents an Ioc (or simply an indicator) object 

 Show properties 

 investigationId string Optional 

 manually boolean Optional 

 seenNow boolean Optional 

 Responses 

 200 

 IocObject 

 application/json 

 IocObject - represents an Ioc (or simply an indicator) object 

 CustomFields object · CustomFields ... Optional 

 The keys should be the field's display name all lower and without spaces. For example: Scan IP -> scanip
To get the actual key name you can also go to Cortex XSOAR CLI and run /incident_add and look for the key that you would like to update 

 Show properties 

 account string Optional 

 aggregatedReliability string Optional 

 cacheVersn integer · int64 Optional 

 calculatedTime string · date-time Optional 

 Do not set the fields bellow this line 

 comment string Optional 

 comments object · Comment ...[] Optional 

 Show properties 

 created string · date-time Optional 

 deletedFeedFetchTime string · date-time Optional 

 expiration string · date-time Optional 

 expirationSource object · ExpirationSource .. . Optional 

 Show properties 

 expirationStatus string Optional 

 firstSeen string · date-time Optional 

 firstSeenEntryID string Optional 

 highlight object Optional 

 Show properties 

 id string Optional 

 indexName string Optional 

 indicator_type string Optional 

 insightCache object · InsightCache Optional 

 InsightCache - map insight name to all its metadata, name will be case insensitive 

 Show properties 

 investigationIDs string[] Optional 

 isDetectable boolean Optional 

 isPreventable boolean Optional 

 isShared boolean Optional 

 lastReputationRun string · date-time Optional 

 lastSeen string · date-time Optional 

 lastSeenEntryID string Optional 

 manualExpirationTime string · date-time Optional 

 manualScore boolean Optional 

 manualSetTime string · date-time Optional 

 manuallyEditedFields string[] Optional 

 modified string · date-time Optional 

 modifiedTime string · date-time Optional 

 moduleToFeedMap object Optional 

 Show properties 

 numericId integer · int64 Optional 

 primaryTerm integer · int64 Optional 

 relatedIncCount integer · int64 Optional 

 score integer · int64 Optional 

 sequenceNumber integer · int64 Optional 

 setBy string Optional 

 sizeInBytes integer · int64 Optional 

 sortValues string[] Optional 

 source string Optional 

 sourceBrands string[] Optional 

 sourceInstances string[] Optional 

 syncHash string Optional 

 timestamp string · date-time Optional 

 value string Optional 

 version integer · int64 Optional 

 post /indicator/create 

 HTTP 

 Ask Copy 

 POST /indicator/create HTTP/1.1 
 Host: hostname 
 Authorization: YOUR_API_KEY 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 3617 

 { 
 "entryId": "text", 
 "indicator": { 
 "CustomFields": { 
 "ANY_ADDITIONAL_PROPERTY": {} 
 }, 
 "account": "text", 
 "aggregatedReliability": "text", 
 "cacheVersn": 1, 
 "calculatedTime": "2026-01-01T00:00:00.000Z", 
 "comment": "text", 
 "comments": [ 
 { 
 "cacheVersn": 1, 
 "category": "text", 
 "content": "text", 
 "created": "2026-01-01T00:00:00.000Z", 
 "entryId": "text", 
 "highlight": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "id": "text", 
 "indexName": "text", 
 "modified": "2026-01-01T00:00:00.000Z", 
 "numericId": 1, 
 "primaryTerm": 1, 
 "sequenceNumber": 1, 
 "sizeInBytes": 1, 
 "sortValues": [ 
 "text" 
 ], 
 "source": "text", 
 "syncHash": "text", 
 "type": "text", 
 "user": "text", 
 "version": 1 
 } 
 ], 
 "created": "2026-01-01T00:00:00.000Z", 
 "deletedFeedFetchTime": "2026-01-01T00:00:00.000Z", 
 "expiration": "2026-01-01T00:00:00.000Z", 
 "expirationSource": { 
 "brand": "text", 
 "expirationInterval": 1, 
 "expirationPolicy": "text", 
 "instance": "text", 
 "moduleId": "text", 
 "setTime": "2026-01-01T00:00:00.000Z", 
 "source": "text", 
 "user": "text" 
 }, 
 "expirationStatus": "text", 
 "firstSeen": "2026-01-01T00:00:00.000Z", 
 "firstSeenEntryID": "text", 
 "highlight": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "id": "text", 
 "indexName": "text", 
 "indicator_type": "text", 
 "insightCache": { 
 "cacheVersn": 1, 
 "created": "2026-01-01T00:00:00.000Z", 
 "highlight": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "id": "text", 
 "indexName": "text", 
 "modified": "2026-01-01T00:00:00.000Z", 
 "numericId": 1, 
 "primaryTerm": 1, 
 "scores": { 
 "ANY_ADDITIONAL_PROPERTY": { 
 "content": "text", 
 "contentFormat": "text", 
 "context": { 
 "ANY_ADDITIONAL_PROPERTY": {} 
 }, 
 "isTypedIndicator": true, 
 "reliability": "text", 
 "score": 1, 
 "scoreChangeTimestamp": "2026-01-01T00:00:00.000Z", 
 "timestamp": "2026-01-01T00:00:00.000Z", 
 "type": "text" 
 } 
 }, 
 "sequenceNumber": 1, 
 "sizeInBytes": 1, 
 "sortValues": [ 
 "text" 
 ], 
 "syncHash": "text", 
 "version": 1 
 }, 
 "investigationIDs": [ 
 "text" 
 ], 
 "isDetectable": true, 
 "isPreventable": true, 
 "isShared": true, 
 "lastReputationRun": "2026-01-01T00:00:00.000Z", 
 "lastSeen": "2026-01-01T00:00:00.000Z", 
 "lastSeenEntryID": "text", 
 "manualExpirationTime": "2026-01-01T00:00:00.000Z", 
 "manualScore": true, 
 "manualSetTime": "2026-01-01T00:00:00.000Z", 
 "manuallyEditedFields": [ 
 "text" 
 ], 
 "modified": "2026-01-01T00:00:00.000Z", 
 "modifiedTime": "2026-01-01T00:00:00.000Z", 
 "moduleToFeedMap": { 
 "ANY_ADDITIONAL_PROPERTY": { 
 "ExpirationSource": { 
 "brand": "text", 
 "expirationInterval": 1, 
 "expirationPolicy": "text", 
 "instance": "text", 
 "moduleId": "text", 
 "setTime": "2026-01-01T00:00:00.000Z", 
 "source": "text", 
 "user": "text" 
 }, 
 "bypassExclusionList": true, 
 "classifierId": "text", 
 "classifierVersion": 1, 
 "comments": [ 
 { 
 "content": "text", 
 "created": "2026-01-01T00:00:00.000Z", 
 "id": "text", 
 "user": "text" 
 } 
 ], 
 "expirationInterval": 1, 
 "expirationPolicy": "text", 
 "fetchTime": "2026-01-01T00:00:00.000Z", 
 "fields": { 
 "ANY_ADDITIONAL_PROPERTY": {} 
 }, 
 "isEnrichment": true, 
 "mapperId": "text", 
 "mapperVersion": 1, 
 "modifiedTime": "2026-01-01T00:00:00.000Z", 
 "moduleId": "text", 
 "rawJSON": { 
 "ANY_ADDITIONAL_PROPERTY": {} 
 }, 
 "relationships": [ 
 { 
 "brand": "text", 
 "entityA": "text", 
 "entityAFamily": "text", 
 "entityAType": "text", 
 "entityB": "text", 
 "entityBFamily": "text", 
 "entityBType": "text", 
 "fields": { 
 "ANY_ADDITIONAL_PROPERTY": {} 
 }, 
 "id": "text", 
 "instance": "text", 
 "name": "text", 
 "reliability": "text", 
 "reverseName": "text", 
 "startTime": "2026-01-01T00:00:00.000Z", 
 "type": "text" 
 } 
 ], 
 "reliability": "text", 
 "score": 1, 
 "sourceBrand": "text", 
 "sourceInstance": "text", 
 "timestamp": "2026-01-01T00:00:00.000Z", 
 "type": "text", 
 "value": "text" 
 } 
 }, 
 "numericId": 1, 
 "primaryTerm": 1, 
 "relatedIncCount": 1, 
 "score": 1, 
 "sequenceNumber": 1, 
 "setBy": "text", 
 "sizeInBytes": 1, 
 "sortValues": [ 
 "text" 
 ], 
 "source": "text", 
 "sourceBrands": [ 
 "text" 
 ], 
 "sourceInstances": [ 
 "text" 
 ], 
 "syncHash": "text", 
 "timestamp": "2026-01-01T00:00:00.000Z", 
 "value": "text", 
 "version": 1 
 }, 
 "investigationId": "text", 
 "manually": true, 
 "seenNow": true 
 } 

 application/json 

 200 

 IocObject 

 Ask Copy 

 { 
 "CustomFields": { 
 "ANY_ADDITIONAL_PROPERTY": {} 
 }, 
 "account": "text", 
 "aggregatedReliability": "text", 
 "cacheVersn": 1, 
 "calculatedTime": "2026-01-01T00:00:00.000Z", 
 "comment": "text", 
 "comments": [ 
 { 
 "cacheVersn": 1, 
 "category": "text", 
 "content": "text", 
 "created": "2026-01-01T00:00:00.000Z", 
 "entryId": "text", 
 "highlight": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "id": "text", 
 "indexName": "text", 
 "modified": "2026-01-01T00:00:00.000Z", 
 "numericId": 1, 
 "primaryTerm": 1, 
 "sequenceNumber": 1, 
 "sizeInBytes": 1, 
 "sortValues": [ 
 "text" 
 ], 
 "source": "text", 
 "syncHash": "text", 
 "type": "text", 
 "user": "text", 
 "version": 1 
 } 
 ], 
 "created": "2026-01-01T00:00:00.000Z", 
 "deletedFeedFetchTime": "2026-01-01T00:00:00.000Z", 
 "expiration": "2026-01-01T00:00:00.000Z", 
 "expirationSource": { 
 "brand": "text", 
 "expirationInterval": 1, 
 "expirationPolicy": "text", 
 "instance": "text", 
 "moduleId": "text", 
 "setTime": "2026-01-01T00:00:00.000Z", 
 "source": "text", 
 "user": "text" 
 }, 
 "expirationStatus": "text", 
 "firstSeen": "2026-01-01T00:00:00.000Z", 
 "firstSeenEntryID": "text", 
 "highlight": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "id": "text", 
 "indexName": "text", 
 "indicator_type": "text", 
 "insightCache": { 
 "cacheVersn": 1, 
 "created": "2026-01-01T00:00:00.000Z", 
 "highlight": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "id": "text", 
 "indexName": "text", 
 "modified": "2026-01-01T00:00:00.000Z", 
 "numericId": 1, 
 "primaryTerm": 1, 
 "scores": { 
 "ANY_ADDITIONAL_PROPERTY": { 
 "content": "text", 
 "contentFormat": "text", 
 "context": { 
 "ANY_ADDITIONAL_PROPERTY": {} 
 }, 
 "isTypedIndicator": true, 
 "reliability": "text", 
 "score": 1, 
 "scoreChangeTimestamp": "2026-01-01T00:00:00.000Z", 
 "timestamp": "2026-01-01T00:00:00.000Z", 
 "type": "text" 
 } 
 }, 
 "sequenceNumber": 1, 
 "sizeInBytes": 1, 
 "sortValues": [ 
 "text" 
 ], 
 "syncHash": "text", 
 "version": 1 
 }, 
 "investigationIDs": [ 
 "text" 
 ], 
 "isDetectable": true, 
 "isPreventable": true, 
 "isShared": true, 
 "lastReputationRun": "2026-01-01T00:00:00.000Z", 
 "lastSeen": "2026-01-01T00:00:00.000Z", 
 "lastSeenEntryID": "text", 
 "manualExpirationTime": "2026-01-01T00:00:00.000Z", 
 "manualScore": true, 
 "manualSetTime": "2026-01-01T00:00:00.000Z", 
 "manuallyEditedFields": [ 
 "text" 
 ], 
 "modified": "2026-01-01T00:00:00.000Z", 
 "modifiedTime": "2026-01-01T00:00:00.000Z", 
 "moduleToFeedMap": { 
 "ANY_ADDITIONAL_PROPERTY": { 
 "ExpirationSource": { 
 "brand": "text", 
 "expirationInterval": 1, 
 "expirationPolicy": "text", 
 "instance": "text", 
 "moduleId": "text", 
 "setTime": "2026-01-01T00:00:00.000Z", 
 "source": "text", 
 "user": "text" 
 }, 
 "bypassExclusionList": true, 
 "classifierId": "text", 
 "classifierVersion": 1, 
 "comments": [ 
 { 
 "content": "text", 
 "created": "2026-01-01T00:00:00.000Z", 
 "id": "text", 
 "user": "text" 
 } 
 ], 
 "expirationInterval": 1, 
 "expirationPolicy": "text", 
 "fetchTime": "2026-01-01T00:00:00.000Z", 
 "fields": { 
 "ANY_ADDITIONAL_PROPERTY": {} 
 }, 
 "isEnrichment": true, 
 "mapperId": "text", 
 "mapperVersion": 1, 
 "modifiedTime": "2026-01-01T00:00:00.000Z", 
 "moduleId": "text", 
 "rawJSON": { 
 "ANY_ADDITIONAL_PROPERTY": {} 
 }, 
 "relationships": [ 
 { 
 "brand": "text", 
 "entityA": "text", 
 "entityAFamily": "text", 
 "entityAType": "text", 
 "entityB": "text", 
 "entityBFamily": "text", 
 "entityBType": "text", 
 "fields": { 
 "ANY_ADDITIONAL_PROPERTY": {} 
 }, 
 "id": "text", 
 "instance": "text", 
 "name": "text", 
 "reliability": "text", 
 "reverseName": "text", 
 "startTime": "2026-01-01T00:00:00.000Z", 
 "type": "text" 
 } 
 ], 
 "reliability": "text", 
 "score": 1, 
 "sourceBrand": "text", 
 "sourceInstance": "text", 
 "timestamp": "2026-01-01T00:00:00.000Z", 
 "type": "text", 
 "value": "text" 
 } 
 }, 
 "numericId": 1, 
 "primaryTerm": 1, 
 "relatedIncCount": 1, 
 "score": 1, 
 "sequenceNumber": 1, 
 "setBy": "text", 
 "sizeInBytes": 1, 
 "sortValues": [ 
 "text" 
 ], 
 "source": "text", 
 "sourceBrands": [ 
 "text" 
 ], 
 "sourceInstances": [ 
 "text" 
 ], 
 "syncHash": "text", 
 "timestamp": "2026-01-01T00:00:00.000Z", 
 "value": "text", 
 "version": 1 
 } 

 Edit Indicator 

 post https://hostname /indicator/edit 

 Edit an indicator entity To update indicator custom fields you should lowercase them and remove all spaces. For example: Scan IP -> scanip 

 Authorizations 

 api_key 

 Authorization string Required 

 Body 

 application/json 

 IocObject - represents an Ioc (or simply an indicator) object 

 CustomFields object · CustomFields ... Optional 

 The keys should be the field's display name all lower and without spaces. For example: Scan IP -> scanip
To get the actual key name you can also go to Cortex XSOAR CLI and run /incident_add and look for the key that you would like to update 

 Show properties 

 account string Optional 

 aggregatedReliability string Optional 

 cacheVersn integer · int64 Optional 

 calculatedTime string · date-time Optional 

 Do not set the fields bellow this line 

 comment string Optional 

 comments object · Comment ...[] Optional 

 Show properties 

 created string · date-time Optional 

 deletedFeedFetchTime string · date-time Optional 

 expiration string · date-time Optional 

 expirationSource object · ExpirationSource .. . Optional 

 Show properties 

 expirationStatus string Optional 

 firstSeen string · date-time Optional 

 firstSeenEntryID string Optional 

 highlight object Optional 

 Show properties 

 id string Optional 

 indexName string Optional 

 indicator_type string Optional 

 insightCache object · InsightCache Optional 

 InsightCache - map insight name to all its metadata, name will be case insensitive 

 Show properties 

 investigationIDs string[] Optional 

 isDetectable boolean Optional 

 isPreventable boolean Optional 

 isShared boolean Optional 

 lastReputationRun string · date-time Optional 

 lastSeen string · date-time Optional 

 lastSeenEntryID string Optional 

 manualExpirationTime string · date-time Optional 

 manualScore boolean Optional 

 manualSetTime string · date-time Optional 

 manuallyEditedFields string[] Optional 

 modified string · date-time Optional 

 modifiedTime string · date-time Optional 

 moduleToFeedMap object Optional 

 Show properties 

 numericId integer · int64 Optional 

 primaryTerm integer · int64 Optional 

 relatedIncCount integer · int64 Optional 

 score integer · int64 Optional 

 sequenceNumber integer · int64 Optional 

 setBy string Optional 

 sizeInBytes integer · int64 Optional 

 sortValues string[] Optional 

 source string Optional 

 sourceBrands string[] Optional 

 sourceInstances string[] Optional 

 syncHash string Optional 

 timestamp string · date-time Optional 

 value string Optional 

 version integer · int64 Optional 

 Responses 

 200 

 IocObject 

 application/json 

 IocObject - represents an Ioc (or simply an indicator) object 

 CustomFields object · CustomFields ... Optional 

 The keys should be the field's display name all lower and without spaces. For example: Scan IP -> scanip
To get the actual key name you can also go to Cortex XSOAR CLI and run /incident_add and look for the key that you would like to update 

 Show properties 

 account string Optional 

 aggregatedReliability string Optional 

 cacheVersn integer · int64 Optional 

 calculatedTime string · date-time Optional 

 Do not set the fields bellow this line 

 comment string Optional 

 comments object · Comment ...[] Optional 

 Show properties 

 created string · date-time Optional 

 deletedFeedFetchTime string · date-time Optional 

 expiration string · date-time Optional 

 expirationSource object · ExpirationSource .. . Optional 

 Show properties 

 expirationStatus string Optional 

 firstSeen string · date-time Optional 

 firstSeenEntryID string Optional 

 highlight object Optional 

 Show properties 

 id string Optional 

 indexName string Optional 

 indicator_type string Optional 

 insightCache object · InsightCache Optional 

 InsightCache - map insight name to all its metadata, name will be case insensitive 

 Show properties 

 investigationIDs string[] Optional 

 isDetectable boolean Optional 

 isPreventable boolean Optional 

 isShared boolean Optional 

 lastReputationRun string · date-time Optional 

 lastSeen string · date-time Optional 

 lastSeenEntryID string Optional 

 manualExpirationTime string · date-time Optional 

 manualScore boolean Optional 

 manualSetTime string · date-time Optional 

 manuallyEditedFields string[] Optional 

 modified string · date-time Optional 

 modifiedTime string · date-time Optional 

 moduleToFeedMap object Optional 

 Show properties 

 numericId integer · int64 Optional 

 primaryTerm integer · int64 Optional 

 relatedIncCount integer · int64 Optional 

 score integer · int64 Optional 

 sequenceNumber integer · int64 Optional 

 setBy string Optional 

 sizeInBytes integer · int64 Optional 

 sortValues string[] Optional 

 source string Optional 

 sourceBrands string[] Optional 

 sourceInstances string[] Optional 

 syncHash string Optional 

 timestamp string · date-time Optional 

 value string Optional 

 version integer · int64 Optional 

 post /indicator/edit 

 HTTP 

 Ask Copy 

 POST /indicator/edit HTTP/1.1 
 Host: hostname 
 Authorization: YOUR_API_KEY 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 3530 

 { 
 "CustomFields": { 
 "ANY_ADDITIONAL_PROPERTY": {} 
 }, 
 "account": "text", 
 "aggregatedReliability": "text", 
 "cacheVersn": 1, 
 "calculatedTime": "2026-01-01T00:00:00.000Z", 
 "comment": "text", 
 "comments": [ 
 { 
 "cacheVersn": 1, 
 "category": "text", 
 "content": "text", 
 "created": "2026-01-01T00:00:00.000Z", 
 "entryId": "text", 
 "highlight": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "id": "text", 
 "indexName": "text", 
 "modified": "2026-01-01T00:00:00.000Z", 
 "numericId": 1, 
 "primaryTerm": 1, 
 "sequenceNumber": 1, 
 "sizeInBytes": 1, 
 "sortValues": [ 
 "text" 
 ], 
 "source": "text", 
 "syncHash": "text", 
 "type": "text", 
 "user": "text", 
 "version": 1 
 } 
 ], 
 "created": "2026-01-01T00:00:00.000Z", 
 "deletedFeedFetchTime": "2026-01-01T00:00:00.000Z", 
 "expiration": "2026-01-01T00:00:00.000Z", 
 "expirationSource": { 
 "brand": "text", 
 "expirationInterval": 1, 
 "expirationPolicy": "text", 
 "instance": "text", 
 "moduleId": "text", 
 "setTime": "2026-01-01T00:00:00.000Z", 
 "source": "text", 
 "user": "text" 
 }, 
 "expirationStatus": "text", 
 "firstSeen": "2026-01-01T00:00:00.000Z", 
 "firstSeenEntryID": "text", 
 "highlight": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "id": "text", 
 "indexName": "text", 
 "indicator_type": "text", 
 "insightCache": { 
 "cacheVersn": 1, 
 "created": "2026-01-01T00:00:00.000Z", 
 "highlight": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "id": "text", 
 "indexName": "text", 
 "modified": "2026-01-01T00:00:00.000Z", 
 "numericId": 1, 
 "primaryTerm": 1, 
 "scores": { 
 "ANY_ADDITIONAL_PROPERTY": { 
 "content": "text", 
 "contentFormat": "text", 
 "context": { 
 "ANY_ADDITIONAL_PROPERTY": {} 
 }, 
 "isTypedIndicator": true, 
 "reliability": "text", 
 "score": 1, 
 "scoreChangeTimestamp": "2026-01-01T00:00:00.000Z", 
 "timestamp": "2026-01-01T00:00:00.000Z", 
 "type": "text" 
 } 
 }, 
 "sequenceNumber": 1, 
 "sizeInBytes": 1, 
 "sortValues": [ 
 "text" 
 ], 
 "syncHash": "text", 
 "version": 1 
 }, 
 "investigationIDs": [ 
 "text" 
 ], 
 "isDetectable": true, 
 "isPreventable": true, 
 "isShared": true, 
 "lastReputationRun": "2026-01-01T00:00:00.000Z", 
 "lastSeen": "2026-01-01T00:00:00.000Z", 
 "lastSeenEntryID": "text", 
 "manualExpirationTime": "2026-01-01T00:00:00.000Z", 
 "manualScore": true, 
 "manualSetTime": "2026-01-01T00:00:00.000Z", 
 "manuallyEditedFields": [ 
 "text" 
 ], 
 "modified": "2026-01-01T00:00:00.000Z", 
 "modifiedTime": "2026-01-01T00:00:00.000Z", 
 "moduleToFeedMap": { 
 "ANY_ADDITIONAL_PROPERTY": { 
 "ExpirationSource": { 
 "brand": "text", 
 "expirationInterval": 1, 
 "expirationPolicy": "text", 
 "instance": "text", 
 "moduleId": "text", 
 "setTime": "2026-01-01T00:00:00.000Z", 
 "source": "text", 
 "user": "text" 
 }, 
 "bypassExclusionList": true, 
 "classifierId": "text", 
 "classifierVersion": 1, 
 "comments": [ 
 { 
 "content": "text", 
 "created": "2026-01-01T00:00:00.000Z", 
 "id": "text", 
 "user": "text" 
 } 
 ], 
 "expirationInterval": 1, 
 "expirationPolicy": "text", 
 "fetchTime": "2026-01-01T00:00:00.000Z", 
 "fields": { 
 "ANY_ADDITIONAL_PROPERTY": {} 
 }, 
 "isEnrichment": true, 
 "mapperId": "text", 
 "mapperVersion": 1, 
 "modifiedTime": "2026-01-01T00:00:00.000Z", 
 "moduleId": "text", 
 "rawJSON": { 
 "ANY_ADDITIONAL_PROPERTY": {} 
 }, 
 "relationships": [ 
 { 
 "brand": "text", 
 "entityA": "text", 
 "entityAFamily": "text", 
 "entityAType": "text", 
 "entityB": "text", 
 "entityBFamily": "text", 
 "entityBType": "text", 
 "fields": { 
 "ANY_ADDITIONAL_PROPERTY": {} 
 }, 
 "id": "text", 
 "instance": "text", 
 "name": "text", 
 "reliability": "text", 
 "reverseName": "text", 
 "startTime": "2026-01-01T00:00:00.000Z", 
 "type": "text" 
 } 
 ], 
 "reliability": "text", 
 "score": 1, 
 "sourceBrand": "text", 
 "sourceInstance": "text", 
 "timestamp": "2026-01-01T00:00:00.000Z", 
 "type": "text", 
 "value": "text" 
 } 
 }, 
 "numericId": 1, 
 "primaryTerm": 1, 
 "relatedIncCount": 1, 
 "score": 1, 
 "sequenceNumber": 1, 
 "setBy": "text", 
 "sizeInBytes": 1, 
 "sortValues": [ 
 "text" 
 ], 
 "source": "text", 
 "sourceBrands": [ 
 "text" 
 ], 
 "sourceInstances": [ 
 "text" 
 ], 
 "syncHash": "text", 
 "timestamp": "2026-01-01T00:00:00.000Z", 
 "value": "text", 
 "version": 1 
 } 

 application/json 

 200 

 IocObject 

 Ask Copy 

 { 
 "CustomFields": { 
 "ANY_ADDITIONAL_PROPERTY": {} 
 }, 
 "account": "text", 
 "aggregatedReliability": "text", 
 "cacheVersn": 1, 
 "calculatedTime": "2026-01-01T00:00:00.000Z", 
 "comment": "text", 
 "comments": [ 
 { 
 "cacheVersn": 1, 
 "category": "text", 
 "content": "text", 
 "created": "2026-01-01T00:00:00.000Z", 
 "entryId": "text", 
 "highlight": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "id": "text", 
 "indexName": "text", 
 "modified": "2026-01-01T00:00:00.000Z", 
 "numericId": 1, 
 "primaryTerm": 1, 
 "sequenceNumber": 1, 
 "sizeInBytes": 1, 
 "sortValues": [ 
 "text" 
 ], 
 "source": "text", 
 "syncHash": "text", 
 "type": "text", 
 "user": "text", 
 "version": 1 
 } 
 ], 
 "created": "2026-01-01T00:00:00.000Z", 
 "deletedFeedFetchTime": "2026-01-01T00:00:00.000Z", 
 "expiration": "2026-01-01T00:00:00.000Z", 
 "expirationSource": { 
 "brand": "text", 
 "expirationInterval": 1, 
 "expirationPolicy": "text", 
 "instance": "text", 
 "moduleId": "text", 
 "setTime": "2026-01-01T00:00:00.000Z", 
 "source": "text", 
 "user": "text" 
 }, 
 "expirationStatus": "text", 
 "firstSeen": "2026-01-01T00:00:00.000Z", 
 "firstSeenEntryID": "text", 
 "highlight": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "id": "text", 
 "indexName": "text", 
 "indicator_type": "text", 
 "insightCache": { 
 "cacheVersn": 1, 
 "created": "2026-01-01T00:00:00.000Z", 
 "highlight": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "id": "text", 
 "indexName": "text", 
 "modified": "2026-01-01T00:00:00.000Z", 
 "numericId": 1, 
 "primaryTerm": 1, 
 "scores": { 
 "ANY_ADDITIONAL_PROPERTY": { 
 "content": "text", 
 "contentFormat": "text", 
 "context": { 
 "ANY_ADDITIONAL_PROPERTY": {} 
 }, 
 "isTypedIndicator": true, 
 "reliability": "text", 
 "score": 1, 
 "scoreChangeTimestamp": "2026-01-01T00:00:00.000Z", 
 "timestamp": "2026-01-01T00:00:00.000Z", 
 "type": "text" 
 } 
 }, 
 "sequenceNumber": 1, 
 "sizeInBytes": 1, 
 "sortValues": [ 
 "text" 
 ], 
 "syncHash": "text", 
 "version": 1 
 }, 
 "investigationIDs": [ 
 "text" 
 ], 
 "isDetectable": true, 
 "isPreventable": true, 
 "isShared": true, 
 "lastReputationRun": "2026-01-01T00:00:00.000Z", 
 "lastSeen": "2026-01-01T00:00:00.000Z", 
 "lastSeenEntryID": "text", 
 "manualExpirationTime": "2026-01-01T00:00:00.000Z", 
 "manualScore": true, 
 "manualSetTime": "2026-01-01T00:00:00.000Z", 
 "manuallyEditedFields": [ 
 "text" 
 ], 
 "modified": "2026-01-01T00:00:00.000Z", 
 "modifiedTime": "2026-01-01T00:00:00.000Z", 
 "moduleToFeedMap": { 
 "ANY_ADDITIONAL_PROPERTY": { 
 "ExpirationSource": { 
 "brand": "text", 
 "expirationInterval": 1, 
 "expirationPolicy": "text", 
 "instance": "text", 
 "moduleId": "text", 
 "setTime": "2026-01-01T00:00:00.000Z", 
 "source": "text", 
 "user": "text" 
 }, 
 "bypassExclusionList": true, 
 "classifierId": "text", 
 "classifierVersion": 1, 
 "comments": [ 
 { 
 "content": "text", 
 "created": "2026-01-01T00:00:00.000Z", 
 "id": "text", 
 "user": "text" 
 } 
 ], 
 "expirationInterval": 1, 
 "expirationPolicy": "text", 
 "fetchTime": "2026-01-01T00:00:00.000Z", 
 "fields": { 
 "ANY_ADDITIONAL_PROPERTY": {} 
 }, 
 "isEnrichment": true, 
 "mapperId": "text", 
 "mapperVersion": 1, 
 "modifiedTime": "2026-01-01T00:00:00.000Z", 
 "moduleId": "text", 
 "rawJSON": { 
 "ANY_ADDITIONAL_PROPERTY": {} 
 }, 
 "relationships": [ 
 { 
 "brand": "text", 
 "entityA": "text", 
 "entityAFamily": "text", 
 "entityAType": "text", 
 "entityB": "text", 
 "entityBFamily": "text", 
 "entityBType": "text", 
 "fields": { 
 "ANY_ADDITIONAL_PROPERTY": {} 
 }, 
 "id": "text", 
 "instance": "text", 
 "name": "text", 
 "reliability": "text", 
 "reverseName": "text", 
 "startTime": "2026-01-01T00:00:00.000Z", 
 "type": "text" 
 } 
 ], 
 "reliability": "text", 
 "score": 1, 
 "sourceBrand": "text", 
 "sourceInstance": "text", 
 "timestamp": "2026-01-01T00:00:00.000Z", 
 "type": "text", 
 "value": "text" 
 } 
 }, 
 "numericId": 1, 
 "primaryTerm": 1, 
 "relatedIncCount": 1, 
 "score": 1, 
 "sequenceNumber": 1, 
 "setBy": "text", 
 "sizeInBytes": 1, 
 "sortValues": [ 
 "text" 
 ], 
 "source": "text", 
 "sourceBrands": [ 
 "text" 
 ], 
 "sourceInstances": [ 
 "text" 
 ], 
 "syncHash": "text", 
 "timestamp": "2026-01-01T00:00:00.000Z", 
 "value": "text", 
 "version": 1 
 } 

 Whitelists or deletes Indicator 

 post https://hostname /indicator/whitelist 

 Whitelists or deletes an indicator entity In order to delete an indicator and not whitelist, set doNotWhitelist boolean field to true 

 Authorizations 

 api_key 

 Authorization string Required 

 Body 

 application/json 

 InvestigationId string Optional 

 doNotWhitelist boolean Optional 

 entryId string Optional 

 manualScore boolean Optional 

 reason string Optional 

 reputation integer · int64 Optional 

 reputations string[] Optional 

 value string Optional 

 Responses 

 200 

 UpdateResponse 

 application/json 

 notUpdated integer · int64 Optional 

 updatedIds string[] Optional 

 uppdated integer · int64 Optional 

 post /indicator/whitelist 

 HTTP 

 Ask Copy 

 POST /indicator/whitelist HTTP/1.1 
 Host: hostname 
 Authorization: YOUR_API_KEY 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 153 

 { 
 "InvestigationId": "text", 
 "doNotWhitelist": true, 
 "entryId": "text", 
 "manualScore": true, 
 "reason": "text", 
 "reputation": 1, 
 "reputations": [ 
 "text" 
 ], 
 "value": "text" 
 } 

 application/json 

 200 

 UpdateResponse 

 Ask Copy 

 { 
 "notUpdated": 1, 
 "updatedIds": [ 
 "text" 
 ], 
 "uppdated": 1 
 } 

 Batch export indicators to STIX 

 post https://hostname /indicators/batch/export/stix 

 Exports an indicators batch to STIX file (returns file ID) 

 Authorizations 

 api_key 

 Authorization string Required 

 Body 

 application/json 

 all boolean Optional 

 columns string[] Optional 

 doNotWhitelist boolean Optional 

 filter object · IndicatorFilter Optional 

 IndicatorFilter is a general filter that fetches entities using a query string query using the Query value 

 Show properties 

 ids string[] Optional 

 reason string Optional 

 reputations string[] Optional 

 Responses 

 200 

 STIX file name 

 application/json 

 string Optional 

 post /indicators/batch/export/stix 

 HTTP 

 Ask Copy 

 POST /indicators/batch/export/stix HTTP/1.1 
 Host: hostname 
 Authorization: YOUR_API_KEY 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 1434 

 { 
 "all": true, 
 "columns": [ 
 "text" 
 ], 
 "doNotWhitelist": true, 
 "filter": { 
 "Cache": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "accounts": { 
 "ANY_ADDITIONAL_PROPERTY": {} 
 }, 
 "earlyTimeInPage": "2026-01-01T00:00:00.000Z", 
 "fields": [ 
 "text" 
 ], 
 "filterobjectquery": "text", 
 "firstSeen": { 
 "fromDate": "2026-01-01T00:00:00.000Z", 
 "fromDateLicense": "2026-01-01T00:00:00.000Z", 
 "period": { 
 "by": "text", 
 "byFrom": "text", 
 "byTo": "text", 
 "field": "text", 
 "fromValue": "text", 
 "toValue": "text" 
 }, 
 "timeFrame": 1, 
 "toDate": "2026-01-01T00:00:00.000Z" 
 }, 
 "fromDate": "2026-01-01T00:00:00.000Z", 
 "fromDateLicense": "2026-01-01T00:00:00.000Z", 
 "ignoreWorkers": true, 
 "lastSeen": { 
 "fromDate": "2026-01-01T00:00:00.000Z", 
 "fromDateLicense": "2026-01-01T00:00:00.000Z", 
 "period": { 
 "by": "text", 
 "byFrom": "text", 
 "byTo": "text", 
 "field": "text", 
 "fromValue": "text", 
 "toValue": "text" 
 }, 
 "timeFrame": 1, 
 "toDate": "2026-01-01T00:00:00.000Z" 
 }, 
 "laterTimeInPage": "2026-01-01T00:00:00.000Z", 
 "page": 1, 
 "period": { 
 "by": "text", 
 "byFrom": "text", 
 "byTo": "text", 
 "field": "text", 
 "fromValue": "text", 
 "toValue": "text" 
 }, 
 "prevPage": true, 
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
 "timeFrame": 1, 
 "toDate": "2026-01-01T00:00:00.000Z", 
 "trim_events": 1 
 }, 
 "ids": [ 
 "text" 
 ], 
 "reason": "text", 
 "reputations": [ 
 "text" 
 ] 
 } 

 application/json 

 200 

 STIX file name 

 Ask Copy 

 text 

 Batch export indicators to csv 

 post https://hostname /indicators/batch/exportToCsv 

 Exports an indicators batch to CSV file (returns file ID) 

 Authorizations 

 api_key 

 Authorization string Required 

 Body 

 application/json 

 all boolean Optional 

 columns string[] Optional 

 doNotWhitelist boolean Optional 

 filter object · IndicatorFilter Optional 

 IndicatorFilter is a general filter that fetches entities using a query string query using the Query value 

 Show properties 

 ids string[] Optional 

 reason string Optional 

 reputations string[] Optional 

 Responses 

 200 

 csv file name 

 application/json 

 string Optional 

 post /indicators/batch/exportToCsv 

 HTTP 

 Ask Copy 

 POST /indicators/batch/exportToCsv HTTP/1.1 
 Host: hostname 
 Authorization: YOUR_API_KEY 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 1434 

 { 
 "all": true, 
 "columns": [ 
 "text" 
 ], 
 "doNotWhitelist": true, 
 "filter": { 
 "Cache": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "accounts": { 
 "ANY_ADDITIONAL_PROPERTY": {} 
 }, 
 "earlyTimeInPage": "2026-01-01T00:00:00.000Z", 
 "fields": [ 
 "text" 
 ], 
 "filterobjectquery": "text", 
 "firstSeen": { 
 "fromDate": "2026-01-01T00:00:00.000Z", 
 "fromDateLicense": "2026-01-01T00:00:00.000Z", 
 "period": { 
 "by": "text", 
 "byFrom": "text", 
 "byTo": "text", 
 "field": "text", 
 "fromValue": "text", 
 "toValue": "text" 
 }, 
 "timeFrame": 1, 
 "toDate": "2026-01-01T00:00:00.000Z" 
 }, 
 "fromDate": "2026-01-01T00:00:00.000Z", 
 "fromDateLicense": "2026-01-01T00:00:00.000Z", 
 "ignoreWorkers": true, 
 "lastSeen": { 
 "fromDate": "2026-01-01T00:00:00.000Z", 
 "fromDateLicense": "2026-01-01T00:00:00.000Z", 
 "period": { 
 "by": "text", 
 "byFrom": "text", 
 "byTo": "text", 
 "field": "text", 
 "fromValue": "text", 
 "toValue": "text" 
 }, 
 "timeFrame": 1, 
 "toDate": "2026-01-01T00:00:00.000Z" 
 }, 
 "laterTimeInPage": "2026-01-01T00:00:00.000Z", 
 "page": 1, 
 "period": { 
 "by": "text", 
 "byFrom": "text", 
 "byTo": "text", 
 "field": "text", 
 "fromValue": "text", 
 "toValue": "text" 
 }, 
 "prevPage": true, 
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
 "timeFrame": 1, 
 "toDate": "2026-01-01T00:00:00.000Z", 
 "trim_events": 1 
 }, 
 "ids": [ 
 "text" 
 ], 
 "reason": "text", 
 "reputations": [ 
 "text" 
 ] 
 } 

 application/json 

 200 

 csv file name 

 Ask Copy 

 text 

 Batch whitelist or delete indicators 

 post https://hostname /indicators/batchDelete 

 Batch whitelist or delete indicators entities In order to delete indicators and not whitelist, set doNotWhitelist boolean field to true 

 Authorizations 

 api_key 

 Authorization string Required 

 Body 

 application/json 

 all boolean Optional 

 columns string[] Optional 

 doNotWhitelist boolean Optional 

 filter object · IndicatorFilter Optional 

 IndicatorFilter is a general filter that fetches entities using a query string query using the Query value 

 Show properties 

 ids string[] Optional 

 reason string Optional 

 reputations string[] Optional 

 Responses 

 200 

 UpdateResponse 

 application/json 

 notUpdated integer · int64 Optional 

 updatedIds string[] Optional 

 uppdated integer · int64 Optional 

 post /indicators/batchDelete 

 HTTP 

 Ask Copy 

 POST /indicators/batchDelete HTTP/1.1 
 Host: hostname 
 Authorization: YOUR_API_KEY 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 1434 

 { 
 "all": true, 
 "columns": [ 
 "text" 
 ], 
 "doNotWhitelist": true, 
 "filter": { 
 "Cache": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "accounts": { 
 "ANY_ADDITIONAL_PROPERTY": {} 
 }, 
 "earlyTimeInPage": "2026-01-01T00:00:00.000Z", 
 "fields": [ 
 "text" 
 ], 
 "filterobjectquery": "text", 
 "firstSeen": { 
 "fromDate": "2026-01-01T00:00:00.000Z", 
 "fromDateLicense": "2026-01-01T00:00:00.000Z", 
 "period": { 
 "by": "text", 
 "byFrom": "text", 
 "byTo": "text", 
 "field": "text", 
 "fromValue": "text", 
 "toValue": "text" 
 }, 
 "timeFrame": 1, 
 "toDate": "2026-01-01T00:00:00.000Z" 
 }, 
 "fromDate": "2026-01-01T00:00:00.000Z", 
 "fromDateLicense": "2026-01-01T00:00:00.000Z", 
 "ignoreWorkers": true, 
 "lastSeen": { 
 "fromDate": "2026-01-01T00:00:00.000Z", 
 "fromDateLicense": "2026-01-01T00:00:00.000Z", 
 "period": { 
 "by": "text", 
 "byFrom": "text", 
 "byTo": "text", 
 "field": "text", 
 "fromValue": "text", 
 "toValue": "text" 
 }, 
 "timeFrame": 1, 
 "toDate": "2026-01-01T00:00:00.000Z" 
 }, 
 "laterTimeInPage": "2026-01-01T00:00:00.000Z", 
 "page": 1, 
 "period": { 
 "by": "text", 
 "byFrom": "text", 
 "byTo": "text", 
 "field": "text", 
 "fromValue": "text", 
 "toValue": "text" 
 }, 
 "prevPage": true, 
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
 "timeFrame": 1, 
 "toDate": "2026-01-01T00:00:00.000Z", 
 "trim_events": 1 
 }, 
 "ids": [ 
 "text" 
 ], 
 "reason": "text", 
 "reputations": [ 
 "text" 
 ] 
 } 

 application/json 

 200 

 UpdateResponse 

 Ask Copy 

 { 
 "notUpdated": 1, 
 "updatedIds": [ 
 "text" 
 ], 
 "uppdated": 1 
 } 

 Get indicators as CSV 

 get https://hostname /indicators/csv/ {id} 

 Get an indicators CSV file that was exported, by ID 

 Authorizations 

 api_key 

 Authorization string Required 

 Path parameters 

 id string Required 

 CSV file to fetch (returned from batch export to csv call) 

 Responses 

 200 

 Return Csv file 

 No content 

 get /indicators/csv/ {id} 

 HTTP 

 Ask Copy 

 GET /indicators/csv/{id} HTTP/1.1 
 Host: hostname 
 Authorization: YOUR_API_KEY 
 Accept: */* 

 200 

 Return Csv file 

 No content 

 Create feed indicators from JSON 

 post https://hostname /indicators/feed/json 

 Create indicators from raw JSON (similar to ingesting from a feed). Builds indicators according to the specified feed classifier, or uses the default one if not specified. Indicator properties (all optional except for value): value (string, required) | type (string) | score (number, 0-3, default 0 , where 0 means None, 1 Good, 2 Suspicious, and 3 Bad) | sourceBrand (string, default "External" ) | sourceInstance (string, default "External" ) | reliability (string, one of "A - Completely reliable" , "B - Usually reliable" , "C - Fairly reliable" , "D - Not usually reliable" , "E - Unreliable" , "F - Reliability cannot be judged" ) | expirationPolicy (string, one of "never" , "interval" , "indicatorType" ) | expirationInterval (number, in minutes) 

 Authorizations 

 api_key 

 Authorization string Required 

 Body 

 application/json 

 FeedIndicatorsRequest is the input for JSON feed indicator ingestion 

 bypassExclusionList boolean Optional 

 classifierId string Optional 

 indicators object · RawFeedIndicator[] Optional 

 RawFeedIndicator is an unparsed feed indicator from JSON ingestion 

 Show properties 

 mapperId string Optional 

 Responses 

 201 

 Indicators created 

 No content 

 post /indicators/feed/json 

 HTTP 

 Ask Copy 

 POST /indicators/feed/json HTTP/1.1 
 Host: hostname 
 Authorization: YOUR_API_KEY 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 114 

 { 
 "bypassExclusionList": true, 
 "classifierId": "text", 
 "indicators": [ 
 { 
 "ANY_ADDITIONAL_PROPERTY": {} 
 } 
 ], 
 "mapperId": "text" 
 } 

 application/json 

 201 

 Indicators created 

 No content 

 Search indicators 

 post https://hostname /indicators/search 

 Search indicators by filter 

 Authorizations 

 api_key 

 Authorization string Required 

 Body 

 application/json 

 IndicatorFilter is a general filter that fetches entities using a query string query using the Query value 

 Cache object Optional 

 Cache of join functions 

 Show properties 

 accounts object Optional 

 Show properties 

 earlyTimeInPage string · date-time Optional 

 fields string[] Optional 

 filterobjectquery string Optional 

 firstSeen object · DateRangeFilter Optional 

 DateRangeFilter provides common fields for date filtering 

 Show properties 

 fromDate string · date-time Optional 

 fromDateLicense string · date-time Optional 

 ignoreWorkers boolean Optional 

 Do not use workers mechanism while searching bleve 

 lastSeen object · DateRangeFilter Optional 

 DateRangeFilter provides common fields for date filtering 

 Show properties 

 laterTimeInPage string · date-time Optional 

 page integer · int64 Optional 

 0-based page 

 period object · Period holds the 'Period' query, such as last 3 days, last 6 hours, between 6 days from now until 3 days from now. Optional 

 Show properties 

 prevPage boolean Optional 

 MT support - these fields are for indicator search according to calculatedTime 

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

 timeFrame integer · int64 Optional 

 A Duration represents the elapsed time between two instants
as an int64 nanosecond count. The representation limits the
largest representable duration to approximately 290 years. 

 toDate string · date-time Optional 

 trim_events integer · int64 Optional 

 Responses 

 200 

 indicatorResult 

 application/json 

 accountErrors string[] Optional 

 iocObjects object · IocObject[] Optional 

 IocObject - represents an Ioc (or simply an indicator) object 

 Show properties 

 total integer · int64 Optional 

 totalAccounts integer · int64 Optional 

 post /indicators/search 

 HTTP 

 Ask Copy 

 POST /indicators/search HTTP/1.1 
 Host: hostname 
 Authorization: YOUR_API_KEY 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 1317 

 { 
 "Cache": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "accounts": { 
 "ANY_ADDITIONAL_PROPERTY": {} 
 }, 
 "earlyTimeInPage": "2026-01-01T00:00:00.000Z", 
 "fields": [ 
 "text" 
 ], 
 "filterobjectquery": "text", 
 "firstSeen": { 
 "fromDate": "2026-01-01T00:00:00.000Z", 
 "fromDateLicense": "2026-01-01T00:00:00.000Z", 
 "period": { 
 "by": "text", 
 "byFrom": "text", 
 "byTo": "text", 
 "field": "text", 
 "fromValue": "text", 
 "toValue": "text" 
 }, 
 "timeFrame": 1, 
 "toDate": "2026-01-01T00:00:00.000Z" 
 }, 
 "fromDate": "2026-01-01T00:00:00.000Z", 
 "fromDateLicense": "2026-01-01T00:00:00.000Z", 
 "ignoreWorkers": true, 
 "lastSeen": { 
 "fromDate": "2026-01-01T00:00:00.000Z", 
 "fromDateLicense": "2026-01-01T00:00:00.000Z", 
 "period": { 
 "by": "text", 
 "byFrom": "text", 
 "byTo": "text", 
 "field": "text", 
 "fromValue": "text", 
 "toValue": "text" 
 }, 
 "timeFrame": 1, 
 "toDate": "2026-01-01T00:00:00.000Z" 
 }, 
 "laterTimeInPage": "2026-01-01T00:00:00.000Z", 
 "page": 1, 
 "period": { 
 "by": "text", 
 "byFrom": "text", 
 "byTo": "text", 
 "field": "text", 
 "fromValue": "text", 
 "toValue": "text" 
 }, 
 "prevPage": true, 
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
 "timeFrame": 1, 
 "toDate": "2026-01-01T00:00:00.000Z", 
 "trim_events": 1 
 } 

 application/json 

 200 

 indicatorResult 

 Ask Copy 

 { 
 "accountErrors": [ 
 "text" 
 ], 
 "iocObjects": [ 
 { 
 "CustomFields": { 
 "ANY_ADDITIONAL_PROPERTY": {} 
 }, 
 "account": "text", 
 "aggregatedReliability": "text", 
 "cacheVersn": 1, 
 "calculatedTime": "2026-01-01T00:00:00.000Z", 
 "comment": "text", 
 "comments": [ 
 { 
 "cacheVersn": 1, 
 "category": "text", 
 "content": "text", 
 "created": "2026-01-01T00:00:00.000Z", 
 "entryId": "text", 
 "highlight": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "id": "text", 
 "indexName": "text", 
 "modified": "2026-01-01T00:00:00.000Z", 
 "numericId": 1, 
 "primaryTerm": 1, 
 "sequenceNumber": 1, 
 "sizeInBytes": 1, 
 "sortValues": [ 
 "text" 
 ], 
 "source": "text", 
 "syncHash": "text", 
 "type": "text", 
 "user": "text", 
 "version": 1 
 } 
 ], 
 "created": "2026-01-01T00:00:00.000Z", 
 "deletedFeedFetchTime": "2026-01-01T00:00:00.000Z", 
 "expiration": "2026-01-01T00:00:00.000Z", 
 "expirationSource": { 
 "brand": "text", 
 "expirationInterval": 1, 
 "expirationPolicy": "text", 
 "instance": "text", 
 "moduleId": "text", 
 "setTime": "2026-01-01T00:00:00.000Z", 
 "source": "text", 
 "user": "text" 
 }, 
 "expirationStatus": "text", 
 "firstSeen": "2026-01-01T00:00:00.000Z", 
 "firstSeenEntryID": "text", 
 "highlight": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "id": "text", 
 "indexName": "text", 
 "indicator_type": "text", 
 "insightCache": { 
 "cacheVersn": 1, 
 "created": "2026-01-01T00:00:00.000Z", 
 "highlight": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "id": "text", 
 "indexName": "text", 
 "modified": "2026-01-01T00:00:00.000Z", 
 "numericId": 1, 
 "primaryTerm": 1, 
 "scores": { 
 "ANY_ADDITIONAL_PROPERTY": { 
 "content": "text", 
 "contentFormat": "text", 
 "context": { 
 "ANY_ADDITIONAL_PROPERTY": {} 
 }, 
 "isTypedIndicator": true, 
 "reliability": "text", 
 "score": 1, 
 "scoreChangeTimestamp": "2026-01-01T00:00:00.000Z", 
 "timestamp": "2026-01-01T00:00:00.000Z", 
 "type": "text" 
 } 
 }, 
 "sequenceNumber": 1, 
 "sizeInBytes": 1, 
 "sortValues": [ 
 "text" 
 ], 
 "syncHash": "text", 
 "version": 1 
 }, 
 "investigationIDs": [ 
 "text" 
 ], 
 "isDetectable": true, 
 "isPreventable": true, 
 "isShared": true, 
 "lastReputationRun": "2026-01-01T00:00:00.000Z", 
 "lastSeen": "2026-01-01T00:00:00.000Z", 
 "lastSeenEntryID": "text", 
 "manualExpirationTime": "2026-01-01T00:00:00.000Z", 
 "manualScore": true, 
 "manualSetTime": "2026-01-01T00:00:00.000Z", 
 "manuallyEditedFields": [ 
 "text" 
 ], 
 "modified": "2026-01-01T00:00:00.000Z", 
 "modifiedTime": "2026-01-01T00:00:00.000Z", 
 "moduleToFeedMap": { 
 "ANY_ADDITIONAL_PROPERTY": { 
 "ExpirationSource": { 
 "brand": "text", 
 "expirationInterval": 1, 
 "expirationPolicy": "text", 
 "instance": "text", 
 "moduleId": "text", 
 "setTime": "2026-01-01T00:00:00.000Z", 
 "source": "text", 
 "user": "text" 
 }, 
 "bypassExclusionList": true, 
 "classifierId": "text", 
 "classifierVersion": 1, 
 "comments": [ 
 { 
 "content": "text", 
 "created": "2026-01-01T00:00:00.000Z", 
 "id": "text", 
 "user": "text" 
 } 
 ], 
 "expirationInterval": 1, 
 "expirationPolicy": "text", 
 "fetchTime": "2026-01-01T00:00:00.000Z", 
 "fields": { 
 "ANY_ADDITIONAL_PROPERTY": {} 
 }, 
 "isEnrichment": true, 
 "mapperId": "text", 
 "mapperVersion": 1, 
 "modifiedTime": "2026-01-01T00:00:00.000Z", 
 "moduleId": "text", 
 "rawJSON": { 
 "ANY_ADDITIONAL_PROPERTY": {} 
 }, 
 "relationships": [ 
 { 
 "brand": "text", 
 "entityA": "text", 
 "entityAFamily": "text", 
 "entityAType": "text", 
 "entityB": "text", 
 "entityBFamily": "text", 
 "entityBType": "text", 
 "fields": { 
 "ANY_ADDITIONAL_PROPERTY": {} 
 }, 
 "id": "text", 
 "instance": "text", 
 "name": "text", 
 "reliability": "text", 
 "reverseName": "text", 
 "startTime": "2026-01-01T00:00:00.000Z", 
 "type": "text" 
 } 
 ], 
 "reliability": "text", 
 "score": 1, 
 "sourceBrand": "text", 
 "sourceInstance": "text", 
 "timestamp": "2026-01-01T00:00:00.000Z", 
 "type": "text", 
 "value": "text" 
 } 
 }, 
 "numericId": 1, 
 "primaryTerm": 1, 
 "relatedIncCount": 1, 
 "score": 1, 
 "sequenceNumber": 1, 
 "setBy": "text", 
 "sizeInBytes": 1, 
 "sortValues": [ 
 "text" 
 ], 
 "source": "text", 
 "sourceBrands": [ 
 "text" 
 ], 
 "sourceInstances": [ 
 "text" 
 ], 
 "syncHash": "text", 
 "timestamp": "2026-01-01T00:00:00.000Z", 
 "value": "text", 
 "version": 1 
 } 
 ], 
 "total": 1, 
 "totalAccounts": 1 
 } 

 Get indicators as STIX V2 

 get https://hostname /indicators/stix/v2/ {id} 

 Get an indicators STIX V2 file that was exported, by ID 

 Authorizations 

 api_key 

 Authorization string Required 

 Path parameters 

 id string Required 

 STIX V2 file to fetch (returned from batch export to STIX call) 

 Responses 

 200 

 Return STIX V2 file 

 No content 

 get /indicators/stix/v2/ {id} 

 HTTP 

 Ask Copy 

 GET /indicators/stix/v2/{id} HTTP/1.1 
 Host: hostname 
 Authorization: YOUR_API_KEY 
 Accept: */* 

 200 

 Return STIX V2 file 

 No content 

 Delete indicators timeline 

 post https://hostname /indicators/timeline/delete 

 Delete indicators timeline by filter 

 Authorizations 

 api_key 

 Authorization string Required 

 Body 

 application/json 

 IndicatorFilter is a general filter that fetches entities using a query string query using the Query value 

 Cache object Optional 

 Cache of join functions 

 Show properties 

 accounts object Optional 

 Show properties 

 earlyTimeInPage string · date-time Optional 

 fields string[] Optional 

 filterobjectquery string Optional 

 firstSeen object · DateRangeFilter Optional 

 DateRangeFilter provides common fields for date filtering 

 Show properties 

 fromDate string · date-time Optional 

 fromDateLicense string · date-time Optional 

 ignoreWorkers boolean Optional 

 Do not use workers mechanism while searching bleve 

 lastSeen object · DateRangeFilter Optional 

 DateRangeFilter provides common fields for date filtering 

 Show properties 

 laterTimeInPage string · date-time Optional 

 page integer · int64 Optional 

 0-based page 

 period object · Period holds the 'Period' query, such as last 3 days, last 6 hours, between 6 days from now until 3 days from now. Optional 

 Show properties 

 prevPage boolean Optional 

 MT support - these fields are for indicator search according to calculatedTime 

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

 timeFrame integer · int64 Optional 

 A Duration represents the elapsed time between two instants
as an int64 nanosecond count. The representation limits the
largest representable duration to approximately 290 years. 

 toDate string · date-time Optional 

 trim_events integer · int64 Optional 

 Responses 

 200 

 IndicatorEditBulkResponse 

 application/json 

 total integer · uint64 Optional 

 updated integer · uint64 Optional 

 post /indicators/timeline/delete 

 HTTP 

 Ask Copy 

 POST /indicators/timeline/delete HTTP/1.1 
 Host: hostname 
 Authorization: YOUR_API_KEY 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 1317 

 { 
 "Cache": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "accounts": { 
 "ANY_ADDITIONAL_PROPERTY": {} 
 }, 
 "earlyTimeInPage": "2026-01-01T00:00:00.000Z", 
 "fields": [ 
 "text" 
 ], 
 "filterobjectquery": "text", 
 "firstSeen": { 
 "fromDate": "2026-01-01T00:00:00.000Z", 
 "fromDateLicense": "2026-01-01T00:00:00.000Z", 
 "period": { 
 "by": "text", 
 "byFrom": "text", 
 "byTo": "text", 
 "field": "text", 
 "fromValue": "text", 
 "toValue": "text" 
 }, 
 "timeFrame": 1, 
 "toDate": "2026-01-01T00:00:00.000Z" 
 }, 
 "fromDate": "2026-01-01T00:00:00.000Z", 
 "fromDateLicense": "2026-01-01T00:00:00.000Z", 
 "ignoreWorkers": true, 
 "lastSeen": { 
 "fromDate": "2026-01-01T00:00:00.000Z", 
 "fromDateLicense": "2026-01-01T00:00:00.000Z", 
 "period": { 
 "by": "text", 
 "byFrom": "text", 
 "byTo": "text", 
 "field": "text", 
 "fromValue": "text", 
 "toValue": "text" 
 }, 
 "timeFrame": 1, 
 "toDate": "2026-01-01T00:00:00.000Z" 
 }, 
 "laterTimeInPage": "2026-01-01T00:00:00.000Z", 
 "page": 1, 
 "period": { 
 "by": "text", 
 "byFrom": "text", 
 "byTo": "text", 
 "field": "text", 
 "fromValue": "text", 
 "toValue": "text" 
 }, 
 "prevPage": true, 
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
 "timeFrame": 1, 
 "toDate": "2026-01-01T00:00:00.000Z", 
 "trim_events": 1 
 } 

 application/json 

 200 

 IndicatorEditBulkResponse 

 Ask Copy 

 { 
 "total": 1, 
 "updated": 1 
 } 

 Create indicators 

 post https://hostname /indicators/upload 

 Create indicators from a file 

 Authorizations 

 api_key 

 Authorization string Required 

 Body 

 multipart/form-data 

 fileName string Optional 

 file name 

 file string Optional 

 file 

 Responses 

 200 

 IocObjects 

 application/json 

 IocObject - represents an Ioc (or simply an indicator) object 

 CustomFields object · CustomFields ... Optional 

 The keys should be the field's display name all lower and without spaces. For example: Scan IP -> scanip
To get the actual key name you can also go to Cortex XSOAR CLI and run /incident_add and look for the key that you would like to update 

 Show properties 

 account string Optional 

 aggregatedReliability string Optional 

 cacheVersn integer · int64 Optional 

 calculatedTime string · date-time Optional 

 Do not set the fields bellow this line 

 comment string Optional 

 comments object · Comment ...[] Optional 

 Show properties 

 created string · date-time Optional 

 deletedFeedFetchTime string · date-time Optional 

 expiration string · date-time Optional 

 expirationSource object · ExpirationSource .. . Optional 

 Show properties 

 expirationStatus string Optional 

 firstSeen string · date-time Optional 

 firstSeenEntryID string Optional 

 highlight object Optional 

 Show properties 

 id string Optional 

 indexName string Optional 

 indicator_type string Optional 

 insightCache object · InsightCache Optional 

 InsightCache - map insight name to all its metadata, name will be case insensitive 

 Show properties 

 investigationIDs string[] Optional 

 isDetectable boolean Optional 

 isPreventable boolean Optional 

 isShared boolean Optional 

 lastReputationRun string · date-time Optional 

 lastSeen string · date-time Optional 

 lastSeenEntryID string Optional 

 manualExpirationTime string · date-time Optional 

 manualScore boolean Optional 

 manualSetTime string · date-time Optional 

 manuallyEditedFields string[] Optional 

 modified string · date-time Optional 

 modifiedTime string · date-time Optional 

 moduleToFeedMap object Optional 

 Show properties 

 numericId integer · int64 Optional 

 primaryTerm integer · int64 Optional 

 relatedIncCount integer · int64 Optional 

 score integer · int64 Optional 

 sequenceNumber integer · int64 Optional 

 setBy string Optional 

 sizeInBytes integer · int64 Optional 

 sortValues string[] Optional 

 source string Optional 

 sourceBrands string[] Optional 

 sourceInstances string[] Optional 

 syncHash string Optional 

 timestamp string · date-time Optional 

 value string Optional 

 version integer · int64 Optional 

 post /indicators/upload 

 HTTP 

 Ask Copy 

 POST /indicators/upload HTTP/1.1 
 Host: hostname 
 Authorization: YOUR_API_KEY 
 Content-Type: multipart/form-data 
 Accept: */* 
 Content-Length: 33 

 { 
 "fileName": "text", 
 "file": "text" 
 } 

 200 

 IocObjects 

 Ask Copy 

 [ 
 { 
 "CustomFields": { 
 "ANY_ADDITIONAL_PROPERTY": {} 
 }, 
 "account": "text", 
 "aggregatedReliability": "text", 
 "cacheVersn": 1, 
 "calculatedTime": "2026-01-01T00:00:00.000Z", 
 "comment": "text", 
 "comments": [ 
 { 
 "cacheVersn": 1, 
 "category": "text", 
 "content": "text", 
 "created": "2026-01-01T00:00:00.000Z", 
 "entryId": "text", 
 "highlight": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "id": "text", 
 "indexName": "text", 
 "modified": "2026-01-01T00:00:00.000Z", 
 "numericId": 1, 
 "primaryTerm": 1, 
 "sequenceNumber": 1, 
 "sizeInBytes": 1, 
 "sortValues": [ 
 "text" 
 ], 
 "source": "text", 
 "syncHash": "text", 
 "type": "text", 
 "user": "text", 
 "version": 1 
 } 
 ], 
 "created": "2026-01-01T00:00:00.000Z", 
 "deletedFeedFetchTime": "2026-01-01T00:00:00.000Z", 
 "expiration": "2026-01-01T00:00:00.000Z", 
 "expirationSource": { 
 "brand": "text", 
 "expirationInterval": 1, 
 "expirationPolicy": "text", 
 "instance": "text", 
 "moduleId": "text", 
 "setTime": "2026-01-01T00:00:00.000Z", 
 "source": "text", 
 "user": "text" 
 }, 
 "expirationStatus": "text", 
 "firstSeen": "2026-01-01T00:00:00.000Z", 
 "firstSeenEntryID": "text", 
 "highlight": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "id": "text", 
 "indexName": "text", 
 "indicator_type": "text", 
 "insightCache": { 
 "cacheVersn": 1, 
 "created": "2026-01-01T00:00:00.000Z", 
 "highlight": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "id": "text", 
 "indexName": "text", 
 "modified": "2026-01-01T00:00:00.000Z", 
 "numericId": 1, 
 "primaryTerm": 1, 
 "scores": { 
 "ANY_ADDITIONAL_PROPERTY": { 
 "content": "text", 
 "contentFormat": "text", 
 "context": { 
 "ANY_ADDITIONAL_PROPERTY": {} 
 }, 
 "isTypedIndicator": true, 
 "reliability": "text", 
 "score": 1, 
 "scoreChangeTimestamp": "2026-01-01T00:00:00.000Z", 
 "timestamp": "2026-01-01T00:00:00.000Z", 
 "type": "text" 
 } 
 }, 
 "sequenceNumber": 1, 
 "sizeInBytes": 1, 
 "sortValues": [ 
 "text" 
 ], 
 "syncHash": "text", 
 "version": 1 
 }, 
 "investigationIDs": [ 
 "text" 
 ], 
 "isDetectable": true, 
 "isPreventable": true, 
 "isShared": true, 
 "lastReputationRun": "2026-01-01T00:00:00.000Z", 
 "lastSeen": "2026-01-01T00:00:00.000Z", 
 "lastSeenEntryID": "text", 
 "manualExpirationTime": "2026-01-01T00:00:00.000Z", 
 "manualScore": true, 
 "manualSetTime": "2026-01-01T00:00:00.000Z", 
 "manuallyEditedFields": [ 
 "text" 
 ], 
 "modified": "2026-01-01T00:00:00.000Z", 
 "modifiedTime": "2026-01-01T00:00:00.000Z", 
 "moduleToFeedMap": { 
 "ANY_ADDITIONAL_PROPERTY": { 
 "ExpirationSource": { 
 "brand": "text", 
 "expirationInterval": 1, 
 "expirationPolicy": "text", 
 "instance": "text", 
 "moduleId": "text", 
 "setTime": "2026-01-01T00:00:00.000Z", 
 "source": "text", 
 "user": "text" 
 }, 
 "bypassExclusionList": true, 
 "classifierId": "text", 
 "classifierVersion": 1, 
 "comments": [ 
 { 
 "content": "text", 
 "created": "2026-01-01T00:00:00.000Z", 
 "id": "text", 
 "user": "text" 
 } 
 ], 
 "expirationInterval": 1, 
 "expirationPolicy": "text", 
 "fetchTime": "2026-01-01T00:00:00.000Z", 
 "fields": { 
 "ANY_ADDITIONAL_PROPERTY": {} 
 }, 
 "isEnrichment": true, 
 "mapperId": "text", 
 "mapperVersion": 1, 
 "modifiedTime": "2026-01-01T00:00:00.000Z", 
 "moduleId": "text", 
 "rawJSON": { 
 "ANY_ADDITIONAL_PROPERTY": {} 
 }, 
 "relationships": [ 
 { 
 "brand": "text", 
 "entityA": "text", 
 "entityAFamily": "text", 
 "entityAType": "text", 
 "entityB": "text", 
 "entityBFamily": "text", 
 "entityBType": "text", 
 "fields": { 
 "ANY_ADDITIONAL_PROPERTY": {} 
 }, 
 "id": "text", 
 "instance": "text", 
 "name": "text", 
 "reliability": "text", 
 "reverseName": "text", 
 "startTime": "2026-01-01T00:00:00.000Z", 
 "type": "text" 
 } 
 ], 
 "reliability": "text", 
 "score": 1, 
 "sourceBrand": "text", 
 "sourceInstance": "text", 
 "timestamp": "2026-01-01T00:00:00.000Z", 
 "type": "text", 
 "value": "text" 
 } 
 }, 
 "numericId": 1, 
 "primaryTerm": 1, 
 "relatedIncCount": 1, 
 "score": 1, 
 "sequenceNumber": 1, 
 "setBy": "text", 
 "sizeInBytes": 1, 
 "sortValues": [ 
 "text" 
 ], 
 "source": "text", 
 "sourceBrands": [ 
 "text" 
 ], 
 "sourceInstances": [ 
 "text" 
 ], 
 "syncHash": "text", 
 "timestamp": "2026-01-01T00:00:00.000Z", 
 "value": "text", 
 "version": 1 
 } 
 ] 

 Create whitelisted 

 post https://hostname /indicators/whitelist/update 

 Create or update excluded indicators list 

 Authorizations 

 api_key 

 Authorization string Required 

 Body 

 application/json 

 WhitelistedIndicator Excluded indicator 

 cacheVersn integer · int64 Optional 

 created string · date-time Optional 

 highlight object Optional 

 Show properties 

 id string Optional 

 indexName string Optional 

 locked boolean Optional 

 modified string · date-time Optional 

 numericId integer · int64 Optional 

 primaryTerm integer · int64 Optional 

 reason string Optional 

 reputations string[] Optional 

 sequenceNumber integer · int64 Optional 

 sizeInBytes integer · int64 Optional 

 sortValues string[] Optional 

 syncHash string Optional 

 type string Optional 

 user string Optional 

 value string Optional 

 version integer · int64 Optional 

 whitelistTime string · date-time Optional 

 Responses 

 200 

 WhitelistedIndicator 

 application/json 

 WhitelistedIndicator Excluded indicator 

 cacheVersn integer · int64 Optional 

 created string · date-time Optional 

 highlight object Optional 

 Show properties 

 id string Optional 

 indexName string Optional 

 locked boolean Optional 

 modified string · date-time Optional 

 numericId integer · int64 Optional 

 primaryTerm integer · int64 Optional 

 reason string Optional 

 reputations string[] Optional 

 sequenceNumber integer · int64 Optional 

 sizeInBytes integer · int64 Optional 

 sortValues string[] Optional 

 syncHash string Optional 

 type string Optional 

 user string Optional 

 value string Optional 

 version integer · int64 Optional 

 whitelistTime string · date-time Optional 

 post /indicators/whitelist/update 

 HTTP 

 Ask Copy 

 POST /indicators/whitelist/update HTTP/1.1 
 Host: hostname 
 Authorization: YOUR_API_KEY 
 Content-Type: application/json 
 Accept: */* 
 Content-Length: 427 

 { 
 "cacheVersn": 1, 
 "created": "2026-01-01T00:00:00.000Z", 
 "highlight": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "id": "text", 
 "indexName": "text", 
 "locked": true, 
 "modified": "2026-01-01T00:00:00.000Z", 
 "numericId": 1, 
 "primaryTerm": 1, 
 "reason": "text", 
 "reputations": [ 
 "text" 
 ], 
 "sequenceNumber": 1, 
 "sizeInBytes": 1, 
 "sortValues": [ 
 "text" 
 ], 
 "syncHash": "text", 
 "type": "text", 
 "user": "text", 
 "value": "text", 
 "version": 1, 
 "whitelistTime": "2026-01-01T00:00:00.000Z" 
 } 

 application/json 

 200 

 WhitelistedIndicator 

 Ask Copy 

 { 
 "cacheVersn": 1, 
 "created": "2026-01-01T00:00:00.000Z", 
 "highlight": { 
 "ANY_ADDITIONAL_PROPERTY": [ 
 "text" 
 ] 
 }, 
 "id": "text", 
 "indexName": "text", 
 "locked": true, 
 "modified": "2026-01-01T00:00:00.000Z", 
 "numericId": 1, 
 "primaryTerm": 1, 
 "reason": "text", 
 "reputations": [ 
 "text" 
 ], 
 "sequenceNumber": 1, 
 "sizeInBytes": 1, 
 "sortValues": [ 
 "text" 
 ], 
 "syncHash": "text", 
 "type": "text", 
 "user": "text", 
 "value": "text", 
 "version": 1, 
 "whitelistTime": "2026-01-01T00:00:00.000Z" 
 } 

 Previous Incidents 

 Next Integrations 

 Last updated 1 month ago 

 Was this helpful?
