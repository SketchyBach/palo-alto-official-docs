<!-- KOI source: https://docs.koi.ai/integration-guides/edr/crowdstrike-rtr-guide/add-a-crowdstrike-exclusion-windows.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/edr/crowdstrike-rtr-guide/add-a-crowdstrike-exclusion-windows.md).

# Add a CrowdStrike Exclusion (Windows)

CrowdStrike may trigger a false positive alert on the Koi deployment script due to a basic PowerShell command (`Set-Location C:\`) used during execution. This section explains how to add an IOA exclusion to prevent these alerts.

**Add the Exclusion**

> 📘 The exclusion will prevent CrowdStrike from alerting on this specific command pattern while maintaining security monitoring for other activities.

1. Allow the Koi script to run once and trigger the CrowdStrike detection
2. Navigate to **Activity > Detections**
3. Locate the detection for the Koi script
4. Click on the detection to view details
5. Click **Actions > Create IOA exclusion**
6. CrowdStrike will automatically populate the exclusion with the correct parameters
   1. Make sure that it looks something like that:

      ```
      ".*\\Windows\\System32\\WindowsPowerShell\\v1\.0\\powershell\.exe"\s+-Version\s+5\.1\s+-s\s+-NoLogo\s+-NoProfile\s+-EncodedCommand\s+UwBlAHQALQBMAG8AYwBhAHQAaQBvAG4AIAAnAEMAOgBcACcA
      ```

      `UwBlAHQALQBMAG8AYwBhAHQAaQBvAG4AIAAnAEMAOgBcACcA` is a `base64 & utf16-LE` of`Set-Location C:\`.
7. Click **Next** > **Create exclusion**


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/edr/crowdstrike-rtr-guide/add-a-crowdstrike-exclusion-windows.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
