---
url: https://cortex-docs.paloaltonetworks.com/data-security-documentation/data-management/broker-vm/set-up-and-configure-broker-vm/broker-vm-image-installations/set-up-broker-vm-on-kvm-using-ubuntu
fetched_at: 2026-09-06T10:51:34Z
source: cortex-platform
---

# Set up Broker VM on KVM using Ubuntu | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Data Security 

 Cortex Data Security Documentation 

 Data management 

 Broker VM 

 Set up and configure Broker VM 

 Broker VM image installations 

 Set up Broker VM on KVM using Ubuntu 

 Learn set up your Cortex Data Security Broker virtual machine (VM) on a KVM using Ubuntu. 

 After you download your Cortex Data Security Broker virtual machine (VM) QCOW2 image, you need to upload it to a kernel-based Virtual Machine (KVM). The instructions below provide an example of doing this on the latest Ubuntu. 

 Prerequisite 

 Download a Cortex Data Security Broker VM QCOW2 image. For more information, see the virtual machine compatibility requirements in Set up and configure Broker VM . 

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

 Last updated 26 days ago 

 Was this helpful?
