---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-administrator-guide/6.12/onboard-cortex-xsoar/podman/podman-installation
fetched_at: 2026-09-06T10:47:06Z
source: cortex-platform
---

# Podman Installation | 6.12 (EoL) | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Administrator Guides 

 6.12 (EoL) 

 Onboard Cortex XSOAR 

 Podman 

 Cortex XSOAR 6.12 EoL 

 Podman Installation 

 Install Podman for Cortex XSOAR 6.12. 

 When installing a new server or engine on RHEL 8 or later, the shell installer configures Podman automatically. There are some cases, however, where you might need to install Podman manually: 

 When using an installation method other than the shell installer (e.g. an RPM package) on RHEL 8 or later. 

 When the shell installer did not successfully install Podman. 

 When you want to migrate from Docker to Podman, for an existing Cortex XSOAR server or engine. 

 Note 

 This procedure is intended for RHEL 8 or later. It may not work for other operating system types. 

 Do not use NAS storage for the $HOME directory. The directory needs to be a local directory for Podman to work. 

 For RHEL 8, install Podman by typing the following commands: 

 sudo yum -y install slirp4netns fuse-overlayfs 

 sudo yum -y module install container-tools 

 For RHEL 9 or later, install Podman by typing the following command: 

 sudo yum -y install slirp4netns fuse-overlayfs podman 

 Run the following commands: 

 sudo touch /etc/subuid /etc/subgid 

 sudo mkdir -p /home/demisto 

 sudo chown demisto:demisto /home/demisto 

 Configure the unqualified-search-registries used by Podman. 

 Podman by default uses the fedoraproject.org, redhat.com, and docker.io unqualified search registries. Since Cortex XSOAR images use only the docker.io registry, you can speed up download times for container images by setting unqualified-search-registries to just docker.io. 

 Create or edit the /home/demisto/.config/containers/registries.conf config file. 

 In the file, set the following: 

 unqualified-search-registries = ['docker.io'] 

 Note 

 If you edit the file with the root user, make sure to set the demisto user as file owner by running chown demisto:demisto /home/demisto/.config/containers/registries.conf 

 Change the subuids and subgids by running the following command: 

 sudo usermod --add-subuids 200000-265535 --add-subgids 200000-265535 demisto 

 Migrate existing containers to Podman by typing the following command: 

 sudo sh -c "cd /; runuser -u demisto -- podman system migrate" 

 Set the net.ipv4.ping-group-range , by typing the following commands: 

 sudo sh -c "echo 'net.ipv4.ping_group_range=0 2000000' > /etc/sysctl.d/demisto-ping.conf" 

 sudo sysctl -w "net.ipv4.ping_group_range=0 2000000" 

 As root user, edit one of the following config files: 

 Server : 

 /etc/demisto.conf 

 Engine : 

 /usr/local/demisto/d1.conf 

 Change the "container.engine.type": "docker" to "podman" . 

 If this line does not exist, add the following line to the file: 

 "container.engine.type": "podman" 

 Ask Copy 

 "Server": { 
 "HttpsPort": "443", 
 "ProxyMode": true 
 }, 
 "container": { 
 "engine": { 
 "type": "podman" 
 } 
 }, 
 "db": { 
 "index": { 
 "entry": { 
 "disable": true 

 If the engine or server is running, restart the service. 

 Server: sudo systemctl restart demisto 

 Engine: sudo systemctl restart d1 

 Previous Change container storage directory 

 Next Configure the SELinux Policy for PowerShell Integrations 

 Last updated 1 month ago 

 Was this helpful?
