---
url: https://docs.paloaltonetworks.com/ai-runtime-security/administration/managed-ai-runtime-security-for-aws/monitor-your-managed-airs-for-aws-resource
fetched_at: 2026-09-16T07:54:47Z
source: ai-security
---

# Monitor Clear

Updated on 

 Mon Aug 24 04:41:52 PDT 2026 

 Focus 

 Home 

 Prisma AIRS 

 Administration 

 Managed AI Runtime Security for AWS 

 Monitor 

 Download PDF 

 Prisma AIRS 

 Monitor 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma AIRS Docs 

 Activation & Onboarding 

 Administration 

 AI Supply Chain Security 

 AI Red Teaming 

 Release Notes 

 New Features 

 Previous 

 Author and Enforce Managed AIRS for AWS Policies in AIRS Profile 

 Next 

 View Traffic and Threat Logs in Strata Cloud Manager 

 Monitor 

 Learn how to monitor your Managed AIRS for AWS resrouce. 

 Where Can I Use This? What Do I Need? 

 Managed AIRS for AWS 

 Access to Strata Cloud Manager (SCM) 

 You can monitor the service's overall health and gain deep insights into
 traffic and operations using Managed AIRS for AWS logs and metrics. 

 Managed AIRS for AWS resources are instances of the Cloud NGFW service. To
 monitor the overall health of the Managed AIRS for AWS service, check the Palo
 Alto Networks status page . This page provides region-specific status
 information and allows you to subscribe to service notifications, ensuring you are aware
 of any ongoing service events. 

 Traffic and Threat Logs 

 Managed AIRS for AWS publishes a variety of logs to help you monitor traffic and
 threats for analysis and compliance. These traffic and threat logs provide detailed
 information about network sessions passing through your Managed AIRS for AWS resource. Analyze
 permitted and denied traffic, inspect source/destination IP addresses, URLs, port
 numbers, and protocols. This data is crucial for understanding traffic patterns,
 identifying potential security threats, and troubleshooting connectivity issues.
 These can be streamed to other AWS services for analysis and alarming. 

 Destinations: 

 Amazon CloudWatch: Stream logs for real-time
 monitoring and analysis. 

 Amazon S3 bucket: Store logs for long-term retention
 and further investigation. 

 Amazon Kinesis Firehose: Stream logs to third-party
 providers for integration with external analytic platforms. 

 Strata Logging Service: Stream logs to Palo Alto
 Networks Strata Logging Service for real-time monitoring and
 advanced analysis. 

 Viewing Logs: 

 AWS: Use the AWS Cloudwatch console. 

 Palo Alto Networks: Use the Strata Cloud Management
 (SCM) log viewer. 

 Performance and Health Metrics 

 Managed AIRS for AWS publishes a variety of metrics to help you monitor
 resource health, performance, and traffic usage. These resources assess the overall
 health of your Managed AIRS for AWS resources, identify performance bottlenecks, and
 detect anomalies. 

 Destination: Managed AIRS for AWS publishes custom metrics to AWS CloudWatch . 

 Monitoring: Managed AIRS for AWS streams these metrics to a CloudWatch
 namespace in your AWS account. You can use these metrics to access
 historical performance data. You can also set alarms that monitor
 specific thresholds and send notifications when these thresholds are
 reached. 

 Audit Logs 

 Audit logs track user and API activity
 within your Managed AIRS for AWS tenant. These logs help you audit operations related to
 firewall resources, such as creating, updating, or deleting rules and policies.
 Reviewing these logs helps maintain a historical record of configuration changes and
 ensures compliance with security requirements. 

 Destination: Managed AIRS for AWS streams audit logs to Amazon
 CloudWatch tracking all tenant activity. 

 Viewing Logs: Use the AWS Cloudwatch console. 

 Previous 

 Author and Enforce Managed AIRS for AWS Policies in AIRS Profile 

 Next 

 View Traffic and Threat Logs in Strata Cloud Manager
