---
url: https://docs.paloaltonetworks.com/enterprise-dlp/administration/configure-enterprise-dlp/email-dlp/customize-email-dlp-delivery-notifications
fetched_at: 2026-09-16T08:20:31Z
source: strata-and-sase
---

# Customize Email DLP Delivery Notifications Clear

Updated on 

 Sep 10, 2026 

 Focus 

 Home 

 Enterprise DLP 

 Administration 

 Configure Enterprise DLP 

 Email DLP 

 Customize Email DLP Delivery Notifications 

 Download PDF 

 Enterprise DLP 

 Customize Email DLP Delivery Notifications 

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

 Configure Email DLP Alert Settings 

 Next 

 Review Email DLP Incidents 

 Customize Email DLP Delivery Notifications 

 Customize the subject and body of Enterprise Data Loss Prevention (E-DLP) Email DLP delivery
 notifications to give email senders clear, organization-aligned guidance when their message
 is delayed or cannot be delivered. 

 Where Can I Use This? What Do I Need? 

 Data Security 

 One of the following licenses that include the Enterprise DLP license 

 Review the Supported
 Platforms for details on the required license
 for each enforcement point. 

 Prisma Access CASB license 

 Next-Generation
CASB for Prisma Access and NGFW (CASB-X) license 

 Data Security license 

 Email DLP license 

 When Email DLP delays or cannot deliver an outbound email, it sends a notification to
 the original sender. By default, these notifications use generic system-generated
 messaging that may be unclear to end users and generate unnecessary help desk
 requests. You can customize the subject and body of each notification type so
 senders receive guidance that reflects your internal support processes, terminology,
 and contact information. 

 You configure each notification independently. If you do not configure custom
 content, Enterprise DLP uses the default subject and body for that
 notification. All configuration changes are recorded in audit logs. 

 Log in to 
 Strata Cloud Manager . 

 Review the Email DLP setup prerequisites and allow the
 Email DLP egress IP addresses and outbound SMTP server domains on your
 organization's inbound SMTP server to receive delivery notifications. 

 Select Configuration SaaS Security Data Security Settings Email DLP Customize NDR & DSN Message . 

 Customize the Subject and Message
 Body for the automatic notifications email senders
 receive. 

 You can include the following variables in the notification subject or body
 to provide senders with message-specific details: 

 ${recipients} —The email addresses the message was
 sent to. 

 ${sender} —The email address of the original
 sender. 

 ${sender_domain} —The domain of the original
 sender. 

 ${original_subject} —The subject line of the original
 email. 

 ${sent_date} —The date the original email was
 sent. 

 ${error_code} —The SMTP error code associated with
 the delivery failure. 

 ${error_message} —The error message associated with
 the delivery failure. 

 The subject and message body fields accept plain text only. HTML and rich
 text formatting are not supported. You can include URLs in the message
 body. 

 Email DLP supports the following notifications. You can Reset to
 Default for each notification to restore the predefined
 subject and message body text. 

 Delayed Status Notification (DSN) 

 Sent when delivery to the next-hop mail server remains pending beyond
 30 minutes after DLP scanning completes. A DSN does not indicate
 permanent failure and Enterprise DLP continues retry attempts.
 Use the DSN to reassure senders that Email DLP is still attempting delivery and will deliver the message once connectivity to the next hop is resolved. 

 Non-Delivery Report (NDR) 

 Sent when Enterprise DLP cannot deliver the message within the
 2-day retry period after exhausting all retry attempts due to
 deferred errors (SMTP 4xx responses). Use the NDR to direct senders
 to your internal help channel, include a support contact, or explain
 next steps in language your organization uses. 

 Outlook on macOS ignores custom NDR subject lines and always
 displays the subject as Undeliverable:
 ${original_subject} , regardless of your
 configuration. 

 Permanent Delivery Failure 

 Sent when the next-hop mail server permanently rejects the message
 with an SMTP 5xx response. No retry is attempted. Use this
 notification to confirm the rejection and instruct senders on how to
 report the issue or resend the message. 

 Click Save . 

 Previous 

 Configure Email DLP Alert Settings 

 Next 

 Review Email DLP Incidents
