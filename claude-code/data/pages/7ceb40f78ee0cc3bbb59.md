---
url: https://docs.prismacloud.io/admin-guide/33/vulnerability-management/serverless-functions
fetched_at: 2026-09-16T13:37:02Z
source: prisma-cloud
---

# Configure Serverless Function Scanning | 33 | Prisma Cloud arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Compute Edition 

 Admin Guide 

 33 

 Vulnerability Management 

 Configure Serverless Function Scanning 

 Prisma Cloud can scan serverless functions for visibility into vulnerabilities and compliance issues . For runtime protection, you must deploy a serverless Defender . Prisma Cloud supports AWS Lambda, Google Cloud Functions, and Azure Functions. 

 Serverless computing is an execution model in which a cloud provider dynamically manages the allocation of machine resources and schedules the execution of functions provided by users. Serverless architectures delegate the operational responsibilities, along with many security concerns, to the cloud provider. In particular, your app itself is still prone to attack. The vulnerabilities in your code and associated dependencies are the footholds attackers use to compromise an app. Prisma Cloud can show you a function’s dependencies, and surface the vulnerabilities in those dependent components. 

 Capabilities 

 For serverless, Prisma Cloud can scan Node.js, Python, Java, C#, Ruby, and Go packages. For a list of supported runtimes see system requirements . 

 Prisma Cloud scans are triggered by the following events: 

 When the settings change, including when new functions are added for scanning. 

 When you explicitly click the Scan button in the Monitor > Vulnerabilities > Functions > Scanned Functions page. 

 Periodically. By default, Prisma Cloud rescans serverless functions every 24 hours, but you can configure a custom interval in Manage > System > Scan . 

 The Scanning Process for Serverless Functions 

 Configure Prisma Cloud to periodically scan your serverless functions. Unlike image scanning, the Prisma Cloud console handles all function scanning. Once you onboarded your cloud accounts, the Prisma Cloud console can give you visibility into vulnerabilities and compliance issues in your serverless functions. For runtime protection, you must deploy a serverless Defender . 

 The Prisma Cloud console performs the following steps to scan serverless functions. 

 Validates that the Prisma Cloud role for the onboarded cloud account has the appropriate permissions and that those permissions are not blocked by an organizational policy. 

 Identifies all serverless functions. 

 Extracts a function using the appropriate GET method sending it to the Prisma Cloud console. 

 Scans the function’s code using Palo Alto Networks proprietary methods. 

 Writes the scan results to the the Prisma Cloud console. You can see the results under Monitor > Vulnerabilities > Functions > Scanned functions . 

 In the scan results, the "Defended" column indicates that functions have been scanned for vulnerabilities and compliance by the Prisma Cloud. This status is applied regardless of whether the scan succeeds or fails. Even if a scan fails, functions are marked as "defended" in cloud discovery to signify their inclusion in the security evaluation process. 

 For the serverless API and CSV reports, "defended" means that the serverless functions are protected at runtime by Compute Defender. 

 Deletes the function code after the scan is completed. 

 Validates that the function code is deleted from the Prisma Cloud console. 

 Scan Lambda Layer Serverless Functions 

 In the console, go to Defend > Vulnerabilities > Functions > Functions . 

 Click on Add Rule . 

 Enter a rule name and configure the rule. 

 In the rule configuration, add a Collection that includes serverless functions deployed in the specific cloud region. 

 For more information on creating collections, see Collections . 

 Click Save . 

 View the scan report by navigating to Monitor > Vulnerabilities > Functions > Scanned functions . 

 All vulnerabilities identified in the latest serverless scan report can be exported to a CSV file by clicking on the CSV button in the top right of the table. 

 + 

 View AWS Lambda Layers scan report 

 Prisma Cloud can scan the AWS Lambda Layers code as part of the Lambda function’s code scanning. This capability can help you determine whether the vulnerability issues are associated with the function or function Layers. Follow the steps below to view the Lambda Layers scan results: 

 Open Console. 

 Make sure you selected the Scan Lambda layers in the Defend > Vulnerabilities > Functions > Functions > Serverless Accounts > Function scan scope 

 Go to Monitor > Vulnerabilities > Functions > Scanned functions . 

 Filter the table to include functions with the desired Layer by adding the Layers filter. 

 You can also filter the results by a specific layer name or postfix wildcards. Example: Layers:* OR Layers:arn:aws:lambda:* 

 Open the Function details dialog to view the details about the Layers and the vulnerabilities associated with them: 

 Click on a specific function 

 See the Function’s vulnerabilities, compliance issues and package info in the related tabs. Use the Found in column to determine if the component is associated with the Function or with the Function’s Layers. 

 Use the Layers info tab to see the full list of the Function’s Layers, and aggregated information about the Layers vulnerabilities. In case that there are vulnerabilities associated with the layer you will be able to expand the layer raw to list all the vulnerabilities. 

 Authenticating with AWS 

 The serverless scanner is implemented as part of Console. The scanner requires the following permissions policy: 

 + 

 IAM User 

 If authenticating with an IAM user, use the Security Token Service (STS) to temporarily issue security credentials to Prisma Cloud to scan your Lambda functions. AWS STS is considered a best practice for IAM users per the AWS Well-Architected Framework. Learn how to use AWS STS . 

 When authenticating with an IAM user, Console can access and scan functions across multiple regions. 

 Prisma Cloud doesn’t support scanning Serverless functions with IAM policies containing NotAction and/or NotResource elements. 

 IAM Role 

 Scanning Azure Functions 

 Azure Functions are architected differently than AWS Lambda and Google Cloud Functions. Azure function apps can hold multiple functions. The functions are not segregated from each other. They share the same file system. Rather than separately scanning each function in a function app, download the root directory of the function app, which contains all its functions, and scan them as a bundle. 

 Prisma Cloud supports scanning both Windows and Linux functions. For Linux functions, the support is only for functions that use External package URL as the deployment technology. For more information, see Deployment technologies in Azure Functions . 

 To do this, you must know the Region, Name (of the function), and Service Key. To get the Service Key, download and install the Azure CLI , then: 

 Within your Azure portal, create a custom role with the following permissions: 

 Using the CLI, log into your account with a user that has the User Administrator role. 

 Get the service key. 

 Sample output from the previous command: 

 Copy the JSON output, which is your secret key, and paste it into the Service Key field for your Azure credentials in Prisma Cloud Console. 

 Scanning Google Cloud Functions 

 To scan Google Cloud Functions, you must create an appropriate credential to authenticate with GCP. The service account should include the following custom permissions: 

 Prisma Cloud currently supports scanning functions that are packaged with local dependencies. 

 Scanning functions at build time with twistcli 

 You can also use the twistcli command line utility to scan your serverless functions. First download your serverless function as a ZIP file, then run: 

 To view scan reports in Console, go to Monitor > Vulnerabilities > Functions > CI or Monitor > Compliance > Functions > CI . 

 Twistcli Options 

 --details 
Show all vulnerability details. 

 --tlscacert PATH 
Path to Prisma Cloud CA certificate file. If no CA certificate is specified, the connection to Console is insecure. 

 --include-js-dependencies 
Include javascript package dependencies. 

 --token TOKEN 
Token to use for Prisma Cloud Console authentication. Tokens can be retrieved from the API endpoint api/v1/authenticate or from the Manage > Authenticate > User Certificates page in Console. 

 --cloudformation-template PATH 
Path to the CloudFormation template file in JSON or YAML format. Prisma Cloud scans the function source code for AWS service APIs being used, compares the APIs being used to the function permissions, and reports when functions have permissions for APIs they don’t need. 

 --function NAME 
Function name to be used in policy detection and Console results. When creating policy rules in Console, you can target specific rules to specific functions by function name. If this field is left unspecified, the function zip file name is used. 

 --output-used-apis 
Report APIs used by the function 

 --publish 
Publish the scan result to the Console. True by default. 

 Previous Configure Windows Image Scanning 

 Next Configure VMware Tanzu Blobstore Scanning 

 Last updated 1 month ago 

 Was this helpful?
