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
