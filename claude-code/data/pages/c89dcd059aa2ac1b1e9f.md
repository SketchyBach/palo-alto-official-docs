---
url: https://cortex-docs.paloaltonetworks.com/xsiam-data-model-schema/fields/event
fetched_at: 2026-09-06T10:56:46Z
source: cortex-platform
---

# xdm.event | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Schemas 

 XSIAM Data Model Schema 

 XDM Fields 

 xdm.event 

 An event that occurred 

 Fields 

 xdm.event.id 

 Description 

 The event ID within the original source. 

 Datatype 

 String 

 Dataclass 

 Scalar 

 xdm.event.type 

 Description 

 The event type. 

 Datatype 

 String 

 Dataclass 

 Scalar 

 Examples 

 NETWORK, PROCESS, AUDIT, HOST 

 xdm.event.original_event_type 

 Description 

 The original event type. 

 Datatype 

 String 

 Dataclass 

 Scalar 

 xdm.event.operation 

 Description 

 The operation type. 

 Datatype 

 XDM_CONST.OPERATION_TYPE 

 Dataclass 

 Scalar 

 Examples 

 XDM_CONST.OPERATION_TYPE_DIR_CREATE, XDM_CONST.OPERATION_TYPE_FILE_WRITE, XDM_CONST.OPERATION_TYPE_IMAGE_LOAD, XDM_CONST.OPERATION_TYPE_PROCESS_TERMINATE, XDM_CONST.OPERATION_TYPE_PROCESS_CREATE 

 xdm.event.operation_sub_type 

 Description 

 The operation sub-type. 

 Datatype 

 String 

 Dataclass 

 Scalar 

 Examples 

 INJECTION, TUNNEL, NTLM 

 xdm.event.description 

 Description 

 The event's message or description. 

 Datatype 

 String 

 Dataclass 

 Scalar 

 xdm.event.tags 

 Description 

 List of tags that are related to the activity. 

 Datatype 

 XDM_CONST.EVENT_TAG 

 Dataclass 

 Array 

 Examples 

 XDM_CONST.EVENT_TAG_AUTHENTICATION, XDM_CONST.EVENT_TAG_NETWORK, XDM_CONST.EVENT_TAG_CLOUD, XDM_CONST.EVENT_TAG_SAAS, XDM_CONST.EVENT_TAG_ONPREM 

 xdm.event.outcome 

 Description 

 The result of this activity. 

 Datatype 

 XDM_CONST.OUTCOME 

 Dataclass 

 Scalar 

 Examples 

 XDM_CONST.OUTCOME_SUCCESS, XDM_CONST.OUTCOME_FAILED, XDM_CONST.OUTCOME_PARTIAL, XDM_CONST.OUTCOME_UNKNOWN 

 xdm.event.outcome_reason 

 Description 

 The reason for the outcome. 

 Datatype 

 String 

 Dataclass 

 Scalar 

 xdm.event.duration 

 Description 

 The amount of time, in milliseconds, for the completion of the action. 

 Datatype 

 Number 

 Dataclass 

 Scalar 

 Unit 

 Milliseconds 

 xdm.event.is_completed 

 Description 

 Whether the action was completed or is ongoing. 

 Datatype 

 Boolean 

 Dataclass 

 Scalar 

 xdm.event.log_level 

 Description 

 The importance level of the event. 

 Datatype 

 XDM_CONST.LOG_LEVEL 

 Dataclass 

 Scalar 

 Examples 

 XDM_CONST.LOG_LEVEL_CRITICAL, XDM_CONST.LOG_LEVEL_ERROR, XDM_CONST.LOG_LEVEL_WARNING, XDM_CONST.LOG_LEVEL_DEBUG 

 xdm.event.format 

 Description 

 The log format in which the data was sent. 

 Datatype 

 String 

 Dataclass 

 Scalar 

 Examples 

 RFC-5424, RFC-3164, CEF 

 Previous xdm.session_context_id 

 Next xdm.source 

 Last updated 1 month ago 

 Was this helpful?
