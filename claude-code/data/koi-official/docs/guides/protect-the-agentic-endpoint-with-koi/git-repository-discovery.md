<!-- KOI source: https://docs.koi.ai/guides/protect-the-agentic-endpoint-with-koi/git-repository-discovery.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guides/protect-the-agentic-endpoint-with-koi/git-repository-discovery.md).

# Git Repository Discovery

### Overview

Git Repository Discovery is part of Koi's **Agentic Endpoint** coverage — the unified view of every component that makes an endpoint agentic: agent platforms (Cursor, VS Code, Claude Code), agents themselves, agent extensions (plugins, skills, MCP servers), local AI models, and the **git repositories from which much of this software originates.**

#### Why it matters

Cloned git repositories are an overlooked entry point into the modern enterprise - and they matter for two distinct reasons:

1. **The agentic angle.** Skills, plugins, and sometimes MCP servers — the building blocks of AI Agents — are distributed as git repositories, and they're consumed not just by engineers but by anyone adopting AI for productivity. \
   Each one can put your environment at risk in two ways: a trusted extension can be hijacked to ship malicious code, or a legitimate extension can hand your agent more power than anyone intended.

> **Scenario 1 — a hijacked skill.** A marketing manager finds a popular "email-summarizer" skill on GitHub and adds it to their AI agent to triage their inbox faster — they don't read the code, they just want the productivity boost. Weeks later, a maintainer's account is hijacked and a new version is pushed with hidden instructions to harvest session tokens from the browser. The next time the agent runs the skill, the company's SSO credentials leak.
>
> **Scenario 2 — an over-privileged extension.** A platform engineer installs an Elastic Cloud plugin from GitHub so their agent can manage production clusters. The plugin works exactly as advertised — and inherits the engineer's admin permissions. A single misinterpreted prompt ("clean up old indices") can drop a live production index. The risk isn't a hidden payload; it's the blast radius of a powerful extension with full production access.

2. **The non-binary software angle.** Beyond AI extensions, every repo is just code waiting to run. A hijacked or malicious repo can ship with poisoned build scripts, tampered git hooks, or compromised dependency manifests that execute the moment someone runs the project — no installer, no signed package, no warning.

> **In practice:** A developer clones a popular open-source library to evaluate it for an internal project. Unbeknownst to them, the maintainer's account was compromised days earlier and a malicious `postinstall` script plus a typosquatted dependency were merged into `main`. The moment the developer runs `npm install`, the script harvests SSH keys and Git credentials from their machine and posts them to a remote endpoint. By the time the maintainer regains control, the repo is on dozens of developer endpoints across the company.

Without a fleet-wide view of what's been cloned where, you can't map your agentic attack surface or answer the basic incident-response question: "is that repo on any of our machines?"

Koi closes this gap. Koi discovers every git repository on your endpoints and adds it to your inventory, and for repos hosted on public GitHub, correlates each record with its public source to enrich it with metadata and risk insights (publisher, stars, license, archived status, topics, security posture, and more). When a discovered repo is also the install source for an agent extension on the endpoint, Koi links the two (coming soon) — so you can navigate from a repo to the Skills, plugins, and MCP servers it supplies, and back.

***

### How Repos Are Discovered

#### Discovery mechanism

Koi scans your enterprise endpoints for git repositories and reports what it finds back to your **Repository Inventory**. For every discovered repo, Koi captures the source URL, the hosting platform (GitHub, GitLab, Bitbucket, etc.), the commit, the local path on the endpoint, and the first seen date.

For repos hosted on public GitHub, Koi correlates each discovered record with the repo's public profile to enrich it with publisher details, popularity signals (stars, forks, watchers, issues), language, topics, license, and fork/archived status — all of which feed Koi's risk scoring and become available as filter and policy attributes.

#### What Koi captures per repo

**From the endpoint** — captured for every discovered repo:

| Field                | What it is                                                                                                                                |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**             | `{owner}/{repo}` derived from the remote URL                                                                                              |
| **Commit**           | The commit SHA checked out at time of discovery                                                                                           |
| **URL**              | The repo's URL                                                                                                                            |
| **Marketplace**      | The repo's hosting platform (GitHub, GitLab, Bitbucket, Codeberg, CodeCommit)                                                             |
| **First seen**       | Creation timestamp of the `.git/` directory                                                                                               |
| **Local path**       | Where on the endpoint the repo is cloned                                                                                                  |
| **Public / Private** | Whether the repo was found in GitHub's public catalog. Repos on corporate domains or not found in the public catalog are labeled Private. |
|                      |                                                                                                                                           |

**From public GitHub** — added when the repo is correlated with its public profile:

| Field                                 | What it is                                               |
| ------------------------------------- | -------------------------------------------------------- |
| **Publisher**                         | Owner name and type (user or organization)               |
| **Language**                          | Primary programming language detected by GitHub          |
| **Stars / Forks / Watchers / Issues** | Popularity, adoption, and issue-load signals from GitHub |
| **Topics**                            | Tags applied to the repo by its maintainers              |
| **License**                           | Declared license (MIT, Apache-2.0, etc.)                 |
| **Is Fork**                           | Whether the repo is a fork of another repo               |
| **Archived**                          | Whether the repo has been archived                       |

<figure><img src="/files/MMR0F3IA8NPeNzudx0RZ" alt=""><figcaption></figcaption></figure>

#### Finding repos in the UI

The Repository Inventory shows all repos discovered across your fleet with columns for Name, Commit, Risk Level, Marketplace, Is Public, Clone Date, First Seen, Last Seen, Endpoint count, Installation Method, and Publisher.

<figure><img src="/files/BEc3iNk96geStlfOCOgi" alt=""><figcaption></figcaption></figure>

* **Versioning:** Koi treats the **commit SHA as the canonical version** of a repo — branches and tags are metadata, not identity. Two clones of the same repo at different commits show as two distinct items in inventory. When a developer pulls new commits, the next discovery cycle updates the commit shown for that instance.
* **Repository Category:** Koi classifies each repo into a category — including *AI Components, Skills & Plugins*, *Machine Learning*, *Security & Compliance*, and more — so you can filter directly to the repos most relevant to your concern (for example, every repo on your fleet distributing agentic software).
* **Item detail** opens when you click any repo in the table. It shows the full metadata panel — description, topics, languages, URL, current and latest commit hashes, clone date, public/private status, stars, forks, contributors, branches, publisher, and license — plus the list of endpoint instances where that repo is present.

<figure><img src="/files/fD9fqxHuJKSrTGds81s2" alt=""><figcaption></figcaption></figure>

***

### FAQ

**How does Koi identify the same repo if it's cloned twice on the same machine?**

Each clone is a separate instance. The instance key is `(repo identity, device, local path)` — so if a developer has the same repo cloned at `/projects/app` and `/dev/app`, Koi records two instances under the same repo item. You'll see both paths listed in the item detail Endpoints tab.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guides/protect-the-agentic-endpoint-with-koi/git-repository-discovery.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
