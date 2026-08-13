<!-- KOI source: https://docs.koi.ai/guides/protect-the-agentic-endpoint-with-koi/skills-discovery.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guides/protect-the-agentic-endpoint-with-koi/skills-discovery.md).

# Skills - Discovery (Preview)

Koi gives organizations complete visibility into the Agent **Skills** installed across AI-powered platforms on their endpoints. Skills are modular capabilities that extend what an AI agent can do - packaged as a `SKILL.md` instruction file plus optional scripts, tools, and resources -and they can be installed from public registries, bundled inside plugins, or hand-written by developers.

***

### What is Skills Discovery?

Skills Discovery provides a real-time view of all known Agent Skills installed across AI coding agents on endpoints in your organization. It helps you:

* Understand what skills your developers are using across their AI agents
* See where each skill came from - the marketplace, repository, or plugin it was installed through
* Track skill metadata including name, version, source, and the platforms it applies to
* Identify skills that were hand-written or side-loaded (no known source) and flagged as manually installed
* Establish the inventory foundation that risk scoring, marketplace enrichment, and runtime correlation build on

***

### Supported  Platforms and Sources&#x20;

Koi discovers skills regardless of which agentic platform consumes them, by scanning the standard skill locations on managed endpoints (`.agents`, `.claude`, `.cursor`) and correlating each skill back to its origin.

Skills installed via `.agents/` are available to any agentic platform on the endpoint (Claude Code, Cursor, OpenClaw, and others), so a single skill may apply to multiple platforms.

Koi continuously expands source and platform coverage as the agentic skills ecosystem grows.

#### Supported Skill ecosystems

<table><thead><tr><th>Source</th><th width="378.859375">Discovery Method</th><th>Identifier</th></tr></thead><tbody><tr><td><strong>skills.sh</strong></td><td>Parses <code>skills-lock.json</code> in project-level and global <code>.agents/</code> directories</td><td>skills_sh</td></tr><tr><td><strong>ClawHub</strong></td><td>Filesystem-based plugin enumeration</td><td>clawhub</td></tr><tr><td><strong>Self-made / manual</strong></td><td>Discovers <code>SKILL.md</code> files with no known registry source</td><td>manual</td></tr></tbody></table>

***

### Where Skills Appear

Discovered skills are available in two places:

* **Dedicated Skills inventory** - a standalone view listing all skills discovered across your organization.
* **Agentic AI Inventory** — skills appear alongside other agentic items as a dedicated item type (`Item type = Skill`), so you can filter for them and combine them with other query-builder conditions.

In both views, each skill surfaces:

<table><thead><tr><th width="139.01171875">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Name</strong></td><td>The skill name (e.g. <code>frontend-design</code>)</td></tr><tr><td><strong>Version</strong></td><td>The installed skill version</td></tr><tr><td><strong>Marketplace / Source</strong></td><td>Where the skill was installed from - skills.sh, ClawHub, a GitHub repo, or a plugin</td></tr><tr><td><strong>Installation method</strong></td><td>Marketplace, built-in (via plugin), or manual (self-made)</td></tr><tr><td><strong>Platform</strong></td><td>The agentic platform(s) the skill applies to (Claude Code, Cursor, OpenClaw, …)</td></tr><tr><td><strong>Publisher</strong></td><td>The skill's publisher, when available from the source</td></tr><tr><td><strong>First seen / Last seen</strong></td><td>When the skill was first and most recently observed on endpoints</td></tr></tbody></table>

You can pivot from any skill to the endpoints it's installed on to see exactly where it's running across your fleet.

<figure><img src="/files/3gN0YxmyuZBloliWFNY8" alt=""><figcaption></figcaption></figure>

***

### Why Does This Matter?

Skills are one of the fastest-growing parts of the AI development stack - and one of the least visible. Unlike a traditional dependency, a skill is free-form instruction text that an agent will follow, often bundled with scripts and tool permissions. That means a skill can:

* Instruct an agent to read sensitive files, delete data, or modify databases
* Introduce tools and capabilities the agent didn't have before
* Be installed naively from an unverified publisher, or hand-written and never reviewed
* Carry hidden or malicious instructions that don't match its stated description (skill poisoning, skill shadowing)

Without visibility into which skills are installed, security teams have no way to assess what their agents can actually do. By discovering and cataloging every skill and tracing it back to its source, Koi gives you the foundation to understand, evaluate, and govern the skills your developers rely on.

***

### Key Benefits

* **Full visibility** into skills installed across AI agents on your organization's endpoints
* **Source correlation** tracing each skill back to its marketplace, repository, or parent plugin
* **Manual-skill detection** surfacing hand-written and side-loaded skills that have no registry source
* **Inventory foundation** that powers query-builder filtering, alert policies, and the risk and runtime layers coming next

***

### Known Limitations

* Skills pulled in as part of a **plugin** are discovered through the plugin, but full skill-level correlation to the parent plugin is still in progress.
* **Marketplace enrichment** (stars, install counts, contributors, license, verified-publisher status) is not yet populated in the skill details.
* **Risk scoring** for skills is not yet available - discovery establishes the inventory that risk insights will build on.

***

### 💎 **Coming soon:**

* **Skill details drawer** - a full breakdown of each skill's metadata, instructions, tools, and capabilities (the same depth available for MCP servers)
* **Marketplace enrichment** - stars, installs, contributors, license, and verified-publisher indicators pulled from skills.sh and ClawHub
* **Risk analysis** - risk scoring for skills, including detection of skill poisoning, skill shadowing, and description/body mismatches
* **Runtime correlation** - linking each skill to the agent sessions that invoked it, with navigation to the runtime event report
* **Plugin correlation** - full mapping of plugin-pulled skills back to their parent plugin's item report
* **Skills governance** - block, allow, and remediation policies for skills, extending the same governance model available for extensions and MCP servers


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guides/protect-the-agentic-endpoint-with-koi/skills-discovery.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
