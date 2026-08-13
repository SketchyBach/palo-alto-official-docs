<!-- KOI source: https://docs.koi.ai/integration-guides/mdm/intune-guide/deploy-certificate.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/mdm/intune-guide/deploy-certificate.md).

# Intune - Deploy certificate

**Prerequisites**

* Access to the Intune management dashboard.
* The **Koi certificate file** (`.cer`).
  * Make sure you have the `.cer` because Microsoft InTune **doesn't** support `.pem` certificates.
* Internet access from managed devices.

***

**Integration Steps**

1. **Navigate to the Configuration Section**
   * In the Intune admin center, go to **Devices > Configuration**.
   * Click **+ Create** to start and then **New Policy**.
2. **Select Platform and Profile Type**
   * Platform: **Windows 10 and later**.
   * Profile type: **Templates > Trusted certificate**
   * Click **Create**.
3. **Name the Policy**
   * Enter a **Name** (e.g., `"Koi Certificate Deployment"`).
   * Optionally add a **Description**.
   * Click **Next**.
4. **Upload the Certificate**
   * Upload the `.cer` file.
   * Set the **Destination Store** to **Computer certificate store - Root**.
   * Click **Next**.
5. **Assign Scope Tags**
   * Click **Next**.
6. **Assign to Groups**
   * Under **Assignments**, select the device or user groups that should receive the certificate.
   * Click **Next**.
7. **Apply Applicability Rules**
   * You can leave this **empty**.
   * Click **Next**.
8. **Review and Create**
   * Review your settings.
   * Click **Create** to deploy the certificate profile.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/mdm/intune-guide/deploy-certificate.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
