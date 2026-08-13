---
url: https://docs.paloaltonetworks.com/strata-cloud-manager/activation-and-onboarding/onboard-to-strata-cloud-manager/onboard-ngfws-with-site-management
fetched_at: 2026-08-13T17:37:04Z
source: palo-alto-main
---

# Onboard NGFWs with Site Management Clear

Onboard NGFWs with Site Management 

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

 Onboard NGFWs with Site Management 

 Updated on 

 Fri Jul 24 11:47:30 PDT 2026 

 Focus 

 Download PDF 

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

 Fri Jul 24 11:47:30 PDT 2026 

 Focus 

 Home 

 Strata Cloud Manager 

 Strata Cloud Manager Activation & Onboarding 

 Onboard to Strata Cloud Manager 

 Onboard NGFWs with Site Management 

 Download PDF 

 Strata Cloud Manager 

 Onboard NGFWs with Site Management 

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

 Onboard to Strata Cloud Manager 

 Next 

 Onboard NGFWs using Zero Touch Provisioning (ZTP) 

 Onboard NGFWs with Site Management 

 Automate NGFW configuration variable resolution during onboarding using Site
 Management in Strata Cloud Manager . 

 Where Can I Use This? What Do I Need? 

 NGFW 

 Contact your account representative if you are interested in
 enabling this feature. 

 One of these licenses: 

 Strata Cloud Manager Essentials 

 Strata Cloud Manager Pro 

 Roles needed: 

 Network Administrator 

 Superuser 

 Business Admin 

 Site Management in Strata Cloud Manager streamlines Next-Generation Firewall (NGFW)
 deployment by automating configuration variable resolution. This feature introduces a
 "Site" as a core entity for NGFW deployment, abstracting device complexity in your
 environment. You define reusable properties and rules to generate specific variable
 values for individual devices, eliminating manual operations and standardizing your
 provisioning process. 

 Site Management improves NGFW deployments by ensuring consistency and reducing errors,
 especially at scale. Previously, configuring settings like IP addresses or hostnames
 manually for each device often caused inconsistencies and increased administrative
 effort. Site Management automates these calculations and standardizes value generation
 across NGFWs, reducing configuration drift and enhancing scalability for large
 deployments. 

 Site Management operates by centralizing your configurations. You define
 Properties — customer-defined metadata consisting of user-specified keys and values
 that describe each site's unique characteristics (such as location, region, or site
 ID) — and assign specific property values to individual Sites. These site-specific
 values are then used by Onboarding Rules, which contain Variable Resolution Rules.
 The Site Manager component dynamically calculates complex configuration details,
 such as derived IP addresses or hostnames, by substituting variables with site
 property values. 

 The workflow begins when you define Properties, Site Properties Groups, Sites, and
 Onboarding Rules within Strata Cloud Manager . An installer then selects a target
 site while installing the NGFWs. Strata Cloud Manager resolves the configuration in
 accordance with the variable resolution rules defined by the admin. This process
 includes Onboarding Properties as customizable metadata and Variable Resolution Rules
 that support string substitution and bit operations for precise IPv4 address
 generation. A Claim process then ties a physical or virtual NGFW to a
 pre-configured Site, triggering automated variable resolution and provisioning
 through Strata Cloud Manager . 

 This feature is only available during the onboarding of NGFWs. 

 This feature exclusively supports IPv4 for all IP address fields,
 variables, and resolution rules; IPv6 is not supported. 

 A site is restricted to being claimed by one single device. 

 Define Site Properties. 

 Log in to 
 Strata Cloud Manager . 

 Navigate to Configuration NGFW and Prisma Access , set the Configuration Scope to
 All Firewalls , and continue to Setup Device Onboarding Site Management Site Properties . 

 Add Property . 

 Properties are defined at the tenant level. 

 Enter a unique Name for the property, for
 example, region_id or
 location . 

 Select the Type for the property and configure
 the type-specific constraints. 

 String —Enter a Maximum
 Length , for example,
 1024 . 

 Integer —Enter a
 Minimum and
 Maximum value, for example,
 0 to 7 . 

 Save . 

 Create Site Property Groups. 

 Site Groups are a collection of Sites with similar properties. 

 Navigate to Configuration NGFW and Prisma Access , set the Configuration Scope to
 All Firewalls , and continue to Setup Device Onboarding Site Management Site Property Groups . 

 Add Site Properties Group . 

 Enter a Name for the site group, for example,
 Branch Deployments . 

 Define and associate the properties that belong to this group. 

 Save . 

 Create Sites. 

 Navigate to Configuration NGFW and Prisma Access , set the Configuration Scope to
 All Firewalls , and continue to Setup Device Onboarding Site Management Sites . 

 Add Site . 

 Select the Site Group this site belongs to, for
 example, Branch Deployments . 

 Enter a unique Name for the site, for example,
 sc-store-1 . 

 ( Optional ) Enter the physical Address 
 for the site. 

 Provide Property Values for each property
 defined in the selected Site Group, for example,
 region_id: 7 . 

 ( Optional ) To add multiple sites at once, select the
 Site Properties Group created in Step 2 and
 choose to either manually add sites in a grid or Import
 CSV . 

 Save . 

 Configure Site-Based Onboarding Rules. 

 Navigate to Configuration NGFW and Prisma Access , set the Configuration Scope to
 All Firewalls , and continue to Setup Device Onboarding Onboarding Rules . 

 Add Rule and configure the general
 settings. 

 Enter a descriptive Name for the rule
 and optionally a Description . 

 Ensure the Enabled toggle is
 active. 

 Select Site-Based as the
 Onboarding Type . 

 Configure the Match Criteria . 

 Select the Site Properties Group from
 Step 2 that this rule will apply to, for example,
 Branch Deployments . 

 ( Optional ) Specify
 Models . 

 Configure the Actions . 

 Select Target Folder . 

 Select any Snippet Association . 

 Select the Target OS Version for the
 device. 

 ( Optional ) Enable VPN
 Onboarding . 

 ( Optional ) Enable Custom
 Interface . 

 Custom Interface
 is disabled by default. When enabled, it disables the
 automatic application of the ZTP Default Snippet
 post-bootstrap, allowing administrator-defined interface and
 routing configurations to take effect. Use this option only
 when the management interface or non-standard ports are
 required for post-onboarding connectivity. Ensure all
 necessary interface and routing configurations are defined
 before enabling this option to prevent connectivity
 interruptions. 

 ( Optional ) Enable User Context
 Onboarding . 

 Enable Variable Resolution and configure
 variables. 

 Only variables defined at the folder selected in
 Target Folder or defined in an associated
 snippet will be available for resolution. 

 For each variable you want to override: 

 Select the variable Name , for example,
 mgmt_ip . 

 Choose the appropriate Resolution Rule
 Type : 

 Replacement —Enter an
 Expression using site
 properties, for example,
 10.1.${region_id}.2 . 

 Bitwise Expression —Define the
 bitwise resolution to dynamically generate an IP
 address for each site. This option provides the
 flexibility to dynamically configure every bit of the
 IP address and use properties to resolve the IP
 address for every site. 

 Save . 

 Preview Site Resolution. 

 To prevent potential runtime errors from inconsistent variable resolution, you
 can preview how variables will resolve for your sites before
 deployment. 

 Navigate to Configuration NGFW and Prisma Access , set the Configuration Scope to
 All Firewalls , and continue to Setup Device Onboarding Site Management Sites . 

 Preview Resolution . 

 ( Optional ) Select the Model
 Family . 

 Review the Resolved Onboarding Rule and
 Resolved Variables for each site. 

 Claim a Site during device onboarding. 

 Initiate the NGFW device onboarding process using Zero Touch Provisioning (ZTP) or manual onboarding . 

 On the ZTP activation page or Strata Cloud Manager onboarding page,
 enter the device's Serial Number and
 Claim Key . 

 Select a pre-defined Onboarding (Site) from the
 available list. 

 A site can only be claimed by one device
 at a time. 

 If you are using the ZTP mobile web
 app , location detection automatically populates sites
 within a 2 km radius of your current position. You can tap
 Tap to change location to update your
 location or toggle Show All Sites to browse
 the complete list of available sites. 

 Submit . 

 Verify Onboarding Status and Resolved Variables. 

 Navigate to Settings Device Management . 

 Locate the newly onboarded device. 

 Review the Onboarding Status . 

 Select the device and navigate to its specific Configuration
 Scope . 

 Manage Variables . 

 Review the Resolved Variables . 

 Previous 

 Onboard to Strata Cloud Manager 

 Next 

 Onboard NGFWs using Zero Touch Provisioning (ZTP) 

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

 Cloud Management of NGFWs 

 Activation & Onboarding 

 Next-Generation Firewall 

 Management 

 Feature Category 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
