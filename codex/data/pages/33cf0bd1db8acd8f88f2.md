---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/ci-cd-security/pipeline-based-access-controls/appsec-cicd-55
fetched_at: 2026-09-16T09:11:08Z
source: cortex-platform
---

# Jenkins jobs can be executed with high privileges | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 CI/CD Security 

 Pipeline Based Access Controls 

 Jenkins jobs can be executed with high privileges 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_CICD_55 

 Category 

 Pipeline Based Access Controls 

 Severity 

 MEDIUM 

 Impact 

 Each executed Jenkins job is assigned with the privileges of a Jenkins user. These privileges are used to interact with the Jenkins system, and include creating jobs, running builds, and executing on the various configured Jenkins nodes. The current authorization configuration on the Jenkins instance allows administrators to configure it to run with the Jenkins SYSTEM user account (that should not be confused with the operating system user). This user account has high privileges over the system, and is allowed to perform any action on the Jenkins instance. Any job configured to run with the context of this user account allows an attacker executing malicious code in the job to take advantage of it to perform impactful actions on the Jenkins instance and its nodes. For more information about access controls for builds: https://www.jenkins.io/doc/book/security/build-authorization/ 

 Recommended Solution - Buildtime 

 Prevent job administrators from configuring jobs to run with the SYSTEM user account: 

 Install the Authorize Project plugin. 

 On the Jenkins instance, under Manage Jenkins , browse to Configure Global Security . 

 Configure the Per-project configurable Build Authorization setting to NOT include the Run as SYSTEM strategy, to prevent it from being configured for specific jobs. In addition, set at least one of the following strategies: 

 Run as Anonymous 

 Run as User who Triggered Build 

 Run as Specific User 

 📌 NOTE 
Follow the least privilege principle when configuring a job to run by a specific user. 

 Previous Jenkins jobs are executed with high privileges by default 

 Next GitLab project job token authorized to access other projects 

 Last updated 1 month ago 

 Was this helpful?
