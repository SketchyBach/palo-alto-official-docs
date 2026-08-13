---
url: https://docs.paloaltonetworks.com/identity/release-notes/cloud-identity-engine/cloud-identity-engine-release-notes-welcome/new-features-introduced-in-may-2024
fetched_at: 2026-08-12T14:07:13Z
source: idira-and-identity
---

# New Features Introduced in May 2024 Clear

New Features Introduced in May 2024 

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

 New Features Introduced in May 2024 

 Updated on 

 Tue Apr 28 14:43:41 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Identity Docs 

 Activation & Onboarding 

 Cloud Identity Engine 

 Help 

 Release Notes 

 New Features 

 Updated on 

 Tue Apr 28 14:43:41 PDT 2026 

 Focus 

 Home 

 Identity 

 Welcome to the Cloud Identity Engine 

 New Features Introduced in May 2024 

 Download PDF 

 Identity 

 New Features Introduced in May 2024 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Identity Docs 

 Activation & Onboarding 

 Cloud Identity Engine 

 Help 

 Release Notes 

 New Features 

 Previous 

 New Features Introduced in June 2024 

 Next 

 New Features Introduced in April 2024 

 New Features Introduced in May 2024 

 Learn more about the new features for the Cloud Identity Engine that have been
 introduced in May 2024. 

 Feature Description 

 Enhancements for Cloud IP-Tag Connection 

 The Cloud IP-Tag Connection 
 feature has been given numerous improvements to expand capabilities
 and simplify usability for this security policy enforcement method,
 including the following: 

 A new connection status indicator (“Connection pending”) for all
 credential configuration types that displays when the cloud
 service provider you configured is syncing the IP address-to-tag
 mappings with the Cloud Identity Engine. 

 The ability to optionally sync service tags from your
 Azure directory, which represent a group of IP address prefixes
 for an Azure service. Service tags allow you to manage the
 address prefixes using the tag and to dynamically update the
 tags when IP addresses change, which simplifies updates in Azure
 for security policy based on IP addresses. 

 The ability to view the IP address-to-tag mapping information in
 much greater detail by using filters or by searching the mapping
 information. 

 Support for a new region in Europe (eu-west-4), allowing
 deployment to expand to new regions while remaining in
 compliance with regional data regulations. 

 The ability to create a credential configuration, a monitoring
 configuration, or both for the Google Cloud Platform (GCP).
 After you create a credential configuration to connect to GCP,
 you can configure a monitoring configuration to share mapping
 information with your other policy enforcement devices using
 segments or simply to monitor your mappings. This enables even
 more deployment scenarios using this cloud service provider,
 expanding the scope of the Cloud IP-Tag Connection’s assistance
 with policy enforcement. 

 These enhancements help expand the deployment possibilities for the
 Cloud IP-Tag Connection in your network even further, helping to
 ensure your mappings remain up to date for consistent security
 policy enforcement. 

 Filter Azure Active Directory Groups 

 Adhering to zero trust policies requires that your security policies
 are based not just on the IP address of the user but also the
 username, known as user-based security policy. To enforce user-based
 security policy, enforcement points (such as firewalls or Prisma
 Access) require access to up-to-date username-to-IP address
 mappings. The Cloud Identity Engine collects attributes from your
 directory to establish these mappings during synchronization (also
 known as a “sync”). To minimize the data that the Cloud Identity
 Engine collects from your directory and reduce sync time, you can
 now specify which groups you want the Cloud Identity Engine to sync. 

 By specifying the attributes (either name, unique identifier, or
 both) that you want to use to define the Azure Active Directory
 groups that the Cloud Identity Engine syncs, you can now
 sync the information from your directory more quickly and more
 frequently than would be possible using the SCIM Connector while
 still limiting group data collection. Updates using the SCIM
 Connector are limited to once every 40 minutes, but by filtering
 groups, you can update your directory information as frequently as
 every five minutes. 

 You can optionally add an operand to filter groups based on multiple
 attributes, allowing you even more fine-grained filtering to select
 only the groups that you need to sync to enforce policy. 

 By ensuring that you collect only the groups that are applicable to
 your policy, you can minimize the time necessary to sync your data. 

 This capability means that your enforcement points can receive more
 frequent updates for the mappings they use to enforce your
 user-based security policy, ensuring consistent application of your
 security policy rules. 

 “Do It Later” option for SAML 2.0-based Authentication
 Types 

 You can now configure the metadata for a SAML 2.0-based authentication
 type in the Cloud Identity Engine at a later time by
 selecting the “Do It Later” option. This option allows you to
 configure and submit the authentication type without specifying the
 metadata for your SAML 2.0-based identity provider (IdP). 

 For example, if your organization requires you to submit a ticket to
 obtain metadata, or if you need to obtain the metadata from your
 IdP, the “Do It Later” option enables you to configure the
 authentication type and submit the changes without requiring
 metadata from your IdP so that you can complete creation of the
 authentication type later without having to recreate the
 authentication type later. 

 Once you have the necessary metadata for your IdP, edit the
 configuration to select the method you want to use to provide the
 IdP metadata, add the metadata, test the connection to verify that
 the Cloud Identity Engine can access data from the IdP, and submit
 the updated configuration. The authentication type is not enabled
 until you edit the configuration and add the metadata. 

 The “Do It Later” option allows you more flexibility when deploying
 an authentication type so that you can enter the IdP information you
 have available and then easily update your configuration later when
 you have the required metadata to complete the configuration. By
 providing more options for you to configure your authentication
 types, the Cloud Identity Engine provides more ways to simplify your
 deployment, providing you even more freedom to configure the
 authentication type at your own pace. 

 Previous 

 New Features Introduced in June 2024 

 Next 

 New Features Introduced in April 2024 

 On This Page 

 Activation and Onboarding 

 Strata Cloud Manager 

 Activate a License or Product 

 Cloud Identity Engine 

 Strata Logging Service 

 Device Associations 

 Hub 

 Identity and Access Management 

 Tenant Management 

 Next-Generation Firewalls 

 AIOps for NGFW 

 Cloud Management for NGFWs 

 Cloud NGFW for AWS 

 Cloud NGFW for Azure 

 CN-Series 

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 Panorama 

 Service Provider 

 VM-Series 

 Plugins 

 SASE 

 Prisma Access 

 Prisma SASE Multitenant Platform 

 Prisma Access Monitoring & Visibility 

 Endpoints 

 GlobalProtect 

 Remote Browser Isolation 

 Prisma Access Agent 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Resources 

 All Products A - Z 

 All Release Notes 

 Compatibility Matrix 

 Experts Corner 

 Network Security Platform 

 Security Policy 

 Decryption 

 Device-ID 

 IPSec VPN 

 Quality of Service 

 Quantum Security 

 Release Notes 

 Network Security 

 Cloud Identity Engine 

 Cloud-Delivered Security Services 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
