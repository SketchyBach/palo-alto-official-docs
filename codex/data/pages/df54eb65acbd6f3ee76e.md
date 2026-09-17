---
url: https://docs.paloaltonetworks.com/content/techdocs/en_US/vm-series/activation-and-onboarding/software-ngfw/customize-data-plane-cores.html
fetched_at: 2026-09-16T13:56:15Z
source: palo-alto-main
---

# Customize Dataplane Cores Clear

Updated on 

 Jun 19, 2026 

 Focus 

 Home 

 VM-Series 

 Software NGFW Credits 

 Customize Dataplane Cores 

 Download PDF 

 VM-Series 

 Customize Dataplane Cores 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 VM-Series Firewall Docs 

 Activation & Onboarding 

 Getting Started 

 Upgrade 

 Deployment 

 Select a Document 

 Public Cloud 

 Private Cloud 

 Previous 

 Set the Number of Licensed vCPUs 

 Next 

 Migrate a Firewall to a Flexible VM-Series License 

 Customize Dataplane Cores 

 Use the CLI to customize the core division between the dataplane and the management plane
 from the VM-Series firewall version 11.1 or later. 

 Where Can I Use This? What Do I Need? 

 VM-Series deployment 

 VM-Series 10.x or above 

 Panorama running PAN-OS 10.1.x or above versions 

 Customer Support Portal (CSP) account with one of the
 following user roles: 
 Super User, Standard User, Limited User, Threat
 Researcher, AutoFocus Trial Role, Group Super User,
 Group Standard User, Group Limited User, Group
 Threat Researcher, Authorized Support Center (ASC)
 User, and ASC Full Service User. 

 Superuser access to the VM-Series firewall 

 As mentioned in Software NGFW Credits , when
 a firewall is deployed using Software NGFW credits, the memory profile and the total
 number of vCPUs determine how many cores are automatically assigned to the
 management plane and the dataplane. The default configurations perform well in most
 cases. 

 Customize dataplane
cores is an optional feature that allows you to customize the number
of dataplane cores in two ways: 

 During the initial deployment, use the init-cfg.txt file bootstrap parameter
 plugin-op-commands=set-dp-cores:<#-cores> . See
 Create Bootstrap Configuration
 Files . 

 From a deployed firewall, using the VM-Series CLI command request plugins vm_series dp-cores <#-cores> .
This procedure is outlined below. 

 Typically you
increase the number of dataplane cores (which decreases the number of
management plane cores) to improve performance. Dataplane core customization does
not require a change to the deployment profile or additional credits
because the total number of vCPUs remains the same. 

 Dataplane
core customization is supported on firewalls running PAN-OS 10.1
or later licensed with a Software NGFW credit pool for 10.0.4 and
above. 

 Dataplane core customization isn’t supported for: 

 NSX-T 

 Intelligent Traffic Offload 

 Follow
theses steps to customize the dataplane cores on the VM-Series firewall. 

 Log in to the VM-Series firewall and view the
number of cores. 

 admin@PA-VM(active)> show plugins vm_series dp-cores 
 Device current DP cores: 13 (Total cores: 18) 

 Change the number of dataplane cores. 

 You must have at least one management plane core, and having too few cores affects
 performance. 

 In this example, we increase the data planes to 14. 

 admin@PA-VM(active)> request plugins vm_series set-cores dp-cores 14 
Device current DP cores: 14 (Total cores: 18) 

 Reboot the VM-Series firewall. 

 request restart system 

 Select Device Setup Operations and
click Reboot Device . 

 Use show plugins vm_series dp-cores to
verify that the number of DP cores has changed. 

 Previous 

 Set the Number of Licensed vCPUs 

 Next 

 Migrate a Firewall to a Flexible VM-Series License
