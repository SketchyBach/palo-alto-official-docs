---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-administrator-guide/6.12/onboard-cortex-xsoar/docker/docker-images-in-cortex-xsoar
fetched_at: 2026-09-06T10:46:55Z
source: cortex-platform
---

# Docker Images in Cortex XSOAR | 6.12 (EoL) | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Administrator Guides 

 6.12 (EoL) 

 Onboard Cortex XSOAR 

 Docker 

 Cortex XSOAR 6.12 EoL 

 Docker Images in Cortex XSOAR 

 Run scripts and integrations in Docker images in Cortex XSOAR 6.12. 

 Docker Images 

 Cortex XSOAR maintains a repository of Docker images, all of which are available in the Docker hub under the Demisto organization . The Docker image creation process is managed in the open-source project demisto/dockerfiles . A search of the repository-info branch should be done prior to creating a new image. The repository is updated nightly with all image metadata and os/python packages used in the images. 

 Caution 

 For security, images that are not part of the Demisto organization in Docker hub cannot be accepted. 

 You have the option to use the Cortex XSOAR private container registry , instead of the Docker hub. Docker images can also be downloaded and then copied to a Cortex XSOAR server without internet connectivity. 

 In a high availability deployment, when a custom Docker image is created by a user in Cortex XSOAR, only the application server that receives the command creates the Docker image locally. When a command requiring that image is run on another application server, the image is requested from the application cluster and a copy is created locally. 

 When an engine needs a Docker image it pulls it either from Docker Hub or from a custom registry, if defined in the server configuration: python.docker.registry . 

 The engine can fetch Docker images directly from the Cortex XSOAR server. If the engine fails to fetch the Docker image from the registry it tries to fetch it from the Cortex XSOAR server. The server packages the image when running docker save , and sends it to the engine, which enables the engine to obtain the required images, even if it does not have network access to the Docker Hub. The engine can only obtain images that are available from the server. 

 Script and Integration Configuration 

 Specify which Docker image to use in the Cortex XSOAR IDE (Open: Settings → Docker image name ). If you do not specify an image, a default Docker image using Python 2.7 is used. New scripts and integrations use Python 3, unless there is a specific reason not to use it, such as a need to use a library which is not available for Python 3. 

 Note 

 You can specify in the Cortex XSOAR IDE the Python version (2.7 or 3.x). If 3.x is chosen, the latest Cortex XSOAR Python 3 Docker image is selected automatically. 

 The selected Docker image is configured in the script or integration YAML file under the dockerimage key. 

 If an existing image cannot be found, you can create a Docker image . 

 Update a Docker Image 

 In some cases, a YAML file may specify to use the latest version of a Docker image, instead of a specific version name. In this case, or if a Docker image did not update due to connection issues when new content was downloaded, you can update a Docker image of a script or integration. 

 Docker Files (Required for Production) 

 If the integration is for public release, the integration pushes Docker files into the dockerfiles repository . Pushing into the repository will add an image (after the approval process) to the Docker hub Cortex XSOAR organization. For more information, see Cortex XSOAR’s Dockerfiles and Image Build Management . 

 Caution 

 When modifying an existing Docker image, ensure the change does not disrupt other integrations that may use the same package. All Docker images are created with unique version tags, for which overriding is blocked. When a new version of a Docker image is created, an integration using that image must specify the new version in the YAML file or specify that the latest version of the Docker image should be used. 

 Previous Configure Python Docker Integrations to Trust Custom Certificates 

 Next Create a Docker Image In Cortex XSOAR 

 Last updated 1 month ago 

 Was this helpful?
