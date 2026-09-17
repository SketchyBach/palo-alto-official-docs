---
url: https://docs.prismacloud.io/content-collections/runtime-security/install/deploy-defender/app-embedded/deploy-app-embedded-defender-aci
fetched_at: 2026-09-16T13:35:15Z
source: prisma-cloud
---

# (Dockerfile method) Deploy App-Embedded Defender in ACI | Prisma Cloud arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Enterprise Edition 

 Content Collections 

 Runtime Security 

 Install 

 Deploy the Prisma Cloud Defender 

 Deploy App-Embedded Defender 

 (Dockerfile method) Deploy App-Embedded Defender in ACI 

 Deploy an App-Embedded Defender in ACI to provide runtime protection to App-Embedded applications installed in ACI. The App-Embedded Defender enforces runtime policy on the application entrypoint and any child processes created by this entrypoint. To learn when to use App-Embedded Defenders, see Defender types . 

 To learn more about App-Embedded Defender’s capabilities, see: 

 Vulnerability scanning for App-Embedded 

 Compliance scanning for App-Embedded 

 Runtime defense for App-Embedded 

 Protecting front-end containers at runtime with WAAS 

 System Requirements 

 ACI supports Linux containers 

 App-Embedded Defender image is supported on Linux (x86) architecture 

 Any Docker image with Prisma Cloud App-Embedded Defender binary. 

 Azure Container Registry (ACR) (recommended) 

 Configure App-Embedded Defender in Prisma Console UI 

 Prisma Console provides you with an App-Embedded Defender bundle that contains the Dockerfile with App-Embedded configurations and the Defender installation binary file. 

 You can select one of the Deployment types : Dockerfile or Manual. 

 Dockerfile : Creates a new Dockerfile based on your Dockerfile and embeds the App-Embedded parameters. 

 Manual : Select the manual method to customize the required Dockerfile parameters in the Console UI and directly download the App-Embedded Defender binary file. 

 Prerequisites 

 You can connect to Azure Container Registry(ACR) or any other registry used to pull your images. 

 The container where you are embedding App-Embedded Defender can reach Console’s port 8084 over the network. 

 You have the Dockerfile for your image if you choose the Deployment type as Dockerfile. 

 Embed App-Embedded Defender with Dockerfile 

 Upload your Dockerfile and Prisma Cloud creates a new Dockerfile with App-Embedded Defender parameters and the Defender binary file. 

 Log in to Prisma Cloud Console. 

 Go to Manage > Defenders > Deployed Defenders > Manual deploy . 

 In Deployment method, select Single Defender . 

 Select the Defender type as Container Defender - App-Embedded . 

 Select the DNS name configured in Manage > Defenders > Names (SAN) or public IP address that Defender will use to connect to Prisma Console. 

 Enable file system runtime protection to allow the sensors to monitor file system events regardless of how your runtime policy is configured, and could impact the underlying workload’s performance. 

 Select Deployment type as Dockerfile . 

 In App ID , enter a unique identifier for the App-Embedded Defender. All vulnerability, compliance, and runtime findings for the container will be aggregated under this App ID. In Console, the App ID is presented as the image name. Be sure to specify an App ID that lets you easily trace findings back to the image. 

 In Data folder , enter the path that the Defender will use to write files and store information. 

 Dockerfile : Upload the Dockerfile for your container image. Set up the task’s entrypoint in the Dockerfile. The embed process modifies the container’s entrypoint to run the App-Embedded Defender first, which in turn starts the original entrypoint process. The Defender starts defending the app from the entrypoint and the thread/child process created by this entrypoint. 

 Download the App-embedded bundle that contains the Dockerfile with Defender deployment configurations appended to your Dockerfile and the App-Embedded Defender binary file. 

 Rebuild the image and embed the Defender in ACI. 

 Embed App-Embedded Defender Manually 

 Embed App-Embedded Defender into a container image manually. Modify your Dockerfile with the given configurations, download the App-Embedded Defender binaries into the image’s build context, then rebuild the image. 

 Prerequisites 

 At runtime, the container where you’re embedding App-Embedded Defender can reach Console over the network. For Enterprise Edition, Defender talks to Console on port 443. For Compute Edition, Defender talks to Console on port 8084. 

 The host where you are rebuilding your container image with App-Embedded Defender can reach Console over the network on port 8083. 

 You have the Dockerfile for your image. 

 Log in to Prisma Cloud Console. 

 Go to Manage > Defenders > Deployed Defenders > Manual deploy . 

 In Deployment method, select Single Defender . 

 Select the Defender type as Container Defender - App-Embedded . 

 Select the DNS name (configured in Manage > Defenders > Names (SAN) or public IP address that Defender will use to connect to Prisma Console. 

 Enable file system runtime protection to allow the sensors to monitor file system events regardless of how your runtime policy is configured, and could impact the underlying workload’s performance. 

 Select Deployment type as Manual 

 Follow the instructions for embedding App-Embedded Defender into your image. 

 Download the App-Embedded bundle using the command or download the file directly. 

 Configure your Dockerfile and set the following environment variables: 

 Add the App-Embedded Defender to Dockerfile. 

 Modify the entrypoint so that your app starts under the control of App-Embedded Defender. 

 Rebuild your image and embed the Defender in Cloud instance. 

 Embed App-Embedded Defender in Azure ACI 

 Prisma Cloud uses the updated Dockerfile to deploy the Defender in your containers running in ACI. Use the updated Dockerfile to build the image for App-Embedded Defender, push it to Azure Container Registry, and then run the container instance. 

 Prerequisite : 

 Log in to Azure 

 Create an Azure resource group 

 Create an Azure ACI context 

 You have an image of the Defender binary from the download App-Embedded zipped bundle from Prisma Cloud Console. 

 You have the modified Dockerfile with App-Embedded Defender deployment configurations. 

 Log in to your Azure instances 

 Copy the App-Embedded zipped bundle and unzip it to get the Dockerfile and App-Embedded Defender binary. 

 Build the Dockerfile: 

 If your Dockerfile is in the current directory, use . for <local_path_host-Dockerfile> 

 Start an Azure container instance from this image: 

 Go to Azure Portal > Azure Container Registry > Repositories . Right-click on the App-Embedded image and select Run Instance . 

 Create a container instance and edit the following: 

 Enter the Container name to be the same as the container image name in Azure. 

 Select the OS type as Linux (as Prisma Cloud only supports Linux x86 App-Embedded Defenders). 

 Select Public IP address if you need routable IPs to establish communication between Prisma Console and Defender installed in Azure. 

 Enter the Port defined for the APP in Dockerfile. 

 Select Create . 

 In Azure Container instances, verify that your application shows a running status. 

 This App-Embedded Defender running in ACI is now recognized in Prisma Console under Manage > Defenders > Deployed Defenders . 

 Embed App-Embedded Defender with twistcli 

 Use the twistcli command line tool to embed an App-Embedded Defender in your Cloud Container Registries. 

 Prerequisites : 

 Running tasks can connect to Prisma Cloud Console over the network. 

 Prisma Cloud Defender connects to Console to retrieve runtime policies and send audits. 

 Defender uses port 443 to connect to the Prisma Cloud Console. 

 The container where you’re embedding App-Embedded Defender can reach Console’s port 8084 over the network. 

 You have Dockerfile for you image. 

 Cloud CLI, such as Azure CLI, or Google Cloud CLI. 

 Log in to Prisma Cloud Console. 

 Download twistcli 

 Go to Runtime Security > Manage > System > Utilities , and download twistcli for your platform. 

 Run twistcli to embed Defender in your Cloud Registry (such as Azure, or Google Run). 

 A file named app_embedded_embed <app_id>.zip_ is created, that has the Dockerfile for App-Embedded Defender and App-Embedded Defender binary file. 

 Get the API Token details from Manage > System > Utilities > API token, Token details . 

 <user> — Name of a Prisma Cloud user with a minimum role of Defender Manager. 

 <password> — For Prisma Cloud Enterprise Edition, you can also specify the secret key that you configured under Prisma > Settings > Access Control > Access Keys . 

 <token> — API Token for authenticating with Prisma Cloud Console. (For Enterprise Edition only) 

 <CONSOLE> — DNS name or IP address for Console. 

 <APP-ID> — Unique identifier. 

 When setting <APP-ID> , specify a value that lets you easily trace findings back to the image. All vulnerability, compliance, and runtime findings for the container will be aggregated under this App ID. 

 In Console, the App ID is presented as the image name. 

 <DATA-FOLDER> — Readable and writable directory in the container’s filesystem. 

 To enable file system protection, add the --filesystem-monitoring flag to the twistcli command. 

 Unpack app_embedded_embed_help.zip . 

 Create and push the docker image to ACR 

 Check the image exists in Azure repo 

 Create a container instance (ACI) 

 Delete a Container Instance 

 View Deployed Defenders 

 You can review the list of all Defenders connected to Console under Runtime Security > Manage > Defenders > Deployed Defenders . 

 To narrow the list to just App-Embedded Defenders, filter the table by type Type: Container Defender - App-Embedded . 

 By default, Prisma Cloud removes disconnected App-Embedded Defenders from the list after an hour. As part of the cleanup process, data collected by the disconnected Defender is also removed from Monitor > Runtime > App-Embedded observations . 

 There is an advanced settings dialog under Runtime Security > Manage > Defenders > Deployed Defenders , which lets you configure how long Prisma Cloud should wait before cleaning up disconnected Defenders. This setting doesn’t apply to App-Embedded Defenders. Disconnected App-Embedded Defenders are always removed after one hour. 

 Trigger Events for App-Embedded 

 Refer to Runtime defense for App-Embedded . 

 Monitor App-Embedded Events 

 You can view the App-Embedded runtime events by app ID under Monitor > Events > App-Embedded audits , and view the App-Embedded incidents under Monitor > Runtime > Incident Explorer . 

 You can also deploy WAAS for Containers Protected By App-Embedded Defender , create a WAAS rule policy, add an app, enable protections, run WAAS sanity tests, and monitor the events under Monitor > Events > WAAS for App-Embedded . 

 Previous (Dockerfile method) Deploy App-Embedded Defender for Fargate 

 Next (Dockerfile method) Deploy App-Embedded Defender in GCR 

 Last updated 1 month ago 

 Was this helpful?
