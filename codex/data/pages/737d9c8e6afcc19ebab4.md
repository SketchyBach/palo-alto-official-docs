---
url: https://docs.paloaltonetworks.com/autofocus/autofocus-admin/use-autofocus-miners-with-the-palo-alto-networks-firewall
fetched_at: 2026-08-13T15:25:06Z
source: palo-alto-main
---

# use-autofocus-miners-with-the-palo-alto-networks-firewall Clear

use-autofocus-miners-with-the-palo-alto-networks-firewall 

 Home 

 EN

 Location 

 Documentation Home 

 Palo Alto Networks 

 Support 

 Live Community 

 Knowledge Base 

 Strata Copilot

 AutoFocus™ Administrator’s Guide 

 : 
 Use AutoFocus Miners with the Palo Alto Networks Firewall 

 Updated on 

 Tue Jul 26 14:29:53 PDT 2022 

 Focus 

 Download PDF 

 Filter

 Expand all | Collapse all 

 Get Started With AutoFocus 

 About AutoFocus 

 Activate AutoFocus Licenses 

 First Look at the AutoFocus Portal 

 AutoFocus Concepts 

 Use AutoFocus with the Palo Alto Networks Firewall 

 AutoFocus Portal Settings 

 AutoFocus Dashboard 

 Dashboard Overview 

 Set the Dashboard Date Range 

 Drill Down on Dashboard Widgets 

 Customize the Dashboard 

 DNS Security Dashboard 

 DNS Security Dashboard Overview 

 DNS Security Dashboard Widgets 

 AutoFocus Search 

 Start a Quick Search 

 Work with the Search 

 Drill Down in Search Results 

 Sample 

 Sessions 

 Indicators 

 Set Up Remote Search 

 Artifact Types 

 General Artifacts 

 Sample Artifacts 

 Session Artifacts 

 Analysis Artifacts 

 Linux Artifacts 

 Windows Artifacts 

 Mac Artifacts 

 Android Artifacts 

 Search Operators and Values 

 Guidelines for Partial Searches 

 Contains and Does Not Contain Operators 

 Proximity Operator 

 AutoFocus Alerts 

 Alert Types 

 Email Alerts 

 HTTP/HTTPS Alerts 

 Supported TLS Ciphers 

 Create Alerts 

 Define Alert Actions 

 Enable Alerts by Tag Type 

 Create Alert Exceptions 

 View Alerts in AutoFocus 

 Edit Alerts 

 AutoFocus Tags 

 Tag Concepts 

 Tag Types 

 Tag Class 

 Tag Status 

 Tag Visibility 

 Tag Group 

 Tag Details 

 Create a Tag 

 Work with Tags 

 Find Samples by Tag Details 

 Filter and Sort Tags 

 Find the Top Tags Detected During a Date Range 

 Vote for, Comment on, and Report Tags 

 Assess AutoFocus Artifacts 

 Find High-Risk Artifacts 

 Add High-Risk Artifacts to a Search or Export List 

 Export AutoFocus Content 

 Export AutoFocus Artifacts 

 Build an AutoFocus Export List 

 Create a CSV File 

 Use Export Lists with the Palo Alto Networks Firewall 

 Export AutoFocus Page Content 

 Export AutoFocus Dashboard and Reports 

 AutoFocus Reports 

 Reports Overview 

 Customize Reports 

 Scheduled Reporting 

 Use the Threat Summary Report to Observe Malware Trends 

 Threat Summary Report Overview 

 View Threat Summary Report Details 

 AutoFocus Feeds 

 Feed Overview 

 Create Custom Feeds 

 Use AutoFocus Custom Feeds with the Palo Alto Networks Firewall 

 Manage Custom Feeds 

 AutoFocus-Hosted MineMeld 

 Updated on 

 Tue Jul 26 14:29:53 PDT 2022 

 Focus 

 Home 

 AutoFocus 

 AutoFocus™ Administrator’s Guide 

 Use AutoFocus Miners with the Palo Alto Networks Firewall 

 Download PDF 

 AutoFocus™ Administrator’s Guide 

 Use AutoFocus Miners with the Palo Alto Networks Firewall 

 Table of Contents 

 Filter

 Expand all | Collapse all 

 Get Started With AutoFocus 

 About AutoFocus 

 Activate AutoFocus Licenses 

 First Look at the AutoFocus Portal 

 AutoFocus Concepts 

 Use AutoFocus with the Palo Alto Networks Firewall 

 AutoFocus Portal Settings 

 AutoFocus Dashboard 

 Dashboard Overview 

 Set the Dashboard Date Range 

 Drill Down on Dashboard Widgets 

 Customize the Dashboard 

 DNS Security Dashboard 

 DNS Security Dashboard Overview 

 DNS Security Dashboard Widgets 

 AutoFocus Search 

 Start a Quick Search 

 Work with the Search 

 Drill Down in Search Results 

 Sample 

 Sessions 

 Indicators 

 Set Up Remote Search 

 Artifact Types 

 General Artifacts 

 Sample Artifacts 

 Session Artifacts 

 Analysis Artifacts 

 Linux Artifacts 

 Windows Artifacts 

 Mac Artifacts 

 Android Artifacts 

 Search Operators and Values 

 Guidelines for Partial Searches 

 Contains and Does Not Contain Operators 

 Proximity Operator 

 AutoFocus Alerts 

 Alert Types 

 Email Alerts 

 HTTP/HTTPS Alerts 

 Supported TLS Ciphers 

 Create Alerts 

 Define Alert Actions 

 Enable Alerts by Tag Type 

 Create Alert Exceptions 

 View Alerts in AutoFocus 

 Edit Alerts 

 AutoFocus Tags 

 Tag Concepts 

 Tag Types 

 Tag Class 

 Tag Status 

 Tag Visibility 

 Tag Group 

 Tag Details 

 Create a Tag 

 Work with Tags 

 Find Samples by Tag Details 

 Filter and Sort Tags 

 Find the Top Tags Detected During a Date Range 

 Vote for, Comment on, and Report Tags 

 Assess AutoFocus Artifacts 

 Find High-Risk Artifacts 

 Add High-Risk Artifacts to a Search or Export List 

 Export AutoFocus Content 

 Export AutoFocus Artifacts 

 Build an AutoFocus Export List 

 Create a CSV File 

 Use Export Lists with the Palo Alto Networks Firewall 

 Export AutoFocus Page Content 

 Export AutoFocus Dashboard and Reports 

 AutoFocus Reports 

 Reports Overview 

 Customize Reports 

 Scheduled Reporting 

 Use the Threat Summary Report to Observe Malware Trends 

 Threat Summary Report Overview 

 View Threat Summary Report Details 

 AutoFocus Feeds 

 Feed Overview 

 Create Custom Feeds 

 Use AutoFocus Custom Feeds with the Palo Alto Networks Firewall 

 Manage Custom Feeds 

 AutoFocus-Hosted MineMeld 

 Use AutoFocus Miners with the Palo Alto Networks Firewall 

 Use AutoFocus miners to dynamically send indicators
from AutoFocus to an external dynamic list on a PAN-OS 9.0
firewall. 

 Add the root certificate authority (CA) certificate
for MineMeld to the firewall. 
 Download the GoDaddy Class 2 Certification
Authority Root Certificate: https://certs.godaddy.com/repository/gd-class2-root.crt 

 On the firewall, select Device Certificate Management Certificates . 

 Import the certificate to the
firewall. 

 Give the certificate a descriptive
name. 

 Browse for the certificate file and
attach the GoDaddy certificate you downloaded. 

 Click OK . 

 Create a certificate profile for the MineMeld root CA
certificate. 
 On the firewall, select Device Certificate Management Certificate Profile . 

 Add a new certificate profile. 

 Give the certificate profile
a descriptive name. 

 Click Add , select the certificate
name from the CA Certificate drop-down, and click OK . 

 Click OK . 

 Configure the MineMeld nodes that will send indicators
to the firewall. 

 This procedure focuses on using AutoFocus miners
to forward indicators to an external dynamic list; however, you
can use other MineMeld miners that extract IPv4 addresses, domains,
and URLs to forward indicators to an external dynamic list. 

 Use an AutoFocus sample or indicator store
miner to Forward
AutoFocus Indicators to MineMeld . 

 In MineMeld, Connect
MineMeld Nodes (AutoFocus miner and processor) to an output
that can feed indicators to an external dynamic list on the firewall. 

 To find outputs that you can use with
an external dynamic list, view the list of MineMeld Prototypes and
search with the keyword EDL . 

 Restrict access to the indicators. 

 Select the output node you
plan to use with an external dynamic list from the list of Nodes . 

 Click Tags, enter a tag name to use with the output node,
and click OK . 

 Click Admin , and select the Feeds
Users tab. 

 Click (+) to add a new user profile for accessing the indicators
from the output node. 

 Create a username and password, confirm the password, and
click OK . 

 Grant the user you just created access to the output node.
In the Access setting for the user, select the tag for the output
node and click OK . 

 Configure the firewall to access an external
dynamic list based on the indicators from the AutoFocus miners. 

 Follow the steps to add a new external dynamic list to
the firewall and observe the following guidelines: 

 Enter
the MineMeld-provided link from the output node as the Source of
the external dynamic list. To find this link in MineMeld, select
the output node from the list of Nodes and
copy the Feed Base URL link. 

 Select the Certificate Profile you created
for the MineMeld root CA certificate. 

 Select Client Authentication , and enter
the username and password for the user you created from the previous
step. 

 Verify that the firewall can receive indicators from
the AutoFocus miners. 

 On the firewall, retrieve entries for the external dynamic list you
added and view the list entries . 

 Previous 

 Next 

 About AutoFocus 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
