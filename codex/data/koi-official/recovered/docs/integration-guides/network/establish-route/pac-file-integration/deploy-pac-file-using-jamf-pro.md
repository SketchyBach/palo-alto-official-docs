Source: https://docs.koi.ai/integration-guides/network/establish-route/pac-file-integration/deploy-pac-file-using-jamf-pro.md

# Deploy PAC File using Jamf Pro

{% hint style="warning" %}
Establish trust before configuring any route. See [Establishing Trust](/integration-guides/network/establishing-trust.md).
{% endhint %}

***

This guide explains how to deploy Koi's PAC file using Jamf Pro. The approach is to use a configuration profile to ensure robustness for the configuration set. Once the PAC file is set the endpoint should route through Koi's proxy for the defined marketplaces.

***

### Prerequisites

1. Access to Jamf Pro.
2. An already established method of trust, see [Establishing Trust](/integration-guides/network/establishing-trust.md)
3. Access to Koi deployment portal.

***

### Steps to integrate

#### Access Jamf Pro

1. Sign in to Jamf Pro (web UI)
   1. Make sure you have an account that can edit Configuration Profiles.
2. Navigate to the Configuration Profiles area.
   1. From the left sidebar select Computers, then Configuration Profiles.

#### Create a new profile (or edit an existing one)

1. Click New (or click the profile you want to modify).
2. Add the Proxies payload
   1. In the payload list, find and select Proxies (the screenshot you provided shows this payload).
   2. This opens the Proxies options on the right.
3. Enable Automatic Proxy Configuration
   1. Under Hosts & Domains (or the Proxies section) check Enable Automatic Proxy Configuration.
   2. In the field that appears paste your PAC URL. The URL is found in your Koi deployment portal → Network Integration → PAC File Integration.
4. Save the profile
   1. Give the profile a clear Display Name (e.g., Koi Proxy Setup), add any description.

#### Set Scope (who gets it)

1. Switch to the Scope tab of the profile.
2. Add target computers (Static Group, Smart Group, or individual devices).
3. Use Exclusions as needed.
4. Deploy; Save/apply the profile (if not already saved). Jamf Pro will deliver the profile at next check-in

### Verify on a macOS client

1. Check the automatic proxy URL for a service by running `scutil --proxy`
2. It is also possible to perform an interactive test by browsing to one of the configured domains in the PAC file with `/koi` as a path. For example: `https://marketplace.visualstudio.com/koi` for VSCode marketplace.

![](https://files.readme.io/80f473027f6c410d22dc1640f1175f1f0fc8f716f5f36442481ecc8f13ed073b-image.png) *A custom page served by the Koi proxy that verifies that you are routing through Koi Proxy*

### Rollback / Remove

To remove the PAC from devices

1. Edit the Configuration Profile and either uncheck Enable Automatic Proxy Configuration or remove the profile from Scope (or delete the profile).
2. Save changes. Devices will receive the updated profile at next check-in and proxy settings will be removed.


---

---
