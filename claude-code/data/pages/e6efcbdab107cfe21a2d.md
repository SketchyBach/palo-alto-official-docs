---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/cloudblades/cloudblade-integrations/chatbot-ms-teams-cloudblade-integration/create-user-groups-and-configure-chatbot-ms-teams
fetched_at: 2026-08-13T17:29:03Z
source: palo-alto-main
---

# Create User Groups and Configure Chatbot MS Teams   Clear

Create User Groups and Configure Chatbot MS Teams 

 Home 

 EN

 Location 

 Documentation Home 

 Palo Alto Networks 

 Support 

 Live Community 

 Knowledge Base 

 >

 Strata Copilot

 Create User Groups and Configure Chatbot MS Teams 

 Updated on 

 Wed Feb 25 07:42:19 PST 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma SD-WAN Docs 

 Activation & Onboarding 

 Administration 

 CloudBlades 

 Select a Document 

 CloudBlade Integrations 

 CloudBlades Integration with Prisma Access 

 Deployment 

 Incidents & Alerts 

 Reference 

 Release Notes 

 Select a Document 

 ION 6.8 

 ION 6.6 

 ION 6.5 

 ION 6.4 

 ION 6.3 

 ION 6.1 

 ION 5.6 

 Prisma SD-WAN Controller 

 Prisma SD-WAN On-Premises Controller 

 Prisma SD-WAN CloudBlades 

 Prisma Access CloudBlade Cloud Managed 

 Prisma Access CloudBlade Panorama Managed 

 New Features 

 Updated on 

 Wed Feb 25 07:42:19 PST 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Chatbot MS Teams CloudBlade Integration 

 Create User Groups and Configure Chatbot MS Teams 

 Download PDF 

 Prisma SD-WAN 

 Create User Groups and Configure Chatbot MS Teams 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma SD-WAN Docs 

 Activation & Onboarding 

 Administration 

 CloudBlades 

 Select a Document 

 CloudBlade Integrations 

 CloudBlades Integration with Prisma Access 

 Deployment 

 Incidents & Alerts 

 Reference 

 Release Notes 

 Select a Document 

 ION 6.8 

 ION 6.6 

 ION 6.5 

 ION 6.4 

 ION 6.3 

 ION 6.1 

 ION 5.6 

 Prisma SD-WAN Controller 

 Prisma SD-WAN On-Premises Controller 

 Prisma SD-WAN CloudBlades 

 Prisma Access CloudBlade Cloud Managed 

 Prisma Access CloudBlade Panorama Managed 

 New Features 

 Previous 

 Chatbot MS Teams CloudBlade Integration 

 Next 

 Assign Chatbot to a Channel/Team 

 Create User Groups and Configure Chatbot MS Teams 

 Learn to create user groups and configure the chatbot MS teams
 cloudblade. 

 Where Can I Use This? What Do I Need? 

 Prisma SD-WAN (Managed by Strata Cloud Manager ) 

 Prisma SD-WAN 

 Chatbot MS Teams CloudBlade 

 Create a user group on MS Teams. You can follow any of the following methods to
 create a user group: 

 Create a user group on Azure
 Active Directory 

 Create a team/user group from
 scratch 

 Create a team from an existing
 team 

 Create a team from an existing
 group 

 After a user group is created on MS Teams, copy the User Group ID (object ID). 

 Enter the ID when configuring the Chatbot-MS Teams CloudBlade on Prisma SD-WAN . You can configure more than one user group on
 the CloudBlade. The User Group ID(s) can be retrieved by any of the
 following methods: 

 Azure Active Directory 

 Go to the Azure Active Directory
 portal and select
 Groups on the left panel. 

 Search and select the specific User
 Group and copy the
 object-id from the Azure
 portal. 

 Microsoft Teams 

 Go to your Team More Options Get a link to Team . 

 This provides a URL that contains the group-id. 

 For example, the Get link to Team option will display
 a URL like the one below. Embedded in the URL is the
 groupId highlighted below. Only copy the groupId
 text between = and & for
 configuration on the CloudBlade. 

 https://teams.microsoft.com/l/team/19%3afZljepRtSxrVfX1hkf876XCvPFY_jion787GBcD5lvY1%40thread.tacv2/conversations?groupId =abc6d320-b3f1-87c2-8755-02e9endaeda1 &tenantId=123dr678-h456-b758-b010-41830555h3bd 

 Configure Chatbot MS Teams 

 From the Strata Cloud Manager, select Configuration Prisma SD-WAN CloudBlades . 

 In CloudBlades, locate the Chatbot MS Teams tile and
 click Configure . 

 Contact the Palo Alto Support team if this CloudBlade does not appear in
 the list. 

 In the Chatbot-MS Teams page, enter the following
 information in the fields shown below, change where appropriate. 

 Version : Select the latest version of the
 Chatbot-MS Teams CloudBlade. 

 Admin State : For Admin State, select
 Enabled. 

 Microsoft Teams Group Information : Enter the Teams
 group Azure Active Directory ID obtained in the previous section. 

 To add multiple user groups, enter the IDs as comma-separated values. For
 example: Teams_group_AAD_ID1, Teams_group_AAD_ID2, Teams_group_AAD_ID3.

 Click Save and Install . 

 Previous 

 Chatbot MS Teams CloudBlade Integration 

 Next 

 Assign Chatbot to a Channel/Team 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Activate a License or Product 

 Cloud Identity Engine 

 Hub 

 Identity and Access Management 

 Tenant Management 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 AI-Powered ADEM 

 Prisma Access Monitoring and Visibility 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 FedRAMP 

 Prisma SASE for FedRAMP 

 Hardware Reference 

 ION 1000 

 ION 1200 

 ION 1200-S 

 ION 2000 

 ION 3000 

 ION 3200 and ION 3200H 

 ION 5200 

 ION 7000 

 ION 9000 

 ION 9200 

 Hardware Quick Start Guides 

 ION 1200 

 ION 1200 4G 

 ION 1200 5G 

 ION 1200-S 

 ION 1200-S 4G 

 ION 1200-S 5G 

 ION 3200 

 ION 3200H 

 ION 3200H 5G 

 ION 5200 

 ION 9200 

 Virtual ION Deployment 

 Virtual ION on AWS 

 Virtual ION on Azure 

 Virtual ION on GCP 

 Virtual ION on Alibaba Cloud 

 Virtual ION on KVM for NFV 

 Virtual ION on OCI 

 Virtual ION on VMware 

 Virtual ION on Megaport Virtual Edge 

 Virtual ION on Dell PowerEdge 

 Prisma SD-WAN Integration 

 AWS Cloud-WAN Integration (GRE Connect) 

 AWS Cloud-WAN Integration (Tunnel-less Connect) 

 Checkpoint Integration 

 LiveAction Integration 

 Netskope Integration 

 Symantec Web Security Services Integration 

 Prisma SD-WAN Experts Corner 

 Network Policy 

 QoS Whitepaper 

 Security Architecture Whitepaper 

 External Antennas for ION-C Series 

 Dynamic Path Selection 

 Best Practices 

 Best Practices Library 

 Resources 

 All Products A - Z 

 Compatibility Matrix 

 Prisma SD-WAN 

 Strata Cloud Manager 

 Prisma SASE 

 CloudBlades 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
