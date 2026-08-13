<!-- KOI source: https://docs.koi.ai/integration-guides/network/establish-route/bluecoat-guide.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/network/establish-route/bluecoat-guide.md).

# BlueCoat Guide

This guide explains how to integrate Koi with **Blue Coat ProxySG** using **proxy chaining** to direct marketplace traffic to Koi’s proxy. Follow the steps below to ensure a secure and reliable configuration.

***

### **Prerequisites**

Before starting the integration, make sure you have the following:

1. **Access to Blue Coat ProxySG** admin interface.
2. **Koi root CA** from your Koi deployment portal.
3. **Proxy FQDN + port** from your Koi deployment portal.
4. **List of marketplace domains** from your Koi deployment portal.
5. SSL interception configured on ProxySG.

***

### **Steps to Integrate**

#### **1. Import the Koi Root CA into Blue Coat**

1. Navigate to **Configuration tab → SSL → CA Certificates → CA Certificates tab**.
2. Click **Import**, then upload the Koi root CA.

***

#### **2. Configure Koi as a Forwarding Host**

1. Go to **Configuration tab → Forwarding → Forwarding Hosts → Forwarding Hosts tab**.
2. Click **New**.
3. Set the **Host** to the proxy FQDN provided by Koi.
4. Set the **HTTP Port** as provided by Koi.
5. Click **OK** to save.

***

#### **3. Define Marketplace Domains as a Category**

1. Open **Configuration tab → Policy → Visual Policy Manager → Configuration → Edit Categories**.
2. Create a new category object in the Blue Coat ProxySG policies and add the marketplace domains provided by Koi.
3. Save the new category.

***

#### **4. Create a Forwarding Layer for Marketplace Traffic**

1. In **Visual Policy Manager**, go to the **Forwarding Layer** tab.
2. Add a new rule:
   * **Destination**: Select the category object created in Step 3.
   * **Action**: Set to the forwarding object pointing to the Koi proxy.
   * **Service**: Set to **ALL HTTPS** to forward HTTPS traffic only.

***

#### **5. Enable SSL Interception**

1. In **Visual Policy Manager**, go to the **SSL Intercept Layer** tab.
2. Add a rule:
   * **Destination**: Set as needed to target marketplace domains.
   * **Action**: Set to **Enable SSL Interception**.

> This step is required to insert identity headers and capture HTTPS traffic.

***

#### **6. Add Headers for Identity Forwarding**

1. Go to **Web Access Layer** in **Visual Policy Manager**.
2. Add a rule:
   * **Destination**: Use the marketplace domain category.
   * **Action**: Create a **Combined Action Object**:
     * Add a **Control Request Header** to set `X-Authenticated-User` to the authenticated user ID.
   * **Service**: Apply only when the request is being forwarded to Koi (optionally using a Health Status object).

***

#### **7. Apply the Policy**

1. In **Visual Policy Manager**, click **Install Policy** to apply all changes.

***

### **Summary**

You have successfully integrated Blue Coat ProxySG with Koi using proxy chaining. This setup ensures all relevant marketplace traffic is securely forwarded to Koi’s proxy for analysis and enforcement.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/network/establish-route/bluecoat-guide.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
