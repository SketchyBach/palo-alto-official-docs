<!-- KOI source: https://docs.koi.ai/integration-guides/endpoint-integration/capabilities-per-os.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/endpoint-integration/capabilities-per-os.md).

# Capabilities per OS

| Capabilities                 | Windows | Mac OS | Linux         |
| ---------------------------- | ------- | ------ | ------------- |
| **IDE extensions**           |         |        |               |
| VS Code Extensions           | ✅       | ✅      | ✅             |
| Cursor Extensions            | ✅       | ✅      | ✅             |
| Windsurf Extensions          | ✅       | ✅      | ✅             |
| Kiro Extensions              | ✅       | ✅      | ✅             |
| JetBrains Plugins            | ✅       | ✅      | ❌ coming soon |
| **Browsers Extensions**      |         |        |               |
| Chrome Extensions            | ✅       | ✅      | ✅             |
| Edge Extensions              | ✅       | ✅      | ✅             |
| Firefox Extensions           | ✅       | ✅      | ✅             |
| Brave Extensions             | ✅       | ✅      | ✅             |
| Arc Extensions               | ✅       | ✅      | ✅             |
| Opera Extensions             | ✅       | ✅      | ✅             |
| Talon Extensions             | ✅       | ✅      | ✅             |
| **Official applications**    |         |        |               |
| Outlook Extensions           | ✅       | ✅      | ❌             |
| Word Extensions              | ✅       | ✅      | ❌             |
| Excel Extensions             | ✅       | ✅      | ❌             |
| PowerPoint Extensions        | ✅       | ✅      | ❌             |
| **Code packages**            |         |        |               |
| NPM Packages                 | ✅       | ✅      | ✅             |
| PyPI Packages                | ✅       | ✅      | ✅             |
| **OS Packages**              |         |        |               |
| Homebrew packages            | ❌       | ✅      | ✅             |
| Chocolaty packages           | ✅       | ❌      | ❌             |
| **Text Editors**             |         |        |               |
| Notepad++ Plugins            | ✅       | ❌      | ❌             |
| **AI/ML Platforms**          |         |        |               |
| HuggingFace Model            | ✅       | ✅      | ✅             |
| Claude Desktop (MCP)         | ✅       | ✅      | ❌             |
| MCP Server Discovery         | ✅       | ✅      | ✅             |
| **Network Configuration**    |         |        |               |
| PAC configuration            | ✅       | ✅      | ✅             |
| Hosts File Management        | ✅       | ✅      | ✅             |
| Proxy Settings (JetBrains)   | ✅       | ✅      | ❌ coming soon |
| **Application Inventory**    |         |        |               |
| Discover applications        | ✅       | ✅      | ❌             |
| **Binaries Inventory**       |         |        |               |
| Discover and Govern binaries | ❌       | ✅      | ❌             |
| **System Features**          |         |        |               |
| PAC File configuration       | ✅       | ✅      | ✅             |
| Desktop Notifications        | ✅       | ✅      | ❌             |
| Set a home directory         | ❌       | ❌      | ✅             |
| **Discovery Features**       |         |        |               |
| Quick Search (File System)   | ✅       | ✅      | ✅             |
| User-based Discovery         | ✅       | ✅      | ✅             |
| Slack User ID Discovery      | ✅       | ✅      | ❌             |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/endpoint-integration/capabilities-per-os.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
