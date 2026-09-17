---
url: https://docs.prismacloud.io/content-collections/application-security/get-started/connect-code-and-build-providers/ci-cd-systems/add-circleci-cicd-system
fetched_at: 2026-09-16T13:35:40Z
source: prisma-cloud
---

# CircleCI | Prisma Cloud arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Enterprise Edition 

 Content Collections 

 Application Security 

 Get Started with Application Security 

 Connect Code and Build Providers 

 CI/CD Systems 

 CircleCI 

 Integrate CircleCI CI/CD systems (CircleCI) with Prisma Cloud to gain visibility into and monitor CircleCI and all systems, technologies and processes in your environment connected to CircleCI. This integration allows Prisma Cloud to scan your CircleCI environment and provide the results of the scan, allowing you to understand and fix issues as soon as they are detected. 

 Before you begin. 

 Add the Prisma Cloud IP addresses and hostname for Application Security to an allow list to enable access to the Prisma Cloud Console. 

 Permissions : To enable Prisma Cloud visibility for all CircleCI projects, a version control system (VCS) user must be authorized to grant access. This is because the CircleCI user base is integrated with the (VCS), and inherits permissions granted to VCS users. 

 Create a dedicated VCS user to integrate CircleCI with Prisma Cloud, to prevent the integration breaking if the user leaves the organization. 

 Verify that the dedicated user follows all the organization’s projects in CircleCI. 

 Create a personal API token (see step 2 below). The main reason that Prisma Cloud requires personal API tokens is to allow reading the configurations from CircleCI for all the projects that a user tracks. 

 Generate a personal API token in CircleCI. 

 Login to your CircleCI instance with VCS user credentials. 

 CircleCI utilizes the VCS user visibility. For example, if a GitHub user has access to specific organizations and repositories, these entities are visible and available in CircleCI. 

 Create and save a personal API token in CircleCI . 

 On Prisma Cloud. 

 In Application Security, select Home > Settings > Connect Provider > Code & Build Providers . 

 Select CircleCI (under CI/CD Systems) in the catalog that is displayed. 

 The CircleCI integration wizard is displayed. 

 Fill in the following details in the provided fields of the wizard. 

 Integration Name : An alias allowing you to identify the integration 

 Personal API Token : The personal API token generated in step 2 above 

 Select Create . 

 The Prisma Cloud Application Security module is integrated with your CircleCI system. 

 Verify integration. 

 In Application Security , select Home > Settings > CI/CD Systems tab. 

 Confirm that the status of the CircleCI instance displays Active under Status . 

 It may take up to 3 minutes for the integration status to be updated. 

 Next step: Monitor and manage scan results. 

 The next scan of your CircleCI systems will include the new integration, and the results will be displayed in Repositories . 

 Support for Multiple Integrations 

 Prisma Cloud supports multiple integrations for CircleCI instances. 

 Multiple integrations from a single Prisma Cloud account enables you to: 

 View a list of integrations on a single console 

 Delete an existing integration 

 In Application Security, select Home > Settings > Connect Provider > Code & Build Providers > CircelCI (under CI/CD SYstems). 

 Select Add integration in the wizard. 

 Repeat the integration process above. 

 The new integration is displayed on the landing page of the integration wizard. To view scan results, see the integration process above. 

 Manage Integrations 

 Manage integrations from the integration wizard. 

 Access the CircleCi integration wizard - see step 1 of Support for Multiple Integrations above > select the menu under Actions . 

 From Actions you can: 

 Remove integrations 

 Edit integrations 

 Previous CI/CD Systems 

 Next Jenkins Server 

 Last updated 1 month ago 

 Was this helpful?
