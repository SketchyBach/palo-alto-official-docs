<!-- KOI source: https://docs.koi.ai/get-started/whats-new-in-koi.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/get-started/whats-new-in-koi.md).

# What’s new in Koi

### July 2026

**AI Protection:**

* **AI Agent Personal Account Usage \[Preview]** - Koi now detects the user account behind AI agent session, turning shadow AI usage into something you can see and act on. Employees often run agents like Claude Code, Cursor, and Codex with personal accounts on corporate endpoints. When corporate data flows through a personal account, it leaves the organization's visibility and control, creating a real data exfiltration risk. Depending on the account's settings the data can even be used to train the LLM model. Personal account activity now surfaces directly in the AIDR - Agent Activity view. [Learn more](https://docs.koi.ai/guides/agentic-runtime-control/runtime-agent-activity/ai-agent-personal-account-usage).
  * **Per-session user account detection** - the user email account signed in to the agent, captured per session across Claude Code, Cursor, Codex, and Antigravity.
  * **Personal account classification** - an account is flagged as personal when its email domain doesn't match your organization's domain.
  * **Personal user account filter** - a new Query Builder filter to instantly find all sessions running under personal accounts.
  * **Subscription** - the account's subscription (for example Free, Pro, Enterprise), shown in the session details drawer -useful for spotting free tiers that may train on your data by default.
* **AIDR Sessions view -** AIDR page is now organized by session (the single continuous conversation between a developer and an agent) instead of a flat event stream. Every shell command, file access, MCP tool call, skill, and network request is grouped into the session that produced it, so you can follow the full arc of an agent's work from start to finish.
  * **One row per session:** With aggregates for total sessions, distinct endpoints, distinct users, and average session duration.
  * **Full session timeline:** Open any session to see every action in order with its timestamp and the resource it touched (file path, command, MCP tool, skill, or URL/IP); expand an event for detail such as a code diff or a tool's input and output.
  * **Agent extensions per session:** see exactly which MCP servers, skills, and plugins each session used.
  * **Governance per session:** Blocked actions shown in context, with a new "Governed by" column identifying the enforcing policy, filterable in the query builder.
  * **Session-aware search** and saved queries across agent, endpoint, user account, action category, extension, duration, and time range.
* **Plugin remediation for Claude Code** - Koi now governs the plugins agents install to expand their own capabilities. Admins can remediate a Claude Code plugin on demand from the Inventory or Endpoints table, fully removing it from the device.&#x20;

**Binaries Discovery & Governance**

* **Binaries visibility & governance for macOS \[Preview]** - Centralized visibility and control over binary execution across your macOS fleet, powered by Koi's integration with Santa. Every binary launch is captured with full context - who executed it, on which endpoint, the path, and the file's SHA-256 - making Koi the single portal to govern all software running on macOS devices, binaries and non-binaries alike. [Learn more](https://docs.koi.ai/guides/protect-applications-with-koi/binaries-discovery).
  * **Binaries Inventory** - full visibility into every binary that ran across your macOS endpoints in the org. [Learn more](https://docs.koi.ai/guides/protect-applications-with-koi/binaries-discovery/binaries-inventory-preview#binaries-inventory).
  * **Binary Execution Logs** - the event-level record of what's actually running: every binary launch on a macOS endpoint, captured with full context. [Learn more](https://docs.koi.ai/guides/protect-applications-with-koi/binaries-discovery/binary-executions-preview).
  * **Block and Alert policies** - define custom policies to govern which binaries can run across your macOS fleet.
  * **Impact Check** - before applying a new policy, run an Impact check to see which binaries and endpoints it would affect.
  * **Request Approval flow** - blocked users aren't left stuck: they get a clear notification and can request approval on the spot, so admins can review and approve the binary from the dashboard.
  * **New Guardrail: Block execution from risky paths** - blocks execution of binaries from high-risk, user-writable paths such as `/tmp`, `/var/tmp`, and `$TMPDIR`, reducing exposure to untrusted and potentially unsafe content.

### June 2026

**AI Protection:**

* [**AI Agents Discovery**](/guides/protect-the-agentic-endpoint-with-koi/ai-agents-discovery.md) to identify AI agents across all item types, including binaries and non-binaries, so new and emerging agents surface automatically in your inventory.&#x20;
* [**Skills Discovery**](/guides/protect-the-agentic-endpoint-with-koi/skills-discovery.md) - Koi now discovers and inventories Agent Skills installed across AI agents on your endpoints - from the **skills.sh** and **ClawHub** registries, as well as self-made and manually installed skills. Each skill is correlated back to its source and surfaced both in a dedicated Skills inventory and as a filterable item type in the Agentic AI Inventory.
* **Claude Connectors MCP Governance** - Koi extends MCP governance to the Claude Connectors marketplace built into the Claude desktop app. Admins can get visibility on desktop connectors with marketplace metadata, set allow/block lists enforced at install and update time, and remediate connectors already installed on endpoints.
* **MCP Request Approval support** - Blocked MCP installs can now be routed through an approval workflow instead of a hard block. When a user tries to install a blocked server, Koi replaces the 'Install' button with **Request Approval** - the user submits a request, and the admin approves or denies it from the dashboard. Available for the **Claude Connectors** marketplace and the **GitHub MCP Registry** (VS Code).
* Once a runtime policy is live, the **side panel** now has two additional tabs:
  * Policy Hits - Shows every block and ask event the policy fired, grouped by endpoint and agent. Expand any group to see individual events, each showing the matched rule type (File Path, Command, MCP Tool, Skill, or URL) and the matched entity.&#x20;
  * Devices Excluded - The devices currently excluded from the policy, including who approved each exclusion and the justification. This gives admins an audit trail of every exception granted against the policy.

**UX & Performance**

* Workflow-based navigation that makes it easier to find and manage everything in one place - from **inventory** to **policies** and **guardrails**, with dedicated workspaces for **Agentic AI**, **Non-Binaries**, and **App Control**.

### May 2026

**AI Protection**

* **Agent Enforcement Custom Policies \[Preview]** - Define your own runtime rules for what AI coding agents can do - block or ask before they execute. Policies are composed from five rule types: shell commands, file access, MCP tools, skills, and network requests (URLs/IPs). Each policy supports Block (deny outright) or Ask (pause for developer approval) modes, with an estimated impact check showing how many endpoints and actions it would have affected over the last 30 days before you enable it. [Learn more](https://docs.koi.ai/guides/protect-the-agentic-endpoint-with-koi/runtime-protection/agent-enforcement-custom-policies).
* **Agent Runtime Policies API** - New public API endpoints for creating, updating, and managing runtime enforcement policies programmatically. Lets customers automate policy management via CI/CD pipelines or custom tooling, instead of only through the Koi portal. [Learn more](https://docs.koi.ai/api-reference/reference/agents-runtime-policies).
* **New agents supported for Agents runtime** - Agent Activity, Guardrails, and Agent Runtime Custom Policies now extend beyond Cursor and Claude Code to three additional AI coding agents:
  * **Codex CLI** - Block-mode enforcement across shell, files, MCP tools, skills, and network.
  * **GitHub Copilot CLI** - Full coverage including both Block and Ask enforcement modes.
  * **Gemini CLI** - Block-mode enforcement across all rule types except network controls (Codex and Gemini CLI run web access through hosted infrastructure, so URL/IP rules are best expressed as shell rules on curl/wget). [Learn more](https://docs.koi.ai/guides/protect-the-agentic-endpoint-with-koi/runtime-protection/agent-enforcement-custom-policies#supported-agents).

**Remote Developer Environments**

* **Coder support** — Coder workspaces now show up in Koi like any other endpoint. The items running inside each workspace are shown in the same inventory, endpoint, and\
  dashboard views as any other endpoint. [Learn more](/integration-guides/remote-development-environments/coder/deploying-koi-on-coder-workspaces.md)

**Inventory**

* **View by item** — Switch the inventory from one row per install to one row per unique item. Instead of scrolling past the same package repeated across hundreds of endpoints, you see each item once — with its versions, footprint across the fleet, and risk grouped under the same row. Expand a row to drill into where it's installed and which versions are out there.
* **Git Repository Discovery \[Preview]** — Koi now surfaces git repositories cloned across your fleet and adds it to a new Repository Inventory, enriched with publisher, stars, license, and risk signals for public GitHub repos.&#x20;

**Governance**

* **NPM package remediation** **\[Preview]** - Remediate critical-risk NPM packages directly from Koi for fast response to supply chain incidents like Shai Hulud. Learn more in the [Docs](/guides/protect-code-packages-with-koi/code-packages-remediation.md).
  * Want early access? Please contact the Koi Customer Experience team
* **New Policies page design** - We've redesigned the Policies page to make managing your supply chain gateway easier and more intuitive. The page is now organized into three focused tabs:
  * **Marketplace Modes** - Configure which marketplaces are blocked by default and which are allowed friction-free. A new toggle-based layout makes enabling "block by default" clearer and simpler to use.
  * **Policies** - Create custom policies or apply ready-made ones from the Policy Library. Policies can now be reordered via drag-and-drop, and toggling them on or off is a single click.
  * **Global Lists** - Manage your globally allowed and blocked items in a dedicated, distraction-free tab.

**End user experience**

* **End-User Experience settings** - A new centralized settings page to control how end users experience your security policies - customize block messages for IDE extensions and code packages, configure Slack/Email notifications for policy events, and choose whether blocked items are hidden or shown in IDE marketplaces. Learn more in the [Docs](/guides/end-user-experience-settings.md).
* **Email Notifications** - Koi now supports end-user email notifications, giving you another way to inform users on policy violations. This feature requires an [Okta](/integration-guides/okta.md) or [Entra ID](/integration-guides/entra-id-integration.md) integration.

**UX & Performance**

* Refreshed UI color theme aligned with the **Cortex Palo Alto Networks** brand with a **dark mode**.
* New **Deployment Portal** brings endpoint deployment and network routing into one place, each with a wizard that walks your team through every option for their stack.

### April 2026

**AI Protection**

* **Agentic AI Inventory:** Full visibility into every AI component installed on your endpoint fleet: Plugins, Skills, MCP Servers, platforms, agents, AI extensions, and AI models. Filter by type, risk level, findings, and more to stay on top of what's used across your org.
* **Ollama model discovery:** Koi now discovers Ollama models installed on endpoints, giving you visibility into locally deployed AI models alongside the rest of your software inventory.

**Code Package Risk**

Koi now goes deeper on code package risk - with enhanced malicious intent detection and out of the box prevention policies.

* **Enhanced detections:** Deeper behavioral and structural signals covering obfuscated code, API abuse, data exfiltration, shell execution, persistence, registry access, privilege escalation, and more.
* **Expanded policy library:** New and updated built-in policies for code packages covering obfuscated code, malicious dependencies, RCE, prompt injection, and publisher-level signals — strong defaults, zero custom config needed.

### March 2026

**Code Package Governance**

* **More powerful Code Package policies** - Block and allow policies for code packages now support a significantly broader set of conditions, including all Wings deep risk analysis findings and vulnerability data, giving you more powerful and granular control over what enters your environment.

**AI Protection**

* **Claude Code MCP** discovery and remediation - Koi now provides visibility and control over MCP servers used by Claude Code across local, project, and global scopes, including MCPs introduced via plugins.
* **Hugging Face** search in Koidex - Koidex now includes search for Hugging Face items, enabling to discover models and datasets observed across environments and accelerate investigation and research workflows.

**Binaries Governance**

* **Custom block policies for Binaries** - Create binary block policies on macOS devices with granular scoping by organizational profiles.
* **Productivity Impact Check** - Evaluate the expected productivity impact of binary block policies before enforcement to reduce disruption to business workflows.
* **End-user notifications and approval workflow for blocked binaries** - When execution is blocked, end users receive a notification and can request administrator approval through a built-in approval flow.
* **New Guardrail: Block execution from risky paths** - Block execution of binaries from high-risk, user-writable paths such as /tmp, /var/tmp, $TMPDIR, and /Users/Shared/ to reduce exposure to untrusted or potentially unsafe content.
* **Policy Library templates for Binaries** - Ready-to-use templates help teams quickly block untrusted publishers or applications and adapt enforcement to organizational needs.

**Binaries Discovery**

* [Santa integration](https://docs.koi.ai/integration-guides/endpoint-integration/santa-integration) on macOS provides centralized visibility into binary execution on endpoints covered by Koi and synced to Koi Santa sync server.
* **Binaries Inventory** - A new inventory view that provides visibility into binaries observed across macOS endpoints, including file name, SHA-256, signing context, first seen, last seen, last used, path, and more.

**API & Integrations**

* [Reports API](https://docs.koi.ai/api-reference/reference/reports) **-** Export Koi inventory reports for installed items via `POST /api/external/v2/reports`, then poll `GET /api/external/v2/reports/{report_id}` for a `download_url` (presigned, 12-hour expiry).
* **Search inventory** **API -** Build queries with AND/OR logic and advanced filters through the [Search inventory API](https://docs.koi.ai/api-reference/reference/inventory#post-api-external-v2-inventory-search), enabling precise, automated inventory investigations.
* **Validate Webhook Integration** with a Test Webhook capability that sends a live sample payload to your configured endpoint using your existing headers.
* **Establish Network route via PAC file** - distribute by a click Koi PAC configuration on ALL devices running the Koi script via the deployment portal.

**UX & Performance**

* Consolidated view of key metrics on the **Dashboard** page with Risk distribution (Critical / High / Medium / Low) over different item types and Risk overtime view.
* New **Audit & Koidex pages** with a cleaner, easier-to-navigate and filter layout.
* New **item** and **endpoint** **drawers** - A redesigned drawer experience across items and endpoints, providing a faster, more consistent, and structured way to explore details, investigate risk, and understand context directly within Koi.

**Audit**

* **Enhanced audit logs** - Audit logs have been significantly improved to provide more complete, structured, and actionable visibility into both user and system activity, making it easier to investigate changes and track actions across Koi.

***

### February 2026

**AI Protection**

* **OpenAI Codex MCP Discovery -** Koi's MCP inventory now includes visibility into MCP servers configured with OpenAI's Codex platform. Codex connects to MCP servers to access external tools and services as part of its automated workflows - extending consistent MCP visibility across your organization. The Codex application and Codex CLI are also discoverable in the relevant inventories.
* **New MCP Security Findings -** Five new finding types now surface risk in MCP tool configurations: **Tool Poisonin**g, **Tool Shadowing**, **Vulnerable to Prompt Injection**, **Data Export Capability**, and **Arbitrary Code Execution**. These findings help security teams identify risky MCP tool behaviors before they cause damage.
* **OpenClaw (previously Clawdbot/Moltbot) Discovery & Blocking -** Koi discovers OpenClaw (Clawdbot/Moltbot) across npm, Homebrew, and macOS app installations. A ready-to-use "Block ClawdBot" policy is available in the Policy Library under AI, enabling immediate blocking or alerting across your environment.

**Applications Inventory & Discovery**

* **Richer Application details**, adding usage and signing context so teams can understand what is actually running, and make better governance decisions.
  * **Last used** shows the most recent time the application was used in the organization. Use it to find apps that have not been used in the last 30, 60, or 90 days, identify cleanup candidates, and reduce exposure to outdated or unnecessary software.
  * **Signing identity** adds **Team ID** and **Signing ID** to reliably attribute macOS applications to the signing developer and group all versions of the same app under the same identity.
  * **Signature and certificate context** is now available directly in the application view, giving teams better certificate hygiene insights and making it easier to review certificates across the organization.
    * Including data such as Is Signed, Certificate Expiration Status, Certificate Expiration Date, Certificate Issuer, Key Size, Certificate Signature Algorithm, and Signing Certificate Hash.
    * You can quickly spot potentially less secure certificates, such as certificates that are expired, expiring soon (60 days or less), using short key sizes (below 2048 bits), or signed with weak algorithms (SHA-1, MD5).
  * **SHA256** is shown for precise identification of the specific binary version observed.

**Applications Governance**

* Added **alert policies for Applications** to surfaces installed applications that matches your risk conditions.

**Governance**

* **New guardrails support for Code packages:**
  * The ***Delayed Access*** guardrail now supports npm and PyPI packages, blocking installation of newly published packages for a configurable period to protect against zero-day supply chain attacks.
  * ***Version update cooldown*** is now also supported for PyPi packages, allowing you to configure a set period of time before a new version of a PyPi package can be pulled.

***

### January 2026

**AI Inventory & Risk Analysis**

* **Enhanced MCP risk context**, giving teams visibility into *how* MCP servers introduce risk, not just where they exist.
  * View **tools exposed by MCP servers**, whether local or remote.
  * Understand **tool capabilities**, including code execution, OS commands, data writes, and data export.
  * See **MCP** **authentication methods** (no auth, API keys, OAuth).
* **Agent Activity** provides deep, investigation-ready visibility into what agents actually do across your environment. This feature is in early access starting with **Cursor** and **Claude Code**.
  * **Tool Activity view** shows which MCPs and tools agents invoke and how executions resolve.
  * **All Activity view** offers a unified, filterable feed of agent events across endpoints, agents, tools, and models for audits and investigations.

**Inventory & Discovery**

* **\[Gradual rollout] Chocolatey package discovery** extends software visibility to Windows OS packages installed via Chocolatey.

**Remediation**

* **Item-level force remediation**, allowing force enforcement to be applied **per item** instead of relying on a global setting.
  * Clear **Pending remediation status**, showing exactly what’s blocking completion.
  * Full transparency into **what processes or dependencies will be force-closed** before enforcement.
  * Eliminates stalled remediations while ensuring force actions are applied only when truly required.

**Threat Intelligence & Malware Context**

* **Expanded malicious version visibility** in item reports.
  * View **all known malicious versions** of an item, not just the currently selected one.

**Documentation & Access**

* **New Koi documentation platform** is now live.
  * Access docs at **docs.koi.ai** using your existing Koi platform credentials for simpler, unified access.

***

### December 2025

**API & Integrations**

* Introduced **Koi API v2**, delivering a modern RESTful design with resource-based URLs, consistent schemas, and improved reliability for large-scale integrations.
  * Fully **OCSF-aligned Alerts API**, making it easier to normalize, correlate, and ingest Koi alerts into SIEM and SOAR platforms.
  * **Transaction-based batch operations**, ensuring atomic, all-or-nothing processing to prevent partial or inconsistent updates.
  * Expanded and refined **API documentation**, including clearer examples, full response schemas, and explicit error handling guidance.
  * Announced **API v1 deprecation timeline** (January 31, 2026), with a supported transition period to help teams migrate safely to v2.

**UX & Performance**

* Major performance improvements to **Inventory views**.
* A new **Endpoints page** with a cleaner, easier-to-navigate and filter layout.
* The **Items Report** now includes **campaign-level context** for risky items, directly showing when an item is associated with a known malicious campaign.

**Governance**

* **Impact checks** now show a full list of installed items that match the guardrail conditions, along with affected endpoints and endpoint groups including the name, devices, publisher, platform, and marketplace for each impacted item.

**MCP Governance**

* Added **alert policies for MCP** to surfaces installed MCP servers that matches your risk conditions.

**Remediation**

* **Force remediation for Windows** ensures extensions are fully removed when enforcement is required even if the hosting application is still open. Force remediation can now be enabled in Settings → Advanced to enforce extensions removal across browsers, IDEs, and Notepad++.

***

### November 2025

**Endpoint Lifecycle Management**

* **Manually or automatically archive inactive endpoints**, ensuring dashboards and remediation views reflect only relevant, active assets.

**Governance**

* **Metadata-based policies for PyPI packages**, enabling governance based on package and publisher metadata, similar to existing npm controls.

**Audit**

* Enhanced **remediation audit logs** with richer context, such as who initiated remediation and why.

**UX & Performance**

* New **policy creation wizard** to simplify governance workflows.
* Refreshed navigation bar, an improved remediation page, and **faster inventory performance** for smoother day-to-day operations.
* New export options, including **Inventory by instance** (endpoint-level detail) and a **Risk report PDF** for easier sharing and audits.

**MCP Governance**

* **MCP governance capabilities**, including prevention and remediation:
  * **Control what can be used** - Define which MCP servers are **allowed or blocked across your org**.
  * Match enforcement to your risk approach - Start with monitor-only visibility, apply targeted **block policies**, or go strict with full **allowlist mode**.
  * **New Guardrail: MCP Registry Monitoring** - Ensure MCP servers can only be installed from the official MCP registry on supported platforms.
  * **Remediate safely from one place** - Continuously surface violating MCPs and remove them with one click, without disrupting end-user workflows.

***

### October 2025

**API & Integrations**

* New **Inventory APIs** that provide programmatic access to installed items, with rich filtering and endpoint-level context.

**Coverage Expansion**

* Expanded visibility and governance to include the **GitHub MCP registry**, **Kiro IDE**, and **ChatGPT Atlas**, extending protection to emerging platforms.

**Governance**

* **Granular version update cooldown controls**, allowing per-marketplace and per-item configuration.
* **Custom Hugging Face policies** based on marketplace metadata.

**UX & Performance**

* **Activation status filtering** to help teams prioritize items that are actively enabled in their environment.

***

### September 2025

**Remediation**

* Support for **item- and version-specific remediation directly from the inventory**, without requiring a global block policy.
* Remediation for**Hugging Face models and data sets**.

**Governance**

* **Marketplace-level configuration** for Allowlist and Blocklist modes, with clearer, more consistent governance controls per marketplace.

**Notifications**

* **Customizable Slack notifications** for end users, allowing admins to tailor messaging, tone, and included details.

**API & Integrations**

* Enhanced the **Audit Log API** with improved querying, structured responses, and higher fetch limits.

**Inventory & Discovery**

* **Installation method visibility** (Marketplace, Manual, Built-in, Sideloaded) available in inventories to improve traceability and items risk assessment.

***

### August 2025

**Inventory & Discovery**

* Expanded inventory to provide **complete asset visibility**, including items installed via sideloading or private sources.
* **PyPI package discovery**- enabling monitoring of Python packages across endpoints.
* Introduced the **MCP Servers Inventory (preview)**, providing real-time visibility into local and remote MCP servers across IDEs and AI tools.

**Governance**

* **Policy scopes by item type** (Extensions, OS packages, Code packages) for more precise governance.
* **npm package prevention** (available for SWG-integrated customers).
* **PyPI prevention** via global blocklists.
* Added **impact checks** to preview the effect of guardrails before enforcement.

**Notifications**

* Enabled **end-user notifications** for **alert policies** to support progressive enforcement.

***

### July 2025

**Governance**

* **Granular guardrail configuration by endpoint group**, enabling targeted enforcement across different environments.
* **Alert-only mode** for applicable guardrails, allowing teams to detect risk without immediately blocking or remediating.
* Enhanced **global allowlist and blocklist management** with **CSV export**, improved auditing, and clearer conflict handling.
  * Added visibility into **who added each item** and how many **endpoints are affected**, improving traceability.
  * Enabled notes and renaming for non-marketplace items to improve collaboration and clarity.

**UX & Performance**

* **Customizable inventory and endpoint views**, allowing teams to tailor visible columns to their workflows.

***

*Want early access to upcoming features? Contact your Koi point of contact.*


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/get-started/whats-new-in-koi.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
