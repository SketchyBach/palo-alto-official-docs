---
url: https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/configuration-scm/manage-configuration-ngfw-and-prisma-access/configuration-overview
fetched_at: 2026-08-13T17:37:25Z
source: palo-alto-main
---

# Configuration: Overview Clear

Configuration: Overview 

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

 Configuration: Overview 

 Updated on 

 Mon Aug 03 07:58:33 PDT 2026 

 Focus 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deutsch (German) 

 Filter

 Expand All 
 | 
 Collapse All 

 Strata Cloud Manager Docs 

 Activation & Onboarding 

 Subscription & Tenant Management 

 Getting Started 

 AIOps 

 Release Notes 

 New Features 

 Updated on 

 Mon Aug 03 07:58:33 PDT 2026 

 Focus 

 Home 

 Strata Cloud Manager 

 Strata Cloud Manager Getting Started 

 Configuration: Strata Cloud Manager 

 Configuration:
 NGFW and Prisma Access 

 Configuration: Overview 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Deutsch (German) 

 Strata Cloud Manager 

 Configuration: Overview 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Strata Cloud Manager Docs 

 Activation & Onboarding 

 Subscription & Tenant Management 

 Getting Started 

 AIOps 

 Release Notes 

 New Features 

 Previous 

 Configuration: NGFW and Prisma Access 

 Next 

 Configuration: Snippets 

 Configuration : Overview 

 Learn about the management options available to you in Strata Cloud
 Manager. 

 Where Can I Use This? What Do I Need? 

 Prisma Access (Managed by Panorama or Strata Cloud Manager) 

 NGFW , including those funded by Software NGFW
 Credits 

 Each of these licenses include access to Strata Cloud Manager : 

 Prisma Access 

 AIOps for NGFW Premium license (use the Strata Cloud Manager app) 

 Strata Cloud Manager Essentials 

 Strata Cloud Manager Pro 

 → The features and capabilities available to you in Strata Cloud Manager depend on which license(s) you are
 using. 

 Think of the Overview page as your launching point in to NGFW and Prisma Access both for
 first time setup, and for day-to-day configuration management ( Configuration NGFW and Prisma Access Overview ). 

 Configuration Scope 

 With Strata Cloud Manager , you can apply configuration settings and
 enforce policy globally across your environment, or target them to specific parts of
 your organization. When working in your Strata Cloud Manager configuration
 management, the current Configuration Scope is always visible
 to you, and you can toggle your view to manage a broader or more granular
 configuration. 

 Learn more about: 

 Folder Management 
 Use
 folders to logically group your devices and deployment types for
 simplified configuration management. 

 Snippets 
 Use snippets to group configurations that you
 can quickly push to your firewalls or deployments. 

 Variables 
 Use variables your configurations to
 accommodate device or deployment-specific configuration
 objects. 

 Configuration Operations 

 Use the Strata Cloud Manager operations to push configuration changes, review past
 configuration pushes, and manage your configuration versions snapshots to load or
 revert them to a previous configuration version. 
 Push
 your configuration changes 

 Review
 the status of a configuration push 

 Revert configuration changes by Administrator 

 Manage your configuration versions
 snapshot 

 Per-Admin Configuration Push and Revert 

 Please contact your account team to enable the
 feature. 

 In shared environments, concurrent configuration changes by multiple
 administrators can lead to conflicts where a single error traditionally requires
 reverting all uncommitted changes. Strata Cloud Manager addresses this challenge
 by moving beyond the traditional all-or-nothing commit model to offer precise
 control in multi-administrator environments. 

 You can now selectively revert uncommitted changes made by specific
 administrators within defined scopes or within designated containers, cloud
 containers, on-premises containers, and snippets. This feature allows you to
 revert specific uncommitted changes from the candidate configuration while
 preserving other administrators' work. In addition to reverting changes, you can
 perform partial configuration pushes to deploy only the changes within your
 selected scope to designated device. 

 To ensure deployment accuracy, you can preview changes before you revert or push
 them. The system provides detailed information about dependencies that might
 prevent the operation, allowing you to resolve issues before deployment. 

 You cannot use selective push or revert and must perform all-admin push in the
 following scenarios: 
 Configuration load operations. 

 Changes in container hierarchy, such as snippet association or
 disassociation. 

 Internal commits triggered by tenant upgrades. 

 When the number of uncommitted changes exceeds 500. 

 This procedure guides you through selectively reverting uncommitted configuration
 changes within Strata Cloud Manager. 

 Log in to Strata Cloud Manager . 

 Select Push Config and
 Revert . 

 Define the scope for the revert operation in the Revert
 Candidate Configuration window. 

 Use the Admin Scope to choose the
 administrator(s) whose uncommitted changes you want to
 revert. The Admin Scope lists all
 administrators who have made changes to your tenant. 

 Select the Location Scope to specify
 the configuration entities such as folders, snippets,
 cloud-containers, on-prem-containers where changes should be
 reverted. By default, all folders and snippets are selected.
 Adjust this based on the specific changes you intend to
 revert. This granular selection ensures you target only the
 intended changes and prevents accidental rollbacks of other
 administrators' work or unrelated configuration areas. 

 Select Get Target Object List or
 Refresh to view the affected objects. The
 list populates with all uncommitted changes matching your selected
 Admin Scope and Location
 Scope . This step provides a clear overview of all
 modifications affected by the revert, allowing for verification before
 proceeding. Review the Target Objects table to
 see the object type and the number of the objects the revert operation
 will impact. 

 Select Revert Preview . The preview displays a
 detailed before-and-after comparison of the configuration objects,
 indicating what will be restored or deleted. The revert preview provides
 a critical safety check, allowing you to confirm the selected changes
 and understand the operation's exact impact. This helps prevent
 unintended configuration disruptions. 
 Object Name identifies the policy,
 object, network settings, or device setting. 

 Type specifies is the kind of setting,
 such as Address, Security rule, or Zone. 

 In the preview window, compare the proposed against the running
 configuration. The preview window uses color coding to indicate
 additions in green, modifications in yellow, and deletions in
 red. 

 Revert . The rollback process initiates for all
 changes identified within your defined scope. 

 Address any dependency errors if the revert fails. 
 Review the error message for schema verification failures or
 object dependencies. The system indicates specific dependencies
 (for example, an invalid reference or an application override
 rule) that prevent the revert. 

 Navigate to the conflicting configuration and resolve the
 dependency. For example, delete an Application
 Override Policy rule causing a conflict. The
 revert process includes robust validation to prevent
 configuration breakage. Understanding and resolving dependencies
 is essential to successfully roll back changes without
 introducing new errors or inconsistencies. 

 Verify the successful revert. 
 Observe the UI reloading automatically after a successful
 revert. 

 Navigate to the relevant configuration sections to confirm that
 the reverted objects have been removed or restored to their
 previous state. Verifying the revert ensures the intended
 changes have been successfully undone and your system's
 configuration is in the expected state. This confirms the
 integrity and correctness of the rollback operation. 

 Global Find Using Config Search 

 This feature is available on request for users with Strata
 Cloud Manager Pro license tier. Please contact your account team to enable the
 feature. 

 Config Search enables you to search configuration objects
 and settings for a particular string, such as IP addresses, object name, referenced
 objects, duplicate objects, policy names, policy rules, policies covered for
 specific CVEs, rule UUID, predefined snippets, or application name and get the list
 of all references where the object is used. 

 To launch Config Search , click the 

 icon beside Push
 Config on the upper right side of the web interface.
 Config Search is available from all pages under
 Manage . 

 In the Config Search screen, you can search by using
 the Config String , Location ,
 Object Type , Edited By , or
 Edited At fields. 

 Search tips: 
 To find an exact phrase, enclose the phrase in quotes. 

 Spaces in search terms are handled as AND operations. For
 example, if you search on corp policy, the search results
 include instances where corp and policy exist in the
 configuration. 

 To rerun a previous search, click the Config Search icon, which
 displays the last 50 searches. Click any item in the list to
 rerun that search. The search history list is unique to each
 administrator account. 

 Config Search is available for each field that’s searchable. For
 example, you can search on the following object types for a
 Security policy: Tags, Zone, Address, User, HIP Profile,
 Application, UUID, and Service. 

 Location is grouped by folders and snippets. You can select more
 than one location to search. If you do not select any location,
 All locations will be selected by
 default. 

 If the object type is not selected, All 
 will be selected. 

 The search results are categorized and provide links to the configuration
 location in the Strata Cloud Manager, allowing you to easily find all
 occurrences and references of the searched string. 

 Global 

 Prisma Access 

 Configuration Overview (Strata Cloud Manager) 

 Global 

 Where Can I Use
 This? What Do I Need? 

 Prisma Access (Managed by Strata Cloud Manager) 

 NGFW (Managed by Strata Cloud Manager) 

 NGFW (Managed by PAN-OS or Panorama) 

 VM-Series, funded with Software NGFW Credits 

 AIOps for NGFW Premium license (use the Strata Cloud Manager app) 

 Prisma Access license 

 If you select the Global configuration scope, you can view the
 following details: 

 Global folders you create and their variables 

 Firewalls with config conflicts 

 Firewall sync status 

 Firewall connectivity status 

 General information 

 Configuration snippets 

 License 

 Optimize 

 Trusted tenants for snippet sharing 

 Config version snapshots 

 Configuration Overview (Prisma Access) 

 Where Can I Use
 This? What Do I Need? 

 Prisma Access (Managed by Strata Cloud Manager) 

 Prisma Access license 

 If you’re just getting started with Prisma Access: 

 The Basics checklist shows you on how to get up and
 running with Prisma Access; complete the tasks and walkthroughs here to get
 started with a basic setup; then, test your environment and build out your
 deployment. 

 Here’s how policy and configuration folders work . 

 Here’s how
 to push configuration changes to Prisma Access . 

 For details on your Prisma Access environment: 

 Review License details to see what’s included with your Prisma Access
 subscription . 

 The About panel displays the software and tenant information for
 your Prisma Access environment. 

 For day-to-day configuration management: 

 Get at-a-glance configuration status 

 Standardize a common base configuration for a set of Prisma Access deployments
 using the configuration snippets 

 Find configuration
 snapshots —compare configuration versions and restore (or load) an earlier
 version to recover from a configuration push with unintended impact to traffic
 flow or security 

 Optimize
 your configuration by cleaning up unused objects and rules, and
 tightening rules that are introducing security gaps by allowing applications
 you’re not using 

 Pinpoint areas where you can make configuration changes that would strengthen your security posture 

 You can also find details about your Prisma Access license and what it
 includes 

 After completing basic setup, you can start testing your
 environment and building out your deployment. 

 Configuration Overview (Strata Cloud Manager) 

 Where Can I Use
 This? What Do I Need? 

 NGFW (Managed by Strata Cloud Manager) 

 NGFW (Managed by PAN-OS or Panorama) 

 VM-Series, funded with Software NGFW Credits 

 AIOps for NGFW Premium license (use the Strata Cloud Manager app) 

 If you’re just getting started with Cloud Management of NGFW: 

 Here’s how policy and configuration folders work . 

 Here’s how
 to push configuration changes to firewalls . 

 For day-to-day configuration management: 

 Get at-a-glance summary of the current folder name, number of firewalls added to the folder ,
 number of variables created for the folder. 

 Gain visibility and control over local firewall configurations without
 the need for switching between the central management and individual firewalls
 for managing local configurations. 
 Firewalls with config conflicts shows the number
 of firewalls with conflicts. View Conflicts to see conflicts for
 all firewalls and their respective locations. Click the individual
 firewall to further investigate device-level conflicts. 

 Objects with config conflicts shows the number of
 conflicts per firewall. Click the number to view the conflicted objects
 and their corresponding types specific to that firewall. Click the
 object to get the granular details on the conflict. 

 Connectivity Status 
 Review the
 Connectivity Status of managed firewalls
 to Strata Cloud Manager . 

 Sync Status 

 Review the configuration Sync Status between
 Strata Cloud Manager and the current running configuration on
 your managed firewalls. 

 Configuration Snippets 
 Standardize a common base configuration
 for a set of managed firewalls using configuration
 snippets . 

 HA Devices 
 Configure managed firewalls in a high availability (HA) 
 configuration to provide redundancy and ensure business
 continuity. 

 For details on your managed firewalls: 

 Review Content Distribution and
 Software Versions details to
 see which dynamic content
 updates and PAN-OS software versions are
 running on your managed firewalls. 

 Review License details to see
 which licenses are activate on your managed
 firewalls. 

 Previous 

 Configuration: NGFW and Prisma Access 

 Next 

 Configuration: Snippets 

 On This Page 

 Next-Generation Firewalls 

 AIOps for NGFW 

 Cloud Management for NGFWs 

 Cloud NGFW for AWS 

 Cloud NGFW for Azure 

 CN-Series 

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 Service Provider 

 VM-Series 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 AI-Powered ADEM 

 Prisma Access Monitoring and Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

 Cloud-Delivered Security Services 

 Advanced WildFire 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 Device Security 

 Enterprise DLP 

 SaaS Security 

 Network Security 

 Shared Policy for NGFWs and Prisma Access 

 Endpoints 

 GlobalProtect 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Getting Started 

 Strata Cloud Manager 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
