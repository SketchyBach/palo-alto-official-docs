---
url: https://docs.paloaltonetworks.com/identity/cloud-identity-engine/identify-users-and-devices-with-cie/manage-your-directories
fetched_at: 2026-09-15T15:14:34Z
source: idira-and-identity
---

# Manage Your Directories Clear

Updated on 

 Aug 5, 2026 

 Focus 

 Home 

 Identity 

 Identify Users and Devices with Cloud Identity Engine 

 Manage Your Directories 

 Download PDF 

 Identity 

 Manage Your Directories 

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

 Configure a CIE Directory 

 Next 

 Manage Your Azure Directory 

 Manage Your Directories 

 Learn about managing your cloud-based and on-premise directories. 

 Where Can I Use This? What Do I Need? 

 NGFW 

 Prisma Access 

 The Cloud Identity Engine service is free; however, the
 enforcement points utilizing directory data may require specific
 licenses. Click here for more
 information. 

 Managing your directory integrations is essential for maintaining an accurate source
 of truth for user identification and policy enforcement. Whether utilizing
 on-premises infrastructure or cloud providers, the Cloud Identity Engine provides
 tools to monitor connections, customize data collection, and troubleshoot
 synchronization issues. 

 For On-Premises directories (Active Directory or OpenLDAP), management focuses on the Cloud Identity Agent . You must
 ensure the agent remains online and updated to the latest version to maintain a
 secure connection. Administrative tasks include managing the certificates used for
 mutual authentication and configuring filters to limit the objects—such as specific
 Organizational Units, computers, or containers —that are synchronized to the cloud,
 which helps optimize performance. 

 Cloud-Based directories require maintaining valid API connections and
 permissions to ensure continuous data access: 
 Microsoft Entra ID (Azure AD) Directory : You may
 need to reconnect the directory to grant new permissions for advanced
 features like risk scoring or to update your client credentials. You can
 also manage group filters, including uploading CSV files to precisely
 specify which groups the engine should collect. 

 Okta Directory : If using the Auth Code flow, you
 must periodically reconnect the directory to refresh tokens. For
 configurations using the Client Credential flow, management typically
 involves updating secrets or adjusting the scope of collected data, such as
 enabling the collection of enterprise applications. 

 Google Directory : Unlike other providers, Google
 Directory allows you to manually configure the synchronization interval
 (e.g., every 6, 12, or 24 hours) to align with your API quotas and data
 freshness requirements. 

 Across all directory types, you can view the collected data to verify user and group
 mappings. If you notice discrepancies, you can manually trigger a Full Sync 
 or Sync Changes to propagate updates immediately without waiting for the
 scheduled interval. 

 Previous 

 Configure a CIE Directory 

 Next 

 Manage Your Azure Directory
