---
url: https://docs.paloaltonetworks.com/content/techdocs/en_US/identity/cloud-identity-engine/identify-users-and-devices-with-cie/choose-directory-type/configure-a-cloud-based-directory.html
fetched_at: 2026-09-16T09:20:53Z
source: palo-alto-main
---

# Configure a Cloud-Based Directory Clear

Updated on 

 Aug 5, 2026 

 Focus 

 Home 

 Identity 

 Identify Users and Devices with Cloud Identity Engine 

 Configure Directories for User Identification 

 Configure a Cloud-Based Directory 

 Download PDF 

 Identity 

 Configure a Cloud-Based Directory 

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

 Authenticate the Agent and the Cloud Identity Engine 

 Next 

 Set Up an Entra ID Directory 

 Configure a Cloud-Based Directory 

 Where Can I Use
 This? What Do I
 Need? 

 NGFW 

 Prisma Access 

 The Cloud Identity Engine service is free;
 however, the enforcement points utilizing
 directory data may require specific licenses.
 Click here for
 more information. 

 After you activate your Cloud Identity Engine tenant,
configure a cloud-based directory, such as Azure Active Directory
(Azure AD), Okta Directory, or Google Directory, to communicate
with the Cloud Identity Engine. 

 Configuring a cloud-based directory in the Cloud Identity Engine enables
 your network security infrastructure to identify users and enforce
 policies based on identity rather than IP addresses. By granting the
 Cloud Identity Engine read-only access to your organization's
 directory data, you establish a centralized source of truth that
 synchronizes user, group, and device attributes across your entire
 deployment. 

 For Microsoft Entra ID (Azure AD) , you can
 establish a connection using the recommended CIE Enterprise App or a
 client credential flow, with options to collect advanced data like
 user risk signals for dynamic policy adjustments. Okta
 integrations offer similar flexibility, allowing you
 to connect via an OpenID Connect (OIDC) app using either an
 authorization code or client credential flow to sync user and group
 attributes. For organizations using Google
 Directory , the engine connects directly via the
 Google Admin API to retrieve organizational units and user
 details. 

 If your organization requires a more customized approach or uses a
 different provider, the SCIM
 Connector allows you to ingest identity data from any
 SCIM-compliant source—such as PingFederate or customized Entra ID
 setups—giving you granular control over which attributes are shared.
 Additionally, for scenarios where an external identity provider is
 not available or necessary, you can configure a CIE Directory . This
 cloud-native, local directory lets you create and manage users
 directly within the engine, offering a quick solution for testing or
 specific user segments without requiring external
 infrastructure. 

 To use the System for Cross-domain Identity Management (SCIM)
provisioning to customize which attributes your Azure AD shares
with the Cloud Identity Engine, you can configure the SCIM Connector. 

 If the connection between your directory and the Cloud Identity
Engine is not active, you can reconnect your directory. If you no
longer want to associate a directory with the Cloud Identity Engine,
learn how to revoke the permissions for that directory. 

 Previous 

 Authenticate the Agent and the Cloud Identity Engine 

 Next 

 Set Up an Entra ID Directory
