---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-agent/8.7/cortex-xdr-agent-for-macos/manage-the-agent-deployment-notifications-for-mac
fetched_at: 2026-09-06T10:20:23Z
source: cortex-platform
---

# Manage the Agent Deployment Notifications for Mac | 8.7 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR Agent 

 Cortex XDR Agent Documentation 

 8.7 

 Cortex XDR Agent for MacOS 

 Cortex XDR agent 8.7 

 Manage the Agent Deployment Notifications for Mac 

 An overview of user notifications for the Cortex XDR agent during installation, upgrade, and removal on a Mac. 

 When you install, upgrade, or remove the Cortex XDR agent from your Mac endpoint, both the operating system and the Cortex XDR agent prompt specific notifications the end user has to approve. The operating system notifications are in line with Apple’s security improvements starting with macOS 10.15.4, which include the deprecation of kernel extensions by third-party providers. As a result, the Cortex XDR agent 7.1 and later releases no longer use the kernel extension. Instead, the agent is designed to deploy two System Extensions. 

 Since the 7.1 release, the Cortex XDR agent deploys the Endpoint Security extension to monitor system events, and starting in the 7.2.1 agent release, a new Network extension was added to monitor network events. Together, these two System extensions provide full coverage of the endpoint traffic and replace the deprecated kernel extension. To suppress the extension notifications for the Cortex XDR agent installation process, refer to Install the Cortex XDR Agent Using JAMF . For a one-click installation using a MDM of your choice, refer to Install with a Unified Configuration Profile for MDMs . 

 The following tables describe the extension and notification approval workflow the end user is required to perform on a Mac endpoint during agent installation, upgrade, and removal processes. 

 Installing a Cortex XDR Agent 

 The following table describes the extension approval workflow the end user is required to perform on the endpoint during agent installation, when performed manually or using an MDM. 

 macOS 10.15.3 and earlier 

 macOS 10.15.4 and later 

 Install a Cortex XDR agent 

 Kernel extension — Requires user approval. Can be suppressed in your MDM profile. 

 Endpoint Security extension —Requires user approval. Can be suppressed in your MDM profile. 

 Network extension —Requires user approval. Can be suppressed in your MDM profile. 

 Network content filter —Requires user approval. Can be suppressed in your MDM profile. You can also suppress this operating system prompt by uploading a configuration file provided by Palo Alto Networks. 

 Upgrading to a Cortex XDR Agent 

 The following table describes the extension approval workflow the end user is required to perform on the endpoint during agent upgrade, when performed manually or using an MDM. 

 macOS 10.15.3 and earlier 

 macOS 10.15.4 and later 

 Upgrade a Cortex XDR agent 

 Kernel extension —If already allowed during initial agent installation, nothing to allow during upgrade. Otherwise, allow once. Can be suppressed in your MDM profile. 

 Endpoint Security extension —If already allowed during initial agent installation, nothing to allow during upgrade. Otherwise, allow once. Can be suppressed in your MDM profile. 

 Network extension —If you are upgrading from a Cortex XDR agent release prior to 7.2.1 where this extension did not exist, requires user approval. Can be suppressed in your MDM profile. Otherwise, if you are upgrading from a 7.2.1 agent or later and approval was already provided, nothing to allow during upgrade. 

 Network content filter —If you are upgrading from a Cortex XDR agent release prior to 7.2.1 where this addition did not exist, requires user approval. If you are using an MDM to deploy the agents in your networks, you can suppress this operating system prompt by uploading a configuration file provided by Palo Alto Networks. Otherwise, if you are upgrading from a 7.2.1 agent or later and approval was already provided, nothing to allow during upgrade. 

 Removing a Cortex XDR Agent 

 The following table describes the approval workflow the end user is required to perform on the endpoint during agent removal, when performed manually or using an MDM. 

 macOS 10.15.3 and earlier 

 macOS 10.15.4 and later 

 Remove a Cortex XDR agent 7.6 and later 

 User approval and password are required. Can be suppressed in your MDM profile. 

 User approval and password are required by Apple for each System extension. In the current operating system release, you cannot suppress this option in your MDM profile, and will be required to approve twice. 

 Previous Uninstall the Cortex XDR Agent for Mac 

 Next Troubleshooting Resources for Mac 

 Last updated 5 days ago 

 Was this helpful?
