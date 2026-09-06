---
url: https://cortex-docs.paloaltonetworks.com/amazon-web-services-manual-onboarding/aws-manual-onboarding-guide/phase-3-complete-the-onboarding-wizard-in-cortex
fetched_at: 2026-09-06T11:16:39Z
source: cortex-platform
---

# Phase 3: Complete the onboarding wizard in Cortex | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Manual Cloud Onboarding 

 Amazon Web Services Manual Onboarding 

 AWS Manual Onboarding Guide 

 Phase 3: Complete the onboarding wizard in Cortex 

 After creating all AWS resources, provide the following details in the Cortex AWS onboarding wizard. These details correspond to the data that the automated CloudFormation flow sends via its Lambda callback: 

 Account details: 

 Field 

 Value 

 How to Retrieve 

 Account ID 

 Your 12-digit AWS account ID 

 aws sts get-caller-identity --query Account --output text 

 Account Name 

 A display name for this account 

 User-defined 

 Credentials: 

 Field 

 Value 

 How to Retrieve 

 Role ARN 

 ARN of the Cortex Platform Role (Step 2.2) 

 aws iam get-role --role-name "${CORTEX_ROLE_NAME}" --query Role.Arn --output text 

 External ID 

 The ExternalID chosen by the user 

 Listed in the identifiers JSON file 

 Audit log collection (BYOB) resources: 

 Field 

 Value 

 How to Retrieve 

 SQS Queue URL 

 URL of the CloudTrail logs SQS queue (Step 2.3) 

 aws sqs get-queue-url --queue-name "${SQS_QUEUE_NAME}" --query QueueUrl --output text 

 CloudTrail Role ARN 

 ARN of the CloudTrail read role (Step 2.6) 

 aws iam get-role --role-name "${LOGS_ROLE_NAME}" --query Role.Arn --output text 

 Scanner (optional): 

 Field 

 Value 

 How to Retrieve 

 Scanner Role ARN 

 ARN of the Scanner Role (Step 2.7) 

 aws iam get-role --role-name "${SCANNER_ROLE_NAME}" --query Role.Arn --output text 

 Quick retrieval script 

 You can use the following script to retrieve all of the required details at once: 

 Ask Copy 

 echo " === Details to provide to Cortex === " 
 echo "" 
 echo " Account ID: ${ AWS_ACCOUNT_ID }" 
 echo " Role ARN: $( aws iam get-role --role-name "${ CORTEX_ROLE_NAME }" --query Role.Arn --output text )" 
 echo " External ID: ${ EXTERNAL_ID }" 
 echo " SQS Queue URL: $( aws sqs get-queue-url --queue-name "${ SQS_QUEUE_NAME }" --query QueueUrl --output text )" 
 echo " CloudTrail Role ARN: $( aws iam get-role --role-name "${ LOGS_ROLE_NAME }" --query Role.Arn --output text )" 

 # If using outpost scanning: 
 # echo "Scanner Role ARN: $(aws iam get-role --role-name "${SCANNER_ROLE_NAME}" --query Role.Arn --output text)" 

 Note: In the automated CloudFormation flow, a Lambda function sends these details to Cortex automatically using a callback URL. In the manual flow, you enter them manually in the Cortex AWS onboarding wizard. 

 Format requirements 

 Ensure the values you provide match the expected formats: 

 Field 

 Format 

 Account ID 

 Exactly 12 digits (e.g., 123456789012) 

 Organization ID 

 Starts with r- followed by alphanumeric characters (e.g., r-ab12) 

 SQS URL 

 https://sqs..amazonaws.com// 

 Role ARNs 

 Valid AWS ARN format: arn:aws:iam:::role/ 

 Previous Phase 2: Provision the AWS resources 

 Next Manage configuration changes 

 Last updated 10 days ago 

 Was this helpful?
