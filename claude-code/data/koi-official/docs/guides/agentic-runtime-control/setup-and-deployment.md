<!-- KOI source: https://docs.koi.ai/guides/agentic-runtime-control/setup-and-deployment.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guides/agentic-runtime-control/setup-and-deployment.md).

# Setup & Deployment

Runtime Protection - both **Agent Activity** and **Agent Enforcement Custom Policies and guardrails** - runs on a can be deployed through a single shared installation on the endpoint. Deployment is handled in coordination with your Koi customer team, who will work with you to install Runtime Protection across your fleet. Once Runtime Protection is in place, enabling or disabling individual policies is done from the Koi portal or via API, without re-deploying. See the [Agent Runtime Policies API reference](https://docs.koi.ai/api-reference/reference/agents-runtime-policies) for programmatic management.<br>

***

### Prerequisites

* **Cursor**: Version 1.7 or later
* **Claude Code**: Version 1.0 or later
* **Codex CLI**: Version 0.130 or later
* **GitHub Copilot CLI**: Version 1.0 or later
* **Gemini CLI**: Version 0.26.0 or later
* **Antigravity CLI:** Version 1.0.0 or later
* **MDM script package:** standard (non-Nuitka) deployment required
* **Agent Activity** must be enabled before Custom Policies can be deployed - Custom Policies use the same hooks infrastructure and event pipeline.

{% hint style="warning" %}
&#x20;**Claude Code:** managed settings must be delivered **file-based, not server-managed.**

If your organization uses Claude Code's server-managed settings (configured in the claude.ai admin console), they take precedence and file-based settings and Koi's hooks will never load. See [Claude Code managed settings precedence](#claude-code-managed-settings-precedence) below.
{% endhint %}

### Deployment Flow

Runtime Protection can be deployed automatically through the Koi MDM script package. When set up, no manual configuration is required on individual endpoints.

**When Agent Activity is enabled:**

* The MDM deploys the hooks configuration to each endpoint, registering Koi as a listener for the relevant agent lifecycle events.
* The MDM creates the hooks configuration file if none exists, or adds Koi's command to an existing configuration without overwriting custom hooks.
  * For **Claude Code**, Koi uses the `managed-settings.d/` drop-in directory (see Drop-in deployment for Claude Code) so existing `managed-settings.json` files are preserved.
  * For **Codex**, the MDM also writes a per-hook trust block to `config.toml` and enables the `features.hooks` flag.

**When a Custom Policy is created or enabled in the Koi portal or via API:**

* The MDM delivers the policy configuration to the endpoint and writes it to a local config file.
* The configuration is refreshed on every MDM run cycle. Policy changes propagate without restarting agents.

### Supported Paths

Hooks are deployed differently per agent. Cursor, Claude Code, and Gemini CLI use **enterprise-wide configuration paths** that apply to every user on the endpoint. Codex, Copilot and Antigravity use **per-user paths** under each developer's home directory, because their CLIs don't currently support an enterprise hook configuration.

#### Cursor *(enterprise path)*

* **macOS**: `/Library/Application Support/Cursor/hooks.json`
* **Linux**: `/etc/cursor/hooks.json`
* **Windows**: `C:\ProgramData\Cursor\hooks.json`

#### Claude Code *(enterprise path, drop-in)*

Deployed as `koi-security.json` inside the `managed-settings.d/` drop-in directory:

* **macOS**: `/Library/Application Support/ClaudeCode/managed-settings.d/koi-security.json`
* **Linux**: `/etc/claude-code/managed-settings.d/koi-security.json`
* **Windows**: `C:\Program Files\ClaudeCode\managed-settings.d\koi-security.json`

See Drop-in deployment for Claude Code below for details on how this interacts with an existing `managed-settings.json`.

#### Gemini CLI *(enterprise path)*

* **macOS**: `/Library/Application Support/GeminiCli/settings.json`
* **Linux**: `/etc/gemini-cli/settings.json`
* **Windows**: `C:\ProgramData\gemini-cli\settings.json`

#### Codex *(per-user path)*

Deployed to each user's home directory:

* **macOS / Linux**: `~/.codex/hooks.json` and `~/.codex/config.toml`
* **Windows**: `%USERPROFILE%\.codex\hooks.json` and `%USERPROFILE%\.codex\config.toml`

The `config.toml` file holds Codex's per-hook trust hash and the `features.hooks` toggle. Both are written by the MDM and refreshed on every run cycle.

#### GitHub Copilot CLI *(per-user path)*

Deployed to each user's home directory:

* **macOS / Linux**: `~/.copilot/hooks/koi-security.json`
* **Windows**: `%USERPROFILE%\.copilot\hooks\koi-security.json`

> **Note**: Agent platform restart is required. After initial hook deployment, the application must be restarted once for hooks to take effect.

#### **Antigravity (per-user path)**

Deployed to each user's home directory:

* **macOS / Linux:** `~/.gemini/config/hooks.json`
* **Windows:** `%USERPROFILE%\.gemini\config\hooks.json`

Antigravity reuses the `~/.gemini/` directory used by Gemini CLI but writes to a separate [`config/hooks.json`](https://github.com/placeholder-security/Koi/blob/claude/magical-meitner-58wp2d/config/hooks.json) file, so the two agents' hook configurations do not collide.

### Drop-in Deployment for Claude Code

Claude Code supports a `managed-settings.d/` drop-in directory alongside the main `managed-settings.json` file. Multiple JSON files can live in `managed-settings.d/`, and Claude Code deep-merges them on top of the base `managed-settings.json` - sorted alphabetically by filename, with later filenames overriding earlier ones. This follows the same convention as `systemd` and `sudoers`, letting different teams maintain independent policy fragments without coordinating edits to a single admin-owned file. For full details, see Anthropic's [Claude Code settings documentation](https://code.claude.com/docs/en/settings).

**How Koi uses it.** Koi deploys its hooks to `managed-settings.d/koi-security.json` instead of writing into the main `managed-settings.json`. This means:

* Your existing `managed-settings.json` is left untouched - Koi never edits or overwrites admin-authored settings.
* Other teams' policy fragments under `managed-settings.d/` continue to coexist with Koi's file.
* Removing Koi from an endpoint cleanly deletes a single file (`koi-security.json`) without risk to the base configuration.

**Legacy installations.** Earlier versions of Koi wrote hooks directly into `managed-settings.json`. The MDM script automatically detects and cleans up these legacy entries on the next run, so customers upgrading don't end up with duplicated hooks across the base file and the drop-in.

**Other agents.** The drop-in pattern is currently a Claude Code-only capability. Cursor, Gemini CLI, Codex, and GitHub Copilot CLI use the single-file paths listed above.

### Claude Code managed settings precedence

Claude Code has four configuration scopes, from strongest to weakest: \
**Managed** (where Koi deploys) → **User** → **Project** → **Local**. \
When a setting appears in more than one scope, the strongest scope wins. This is what guarantees that once Koi deploys a setting, lower scopes cannot override it.

Within the Managed scope, there are three delivery methods:

<table><thead><tr><th width="164.62890625">Method</th><th width="311.34375">How it's delivered</th><th>Interaction with Koi</th></tr></thead><tbody><tr><td>Server-managed settings (Enterprise)</td><td>Configured in the claude.ai admin console; fetched by each client at login and hourly</td><td><strong>Overrides Koi.</strong> <br>If active, file-based settings are ignored and Koi's hooks never load.</td></tr><tr><td>OS-level settings</td><td>Native OS management (macOS Managed Preferences, Windows Registry) via MDM</td><td>Compatible</td></tr><tr><td>File-based settings</td><td><code>managed-settings.json</code> + the <code>managed-settings.d/</code> drop-in directory, placed on the endpoint via MDM</td><td><strong>This is how Koi delivers config.</strong></td></tr></tbody></table>

**The critical constraint:** server-managed and file-based settings do not merge. If server-managed settings deliver any keys at all, Claude Code uses them and ignores the file-based settings completely. There is no partial merge across these two methods. An organization on server-managed settings will see Koi's koi-security.json present on disk while none of its hooks fire.\
\
**What to do:** To run Koi enforcement on Claude Code, deliver managed settings via the file-based path (or OS-level MDM). Do not configure Claude Code settings in the claude.ai admin console for machines that should be governed by Koi.

### Single-File Hook Merging (Cursor, Antigravity & other agents)

Since Cursor doesn't have a drop-in directory like Claude Code's `managed-settings.d/`, hooks live in a single file and have to be merged in. Here's the pattern Koi uses:

1. **Tag the hooks with a marker:** Every hook command Koi injects contains a unique marker string. This is how Koi tells its own hooks apart from the user's hooks on future runs.
2. **Read the existing file:** Koi parses `hooks.json` (using a JSONC parser to handle comments). If the file doesn't exist yet, it starts with an empty config.
3. **For each event type** (e.g. `beforeShellExecution`, `beforeMCPExecution`, `afterFileEdit`):
   1. Koi filters out any entries that contain its marker - its old hooks from a previous run.
   2. Keeps everything else - those are the user's hooks
   3. Appends its new hooks at the end.

**4. Write back:** The file is overwritten with the merged result.

**Key properties:**

* User hooks always come first and are never modified.
* Idempotent- Running it twice produces the same result (old tagged hooks get replaced, not duplicated).
* Rollback is easy- Koi reads the file, strips entries containing its marker, and writes back.

**Antigravity uses a simpler variant of the same pattern.** Antigravity's `hooks.json` is keyed by hook name at the top level, so Koi reserves a single top-level key for its entire hook block instead of tagging individual hook entries with a marker. Deploy sets that key; rollback removes it. User-authored hooks under other top-level keys are never read, modified, or moved by Koi.

### Verify Installation

#### Cursor

1. Open Cursor → Settings → Hooks
2. Confirm hooks appear under "Configured Hooks"
3. Run any agent action (e.g., ask Cursor to read a file)
4. Check Koi portal → Runtime/Agents page for the event

<figure><img src="/files/kF7BFCClQ1N5nChJG5kQ" alt=""><figcaption></figcaption></figure>

#### Claude Code

1. Open `managed-settings.d/koi-security.json` (see paths above per OS in "Supported Paths")
2. Confirm Koi hook entries are present under `"hooks"`
3. Run any agent action (e.g., ask Claude Code to read a file)
4. Check Koi portal → Runtime/Agents page for the event

<figure><img src="/files/mcFiwXP2V1kb2svi4ffh" alt=""><figcaption></figcaption></figure>

If Koi hook entries are present in koi-security.json but events are not appearing in the Koi portal, the most common cause is server-managed settings taking precedence. To check which managed source is active:

* In Claude Code, run `/status` - it reports which managed settings source is in effect (server-managed vs. endpoint/file-based).
* You can also run `/doctor`, which surfaces active settings sources and configuration errors.
* As a secondary signal, the presence of a populated `~/.claude/remote-settings.json` indicates the organization is receiving server-managed settings (this file is a cache and is absent when none are configured).

If /status shows a server-managed source, that is overriding Koi's file-based settings - switch Claude Code management to the file-based / MDM path (see [Claude Code managed settings precedence](#claude-code-managed-settings-precedence)).

#### Codex

1. Open `~/.codex/hooks.json` and confirm Koi hook entries are present
2. Open `~/.codex/config.toml` and confirm the Koi-managed `[hooks.state."..."]` trust block exists and `features.hooks` is enabled
3. Run any agent action in Codex
4. Check Koi portal → Runtime/Agents page for the event

#### GitHub Copilot CLI

1. Open `~/.copilot/hooks/koi-security.json` and confirm Koi hook entries are present
2. Run any agent action in Copilot
3. Check Koi portal → Runtime/Agents page for the event

#### Gemini CLI

1. Open the `settings.json` file at the enterprise path above
2. Confirm Koi hook entries are present under `"hooks"`
3. Run any agent action in Gemini CLI
4. Check Koi portal → Runtime/Agents page for the event

To verify Custom Policies specifically, create a test policy with a single rule, run an impact check, and trigger a matching action - the block message should appear in the IDE/CLI (where supported; on Codex and Gemini CLI, only Block mode is supported) and the decision should appear in Agent Activity.

#### Antigravity

1. Open `~/.gemini/config/hooks.json` and confirm Koi hook entries are present.
2. Run any agent action in Antigravity (e.g., ask it to read a file).
3. Check Koi portal → Runtime/Agents page for the event.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guides/agentic-runtime-control/setup-and-deployment.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
