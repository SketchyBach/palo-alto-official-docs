---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/engines/install-an-engine/podman/change-the-container-storage
fetched_at: 2026-09-16T08:34:29Z
source: cortex-platform
---

# Change the Container storage | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSIAM 

 Cortex XSIAM Documentation 

 Configure Cortex XSIAM 

 Engines 

 Install an engine 

 Podman 

 Cortex XSIAM 

 Change the Container storage 

 Configure Podman container storage for Cortex XSIAM engines. 

 By default, Podman uses the $HOME/.local/share/containers/storage directory. To use a different directory for container storage, edit the Podman config file located at /home/demisto/.config/containers/storage.conf . If the Podman config file does not exist, you need to create it and change the ownership. 

 The new storage directory needs to be owned by the demisto user, otherwise, they will be denied access to it. 

 Do not use NAS storage or a temporary (tmpfs) directory for the graphroot setting. The graphroot needs to be a local, non-temporary directory for Podman to work. For more information, see https://en.wikipedia.org/wiki/Network-attached_storage . 

 We recommend reserving 150 GB for container storage, either in the /home partition or a different storage directory that you have set using the graphroot key. 

 If the Podman config file does not exist: 

 Create the Podman config file. 

 sudo mkdir -p /home/demisto/.config/containers 

 cp /etc/containers/storage.conf /home/demisto/.config/containers 

 Change the ownership of the Podman config file. 

 sudo chown -R demisto:demisto /home/demisto 

 To set a different directory for container storage, change the key: graphroot in the storage.conf file. For example: 

 graphroot = "/var/lib/containers/cortex-storage" 

 Some additional changes are required in the storage.conf file. Comment out the runroot setting by adding a # (hash) before it. For example: 

 #runroot = "/run/containers/storage" 

 Alternatively, the runroot setting may be set to some temporary directory that is accessible by the user demisto. If you choose to set the runroot , it must be a directory that is mounted as tmpfs (temporary filesystem), unlike the graphroot. 

 Under [storage.options.overlay], uncomment the following line (remove the # from the start): 

 mount_program = "/usr/bin/fuse-overlayfs" 

 If the engine has already been installed, apply your changes to any existing containers: 

 sudo -u demisto podman system migrate 

 Verify the change (once the engine is installed): 

 sudo -u demisto podman info | grep graph 

 Previous Podman 

 Next Install Podman 

 Last updated 1 month ago 

 Was this helpful?
