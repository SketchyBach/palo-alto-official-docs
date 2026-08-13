<!-- KOI source: https://docs.koi.ai/integration-guides/network/establishing-trust/marketplace-domains.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/network/establishing-trust/marketplace-domains.md).

# Marketplace domains

### Firefox

```
addons.mozilla.org
*.addons.mozilla.org
aus5.mozilla.org
```

### Chromium

```
chromewebstore.google.com
clients2.googleusercontent.com
clients2.google.com
edge.microsoft.com
clients2.googleusercontent.com
chrome.google.com
update.googleapis.com
storage.googleapis.com
```

### Office&#x20;

```
addinsinstallation.store.office.com
addinslicensing.store.office.com
api.addins.omex.office.net |
```

### VSCode

```
marketplace.visualstudio.com
marketplace.cursorapi.com
*.gallerycdn.vsassets.io
*.gallery.vsassets.io
main.vscode-cdn.net
*.vscode-unpkg.net
cursor-cdn.com
marketplace.windsurf.com
openvsxorg.blob.core.windows.net
open-vsx.org
az764295.vo.msecnd.net
```

### JetBrains

```
downloads.marketplace.jetbrains.com
plugins.jetbrains.com
```

### Huggingface

```
huggingface.co
cdn-lfs.huggingface.co
router.huggingface.co
```

### Npm

```
registry.npmjs.org
```

### PyPI

```
pypi.org
files.pythonhosted.org
```

### Github MCP Registry

```
api.mcp.github.com
```


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/network/establishing-trust/marketplace-domains.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
