<!-- KOI source: https://docs.koi.ai/integration-guides/network/establish-route/zscaler-guide.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/network/establish-route/zscaler-guide.md).

# Zscaler Guide

This guide explains how to integrate Koi with **Zscaler ZIA** using **proxy chaining** to direct marketplace traffic to Koi's proxy. Follow the steps below to ensure a smooth and secure configuration.

***

### **Prerequisites**

Before starting the integration, make sure you have the following:

1. **Access to Zscaler ZIA Panel**.
2. **Organizational Root Certificate Authority (CA):** Ensure it is installed and trusted by your organization's devices.
3. **List of Marketplace Domains:** Provided by Koi.
4. **Proxy IP Address/FQDN + Port:** Provided by Koi.
5. **Signed Certificate:** The CSR provided by Koi has been signed with your root CA.
6. Zscaler Advanced Firewall license, or other tier that supports proxy chaining

***

### **Steps to Integrate**

#### **1. Upload Your CA to Zscaler**

1. If organizational CA is already uploaded to Zscaler skip to step 2.
2. Navigate to **Zscaler ZIA Panel**.
3. Navigate to **Administration → Root Certificates**.
4. Add a new CA:
   1. Choose **Add Root Certificate** (top-left corner).
   2. Fill in the following attributes:
      1. **Name**: Assign a descriptive name
      2. **Type**: Choose Proxy Chaining
      3. **Content**: Choose the CA `.pem` file you used to sign Koi CSR
5. Click Save.

***

#### **2. Create a Proxy Item**

1. Navigate to **Administration → Proxies & Gateways → Proxies (tab)**.
2. Add a new proxy:
   1. Choose **Add Proxy** (top-left corner).
   2. Fill in the following attributes:
      1. **Proxy Name**: Assign a descriptive name, such as Koi Proxy
      2. **IP Address / FQDN**: Provided by Koi
      3. **Port**: Provided by Koi
      4. **Proxy’s Root Certificate**: Choose the organizational CA you used to sign Koi CSR
      5. **Insert X-Authenticated-User**: Make sure the toggle is **on**
      6. **Enable Base64 Encoding for X-Authenticated-User value**: Turn **off**
3. Save the Proxy.

***

#### **3. Create a Proxy Gateway**

1. Go to **Administration → Proxies & Gateways → Proxy Gateways (tab)**.
2. Add a new gateway:
   1. Choose **Add Gateway for Proxies** (top-left corner).
   2. Fill in the following attributes:
      1. **Gateway Name**: Assign a descriptive name, such as Koi Gateway
      2. **Fail Close**: Leave it on
      3. **Primary Proxy**: The name of the proxy you created in Step 1
      4. **Secondary Proxy**: Leave it as None
3. Save the gateway.

***

#### **4. Create a Forwarding Control Policy**

1. Navigate to **Policy → Forwarding Control**.
2. Click on **Add a Policy**.
3. Add a Forwarding Rule:
   1. Choose **Add Forwarding Rule** (top-left corner).
   2. Fill in the following attributes:
      1. **Rule Name**: Assign a descriptive name, such as Koi Forwarding
      2. **Rule Order**: Highest priority possible
      3. **Rule State**: Enabled
      4. **Forwarding Method**: Proxy Chaining
   3. Navigate to the Destination tab.
   4. Enter the given list of marketplace domains.
   5. Click **Add Items**.
   6. In the **Action section**, choose the name of the gateway you created in Step 2.

***

#### **5. Activate Your Changes**

1. Hover over **Activation button** (on the sidebar).
2. Click **Activate** to apply your changes.

***

### **Summary**

By completing these steps, you have successfully configured Zscaler ZIA to integrate with Koi. This integration ensures that all marketplace traffic is securely directed to Koi's proxy for enhanced security and control.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/network/establish-route/zscaler-guide.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
