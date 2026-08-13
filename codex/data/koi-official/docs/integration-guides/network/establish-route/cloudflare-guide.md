<!-- KOI source: https://docs.koi.ai/integration-guides/network/establish-route/cloudflare-guide.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/network/establish-route/cloudflare-guide.md).

# Cloudflare Guide

This guide explains how to integrate Koi with **Cloudflare Zero Trust** using a **DNS override policy** to direct marketplace traffic to Koi's proxy. Follow the steps below to ensure a smooth and secure configuration.

***

### **Prerequisites**

Before starting the integration, make sure you have the following:

1. **Access to Cloudflare Zero Trust Admin Panel**
2. **Organizational Root Certificate Authority (CA):** Ensure it is installed and trusted by your organization's devices.
3. **List of Marketplace Domains:** Provided by Koi.
4. **Proxy FQDN:** Provided by Koi.
5. **Signed Certificate:** The CSR provided by Koi has been signed with your root CA.

***

### **Steps to Integrate**

#### **1. Create a List of Marketplace Domains**

1. Navigate to the **Cloudflare Admin Panel**.
2. Go to **My Team → Lists**.
3. Create a new list:
   * Choose **Manual Creation** or **Upload a CSV**.
   * Assign a descriptive name, such as `Koi Marketplace Domains`.
   * Set the list type to **Hostnames**.
4. Insert the marketplace domains provided by Koi.
5. Save the list.

***

#### **2. Create a DNS Policy**

1. Navigate to **Gateway → Firewall Policies → DNS**.
2. Click on **Add a Policy**.
3. Configure the policy:
   * Assign an indicative name, such as `Koi DNS Override`.
   * Under **Traffic**, add a **Domain** selector:
     * Set the operator to **"in list"**.
     * Choose the list created in Step 1.
   * Under **Select an Action**, choose **Override**.
     * Enter the proxy's FQDN provided by Koi.
4. Click **Create Policy** to save.

***

#### **3. Create an HTTP Policy**

1. Navigate to **Gateway → Firewall Policies → HTTP**.
2. Click on **Add a Policy**.
3. Configure the policy:
   * Assign an indicative name, such as `Koi Allow`.
   * Under **Traffic**, add a **Domain** selector:
     * Set the operator to **"in list"**.
     * Choose the list created in Step 1.
   * Under **Select an Action**, choose **Allow**.
   * Under **Untrusted Certificate Action**, select **Pass Through** (this ensures the certificate is validated by your organization’s root CA rather than Cloudflare’s CA).
4. Click **Create Policy** to save.

***

### **Summary**

By completing these steps, you have successfully configured Cloudflare Zero Trust to integrate with Koi. This integration ensures that all marketplace traffic is securely directed to Koi's proxy for enhanced security and control.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/network/establish-route/cloudflare-guide.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
