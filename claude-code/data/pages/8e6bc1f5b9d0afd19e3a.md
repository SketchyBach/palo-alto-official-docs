---
url: https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/data-management/broker-vm/set-up-and-configure-broker-vm/broker-vm-image-installations/set-up-broker-vm-on-kvm-using-ubuntu
fetched_at: 2026-09-06T09:59:05Z
source: cortex-platform
---

# Set up Broker VM on KVM using Ubuntu | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Cortex CLOUD Runtime Security 

 Data Management 

 Broker VM 

 Set up and configure Broker VM 

 Broker VM image installations 

 Cortex Cloud Runtime 

 Set up Broker VM on KVM using Ubuntu 

 Deploy Broker VM on KVM hosts running Ubuntu. 

 Learn set up your Cortex Cloud Broker virtual machine (VM) on a KVM using Ubuntu. 

 After you download your Cortex Cloud Broker virtual machine (VM) QCOW2 image, you need to upload it to a kernel-based Virtual Machine (KVM). The instructions below provide an example of doing this on the latest Ubuntu. 

 Prerequisite 

 Download a Cortex Cloud Broker VM QCOW2 image. For more information, see the virtual machine compatibility requirements in Set up and configure Broker VM . 

 Open KVM on Ubuntu. 

 Click the New VM icon. 

 Complete the new virtual machine wizard: 

 In Step 1 , select Import existing disk image . Click Forward . 

 In Step 2 , configure the storage: 

 Browse to the downloaded QCOW2 image. 

 Click Browse Local , select the image, then click Open . 

 Leave OS type and Version set to Generic . 

 Click Forward . 

 In Step 3 , specify these resources: 

 Memory (RAM): 8192 MB (8 GB) 

 CPUs: 4 

 Click Forward . 

 In Step 4 , enter a name for the VM. 

 Click Finish . The VM is listed and ready to use. 

 Previous Set up Broker VM on Google Cloud Platform (GCP) 

 Next Set up Broker VM on Microsoft Azure 

 Last updated 1 month ago 

 Was this helpful?
