---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-administrator-guide/6.14/onboard-cortex-xsoar/marketplace/content-pack-installation/install-a-content-pack/set-up-your-use-case-with-the-deployment-wizard
fetched_at: 2026-09-06T10:40:47Z
source: cortex-platform
---

# Set up Your Use Case with the Deployment Wizard | 6.14 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Administrator Guides 

 6.14 

 Onboard Cortex XSOAR 

 Marketplace 

 Content Pack Installation 

 Install a Content Pack 

 Cortex XSOAR 6.14 

 Set up Your Use Case with the Deployment Wizard 

 Configure a supported Cortex XSOAR 6.14 content pack with the Deployment Wizard. 

 The Deployment Wizard significantly reduces the time required to set up your use case. 

 It guides you through the process of setting up your content pack for your specific use case, including: 

 Configuring the fetching integration. 

 Configuring the main playbook and its input parameters. 

 Configuring any supporting integrations. 

 Note 

 When browsing for content packs, you can filter by those that support the Deployment Wizard, such as Malware Investigation and Response . 

 To access the Deployment Wizard for the first time, you need to first install or update your content pack(s) in Marketplace. The Deployment Wizard tab appears in Marketplace after the content pack installation or update is completed. 

 Prerequisites 

 Before installing or updating your content pack, you are prompted to install the content packs containing relevant supporting integrations (if not already installed). 

 Examples : 

 For the Malware Investigation and Response content pack, you need at least one incident fetching content pack (mandatory). You can also optionally install sandbox, messaging, case management, and data enrichment and threat intelligence content packs. 

 For the Phishing content pack, you need at least one email gateway content pack (mandatory). You can also optionally install sandbox, EDR systems, network devices, email security gateways, mail sender, and data enrichment and threat intelligence content packs. 

 In Marketplace, select the content pack for your use case (for example, Malware Investigation and Response or Phishing ) and click Install or Update (if the pack is already installed). 

 When browsing for content packs, you can search for content packs that contain the Deployment Wizard when you filter by Content Pack includes and then select Wizards . 

 deployment-wizard-pack-filter.png 

 The Select Content Packs window opens, where you select the items to include in the pack (for the mandatory items you must select at least one). These items are automatically added to the cart. 

 Note 

 If an item is already installed, it will automatically be checked off and grayed out and will not be listed in the cart checkout list, unless an update is required). 

 deployment-wizard-select-content-packs.png 

 Click Continue and then Install or Update the content pack. 

 When the content pack finishes installing or updating, click Refresh content or refresh your web page. 

 The DEPLOYMENT WIZARD tab appears. 

 Note 

 After you start running your use case you can return to this tab and make changes to the configurations, for example, your integration’s credentials or playbook parameters. 

 A small popup window appears next to the DEPLOYMENT WIZARD tab where you click Let’s Start to start the wizard. 

 deployment-wizard-Lets-Start.png 

 The tab opens showing the use case deployment flow. 

 Tip 

 What needs to be done actions for each step guide you through setting up your use case. 

 Step 1: Fetching Integration - click the displayed fetching integration. If the integration is new, select New instance . If you want to use an existing instance, select it from Update existing instance . The integration will stay disabled until you complete all steps of the wizard. 

 Note 

 You must define the incident type in order to set the playbook in the next step. 

 deployment-wizard-fetching-integration.png 

 The default fetching integration that appears depends on which fetching integration(s) are installed. For example: 

 Content Pack 

 Display Order for Default Fetching Integration 

 Malware Investigation and Response 

 1. Palo Alto Networks Cortex XDR - Investigation and Response 

 2. CrowdStrike Falcon 

 3. Microsoft Defender for Endpoint 

 Phishing 

 1. Gmail 

 2. EWS v2 (Make sure you also install the Microsoft Exchange On-Premise pack) 

 3. O365 Outlook Mail (Using Graph API) 

 4. Gmail Single User 

 5. O365 Outlook Mail Single User (Using Graph API) 

 Tip 

 Refreshing the page can resolve issues when running the wizard. 

 To update an existing integration: select Update existing instance and click Next . If more than one integration instance exists, choose the one you want to update. 

 deployment-wizard-update-instance.png 

 To create a new instance: Select New instance and click Next . 

 A list of What needs to be done guides you through the required fetching integration instance settings configurations. Scroll down to see the complete list. 

 deployment-wizard-configure-fetching-integration.png 

 After you save your settings, the wizard initiates a test connection. If the connection succeeds, the Fetching Integration step turns green and moves to the next step ( Set Playbook ). 

 deployment-wizard-fetching-test-success.png 

 Step 2: Set Playbook - select Configure Playbook & Parameters . 

 For example, the Setup Malware playbook pane opens showing the recommended primary playbook for the incident type you selected when configuring the fetching integration. 

 The playbook configuration includes all the input parameters to configure that will change the playbook behavior, for example, whether to use sandbox detonation or whether to perform isolation response. You can open the playbook by clicking the link on the bottom. 

 deployment-wizard-configure-playbook-4.png 

 Note 

 The wizard displays the recommended playbook. If for the fetching integration setup you chose an incident type that uses a different playbook from the recommended one, the incident type will be detached. 

 Click Done . 

 Step 3: Supporting Integrations - configure any installed supporting integrations in the content pack. 

 If a supporting integration is already installed and connected, it appears with a green check. Otherwise, click the integration to configure it. 

 deployment-wizard-supporting-integrations.png 

 Note 

 After you save the settings, the integration instance is automatically enabled. 

 Step 4: What’s Next - select Turn on Use Case . 

 Note 

 Your instance is disabled until you finish the wizard. Clicking Turn on Use Case starts the fetching process and runs the playbooks and automations. 

 deployment-wizard-turn-on-use-case.png 

 Previous Install a Content Pack 

 Next Delete a Content Pack 

 Last updated 4 days ago 

 Was this helpful?
