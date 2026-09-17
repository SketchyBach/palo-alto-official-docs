---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-administrator-guide/6.14/onboard-cortex-xsoar/docker/troubleshoot-docker-performance-issues
fetched_at: 2026-09-16T08:56:02Z
source: cortex-platform
---

# Troubleshoot Docker Performance Issues | 6.14 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Administrator Guides 

 6.14 

 Onboard Cortex XSOAR 

 Docker 

 Cortex XSOAR 6.14 

 Troubleshoot Docker Performance Issues 

 Troubleshoot Cortex XSOAR 6.14 Docker performance issues and update Docker packages and dependencies. 

 You might experience several Docker performance issues. This information is intended to help resolve the following Docker performance issues. 

 Containers are getting stuck. 

 The Docker process consumes a lot of resources. 

 Time synchronization issues between the container and the OS. 

 Cause 

 The installed Docker package and its dependencies are not up to date. 

 Workaround 

 Update the package manager cache. 

 Linux Distribution 

 Command 

 Debian 

 apt-get update 

 (Optional) Check for a newer version of the Docker package. 

 Linux Distribution 

 Command 

 Debian 

 apt-cache policy docker 

 Update the Docker package. 

 Linux Distribution 

 Command 

 Debian 

 apt-get update docker 

 Previous Troubleshoot Docker Networking Issues 

 Next Configure Docker Pull Rate Limit 

 Last updated 13 days ago 

 Was this helpful?
