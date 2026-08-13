<!-- KOI source: https://docs.koi.ai/integration-guides/edr/sentinelone-guide.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/edr/sentinelone-guide.md).

# SentinelOne Guide

This document provides step-by-step instructions on integrating **Koi** into your environment with SentinelOne.

### Prerequisites

1. SentinelOne Singularity Complete with the Remote Script Orchestration Add-on.
2. Access to the SentinelOne Management Console with the following permissions in RemoteOps:
   * View
   * View Output
   * Upload
   * Run scripts
     * Run Data Collection Script
     * Run Artifact Collection Script
     * Run Action Script
   * Schedule Actions
     * View Scheduled Tasks
     * Update Scheduled Tasks
     * Delete Scheduled Tasks
     * Create Scheduled Tasks
3. Your Koi script package from the deployment portal, uploaded as a custom script to RemoteOps in the SentinelOne Management Console. Create a different script for each OS:
   * **Bash** for Linux/macOS.
   * **PowerShell** for Windows.

### Integrations Steps

1. Choose the script & the scope

* In **Endpoints**, select one or more endpoints. Click **Actions** and select **Run Script**.
* You can also run a script on all endpoints in your scope with the script's defined OS by clicking **Play** on a script in the **Automation**->**RemoteOps** page.
* The Script Configuration wizard opens.

2. Set Up the Recurring Script Execution

* In **Input/Output**: choose None.
* In the **Task Parameters**:
  * Enter a task name in the **Task Description** field.
  * Choose a **Script Execution Timeout**.
  * **Execution Scheduling**: choose Re-occurring Daily.
* In the **Summary** window, review the script configuration and submit.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/edr/sentinelone-guide.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
