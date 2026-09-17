---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-on-prem/8.11/configure-cortex-xsoar/integrations/change-the-docker-image-in-an-integration-or-script/connect-your-engine-to-an-image-registry
fetched_at: 2026-09-16T08:54:35Z
source: cortex-platform
---

# Connect your engine to an image registry | 8.11 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 8 

 Cortex XSOAR 8 On-prem Documentation 

 8.11 

 Configure Cortex XSOAR 

 Integrations 

 Change the Docker image in an integration or script 

 Cortex XSOAR 8.11 On-prem 

 Connect your engine to an image registry 

 Connect an engine to an image registry in Cortex XSOAR 8.11 On-prem. 

 Using an engine to communicate with an image registry streamlines deployment by managing dependencies, ensuring version control, and facilitating scalability, load balancing, and secure access to private images. 

 To use an engine, you need to connect the engine to an authenticated Docker image registry and then set it up in the tenant. 

 Note 

 This procedure uses the --username and --password command line options to pass the username and password directly. For environments where command history or logs are visible to others, consider more secure methods like Docker configuration files for handling authentication in production or CI/CD environments. For more details, see docker login or podman-login . 

 Open a terminal on the machine where your engine is running. 

 Run docker login with username and password. 

 Ask Copy 

 docker login --username=<your-username> --password=<your-password> <registry-url> 

 Replace <your-username> , <your-password> , and <registry-url> with your Docker registry credentials and the URL of your Docker image registry. 

 (Optional) Search for or pull a Docker image. 

 After logging in successfully, you can optionally validate access to images by searching for an image or pulling an image from the registry to your local machine using the docker search or docker pull command. 

 Ask Copy 

 docker search <registry-url>/<image-name>:<tag> 
 docker pull <registry-url>/<image-name>:<tag> 

 Replace <registry-url> , <image-name> , and <tag> with your registry URL, the name of the Docker image, and the image tag, respectively. 

 In the tenant, set up the engine to pull images from a private image registry. 

 Previous Change the Docker image in an integration or script 

 Next Pull images from a private image registry 

 Last updated 2 months ago 

 Was this helpful?
