<!-- KOI source: https://docs.koi.ai/integration-guides/network/establish-route/umbrella-guide.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/network/establish-route/umbrella-guide.md).

# Cisco Umbrella Guide

#### **Prerequisites**

Before starting the integration, make sure you have the following:

1. **Access to the Cisco Umbrella Dashboard** with admin privileges.
2. **Organizational Root Certificate Authority (CA):** Ensure it is installed and trusted by your organization's devices.
3. **List of Marketplace Domains:** Provided by Koi.
4. **Proxy IP Address/FQDN + Port:** Provided by Koi.
5. **Signed Certificate:** The CSR provided by Koi has been signed with your root CA.
6. Cisco Umbrella **SIG Essentials** license, or higher tier that supports SWG.

***

#### **Steps to Integrate**

**1. Add Marketplace Domains to External Domains**

1. Navigate to **Deployments → Configuration → Domain Management**.
2. Select the **External Domains** tab.
3. Add each marketplace domain provided by Koi.
4. Click **Save**.

> This ensures marketplace traffic bypasses Umbrella's SWG and is routed directly to Koi's proxy.

***

**2. Establish Trust**

Since marketplace traffic bypasses Umbrella, endpoints connect directly to Koi's proxy. Endpoints must therefore trust Koi's certificate.

For instructions on deploying Koi's CA to your endpoints, see [Establishing Trust](https://docs.koi.ai/integration-guides/network/index-2).

***

**3. Upload a Custom PAC File**

1. Navigate to **Policies → Management → Web Policy → Global Settings → Custom Files**.
2. Click **Upload PAC File**.
3. Upload the PAC file provided by Koi.
   * The PAC file is located in your deployment portal under **Set up Network → 2. Umbrella Integration**.
4. Click **Save**.

> The PAC file routes marketplace domains to Koi's proxy while leaving all other traffic unaffected.

***

**4. Verify the Integration**

1. From a managed endpoint, access any marketplace domain and navigate to `/koi`.
2. You should see Koi's custom page, confirming traffic is being routed correctly.

***

#### **Summary**

By completing these steps, you have successfully configured Cisco Umbrella to integrate with Koi. Marketplace domains bypass Umbrella's SWG and are securely routed to Koi's proxy for enhanced security and control.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/network/establish-route/umbrella-guide.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
