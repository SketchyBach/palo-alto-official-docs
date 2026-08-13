---
url: https://docs.paloaltonetworks.com/iot/administration/detect-iot-device-vulnerabilities/iot-risk-assessment
fetched_at: 2026-08-13T16:36:17Z
source: palo-alto-main
---

# Risk Assessment Clear

Risk Assessment 

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

 Risk Assessment 

 Updated on 

 Thu Jul 30 16:42:12 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Device Security Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Enterprise Administration 

 Integrations 

 Release Notes 

 Best Practice 

 New Features 

 Updated on 

 Thu Jul 30 16:42:12 PDT 2026 

 Focus 

 Home 

 Device Security 

 Device Security Administration Guide 

 IoT Device Vulnerability Detection 

 Risk Assessment 

 Download PDF 

 Device Security 

 Risk Assessment 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Device Security Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Enterprise Administration 

 Integrations 

 Release Notes 

 Best Practice 

 New Features 

 Previous 

 Vulnerability Details Page 

 Next 

 Customize Risk Scores 

 Risk Assessment 

 Device Security assesses risk and assigns a risk score for devices, device profiles,
 sites, and organizations.

 Where Can I Use This? What Do I Need? 

 Device Security (Managed by Strata Cloud Manager) 

 (Legacy) IoT Security (Standalone portal) 

 One of the following subscriptions: 

 Device Security subscription

 Precision AI bundle subscription

 Device Security X subscription

 Assessing risk is a continuous process of discovering vulnerabilities and detecting
 threats. During this ongoing process, Device Security measures risk and assigns a
 score for the amount of risk it observes. Device Security measures risk at
 different levels, starting from individual risk factors identified on a device.
 Device Security uses risk factors to calculate individual device risk scores, which
 then contribute to the profile, category, type, site, and organization risk scores.

 Device Security assesses risk based on the following risk categories when
 identified on devices:

 Vulnerabilities : Discovered through passive analysis and detections, and
 through vulnerability scans using integrated third-party vulnerability
 scanning engines such as Qualys, Rapid7, or Tenable.

 Security Alerts : Real time threat detections and anomalous behavioral
 detections by using threat signatures.

 Other Risk Factors : Risk factors not associated with CVEs or
 threat signatures.

 Poor Security Hygiene : Factors that reflect poor security
 practices in the network, such as using operating systems that are
 past end-of-support.

 Exposure : Factors related to the exposure of the device, such as
 external connectivity.

 By collecting and modeling data and analyzing these risk categories, 
 Device Security calculates risk daily. When calculating the risk scores
 of device profiles, sites, and organizations, Device Security considers not only
 the scores of individual devices within a particular group but also the percent of
 risky devices in relation to all devices in the group.

 Device Risk 

 Device Security displays the device risk score for each device in the
 Risk column on the Devices page ( Assets Devices ). It generates risk scores for devices daily.

 On the Device Details page, you can also find a more comprehensive breakdown of a
 device’s risk score. At the top, select See Details next to
 the device’s risk score under the thumbnail image. This brings up the
 Risk Score Details side panel, which displays the factors that contribute
 to the device’s risk score.

 Device Security uses two main factors to determine the device risk score:
 a device’s exposure score and the impact factor of the
 device’s criticality. The exposure score captures all risks identified for the
 device, while the impact factor enhances the exposure score based on the
 device’s asset criticality. You can adjust risks, compensating controls, and
 impact factors by customizing risk scores 
 to fit your organization’s security posture.

 Device Security uses a variety of risk factors to calculate the exposure score.
 We generate the exposure score based on the following:

 Vulnerabilities: Known vulnerabilities that appear in the
 Vulnerabilities inventory.

 Security Alerts: Alerts triggered by anomalous behavior, specific traffic
 patterns, custom-defined alerts, and threats. View all alerts on
 Alerts Security Alerts .

 Other Risk Factors: Poor hygiene and exposure-related factors, such as an
 unsupported OS or internet exposure.

 Compensating Controls: Steps that you have taken to manually offset or
 mitigate risk.

 Each individual risk in the risk categories have a system default risk score.
 Compensating controls reduce the risk score of individual risks, resulting in
 an effective risk score . The exposure score of a device comes from
 combining the effective risk scores of all risk factors associated with the device.

 After Device Security calculates the exposure score, it incorporates the
 impact factor to determine the final device risk score. The impact factor
 calculates the percentage increase of the exposure score, with the
 percentage increase determined by the device’s asset criticality. For example, if
 two devices have the same exposure score, but one has an asset criticality of high,
 while the other has an asset criticality of low, the device with a high
 asset criticality will have a higher impact factor, and therefore a
 higher device risk score. 

 The impact factor of a device must be 0 or greater, so the impact factor can't
 reduce the exposure score. The device risk score will always be equal to or greater
 than the exposure score.

 Device Profile Risk 

 Device Security displays risk scores for device profiles in the Risk column on the Profiles page ( Assets Profiles ). 

 Device Security uses the scores of individual
 at-risk devices (that is, those with a risk score of 40 or higher) in the same
 profile to calculate the risk score for the entire device profile. However, it's not
 as simple as averaging the risk scores of all the devices in the profile. The
 computation takes other factors into consideration such as the number of risky
 devices in the profile. 

 For example, if five devices in the same profile have individual
risk scores of 42, Device Security would calculate the risk score for
the profile to be 89. In this case, because all of the devices in
the profile are at risk, the profile score becomes higher than you
might have expected at first. 

 Consider another example, again with five devices in the same
profile. One device is at high risk with a score of 98. The other
four devices are at normal risk each with a score of 30. In this
case, Device Security calculates the risk score for their profile to
be 64. In such a small set, the one high-risk device has a much
greater impact on the profile score than it would if the scores
of more devices had been involved in the calculation. 

 Site Risk 

 See the Risk Score column in the Risk column on the Sites page ( Networks Networks and Sites Sites ). 

 The formula that Device Security uses to calculate the risk score
for a site uses a weighted average of device profile risk scores,
the weight for each profile being determined by the number of devices
in the profile and the profile risk level. 

 Organization Risk 

 See the Risk Score in the Risk panel on the Dashboards Security Dashboard . 

 Device Security uses the same method to calculate the risk score
for an organization as it does for sites. 

 Risk Scores and Severity Levels 

 The following explains how the severity of a risk score
is ranked: 

 Risk score Risk severity Notes 

 < 40 Low This is a normal risk level. 

 40-69 Medium There might be a few anomalous network behaviors, medium-level
alerts, and vulnerabilities with CVSS (Common Vulnerability Scoring
System) scores between 4.0 and 6.9. 

 70-89 High There might be multiple highly anomalous behaviors, high-level
alerts, and vulnerabilities with CVSS scores between 7.0 and 8.9. 

 90-100 Critical There might be multiple extremely anomalous behaviors, critical
alerts (such as a malware attack), and vulnerabilities with the
highest CVSS score of 10. 

 Alerts for Risk Score Changes 

 When the increase of a risk score causes it to cross
a threshold separating one risk level from another, Device Security 
generates a risk change alert. (Crossing a risk level threshold
as the result of a risk decrease does not trigger an alert.) A risk
increase triggers an alert with differing severity levels depending
on the new severity of the risk: 

 Warning when the risk level increases from high
to critical 

 Caution when the risk level increases from medium
to high 

 To reduce the overall number of alerts generated,
no alert is triggered when the risk level increases from low to
medium. 

 In addition to risk scores changing because of a manually adjusted
risk factor, they can also change for the following reasons: 

 Increased risk 

 A daily risk refresh discovers new vulnerabilities or
increased CVSS risk scores. 

 Decreased risk 

 A user resolves a risk factor. 

 A daily risk refresh discovers reduced vulnerabilities or
decreased CVSS scores or mitigated risks. 

 Resolve Risks 

 You can resolve vulnerabilities and security alerts through a workflow built into
 Device Security . Resolve them by either remediating, mitigating, or
 ignoring the vulnerability or alert. As a result, the device risk score might
 lower depending on other contributing factors such as the severity of the risk and
 the number and severity of other risks. When you resolve vulnerabilities, they no longer
 contribute to the device risk score. Resolving a vulnerability or alert on a device
 might similarly affect its profile, site, and organization risk scores depending on how
 significant of an impact the change makes in relation to the number and risk levels of other
 devices in the same group. For information about resolving vulnerabilities and
 security alerts, see Vulnerability Details Page and
 Act on Security Alerts .

 Previous 

 Vulnerability Details Page 

 Next 

 Customize Risk Scores 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Activate a License or Product 

 Cloud Identity Engine 

 Strata Logging Service 

 Device Associations 

 Hub 

 Identity and Access Management 

 Tenant Management 

 Next-Generation Firewalls 

 AIOps for NGFW 

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 Service Provider 

 VM-Series 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 Device Security 

 Administration 

 Cloud-Delivered Security Services 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
