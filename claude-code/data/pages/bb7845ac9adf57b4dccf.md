---
url: https://cortex-docs.paloaltonetworks.com/8.x/8.3-eol/cortex-xdr-agent-8.3-release-information/changes-to-default-behavior-in-cortex-xdr-agent-8.3
fetched_at: 2026-09-16T09:13:38Z
source: cortex-platform
---

# Changes to Default Behavior in Cortex XDR Agent 8.3 | 8.3 (EoL) | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Release Notes 

 Cortex XDR Agent 

 Cortex XDR Agent 8.x 

 8.3 (EoL) 

 Cortex XDR Agent 8.3 Release Information 

 Changes to Default Behavior in Cortex XDR Agent 8.3 

 Changes to default behavior in Cortex XDR agent 8.3 for Windows, macOS, and Linux endpoints. 

 This section details behavior changes that you may encounter when using a new version of the Cortex XDR agent. For further details, refer to the admin guide for your product. 

 Certificate enforcement for Windows and macOS endpoints 

 To improve security, the Cortex XDR agent 8.3 is now ensuring the use of a provided certificate without using the local fallback store (trusted root CA file). In order to graduate the adoption of this requirement, Disabled (Notify) is default for existing tenants; new tenants will have the Enabled configuration by default. 

 There are three modes of operation, set in the Agent Settings profile: 

 Enabled: Enforcement is enabled. Note, If the agent is initially unable to communicate without the local store, enforcement is not enabled and the agent will show as partially protected in the server UI. 

 Disabled (Notify): Enforcement is disabled. Agents with this policy will trigger a visible banner in the UI to notify customers about potential risk and direct them to change the certificate and the setting. 

 Disabled: Enforcement is disabled. Agents with this policy will trigger a visible banner in the UI to notify customers about potential risk. With this mode, the Last Certificate Enforcement Fallback column in the Endpoints table is not updated, and there are no management audit logs related to the local store fallback. 

 Linux packages validation key 

 New Public key for validating Linux installation packages. For the download link, see the Install the Cortex XDR Agent for Linux section of the Cortex XDR agent admin guide. 

 Previous Features introduced in Cortex XDR agent 8.3 

 Next Addressed Issues in Cortex XDR Agent 8.3 

 Last updated 1 month ago 

 Was this helpful?
