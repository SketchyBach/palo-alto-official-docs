---
url: https://cortex-docs.paloaltonetworks.com/xsiam-data-model-schema/fields/target/file
fetched_at: 2026-09-06T10:57:08Z
source: cortex-platform
---

# xdm.target.file | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Schemas 

 XSIAM Data Model Schema 

 XDM Fields 

 xdm.target 

 xdm.target.file 

 The file that has been created, modified, or deleted. 

 Datatype 

 Compound.File 

 Dataclass 

 Compound 

 Field groups 

 xdm.target.file.permissions 

 xdm.target.file.position 

 Fields 

 xdm.target.file.filename 

 Description 

 The file name of the file that has been created, modified, or deleted. 

 Datatype 

 String 

 Dataclass 

 Scalar 

 xdm.target.file.path 

 Description 

 The file path of the file that has been created, modified, or deleted. 

 Datatype 

 String 

 Dataclass 

 Scalar 

 xdm.target.file.directory 

 Description 

 The file directory of the file that has been created, modified, or deleted. 

 Datatype 

 String 

 Dataclass 

 Scalar 

 xdm.target.file.extension 

 Description 

 The file extension of the file that has been created, modified, or deleted. 

 Datatype 

 String 

 Dataclass 

 Scalar 

 xdm.target.file.file_type 

 Description 

 The file type of the file that has been created, modified, or deleted. 

 Datatype 

 String 

 Dataclass 

 Scalar 

 xdm.target.file.md5 

 Description 

 The MD5 hash signature for the file that has been created, modified, or deleted content. 

 Datatype 

 MD5 

 Dataclass 

 Scalar 

 xdm.target.file.sha256 

 Description 

 The SHA256 hash signature for the file that has been created, modified, or deleted content. 

 Datatype 

 SHA256 

 Dataclass 

 Scalar 

 xdm.target.file.is_signed 

 Description 

 Whether the loaded module of the file that has been created, modified, or deleted is signed. 

 Datatype 

 Boolean 

 Dataclass 

 Scalar 

 Examples 

 True 

 xdm.target.file.signer 

 Description 

 The signer of the file that has been created, modified, or deleted. 

 Datatype 

 String 

 Dataclass 

 Scalar 

 Examples 

 Microsoft Corporation 

 xdm.target.file.signature_status 

 Description 

 The signature status of the file that has been created, modified, or deleted. 

 Datatype 

 XDM_CONST.SIGNATURE_STATUS 

 Dataclass 

 Scalar 

 Examples 

 XDM_CONST.SIGNATURE_STATUS_UNSIGNED, XDM_CONST.SIGNATURE_STATUS_SIGNED_INVALID, XDM_CONST.SIGNATURE_STATUS_SIGNED_VERIFIED, XDM_CONST.SIGNATURE_STATUS_STATUS_UNKNOWN 

 xdm.target.file.size 

 Description 

 Size in bytes of the file that has been created, modified, or deleted. 

 Datatype 

 Number 

 Dataclass 

 Scalar 

 Unit 

 Bytes 

 xdm.target.file.last_modified 

 Description 

 The last modified time (millisecs) of the file that has been created, modified, or deleted. 

 Datatype 

 UnixMillis 

 Dataclass 

 Scalar 

 Examples 

 1716549375886 

 xdm.target.file.metadata_change_time 

 Description 

 The metadata last modification time (millisecs) of the file that has been created, modified, or deleted. 

 Datatype 

 UnixMillis 

 Dataclass 

 Scalar 

 Examples 

 1716549375886 

 xdm.target.file.owner_id 

 Description 

 The owner id of the file that has been created, modified, or deleted. 

 Datatype 

 Number 

 Dataclass 

 Scalar 

 Examples 

 123456789 

 xdm.target.file.owner_name 

 Description 

 The owner name of the file that has been created, modified, or deleted. 

 Datatype 

 String 

 Dataclass 

 Scalar 

 Examples 

 admin 

 xdm.target.file.group_id 

 Description 

 The group id of the file that has been created, modified, or deleted. 

 Datatype 

 Number 

 Dataclass 

 Scalar 

 Examples 

 123456789 

 xdm.target.file.group_name 

 Description 

 The group name of the file that has been created, modified, or deleted. 

 Datatype 

 String 

 Dataclass 

 Scalar 

 Examples 

 all 

 xdm.target.file.volume_path 

 Description 

 The path identifies the file's precise location in the volume. 

 Datatype 

 String 

 Dataclass 

 Scalar 

 Examples 

 /etc/shadow/sec.txt 

 xdm.target.file.contributors 

 Description 

 Git contributors and their last commit time of the file that has been created, modified, or deleted. 

 Datatype 

 Json 

 Dataclass 

 Array 

 Examples 

 ['{"name": "gmark", "last_commit_time": 1699110852}'] 

 Previous xdm.target.registry_before 

 Next xdm.target.file.permissions 

 Last updated 1 month ago 

 Was this helpful?
