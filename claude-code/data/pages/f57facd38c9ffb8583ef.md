---
url: https://docs.prismacloud.io/content-collections/application-security/risk-management/monitor-and-manage-code-build/fix-code-issues
fetched_at: 2026-09-16T13:35:45Z
source: prisma-cloud
---

# Fix Code Issues | Prisma Cloud arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Enterprise Edition 

 Content Collections 

 Application Security 

 Risk Management 

 Monitor and Manage Code Build Issues 

 Fix Code Issues 

 On Projects , you can remediate scan results across all code categories by adding issues to the fix cart to create a Pull Request (PR) with a suggested fix. For every issue found on Prisma Cloud console, you can view information like origin of the issue in a file or repository, policy violation, and suggestions to remediate the issue. 

 Access scan results on Projects . 

 Select a code category with an issue. 

 Select an issue from the resource block to view more information and suggested fixes in the resource explorer. 

 Create a PR from the fix recommendation. 

 Select an issue to see the fix recommendation in the resource explorer. 

 You can fix one more issues at once by selecting issues across multiple resources or policy blocks and adding it to the fix cart. 

 Select FIX to add an issue to the fix cart. 

 Select Submit in the 'Resource Explorer' to create a PR with an issue fix. 

 The Naming Method popup is displayed, offering two options: automated values as provided by by Prisma Cloud, and the option to customize your PR title and branch name. 

 Optional : Customize your Pull Request and Branch names. 

 Prerequisite: Enable customization by selecting Application Security in the left sidebar under 'Configure' > scroll down and enable the Modify Fix Pull Request (PR) Title and Branch Name feature. 

 Administrator privileges are required to enable this setting. 

 Return to step 2.3 above and select Use custom Pull Request title and branch name . 

 Enter a PR title in the Pull Request field 

 Enter a branch name in the Branch Name field (Optional) 

 Select Submit . 

 A Success message popup confirms that the PR has been successfully opened. 

 Click on a link in the popup or access the PR on your VCS console to view the PR. 

 If configured, your custom title is displayed in the PR. 

 For issues with no fix recommendation, you can remediate it by a Manual Fix or Suppress . 

 Fix Vulnerability Issues 

 On Projects Vulnerabilities view you see CVE issues that have an automatic fix on the console. You can choose to remediate a single CVE issue or choose to fix all issues in the issue block. When fixing the issue, the CVE Root version gets bumped to the latest version from a Pull Request that you need to submit from the Fix cart . The issue block will continue to be seen till the Pull Request with the fix is not merged. 

 Select Application Security > Projects and then select Vulnerabilities view. 

 Access any issue block and then select Fix corresponding to the issue. 

 Optionally, you can select Fix All . 

 When fixing the issue, you can verify all CVE’s getting fixed by a verification status corresponding to the CVE. 

 Select Submit on the side panel to create a Pull Request (PR) with the fixes. 

 Manual Fix an issue 

 You can perform a manual fix for all issues. A manual fix enables you to access a specific commit to review the code to then resolve the issue manually using the policy guidelines on the Prisma Cloud console. 

 Previous Pull Request Scanning 

 Next Suppress Code Issues 

 Last updated 1 month ago 

 Was this helpful?
