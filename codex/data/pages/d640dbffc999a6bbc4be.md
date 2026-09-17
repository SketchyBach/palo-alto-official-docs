---
url: https://cortex-docs.paloaltonetworks.com/xsiam-data-model-schema/consts/registry-value-type
fetched_at: 2026-09-16T09:04:13Z
source: cortex-platform
---

# XDM_CONST.REGISTRY_VALUE_TYPE | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Schemas 

 XSIAM Data Model Schema 

 XDM Consts 

 XDM_CONST.REGISTRY_VALUE_TYPE 

 Registry value type. See https://docs.microsoft.com/en-us/windows/win32/sysinfo/registry-value-types. 

 Original 

 Mapped 

 Description 

 REG_BINARY 

 XDM_CONST.REGISTRY_VALUE_TYPE_REG_BINARY 

 Binary data in any form. 

 REG_DWORD 

 XDM_CONST.REGISTRY_VALUE_TYPE_REG_DWORD 

 A 32-bit number. 

 REG_DWORD_LITTLE_ENDIAN 

 XDM_CONST.REGISTRY_VALUE_TYPE_REG_DWORD_LITTLE_ENDIAN 

 A 32-bit number in little-endian format. Windows is designed to run on little-endian computer architectures. Therefore, this value is defined as REG_DWORD in the Windows header files. 

 REG_DWORD_BIG_ENDIAN 

 XDM_CONST.REGISTRY_VALUE_TYPE_REG_DWORD_BIG_ENDIAN 

 A 32-bit number in big-endian format. Some UNIX systems support big-endian architectures. 

 REG_EXPAND_SZ 

 XDM_CONST.REGISTRY_VALUE_TYPE_REG_EXPAND_SZ 

 A null-terminated string that contains unexpanded references to environment variables (for example, "%PATH%"). It will be a Unicode or ANSI string depending on whether you use the Unicode or ANSI functions. To expand the environment variable references, use the ExpandEnvironmentStrings function. 

 REG_LINK 

 XDM_CONST.REGISTRY_VALUE_TYPE_REG_LINK 

 A null-terminated Unicode string that contains the target path of a symbolic link that was created by calling the RegCreateKeyEx function with REG_OPTION_CREATE_LINK. 

 REG_MULTI_SZ 

 XDM_CONST.REGISTRY_VALUE_TYPE_REG_MULTI_SZ 

 A sequence of null-terminated strings, terminated by an empty string (\0). The following is an example: String1\0String2\0String3\0LastString\0\0 The first \0 terminates the first string, the second to the last \0 terminates the last string, and the final \0 terminates the sequence. Note that the final terminator must be factored into the length of the string. 

 REG_NONE 

 XDM_CONST.REGISTRY_VALUE_TYPE_REG_NONE 

 No defined value type. 

 REG_QWORD 

 XDM_CONST.REGISTRY_VALUE_TYPE_REG_QWORD 

 A 64-bit number. 

 REG_QWORD_LITTLE_ENDIAN 

 XDM_CONST.REGISTRY_VALUE_TYPE_REG_QWORD_LITTLE_ENDIAN 

 A 64-bit number in little-endian format. Windows is designed to run on little-endian computer architectures. Therefore, this value is defined as REG_QWORD in the Windows header files. 

 REG_SZ 

 XDM_CONST.REGISTRY_VALUE_TYPE_REG_SZ 

 A null-terminated string. This will be either a Unicode or an ANSI string, depending on whether you use the Unicode or ANSI functions. 

 Previous XDM_CONST.HOST_STATE_TYPE 

 Next XDM_CONST.IMAGE_VISIBILITY 

 Last updated 2 months ago 

 Was this helpful?
