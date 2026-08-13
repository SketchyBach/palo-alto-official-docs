<!-- KOI source: https://docs.koi.ai/guardrails/agent-credential-access-restriction.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guardrails/agent-credential-access-restriction.md).

# Agent Credential Access Restriction

Prevents AI coding agents from reading sensitive files that store credentials and secrets - such as SSH keys, cloud credentials, API tokens, and `.env` files - before the read occurs. This guardrail protects against secret exfiltration, one of the highest-severity risks when working with agents, where a compromised or manipulated agent attempts to access credential stores.

### Why It Matters

* Coding agents routinely traverse the filesystem and can read any file the developer has permission to access, including credential stores that should never leave the endpoint.
* Prompt injection, tool poisoning, or a malicious agent extensions can redirect an otherwise trusted agent into reading SSH keys, cloud credentials, or `.env` files and exfiltrating them via a subsequent tool call.
* Once credentials are read into the agent's context, they are effectively exposed -- they may be logged, sent to the model provider, or passed to downstream tools.
* Preventing the read at the hook layer is the only reliable way to keep secrets on the endpoint where they belong.

### How It Works

* Intercepts agent tool calls that read files or shell out to commands that could read files, before the action executes.
* Extracts the target file path from the hook event, expands `~` to the user's home directory, and matches it against a configurable glob-style blocklist.
* If the path matches a blocked pattern, the action is denied and both the developer and the agent receive a clear message explaining that the path is protected.
* If the enforcement script errors or is missing, the action is allowed through — guardrails never break developer workflows.
* All evaluation is local, with no API calls at enforcement time, ensuring consistent low latency.

<figure><img src="/files/yb9uPUajUMcN7XQroIvd" alt=""><figcaption></figcaption></figure>

### What It Covers

The default blocklist covers the credential categories agents are most likely to encounter:

* **Application secrets** — `.env` files, `credentials.json`, `secrets.json`, service account files, `wp-config.php`
* **SSH and GPG keys:** `~/.ssh/**`, `~/.gnupg/**`, `~/.git-credentials`, `~/.netrc`, `~/.authinfo`
* **Cloud credentials:** AWS, GCP, Azure, and GitHub CLI credential directories
* **Package manager tokens:** npm, PyPI, Cargo, Maven, Gradle, Composer, NuGet
* **Container and orchestration credentials:** Docker config, Kubernetes config
* **Infrastructure state:** Terraform state and variables, Vault tokens
* **Certificate and key files:** `.key`, `.pem`, `.p12`, `.pfx`
* **Database credentials:** `~/.pgpass`, `~/.my.cnf`
* **Shell history and config:** `.bash_history`, `.zsh_history`, `.gitconfig`
* **macOS Keychain and system secrets:** Keychain files, `/etc/shadow`, SSH host keys
* **Extended protections:** browser credential stores (Chrome, Firefox, Edge) and cryptocurrency wallets (MetaMask, Exodus, Phantom, Ethereum, Electrum), available as opt-in extensions

The blocklist is fully configurable - add custom paths specific to your environment or remove defaults that don't apply. Both macOS/Linux and Windows path equivalents are supported.

### Benefits

* **Pre-execution blocking** - credentials never enter the agent's context, eliminating downstream exposure risk.
* **Configurable blocklist** - tune the default patterns to match your organization's secret storage conventions.
* **Estimated impact check** - preview how many events from the last 30 days would have been blocked before enabling, so rollout is predictable.
* **Endpoint group scoping** - apply the guardrail to specific groups for phased rollouts or environment-specific policies.
* 💎 **Coming soon: Request approval flow** - developers can request an exception directly from the block message, routed through your existing approval workflow.

### Supported Agents

* **Claude Code** (v1.0 and later)
* **Cursor** (v1.7 and later)
* ​**Codex CLI** ​
* **GitHub Copilot CLI** ​
* **Gemini CLI**&#x20;

<figure><img src="/files/SXsOSARqRM8gQtnncH04" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guardrails/agent-credential-access-restriction.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
