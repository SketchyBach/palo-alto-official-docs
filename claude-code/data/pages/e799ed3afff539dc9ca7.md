---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-agent/9.3/cortex-xdr-agent-for-macos/use-the-cortex-xdr-agent-for-mac
fetched_at: 2026-09-16T08:51:30Z
source: cortex-platform
---

# Use the Cortex XDR Agent for Mac | 9.3 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR Agent 

 Cortex XDR Agent Documentation 

 9.3 

 Cortex XDR Agent for MacOS 

 Cortex XDR agent 9.3 

 Use the Cortex XDR Agent for Mac 

 Learn how to effectively use the Cortex XDR agent for Mac by the different options described in this topic. 

 Open the Cortex XDR Agent application. 

 Use one of the following methods: 

 Browse to the Traps folder in Finder. 

 If you enabled access to the agent console, select the Cortex XDR agent icon in the menu bar, and select Open Console . 

 View status information about the Cortex XDR agent: 

 Version —Displays the agent version. 

 Protection —Displays the active policies in bold. 

 Note 

 On Mac endpoints running macOS 10.15.4, the Protection Status in the agent console indicates the status of both Malware and Exploit modules on the endpoint. 

 Connection —Displays the connection status and, if connected, includes the server to which the agent is connected. 

 Last Check-in —Displays the local time on the endpoint of the last check-in with the server. 

 Manually connect to the server. 

 The Cortex XDR agent communicates with the server at a fixed 5-minute heartbeat interval to send status information and retrieve the latest security policy. The agent performs this operation transparently at regular intervals so it is not typically necessary to connect to the server manually. If your Connection status is Not Connected , you can manually retry your connection. This option is available if you do not want to wait for the automated communication interval to begin. 

 To initiate a manual check-in with the server: On the home page of the Cortex XDR agent console, select Check In Now . If the agent successfully establishes a connection with the server, the Connection status changes to indicated the service to which the agent is connected. 

 Collect Cortex XDR agent logs in a file that can be sent to a support representative for analysis. 

 Select Generate Support File . Cortex XDR agent aggregates the logs into a compressed file. Save it, and then send the file to your support representative. For remote endpoints, you can also retrieve logs from the Action Center. 

 View recent security events that occurred on your endpoint. 

 For each event, the agent console displays the local Time an event occurred, the name of the Process that exhibited malicious behavior, the Module that triggered the event, and the mode specified for the type of event (Termination or Notification). 

 View protected processes on the Mac endpoint. 

 The Protection tab of the agent console displays all running processes in which the Cortex XDR agent is injected to prevent malicious execution or behavior. The agent console also indicates the process ID (PID) associated with each process. 

 Configure proxy communication. 

 The agent can communicate with Cortex XDR using the system proxy server that you define for the endpoint. For information on How to Enter Proxy Settings , see the documentation for your Mac operating system version. If you prefer to use an application proxy, configure a Cortex XDR agent specific proxy . 

 Persistent notification from agent that your machine can’t access the network. Only when the issue is resolved, the notification does not appear. 

 Previous Configure Cortex XDR Agent for Mac 

 Next Uninstall the Cortex XDR Agent for Mac 

 Last updated 1 day ago 

 Was this helpful?
