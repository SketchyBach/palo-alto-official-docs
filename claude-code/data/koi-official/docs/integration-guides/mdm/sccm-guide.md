<!-- KOI source: https://docs.koi.ai/integration-guides/mdm/sccm-guide.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/mdm/sccm-guide.md).

# SCCM Guide

This document provides step-by-step instructions on integrating **Koi** into your environment with SCCM.

## Configuration Guide

**Prerequisites**

* Access to your SCCM
* The configuration script provided by Koi.
* Internet access from managed devices.

**Integrations Steps**

1. **Create a Configuration Item (CI)**:
   * Navigate to **Assets and Compliance > Compliance Settings > Configuration Items**.
   * Click **Create Configuration Item** and give it a descriptive name (e.g., “Koi Configuration Script”).
   * Choose **Windows Desktops and Servers (Custom)** for the configuration item type.
   * In the **Settings** tab, add a new setting:
   * Choose **Script** as the setting type.
   * Select **PowerShell** as the script language.
   * Paste Koi PowerShell script in the script window.
2. **Set Compliance with Minimal Focus**:
   * When defining the compliance rules, configure it so that the script always passes as “compliant” if it runs successfully.
3. **Create a Configuration Baseline**:
   * Go to **Assets and Compliance > Compliance Settings > Configuration Baselines**.
   * Click **Create Configuration Baseline** and name it (e.g., “Recurring Koi Configuration”).
   * Add the **Configuration Item** (CI) you created in the previous step.
4. **Deploy the Configuration Baseline**:

   * Right-click the baseline and choose **Deploy**.
   * Select the target device collection where the script should be run.
   * Under the **Schedule** tab, click on **New Schedule**
     * In the **Custom Schedule** window, select **Simple Recurrence**.
     * Choose **Hourly** from the dropdown menu.
     * Set the recurrence to 1 **hours** (enter “1” in the hours field).
     * Click OK to save the schedule
     * The frequency will affect the management dashboard's remediation window and update period.
   * Enable the **Remediation** option so the script runs every time the baseline is evaluated, effectively making it your periodic task.

   ### **Support and Troubleshooting**

If you encounter any issues during the integration process, please follow these steps:

1. **Check Logs:**
   * Review logs on your SCCM to identify potential misconfigurations.
   * Confirm that the devices have internet access and the scripts are running on schedule.
2. **Contact Support:**
   * For MDM-related issues, ensure the correct permissions and profiles are applied to the relevant devices.
   * For proxy chaining issues, verify the chaining policy and the connectivity with the Koi proxy.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/mdm/sccm-guide.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
