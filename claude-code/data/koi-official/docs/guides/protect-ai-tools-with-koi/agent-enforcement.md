<!-- KOI source: https://docs.koi.ai/guides/protect-ai-tools-with-koi/agent-enforcement.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guides/protect-ai-tools-with-koi/agent-enforcement.md).

# Agent Enforcement (Preview)

Koi Agent Enforcement extends Agent Activity from visibility into active protection. It provides built-in guardrails that block dangerous agent actions, such as accessing credentials or executing destructive commands, before they execute, with minimal disruption to the developer workflows.

Agent Enforcement uses the same hooks infrastructure as Agent Activity, adding a lightweight enforcement layer that evaluates each agent action against configurable policies in real time. When a blocked action is detected, the agent is stopped immediately and both the developer and the agent receive clear feedback explaining what was blocked and why.

💎 **Coming soon:** As the product evolves, Agent Enforcement will expand beyond the initial guardrails to support custom runtime policies, and additional risk categories.

***

### Key Capabilities

* **Two New Gaurdrails:**
  * **Credential access restriction:** Prevent agents from reading sensitive files storing credentials and secrets, such as SSH keys, AWS credentials, and `.env` files.
  * **Destructive command restriction:** Prevent agents from executing destructive commands such as recursive file deletion, database drops, infrastructure teardown, and force-pushes.
* **Configurable blocklists:** Edit the default path and command blocklists to match your organization's environment. Add custom entries or remove defaults that don't apply.
* **Estimated impact check:** Before enabling a guardrail, preview how many agent events from the last 30 days would have been blocked - helping you assess impact before enforcement goes live.
* **Endpoint group scoping:** Apply guardrails to specific endpoint groups rather than your entire fleet, enabling phased rollouts and environment-specific policies.
* **Fail-open design:** If the enforcement script encounters an error or is missing, the action is allowed through. Guardrails never break developer workflows.
* **Request approval flow:** When an action is blocked, developers can request an exception directly from the block message, routing through your existing approval workflow.

***

### How It Works

Agent Enforcement builds on the hooks infrastructure already deployed for Agent Activity. Instead of only logging agent events, the enforcement hook evaluates each action against configured policies and returns an allow or block decision before the action executes.

```
Developer prompt → [Hook fires] → Enforcement script evaluates → Allow / Block → Agent continues or stops
```

**The flow:**

1. Koi deploys an enforcement script alongside the existing hooks configuration via the MDM script package
2. The MDM writes a local policy configuration file containing the enabled guardrails and their blocklists, refreshed on every MDM run cycle
3. When the agent attempts an action, the hook pipes event data to the enforcement script
4. The script evaluates the action against active policies - matching file paths or parsing commands against the configured blocklists
5. The script returns **allow** or **block** with structured feedback
6. Blocked actions surface a message to both the developer and the agent; allowed actions proceed normally and are logged

**All enforcement is local.** The script reads policies from a local config file. No API calls are made at enforcement time, ensuring consistent low latency.

Any change in runtime policies will be enforced in the next MDM run cycle, and will take place even in ongoing user session.&#x20;

***

### Guardrails

#### Agent Credential Access Restriction

Prevents agents from reading sensitive files that store credentials and secrets. This guardrail protects against secret exfiltration - one of the highest-severity risks with working with agents, where a compromised or manipulated agent accesses SSH keys, cloud credentials, API tokens, or environment variables.

**What it intercepts:**

* **Claude Code:** `PreToolUse` on `Read`, `Glob`, `Grep`, `Bash`
* **Cursor:** `preToolUse` on `Read`, `Grep`, `file_search`, `Shell` + `beforeReadFile`, `beforeShellExecution`

**How matching works:**

1. File paths are extracted from event data (directly from tool arguments for file tools)
2. The `~` prefix is expanded to the user's home directory
3. Paths are matched against the blocklist using glob-style patterns

**Default blocklist:**

* **Application secrets:** `**/.env`, `**/.env.*`, `**/credentials.json`, `**/secrets.json`, `**/service-account*.json`, `**/wp-config.php`
* **SSH and GPG keys:** `~/.ssh/**`, `~/.gnupg/**`, `~/.git-credentials`, `~/.netrc`, `~/.authinfo`
* **Cloud credentials:** `~/.aws/**`, `~/.config/gcloud/**`, `~/.azure/**`, `~/.config/gh/**`
* **Package manager tokens:** `~/.npmrc`, `~/.npm/**`, `~/.pypirc`, `~/.gem/credentials`, `~/.cargo/credentials`, `~/.cargo/credentials.toml`, `~/.pip/pip.conf`, `~/.nuget/**`, `~/.m2/settings.xml`, `~/.gradle/gradle.properties`, `~/.composer/auth.json`
* **Container and orchestration credentials:** `~/.docker/config.json`, `~/.docker/**`, `~/.kube/config`
* **Infrastructure state:** `**/*.tfstate`, `**/*.tfstate.backup`, `**/*.tfvars`, `~/.terraform.d/credentials.tfrc.json`, `~/.vault-token`
* **Certificate and key files:** `**/*.key`, `**/*.pem`, `**/*.p12`, `**/*.pfx`
* **Database credentials:** `~/.pgpass`, `~/.my.cnf`
* **Shell history and config:** `~/.bash_history`, `~/.zsh_history`, `~/.gitconfig`
* **macOS Keychain:** `~/Library/Keychains/**`
* **Application frameworks:** `**/config/master.key`, `**/config/credentials.yml`, `**/.github/workflows/*.yml`
* **System secrets:** `/etc/shadow`, `/etc/ssh/ssh_host_*_key`, `/proc/*/environ`

An additional 14 extended protection paths are available covering browser credential stores (Chrome, Firefox, Edge) and cryptocurrency wallets (MetaMask, Exodus, Phantom, Ethereum, Electrum).

> **Note:** Both macOS/Linux and Windows paths are supported. The blocklist includes platform-appropriate path equivalents for Windows endpoints.

#### Agent Destructive Command Restriction

Prevents agents from executing commands that cause irreversible damage — file deletion, disk operations, database destruction, infrastructure teardown, and history-rewriting git operations. This guardrail protects against environment destruction, whether caused by agent hallucination, prompt injection, or tool poisoning.

**What it intercepts:**

* **Claude Code:** `PreToolUse` on `Bash`
* **Cursor:** `preToolUse` on `Shell` + `beforeShellExecution`

**How matching works:**

1. The command string is extracted from the hook event
2. Commands are tokenized — split by pipes, `;`, `&&`, `||`
3. Evasion prefixes are stripped: `\`, `command`, `env`, `/usr/bin/`, `bash -c`
4. The base command and its arguments are matched against the blocklist
5. SQL keywords use case-insensitive substring matching

> **Note:** Commands are matched with their specific destructive arguments. For example, `rm` is only blocked when used with `-rf` or `-r` flags — not when used for single-file deletion. This ensures guardrails target genuinely destructive patterns without interfering with normal development.

**Default blocklist:**&#x20;

* **File and directory destruction:** `rm -rf` / `rm -r`, `shred`, `find -delete` / `find -exec rm`, `truncate`
* **Database destruction:** `DROP DATABASE` / `DROP TABLE`, `TRUNCATE TABLE`, `DELETE FROM` (without WHERE)
* **Infrastructure teardown:** `terraform destroy`, `kubectl delete namespace` / `kubectl delete`, `pulumi destroy`, `helm uninstall`
* **Cloud resource destruction:** `aws ec2 terminate-instances`, `aws s3 rm --recursive`, `gcloud ... delete`, `az ... delete`
* **Disk and partition operations:** `dd if=/dev/zero` / `dd if=/dev/urandom`, `mkfs`, `wipefs`, `fdisk` / `parted`
* **Git history destruction:** `git push --force` / `git push -f`, `git reset --hard`, `git clean -fd`, `git branch -D`
* **System operations:** `shutdown` / `reboot` / `halt`, `kill -9` / `killall` / `pkill`
* **Container destruction:** `docker system prune -af`, `docker rm -f` / `docker rmi -f`, `docker-compose down -v`
* **Data exfiltration:** `curl -d @`, `wget --post-file`
* **Supply chain risks:** `npm publish`, `pip upload`
* **Permission changes:** `chmod 777 -R` / `chmod -R 000`
* **Shell config injection:** `echo >>` targeting `~/.bashrc` / `~/.zshrc` / `~/.profile`

An additional 15 extended commands and 9 evasion-pattern detections are available for broader coverage.

***

### Estimated Impact Check

Before enabling a guardrail, you can preview its impact on your fleet. The estimated impact check queries all agent activity events from the last 30 days and shows how many would have been blocked by the current blocklist configuration.

**What it shows:**

* Total number of events that would have been blocked
* Number of affected endpoints
* Breakdown by matched path or command, with event counts and endpoint groups

**No matches state:** If no matching events are found, a confirmation message indicates that enabling the guardrail will not disrupt current workflows.

> **Note:** Impact check numbers are estimates. Because resolving relative file paths from historical event data is not always possible (for example, if an agent changed directories before accessing a file), the impact check may undercount some events. This limitation does not affect enforcement, which has access to the full runtime environment for accurate path resolution.

***

### Blocking Experience

When an action is blocked, two messages are delivered - one for the developer and one for the agent. This dual-message approach ensures the developer understands what happened while instructing the agent not to retry the blocked action.

**Developer-facing message (shown in the IDE):**

<figure><img src="/files/iBxxdggxPn2R5rWRo17m" alt=""><figcaption></figcaption></figure>

The developer sees the policy name and a link to request an exception. The specific pattern that triggered the block is intentionally omitted to prevent enumeration of protected paths or commands.

**Agent-facing message (sent to the LLM):**

The agent receives an explicit instruction not to retry or attempt variations, preventing retry loops. Context varies by guardrail type — for example, "This file path is protected" or "This command is restricted."

<figure><img src="/files/xjkhRLlUhHvW5CQPOyVJ" alt=""><figcaption></figcaption></figure>

#### Request Approval

The block message includes a link to a request approval form, pre-filled with the policy ID, endpoint details, and blocked action context. This uses the same approval mechanism as Koi's existing workflow - either the built-in Koi approval flow or your configured custom ticketing URL.\
For agent enforcemnt flows, the developer can request to exclude their endpoint from the gaurdrail, and provide justification for the security team to approve.

💎 **Coming soon:** Time-based exclusions for more granular exception handling, configurable request urls and agent-facing API.

***

### Configuring Guardrails

Both guardrails are configured from the Guardrails page in the Koi portal.

**For each guardrail you can:**

* **Enable or disable** the guardrail
* **Edit the blocklist** - add custom paths, or remove commands that don't apply to your environment, via a dedicated configuration modal
* **Scope to endpoint groups** - apply the guardrail to specific groups rather than the entire fleet
* **Run an impact check** - preview how many events would have been blocked before enabling

**Default state:** Both guardrails are off by default. Enable them when you're ready to enforce.

***

### Supported Agents

#### Cursor

Koi supports enforcement on Cursor v1.7 and later.

**Enforced hook events:**

* `preToolUse` - Fires before a tool call executes. Used by both guardrails to intercept Read, Grep, file\_search, and Shell tools.
* `beforeReadFile` - Fires before a file is read. Used by the credential access guardrail.
* `beforeShellExecution` - Fires before a shell command runs. Used by both guardrails.

#### Claude Code

Koi supports enforcement on Claude Code v1.0 and later.

**Enforced hook events:**

* `PreToolUse` - Fires before any tool execution (Bash, Read, Glob, Grep, MCP). Used by both guardrails.

💎 **Coming soon:** Support for additional agent hosts including Gemini CLI, GitHub Copilot, Windsurf, Cline, and Kiro.

***

### Setup

#### Prerequisites

* **Cursor:** Version 1.7 or later
* **Claude Code:** Version 1.0 or later
* **Agent Activity:** Must be enabled (enforcement builds on the same hooks infrastructure)
* **MDM script package:** Standard (non-Nuitka) deployment required

#### Deployment

Agent Enforcement is deployed automatically through the existing MDM script package. When guardrails are enabled in the Koi portal:

1. Guardrail settings configured in the portal are delivered to the MDM
2. The MDM deploys the enforcement script as pre-compiled `.pyc` bytecode to the Koi configuration directory
3. The MDM writes the `guardrails_config.json` policy file alongside the script, containing the enabled guardrails and their blocklists
4. The MDM updates the hooks configuration to route agent events through the enforcement script

The policy configuration is refreshed on every MDM run cycle. No manual configuration is required on endpoints.

**Hook command format:**

```bash
/usr/bin/python3 "/Library/Application Support/Koi/koi_agent_guard.pyc" --event beforeShellExecution --agent cursor
```

> **Note:** The MDM resolves the absolute Python path at deployment time (using `sys.executable`), so the hook command does not depend on `python3` being in PATH.

#### Supported Paths

Enforcement scripts and configuration are deployed to the enterprise configuration path, ensuring consistent coverage across all users and projects on the endpoint.

* **Cursor:**
  * macOS: `/Library/Application Support/cursor/hooks.json`
  * Windows: `C:\ProgramData\Cursor\hooks.json`
* **Claude Code:** `managed-settings.json` deployed via MDM to OS-specific paths
  * macOS: `/Library/Application Support/ClaudeCode/managed-settings.json`
  * Windows: `C:\ProgramData\ClaudeCode\managed-settings.json`
* **Guardrail config:**
  * macOS: `/Library/Application Support/Koi/guardrails_config.json`
  * Windows: `C:\ProgramData\Koi\guardrails_config.json`

***

### Relationship to Agent Activity

Agent Enforcement and Agent Activity share the same underlying hooks infrastructure and work together:

* **Agent Activity** provides visibility - capturing and logging all agent events for monitoring, investigation, and audit.
* **Agent Enforcement** adds protection - evaluating agent events against policies and blocking dangerous actions before they execute.

💎 **Coming soon:** Enforcement events (both allowed and blocked) appear in the Agent Activity feed with their enforcement decision, providing a complete audit trail that includes both what happened and what was prevented.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guides/protect-ai-tools-with-koi/agent-enforcement.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
