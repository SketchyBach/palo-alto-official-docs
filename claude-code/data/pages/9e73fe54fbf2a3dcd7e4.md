---
url: https://docs.cyberark.com/setup/latest/en/content/identity/endpoints/deploy-mobile-apps-intune.htm
fetched_at: 2026-08-16T10:04:49.538Z
source: idira-docs
capture_method: official interactive browser
---

# Configure the Idira Identity mobile app using a third-party MDM

Skip To Main Content
Our Products
Configure the Idira Identity mobile app using a third-party MDM

This topic describes how to configure the Idira Identity mobile app using a supported third-party mobile device management (MDM) solution. Supported MDM solutions include Microsoft Intune and AirWatch.

Deploy using Microsoft Intune

You can use Microsoft Intune to deploy the Idira Identity mobile app to managed devices in a centralized and automated way.

For more information, see the Microsoft Intune documentation topics Add Managed Google Play apps to Android Enterprise devices with Intune and Add iOS store apps to Microsoft Intune.

To deploy the app using Microsoft Intune:

Sign in to the Microsoft Intune admin center.

Add a new app with the app type appropriate for your platform:

App types

Platform

	

App type




Android

	

Managed Google Play app




iOS

	

iOS store app

When prompted to search the app store, select the app store region, search for Idira, and then select Idira Identity.

(Optional) When prompted, add scope tags for the app. For more information, see the Microsoft documentation topic Use role-based access control (RBAC) and scope tags for distributed IT.

When prompted, select the appropriate group assignments for the app. For more information, see the Microsoft documentation topic Add groups to organize users and devices.

Review your configuration and create the deployment.

If you are using an external identity provider (IdP), see Configure Idira Identity mobile enrollment for Intune-managed iOS devices for additional steps.

After the mobile app is deployed, end users need to associate the app with their accounts by enrolling the mobile app. For more information, see Enroll mobile devices.

Configure using AirWatch MDM

You can use AirWatch MDM to push the Idira Identity mobile app configuration to managed devices. You set up and apply the configuration from the AirWatch Admin Portal.

To configure the app using AirWatch MDM:

Sign in to the AirWatch Admin Portal.

Add the following configuration. Replace {Tenant URL} with your tenant URL.

<dict>
    <key>TenantUrl</key>
    <string>{Tenant URL}</string>
    <key>EndpointIdentifier</key>
    <string>{{deviceid}}</string>
    <key>BrowserLoginEnabled</key>
    <true/>
</dict>

{{deviceid}} is an AirWatch lookup value. AirWatch substitutes it with the unique device identifier at runtime.

After the mobile app is configured, end users need to associate the app with their accounts by enrolling the mobile app. For more information, see Enroll mobile devices.

Deploy using Microsoft Intune
Configure using AirWatch MDM
Contact the docs team

Was this topic helpful?
