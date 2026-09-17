---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-administrator-guide/6.13/onboard-cortex-xsoar/docker/docker-hardening-guide/docker-network-hardening
fetched_at: 2026-09-16T08:56:45Z
source: cortex-platform
---

# Docker Network Hardening | 6.13 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Administrator Guides 

 6.13 

 Onboard Cortex XSOAR 

 Docker 

 Docker Hardening Guide 

 Cortex XSOAR 6.13 

 Docker Network Hardening 

 Harden Docker networking for Cortex XSOAR 6.13. 

 Docker creates a networking stack for container communication. By default, containers can communicate with all IP addresses. Use iptables rules to restrict this access. 

 These instructions apply to Docker-based Python and PowerShell integrations and automations. For JavaScript integrations, set js.http.restricted to a comma-separated list of allowed IPs or hosts. 

 The default Docker network is bridge and its default interface is docker0 . List Docker networks with sudo docker network ls . Inspect a network with sudo docker network inspect <network name> . 

 Key 

 Value 

 js.http.restricted 

 169.254.169.254,localhost,127.0.0.1 

 Block network access to the host machine 

 Integrations and automations usually do not need host-network access. Block access from containers to host services, including Cortex XSOAR Server. 

 Add an iptables rule for each private host IP address: 

 Ask Copy 

 sudo iptables -I INPUT -s <IP address range> -d <host private ip address> -j DROP 

 For Docker’s default 172.16.0.0/12 range, use: 

 Ask Copy 

 sudo iptables -I INPUT -s 172.16.0.0/12 -d 10.18.18.246 -j DROP 

 If you configured another range in Docker’s daemon.json , use that range. You can also limit a specific source interface, such as docker0 . 

 Block access to the Docker gateway IP: 

 Ask Copy 

 iptables -I INPUT -i docker0 -d 172.17.0.1/32 -j DROP 

 Optionally, list private host IP addresses: 

 Ask Copy 

 sudo ifconfig -a 

 Block cloud instance metadata access 

 Block containers from accessing the instance metadata service on 169.254.169.254 . 

 On GCP, allow DNS queries to the metadata server when required: 

 For metadata service details, see the AWS documentation and GCP documentation . 

 Assign a Docker network for an image 

 Create a separate network for integrations that require metadata access. Most AWS integrations use the demisto/boto3py3 image. 

 Create the network: 

 Add the following server configuration: 

 Key 

 Value 

 python.pass.extra.keys.demisto/boto3py3 

 --network=aws-metadata 

 Reset running containers with /reset_containers . 

 Verify the network: 

 Block internal network access 

 Block selected integrations from internal resources. This is recommended for the Rasterize integration when processing untrusted URLs or HTML. 

 Create an external Docker network: 

 Block host access: 

 Block metadata access: 

 Block internal address ranges: 

 Add the following server configuration: 

 Key 

 Value 

 python.pass.extra.keys.demisto/chromium 

 --network=external 

 Reset running containers with /reset_containers . 

 Verify the network: 

 Persist iptables rules 

 iptables rules do not persist after a reboot. Save them using your operating system’s recommended configuration: 

 Ubuntu 

 Red Hat and related operating systems 

 Previous Configure the Open File Descriptors Limit 

 Next Docker FAQs 

 Last updated 13 days ago 

 Was this helpful?
