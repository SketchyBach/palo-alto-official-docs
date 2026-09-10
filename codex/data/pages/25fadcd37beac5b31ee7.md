---
url: https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/cortex-cloud-data-sources-and-connectors/cloud-posture-and-runtime-security-data-sources/container-registry-scanning/connect-gitlab-container-registry
fetched_at: 2026-09-06T10:01:54Z
source: cortex-platform
---

# Connect GitLab container registry | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Cortex CLOUD Runtime Security 

 Cortex Cloud Data Sources and Connectors 

 Cloud Posture and Runtime Security data sources 

 Container Registries 

 Connect GitLab container registry 

 Configure Cortex Cloud to scan your GitLab Container Registry without using administrator credentials. Use a GitLab Personal Access Token (PAT) to authenticate Cortex to access the GitLab Container Registry. This allows Cortex to list all container registries or images, and secure them from vulnerabilities, malware, and secrets. 

 How to connect GitLab registry 

 Follow the wizard to connect the GitLab Container Registry connector in Cortex Cloud. 

 Navigate to Settings → Data Sources & Integrations . 

 On the Add Data Sources or Integrations page, click + Add New , search for GitLab Container Registry , then hover over it and click Add. 

 The Instance Name is automatically populated. You can change it to a more meaningful name. 

 Choose the Scan Mode , and then follow the steps provided for that mode to configure the connection. 

 Cloud Scan 

 Security scanning is done in the Cortex Cloud environment when you select this mode. 

 Select the appropriate Cloud Provider and Region for the Cortex environment to use for registry scanning. 

 As a best practice, choose the region closest to your registry deployment to achieve the best scanning throughput and potentially reduce cloud costs. 

 (Optional) Enable Allow access by IPs to specify a static IP address for the scanner to use. Make sure the static IP is allowed through your firewall so the scanner can access the registry during the scanning process. 

 Choose the relevant Account Type for GitLab deployments: 

 GitLab Cloud (Saas) 

 (Optional) Enter the Group Id . 

 You can enter a single group ID or a list of group IDs separated by a comma. The group ID is used to locate all the registries within a specific group. 

 (Optional) Enter the Project Id . 

 You can enter a GitLab Project ID or a list of project IDs separated by a comma. The project ID is used to locate all the registries located within a specific project. 

 When both the group ID and project ID are provided, the system retrieves container images from all projects within the specified group as well as from the specified project. 

 If neither the group ID nor the project ID is provided, the system retrieves container images from all registries (across all groups and projects) accessible to the authenticated user or token in GitLab. 

 Under Authentication Method , enter your GitLab Access Token . 

 GitLab Self-Hosted 

 Enter the Registry URL . 

 If you are using a CA certificate, enter the server IP address instead of the registry url. 

 (Optional) Enter the Group id . 

 You can enter a single group ID or a list of group IDs separated by a comma. The group ID is used to locate all the registries within a specific group. 

 (Optional) Enter the Project Id . 

 You can enter a GitLab Project ID or a list of project IDs separated by a comma. The project ID is used to locate all the registries located within a specific project. 

 When both the group ID and project ID are provided, the system retrieves container images from all projects within the specified group as well as from the specified project. 

 If neither the group ID nor the project ID is provided, the system retrieves container images from all registries (across all groups and projects) accessible to the authenticated user or token in GitLab. 

 Enter the Api Domain . Include the GitLab API base URL with the https:// prefix (for example, https://gitlab.example.dev ). 

 Under Authentication Method, enter your GitLab Access Token . 

 (Optional) Expand Show Advanced Settings , and then enter the CA certificate in PEM format for Cortex to validate the GitLab registry. 

 Select Next. 

 Scan with Outpost 

 Security scanning is done on infrastructure deployed to a cloud account that you own. This mode requires additional cloud provider permissions and may incur extra costs. 

 Prerequisite 

 Ensure an Outpost is connected to your tenant. 

 Choose a Cloud Provider to initialize registry scanning. 

 Note 

 If you choose Azure as the Cloud Provider , you must also select the Tenant Id. The Tenant Id is required to approve Cortex as an enterprise application in your Azure tenant. 

 Choose Outpost account to use for this instance. If no Outposts are shown, you can Create a new one. For more details, see Outposts . 

 Note 

 If you choose Azure as the cloud provider, only Outposts associated with the selected tenant ID are displayed. 

 Select the Region where the registry is hosted. 

 (Optional) Enable Allow access by IPs if you want to specify a static IP address for the scanner to use. Make sure the static IP is allowed through your firewall so that the scanner can access the registry during the scanning process. 

 Choose the relevant Account Type for GitLab deployments: 

 GitLab Cloud (Saas) 

 (Optional) Enter the Group Id . 

 You can enter a single group ID or a list of group IDs separated by a comma. The group ID is used to locate all the registries within a specific group. 

 (Optional) Enter the Project Id . 

 You can enter a GitLab Project ID or a list of project IDs separated by a comma. The project ID is used to locate all the registries located within a specific project. 

 When both the group ID and project ID are provided, the system retrieves container images from all projects within the specified group as well as from the specified project. 

 If neither the group ID nor the project ID is provided, the system retrieves container images from all registries (across all groups and projects) accessible to the authenticated user or token in GitLab. 

 Under Authentication Method , enter your GitLab Access Token . 

 GitLab Self-Hosted 

 Enter the Registry URL . 

 If you are using a CA certificate, enter the server IP address instead of the registry url. 

 (Optional) Enter the Group id . 

 You can enter a single group ID or a list of group IDs separated by a comma. The group ID is used to locate all the registries within a specific group. 

 (Optional) Enter the Project Id . 

 You can enter a GitLab Project ID or a list of project IDs separated by a comma. The project ID is used to locate all the registries located within a specific project. 

 When both the group ID and project ID are provided, the system retrieves container images from all projects within the specified group as well as from the specified project. 

 If neither the group ID nor the project ID is provided, the system retrieves container images from all registries (across all groups and projects) accessible to the authenticated user or token in GitLab. 

 Enter the Api Domain . Include the GitLab API base URL with the https:// prefix (for example, https://gitlab.example.dev ). 

 Under Authentication Method, enter your GitLab Access Token . 

 (Optional) Expand Show Advanced Settings , and then enter the CA certificate in PEM format for Cortex to validate the GitLab registry. 

 Select Next. 

 Scan with Broker VM 

 Security scanning in private networks is performed using broker VM infrastructure when you select this mode. 

 Prerequisite 

 Ensure one of the following is configured: 

 Set up and configure Broker VM . 

 Configure High Availability Cluster . 

 Choose a Scan with Broker VM mode to initiate registry scanning. You can select either a standalone Broker VM or a High Availability (HA) Cluster . 

 Select Applicable Broker VMs . 

 Choose the appropriate Broker VM or Cluster from the list configured in your tenant. 

 Note 

 The list of Broker VMs displays only VMs that support registry scanning. 

 The list of high-availability Clusters displays only clusters that contain at least one VM supporting registry scanning. 

 The registry scanning status for each VM appears in brackets if it was previously activated for that specific VM. 

 If the list does not display any Broker VMs or clusters , Add New Broker VM or A dd New Cluster . For more details, see Set up and configure Broker VM . 

 Choose the relevant Account Type for GitLab deployments: 

 GitLab Cloud (Saas) 

 (Optional) Enter the Group Id . 

 You can enter a single group ID or a list of group IDs separated by a comma. The group ID is used to locate all the registries within a specific group. 

 (Optional) Enter the Project Id . 

 You can enter a GitLab Project ID or a list of project IDs separated by a comma. The project ID is used to locate all the registries located within a specific project. 

 When both the group ID and project ID are provided, the system retrieves container images from all projects within the specified group as well as from the specified project. 

 If neither the group ID nor the project ID is provided, the system retrieves container images from all registries (across all groups and projects) accessible to the authenticated user or token in GitLab. 

 Under Authentication Method , enter your GitLab Access Token . 

 GitLab Self-Hosted 

 Enter the Registry URL . 

 If you are using a CA certificate, enter the server IP address instead of the registry url. 

 (Optional) Enter the Group id . 

 You can enter a single group ID or a list of group IDs separated by a comma. The group ID is used to locate all the registries within a specific group. 

 (Optional) Enter the Project Id . 

 You can enter a GitLab Project ID or a list of project IDs separated by a comma. The project ID is used to locate all the registries located within a specific project. 

 When both the group ID and project ID are provided, the system retrieves container images from all projects within the specified group as well as from the specified project. 

 If neither the group ID nor the project ID is provided, the system retrieves container images from all registries (across all groups and projects) accessible to the authenticated user or token in GitLab. 

 Enter the Api Domain . Include the GitLab API base URL with the https:// prefix (for example, https://gitlab.example.dev ). 

 Under Authentication Method, enter your GitLab Access Token . 

 (Optional) Expand Show Advanced Settings , and then enter the CA certificate in PEM format for Cortex to validate the GitLab registry. 

 Select Next. 

 In the Initial Scan Configuration , set your scanning process to focus on recently added or modified container images and exclude older ones that do not align with your current scanning objectives. This setting helps avoid unnecessary scans. Choose one of the following options: 

 All: Scans all container images, including all versions (tags), in all discovered repositories. 

 Latest Tag : Scans only images tagged 'latest' in all discovered repositories. 

 Days Modified : Scans container images that have been created in the last few days. You can select a range of up to 90 days for the scan. 

 Select Save . 

 When the GitLab data source is saved successfully, a new data connector is created, and the initial discovery scan is started. The connection process may take up to 15 minutes. 

 To check connector status and scan results, follow these steps: 

 Navigate to Settings → Data Sources & Integrations . 

 Find the GitLab Container Registry instance from the list of 3rd Party Data Sources connectors, or use Search . 

 In the GitLab Container Registry instance row, select View Details . The GitLab Instances page appears. 

 On the GitLab Instances page, you can filter results by any heading and value. 

 Select an instance name to open the details pane. The details pane contains the following granular information: 

 Instance Details 

 Description 

 Status 

 Shows the status of the connector: Connected, Error , Warning , Disabled , or Pending . 

 Applet Status on Broker VM 

 Shows the status of the Registry Scanner applet on the Broker VM page. This status is visible only when the Scan with Broker VM mode is selected. 

 Repositories 

 Shows the number of scanned repositories in the registry. 

 Scan Mode 

 Shows the selected scan mode for the data connector, such as Cloud Scan , Scan with Outpost , or Scan with Broker VM . 

 Security Capabilities 

 Shows a breakdown of the security capabilities enabled on the instance and their individual statuses. For example, select Registry Scanning when it shows a warning or error status to see the open errors and issues that contributed to the status. 

 Next Steps . 

 After the scan is complete, you can view the scanned images on the Container Images Inventory page. For more details, see Container Images assets . 

 If you have selected the Scan with Broker VM option, then a Registry Scanner applet is created on the selected Broker VM or Cluster . For details, see Verify Registry Scanner connection . 

 Previous Manage a Docker V2 connector 

 Next Manage a GitLab Container Registry connector 

 Last updated 1 month ago 

 Was this helpful?
