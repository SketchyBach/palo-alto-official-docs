---
url: https://docs.paloaltonetworks.com/enterprise-dlp/administration/configure-enterprise-dlp/enterprise-dlp-migrator
fetched_at: 2026-08-13T15:32:17Z
source: palo-alto-main
---

# Enterprise DLP Migrator Clear

Enterprise DLP Migrator 

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

 Enterprise DLP Migrator 

 Updated on 

 Fri Jul 10 12:56:22 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Enterprise DLP Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Reference 

 Release Notes 

 New Features by OS Version 

 New Features by Month 

 Updated on 

 Fri Jul 10 12:56:22 PDT 2026 

 Focus 

 Home 

 Enterprise DLP 

 Administration 

 Configure Enterprise DLP 

 Enterprise DLP Migrator 

 Download PDF 

 Enterprise DLP 

 Enterprise DLP Migrator 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Enterprise DLP Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Reference 

 Release Notes 

 New Features by OS Version 

 New Features by Month 

 Previous 

 Recommendations for Security Policy Rules 

 Next 

 Configuration Export and Import 

 Enterprise DLP Migrator 

 Migrate your existing data loss prevention policy rules from your old data loss
 prevention service provider to Enterprise Data Loss Prevention (E-DLP) . 

 On May 7, 2025 , Palo Alto Networks is introducing new Evidence Storage and Syslog Forwarding service IP
 addresses to improve performance and expand availability for these services
 globally. 

 You must allow these new service IP addresses on your network
 to avoid disruptions for these services. Review the Enterprise DLP 
 Release Notes for more
 information. 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by Strata Cloud Manager) 

 Prisma Access (Managed by Strata Cloud Manager) 

 Prisma Browser 

 Enterprise Data Loss Prevention (E-DLP) license 

 Review the Supported
 Platforms for details on the required license
 for each enforcement point. 

 Or any of the following licenses that include the Enterprise DLP license 

 Prisma Access CASB license 

 Next-Generation
CASB for Prisma Access and NGFW (CASB-X) license 

 Data Security license 

 Use the Enterprise Data Loss Prevention (E-DLP) Migrator to migrate your Symantec DLP policy rules
 and convert them into SaaS Security Data Asset policy rules. This allows
 you to quickly transition to Palo Alto Networks Enterprise DLP without the need
 to manually recreate all your Data Asset policy rules designed to prevent
 exfiltration of sensitive data. 

 To migrate your existing Symantec DLP policy rules, you simply need to export them
 from Symantec DLP and import them into the Enterprise DLP migration tool. The
 Enterprise DLP migration tool then evaluates the imported Security policy
 rules to verify that they are compatible with Enterprise DLP and SaaS Security . Enterprise DLP creates a data pattern and a classic
 data profile with names identical to the migrated Symantec DLP policy rule as part
 of the migration to capture the traffic match criteria. 

 If Enterprise DLP detects an incompatible Security policy rule traffic match
 criteria, you can choose to delete the incompatible match criteria from the Symantec
 DLP policy rule before the migration begins or choose to exclude that specific
 Symantec DLP policy from migration. Enterprise DLP adds a successfully migrated
 Symantec DLP policy rule as a Disabled 
 SaaS Security Data Asset policy rule. You can then review the Data Asset
 policy rule, make changes if needed, and enable the policy rule. 

 Enterprise DLP supports migration of Symantec DLP policy rules in
 .xml format and with one or more of the following
 match criteria: 

 Regular expressions —A customized expression 
 that defines a specific text pattern to inspect for and block. 

 Keywords —Specific words specified to improve detection accuracy and
 reduce false positives. Referred to as Proximity Keywords in Enterprise DLP . 

 Data Identifiers —The data match criteria added to a Symantec DLP
 policy rule Referred to as a data pattern in Enterprise DLP . 

 Response Action — Enterprise DLP supports one Response Action per
 Symantec DLP policy rule. Enterprise DLP applies the highest priority
 Response Action if it detects a Symantec DLP policy rule with more than one
 Response Action. 

 The priority list of Symantec DLP Response Actions is: 

 Quarantine 

 Remove Collaboration Action and Remove Collaboration Link 

 In SaaS Security , the Change Sharing 
 Action in a Data Asset policy rule 
 allows you to remove collaborators and links using one Data
 Asset policy rule. 

 Notify Owner 

 Export your existing Symantec DLP policy rules in
 .xml format. 

 Log in to Strata Cloud Manager . 

 Select Configuration SaaS Security Settings All Settings DLP Migration Assistant . 

 Upload the Symantec DLP policy rules to the Enterprise DLP Migrator. 

 Enter a descriptive Migration Name for the
 Symantec DLP policy rule migration. 

 In the Upload XML Files section, drag and drop
 the Symantec DLP policy rules files in .xml 
 format. 

 Import the XML files you uploaded to the Enterprise DLP Migrator. 

 Enterprise DLP begins to import and analyze your uploaded policy rules
 to verify compatibility. Continue to the next step once the import status
 reaches 100% . 

 Review your uploaded policy rules. 

 Enterprise DLP lists the number of compatible, partially compatible, and
 incompatible policy rules from the total number of policy rules uploaded in
 the previous step. 

 Compatible —Policy rule is compatible with Enterprise DLP 
 and is ready for migration. No further review required to prepare
 the policy rule for migration to Enterprise DLP . 

 Partially Compatible —Policy rule contains one or more traffic
 match criteria that are incompatible with Enterprise DLP .
 Review and delete the incompatible traffic match conditions before
 you can migrate the policy rule to Enterprise DLP . 

 Incompatible —All traffic match criteria in the policy rule are
 incompatible with Enterprise DLP . You can't migrate an
 incompatible Symantec DLP policy rule to Enterprise DLP . 

 The Notes column displays the specific issue causing
 the traffic match incompatibility with Enterprise DLP . 

 Review and address your Partially Compatible policy
 rules. 

 Skip this step if you want to only migrate Compatible 
 rules and don't want to migrate any Partially
 Compatible policy rules. 

 You can also select multiple Partially Compatible 
 policy rules to review. If you select multiple policy rules, you must
 switch between them to address each policy rule individually. 

 Enterprise DLP Migrator does not support turning an
 Incompatible policy rule into a
 Compatible policy rule. 

 Below is an example of Partially Compatible Symantec
 DLP policy rules an admin might need review before migration to Enterprise DLP . 

 Select one or more Partially Compatible policy
 rules you want to review. 

 Review Selected . 

 Select the Incompatible traffic match criteria
 and Delete . 

 When prompted, confirm you want to Delete the
 selected incompatible traffic match criteria. 

 If you selected multiple policy rules, use the navigation arrows in
 the top-right corner of the Review Policy 
 page and repeat this step until you delete all incompatible traffic
 match criteria. 

 After you delete all incompatible traffic match criteria from the
 selected Partially Compatible policy rules,
 click the X in the top-right corner to
 continue migration to Enterprise DLP . 

 The policy rules now show that they are
 Compatible and Ready to
 Migrate . 

 Migrate one or more policy rules to Enterprise DLP . 

 In the Review Policies page, select one or more
 policy rules and Migrate to PANW . 

 Enterprise DLP displays a verification window detailing the number
 of Compatible policy rules selected for
 migration. 

 Additionally, you can specify whether these policy rules are
 automatically Enabled after successful
 migration. By default, all migrated policy rules are
 Disabled . 

 Migrate the selected policy rules. 

 A progress bar displays the current policy rule migration
 progress. 

 Enterprise DLP displays a summary of the successfully migrated policy
 rules. 

 Additionally, you can: 

 Export PDF —Export a PDF file of the policy
 rules you migrated to Enterprise DLP . You download the PDF to
 your local device. 

 Migration History —Redirected to the view the
 history of all previous successful policy rule migrations. 

 View Policies —Redirected to view your migrated
 policy rules in the SaaS Security 
 Data Asset Policies to review and enable. 

 Click View Policies to continue to the next step. 

 Review and enable your migrated policy rules. 

 After a successful policy rule migration, click View
 Policies or select Configuration SaaS Security Data Security Policies Data Asset Policies . 

 If you manually navigated to the SaaS Security 
 Data Asset Policies , you also need to
 apply the Status: Disabled filter. 

 Click the Policy Name to review the traffic
 match criteria and verify Enterprise DLP successfully migrated the
 policy rule. 

 The Data Asset policy rule name is the same as the Symantec DLP
 policy rule XML file name you uploaded in the previous step. Enterprise DLP automatically populates the following Data Asset
 policy rule settings: 

 Description —Original Symantec DLP
 policy rule honored during migration and applied to the new
 Data Asset policy rule to preserve any important information
 and descriptions about the policy rule. 

 Data Profile — Enterprise DLP 
 enables the Data Pattern/Profile 
 match criteria and attaches the Data
 Profile created during the migration that
 contains all the traffic match criteria to the Data Asset
 policy rule. 

 Action —The SaaS Security 
 equivalent of the Response Action from the Symantec DLP
 policy rule. 

 You can edit the migrated Data Asset policy rule Policy
 Name or make any other changes as needed from this
 page. Click Save if you made any changes or
 Cancel if you reviewed the migrated
 policy rule match criteria and confirmed you don't need to make any
 changes. 

 Expand the Action column and
 Enable the policy rule. 

 Apply the Status: Enabled filter and order your
 policy rule as needed. 

 Refer to the Recommendations for Security Policy Rules for more
 information on how to order your policy rules in your policy
 rulebase. 

 Repeat this step for all migrated policy rules. 

 Previous 

 Recommendations for Security Policy Rules 

 Next 

 Configuration Export and Import 

 On This Page 

 Activation & Onboarding 

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

 SaaS Security 

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

 Administration 

 Cloud-Delivered Security Services 

 Data Filtering 

 Enterprise DLP 

 Task 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
