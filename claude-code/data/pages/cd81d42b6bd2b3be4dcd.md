---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/cloudblades/cloudblade-integrations/prisma-sd-wan-azure-virtual-wan-cloudblade-integration/create-and-acquire-the-azure-information
fetched_at: 2026-09-16T07:48:04Z
source: strata-and-sase
---

# Create and Acquire the Azure Information Clear

Updated on 

 Wed Feb 25 08:09:59 PST 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Azure Virtual WAN CloudBlade Integration 

 Create and Acquire the Azure Information 

 Download PDF 

 Prisma SD-WAN 

 Create and Acquire the Azure Information 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma SD-WAN Docs 

 Activation & Onboarding 

 Administration 

 CloudBlades 

 Select a Document 

 CloudBlade Integrations 

 CloudBlades Integration with Prisma Access 

 Deployment 

 Incidents & Alerts 

 Reference 

 Release Notes 

 Select a Document 

 ION 6.8 

 ION 6.6 

 ION 6.5 

 ION 6.4 

 ION 6.3 

 ION 6.1 

 ION 5.6 

 Prisma SD-WAN Controller 

 Prisma SD-WAN On-Premises Controller 

 Prisma SD-WAN CloudBlades 

 Prisma Access CloudBlade Cloud Managed 

 Prisma Access CloudBlade Panorama Managed 

 New Features 

 Previous 

 Azure vWAN and Prisma SD-WAN CloudBlade Prerequisites 

 Next 

 Configure and Install the Azure Virtual WAN CloudBlade 

 Create and Acquire the Azure Information 

 Learn how to create and acquire the Azure Information in Prisma SD-WAN 
 when integrating the Azure vWAN CloudBlade. 

 Where Can I Use This? What Do I Need? 

 Prisma SD-WAN (Managed by Strata Cloud Manager ) 

 Prisma SD-WAN 

 Azure Virtual WAN CloudBlade 

 Before configuring Prisma SD-WAN to integrate with Azure vWAN, perform
 the following: 

 Create an application registration object. 

 Copy the Application Client ID and Directory tenant ID to be used later in Prisma SD-WAN CloudBlade configuration. 

 Generate and copy a new client secret to be used later in Prisma SD-WAN CloudBlade configuration. 

 Assign Contributor role to the new Application Registration object created in
 Step 1. 

 Locate the Azure subscription ID and copy to be used later in Prisma SD-WAN CloudBlade configuration. 

 Create a Resource Group, a Virtual WAN object, and at least one Hub. Copy the
 Resource Group name and Virtual WAN name to be used later on Prisma SD-WAN . 

 When creating a Hub ensure that the appropriate region is selected for
 your vWAN use case and the Hub address space does not overlap with any
 other subnets in your organization. 

 (Optional) Add a virtual network connection to Virtual WAN in order to
 associate an existing VNET hosting applications and services to a vWAN Hub, such
 that this network could be reachable via vWAN. 

 Previous 

 Azure vWAN and Prisma SD-WAN CloudBlade Prerequisites 

 Next 

 Configure and Install the Azure Virtual WAN CloudBlade
