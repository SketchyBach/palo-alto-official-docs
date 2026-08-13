<!-- KOI source: https://docs.koi.ai/integration-guides/mdm/jamf-guide.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/mdm/jamf-guide.md).

# Jamf Guide

### **Introduction**

This document provides step-by-step instructions on integrating **Koi** into your environment with Jamf.

#### Configuration Guide

**Prerequisites**

* Access to your JAMF portal
* The configuration script provided by Koi.
* Internet access from managed devices.

***

> In case you're deploying the Package, refer to the integration steps below the Script Deployment.

***

#### Integration Steps (Script Deployment)

1. **Set Up the Policy Script**

* Navigate to **Settings > Search "Scripts" > Select "Scripts"** under **Computer Management**.
* Click on **"+New"** at the top right of the screen.
* Choose a **Display Name** and **Category** for the script.
  * Example: `"Configure Koi"`.
* Select the **Script** tab on the top navigation bar.
* Paste the **Koi script package** provided through your dashboard.
* Click **Save** at the bottom right.

2. **Set Up the Recurring Policy**

* Navigate to **Computers > Policies** under **Content Management**.
* Click on **"+New"** at the top right of the screen.
* Choose a **Display Name** for the policy.
  * Example: `"Configure Koi"`.
* Under **Trigger**, select **Recurring Check-in**.
* Under **Execution Frequency**, set it to **Ongoing**.

3. **Add the Script to the Policy**

* Navigate to **Scripts** on the left pane.
* Click on **Configure** and add the script created in Step 1.

4. **Configure the Scope**

* Navigate to the **Scope** tab at the top.
* Configure the target machines or groups to apply the policy to.
* Click **Save** at the bottom right.

***

#### Integration Steps (Package Deployment)

1. **Create the Configuration Profile**

* Navigate to **Computers > Configuration Profiles**.
* Click on **"+New"** at the top right of the screen.
* Choose a **Name** for the profile.
  * Example: `"Koi Configuration"`.

2. **Add Custom Settings Payload**

* In the left pane, scroll down and click on **Application & Custom Settings**.
* Click **Upload** and then click on **Add**.
* Under **Preference Domain**, enter: `koi.security.mdm`
* Add the following properties:
  * **CUSTOMER\_ID**: Your customer ID from the Koi dashboard in place of `your_customer_id`.
  * **XT\_ENV**: Your environment value from the Koi dashboard in place of `your_xt_env`.
* PLIST content:

  ```xml
    <dict>
        <key>CUSTOMER_ID</key>
        <string>your_customer_id</string>
        <key>XT_ENV</key>
        <string>your_xt_env</string>
    </dict>
  ```
* (optional, the default is 1 hour) In order to set the Interval time, add this interval parameter to the plist (in seconds):<br>

  ```xml
  <key>INTERVAL</key>
  <integer>3600</integer>
  ```

3. **Configure the Scope**

* Navigate to the **Scope** tab at the top.
* Configure the target machines or groups to apply the profile to.
* Click **Save** at the bottom right.

{% hint style="warning" %}
The configuration profile must be set before the installation
{% endhint %}

4. **Upload the Package**

* Navigate to **Settings > Search "Packages" > Select "Packages"** under **Computer Management**.
* Click on **"+New"** at the top right of the screen.
* Choose a **Display Name** and **Category** for the package.
  * Example: `"Koi Installer"`.
* Click **Choose File** to upload the PKG file provided by Koi.
* Configure any additional settings as needed.
* Click **Save** at the bottom right.

5. **Set Up the Policy**

* Navigate to **Computers > Policies** under **Content Management**.
* Click on **"+New"** at the top right of the screen.
* Choose a **Display Name** for the policy.
  * Example: `"Install Koi"`.
* Under **Trigger**, select whatever suits you.
* Under **Execution Frequency**, set it to **Once per computer** or **Ongoing** based on your needs.

6. **Add the Package to the Policy**

* Navigate to **Packages** on the left pane.
* Click on **Configure** and add the package created in Step 1.
* Under **Action**, select **Install**.

7. **Configure the Scope**

* Navigate to the **Scope** tab at the top.
* Configure the target machines or groups to apply the policy to.
* **Important:** Ensure these are the same targets as the Configuration Profile from Step 3.
* Click **Save** at the bottom right.

***

### **Support and Troubleshooting**

If you encounter any issues during the integration process, please follow these steps:

1. **Check Logs:**
   * Review logs on your MDM or proxy to identify potential misconfigurations.
   * Confirm that the devices have internet access and the scripts are running on schedule.
2. **Check configuration/permissions:**
   * For MDM-related issues, ensure the correct permissions and profiles are applied to the relevant devices.
   * For proxy chaining issues, verify the chaining policy and the connectivity with the Koi proxy.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/mdm/jamf-guide.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
