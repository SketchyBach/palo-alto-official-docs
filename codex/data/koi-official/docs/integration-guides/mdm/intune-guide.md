<!-- KOI source: https://docs.koi.ai/integration-guides/mdm/intune-guide.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/mdm/intune-guide.md).

# Intune Guide

This document provides step-by-step instructions on integrating **Koi** into your environment with Microsoft Intune.

## **Windows Service**

#### **Prerequisites**

* Access to the Intune management dashboard.
* Intune remediation requires Windows 10/11 Enterprise E3 or E5 (included in Microsoft 365 F3, E3, or E5) or Windows 10/11 Education A3 or A5 (included in Microsoft 365 A3 or A5)
* Verify your tenant has the required license and then:
  * Under Tenant administration > Connectors and tokens > Windows data
  * Expand Windows license verification
  * Set “I confirm that my tenant owns one of these licenses” to ON
* The MSI provided by Koi.
* Internet access from managed devices.

#### Steps

1. **Navigate to the Apps Section**
   * Go to **Apps > Windows**.
   * Click **Create**.
2. **Select App Type**
   * Under **Other**, select **Line-of-business app**.
   * Click **Select**.
3. **Upload the MSI File**
   * Click **Select app package file**.
   * Upload the **Koi.msi** file.
   * Click **OK**.
4. **Configure App Information**
   * Enter a **Name** (e.g., `"Koi Installer"`)
   * Enter a **Description**.
   * Write "Koi" as the **Publisher**.
   * Set the Command-Line arguments:
     * ```
       CUSTOMERID="<YOUR_CUSTOMER_ID>" CUSTOMERSLUG="<YOUR_CUSTOMER_SLUG>" INTERVAL=60
       ```
     * INTERVAL is the execution frequency in minutes
   * Click **Next**.
5. **Configure scope tags for this application**
   * Configure Scope Tags.
   * Click **Next**.
6. **Assign the App**
   * Under **Assignments**, select device or user groups.
   * Choose **Required** to install automatically or **Available** to show in the Company Portal.
   * Click **Next**.
7. **Review and Create**
   * Review all settings.
   * Click **Create** to deploy the MSI.

***

## **MacOS LaunchDaemon**

**Prerequisites**

* Access to the Intune management dashboard.
* macOS devices enrolled in Intune.
* The `koi-security-mdm.pkg` file provided by Koi (downloaded from your Koi dashboard).
* Your `CUSTOMER_ID` and `XT_ENV` values from the Koi deployment portal.
* Internet access from managed devices (HTTPS connectivity to Koi's domain).

1. **Add the macOS App**
   * In the Intune admin center, navigate to **Apps > macOS**.
   * Click **+ Add**.
   * Under **App type**, select **macOS app (PKG)** from the dropdown.
   * Click **Select**.
2. **Configure the App**
   * Upload the `koi-security-mdm.pkg` file.
   * Enter a **Name** (e.g., `"Koi Security"`).
   * Enter a **Description**.
   * Set **Publisher** to `"Koi"`.
   * Leave other fields at defaults or fill in as appropriate.
   * Click **Next**.
3. **Configure Pre-Install and Post-Install Scripts**

In the **Pre-install script** field, paste the following script. Replace the placeholder values with your actual values from the Koi dashboard:

```bash
#!/bin/bash
sudo defaults write koi.security.mdm CUSTOMER_ID '<your_customer_id>'
sudo defaults write koi.security.mdm XT_ENV '<your_xt_env>'
exit 0
```

In the **Post-install script** field, paste the following script to remove the configuration values from the defaults domain after installation:

```bash
#!/bin/bash
sudo defaults delete koi.security.mdm CUSTOMER_ID
sudo defaults delete koi.security.mdm XT_ENV
exit 0
```

Click **Next**.

4. **Configure Requirements**
   * Set to **macOS Ventura 13.0**.
   * Click **Next**.
5. **Detection Rules**
   * Click **Next**.
6. **Assign to Groups**
   * On the **Assignments** tab, under **Required**, add the device or user groups that should receive the Koi agent.
   * Click **Next**.
7. **Review and Create**
   * Review all settings.
   * Click **Create** to deploy the package.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/mdm/intune-guide.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
