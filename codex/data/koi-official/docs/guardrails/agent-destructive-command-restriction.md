<!-- KOI source: https://docs.koi.ai/guardrails/agent-destructive-command-restriction.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guardrails/agent-destructive-command-restriction.md).

# Agent Destructive Command Restriction

Prevents AI coding agents from executing commands that cause irreversible damage - recursive file deletion, disk operations, database drops, infrastructure teardown, and history-rewriting git operations - before the command runs. This guardrail protects against environment destruction, whether caused by agent hallucination, prompt injection, or tool poisoning.

### Why It Matters

* Coding agents execute shell commands autonomously, and a single destructive command can wipe source code, drop production databases, tear down infrastructure, or rewrite git history in ways that are not recoverable.
* Agent hallucinations, misinterpreted instructions, prompt injection, and poisoned MCP tools can all cause an agent to issue a destructive command that the developer never intended.
* Developers often grant broad shell permissions to agents to avoid interrupting their flow, which increases blast radius when something goes wrong.
* Blocking destructive commands at the hook layer (before execution) is the only reliable way to prevent irreversible outcomes, since detecting them after the fact is too late.

### How It Works

* Intercepts agent shell tool calls before the command runs.
* Tokenizes the command and strips common evasion prefixes such as `\`, `command`, `env`, `/usr/bin/`, and `bash -c`.
* Matches the base command and its arguments against a configurable blocklist. Commands are blocked only when combined with their destructive arguments (for example, `rm` is blocked with `-rf` or `-r`, not on single-file deletion), so normal development commands are not affected.
* If the command matches, the action is denied and both the developer and the agent receive a clear message explaining that the command is restricted.
* All evaluation is local, with no API calls at enforcement time, ensuring consistent low latency.

<figure><img src="/files/rjaNk5lksYF5qODDpKTH" alt=""><figcaption></figcaption></figure>

### What It Covers

The default blocklist targets commands whose destructive intent is unambiguous:

* **File and directory destruction:** `rm -rf` / `rm -r`, `shred`, `find -delete` / `find -exec rm`, `truncate`
* **Database destruction:** `DROP DATABASE` / `DROP TABLE`, `TRUNCATE TABLE`, `DELETE FROM` without `WHERE`
* **Infrastructure teardown:** `terraform destroy`, `kubectl delete namespace` / `kubectl delete`, `pulumi destroy`, `helm uninstall`
* **Cloud resource destruction:** `aws ec2 terminate-instances`, `aws s3 rm --recursive`, `gcloud ... delete`, `az ... delete`
* **Disk and partition operations:** `dd if=/dev/zero` / `dd if=/dev/urandom`, `mkfs`, `wipefs`, `fdisk` / `parted`
* **Git history destruction:** `git push --force` / `git push -f`, `git reset --hard`, `git clean -fd`, `git branch -D`
* **System operations:** `shutdown` / `reboot` / `halt`, `kill -9` / `killall` / `pkill`
* **Container destruction:** `docker system prune -af`, `docker rm -f` / `docker rmi -f`, `docker-compose down -v`
* **Data exfiltration:** `curl -d @`, `wget --post-file`
* **Supply chain risks:** `npm publish`, `pip upload`
* **Permission changes:** `chmod 777 -R` / `chmod -R 000`
* **Shell config injection:** `echo >>` targeting `~/.bashrc`, `~/.zshrc`, or `~/.profile`
* **Extended coverage:** 15 additional commands and 9 evasion-pattern detections available for broader coverage

The blocklist is configurable - remove defaults that don't apply.

### Benefits

* **Pre-execution blocking** - destructive commands are stopped before they run, preventing irreversible damage.
* **Targeted matching** - commands are blocked only with their destructive arguments, so everyday development commands continue to work without friction.
* **Evasion-resistant tokenization** - common obfuscation patterns (chained commands, prefixed paths, `bash -c` wrappers) are normalized before matching.
* **Estimated impact check** - preview how many events from the last 30 days would have been blocked before enabling, so rollout is predictable.
* **Endpoint group scoping** - apply the guardrail to specific groups for phased rollouts or environment-specific policies.
* 💎 **Coming soon: Request approval flow** - developers can request an exception directly from the block message, routed through your existing approval workflow.

### Supported Agents

* **Claude Code** (v1.0 and later)
* **Cursor** (v1.7 and later)
* ​**Codex CLI** ​
* **GitHub Copilot CLI** ​
* **Gemini CLI**&#x20;

<figure><img src="/files/wTzuQbJAYvv1yCLTEHiF" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guardrails/agent-destructive-command-restriction.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
