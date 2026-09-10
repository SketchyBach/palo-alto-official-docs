---
url: https://cortex-docs.paloaltonetworks.com/xsiam-data-model-schema/fields/intermediate/process
fetched_at: 2026-09-06T10:56:57Z
source: cortex-platform
---

# xdm.intermediate.process | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Schemas 

 XSIAM Data Model Schema 

 XDM Fields 

 xdm.intermediate 

 xdm.intermediate.process 

 The intermediate process. 

 Datatype 

 Compound.Process 

 Dataclass 

 Compound 

 Field groups 

 xdm.intermediate.process.executable 

 Fields 

 xdm.intermediate.process.name 

 Description 

 The name of the intermediate process. 

 Datatype 

 String 

 Dataclass 

 Scalar 

 xdm.intermediate.process.pid 

 Description 

 The ID of the intermediate process, provided by the operating system. 

 Datatype 

 Number 

 Dataclass 

 Scalar 

 xdm.intermediate.process.identifier 

 Description 

 The unique ID of the intermediate process, provided by the agent. 

 Datatype 

 String 

 Dataclass 

 Scalar 

 xdm.intermediate.process.command_line 

 Description 

 The command line that the intermediate process is executing. 

 Datatype 

 String 

 Dataclass 

 Scalar 

 xdm.intermediate.process.causality_id 

 Description 

 The ID of the root process that triggered the chain that the intermediate process is a part of. 

 Datatype 

 String 

 Dataclass 

 Scalar 

 xdm.intermediate.process.parent_id 

 Description 

 The ID of the direct parent process that triggered the intermediate process. 

 Datatype 

 String 

 Dataclass 

 Scalar 

 xdm.intermediate.process.integrity_level 

 Description 

 The mode of operation level in which the intermediate process is running. 

 Datatype 

 Number 

 Dataclass 

 Scalar 

 xdm.intermediate.process.thread_id 

 Description 

 The thread ID of the intermediate process. 

 Datatype 

 Number 

 Dataclass 

 Scalar 

 xdm.intermediate.process.is_injected 

 Description 

 Whether the intermediate process's thread/activity is executed via process injection. 

 Datatype 

 Boolean 

 Dataclass 

 Scalar 

 xdm.intermediate.process.container_id 

 Description 

 ID of the container that is running the intermediate process. 

 Datatype 

 String 

 Dataclass 

 Scalar 

 Previous xdm.intermediate.user.key_management 

 Next xdm.intermediate.process.executable 

 Last updated 1 month ago 

 Was this helpful?
