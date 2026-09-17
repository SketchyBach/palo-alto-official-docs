---
url: https://docs.prismacloud.io/use-cases/secure-the-infrastructure/gain-visibility-into-your-cloud-estate
fetched_at: 2026-09-16T13:35:54Z
source: prisma-cloud
---

# Gain Visibility into Your Cloud Estate | Prisma Cloud arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Enterprise Edition 

 Use Cases 

 Secure the Infrastructure 

 Gain Visibility into Your Cloud Estate 

 Enterprises are leveraging cloud platforms at a very rapid rate in order to deliver differentiated applications for their customers. As a consequence, DevOps teams are deploying a large number of applications using sophisticated cloud infrastructures and deployment patterns. This however, poses a massive security risk as security teams are unable to keep pace with the deployment velocity. 

 Therefore, the first step to a strong security posture is complete and contextual visibility. This involves knowing and identifying the cloud accounts, ownership, the data they contain along with the security and compliance posture of these accounts and applications. Without complete visibility into your cloud estate, you are at risk of data breaches, compliance violations, and operational inefficiencies. 

 The journey that a security practitioner should embark on to operationalize Prisma Cloud is as follows: 

 1. DISCOVER 

 Onboard your cloud accounts in order to obtain comprehensive visibility into your cloud estate. Prisma Cloud provides detailed visibility into the assets deployed across your entire cloud estate. 

 As shown in the example below, when you onboard a cloud account on Prisma Cloud, you can navigate to the Inventory > Assets to obtain an instantaneous view of the assets in the cloud account as well as a summary of the security posture associated with those assets.
You can start on the Asset Inventory for a listing of all the assets deployed in the cloud account, and use it to enable further workflows such as dig in and Investigate , adherence to Compliance, or review Alerts . 

The summary of the security posture of the assets in the cloud account provides a starting point to enable the user to further assess and investigate various security issues in order to take the appropriate actions (block or remediate for example). The example shown above demonstrates the ability to use the Asset Inventory and associate these assets to corresponding alerts raised. 

 You can then continue to obtain a detailed analysis of the failed assets by clicking on “Fail” tab to obtain detailed information pertaining to failures along with a prioritized list of alerts associated with those assets. 

 The discovery phase is composed of two parts, the first is the discovery of known assets and the second being the discovery of unknown assets potentially deployed due to shadow IT. The CDEM module in Prisma Cloud can be used to discover the view that an attacker has of the cloud account, providing the benefit of visibility into the assets that are not known to the Cloud Architecture and Governance teams. 

 2. ASSESS 

 Alerts in Prisma Cloud are based on the evaluation of policies against the configuration or runtime posture of an asset. Users can either leverage out of the box policies from Prisma Cloud or define custom policies which will be evaluated against the cloud assets. 

 The next step is to leverage the rich set of out of the box policies available on Prisma Cloud, in order to assess the security and compliance posture of your cloud assets. Additionally, Prisma Cloud enables users to develop custom policies which can be used to further evaluate the security posture and configuration of the assets. 

 For example, a user working in the Infosec team at a financial institution has a requirement to assess the PCI compliance posture of the deployed cloud assets and applications.This information is readily available under the Compliance tab illustrating the PCI compliance posture of assets deployed in the cloud environment. As shown below the user can apply out-of-the-box PCI compliance policies to be evaluated against all or a subset of the cloud assets, in order to determine the compliance posture of those assets. The information retrieved can be used to plan on remediation tasks as necessary. 

 Leverage Command Center to identify the top risks, alerts and incidents in order to understand your security posture, exposures and risks. The information from the command center can be used to develop a plan to address the security threats and issues based on the findings on the platform. 

 For example, as shown below, Command Center can be used to build powerful views to gain visibility into the security posture of the entire cloud estate. 

 The Command Center can be used to visualize important security dimensions such as “Incidents by Policy”, “Attack Paths” and “Misconfigurations”. This information is further prioritized based on criticality to the business thus enabling the security user to build out a remediation plan. 

 3. INVESTIGATE 

 A Prisma Cloud user has now gone through the Discover and Assess phases. The next logical step is to dig deeper into specific findings or alerts in order to ensure the necessary remediation steps are executed. 

 Take advantage of the Alerts dashboard to further investigate and analyze the security posture of all the cloud assets . Most organizations have dedicated teams to manage Vulnerabilities, Risk, Compliance, Incidents and Misconfigurations and each of these teams can leverage the saved views on the Alerts dashboard to further investigate and remediate risky assets. 

 You can further continue to gain deeper visibility with Investigate as shown below.

 Run sophisticated queries against runtime and configuration attributes of an asset to gain or uncover security landmines. For example, one of the most relevant searches and also serves as a starting point for investigation is to retrieve a list of all instances that are exposed to the internet (shown below). 

 This investigation query can be further expanded to retrieve all instances that are exposed to the internet which contain a high severity vulnerability that can be exploited by malicious actors. 

 Additionally, a Cloud Architecture team that is responsible for the overall management of cloud assets can generate customized reports for each of these teams in order to facilitate the necessary next steps. For example, the Cloud Architecture team can generate an Alerts report and deliver this to the Infosec team in order to analyze and take the necessary steps. The Prisma Cloud platform is designed to meet the needs of various teams and personas. The Infosec team can leverage the report and in turn use it to execute search and investigate activities to ensure they appropriately secure assets that are susceptible to exploits. 

 4. ADOPT 

 The final part of gaining visibility into your cloud estate is to ensure that enterprises are leveraging all the powerful capabilities of the Prisma Cloud platform in order to secure their cloud estate. Use the Prisma Cloud Adoption Advisor as a guide to continue to build out your security plan and improve the security posture of applications. 

 For example, the figure below illustrates the adoption of the Prisma Cloud platform across the Code & Build, Deploy and Runtime phases. As an enterprise continues to remediate and fix security issues prior to deployment, it is important to mature the adoption of the Code & Build modules. In this example, both Remediation and Drift Detection in the Code & Build phase are at the Intermediate level. This provides guidance to Cloud Security teams that they continue to expand the adoption of security capabilities in this phase and move into Advanced levels of adoption. 

 Previous Secure the Infrastructure 

 Next Gain Visibility into Your Shadow Cloud Assets 

 Last updated 1 month ago 

 Was this helpful?
