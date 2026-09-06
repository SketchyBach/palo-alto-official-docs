---
url: https://cortex-docs.paloaltonetworks.com/cortex-agentix/configure-cortex-agentix/engines/docker/docker-hardening-guide/run-docker-with-non-root-internal-users
fetched_at: 2026-09-06T10:17:52Z
source: cortex-platform
---

# Run Docker with non-root internal users | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex AgentiX 

 Cortex AgentiX Documentation 

 Configure Cortex AgentiX 

 Engines 

 Docker 

 Docker hardening guide 

 Cortex AgentiX 

 Run Docker with non-root internal users 

 Run Docker with non-root internal users for secure Cortex AgentiX engine operations. 

 For additional security isolation, we recommend to run Docker containers as non-root internal users. This follows the principle of least privilege. 

 Edit the engine configuration file either by editing the d1.conf file, or If you installed via Shell, you can edit the configuration in the UI as well as editing the file directly. For details, see Configure engines . 

 Add the following key: 

 "docker.run.internal.asuser": true 

 For containers that do not support non-root internal users, add the following key: 

 "docker.run.internal.asuser.ignore" : " A comma separated list of container names. The engine matches the container names according to the prefixes of the key values> " 

 For example, "docker.run.internal.asuser.ignore"="demisto/python3:","demisto/python:" 

 The engine matches the key values for the following containers: 

 Ask Copy 

 demisto/python:1.3-alpine 
 demisto/python:2.7.16.373 
 demisto/python3:3.7.3.928 
 demisto/python3:3.7.4.977 

 The : character should be used to limit the match to the full name of the container. For example, using the : character does not find demisto/python-ubuntu:2.7.16.373 . 

 Save the changes. 

 Restart the demisto service on the engine machine. 

 sudo systemctl start d1 

 (Ubuntu) sudo service d1 restart 

 Previous Configure Docker images 

 Next Configure the memory limit support without swap capabilities 

 Last updated 1 month ago 

 Was this helpful?
