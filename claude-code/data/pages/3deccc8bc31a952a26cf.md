---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-3.x/cortex-xdr-3.x-documentation/data-management/broker-vm/set-up-and-configure-broker-vm/broker-vm-image-installations/set-up-broker-vm-on-microsoft-azure
fetched_at: 2026-09-06T09:49:46Z
source: cortex-platform
---

# Set up Broker VM on Microsoft Azure | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR 

 Cortex XDR 3.x Documentation 

 Cortex XDR 3.x Documentation 

 Data management 

 Broker VM 

 Set up and configure Broker VM 

 Broker VM image installations 

 Cortex XDR 3.x 

 Set up Broker VM on Microsoft Azure 

 Learn how to set up your Cortex XDR Broker virtual machine (VM) on Microsoft Azure. 

 After you download your Cortex XDR Broker VHD (Azure) image, you need to upload it to Azure as a storage blob. 

 Prerequisite 

 Download a Cortex XDR Broker VM VHD (Azure) image. For more information, see the virtual machine compatibility requirements in Set up and configure Broker VM . 

 Perform the following procedures in the order listed below. 

 Task 1. Extract the downloaded VHD (Azure) image 

 Make sure you extract the zipped hard disk file on a server that has more then 512 GB of free space. 

 Note 

 Extraction can take up to a few hours. 

 Task 2. Create a new storage blob on your Azure account by uploading the VHD file 

 Upload from Microsoft Windows or Ubuntu. 

 Windows 

 Verify you have: 

 Windows PowerShell version 5.1 or later. 

 .NET Framework 4.7.2 or later. 

 Open PowerShell and run Set-ExecutionPolicy unrestricted . 

 [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12 

 Install-PackageProvider -Name NuGet -MinimumVersion 2.8.5.201-Force 

 Install azure cmdlets . 

 Install-Module -Name Az -AllowClobber 

 Connect to your Azure account. 

 Connect-AzAccount 

 Start the upload. 

 For Azure PowerShell: 

 Ask Copy 

 Set-AzStorageBlobContent -Container $containerName -File $localFilePath -Context $storageContext -BlobType Page 

 For Azure CLI: 

 Ask Copy 

 az storage blob upload -f <vhd to upload> -n <vhd name> -c <container name> --account-name <account name> 

 Note 

 Upload can take up to a few hours. 

 Linux 

 Option 1: 

 Ask Copy 

 curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash 

 Option 2: 

 Get the packages needed for the installation process: 

 Ask Copy 

 sudo apt-get update 
 sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release 

 Download and install the Microsoft signing key: 

 Ask Copy 

 sudo mkdir -p /etc/apt/keyrings 
 curl -sLS https://packages.microsoft.com/keys/microsoft.asc | 
 gpg --dearmor | sudo tee /etc/apt/keyrings/microsoft.gpg > /dev/null 
 sudo chmod go+r /etc/apt/keyrings/microsoft.gpg 

 Add the Azure CLI software repository: 

 Ask Copy 

 AZ_DIST=$(lsb_release -cs) 
 echo "Types: deb 
 URIs: https://packages.microsoft.com/repos/azure-cli/ 
 Suites: ${AZ_DIST} 
 Components: main 
 Architectures: $(dpkg --print-architecture) 
 Signed-by: /etc/apt/keyrings/microsoft.gpg" | sudo tee /etc/apt/sources.list.d/azure-cli.sources 

 Update repository information and install the azure-cli package: 

 Ask Copy 

 sudo apt-get update 
 sudo apt-get install azure-cli 

 Install Azure util. 

 There are two different ways to install the Azure util. 

 Note 

 For more information, see the Azure Documentation . 

 Connect to Azure. 

 az login 

 Start the upload. 

 az storage blob upload -f <vhd to upload> -n <vhd name> -c <container name> --account-name <account name> 

 Task 3. Add and configure a new disk in Azure 

 In the Azure home page, navigate to Azure services → Disks and Add a new disk. 

 Navigate to the Create a managed disk → Basics page, and define the following information: 

 Heading 

 Parameter 

 Project details 

 Resource group : Select your resource group. 

 Disk details 

 Disk name : Enter a name for the disk object.

 Region : Select your preferred region.

 Source type : Select Storage Blob .

Additional fields are displayed, which you can define as follows: 

 Source blob : 

 Select Browse . You are directed to the Storage accounts page. 

 From the navigation panel, select the bucket and then container to which you uploaded the Cortex XDR VHD image. 

 In the Container page, Select your VHD image. 

 OS type : Select Linux 

 VM generation : Select Gen 1 

 Check you settings by clicking Review + create . 

 Task 4. Create the Broker VM disk 

 Create your Broker VM disk, and after deployment is complete, click Go to resource . 

 In your created Disks page, click Create VM . 

 In the Create a virtual machine page, define the following: 

 Read more... 

 | 

 Heading 

 | 

 Parameter 

 | |----|----| | 

 Instance details 

 | 

 (Optional) Virtual machine name : Enter the same name as the disk name you defined. 

 | | 

 Size : Select the size according to your company guidelines. 

 Select Next to navigate to the Networking tab. 

 | | | 

 Network interface 

 | 

 NIC network security group —Select Advanced . 

 | | 

 Configure network security group —Select HTTPS to be able to access the Broker VM Web UI, and SSH to allow for remote access when troubleshooting. Make sure to allow these connection to the Broker VM from secure networks only. 

 | | 

 To check your settings, click Review + create . 

 Create your VM. 

 After deployment is complete, click Go to resource . You are directed to your VM page. 

 Note 

 Creating the VM can take up to 15 minutes. The Broker VM Web UI is not accessible during this time. 

 Ensure that the VM you created contains an Outbound port rule that allows the broker to reach the Azure Instance Metadata Service using the IP address 169.254.169.254 and port 80 . For more information about the Azure Instance Metadata Service, see the Azure Documentation . 

 To configure an outbound rule on your VM, select Networking → Network settings , and under the Rules → Outbound port rules section, you can either: 

 Note 

 For more information on creating a rule in an Azure VM, see Create a Security Rule in the Azure Documentation. 

 Configure a new outbound port rule by selecting Create port rule → Outbound port rule and setting the following settings in the Add outbound security rule dialog box: 

 Destination : Select IP Addresses . 

 Destination IP addresses/CIDR ranges : Enter the IP address as 169.254.169.254 . 

 Destination port ranges : Enter the port as 80 . 

 Protocol : Select TCP . 

 Name : Enter a unique name for this new outbound port rule, such as AzureInstanceMetadataService . 

 Click Add to create the new outbound port rule. 

 Edit an existing outbound port rule and ensure that the settings provided above for creating a new outbound port rule match what is already configured in the rule. 

 Previous Set up Broker VM on KVM using Ubuntu 

 Next Set up Broker VM on Microsoft Hyper-V 

 Last updated 10 days ago 

 Was this helpful?
