---
url: https://docs.paloaltonetworks.com/cloud-ngfw-aws/administration/monitor-your-cloud-ngfw-resource/enable-audit-logging-on-cloud-ngfw-for-aws
fetched_at: 2026-08-13T15:30:45Z
source: palo-alto-main
---

# View Audit Logs on Cloud NGFW for AWS Clear

View Audit Logs on Cloud NGFW for AWS 

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

 View Audit Logs on Cloud NGFW for AWS 

 Updated on 

 Tue May 19 03:36:42 PDT 2026 

 Focus 

 Download PDF 

 English 

 日本語 (Japanese) 

 Français (French) 

 Deutsch (German) 

 Filter

 Expand All 
 | 
 Collapse All 

 Cloud NGFW for AWS Docs 

 Getting Started 

 Deployment 

 Administration 

 Reference 

 Release Notes 

 New Features 

 Updated on 

 Tue May 19 03:36:42 PDT 2026 

 Focus 

 Home 

 Cloud NGFW for AWS 

 Cloud NGFW for AWS Administration 

 Monitor 

 View Audit Logs on Cloud NGFW for AWS 

 Download PDF 

 English 

 日本語 (Japanese) 

 Français (French) 

 Deutsch (German) 

 Cloud NGFW for AWS 

 View Audit Logs on Cloud NGFW for AWS 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Cloud NGFW for AWS Docs 

 Getting Started 

 Deployment 

 Administration 

 Reference 

 Release Notes 

 New Features 

 Previous 

 View Traffic and Threat Logs in Strata Logging Service 

 Next 

 Publish and View Custom Metrics in AWS CloudWatch 

 View Audit Logs on Cloud NGFW for AWS 

 Learn about audit logging on Cloud NGFW for AWS. 

 Where Can I Use This? What Do I Need? 

 Cloud NGFW for AWS 

 Cloud NGFW subscription 

 Palo Alto Networks Customer Support Account (CSP) 

 AWS Marketplace account 

 User role (either tenant or administrator) 

 Track administrator activity on Cloud NGFW for AWS to achieve real-time reporting of
 activity across your deployment. If you have reason to believe that an administrator
 account is compromised, the audit log provides you with a full history of where an
 administrator navigated throughout the Cloud NGFW tenant and what configuration
 changes they made so you can analyze in detail and respond to all actions taken be
 the compromised account. 

 If you have already deployed Cloud NGFW for AWS, you may need to update your CFT. If
 your current CFT does not include the Audit Log field. 

 The log group must be created in the AWS console in the same region where
 the Cloud NGFW CFT was deployed. 

 For Cloud NGFW tenants created after July 30, 2025 (V2 tenants) ,
 audit logging is currently unavailable for certain UI and core firewall
 management APIs. Actions performed through the firewall list and
 firewall details pages in the UI (e.g., viewing the list of firewalls),
 or via the corresponding APIs, will not generate audit log
 entries. 

 Following are the affected firewall management
 APIs: 

POST /ngfirewalls (create ngfirewall)

GET /ngfirewalls (list ngfirewalls)

GET /ngfirewalls/{firewall_id} (read ngfirewall)

PATCH /ngfirewalls/{firewall_id} (update ngfirewall)

DELETE /ngfirewalls/{firewall_id} (delete ngfirewall)

POST /ngfirewalls/{firewall_id}/link (associate fw link)

DELETE /ngfirewalls/{firewall_id}/link (disassociate fw link)

POST /ngfirewalls/{firewall_id}/rulestack (associate rulestack)

DELETE /ngfirewalls/{firewall_id}/rulestack (disassociate rulestack)

GET /ngfirewalls/{firewall_id}/logprofile (read logprofile)

POST /ngfirewalls/{firewall_id}/logprofile (update logprofile) 

 The V1 tenants , where audit logging for all APIs continues to
 function as expected. 

 When an event occurs, an audit log is generated and forwarded to the CloudWatch log
 group you specify. 

 If necessary, update your CFT to add permissions necessary to write to the
 Audit Log CloudWatch log group. 

 Log in to the Cloud NGFW console. 

 Select AWS Accounts Download CFT to download the CFT as a yaml file. 

 Upload, edit, and apply your CFT to the AWS console. 

 Log in to the AWS Console and select CloudFormation Stacks . 

 Locate the Cloud NGFW
 stack— PaloAltoNetworksCrossAccountRoleSetup . 

 Select Update . 

 Select Replace current template and
 Upload a template file . 

 Select your CFT yaml file and click
 Next . 

 Verify the CFT stack setting and click
 Next . 

 Verify the CFT stack options and click
 Next . 

 Review the CFT stack and click
 Update . 

 Log in to the Cloud NGFW tenant console. 

 Select Tenant . 

 Click the Audit Log Settings edit icon 

 . 

 Select the CloudWatch radio button. 

 Enter the Amazon Resource Name (ARN) of your target CloudWatch Log Group. 

 Ensure that the ARN you enter here corresponds with the CloudWatch Log Group
 you specified in your CFT stack. 

 Click Save . 

 Previous 

 View Traffic and Threat Logs in Strata Logging Service 

 Next 

 Publish and View Custom Metrics in AWS CloudWatch 

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

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 Service Provider 

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

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Cloud NGFW for AWS 

 Administration 

 AWS 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
