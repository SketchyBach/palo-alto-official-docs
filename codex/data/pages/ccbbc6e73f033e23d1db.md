---
url: https://docs.prismacloud.io/admin-guide/33/install/deploy-defender/serverless/install-serverless-defender-layer
fetched_at: 2026-09-16T13:36:42Z
source: prisma-cloud
---

# Deploy Serverless Defender as a Lambda Layer | 33 | Prisma Cloud arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Compute Edition 

 Admin Guide 

 33 

 Install 

 Deploy the Prisma Cloud Defender 

 Deploy Serverless Defender 

 Deploy Serverless Defender as a Lambda Layer 

 Prisma Cloud Serverless Defenders protect serverless functions at runtime. Currently, Prisma Cloud supports AWS Lambda functions. 

 Lambda layers are ZIP archives that contain libraries, custom runtimes, or other dependencies. Layers let you add reusable components to your functions, and focus deployment packages on business logic. They are extracted to the /opt directory in the function execution environment. For more information, see the AWS Lambda layers documentation . 

 Prisma Cloud delivers Serverless Defender as a Lambda layer. Deploy Serverless Defender to your function by wrapping the handler and setting an environment variable. 

 Secure the Serverless Functions 

 To secure an AWS Lambda function with the Serverless Defender layer: 

 Download the Serverless Defender Lambda layer ZIP file. 

 Upload the layer to AWS. 

 Define a serverless protection runtime policy. 

 Define a serverless WAAS policy. 

 Add the layer to your function, update the handler, and set an environment variable. After completing this integration, Serverless Defender runs when your function is invoked. 

 Download the Serverless Defender Layer 

 Download the Serverless Defender layer from Compute Console. 

 Open Console, then go to Manage > Defenders > Deploy> Defenders > Single Defender . 

 Choose the DNS name or IP address that Serverless Defender uses to connect to Console. 

 Set the Defender type to Serverless Defender . 

 Select a runtime. 

 Prisma Cloud supports Lambda layers for Node.js , Python , Ruby , C# , and Java . See system requirements for the runtimes that are supported for Serverless Defender as a Lambda layer. 

 For Deployment Type , select Layer . 

 Download the Serverless Defender layer. A ZIP file is downloaded to your host. 

 Upload the Serverless Defender layer to AWS 

 Add the layer to the AWS Lambda service as a resource available to all functions. 

 In the AWS Management Console, go to the Lambda service. 

 Select Layers > Create Layer . 

 In Name , enter twistlock . 

 Click Upload , and select the file you just downloaded, twistlock_defender_layer.zip 

 Select the compatible runtimes: Python , Node.js , *Ruby , C# , or Java . 

 Click Create . 

 Define your Runtime Protection Policy 

 By default, Prisma Cloud ships with an empty serverless runtime policy. An empty policy disables runtime defense entirely. 

 You can enable runtime defense by creating a rule. By default, new rules: 

 Apply to all functions ( * ), but you can target them to specific functions by function name. 

 Block all processes from running except the main process. This protects against command injection attacks. 

 When functions are invoked, they connect to Compute Console and retrieve the latest policy. To ensure that functions start executing at time=0 with your custom policy, you must predefine the policy. Predefined policy is embedded into your function along with the Serverless Defender by way of the TW_POLICY environment variable. 

 Log into Prisma Cloud Console. 

 Go to Defend > Runtime > Serverless Policy . 

 Click Add rule . 

 In the General tab, enter a rule name. 

 (Optional) Target the rule to specific functions. 

 Set the rule parameters in the Processes , Networking , and File System tabs. 

 Click Save . 

 Define your Serverless WAAS Policy 

 Prisma Cloud lets you protect your serverless functions against application layer attacks by utilizing the serverless Web Application and API Security (WAAS) . 

 By default, the serverless WAAS is disabled. To enable it, add a new serverless WAAS rule. 

 Log into Prisma Cloud Console. 

 Go to Defend > WAAS > Serverless . 

 Click Add rule . 

 In the General tab, enter a rule name. 

 (Optional) Target the rule to specific functions. 

 Set the protections you want to apply ( SQLi , CMDi , Code injection , XSS , LFI ). 

 Click Save . 

 Embed the Serverless Defender 

 Embed the Serverless Defender as a layer, and run it when your function is invoked. If you are using a deployment framework such as SAM or Serverless Framework you can reference the layer from within the configuration file. 

 Prerequisites: 

 You already have a Lambda function. 

 Your Lambda function is written for Node.js, Python, or Ruby. 

 Your function’s execution role grants it permission to write to CloudWatch Logs. Note that the AWSLambdaBasicExecutionRole grants permission to write to CloudWatch Logs. 

 Go to the function designer in the AWS Management Console. 

 Click on the Layers icon. 

 In the Referenced Layers panel, click Add a layer . 

 In the Select from list of runtime compatible layers , select twistlock . 

 In the Version drop-down list, select 1 . 

 Click Add . 

 When you return to the function designer, you’ll see that your function now uses one layer. 

 Update the handler for your function to be twistlock.handler . 

 Set the TW_POLICY and ORIGINAL_HANDLER environment variable, which specifies how your function connects to Compute Console to retrieve policy and send audits. 

 In Compute Console, go to Manage > Defenders > Deploy > Single Defender . 

 For Defender type , select Serverless . 

 In Set the Twistlock environment variable , enter the function name and region. 

 Copy the generated Value . 

 In AWS Console, open your function in the designer, and scroll down to the Environment variables panel. 

 For Key , enter TW_POLICY. 

 For Value , paste the rule you copied from Compute Console. 

 For ORIGINAL_HANDLER , this is the original value of handler for your function before your modification. 

 Click Save to preserve all your changes. 

 Previous Deploy Serverless Defender 

 Next Auto-defend serverless functions 

 Last updated 1 month ago 

 Was this helpful?
