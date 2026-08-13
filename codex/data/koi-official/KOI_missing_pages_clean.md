# KOI Missing Documentation Pages

This file contains the 13 KOI documentation pages that were not captured by the automated downloader.
Repeated GitBook agent-instruction blocks were removed. Product content, commands, tables, links, and image references were preserved.

## Contents

1. [Contacting Support](#contacting-support)
2. [Associated with Malicious Campaign](#associated-with-malicious-campaign)
3. [Identity & Authentication Permissions](#identity--authentication-permissions)
4. [Palo Alto Cortex XDR](#palo-alto-cortex-xdr)
5. [Kandji Guide](#kandji-guide)
6. [Deploy Koi Root CA via Jamf Pro](#deploy-koi-root-ca-via-jamf-pro)
7. [Fortinet FortiGate Guide](#fortinet-fortigate-guide)
8. [Netskope Guide](#netskope-guide)
9. [Deploy PAC File using Jamf Pro](#deploy-pac-file-using-jamf-pro)
10. [Sonatype Nexus (Post POV)](#sonatype-nexus-post-pov)
11. [SSO Set Up](#sso-set-up)
12. [JIT user provisioning for SSO](#jit-user-provisioning-for-sso)
13. [Audit logs](#audit-logs)

---

Source: https://docs.koi.ai/get-started/contacting-support.md

# Contacting Support

### How to contact our technical support team:

Should you encounter any issues with the platform, please navigate to your Palo Alto Networks Customer Support Portal to open a ticket and a member of our Technical Support team will be happy to assist you. You can use this link to log in to the CSP:

[support.paloaltonetworks.com](https://support.paloaltonetworks.com)


---

---

Source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index/associated-with-malicious-campaign.md

# Associated with Malicious Campaign

**Severity**

🔴 Critical (10)

**Short Description**

Flags items that have been linked to known malicious campaigns based on threat intelligence or prior incidents. Indicates coordinated activity with intent to compromise, deceive, or exploit users.

**Suggestion**

Immediately remove the item from the endpoint to prevent compromise and contain the threat. This is a critical security threat requiring urgent action.

**Information**

Items linked to known malicious campaigns pose an immediate and severe threat to organizational security and user safety. These items have been identified through threat intelligence feeds, security research, or prior security incidents as being part of coordinated malicious operations orchestrated by threat actors. Such campaigns are deliberately designed with malicious intent to compromise endpoints, deceive users, steal sensitive information, or exploit system vulnerabilities. When an item is flagged as associated with a malicious campaign, it indicates that the item is not an isolated threat but part of a broader, organized attack strategy. This represents one of the most dangerous types of threats that can be present on an endpoint, as the item's behavior and objectives are confirmed malicious rather than merely suspicious.

**Risks of Associated with Malicious Campaign**

* **Endpoint Compromise**: The item may contain malicious code designed to gain unauthorized access to the endpoint and its resources.
* **Data Theft and Exfiltration**: Coordinated campaigns often target sensitive data such as credentials, financial information, or proprietary business data.
* **User Deception and Social Engineering**: The item may employ deceptive tactics to manipulate users into revealing sensitive information or performing harmful actions.
* **Network Propagation**: As part of a coordinated campaign, the item may attempt to spread to other endpoints or systems within the organization.
* **Command-and-Control Communication**: The item may establish connections with attacker infrastructure to receive instructions or exfiltrate data.
* **Persistent Threat Presence**: Campaign-related items often include mechanisms to maintain persistence on the endpoint even after detection attempts.

**Recommended Actions**

1. **Immediate Action**:
   * **Isolate the Endpoint**: Immediately disconnect the affected endpoint from the network to prevent further malicious activity and potential lateral movement.
   * **Remove the Item**: Uninstall the item immediately and terminate any associated processes.
   * **Initiate Incident Response**: Activate your organization's incident response plan and engage security teams immediately.
2. **Investigation and Containment**:
   * **Threat Intelligence Review**: Investigate the specific malicious campaign associated with the item to understand attack vectors, indicators of compromise, and potential impact.
   * **Endpoint Forensics**: Conduct a thorough analysis of the endpoint to identify any malicious activities, data accessed, or modifications made by the item.
   * **Network Traffic Analysis**: Review network logs for suspicious outbound connections, data exfiltration attempts, or communication with known malicious infrastructure.
   * **Scope Assessment**: Check for signs that the campaign has affected other endpoints or users within the organization.
3. **Recovery and Prevention**:
   * **Credential Reset**: Change passwords and credentials for any accounts that may have been accessed from the affected endpoint.
   * **Deploy Threat Intelligence**: Update security tools with indicators of compromise related to the malicious campaign to prevent reinfection.
   * **Security Policy Review**: Strengthen endpoint security policies and implement stricter controls for item installation and approval processes.
   * **Report to Authorities**: Consider reporting the incident to relevant cybersecurity authorities, law enforcement, and the platform provider.
   * **User Education**: Inform users about the campaign and provide guidance on identifying similar threats in the future.


---

---

Source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-4/identity-authentication-permissions.md

# Identity & Authentication Permissions

**Severity**

🟡 Medium (5)

**Short Description**

Flags items that request access to user identity or authentication flows. These capabilities may expose session credentials or login behavior, increasing the risk of impersonation, session hijacking, or unauthorized account access.

**Suggestion**

Carefully review the item's permissions and assess whether access to identity and authentication flows is necessary for its intended functionality. Consider removing or replacing the item if the permissions appear excessive or if the item's purpose does not justify such sensitive access.

**Information**

Items requesting access to user identity or authentication flows have the ability to interact with sensitive credential data, session tokens, and login mechanisms. While some items may require these permissions for legitimate purposes such as single sign-on or authentication management, these capabilities can also be exploited by malicious actors to compromise user accounts. When an item has access to authentication flows, it can potentially observe, intercept, or manipulate session credentials and login behavior, creating opportunities for unauthorized access to user accounts and organizational systems.

**Included Permissions**

* cookies
* webAutheticationProxy
* pkcs11
* webRequestAuthProvider
* signedInDevices

**Risks of Identity & Authentication Permissions**

* **Session Hijacking**: The item may capture or manipulate active session tokens, allowing attackers to impersonate legitimate users without needing passwords.
* **Credential Exposure**: Access to authentication flows could expose login credentials, enabling unauthorized account takeover.
* **Account Impersonation**: The item could leverage captured identity information to perform actions on behalf of users, potentially accessing sensitive data or systems.
* **Persistent Unauthorized Access**: Compromised authentication mechanisms can provide ongoing access to user accounts even after password changes.

**Recommended Actions**

1. **Investigate the Item**:
   * **Review Permission Justification**: Determine whether the item's core functionality legitimately requires access to identity and authentication flows.
   * **Evaluate Publisher Trust**: Verify the publisher's reputation and history, particularly regarding handling of sensitive data.
   * **Assess Usage Context**: Identify which users have this item installed and what level of access they have to sensitive systems.
2. **Immediate Action**:
   * **Restrict or Remove**: If the permissions appear excessive or unjustified, remove the item from affected endpoints.
   * **Monitor Activity**: Track the item's behavior for any unusual authentication-related activities or network requests.
   * **Review Access Logs**: Check authentication logs for suspicious login patterns or session anomalies that may indicate exploitation.


---

---

Source: https://docs.koi.ai/integration-guides/edr/palo-alto-cortex-xdr.md

# Palo Alto Cortex XDR

This guide provides step-by-step instructions to deploy the Koi Script Package to your managed endpoints using Palo Alto Networks Cortex XDR.

***

## Prerequisites

* **Access to the Cortex XDR Management Console with permissions** to create and run scripts.
* **Python Script Package** - found in your Deployment Portal.
* **Endpoints with Cortex XDR Agent** installed and active.

***

## Step 1: Download the Koi Script

1. **Log in to the Koi Deployment Portal**.
2. **Download the correct version** for each operating system you plan to deploy to (e.g., Windows, macOS).
   1. If your environment includes multiple OS types, ensure you download all relevant versions to cover your deployment needs.
3. **Keep the Script Package unmodified** unless instructed by Koi Support.

### Optional - Test the Script Locally

1. **Ensure Python 3.8+ is installed** on your test machine.
2. **Run the script** through Python.
3. **Review Koi's deployment portal**.
   1. You should see your endpoint under the Endpoints section.
   2. **Review the output or logs** to verify the script completes successfully. This step ensures that no environment-specific issues block deployment.

***

## Step 2: Upload the Script to Cortex XDR

1. Log in to Cortex XDR Console.
2. Navigate to **Incident Response → Response → Action Center → Agent Script Library**.
3. Click **+ New Script**.
4. **Upload** the Script Package.
5. **Fill out** the necessary details in the form:
   1. Name: Koi Script Package.
   2. Description: Deploy Koi Script Package for endpoint registration, discovery, or remediation tasks.
   3. Supported OS: Make sure you have uploaded the correct script for the OS.
6. Save the script. It will now be available in the Script Library.

***

## Step 4: Deploy the Script Manually

1. Go to **Incident Response → Response → New Action → Run Endpoint Script**.
2. **Choose Koi's Script Package**, defined in "Step 2: Upload the Script to Cortex XDR".
3. **Select one or more** target endpoints.
4. Click **Next**.
5. Click **Run and wait for completion**.
6. **Review the execution results** to confirm success.
   1. See the endpoints under the Endpoints section in Koi's Deployment Portal..

***

## Step 5: Orchestrating Recurring Execution

Cortex XDR’s native interface allows on-demand execution only.

For recurring, automated execution at scale, organizations typically integrate with:

* Cortex XSOAR Playbooks (for scheduling and orchestration).

  OR
* Custom scripts or tools calling the XDR public API (advanced use cases).

***

## Step 6: Uninstall Koi (Rollback)

Run rollback on each endpoint (Administrator on Windows, `sudo` on macOS). Cortex XDR’s Run Endpoint Script action cannot uninstall Koi by itself, it always runs in normal discovery mode.

**Windows:** use the Cortex script you already have:

`$env:KOI_ROLLBACK = "1"`\
`python "C:\path\to\mdm-cortex.py"`

If anything remains, download `mdm.pyz.ps1` from the Deployment Portal (standard package, not the Cortex wrapper) and run:

`powershell -ExecutionPolicy Bypass -File ".\mdm.pyz.ps1" --rollback`

**macOS:** download `mdm.pyz.sh` from the Deployment Portal (standard package, not `mdm-cortex.py`), then:

`chmod +x mdm.pyz.sh`\
`sudo ./mdm.pyz.sh --rollback`

Verify: `C:\ProgramData\Koi` (Windows) or `/Library/Application Support/Koi` (macOS) is removed, and Koi entries are gone from agent hook files (e.g. Cursor `hooks.json`).

> Note: `mdm-cortex.py --rollback` does not work. On Windows, use the `KOI_ROLLBACK` environment variable as shown above.


---

---

Source: https://docs.koi.ai/integration-guides/mdm/kandji-guide.md

# Kandji Guide

This document provides step-by-step instructions on integrating **Koi** into your environment with [Kandji](https://support.kandji.io/kb/certificate-library-item).

## Configuration Guide

**Prerequisites**

* Access to the Kandji management dashboard.
* The configuration script provided by Koi.
* Internet access from managed devices.

**Integrations Steps**

1. Log in to Kandji's admin dashboard
2. In the sidebar, navigate to **LIBRARY**
3. In the top right corner, click the **Add Library Item** button
4. Search for the **Custom Scripts** component. Select it, then click **Add and configure** at the bottom right.
5. *Configuring the library*
   1. Add *title* to the component (eg: Koi Security)
   2. In the *Execution Frequency* section, select **Run every 15 minutes**
   3. inside *Script Details* -> *Audit Script*, paste the **Koi MDM script** provided to you
6. Press **Save** on the bottom right
7. Add the recent created *library* you created, into a **Blueprint** in order to apply the MDM script to the devices


---

---

Source: https://docs.koi.ai/integration-guides/network/establishing-trust/deploy-koi-root-ca-via-jamf-pro.md

# Deploy Koi Root CA via Jamf Pro

This guide explains how to deploy Koi's PAC file using Jamf Pro. The approach is to use a configuration profile to ensure robustness for the configuration set. Once the PAC file is set the endpoint should route through Koi's proxy for the defined marketplaces.

### Prerequisites

Access to Jamf Pro. An already established method of trust, see Establishing Trust Access to Koi deployment portal.

***

### Steps to integrate

#### Access Jamf Pro

1. Sign in to Jamf Pro (web UI).
   1. Make sure you have an account that can edit Configuration Profiles.
2. Navigate to the Configuration Profiles area.
   1. From the left sidebar select Computers, then Configuration Profiles.

#### Create a new profile (or edit an existing one)

1. Click New (or click the profile you want to modify).
2. In the payload list choose Certificates (or Certificate).
3. Click Upload and select your Root CA file (DER/PEM).
   1. Download Koi's Root CA. The certificate is located in your Koi deployment portal → Network Integration → Establish network trust.
   2. Jamf Pro accepts `DER` format.
   3. `openssl x509 -inform PEM -in {Koi Root CA}.pem -outform DER -out {Koi Root CA}.cer`
4. Name the profile (e.g., Koi Root CA), add description.
5. Switch to Scope and add target computers/groups.
6. Save → devices will receive the cert at next check-in.

#### Set Scope (who gets it)

1. Switch to the Scope tab of the profile.
2. Add target computers (Static Group, Smart Group, or individual devices).
3. Use Exclusions as needed.
4. Deploy; Save/apply the profile (if not already saved). Jamf Pro will deliver the profile at next check-in


---

---

Source: https://docs.koi.ai/integration-guides/network/establish-route/fortinet-fortigate-guide.md

# Fortinet FortiGate Guide

This guide describes how to configure **FortiGate** to forward HTTP/HTTPS traffic to **Koi Proxy** using **proxy chaining**. This setup ensures that traffic destined for specific domains is routed through Koi Proxy for inspection and policy enforcement.

***

## Prerequisites

Before starting, ensure you have the following:

* Access to your **FortiGate Admin Console** (Web or CLI).
* **Administrator privileges** to configure web proxy settings and security policies.
* **Koi Proxy CA certificate**, provided by Koi.
* **Covered domain names** - domains that should be forwarded to Koi Proxy. The list is provided by Koi.
* **Koi Proxy server address and port**

***

## Step 1 – Download and Upload the Koi CA Certificate

1. Obtain the **Koi Proxy CA certificate** from your Koi support team.
2. Log in to your **FortiGate Admin Console**.
3. Navigate to: **System → Certificates**
4. Click **Import → CA Certificate**.
5. Select the **Koi CA certificate file** and upload it.
6. Confirm the certificate is listed under **Trusted CA Certificates**.

> **Note:** This step ensures FortiGate trusts Koi Proxy when forwarding HTTPS traffic.

***

## Step 2 – Configure the Web Proxy Forwarding Server

1. In the FortiGate GUI, go to: **Network → Forwarding Servers**.
2. Click **Create New** and configure the following:
   * **Name:** `KoiProxy`.
   * **Type:** `Web Proxy Forwarding Server`.
   * **IP Address / FQDN:** `<Koi Proxy server address>`.
   * **Port:** `<Koi Proxy port>`.
   * **Authentication:** `None` (unless specified by Koi).
3. Click **OK** to save.

***

## Step 3 – Create a Proxy Policy for Target Domains

1. Navigate to: **Policy & Objects → Proxy Policy**
2. Click **Create New**.
3. Configure:
   * **Incoming Interface:** Your internal network interface (e.g., `LAN`)
   * **Outgoing Interface:** `Forwarding Server`
   * **Source:** `all` or specify internal subnets
   * **Destination:** Create an **Address Group** for Koi’s **covered domain names**:
     * Go to **Policy & Objects → Addresses → Create New**
     * Select **FQDN** type for each domain and add all domains provided by Koi
     * Group them into **"Koi-Domains"**
   * **Service:** `HTTP, HTTPS`
   * **Action:** `Forward to Proxy`
   * **Forward Server:** `KoiProxy`
4. Enable **SSL Inspection** and select the profile that trusts the **Koi CA certificate**.
5. Click **OK** to save the policy.

***

## Step 4 – Verify the Configuration

1. From a client machine behind FortiGate, attempt to access one of the covered domains.
2. Verify:
   * The traffic is being forwarded to Koi Proxy.
   * SSL certificates are trusted (no browser warnings).
   * Policy matches are logged in FortiGate under:
     * `Log & Report → Forward Traffic`

***

## Summary

By configuring FortiGate to forward specific domain traffic to Koi Proxy, you ensure that HTTP and HTTPS requests are routed through Koi for inspection and policy enforcement.

These steps provide a secure, reliable, and seamless connection between endpoints and Koi services.


---

---

Source: https://docs.koi.ai/integration-guides/network/establish-route/netskope-guide.md

# Netskope Guide

This guide explains how to integrate Koi with Netskope Secure Web Gateway (SWG) using two supported integration modes:

1. **Proxy Chaining** – Configure Netskope SWG to use Koi as an upstream proxy for specific marketplace domains.
2. **Bypass** – Configure Netskope SWG to bypass selected domains and deploy a PAC file to route those domains directly to Koi.

Follow the steps below to ensure a secure and enterprise-grade integration.

***

## **Prerequisites**

Before starting the integration, ensure you have the following:

* **Access to Netskope Admin Console** with SWG policies enabled.
* **Organizational Root Certificate Authority (CA)** installed and trusted by all managed endpoints.
* **List of marketplace domains** provided by Koi.
* **Koi proxy IP/FQDN and port** provided by Koi.
* **A Signed certificate** – Koi’s CA that would use to establish trust between Netskope and Koi’s proxy. Trust can be established using a CSR provided by Koi has been signed by your root CA as well.

***

## **Proxy Chaining Integration**

Use this mode when you want Netskope SWG to remain in the traffic path and forward selected domains to Koi for advanced inspection.

### **Step 1: Upload Koi Root CA to Netskope**

1. Log in to the **Netskope Admin Console**.
2. Navigate to **Settings → Manage → Certificates.**
3. Click **Upload Certificate**.
   1. Download Koi’s root CA from your deployment portal under **Set up Network → 1. Establish Network trust → Download CA**.
4. Provide:
   * **Name**: e.g., Koi Root CA
   * **Certificate Type**: *Trusted Root CA*
   * **Certificate File**: Upload the CA .pem file.
5. Click **Save** and ensure the CA is active.

### **Step 2: Create an Upstream Proxy Profile**

1. Go to **Settings →** **Manage →** **Forward to Proxy Integration**.
2. Click **SETUP Proxy**.
3. Add a new proxy profile:
   * **Proxy Name**: Koi Proxy
   * **Proxy FQDN**: Located in your deployment portal. **Set up Network → 2. Netskope Integration.**
   * **Port**: Located in your deployment portal. **Set up Network → 2. Netskope Integration.**
   * **Insert X-Authenticated-User header**: Enabled
4. Click **Save**

### Step 3: Create a Custom URL Category for Marketplace Domains

1. Navigate to **Policies → Profiles → Custom Categories**.
2. Click **Add New Category**.
3. Name the category, e.g., `Koi Marketplace Domains`.
4. Add all marketplace domains provided by Koi into this category.
   1. The list is located on your deployment portal under **Set up Network → 2. Netskope Integration.**
5. Save the custom category.

### **Step 4: Create a Forwarding Policy Rule**

1. Navigate to **Policies → Real-time Protection.**
2. Create new policy: **New Policy → Web Access.**
3. Configure:
   1. **Source** - the devices that should forward marketplace traffic to Koi.
      1. It is advised to create a test group.
   2. **Destination -** **Category** - configure the custom category
      1. Select the name of the category from step 3.
   3. **Profile & Action** - configure the Koi’s proxy profile
      1. Action: Forward to Proxy; Proxy - the name of the proxy given in step 2.
   4. **Policy Name** - the name of the policy, e.g., `Koi Forward Marketplace Domains`.
   5. **Group** - 1. Header Policies.
   6. **Status** - Enabled.
4. Save the policy rule.

### **Step 5: Activate Configuration**

1. Review all changes.
2. Click **Activate Configuration** in the Netskope Admin Console.
3. Confirm the policy is applied and active.
4. Access a marketplace domain and navigate to `/koi`.
   1. You should see Koi’s custom page.

This completes Proxy Chaining mode, ensuring Netskope remains in-line while securely forwarding marketplace traffic to Koi.

***

## **Bypass Integration**

Use this mode when you want specific domains to completely bypass Netskope SWG and be routed directly to Koi via a PAC file.

### **Step 1: Configure Traffic Steering Exception (Domains) to Bypass Netskope for Marketplace**

1. Log in to the **Netskope Admin Console**.
2. Navigate to
3. **Settings → Security Cloud Platform → Traffic Steering → \[Select your steering configuration, e.g. Default tenant config] → Exceptions tab**.
4. Click **New Exception**.
5. Choose **Exception Type: Domain**.
6. Add the marketplace domains provided by Koi.
   1. The list is located on your deployment portal under **Set up Network → 2. Netskope Integration.**
7. **Set Action = Bypass** to ensure the traffic is not steered to Netskope and goes direct to destination
   1. (Optional) Add a **Note** for audit tracking, such as “Koi bypass for marketplace traffic.”
8. Click **Save** to apply the bypass exception.

### **Step 2: Establish Trust**

Trust establishment can be done via settings up Koi’s CA in the connecting devices. Another approach is available by signing a CSR by a root CA, that is already installed on your devices in the organization.

For more information, see: [Establishing Trust](/integration-guides/network/establishing-trust.md)

### **Step 3: Deploy a PAC File for Marketplace Domains**

Once the steering exceptions are configured in Netskope, you must deploy a PAC file that routes the bypassed marketplace domains directly to Koi.

For more information, see [PAC File Integration](/integration-guides/network/establish-route/pac-file-integration.md)

***

## **Summary**

By following this guide, you can integrate Koi with Netskope SWG using either **Proxy Chaining** or **Bypass** mode:

* **Proxy Chaining** keeps Netskope in-line and forwards specific traffic to Koi.
* **Bypass** excludes specified domains from Netskope and routes them directly to Koi via PAC file.

Both approaches ensure marketplace traffic is securely directed to Koi for enhanced inspection, security, and control.


---

---

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

Source: https://docs.koi.ai/integration-guides/code-packages/upstream-integration-guide-post-pov/sonatype-nexus-post-pov.md

# Sonatype Nexus (Post POV)

### Introduction

Integrating Koi as an upstream registry in Sonatype Nexus Repository Manager allows your organization to enforce governance and security policies across all third-party packages before they reach developer environments or build pipelines.&#x20;

By routing package pulls through Koi, every package is evaluated, logged, and governed according to your policies - enabling centralized policy enforcement, real-time package inventory, and detailed audit trails for compliance and incident response.

This guide covers configuring npm or PyPI remote repositories in JFrog Artifactory to route through Koi.

### Configuration Guide

**Prerequisites**

* Access to your Nexus Repository Manager admin console
* Koi tenant provisioned with gateway URLs
* Network connectivity from Nexus to Koi gateway endpoints

**Integration Steps**

1. **Navigate to Repository Settings**
   * Log into Nexus Repository Manager
   * Go to **Settings > Repositories**
2. **Create or Edit Proxy Repository**
   * Click **Create repository** and select proxy type (`npm (proxy)` or `pypi (proxy)`)
   * Or edit an existing proxy repository
3. **Configure Remote Storage URL**

   * Replace the default public registry URL with the Koi gateway URL:

   | Package Type | Default URL                  | Koi Gateway URL                                     |
   | ------------ | ---------------------------- | --------------------------------------------------- |
   | npm          | `https://registry.npmjs.org` | `https://koi-npmjs-<customer>.gateway.koi.security` |
   | PyPI         | `https://pypi.org`           | `https://koi-pypi-<customer>.gateway.koi.security`  |
4. **Save Configuration**
   * Click **Save**
5. **(Optional) Add to Group Repository**
   * If using a group repository for unified access, add the Koi-configured proxy to the group members

***

### Traffic Flow

```
Developer → Nexus Proxy → Koi Gateway → Public Registry
                ↓              ↓
         Local Cache    Policy Check
```

***

### Validation

Test the Koi endpoint is reachable:

```bash
curl https://koi-npmjs-<customer>.gateway.koi.security/koi
```

***

### Known Limitations & Considerations

#### Caching Behavior

Nexus caches packages locally. Components cached **before** Koi integration remain accessible from cache and bypass Koi policy enforcement.

**Mitigations:**

* **Invalidate cache** after integration: **Settings > Repositories > \[Proxy Repository] > Invalidate Cache**
* For complete cache purge, clean up the blob store
* Ensure Koi is the sole upstream (no alternative routes to public registries)


---

---

Source: https://docs.koi.ai/integration-guides/single-sign-on/sso-saml-jit.md

# SSO Set Up

**Capabilities**

1. User creation and access is managed via your IdP.
2. Group mapping - Map groups to Koi platform's roles to manage users’ permissions in the platform. The current roles are:
   * **Read only** - **View** access to all platforms' sections
   * **Security** - **Full** access to all platform's sections, with exception of the settings page
   * **Admin** - **Full** access to all platform's sections

**Default Authentication**\
By default, user authentication to your tenant is done via a 'magic link' that is sent to authorized users' email address and is accessed through their inbox. The link will expire after 3 minutes and access will remain open for 30 days after using the link.

**How to set up SSO?**

Request SSO set-up link from your Koi customer experience representative, and by following the link, complete the Wizard set up process:

1. From the home page, select **SSO Configuration**

![](https://files.readme.io/37aac6c59d309d39e6cb0245b58587fbe61fd3f9af98a8d53c1b113407f5afad-image.png)

2. Choose your **IdP vendor** and click \***SAML**. You would then be forwarded to the "Service Provider Information" page, and be asked to fill the information according to the relevant vendor.

If you don't find your IdP vendor, use the generic configuration options at the bottom of the screen.

![](https://files.readme.io/67e00e2aefd775880f889a627d22981c31a639ca9073c704e03ae73b282e0c3a-image.png)

3. **User attribute mapping** - you can map attribute names from the IdP (name, email, etc.) to user attributes.

![](https://files.readme.io/29e03f110afe4e5415fc2c90587d464355fe357d029f216bfbc1395ea5534077-image.png)

4. **Group Attribute Mapping** you can add group attribute statements on the same page.

![](https://files.readme.io/3a665574a1b9e52a47949e02a9829baa6665d716d620be215343bb902dea0960-image.png)

5. **Add the Identity Provider information**

![](https://files.readme.io/a9a01827d362177b1cbbe1d6b23d2aa2cd170002e917809c41d036d379da3193-image.png)

6. **Assign Groups**:

![](https://files.readme.io/1afe470f904d98c87f31b7456311f0338b551718cbbe732fbd17fdc52f1843ff-image.png)

7. **SSO Domains** - Specify the approved domains for SSO

![](https://files.readme.io/91c0e10f5304943a00fe811aa894d6f88c130ef60f696e1b31a664a6d2721af2-image.png)

8. **Testing**- Perform the test at the end of the set up wizard. Please send the test results to your customer experience representative.

![](https://files.readme.io/cae7e94459cc439e04f201ec42cec832690325699ca49e6c80192ebced3288fb-image.png)

Once the set up wizard is complete, Koi's team will approve and complete the SSO configuration.


---

---

Source: https://docs.koi.ai/integration-guides/single-sign-on/jit-user-provisioning-for-sso.md

# JIT user provisioning for SSO

JIT user provisioning is optional but recommended. When enabled, Koi automatically creates user accounts the first time users sign in via SSO, eliminating the need for admins to manually invite them. The identity provider remains the source of truth, controlling who has access to Koi. Users must still be granted access through the identity provider before their account can be provisioned in Koi.

To enable JIT provisioning, please reach out to your technical contact at Koi.


---

---

Source: https://docs.koi.ai/guides/audit-logs.md

# Audit logs

Koi generates audit logs across 8 categories to provide transparency, accountability, and compliance visibility. Each log includes a `type` field that maps to one of the categories below.

***

### 1. Items / Inventory

#### Description

The **Items/Inventory** audit log records activity related to inventory items. Includes installation and deletion events across your endpoints.

#### Trigger Conditions

* A new item is **installed**.
* An item is **deleted**.

#### Fields

| Field       | Description                   | Example                                                                                         |
| ----------- | ----------------------------- | ----------------------------------------------------------------------------------------------- |
| `type`      | Always `Extensions`           | `"Extensions"`                                                                                  |
| `message`   | Human-readable event message  | `"Extension ms-vscode.PowerShell version 2024.2.2 installed on device Amits-MacBook-Pro.local"` |
| `extension` | Identifier (publisher + name) | `ms-vscode.PowerShell`                                                                          |
| `version`   | Version involved              | `2024.2.2`                                                                                      |
| `action`    | `installed` or `deleted`      | `installed`                                                                                     |
| `device`    | Device hostname               | `Amits-MacBook-Pro.local`                                                                       |
| `timestamp` | UTC timestamp (if available)  | `2025-08-29T09:45:00Z`                                                                          |

#### Event Actions

* **Installed** → item added.
* **Deleted** → item removed.

#### Sample Log

```json
{
  "type": "Extensions",
  "message": "Extension KevinRose.vsc-python-indent deleted from device h-MacBook-Pro-sl-Ity.local"
}
```

#### Interpretation Guidance

* Tracks which items users install or remove.
* Deletions may be user-initiated, policy-driven, or security responses.

***

### 2. Firewall

#### Description

The **Firewall** audit log captures actions where Koi blocks or hides risky items during searches or lookups in marketplaces.

#### Trigger Conditions

* End user searches the marketplace.
* Restricted items are blocked (mitigated).

#### Fields

| Field        | Description              | Example                                                            |
| ------------ | ------------------------ | ------------------------------------------------------------------ |
| `type`       | Always `Firewall`        | `"Firewall"`                                                       |
| `message`    | Event message            | `"Mitigated 105 extensions searched by Lirons-MacBook-Pro.local."` |
| `hostname`   | Originating device       | `"Lirons-MacBook-Pro.local"`                                       |
| `mitigated`  | Count of items blocked   | `105`                                                              |
| `created_by` | User initiating search   | `"lironkaykov"`                                                    |
| `searchTerm` | (Optional) Term searched | `"gpt"`                                                            |
| `timestamp`  | UTC timestamp            | `2025-08-29T10:02:00Z`                                             |

#### Event Actions

* **Mitigated (N)** → N items blocked during a search.

#### Sample Log

```json
{
  "type": "Firewall",
  "message": "Mitigated 11 extensions searched by Amits-MacBook-Pro.local.",
  "hostname": "Amits-MacBook-Pro.local",
  "mitigated": 11,
  "created_by": "amit",
  "searchTerm": "gpt"
}
```

#### Interpretation Guidance

* Large `mitigated` values = broad searches.
* `searchTerm` helps identify blocked queries.

***

### 3. Guardrails

#### Description

The **Guardrails** audit log tracks enablement and disablement of protection mechanisms. Guardrails are global safety nets (e.g., Scan-first protection, Malware protection).

#### Trigger Conditions

* A guardrail is **enabled**.
* A guardrail is **disabled**.

#### Fields

| Field        | Description                          | Example                                         |
| ------------ | ------------------------------------ | ----------------------------------------------- |
| `type`       | Always `Guardrails`                  | `"Guardrails"`                                  |
| `message`    | Event message                        | `"Guardrail Scan-first protection was enabled"` |
| `created_by` | Actor making the change (user/email) | `"itay@koi.security"`                           |
| `timestamp`  | UTC timestamp                        | `2025-08-29T11:30:00Z`                          |

#### Event Actions

* **Enabled** → Guardrail turned on.
* **Disabled** → Guardrail turned off.

#### Sample Log

```json
{
  "type": "Guardrails",
  "message": "Guardrail Malware protection was enabled",
  "created_by": "itay@koi.security"
}
```

#### Interpretation Guidance

* Enables/Disables reflect administrative configuration changes.
* Critical for compliance audits and rollback checks.

***

### 4. Notifications

#### Description

The **Notifications** audit log records when alerts, messages, or updates are sent to users or external integrations. These logs provide visibility into which recipients received notifications about policy violations, guardrails, remediations, or test alerts.

#### Trigger Conditions

* Malware protection alert sent.
* Guardrail or policy-triggered alert sent.
* Test alert/notification triggered (for validation).
* Notifications delivered to external systems (Slack, email, API endpoint).

#### Fields

| Field       | Description                                                   | Example                                                                |
| ----------- | ------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `type`      | Always `Notifications`                                        | `"Notifications"`                                                      |
| `message`   | Human-readable event message describing notification          | `"Malware Protection notification sent to eitan@koi.security"`         |
| `recipient` | Target recipient (email or integration endpoint)              | `"eitan@koi.security"`                                                 |
| `context`   | Notification type or alert category (inferred from `message`) | `"Malware Protection"`, `"Test alerting for 'High Severity' findings"` |
| `timestamp` | \[If available] UTC timestamp of the log                      | `2025-08-29T12:15:00Z`                                                 |

#### Event Actions

* **Sent** → Notification successfully delivered.
* **Test Sent** → Test/broadcast message delivered.

#### Sample Log Entries

```json
{
  "type": "Notifications",
  "message": "Malware Protection notification sent to eitan@koi.security"
}
```

```json
{
  "type": "Notifications",
  "message": "notification sent to monitoring-extensioln-aaaaqqpsmf4gbxtqhusvdydp2u@phaidra-workspace.slack.com"
}
```

```json
{
  "type": "Notifications",
  "message": "Test alerting for 'High Severity' findings notification sent to yoni.shiloh@mobileye.com"
}
```

#### Interpretation Guidance

* Notifications confirm which recipients were informed of an event.
* Useful for auditing **alert coverage** (who was notified of a critical finding).
* Test alerts allow validation of notification pipelines without triggering real enforcement.
* Logs can be correlated with **Policies** and **Remediation** events to understand what action was taken and who was informed.

***

### 5. Remediation

#### Description

The **Remediation** audit log tracks when Koi automatically or manually removes risky items (extensions, add-ons, or packages) from endpoints.

#### Trigger Conditions

* A blocked item is forcibly uninstalled.
* An admin initiates a remediation task.
* A guardrail or policy automatically triggers remediation.

#### Fields

| Field                   | Description                                                   | Example                                                                   |
| ----------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `type`                  | Always `Remediation`                                          | `"Remediation"`                                                           |
| `user`                  | Username of actor who initiated or was subject to remediation | `"Itay"`                                                                  |
| `message`               | Human-readable event message                                  | `"Extension save-to-pocket version 4.0.6 remediated on device LT-IttayD"` |
| `hostname`              | Endpoint where remediation occurred                           | `"LT-ItayD"`                                                              |
| `extension.version`     | Version of the remediated item                                | `"4.0.6"`                                                                 |
| `extension.extensionId` | Unique ID of the remediated item                              | `"niloccemoadcdkdjlinkgdfekeahmflj"`                                      |
| `timestamp`             | \[If present] UTC timestamp                                   | `2025-08-29T13:20:00Z`                                                    |

#### Event Actions

* **Remediated** → Item forcibly removed.

#### Sample Log

```json
{
  "type": "Remediation",
  "user": "Itay",
  "message": "Extension save-to-pocket version 4.0.6 remediated on device LT-IttayD",
  "hostname": "LT-IttayD",
  "extension": {
    "version": "4.0.6",
    "extensionId": "niloccemoadcdkdjlinkgdfekeahmflj"
  }
}
```

#### Interpretation Guidance

* **Extension details** confirm what was removed.
* **Hostname** ties action to endpoint.
* **User** shows whether it was targeted or system-wide.
* Often correlates with **Guardrails** or **Policies**.

***

### 7. Settings

#### Description

The **Settings** audit log captures administrative and configuration changes in Koi. Includes user management, group creation, role assignments, invitations, and other system changes.

#### Trigger Conditions

* Group created/removed.
* User invited/deleted/role assigned.
* Risk score updated.
* Other configuration updates applied.

#### Fields

| Field        | Description                    | Example                     |
| ------------ | ------------------------------ | --------------------------- |
| `type`       | Always `Settings`              | `"Settings"`                |
| `message`    | Message describing the action  | `"Group created"`           |
| `created_by` | Actor who performed the action | `"itay@extensiontotal.com"` |
| `timestamp`  | \[If present] UTC timestamp    | `2025-08-29T14:10:00Z`      |

#### Event Actions

* **Group Created / Removed**
* **User Invited / Deleted / Role Assigned**
* **Risk Score Updated**
* **Other Configuration Updates**

#### Sample Log Entries

```json
{
  "type": "Settings",
  "message": "Group created",
  "created_by": "itay@extensiontotal.com"
}
```

```json
{
  "type": "Settings",
  "message": "Invited a new user to the system",
  "created_by": "itay@extensiontotal.com"
}
```

```json
{
  "type": "Settings",
  "message": "User updated a finding risk score",
  "created_by": "christopher.durgin@capitalone.com"
}
```

***

### 8. Policies

#### Description

The **Policies** audit log records the lifecycle of governance policies. It tracks when policies are created, updated, removed, or when their status changes.

#### Trigger Conditions

* Policy created.
* Policy removed.
* Policy status changed (enabled/disabled).
* Allowlist mode enabled.

#### Fields

| Field        | Description                          | Example                           |
| ------------ | ------------------------------------ | --------------------------------- |
| `type`       | Always `policies`                    | `"policies"`                      |
| `message`    | Message describing the policy action | `"Policy Block GPT Code created"` |
| `created_by` | Actor who performed the action       | `"amit@koi.security"`             |
| `timestamp`  | \[If present] UTC timestamp          | `2025-08-29T15:15:00Z`            |

#### Event Actions

* **Created**
* **Removed**
* **Status Changed**
* **Allowlist Mode Enabled**

#### Sample Log Entries

```json
{
  "type": "policies",
  "message": "Policy Block GPT Code created",
  "created_by": "amit@koi.security"
}
```

```json
{
  "type": "policies",
  "message": "Policy Block deprecated extensions removed",
  "created_by": "amit@koi.security"
}
```

```json
{
  "type": "policies",
  "message": "Policy Block Publisher Test status changed",
  "created_by": "christopher.durgin@capitalone.com"
}
```

```json
{
  "type": "policies",
  "message": "Allowlist mode enabled",
  "created_by": "itay@extensiontotal.com"
}
```

#### Interpretation Guidance

* Ensures full traceability for compliance.
* Shows evolution of governance (who created/removed what).
* Highlights enforcement changes.
* Allowlist mode = strict governance baseline..

***


---
