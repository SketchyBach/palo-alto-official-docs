<!-- KOI source: https://docs.koi.ai/integration-guides/code-packages/registry-approach/deploying-registry-configuration/wsl-setup.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/code-packages/registry-approach/deploying-registry-configuration/wsl-setup.md).

# WSL Setup

### Introduction

Koi supports prevention of code packages (from NPM and PyPi) in WSL environments.

WSL runs as an isolated Linux environment on Windows, with its own file system, shell, and tool configurations. Because of this isolation, pip and npm inside WSL maintain their own settings independently from the host machine - registry configuration applied on the Windows side does not carry over into WSL automatically.

To enforce prevention inside WSL, pip and npm must be explicitly configured to route through the Koi registry **within the WSL environment itself**.

***

### Configuration Steps

The following commands can be run directly from the **host machine** (PowerShell or Command Prompt) - there is no need to open a WSL session manually.

Replace `<subdomain>` with your Koi customer subdomain in each command.

#### 1. Configure pip inside WSL

Run the following command from the host to point pip's global index to the Koi PyPI registry inside WSL:

```bash
wsl bash -lc "pip config set --global global.index-url https://koi-pypi-<subdomain>.gateway.koi.security/simple"
```

This writes to the global pip configuration inside the WSL environment, so all Python package installs via pip will be routed through Koi.

#### 2. Configure npm inside WSL

Run the following command from the host to set the Koi npm registry in the WSL user's `.npmrc` file:

```bash
wsl bash -lc "grep -q '^registry=' ~/.npmrc 2>/dev/null && sed -i 's|^registry=.*|registry=https://koi-npmjs-<subdomain>.gateway.koi.security|' ~/.npmrc || echo 'registry=https://koi-npmjs-<subdomain>.gateway.koi.security' >> ~/.npmrc"
```

This updates the registry entry if one already exists, or appends it if `.npmrc` doesn't have a registry set yet.

***

### Notes

* These commands target the **default WSL distribution**. If multiple WSL distributions are in use, the commands may need to be run once per distribution (e.g., `wsl -d Ubuntu bash -lc "..."`).
* These commands configure the **default pip and npm installations** inside WSL. Any other Node.js or Python installation, whether managed by a version manager such as `nvm` or `pyenv`, or installed through other means, maintains its own separate configuration and will need to be targeted independently.
* To verify the configuration is applied correctly inside WSL, run:

```shellscript
wsl bash -lc "cat ~/.npmrc"
```

```bash
wsl bash -lc "pip config list"
```

***

### Support and Troubleshooting

If prevention is not being enforced inside WSL after completing the steps above:

1. **Verify the configuration was applied:** Run the verification commands above and confirm the Koi registry URLs are present.
2. **Check for conflicting configuration:** Project-level `.npmrc` files or environment variables like `PIP_INDEX_URL` can override the global settings. Check for these and remove or update them if found.
3. **Confirm the correct WSL distribution was targeted:** If multiple distributions are installed, ensure the commands were run against the one your developers are using. Use `wsl --list` to see available distributions.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/code-packages/registry-approach/deploying-registry-configuration/wsl-setup.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
