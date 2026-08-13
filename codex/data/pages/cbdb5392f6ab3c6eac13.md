---
url: https://docs.paloaltonetworks.com/cloud-ngfw-aws/administration/monitor-your-cloud-ngfw-resource/publish-and-view-custom-metrics-in-aws-cloudwatch
fetched_at: 2026-08-13T15:30:45Z
source: palo-alto-main
---

# Publish and View Custom Metrics in AWS CloudWatch Clear

Publish and View Custom Metrics in AWS CloudWatch 

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

 Publish and View Custom Metrics in AWS CloudWatch 

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

 Publish and View Custom Metrics in AWS CloudWatch 

 Download PDF 

 English 

 日本語 (Japanese) 

 Français (French) 

 Deutsch (German) 

 Cloud NGFW for AWS 

 Publish and View Custom Metrics in AWS CloudWatch 

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

 View Audit Logs on Cloud NGFW for AWS 

 Next 

 Firewall-as-Code 

 Publish and View Custom Metrics in AWS CloudWatch 

 Publish custom metrics in AWS CloudWatch for your Cloud NGFW for AWS
 resource 

 Where Can I Use This? What Do I Need? 

 Cloud NGFW for AWS 

 Cloud NGFW subscription 

 Palo Alto Networks Customer Support Account (CSP) 

 AWS Marketplace account 

 User role (either tenant or administrator) 

 Cloud NGFW for AWS publishes custom metrics in AWS CloudWatch to help you monitor your
 Cloud NGFW's health, performance, and usage patterns. With these additional metrics
 you can assess the overall health of your Cloud NGFW resources, identify performance
 bottlenecks and detect anomalies. These metrics are numerical values describing
 aspects of a Cloud NGFW at a particular time. Collected every 5 minutes, metrics are
 useful for alerting due to their frequent sampling. 

 The
 CloudWatch log group, S3 bucket, CloudWatch namespace and the Kinesis stream
 should be precreated in the CloudFormation template (CFT). 

 Metrics are collected every 5 minutes. All
 metrics are published to one namespace. CloudWatch stores your metrics, so that
 you can access historical information for an added perspective on how your Cloud
 NGFW resources are performing. You can also set alarms that watch for certain
 thresholds, and send notifications or take actions when those thresholds are
 met. For more information, see the Amazon CloudWatch documentation .

 The following CloudWatch metrics are supported by the Cloud NGFW resource: 

 Field Name 

 Description 

 Dataplane CPU Utilization (%) 

 Monitors dataplane CPU usage and measures the traffic load on the
 Cloud NGFW resource. 

 Dataplane Packet Buffer Utilization (%) 

 Monitors dataplane buffer usage and measures buffer utilization.
 If you have a sudden burst in traffic, monitoring your buffer
 utilization allows you to ensure that the firewall does not
 deplete the dataplane buffer, which results in dropped
 packets. 

 Connection per Second 

 Represents the total number of concurrent TCP connections. 

 Session throughput Kbps 

 The session throughputis , measured in Kbps. 

 Session throughput Pps 

 The session throughputis , measured in Pps. 

 Sessions Active 

 Monitors the total number of sessions that are active on the
 Cloud NGFW resource. An active session is a session that is in
 the flow lookup table for which packets will be inspected and
 forwarded, as required by policy. 

 Session Utilization (%) 

 Monitors the TCP, UDP, ICMP, and SSL sessions that are currently
 active and the packet rate, new connection establish rate, and
 firewall throughput to determine session utilization. 

 BytesIn 

 Number of bytes in the server-to-client direction of the
 session. 

 BytesOut 

 Number of bytes in the client-to-server direction of the
 session. 

 PktsIn 

 Number of server-to-client packets for the session. 

 PktsOut 

 Number of client-to-server packets for the session. 

 To publish CloudWatch Metrics: 

 Log in to your Cloud NGFW resource. 

 Select NG Firewalls . 

 Select Log Settings . 

 Under Metrics , specify the following: 

 CloudWatch Namespace . This field represents the
 location on AWS where the metrics are collected. 

 CloudWatch Metric . Select the metrics you want
 to monitor. See the table above for supported metrics. 

 Click Save. 

 A sample output of metrics displayed in an account resembles: 

 Track How Your Cloud NGFW Resource uses Memory 

 You can track how your Cloud NGFW resources use available memory. This
 functionality is useful when you commit a configuration that includes a large
 rulestack and want to monitor the amount of memory used across all firewall
 instances. 

 To track how your Cloud NGFW resource uses memory: 

 Log in to your Cloud NGFW resource. 

 Select NG Firewalls . 

 Select Log Settings . 

 Under Metrics , use the drop-down menu to select
 Config Memory Utilization . When this field is
 selected, the size of your Cloud NGFW configuration is displayed as a
 percentage when compared to the amount of available memory. 

 After selecting the Config Memory Utilization 
 option the CloudWatch Metrics field displays how
 memory is used across your firewall instance. 

 Previous 

 View Audit Logs on Cloud NGFW for AWS 

 Next 

 Firewall-as-Code 

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

 Deployment 

 AWS 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
