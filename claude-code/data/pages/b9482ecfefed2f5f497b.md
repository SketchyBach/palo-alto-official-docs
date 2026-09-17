---
url: https://docs.prismacloud.io/content-collections/administration/configure-external-integrations-on-prisma-cloud/integrate-prisma-cloud-with-amazon-sqs
fetched_at: 2026-09-16T13:35:08Z
source: prisma-cloud
---

# Integrate Prisma Cloud with Amazon SQS | Prisma Cloud arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Enterprise Edition 

 Content Collections 

 Administration 

 Configure External Integrations on Prisma Cloud 

 Integrate Prisma Cloud with Amazon SQS 

 Learn how to integrate Prisma® Cloud with Amazon Simple Queue Service (SQS). 

 If you use Amazon Simple Queue Service (SQS) to enable custom workflows for alerts, Prisma® Cloud integrates with Amazon SQS. When you set up the integration, as soon as an alert is generated, the alert payload is sent to Amazon SQS. 

 The integration gives you the flexibility to send alerts to a queue in the same AWS account that you may have onboarded to Prisma Cloud or to a queue in a different AWS account. If you want to send alerts to an SQS in a different AWS account, you must provide the relevant IAM credentials—Access Key or IAM Role. 

 Amazon SQS allows a maximum payload size of 256KB. Some Prisma Cloud alerts, such as the anomaly policy alerts, can exceed this size limit and AWS recommends using S3 in such cases . To set up an Amazon S3 integration to send alerts, see Integrate Prisma Cloud with Amazon S3 . 

 Configure Amazon SQS to receive Prisma Cloud alerts. 

 Log in to the Amazon console with the necessary credentials to create and configure the SQS. 

 Click Simple Queue Services (under Application Integration ). 

 Create New Queue or use an existing queue. 

 Enter a Queue Name and choose a Queue Type— Standard or FIFO . 

 Click Configure Queue . 

 For the attributes specific to the Queue, use either the AWS default selection or set them per your company policies. Use SSE to keep all messages in the Queue encrypted, and select the default AWS KMS Customer Master Key (CMK) or enter your CMK ARN. 

 Create Queue . 

 This creates and displays your SQS Queue. 

 Click the Queue that you created and view the Details and copy the URL for this queue. 

 You provide this value in Prisma Cloud to integrate Prisma Cloud notifications in to this Queue. 

 If you are using a Customer Managed Key to encrypt queues in Amazon SQS, you must configure the Prisma Cloud Role with explicit permission to read the key. 

 On the Amazon console, select KMS > Customer Managed Keys and Create Key . 

 Refer to the AWS documentation for details on creating keys . 

 Enter an Alias and Description, and add any required Tags and click Next . 

 Select the IAM users and roles who can use this key through the KMS API and click Next . 

 Select the IAM users and roles who can use this key to encrypt and decrypt the data. 

 Review the key policy and click Finish . 

 Enable read-access permissions to Amazon SQS on the IAM Role policy. 

 The Prisma Cloud IAM Role policy you use to onboard your AWS setup needs these permissions: screen:["sqs:GetQueueAttributes", "sqs:ListQueues","sqs:SendMessage", "sqs:SendMessageBatch", "tag:GetResources","iam:GetRole"] 

 If you have configured Server-Side Encryption (SSE) for SQS, you must also include the kms:GenerateDataKey IAM permission. 

 When you add the above permissions to the CFT Templates and the account you run the template on is the same account to which the SQS Queue belongs, the Prisma Cloud IAM role will have the permissions required to write to the queue. If you do not want to add the permissons to the role or if the SQS Queue belongs to a different account, then proceed to Integrate Prisma Cloud with Amazon SQS . 

 Set up Amazon SQS integration in Prisma Cloud. 

 Log in to Prisma Cloud. 

 Select Settings > Integrations . 

 Add Integration > Amazon SQS . A modal wizard opens where you can add the SQS integration. 

 Enter a Name and Description for the integration. 

 Enter the Queue URL that you copied when you configured Prisma Cloud in Amazon SQS. 

 The queue URL format on AWS China should be https://sqs.<China region api identifier>.amazonaws.com.cn/<account id>/<queue name> . 

 (tt:[Optional]) Select More Options to provide IAM credentials associated with a different AWS account. 

 By default, Prisma Cloud accesses the SQS queue using the same credentials with which you onboarded the AWS account to Prisma Cloud. If your queue is in a different account or if you want to authorize access using a separate set of IAM security credentials, you can pick of the following options. 

 Select the IAM Access Key and enter the Access Key and Secret Key, or IAM Role and enter the External ID and Role ARN. 

 The External ID associated with the IAM role must be a UUID in a 128-bit format, and not any random string. For your convenience, the External ID is automatically generated on the Prisma Cloud web console when you click Generate . You must manually create one if you’re using the Prisma Cloud API. 

 Any existing integrations will continue to work. If you modify an existing Amazon SQS integration, you must replace the External ID to complete the validation check and save your changes. 

 This IAM permissions for both options must include sqs:SendMessage and sqs:SendMessageBatch. Additionally, the kms:GenerateDataKey is required if you have configured Server-Side Encryption (SSE) for SQS. 

 Next to review the Summary . 

 Test and Save the integration. 

 After you set up the integration successfully, you can use the Get Status link in Settings > Integrations to periodically check the integration status. 

 To edit the integration, on Settings > Integrations , click the corresponding edit icon. The integration Summary page opens. 

 Edit to update the integration as required. 

 Next to review your edits. 

 Test and Save the integration. 

 Create an Alert Rule for Run-Time Checks or modify an existing rule to enable the Amazon SQS Integration. 

 Previous Integrate Prisma Cloud with Amazon Security Lake 

 Next Integrate Prisma Cloud with Azure Service Bus Queue 

 Last updated 1 month ago 

 Was this helpful?
