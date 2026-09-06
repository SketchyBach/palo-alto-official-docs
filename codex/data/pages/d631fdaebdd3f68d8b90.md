---
url: https://cortex-docs.paloaltonetworks.com/application-security/code-security/ide/jetbrains/how-to-use-the-jetbrains-cortex-cloud-extension
fetched_at: 2026-09-06T10:13:42Z
source: cortex-platform
---

# How to use the JetBrains Cortex Cloud extension | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center shield-alt

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Application Security 

 Code Security 

 IDE 

 JetBrains 

 How to use the JetBrains Cortex Cloud extension 

 The Cortex Cloud security extension for JetBrains IDEs integrates comprehensive scanning, efficient issue management, and remediation capabilities directly into your coding environment, without disturbing development. 

 Understand the interface 

 The Cortex Cloud plugin presents its results in the Details panel, a tool window docked at the bottom of the JetBrains IDE workspace. The plugin operates alongside the standard JetBrains Project tool window and the Code editor , and all three surfaces are referenced by name throughout this guide. 

 Select the Cortex Cloud icon in the tool window bar at the bottom of the IDE to open the Details panel. 

 Surface 

 Position 

 Function 

 Project tool window 

 Left 

 The standard JetBrains project tree. Navigate the project structure and open a file in the Code editor . Opening a file triggers a single file scan. 

 Code editor 

 Center 

 Displays the codebase, the issues related to resources (for IaC misconfigurations) or files, and the remediation options. 

 Details panel — issue tree 

 Bottom tool window, left section 

 Displays a hierarchical view of folders and files containing issues. Category tabs across the top of the panel group issues by security category, and the folder tree reshapes to the selected category. 

 Details panel — issue detail view 

 Bottom tool window, right section 

 Displays detailed information about a selected issue, including code differences when available, and remediation options. 

 Two navigation paths reach the same issue. The path you take determines what you see first: 

 From the Details panel — Select an issue in the issue tree. The plugin opens the corresponding file in the Code editor and displays the issue details in the right section of the Details panel. Use this path when working a prioritized queue, because the issue tree is filtered and ordered by risk. 

 From the Project tool window — Open a file in the Code editor . Opening the file triggers a single file scan, and the issues detected in that file are marked in the editor. Use this path when working on a specific file, rather than working the queue. 

 Caution: The Project tool window is the standard JetBrains project tree and carries no security indication. A file that contains issues is visually identical to a file that does not. Read the Details panel issue tree, not the Project tool window, to determine where issues exist. 

 Note: The JetBrains plugin consolidates the issue tree and the issue detail view into a single Details panel with two sections. The equivalent surfaces in Visual Studio Code are separate panes. See Understand, prioritize, investigate, and remediate issues in Visual Studio Code. 

 Workflow 

 Stage 

 Decision 

 Primary surface 

 Scan 

 Whether to analyze the whole project or a single file 

 Play button in the Details panel 

 Understand 

 Which security categories carry issues, and how many 

 Category tabs in the Details panel 

 Prioritize 

 Which issue to work on next 

 Severity and Fix Available filters 

 Investigate 

 What the issue is and where the issue lives in the code 

 Issue detail view and the Code editor 

 Remediate 

 Whether to fix, suppress, or consult documentation 

 Fix , Suppress , and Documentation actions 

 Scan 

 Scan your code for security issues using two primary methods: full project scans and single file scans. Select the method by the size of the change under review. 

 Method 

 Trigger 

 Use when 

 Full project scan — automatic 

 Triggered automatically when you open a project 

 Establishing the baseline issue set at the start of a working session 

 Full project scan — manual 

 Initiated by clicking the Play button in the Details panel 

 Re-establishing the baseline after a broad change, such as a dependency upgrade or a merge 

 Single file scan 

 Triggered automatically when you open or save that file 

 Validating a focused edit without re-analyzing the entire project 

 Understand the results 

 The Detail panel's main display features a series of tabs for categorizing issues. Read the tabs before selecting any individual issue — the tab counts describe the distribution of the result set and determine where to commit attention. 

 The Overview tab provides a summary of all detected issues and displays the total count of all issues. 

 Dedicated tabs exist for specific security categories. Issues are organized by security category: IaC , Secrets , Vulnerabilities , Licenses , and Package Operational Risk . 

 Each category-specific tab displays the total count of issues associated with its specific type. 

 The Details panel displays a hierarchical view of folders and files that contain issues, with this display dynamically updated based on the selected issue type tab. Selecting a category tab therefore reshapes the folder tree to the files affected by that category alone. 

 Confirm the scan that produced the result set. Select Scan History in the Details panel to view a record of past scanning activities. For each recorded scan, review the start time and duration of the scan, the path that was scanned, the scan trigger (such as Manual or File Opened ), the total number of issues detected, and the CLI command used to execute the scan. Filters are available within the Scan History to view All Scans , Project Scans , or File Scans . 

 Note: Use the scan trigger and scanned path in Scan History to confirm that the result set covers the code under review. A single file scan reports issues only for the file that was opened or saved. 

 Prioritize 

 Two filters narrow the result set into a work queue. Apply both — severity establishes the order of risk, and fix availability establishes the order of throughput. 

 Filter 

 Control 

 Use when 

 Severity level 

 L M H C 

 Ordering the queue by risk. Start at C and work down. 

 Fix availability 

 Fix Available 

 Maximizing issues resolved per unit of effort. Isolates the issues that carry a suggested fix. 

 Note: After selecting Fix Available , the number of issues displayed in the issue categories (such as IaC ) reflect the number of fixable issues for that type. The category counts therefore change meaning once the filter is applied — read the counts as fixable issues, not total issues. 

 Sequence the queue. Filter to the highest severity first, then apply Fix Available within that severity to clear the issues with a suggested fix. Return to the remaining issues at that severity, which require a manual decision — suppression or documentation-guided mitigation. 

 Investigate 

 An issue count tells you that risk exists. Investigation establishes what the issue is and where the issue lives in the code, which determines the remediation path. 

 Open the issue. 

 Under a scan category, browse through folders/subfolders to locate and click on a file containing issues. 

 (Optional) Use a filter to prioritize issues. 

 Select an individual issue within the file to display its details in the right section of the Details panel. 

 The corresponding file simultaneously opens in the Code editor , highlighting the issue within its exact code context. 

 Read the issue detail view. The detailed issue view provides: 

 The name and description of the issue. 

 The code lines (or resource for IaC misconfigurations) in which the issue has been detected. 

 Contextual remediation options, provided specifically for each issue type to guide resolution. 

 Read the issue in the Code editor. Issues are marked by a red i icon next to the code line. 

 Click the red i icon for basic details about an issue: name, severity, and remediation options. 

 For IaC resources with multiple issues, hovering over the line of code marked i displays a list of issues at the resource's starting line. Scroll to view all issues. 

 Select Console to display the issue in the Details panel. 

 Important: For an IaC resource, the count of issues at the resource's starting line determines the remediation effort. A single configuration block carrying several misconfigurations is one edit against several issues — inspect the full hovered list before applying any fix. 

 Remediate 

 Mitigate issues directly through both the Code editor or the Details panel. Options include Fix , Suppress , and Documentation . 

 Path 

 Use when 

 Fix 

 A suggested fix is displayed for the issue. The fastest path — the fix is applied to the code on selection. 

 Suppress 

 No fix is available, or the issue is not the current priority, and the issue is an accepted risk for the file. 

 Documentation 

 No automated fix is available and the mitigation approach is unclear. 

 Note: Not all types of remediation are available for all issue categories. For example, fixes are not available for License issues. 

 Apply a fix 

 When selecting an issue in either the Code editor and Details panel, a suggested fix is displayed when available. Fixes are automatically applied to the code upon selection. 

 Issue category 

 Fix behavior 

 CVE vulnerabilities 

 The fix bumps the package version. Fix the specific CVE vulnerability detected during the scan by upgrading the package to the version that includes a fix 

 IaC misconfigurations 

 The fix modifies the configuration. The Details panel displays the code difference to be fixed 

 Secrets issues 

 No fix available. For rotation guidance, see Secrets issues 

 License mis-compliance 

 No fix available. For handling guidance, see License compliance issues 

 Package Integrity 

 No fix available 

 Suppress an issue 

 Suppress an issue to temporarily hide or ignore an issue without fixing it, allowing you to concentrate on more important issues. The suppression is scoped to the file. 

 Select an issue from the Details panel → click Suppress in either the Code editor or Details panel. 

 Provide a justification for the suppression → click OK . 

 The justification will be added as a commented annotation to your source code. Write the justification for a reviewer, not for yourself — the annotation is committed with the code and is the only record of the risk-acceptance decision. 

 Caution: After suppressing an issue, the file will not be scanned for two minutes. This is to prevent the issue from being re-triggered. Saving the file during the hold period will not trigger a scan. Wait out the hold period before treating a subsequent clean save as verification. 

 For information on developer suppression refer to Developer suppressions . 

 Consult the documentation 

 If automated fixes are not available, policy documentation can provide guidance on how to address the issue. Select an issue → click Documentation in either the Code editor or Details panel. You are redirected to the relevant documentation which includes suggested guidelines on how to mitigate the issue. 

 Plugin actions 

 The Details panel carries the plugin actions. These actions run the scan and diagnose a scan that behaved unexpectedly. Every action operates on the plugin as a whole, not on an individual issue. 

 Action 

 Use when 

 Play 

 Running a full project scan across all security categories. 

 Scan History 

 Confirming what a previous scan actually covered, or reproducing a scan outside the IDE. 

 Log file 

 Diagnosing a scan that failed, produced no results, or behaved unexpectedly. 

 Manage plugin settings 

 The JetBrains plugin settings are located in the IDE settings rather than in the Details panel: Navigate to File → Settings → Tools → Cortex Cloud and manage the extension settings. 

 When a scan result is unreliable 

 A scan that reports no issues is not evidence of clean code until the scan itself is confirmed. 

 Open Scan History in the Details panel and confirm the scanned path and the scan trigger match the code under review. 

 Select the Log file icon, next to the Play button in the Details panel, to view log files. These logs provide diagnostic information and details about the execution of your scans, which can be useful for troubleshooting. 

 Re-run the scan by clicking the Play button, and compare the new record in Scan History against the previous record. 

 If the re-run produces an identical result, identify the cause. 

 Under scan history, you can also run scans locally from the terminal for support purposes and so on. The CLI command recorded for each scan reproduces that scan outside the IDE. 

 Previous JetBrains 

 Next Developer suppressions 

 Last updated 26 days ago 

 Was this helpful?
