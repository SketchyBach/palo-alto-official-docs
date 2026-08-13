<!-- KOI source: https://docs.koi.ai/integration-guides/mdm/fleetdm-guide.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/mdm/fleetdm-guide.md).

# FleetDM Guide

**Prerequisites**

* Access to your FleetDM dashboard.
* The Koi `.pkg` file (macOS) and/or `Koi.msi` file (Windows) provided through your Koi dashboard.
* Your **CUSTOMER\_ID**, **CUSTOMER\_SLUG**, and **XT\_ENV** values from the Koi dashboard.
* `fleetd` deployed on target hosts with the `--enable-scripts` flag (enabled by default if using MDM features).
* Internet access from managed devices.

***

### **macOS — Package (.pkg) Deployment**

**1. Upload the Koi Package**

* Navigate to **Software** and select your target team.
* Click **Add software** in the top right corner.
* Select the **Custom package** tab.
* Upload the `koi-security-mdm.pkg` file provided by Koi.
* **Important:** Don't mark **Self-service** option.

**2. Configure the Install Script**

* Click **Advanced options** before saving.
* In the **Install script** field, replace the default script with the following:

  ```bash
  #!/bin/bash
  sudo defaults write koi.security.mdm CUSTOMER_ID '<your_customer_id>' && sudo defaults write koi.security.mdm XT_ENV '<your_xt_env>'
  sudo installer -pkg "$INSTALLER_PATH" -target /
  ```
* Replace `<your_customer_id>` and `<your_xt_env>` with the values from your Koi dashboard.
* Check **Automatic install** to automatically deploy Koi to all hosts in the team.
* Click **Add software**.

**3. Install the Package on Hosts**

**Manual install (per-host):**

* Navigate to **Hosts** and select the target host.
* Go to **Software > Library**.
* Find the Koi package and click **Install**.

**Automatic install:**

* If you checked **Automatic install** in Step 2, Fleet will automatically create a policy and install the package on hosts where Koi is not detected.

***

### **Windows — MSI Deployment**

**1. Upload the Koi MSI Package**

* Navigate to **Software** and select your target team.
* Click **Add software** in the top right corner.
* Select the **Custom package** tab.
* Upload the `Koi.msi` file provided by Koi.
* **Important:** Don't mark **Self-service** option.

**2. Configure the Install Script**

* Click **Advanced options** before saving.
* In the **Install script** field, replace the default script with the following:

  ```powershell
  $installer = $env:INSTALLER_PATH
  msiexec /i "$installer" /qn CUSTOMERID="<YOUR_CUSTOMER_ID>" CUSTOMERSLUG="<YOUR_CUSTOMER_SLUG>" INTERVAL=60
  Exit $LASTEXITCODE
  ```
* Replace `<YOUR_CUSTOMER_ID>` and `<YOUR_CUSTOMER_SLUG>` with the values from your Koi dashboard.
* `INTERVAL` is the execution frequency in minutes (default: 60).
* (Optional) Check **Automatic install** to automatically deploy Koi to all Windows hosts in the team.
* Click **Add software**.

**3. Install the MSI on Hosts**

**Manual install (per-host):**

* Navigate to **Hosts** and select the target Windows host.
* Go to **Software > Library**.
* Find the Koi package and click **Install**.

**Automatic install:**

* If you checked **Automatic install** in Step 2, Fleet will automatically create a policy and install the MSI on hosts where Koi is not detected.

***

### **Verifying the Deployment**

**macOS:**

* SSH into the host or use a Fleet live query to confirm the daemon is running:

  ```
  sudo launchctl list | grep koi.security
  ```
* Check logs at `/var/log/koi.security.mdm.out`.

**Windows:**

* Verify the service is running:

  ```
  sc.exe query KoiService
  ```

**Koi Dashboard:**

* Navigate to your Koi dashboard to confirm endpoints are registering and reporting.

***

#### **Support and Troubleshooting**

If you encounter any issues during the integration process, please follow these steps:

1. **Check Logs:**
   * On macOS, review logs at `/var/log/koi.security.mdm.out` and `/var/log/koi.security.mdm.err`.
   * On Windows, review `C:\ProgramData\Koi\KoiService.log`.
   * In Fleet, check the host's **Activity** tab for install status and errors.
2. **Verify Configuration:**
   * On macOS, confirm the `CUSTOMER_ID` and `XT_ENV` values were written correctly by running: `defaults read koi.security.mdm`.
   * On Windows, confirm the MSI command-line arguments include the correct `CUSTOMERID` and `CUSTOMERSLUG` values.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/mdm/fleetdm-guide.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
