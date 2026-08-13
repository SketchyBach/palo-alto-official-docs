---
url: https://docs.paloaltonetworks.com/prisma-access-browser/administration/the-prisma-access-browser-extension/prisma-browser-extension-best-practices
fetched_at: 2026-08-13T17:23:29Z
source: palo-alto-main
---

# Prisma Browser Extension - Best Practices Clear

Prisma Browser Extension - Best Practices 

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

 Prisma Browser Extension - Best Practices 

 Updated on 

 Jul 28, 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Browser Docs 

 Activation & Onboarding 

 Getting Started 

 Deployment 

 Administration 

 Integrations 

 User Guide 

 Updated on 

 Jul 28, 2026 

 Focus 

 Home 

 Prisma Browser 

 Prisma Access Browser Administration 

 The Prisma Browser Extension 

 Prisma Browser Extension - Best Practices 

 Download PDF 

 Prisma Browser 

 Prisma Browser Extension - Best Practices 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Browser Docs 

 Activation & Onboarding 

 Getting Started 

 Deployment 

 Administration 

 Integrations 

 User Guide 

 Previous 

 Prisma Browser Extension Bulk Extension ID Import 

 Next 

 File Types per Category 

 Prisma Browser Extension - Best Practices 

 The definitivve best proactices guide 

 Starting Point - Choose Your Baseline 

 Before creating any specific rules, we recommend that you decide the
 organizational posture that best fits your needs. This choice changes how subsequent
 security filters (like Block by Permission ) behave. 

 Block-First Strategy (Recommended for High Security): Start with a
 Block All rule, then. You then explicitly grant exceptions via an
 Allow List . This is the most restrictive and secure approach. 

 Allow-First Strategy (Recommended for User Flexibility): Start with an
 Allow All rule,. You then layer Block by Risk or specific
 Block Lists to remove dangerous items. 

 Core Mental Model - The Two Stage Resolution 

 Policies are applied in two separate and distinct stages: 
 Stage 1: Identity Resolution (The Stack): The system resolves the
 extension's status based on its specific ID or broad type (Allow All, Block
 All, Allow List, or Block List). 

 Stage 2: The Security Vetoes: Once the identity is resolved, the
 system applies the "Security Filters" ( Block by Risk and Block by
 Permission ) and the "Operational Mandate" ( Force
 Install ). 

 Stage 1: Identity and Risk (The Policy Stack) 

 Rules are processed from the Bottom (lowest priority) to the Top 
 (Highest Priority). 

 A. The "Set Subtraction" Logic 

 When specific lists conflict, they modify the set of allowed extensions through
 mathematical subtraction: 

 Starting Rule Higher Priority Rule Resulting Logic Real-Life Example 

 Allow List (Set A) Block List (Set B) Allow List (A minus B): The Block List removes its
 items from the allowed set. Scenario : You allow 3 productivity extensions (A, B,
 C). A new security policy blocks extension B. Result :
 Only A and C remain allowed. 

 Block List (Set B) Allow List (Set C) Block List (B minus C): The Allow List creates
 exceptions, removing its items from the blocked set. Scenario : You block all File Sharing extensions(X, Y).
 Finance specifically needs App X. Result : App Y remains
 blocked, but App X is now an exception and allowed. 

 B, Integrating Block by Risk 

 Block by Risk acts as a filter that sits on top of the
 Identity resolution: 
 The Filter Rule: If an extension is 'Allowed' by its identity
 in Stage 1, the system checks for any active Block by Risk 
 rules. If the extension matches the risk level defined in the
 highest-priority rule, it is Blocked . 

 The Escape Hatch: A high-priority Allow List / Allow by
 ID rule is the only way to "rescue" a specific extension
 that has been caught by a broad Block by Risk policy. 

 Feature Mechanism Real-Life Example 

 The Filter Rule Block by Risk acts as a security gate for
 extensions allowed by the stack. 
 Scenario: You have a
 Block-First strategy. You add a
 Translation App to your Allow List .
 (in higher priority) However, the app is later
 flagged as High Risk (in higher priority)
 because of excessive data collection. 

 Final structure: High risk rule on top
 of allow list on top of block
 all 
 Result: The extension is
 Blocked because the Risk Rule (Stage 2)
 overrides the Allow List (Stage 1). 

 The Escape Hatch A high-priority Allow List rule can
 specifically "rescue" a risky extension. 
 Scenario: You have a broad policy
 to Block High Risk extensions. Your
 developers need a specific Debugging Tool 
 that is flagged as High Risk due to its deep browser
 access. 
 Result: You place the Debugging
 Tool ID on an Allow List with a higher
 priority than the Risk rule. The tool is
 Installed , effectively bypassing the broad
 risk block for that specific case. 

 Stage 2: The High Priority Vetoes 

 These rules generally sit outside the standard Stack and can override the results of
 Stage 1. 

 A. Force Install: The operational mandate: 

 Force Install ensures an extension is present and enabled,
 regardless of most blocking rules: 

 Force Install vs. Block All: 
 Force Install Wins. 

 Force Install vs. Block by Permission: 
 Force Install Wins. 

 Force Install vs. Block by Risk: Force Install
 Wins 

 Force Install vs. Block List: 
 Block List Wins (Critical Deviation). An explicit ID-based
 block removes even a Force Installed extension. When the Block List
 rule is removed, the extension is re-installed. 

 When Force Install meets... The Winner is... Real-Life Example 

 A "Block All" Strategy Force Install 
 Scenario: You have a strict "Default
 Deny" policy that blocks all extensions. However, you
 Force Install the corporate password
 manager. 
 Result: The password manager stays
 installed and working, even though everything else is
 blocked. 

 A "Block by Permission" Security Gate Force Install 
 Scenario: You block all extensions that
 request "Access to all websites" for security. You then
 Force Install a security agent that needs that
 exact permission. 
 Result: The security agent
 bypasses the gate and stays active. 

 A specific "Block List" Rule Block List (The Exception) 
 Scenario: You Force Install a
 specific browser Extension. Later, you discover a bug and
 add that Extension ID to a Block List to stop its
 use. 
 Result: The Block List rule "wins" and
 removes the extension. If you later delete that Block List rule,
 the extension will automatically re-install. 

 Force Install meets Block by Risk Force Install The extension remains active regardless of its risk
 score. 

 Known Limitation: Identity-based Blocking with Force Install 

 Current Behavior: There is a known limitation regarding the "Kill
 Switch" functionality when using a Block All strategy alongside Force
 Install mandates. Currently, if a global Block All rule is active, a
 specific Block List (Identity-based block) may fail to remove an extension
 that is also present in a Force Install policy. 

 Impact: In this specific configuration, the Force Install 
 mandate maintains the highest authority, preventing the surgical removal of a forced
 extension via its specific ID. Broad security filters, such as Block by
 Permission and Block by Risk , also remain bypassed by the Force
 Install mandate as intended. 

 Workaround: You can To successfully remove or disable a Force Installed 
 extension while this limitation exists; You need to manually remove the extension's
 ID from the Force Install policy list. 

 B. Block By Permission: The Security Veto 

 The Power of the Block by Permission rule depends son the initial strategy selected
 in Section I: 

 Strategy Rule Precedence Functional Impact Real-Life Example 

 Block-First Strategy Allow List Wins Extensions specifically allowed via an Allow List bypass the
 Block by Permission check. 
 Scenario: You block all extensions by
 default. To be extra safe, you also block the "Access to all
 website data" permission. Your Finance team needs a specific
 Legacy Reporting Tool that requires that exact
 permission. 
 Result: You add the tool’s ID to your
 Allow List . The extension installs and runs .
 The system assumes that because you manually vetted it in a
 strict environment, you trust its permissions. 

 Allow-First Strategy Block by Permission Wins. Block by Permission acts as a final gate and disables
 extensions even if they are on an Allow List. 
 Scenario: You allow all extensions by
 default. To prevent data theft, you set a Block by
 Permission for "Access to File System". A user wants
 to install a Photo Editor that is on your "Approved
 Apps" Allow List but requires that forbidden
 permission. 
 Result: The Block by Permission
 rule wins . The extension is disabled . The system
 treats the permission block as a "final safety gate" because
 your overall environment is permissive. 

 Notes on Block by Permission Behavior: 
 If a forbidden permission required , the extension is
 disabled . 

 If a forbidden permission is optional , the extension runs but the
 permission is revoked . 

 Summary Precedence Matrix (Final Lookup) 

 Policy A (Lower Priority) Policy B (Higher Priority) Result Reasoning 

 Block All Allow All Allow List Standard exception handling 

 Allow All Block by Risk Risk Filtered Block by Risk restricts the permissive Allow AI baseline 

 Block by Risk Allow List Allow List Wins Allow List "rescues an extension from a risk block 

 Force Install Block List Removed Deviation: Specific block removes thhe forced install 

 Block by Permission Force Install Installed Force Install is the highest authority over Permission
 Blocks 

 Block by Permission Allow List Varies Allow List wins in Block-First; Block by Permission wins in
 Allow-First. 

 Block by Risk Force Install Force Install Wins An operational mandate to install an extension ignores automated
 risk filters. 

 Frequently Asked Questions 

 What is the difference between "Block-First" and "Allow-First"
 strategies? 
 Block-First (Default Deny): You start by blocking all extensions
 and then create specific "Allow List" exceptions. This is the most
 secure posture and changes how security gates (like permissions)
 behave. 

 Allow-First (Default Permit): You allow all extensions by default
 and use "Block by Risk" or "Block Lists" to filter out the bad ones.
 This is more flexible but requires stronger automated security
 gates. 

 Why is my "Force Installed" extension being removed? 
 The Specificity Rule: While Force Install is a high-authority
 mandate, an explicit Block List rule for that specific extension
 ID will remove it. 

 Self-Healing: If you remove the ID from the Block List, the
 extension will automatically re-install because the Force Install
 mandate is still active. 

 How does "Block by Permission" actually affect the extension? 
 It
 depends on how the extension was coded by the developer. 
 Mandatory Permissions: If you block a permission the
 extension requires to function, the extension is
 Disabled . 

 Optional Permissions: If you block an optional 
 permission, the extension stays Enabled , but that specific
 feature is Revoked and will not work. 

 Can I allow an extension that is flagged as "High Risk"? 
 Yes (The
 Escape Hatch): You can "rescue" a specific extension by adding its
 ID to an Allow List with a higher priority than your Block by Risk
 rule. This allows you to manually vet and approve a tool that the system
 would otherwise block. 

 Why did my Allow List override the Permission Block in one group but not the
 other? 

 It depends on your strategy: 
 In a Block-First setup, an Allow List is treated as a
 manual administrative vetting and Wins over permission
 blocks. 

 In an Allow-First setup, the Block by Permission gate
 is treated as a final safety net and Wins over the Allow
 List. 

 What happens if I have an Allow List and a Block List for the same IDs?

 Identity Subtraction: The system uses "Set Subtraction." A
 higher-priority Block List will "carve out" its items from a lower-priority
 Allow List. 
 Example: If you allow "Tools A, B, and C" but block "Tool B"
 at a higher priority, only A and C remain allowed. 

 Does Force Install bypass the "Block by Permission" gate? 

 Yes: An operational Force Install mandate is considered a
 higher authority than a security permission gate. If you force an extension,
 the system assumes you have already reviewed and accepted its
 permissions. 

 Previous 

 Prisma Browser Extension Bulk Extension ID Import 

 Next 

 File Types per Category 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Cloud Identity Engine 

 Strata Logging Service 

 Device Associations 

 Hub 

 Identity and Access Management 

 Tenant Management 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 AI-Powered ADEM 

 Prisma Access Monitoring and Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

 Remote Browser Isolation 

 Prisma Browser 

 Administration 

 Prisma Access 

 Strata Cloud Manager 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
