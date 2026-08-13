---
url: https://docs.paloaltonetworks.com/vm-series/deployment/public-cloud/set-up-the-vm-series-firewall-on-azure/vm-series-on-azure-service-principal-permissions
fetched_at: 2026-08-13T17:42:08Z
source: palo-alto-main
---

# VM-Series on Azure Service Principal Permissions Clear

VM-Series on Azure Service Principal Permissions 

 Home 

 EN

 Location 

 Documentation Home 

 Palo Alto Networks 

 Support 

 Live Community 

 Knowledge Base 

 >

 Strata Copilot

 VM-Series on Azure Service Principal Permissions 

 Updated on 

 Jul 8, 2026 

 Focus 

 Download PDF 

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

 Updated on 

 Jul 8, 2026 

 Focus 

 Home 

 VM-Series 

 VM-Series Firewall on Azure 

 VM-Series on Azure Service Principal Permissions 

 Download PDF 

 VM-Series 

 VM-Series on Azure Service Principal Permissions 

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

 Minimum System Requirements for the VM-Series on Azure 

 Next 

 Deploy the VM-Series Firewall from the Azure Marketplace (Solution Template) 

 VM-Series on Azure Service Principal Permissions 

 Review the granular permissions for the Service Principal for VM-Series
 integrations 

 Where Can I Use This? What Do I Need? 

 Microsoft Azure 

 Microsoft Azure Stack 

 Azure® Marketplace 

 Azure China Marketplace 

 Azure Government Marketplace 

 VM-Series License (PAYG or BYOL) 

 VM-Series plugin 

 Panorama 

 Panorama plugin for Azure 

 For Panorama to interact with the Azure
APIs and collect information on your workloads, you need to create
an Azure Active Directory application and a Service Principal that
has the permissions required to authenticate with Azure AD and access
the resources within your subscription. 

 To create the Active Directory application and
Service Principal, follow the instructions in How to: Use the portal to create
an Azure AD application and service principal that can access resources .
During the application generation process, there is a step to "Assign
application to role" and assign an IAM role of "reader" to the application. 

 If you don't have the necessary permissions to
create and register the AD application, ask your Azure AD or subscription
administrator to create a Service Principal. 

 After the application has been registered, record these values
so you can enter them in the Panorama plugin for Azure at a later
time: 

 Application ID 

 Secret Key (record it when you make the secret key; the secret key isn't visible once you
 navigate away from the page). 

 Tenant ID 

 Permissions 

 The following table lists the minimum built-in roles required
and the granular permissions if you would like to customize the
role. 

 To support Permissions 

 Azure High Availability 

 See Set up Active/Passive HA on Azure . 

 Azure Application Insights 

 Enable Azure Application Insights on the VM-Series Firewall 

 “Microsoft.Authorization/*/read”, 

 “Microsoft.Network/networkInterfaces/*”, 

 “Microsoft.Network/networkSecurityGroups/*”, 

 “Microsoft.Network/virtualNetworks/*”, 

 “Microsoft.Compute/virtualMachines/read” 

 Azure Monitoring 

 Set Up the Azure Plugin for Monitoring on Panorama 
 Requires a minimum Role of Reader for Service
Principal. Alternatively, you can add the following custom permissions: 
 “Microsoft.Compute/virtualMachines/read”, 

 “Microsoft.Network/networkInterfaces/read”, 

 “Microsoft.Network/virtualNetworks/read”, 

 “Microsoft.Network/virtualNetworks/subnets/read”, 

 “Microsoft.Network/applicationGateways/read”, 

 “Microsoft.Network/locations/serviceTags/read”, 

 "Microsoft.Network/loadBalancers/read", 

 "Microsoft.Network/publicIPAddresses/read", 

 "Microsoft.Resources/subscriptions/resourcegroups/read" 

 Panorama Orchestrated Deployments 

 Create a Custom Role and Associate It with an Active Directory 

 “Microsoft.Resources/subscriptions/resourcegroups/*”, 

 “Microsoft.Resources/deployments/write”, 

 “Microsoft.Resources/deployments/operationStatuses/read”, 

 “Microsoft.Resources/deployments/read”, 

 “Microsoft.Resources/deployments/delete” 

 "Microsoft.Network/publicIPPrefixes/write", 

 "Microsoft.Network/publicIPPrefixes/read", 

 "Microsoft.Network/publicIPPrefixes/delete", 

 "Microsoft.Network/publicIPAddresses/write", 

 "Microsoft.Network/publicIPAddresses/read", 

 "Microsoft.Network/publicIPAddresses/delete", 

 "Microsoft.Network/publicIPAddresses/join/action", 

 "Microsoft.Network/natGateways/write", 

 "Microsoft.Network/natGateways/read", 

 "Microsoft.Network/natGateways/delete", 

 "Microsoft.Network/natGateways/join/action", 

 "Microsoft.Network/virtualNetworks/read", 

 "Microsoft.Network/virtualNetworks/write", 

 "Microsoft.Network/virtualNetworks/delete", 

 "Microsoft.Network/virtualNetworks/subnets/write", 

 "Microsoft.Network/virtualNetworks/subnets/read", 

 "Microsoft.Network/virtualNetworks/subnets/delete", 

 "Microsoft.Network/virtualNetworks/subnets/join/action", 

 "Microsoft.Network/virtualNetworks/virtualNetworkPeerings/read", 

 "Microsoft.Network/networkSecurityGroups/write", 

 "Microsoft.Network/networkSecurityGroups/read", 

 "Microsoft.Network/networkSecurityGroups/delete", 

 "Microsoft.Network/networkSecurityGroups/join/action", 

 "Microsoft.Network/loadBalancers/write", 

 "Microsoft.Network/loadBalancers/read", 

 "Microsoft.Network/loadBalancers/delete", 

 "Microsoft.Network/loadBalancers/probes/join/action", 

 "Microsoft.Network/loadBalancers/backendAddressPools/join/action", 

 "Microsoft.Network/loadBalancers/frontendIPConfigurations/read", 

 "Microsoft.Network/locations/serviceTags/read", 

 "Microsoft.Network/applicationGateways/read", 

 "Microsoft.Network/networkInterfaces/read", 

 "Microsoft.Compute/virtualMachineScaleSets/write", 

 "Microsoft.Compute/virtualMachineScaleSets/read", 

 "Microsoft.Compute/virtualMachineScaleSets/delete", 

 "Microsoft.Compute/virtualMachineScaleSets/virtualMachines/read", 

 "Microsoft.Compute/virtualMachines/read", 

 "Microsoft.Compute/images/read", 

 "Microsoft.insights/components/write", 

 "Microsoft.insights/components/read", 

 "Microsoft.insights/components/delete", 

 "Microsoft.insights/autoscalesettings/write" 

 Previous 

 Minimum System Requirements for the VM-Series on Azure 

 Next 

 Deploy the VM-Series Firewall from the Azure Marketplace (Solution Template) 

 On This Page 

 Activation and Onboarding 

 Strata Cloud Manager 

 Next-Generation Firewalls 

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 VM-Series 

 Plugins 

 Cloud-Delivered Security Services 

 Advanced WildFire 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 AI Access Security 

 Device Security 

 Enterprise DLP 

 SaaS Security 

 Network Security 

 Shared Policy for NGFWs and Prisma Access 

 IPSec VPN 

 Security Policy 

 Quantum Security 

 Endpoints 

 GlobalProtect 

 Resources 

 All Release Notes 

 Compatibility Matrix 

 Experts Corner 

 Network Security 

 Deployment 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
