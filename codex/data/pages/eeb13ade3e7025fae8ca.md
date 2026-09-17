---
url: https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cases-and-issues/investigation-and-response/automation/engines/install-an-engine/docker/docker-hardening-guide/configure-docker-images
fetched_at: 2026-09-16T08:47:25Z
source: cortex-platform
---

# Configure Docker images | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Cortex CLOUD Posture Management 

 Cases and issues 

 Investigation and response 

 Automation 

 Engines 

 Install an engine 

 Docker 

 Docker hardening guide 

 Cortex Cloud Posture 

 Configure Docker images 

 Configure Docker images for hardened engine deployments. 

 You can apply more specific fine tuned settings to Docker images, according to the Docker image name or the Docker image name including the image tag. To apply settings to a Docker image name, add the advanced configuration key to the engine configuration file. If you apply Docker image specific settings, they will be used instead of the general python.pass.extra.keys setting. This overrides the general memory and CPU settings, as needed. 

 Edit the engine configuration file either by editing the d1.conf file, or If you installed via Shell, you can edit the configuration in the UI as well as editing the file directly. For details, see Configure engines . 

 Add the following key to apply settings to a Docker image name. 

 "python.pass.extra.keys.<image_name>" 

 For example, "python.pass.extra.keys.demisto/dl" . 

 To apply settings to a Docker image name, including the image tag, use "python.pass.extra.keys.<image_name>": "<image_tag>" . 

 For example, "python.pass.extra.keys.demisto/dl": "1.4" . 

 To set the Docker images demisto/dl (all tags) to use a higher max memory value of 2g and to remain with the recommended PIDs and ulimit, add the following to the configuration file: "python.pass.extra.keys.demisto/dl": "--memory=2g##--ulimit=no- file=1024:8192##--pids-limit=256" 

 Save the changes. 

 Restart the demisto service on the engine machine. 

 sudo systemctl start d1 

 (Ubuntu) sudo service d1 restart 

 Previous Docker network hardening 

 Next Run Docker with non-root internal users 

 Last updated 1 month ago 

 Was this helpful?
