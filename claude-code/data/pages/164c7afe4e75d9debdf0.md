---
url: https://docs.koi.ai/integration-guides/network/establish-route/pac-file-integration/deploy-pac-file-using-jamf-pro
fetched_at: 2026-09-06T10:23:55.446Z
source: koi-official-browser
capture_method: authenticated official browser
---

# Deploy PAC File using Jamf Pro

For the complete documentation index, see llms.txt. This page is also available as Markdown.
Ask
DocumentationIntegration GuidesNetworkEstablish RoutePAC File Integration
Deploy PAC File using Jamf Pro

Easily deploy Koi PAC File using Jamf Pro

Establish trust before configuring any route. See Establishing Trust.

This guide explains how to deploy Koi's PAC file using Jamf Pro. The approach is to use a configuration profile to ensure robustness for the configuration set. Once the PAC file is set the endpoint should route through Koi's proxy for the defined marketplaces.

Prerequisites

Access to Jamf Pro.

An already established method of trust, see Establishing Trust

Access to Koi deployment portal.

Steps to integrate
Access Jamf Pro

Sign in to Jamf Pro (web UI)

Make sure you have an account that can edit Configuration Profiles.

Navigate to the Configuration Profiles area.

From the left sidebar select Computers, then Configuration Profiles.

Create a new profile (or edit an existing one)

Click New (or click the profile you want to modify).

Add the Proxies payload

In the payload list, find and select Proxies (the screenshot you provided shows this payload).

This opens the Proxies options on the right.

Enable Automatic Proxy Configuration

Under Hosts & Domains (or the Proxies section) check Enable Automatic Proxy Configuration.

In the field that appears paste your PAC URL. The URL is found in your Koi deployment portal → Network Integration → PAC File Integration.

Save the profile

Give the profile a clear Display Name (e.g., Koi Proxy Setup), add any description.

Set Scope (who gets it)

Switch to the Scope tab of the profile.

Add target computers (Static Group, Smart Group, or individual devices).

Use Exclusions as needed.

Deploy; Save/apply the profile (if not already saved). Jamf Pro will deliver the profile at next check-in

Verify on a macOS client

Check the automatic proxy URL for a service by running scutil --proxy

It is also possible to perform an interactive test by browsing to one of the configured domains in the PAC file with /koi as a path. For example: https://marketplace.visualstudio.com/koi for VSCode marketplace.

 A custom page served by the Koi proxy that verifies that you are routing through Koi Proxy

Rollback / Remove

To remove the PAC from devices

Edit the Configuration Profile and either uncheck Enable Automatic Proxy Configuration or remove the profile from Scope (or delete the profile).

Save changes. Devices will receive the updated profile at next check-in and proxy settings will be removed.

Previous
PAC File Integration
Next
Deploy PAC File manually

Last updated 2 months ago
