---
url: https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-third-party-identity-provider-integrations/map-tenants-for-authorization
fetched_at: 2026-08-12T14:06:28Z
source: idira-and-identity
---

# Map a Tenant for Authorization Through Common Services Clear

Map a Tenant for Authorization Through Common Services 

 Home 

 EN

 Location 

 Documentation Home 

 Palo Alto Networks 

 Support 

 Live Community 

 Knowledge Base 

 Strata Copilot

 Common Services: Identity and Access 

 : 
 Map a Tenant for Authorization Through Common Services 

 Updated on 

 May 7, 2026 

 Focus 

 Download PDF 

 Filter

 Expand all | Collapse all 

 Get Started with Common Services: Identity & Access 

 Manage Identity and Access 

 About Identity and Access 

 Add Access 

 Remove Access 

 About Roles and Permissions 

 Assign a Role 

 Assign a Batch of Predefined Roles 

 Add a Custom Role 

 Modify a Custom Role 

 Clone a Role 

 Add a Service Account 

 Update a Service Account 

 Remove a Service Account 

 Manage Third Party Identity Provider Integrations 

 Add an Identity Federation 

 Manually Configure a SAML Identity Provider 

 Upload SAML Identity Provider Metadata 

 Get the URL of a SAML Identity Provider 

 Clone SAML Identity Provider Configuration 

 Add or Delete an Identity Federation Owner 

 Configure Palo Alto Networks as a Service Provider 

 Delete an Identity Federation 

 Map a Tenant for Authorization 

 Update Tenant Mapping for Authorization 

 Configure Custom SAML Role Mapping 

 PAN Resource Name Mapping Properties 

 Configure Third-Party Identity Provider Integration with Microsoft Entra ID 

 Configure Entra ID SAML Integration for Authentication Only 

 Configure Entra ID SAML Integration for Authentication and Authorization 

 SCIM 

 Sailpoint 

 OCI 

 Manage Single Tenant Transition to Multitenant 

 Release Updates 

 Updated on 

 May 7, 2026 

 Focus 

 Home 

 Common Services 

 Common Services: Identity and Access 

 Manage Third-Party Identity Provider Integrations Through Common Services 

 Map a Tenant for Authorization Through Common Services 

 Download PDF 

 Common Services: Identity and Access 

 Map a Tenant for Authorization Through Common Services 

 Table of Contents 

 Filter

 Expand all | Collapse all 

 Get Started with Common Services: Identity & Access 

 Manage Identity and Access 

 About Identity and Access 

 Add Access 

 Remove Access 

 About Roles and Permissions 

 Assign a Role 

 Assign a Batch of Predefined Roles 

 Add a Custom Role 

 Modify a Custom Role 

 Clone a Role 

 Add a Service Account 

 Update a Service Account 

 Remove a Service Account 

 Manage Third Party Identity Provider Integrations 

 Add an Identity Federation 

 Manually Configure a SAML Identity Provider 

 Upload SAML Identity Provider Metadata 

 Get the URL of a SAML Identity Provider 

 Clone SAML Identity Provider Configuration 

 Add or Delete an Identity Federation Owner 

 Configure Palo Alto Networks as a Service Provider 

 Delete an Identity Federation 

 Map a Tenant for Authorization 

 Update Tenant Mapping for Authorization 

 Configure Custom SAML Role Mapping 

 PAN Resource Name Mapping Properties 

 Configure Third-Party Identity Provider Integration with Microsoft Entra ID 

 Configure Entra ID SAML Integration for Authentication Only 

 Configure Entra ID SAML Integration for Authentication and Authorization 

 SCIM 

 Sailpoint 

 OCI 

 Manage Single Tenant Transition to Multitenant 

 Release Updates 

 Map a Tenant for Authorization Through Common Services 

 Learn how to map a tenant for authorization through the Common Services . 

 If you want to grant authorization to your users by passing the login information
 through your Security Assertion Markup Language (SAML) provider, you can map your
 identity federation to a tenant or tenant service group (TSG) hierarchy. By using
 the tenant mapping, you no longer have to add users and access directly through
 Common Services , but that option is still available. 

 After you add an identity federation and
 add an identity federation owner , the federation owner can
 map tenants for authorization. In addition to adding an admin as a federation owner,
 you must also give that admin a role that has permissions to
 assign and remove access policies on the given tenant, such as the following: 

 IAM Administrator 

 Multitenant IAM Administrator 

 Multitenant Superuser 

 Superuser 

 Custom role that includes
 iam.federation_mapping.update and
 iam.federation_mapping.delete 

 Use one of the various ways to access 
 Identity & Access . Only one way is shown here. 

 Select Identity & Access/Access Management Identity Federations 

 Scroll or search to find your identity federation. 

 Select Edit Tenant Mapping for Authorization . 

 Select which tenants can map users to the identity federation users and
 Save . 

 Inheritance applies the same way as it does in access management . If you map a tenant at the top
 level of the hierarchy, the child tenants nested below it will inherit the
 mapping so that the parent can manage them. 

 The identity federation owner can now manage the user access for all the
 selected tenant Service Groups. 

 Configure user access policies using one of the following methods: 

 Custom SAML Role Mapping (recommended) — Map your existing SAML
 attribute values to access policies directly in Strata Cloud Manager.
 See Configure Custom SAML Role
 Mapping . 

 Direct accessPolicies attribute — Go to your third-party identity
 provider's console and configure an
 accessPolicies attribute using the role and TSG
 format. The console details look similar to the following, but all
 providers are slightly different. You must name the attribute
 accessPolicies . 

 (Optional) Use a predefined role to assign a predefined set of
 permissions to a user. For details and syntax, see properties for predefined
 roles . 

 (Optional) Use a custom role to assign a custom set of
 permissions to a user. For details and syntax, see properties for custom
 roles . 

 Example SAML Response 

 This format applies to new customers as of December 2022. For existing Prisma SD-WAN customers, refer to Single Sign On Access using SAML . 

 Your IDPs may pass IDP defined access policies through a SAML attribute as
 follows: 

 <saml2:Attribute Name="email" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:unspecified">
 <saml2:AttributeValue xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">user@example.com</saml2:AttributeValue>
 </saml2:Attribute>
<saml2:Attribute Name="accessPolicies" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:unspecified">
 <saml2:AttributeValue xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">superuser@prn:1563214651::::</saml2:AttributeValue>
 <saml2:AttributeValue xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">view_only_admin@prn:1119006635::::</saml2:AttributeValue>
 </saml2:Attribute>

 In this example, there are two IDP defined access policies for this user:
 superuser@prn:1563214651:::: and
 view_only_admin@prn:1119006635::::: . For each IDP
 defined access policy returned, IAM will attempt to create access policies according
 to what is shown in the SAML, and remove any other IDP defined access policies that
 this user has. 

 If you don't send the
 accessPolicies array in the payload, no changes
 are made to the user's IDP-based access. 

 Previous 

 Delete an Identity Federation 

 Next 

 Update Tenant Mapping for Authorization 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
