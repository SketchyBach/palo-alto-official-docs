<!-- KOI source: https://docs.koi.ai/integration-guides/mdm/workspace-one-guide.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/mdm/workspace-one-guide.md).

# Workspace ONE Guide

This document provides step-by-step instructions on integrating **Koi** into your environment with Workspace ONE UEM.

## Configuration Guide

**Prerequisites**

* Access to your Workspace ONE UEM console.
* The configuration script provided by Koi.
* Internet access from managed devices.

**Integrations Steps**

1. In the Workspace ONE UEM console, navigate to **Resources > Scripts**.
2. Click on **"Add ∨"** at the top left of the screen. Choose **macOS** or **Windows**.

   ![](https://files.readme.io/b4b3613fee2f9ca6bf4f3e06d4f9b0f83d77695d2230ceed066aafa4bd89e5ea-90019-0612-101104-2.png)
3. Choose a **Name** and **Description** for the script.\
   Example: `"Configure Koi"`.
4. Click **Next**.
5. Set the **Language** to **Bash** for macOS or **PowerShell** for Windows.
6. Set the **Execution Context** to **System**.
7. Copy and paste the **Koi configuration script** from your dashboard into the **Code** window.
8. Click **Next**, then click **Save**, and then **Save** again.
9. In the **Scripts** list, check the new script you just created, and click **Assign**.
10. Click **New Assignment**.
11. Choose a name for the assignment.\
    Example: `"Koi MacOS Devices"` or `"Koi Windows Devices"`.
12. For **Select Smart Group**, click in the search box. From the list of Assignment Groups that appear, select the appropriate group.\
    You can create a group under **Groups & Settings > Groups > Assignment Groups**.
13. Click **Next**.
14. Click **Run Periodically** and set the desired cadence.
15. Click **Add**.
16. Click **Save & Publish** and then **Publish**.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/mdm/workspace-one-guide.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
