---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-administrator-guide/6.14/onboard-cortex-xsoar/docker/docker-images-in-cortex-xsoar/create-a-docker-image-in-cortex-xsoar
fetched_at: 2026-09-16T08:56:00Z
source: cortex-platform
---

# Create a Docker Image In Cortex XSOAR | 6.14 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Administrator Guides 

 6.14 

 Onboard Cortex XSOAR 

 Docker 

 Docker Images in Cortex XSOAR 

 Cortex XSOAR 6.14 

 Create a Docker Image In Cortex XSOAR 

 Create a custom Docker image for Cortex XSOAR 6.14 integrations and automations. 

 After due diligence has been completed and licenses checked, the following steps can be taken. 

 Note 

 When using a custom Docker registry, including the Cortex XSOAR Container Registry, you must include localhost when you create a custom Docker image. Examples: 

 localhost.local/directory/container_name 

 localhost/directory/container_name 

 Before creating a new Docker image, we recommend you review the used_packages.csv file in the GitHub dockerfiles repository to determine if any existing Docker images already contain the Python modules you need. Find Requests in the Package Name column and scroll to the right to view the list of Docker images, and then search for the relevant Docker container name to view which modules are included in that image. Determine if the existing image is appropriate for your needs. If so, use the existing Docker image. If not, proceed with the following steps to create a new custom Docker image. 

 In the War Room, type the following command: 

 /docker_image_create name 

 Add the following arguments: 

 Argument 

 Description 

 name 

 New Docker image name. Lower case only 

 dependencies 

 New Docker image dependencies. Python libs like stix or requests; can have multiple comma-separated libs: lib1,lib2,lib3 . 

 packages 

 New Docker image packages. OS packages like libxslt or wget; can have multiple comma-separated packages: pkg1,pkg2,pkg3 . 

 base 

 New Docker image base image to use. It must be Ubuntu-based with Python installed. The default is the demisto/python3-deb base image, with Python 3.x. 

 In the following example, create a Docker image called example_name and use the Python dependency, Mechanize . You can specify OS packages. This example requires wget as a package. 

 /docker_image_create name=example_name dependencies=mechanize packages=wget 

 Note 

 For Python modules, dependencies are not automatically added. If a Python module has dependencies, you need to specify them. 

 Example of a request including the idna and chardet dependencies: 

 /docker_image_create name=custom/requests dependencies=idna,chardet,requests base="demisto/python3-deb:3.10.12.63475 

 When the Docker image is created, the following dialog box appears. 

 docker-image.png 

 The Docker image is ready to use. 

 (Optional) If you need to update a Docker image, type the following command: 

 /docker_image_update 

 Add the following arguments: 

 Argument 

 Description 

 image 

 The name of the image. 

 all 

 Pulls all images. 

 (Optional) To see all available images, type the following: 

 /docker_images 

 This command does not accept any arguments and lists all available Docker images. 

 Previous Docker Images in Cortex XSOAR 

 Next Install Docker Images Offline 

 Last updated 13 days ago 

 Was this helpful?
