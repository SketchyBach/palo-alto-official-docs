---
url: https://docs.prismacloud.io/admin-guide/tools/twistcli-scan-images
fetched_at: 2026-09-16T13:36:37Z
source: prisma-cloud
---

# Scan images with twistcli | Prisma Cloud arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Compute Edition 

 Admin Guide 

 34 

 Tools 

 Scan images with twistcli 

 You can use the Prisma Cloud twistcli command-line tool to scan container images and serverless functions. Scanning with twistcli is supported on Linux, macOS, and Windows. 

 Command 

 The twistcli command-line tool has several subcommands. To scan, use the following subcommand. 

 Ask Copy 

 twistcli images scan 

 The command scans an image for vulnerabilities and compliance issues. The image must be on the system running the twistcli command-line tool. If not and if you are using Docker, you can retrieve the image with the docker pull before scanning it. The twistcli tool does not pull images. 

 Syntax 

 When using twistcli images scan , the image or tarball to scan must be the last parameter. If you specify options after the image or tarball, they are ignored. If scanning a tarball, use the --tarball option. 

 Ask Copy 

 twistcli images scan [OPTIONS] [ IMAGE ] 

 Description 

 The twistcli images scan tool collects information about the packages and binaries in the container image, and sends the information to the Prisma Cloud Console for analysis. 

 The twistcli tool collects data including the following items. 

 Packages in the image. 

 Files installed by each package. 

 Hashes for files in the image. 

 After the Prisma Cloud Console analyzes the image for vulnerabilities, twistcli performs the following tasks. 

 Outputs a summary report. 

 Exits with a pass or fail return value. 

 To specify an image to scan, use either the image ID, or repository name and tag. If you are using Windows with containerd , provide a full image ID because short IDs aren’t supported. Get the full image ID using the following command. 

 The image should be present on the system, having either been built or pulled there. If a repository is specified without a tag, twistcli looks for an image tagged latest . 

 Options 

 --output-file FILENAME 

 Write the results of the scan to a file in JSON format. 

 Example: --output-file scan-results.json 

 --details 

 Show all vulnerability details. 

 --containerized 

 Run the scan from inside the container. 

 --custom-labels 

 Include the image custom labels in the results. 

 --docker-address DOCKER_CLIENT_ADDRESS 

 Docker daemon listening address (default: unix:///var/run/docker.sock ). Can be specified with the DOCKER_CLIENT_ADDRESS environment variable. 

 --docker-tlscacert PATH 

 Path to Docker client CA certificate. 

 --docker-tlscert PATH 

 Path to Docker client Client certificate. 

 --docker-tlskey PATH 

 Path to Docker client Client private key. 

 --containerd 

 Scans images in a containerd environment. 

 --containerd-address value 

 Containerd daemon listening address (default: "/var/run/containerd/containerd.sock"). 

 --containerd-namespace value 

 Containerd target namespace (default: "default"). 

 --docker-runtime 

 Specifies that the running host uses a Docker container runtime, to evaluate the Docker image Compliance benchmark (supported with --tarball). 

 --project value 

 Target project 

 --exit-on-error TRUE/FALSE 

 Immediately exit the scan if an error is encountered (not supported with the --containerized flag). 

 --tlscacert PATH 

 Path to Prisma Cloud CA certificate file. If no CA certificate is specified, the connection to Console is insecure. 

 --podman-path PATH 

 Forces twistcli to use Podman. To use the default installation path, set as podman . Otherwise, provide the appropriate path. 

 --include-js-dependencies 

 Evaluates packages listed only in manifests. 

 --disable-symbol-extraction 

 Disables Go symbol extraction when scanning the image. 

 --SBOM [file_format] 

 Exports Software Bill of Materials (SBOM) for the image in the CycloneDX v1.4 standard ( JSON or XML ). The file_format values are cyclonedx_json or cyclonedx_xml . 

 --include-purl 

 Adds package URLs for packages and vulnerabilities. 

 --token TOKEN 

 Token to use for Prisma Cloud Console authentication. Tokens can be retrieved from the API endpoint api/v1/authenticate or from the Manage > System > Utilities page in Console. 

 --publish TRUE/FALSE 

 Publishes scan results to the Console (default: --publish=true) 

 --tarball 

 Boolean flag that specifies the image to scan is a tar archive. The tarball scan requires enhanced privileges, and must be executed as sudo or as a root user. Prisma Cloud supports tar archives in the Docker Image Specification format, v1.1 and later. 

 The tarball option is supported on Linux only; macOS and Windows versions of twistcli do not support it. 

 The last parameter in the twistcli command should always be the path to the tarball. The --tarball option is simply a boolean flag. It doesn’t accept a corresponding value (e.g. a path to a tarball). For clarity, see the following examples: 

 Correct usage: 

 Incorrect usage: 

 Return Value 

 The exit code is 0 if twistcli images scan finds no vulnerabilities or compliance issues. Otherwise, the exit code is 1. 

 The criteria for passing or failing a scan is determined by the CI vulnerability and compliance policies set in Console. The default CI vulnerability policy alerts on all CVEs detected. The default CI compliance policy alerts on all critical and high compliance issues. 

 The twistcli images scan returns an exit code of 1 in the following scenarios: 

 The scan failed because the scanner found issues that violate your CI policy. 

 Twistcli failed to run due to an error. 

 Although the return value is ambiguous — you cannot determine the exact reason for the failure by just examining the return value — this setup supports automation. From an automation process perspective, you expect that the entire flow will work. If you scan an image, with or without a threshold, either it works or it does not work. If it fails, for whatever reason, you want to fail everything because there is a problem. 

 Scan Results 

 To view scan reports in Console, go to Monitor > Vulnerabilities > Images > CI or Monitor > Compliance > Images > CI . 

 The scan reports includes the image vulnerabilities, compliance issues, layers, process info, package info, and labels. 

 When scanning images in the CI pipeline with twistcli or the Jenkins plugin , Prisma Cloud collects the environment variable JOB_NAME from the machine the scan ran on, and adds it as a label to the scan report. 

 You can also retrieve scan reports in JSON format using the Prisma Cloud API, see the API section. 

 Output 

 The twistcli tool can output scan results to several places: 

 stdout. 

 JSON file. 

 Console. Scan results can be viewed under Monitor > Vulnerabilities > Images > CI and Monitor > Compliance > Images > CI . 

 By passing certain flags, you can adjust how the twistcli scan output looks and where it goes. By default, twistcli writes scan results to stdout and sends the results to Console. 

 To write scan results to stdout in tabular format, pass the --details flag to twistcli. This does not affect where the results are sent. 

 To write scan results to a file in JSON format, pass the --output-file flag to twistcli. The file schema is being kept for backwards compatibility. 

 Following is the output file schema: 

 List of vulnerabilities 

 This section discusses the contents of the scan results when retrieved from the API. 

 Once retrieving the results of a scan via an API call, the list of vulnerabilities in an image can be found under the "cveVulnerabilities" attribute. Each vulnerability has the following name-value pairs: 

 CVE identifier 

 CVSS (CVE score) 

 Description of the vulnerability. 

 Link to CVE report 

 Name of the package to which this CVE applies 

 Version of the package to which this CVE applies 

 Severity of this vulnerability For example, here is a subset of the CVE information: 

 List of packages 

 This section discusses the contents of the scan results when retrieved from the API. The list of content found in an image is found in the data attribute of the JSON. The API results lists all packages in the image under the info/data/packages attribute. 

 Each package has the following name-value pairs: 

 Package name 

 Package version 

 CVE Count for the package For example: 

 Projects 

 When users from a tenant project run twistcli, they must set the --project option to specify the proper context for the command. 

 twistcli images scan --project "<project_name>" 

 API 

 You can retrieve scan reports in JSON format using the Prisma Cloud Compute API. The API returns comprehensive information for each scan report, including the full list of packages, files, and vulnerabilities. 

 The following example curl command calls the API with Basic authentication. You’ll need to apply some filtering with tools like jq to extract specific items from the response. For more information on accessing the API, see the API reference . 

 If you are using assigned collections, then specify the collection in a query parameter: 

 Dockerless Scan 

 By default, twistcli is run from outside the container image. 

 Podman Twistcli Scans 

 Twistcli can run scans on Podman hosts. Use --podman-path PATH to specify the path to podman and force the twistcli scanner to use podman. For additional information, see the Podman section. 

 Running from inside a Container 

 In some cases, you might need to copy twistcli to the container’s file system, and then run the scanner from inside the container. 

 One reason you might want to run the scanner this way is when your build platform doesn’t give you access to the Docker socket. CodeFresh is an example of such a platform. 

 There are some shortcomings with scanning from inside a container, so you should only use this approach when no other approach is viable. The shortcomings are: 

 Automating the scan in your continuous integration pipeline is more difficult. 

 Image metadata, such as registry, repository, and tag aren’t available in the scan report. When twistcli is run from outside the container, this information is retrieved from the Docker API. 

 The image ID isn’t available in the scan report because it cannot be determined when the scan is run from inside a container. 

 The scan report won’t show a layer-by-layer analysis of the image. 

 To run a twistcli image scan within a container and without passing the --containerized flag, you need to run the container as a privileged container. 

 Usage 

 When running the scanner from inside a container, you need to properly orient it by passing it the --containerized flag. There are a couple of ways to run twistcli with the --containerized flag: build-time and run-time. 

 For security reasons, Prisma Cloud recommends that you create a user with the CI User role for running scans. 

 Build-time Invocation 

 After building an image, run it. Mount the host directory that holds the twistcli binary, pass the Prisma Cloud Console user credentials to the container with environment variables, then run the scanner inside the container. The <REPORT_ID> is a user defined string that uniquely identifies the scan report in the Console UI. 

 Rather than username and password, twistcli can also authenticate to Console with a token. Your API token can be found in Console under Manage > System > Utilities > API token . 

 Run-time Invocation 

 If you have access to the orchestrator, you can exec into the running container to run the twistcli scanner. Alternatively, you could SSH to the container. Once you have a shell on the running container, invoke the scanner: 

 To invoke the scanner with an API token: 

 Simple Scan 

 Scan an image with twistcli and print the summary report to stdout. 

 Scan an image named nginx:latest . 

 Command output: 

 Scan with Detailed Report 

 You can have twistcli generate a detailed report for each scan. The following procedure shows you how to scan an image with twistcli, and then retrieve the results from Console. 

 Scan an image named nginx:latest . 

 Sample command output (results have been truncated): 

 This outputs a tabular representation of your scan results to stdout. If you need to retrieve the results of your scan in JSON format, this can be done using the API. For more information on the API, see the API reference . 

 Call the API with authentication (demonstrated here using Basic authentication) to fetch the results of the scan. 

 Format the scan results into human-readable format. 

 Inspect the results. 

 Open scan_results_pp.json to view the results. Vulnerability information can be found in the vulnerabilities array, and compliance results can be found in the complianceIssues array. 

 Scan Images Built with Jenkins in an OpenShift Environment 

 If you are building and deploying images on OpenShift Container Platform (OCP), and you are utilizing their Jenkins infrastructure, then invoke a scan with the twistcli hosts scan command, not the twistcli images scan command. 

 You can scan images generated by Jenkins with the OpenShift plugin by invoking twistcli from a build hook . Build hooks let you inject custom logic into the build process. They run your commands inside a temporary container instantiated from build output image. Build hooks are called when the last layer of the image has been committed, but before the image is pushed to a registry. An non-zero exit code fails the build. A zero exit code passes the build, and allows it to proceed to the next step. 

 To call twistcli from a build hook: 

 Download twistcli into your build environment. Depending on your build strategy, one option is to download it as an external artifact using a save-artifacts S2I script . 

 In your BuildConfig , call twistcli as a script from the postCommit hook. 

 Where the --skip-docker option skips all Docker compliance checks such as the Docker daemon configuration and the --include-3rd-party option scans application-specific files such as JARs. 

 Scan Images when the Docker Docket Isn’t in the Default Location 

 The twistcli scanner uses the Docker API, so it must be able to access the socket where the Docker daemon listens. If your Docker socket isn’t in the default location, use the --docker-address option to tell twistcli where to find it: 

 --docker-address PATH 
Path to the Docker socket. By default, twistcli looks for the Docker socket unix:///var/run/docker.sock . 

 Options 

 --address URI 

 -u, --user USERNAME 

 -p, --password PASSWORD 

 --output-file FILENAME 

 --details 

 --containerized 

 --docker-tlscacert PATH 

 --docker-tlscert PATH 

 --docker-tlskey PATH 

 --tlscacert PATH 

 Scan Podman/CRI Images 

 Podman is a daemon-less container engine for developing, managing, and running OCI containers on Linux. The twistcli tool can use the preinstalled Podman binary to scan CRI images. NOTE: To run a twistcli image scan within a container using podman and without passing the --containerized flag, you need to run the container as a privileged container. 

 --podman-path PATH 
Forces twistcli to use Podman. To call podman from its default install path, specify podman . Otherwise, specify an explicit path. 

 CI/CD Automation 

 Twistcli images scan can be used to shift-left security scans inside of your build pipeline. Plugins are available for Jenkins and other CI/CD tools, but twistcli can also be used from a CI pipeline in order to initiate vulnerability and compliance scans on images. 

 The exit status code can be verified inside of your pipeline to determine pass and fail status of the image scan. A zero exit code signals the scan passes, and any non-zero exit code signals a failure. 

 In order to automate the download and version sync of twistcli, reference the sample Jenkins code below: 

 Scan Image Tarballs 

 twistcli can scan image tarballs. This capability is designed to support the following workflows: 

 Integration with Kaniko. Kaniko is a tool that builds images in a Kubernetes cluster from a Dockerfile without access to a Docker daemon. 

 Vendors deliver container images as tar files, not through a registry. 

 twistcli supports the Docker Image Specification v1.1 and later. Currently, twistcli doesn’t support the Open Container Initiative (OCI) Image Format Specification . 

 Both Kaniko and the docker save command output tarballs using the Docker Image Specification. 

 To scan an image tarball, specify the --tarball option: 

 For example: 

 Scan Windows Images on Windows Hosts with containerd 

 You can use twistcli to scan Windows images on Windows hosts with containerd installed. 

 Windows requires the host OS version to match the container OS version. If you want to run a container based on a newer Windows build, make sure you have an equivalent host build. Otherwise, you can use Hyper-V isolation to run older containers on new host builds. For more information, see Windows containers version compatibility . 

 Scan Images on Linux Hosts with containerd 

 You can use twistcli to scan images on Linux hosts with containerd installed. 

 The image ID passed to twistcli must be the full length image ID . Short IDs aren’t supported. Get full-length image IDs using the following command. 

 Download the ctr utility. 

 Limitations 

 Due to a bug in Kaniko, twistcli can’t map vulnerabilities to layers when scanning image tarballs built by Kaniko. 

 Previous twistcli 

 Next Scan code repos with twistcli 

 Last updated 1 month ago 

 Was this helpful?
