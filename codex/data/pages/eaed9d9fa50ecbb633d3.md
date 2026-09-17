---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-agent/5.0/traps-agent-5.0-for-mac/install-the-traps-agent-for-mac
fetched_at: 2026-09-16T08:51:42Z
source: cortex-platform
---

# Install the Traps Agent for Mac | 5.0 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR Agent 

 Cortex XDR Agent Documentation 

 5.0 

 Traps Agent 5.0 for Mac 

 Install the Traps Agent for Mac 

 Perform steps to install the traps agent for Mac. 

 Before installing Traps on a Mac endpoint, verify that the system meets the requirements described in Traps for Mac Requirements . 

 Install Traps using a software distribution tool of your choice (such as JAMF) or using the following workflow: 

 Download the installation package you want to install from the Traps management service. 

 Copy the installation package to the endpoint on which you want to install the Traps software. 

 Unzip the installation package. 

 Configure a Traps specific proxy on the endpoint (Requires Traps agent 5.0.9 supported by Cortex XDR only) . 

 If you are deploying Traps in an environment where Traps agents communicate with the Cortex XDR server through a proxy, you must assign the proxy IP address and port number during the Traps agent installation on the endpoint. 

 Locate the Config.xml file in the unzipped installation folder. 

 Edit the <proxy_list> <proxyserver>:<port> </proxy_list> tag. 

 To install a Traps agent with a Traps specific proxy, enter your proxy IP address and port number. You can assign up to five different proxies per agent, and the proxy for communication is selected randomly with equal probability. 

 <proxy_list>10.196.20.244:8080,10.196.20.245:8080</proxy_list> 

 To install a Traps agent communicating through the Palo Alto Networks Broker Service, you must enter the broker VM IP address and port number 8888 only. 

 After the initial installation, you can change the proxy settings in Traps management service → Endpoints . 

 Install the Traps software. 

 Unzip the installation package and run the Traps.pkg installation file. 

 Click Continue to proceed with the installation. 

 If prompted to confirm the destination, click Continue . 

 Click Install to begin the installation. 

 Enter the User Name and Password of the administrator with access to install software on the endpoint, and then click Install Software . 

 Allow Traps to install system extensions: 

 Dismiss the System Extension Blocked warning. 

 Go to System Preferences → Security & Privacy → General and select Allow . 

 Traps logs any installation errors to /var/logs/installation.log . If installation fails for any reason, you can view this log to better understand the cause of the installation failure. 

 After the installation completes, verify your connection. 

 To open the Traps console, click the Traps icon in the menu bar, and select Open Console . 

 Click Check In Now to initiate a connection with your tenant of the Traps management service. If successful, the Last Check-In field updates to display the recent check-in date and time. 

 Note 

 If the Traps agent cannot register with the Traps management service, the agent does not retry registration. To retry, reinstall the Traps agent on the endpoint. 

 Previous Traps for Mac Requirements 

 Next Use the Traps Agent for Mac 

 Last updated 2 months ago 

 Was this helpful?
