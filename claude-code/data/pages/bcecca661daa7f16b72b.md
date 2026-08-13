---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/cortex-xsiam-data-sources/cloud-service-provider-csp-onboarding/outpost-onboarding/outpost-troubleshooting
fetched_at: 2026-08-13T15:00:20Z
source: cortex-platform
---

# Outpost troubleshooting | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

Outpost troubleshooting | Cortex Documentation Portal 

 ⌘ Ctrl k 

 Blog Support 
 More 

 Home 

 Products 

 Guides 

 Release Notes 

 API 

 Reference 

 AI Assistant 

 Good afternoon 
 I'm here to help you with the docs. 

 What is this page about? What should I read next? Can you give an example? 

 ⌘ Ctrl i 

 AI Based on your context 
 Send 

 Learn about Cortex XSIAM 

 Navigate the Cortex XSIAM docs 

 Get started with Cortex XSIAM 

 Agentic AI in Cortex XSIAM 

 Cortex XSIAM product licenses 

 In-product support ticket creation 

 Supported web browsers 

 Use the interface 

 Manage API keys 

 Onboard Cortex XSIAM 

 How to onboard Cortex XSIAM 

 Plan and prepare 

 Deployment steps 

 Post-deployment 

 Configure Cortex XSIAM 

 Learn how to configure Cortex XSIAM 

 Data management 

 Cortex XSIAM Data Sources and Connectors 

 What are Cortex XSIAM data sources and connectors? 

 Complete data source and connector catalog 

 Vendor-specific data sources and connectors 

 Connectors 

 Standard data sources 

 Cloud service provider (CSP) onboarding 

 Understand CSP onboarding tiers and licensing 

 Amazon Web Services cloud onboarding 

 Microsoft Azure cloud onboarding 

 Google Cloud Platform cloud onboarding 

 Oracle Cloud Infrastructure cloud onboarding 

 Alibaba Cloud cloud onboarding 

 Outpost onboarding 

 Outpost fundamentals and planning 

 Outpost creation workflow 

 Working with standard outposts 

 Working with Bringing your own Azure app (BYOA) outposts 

 Outpost troubleshooting 

 Outpost Cloud Service Provider (CSP) permissions 

 Introduction to Terraform for Cloud service provider (CSP) onboarding 

 Manually connect a cloud instance 

 Manage cloud instances 

 Pending cloud instances 

 Edit your onboarded CSP configuration 

 Update cloud permissions after Cortex release updates 

 Troubleshoot errors on cloud instances 

 Cloud service provider permissions 

 Generic on-premise data collectors 

 Palo Alto Networks integrations 

 Cloud Posture and Runtime Security data sources 

 External alerts using External Issue Mapping 

 Administration and troubleshooting 

 Marketplace 

 Configure the Cortex Agentic Assistant 

 Cortex MCP server 

 Automations 

 Engines 

 Remote repository management 

 Customize cases and issues 

 XQL query management 

 Multi-Tenant 

 Managed Services configuration in Cortex 

 Protect your endpoints 

 Endpoint security 

 Endpoint DLP 

 Detect, Investigate, and respond to threats 

 Monitor dashboards and reports 

 Investigation and response 

 Agentic Assistant chat 

 Asset management 

 Threat management 

 Attack surface management 

 Vulnerability management 

 Exposure management 

 Cortex Advanced Email Security 

 Identity Threat Detection and Response (ITDR) 

 Cloud Security 

 Monitor and track compliance adherence 

 Cloud security rules and policies 

 Cortex Cloud Data Classification 

 Cortex Data Security 

 Cloud Identity Security 

 Network exposure detection 

 Cortex Cloud SaaS Security 

 Cortex Cloud AI Security 

 Serverless function posture security 

 Cortex Cloud Application Security 

 Cloud workload policies and rules 

 Base image rules 

 Web and API Security (WAAS) 

 Serverless function runtime security 

 Reference and developer docs 

 Cortex XSIAM XQL 

 Graph Search 

 Cortex CLI 

 Role-Based Access Control 

 API documentation 

 Reference 

 Migrating to a new Broker VM image 

 Learn more about migrating to the latest broker VM image 

 Standalone Broker VM 

 Broker VM high availability cluster node 

 On this page 

 For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSIAM 

 Cortex XSIAM Documentation 

 Configure Cortex XSIAM 

 Cortex XSIAM Data Sources and Connectors 

 Cloud service provider (CSP) onboarding 

 Outpost onboarding 

 Outpost troubleshooting 

 Check here for solutions to issues that might occur while configuring, deploying, and operating outposts. 

 This document provides solutions for issues that might occur while deploying, configuring, and operating Cortex XSIAM. outposts. These troubleshooters can help identify symptoms, locate errors, and suggest how you can remediate. 

 General troubleshooting 

 These general troubleshooters apply to all cloud service providers and outpost deployment modes. 

 Terraform executes successfully but no outpost appears in Cortex 

 After a successful Terraform run, your cloud environment sends a notification to Cortex to register the new outpost. If the outpost doesn't appear in the Cortex console, verify that outbound internet connectivity is available from the environment where Terraform was executed. The notification requires an active connection to reach Cortex. If connectivity is confirmed and the outpost still doesn't appear, contact customer support for a manual workaround. 

 Terraform template execution fails on a non-approved tenant, such as after changing the target tenant mid-deployment 

 If Terraform execution fails on a non-approved tenant, such as if you change an Azure target tenant after starting outpost creation. Terraform execution fails because the outpost is bound to the originally-approved tenant. Delete the partially-created outpost from the Cortex console, revert to the approved tenant, and re-run the Terraform template. 

 Standard outpost troubleshooting 

 Standard outposts handle most of the infrastructure and identity provisioning automatically. Issues in this deployment mode might stem, for example, from broad permission gaps, restrictive policy definitions, or quota limits that prevent Cortex from deploying necessary resources. 

 Bring your own app (BYOA) troubleshooting - Azure 

 This section details common deployment and runtime errors that occur when a Bring Your Own App (BYOA) Azure outpost is configured. These errors might appear, for example, if the app registration, service principal, and user-assigned managed identities (UAMIs) were created manually via the Azure portal instead of using the provided helper script. 

 Use the following table to identify symptoms and apply the appropriate resolutions. 

 Symptom / error message 

 Terraform deployment phase 

 Resolution 

 Single-tenant app registration 

 Error: ... sign_in_audience must be 'AzureADMultipleOrgs' ... 

 Plan 

 Recreate the app registration as a multi-tenant application.

The Azure portal defaults to single-tenant ("this org only").

Run this command:

 az ad app create --display-name <name> --sign-in-audience AzureADMultipleOrgs 

 Incorrect service principal ID 

 Error: ... customer_sp_object_id ... is the SP of a different AppReg ... 

 Plan 

 An incorrect service principal object ID was provided.

Retrieve the correct ID by running:

 az ad sp show --id <CUSTOMER_APP_CLIENT_ID> --query id -o tsv 

Update the customer_sp_object_id variable in your tfvars file. 

 Missing Terraform runner ownership 

 Error: Warning: The Terraform runner ... is NOT listed as an owner of the BYO App Registration ... 

 Plan 

 The Terraform runner must be added as an owner of the app registration.

Without this, the deployment fails with an "Insufficient privileges" error when attempting to create the first federated identity credential (FIC).

Run:

 az ad app owner add --id <APP_ID> --owner-object-id <TF_RUNNER_OBJ_ID> 

 Disabled service principal 

 Error: ... Customer SP ... is disabled in Entra ... 

 Plan 

 The service principal is disabled.

Re-enable it by running:

 az ad sp update --id <SP_OBJ_ID> --set accountEnabled=true 

Alternatively, toggle it in the Azure portal under Enterprise applications > [Your SP] > Properties . 

 Cross-subscription UAMI 

 Error: ... Customer UAMI ... lives in subscription <X> but the outpost is being deployed to <Y> ... 

 Plan 

 Cross-subscription UAMIs are not supported because the Azure Instance Metadata Service (IMDS) only returns tokens for local identities.

Recreate the UAMI in the outpost's subscription and update customer_uami_*_id in your tfvars file. 

 Cross-tenant UAMI 

 Error: ... Customer UAMI ... lives in tenant <X> but the outpost subscription is in tenant <Y> ... 

 Plan 

 Cross-tenant UAMIs are not supported.

Recreate the UAMI in the correct Entra ID tenant to match the outpost subscription. 

 Duplicate UAMI IDs 

 Error: ... All 5 customer UAMI IDs must be distinct ... 

 Plan 

 Duplicate UAMI IDs were provided.

The error message lists all 5 IDs.

Replace the duplicates with the correct, distinct UAMI IDs and rerun Terraform. 

 Insufficient privileges for FIC 

 Error: Error: creating Federated Identity Credential ... Insufficient privileges to complete the operation 

 Apply 

 App registration owner permissions are missing for the Terraform runner.

Verify ownership by running az ad app owner list --id <APP_ID> .

Add the owner by running:

 az ad app owner add --id <APP_ID> --owner-object-id <TF_RUNNER> 

 Stale federated credential 

 Error: Another object with the same value for property federatedIdentityCredentials/<name> already exists 

 Apply 

 A stale FIC exists from a previous deployment attempt or manual portal entry.

List existing credentials using az ad app federated-credential list --id <APP_ID> -o table .

Delete the conflicting one with az ad app federated-credential delete --id <APP_ID> --federated-credential-id <NAME> .

Rerun the deployment. 

 Subject does not exist (replication lag) 

 Error: 400 BadRequest: Subject does not exist in directory. 

 Apply 

 The UAMI was created very recently, and it has not yet replicated across Entra ID.

Wait 30 to 60 seconds and rerun terraform apply .

Verify the subject exists with az ad sp show --id <UAMI_PRINCIPAL_ID> . 

 Accidental UAMI deletion 

 Error: terraform destroy deleted my customer-created UAMIs! 

 Destroy 

 The UAMIs were incorrectly placed inside the outpost's Cortex-managed resource group.

Terraform deletes UAMIs placed inside the outpost's Cortex-managed resource group during a destroy operation.

Recreate the UAMIs in a customer-owned resource group outside of the outpost boundaries and re-onboard. 

 Previous The shell script for Azure app registration Next Outpost Cloud Service Provider (CSP) permissions 

 Last updated 15 days ago 

 Was this helpful? 

 ‍ 

 Trust Center 

 ‍ 

 Privacy 

 ‍ 

 Terms of Use 

 ‍ 

 Legal 

 © 2026 Palo Alto Networks, Inc. All rights reserved. 

 General troubleshooting 

 Standard outpost troubleshooting 

 Bring your own app (BYOA) troubleshooting - Azure 

 Was this helpful?
