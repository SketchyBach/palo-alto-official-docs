---
url: https://docs.koi.ai/guides/item-identifiers-per-marketplace
fetched_at: 2026-09-06T09:13:26.268Z
source: koi-official-browser
capture_method: authenticated official browser
---

# Item identifiers per marketplace

For the complete documentation index, see llms.txt. This page is also available as Markdown.
Ask
DocumentationGuides
Item identifiers per marketplace

When managing governance policies or tracking software inventory across your organization, you'll need to correctly identify items from different marketplaces or Source. Each marketplace has its own identifier format, and understanding these formats is crucial for effective governance.

Identifier Formats by Marketplace
Marketplace / Source / Scope
Identifier Format
How to Find/Build the ID
Example

Browsers (Chrome Web Store / Edge Add-ons / Firefox Add-ons)

Extension ID

Get from extension details in the marketplace, or from the extension's URL or folder name. Chrome & Edge are 32 lowercase letters; Firefox is the slug/UUID from addons.mozilla.org.

aapbdbdomjkkjkaonfhkkikfgjllcleb

VSCode-compatible IDEs (VSCode / Cursor / Windsurf / Open VSX / Visual Studio)

Extension itemName

Use itemName from the marketplace URL (marketplace.visualstudio.com/items?itemName=..., open-vsx.org/extension/..., etc.) or the Identifier field shown in the IDE's extensions panel. Format: {publisher}.{extension-name}.

github.github-vscode-theme

JetBrains Marketplace

Numeric plugin ID

Numeric ID from plugins.jetbrains.com URL (/plugin/{id}-...).

12345

Notepad++ Plugins List

{arch}/{folder-name}

Architecture (x86, x64, arm64) plus the plugin's folder name from nppPluginList.

x64/NppExport

Office Add-ins

Item ID

Office Store ID starting with WA (WA + 9 digits).

WA200007038

npm

Package name

Exact package name from npm.

types-registry

PyPI

Package name

Exact package name from PyPI.

requests

Homebrew

Full formula or cask name

{tap}/{type}/{name} (type is cask or formula).

homebrew/cask/sakura

Chocolatey

Package name

Exact id from community.chocolatey.org/packages/{id}.

7zip

Hugging Face

models/{ID} or datasets/{ID}

Prefix with models/ or datasets/ plus the Hugging Face asset name.

models/meta-llama/Llama-3.2-3B

Ollama

{model}:{tag}

Model name and tag from ollama.com/library.

gemma3:7b

Docker

Image reference

Fully-qualified Docker image name, optionally with registry host (defaults to Docker Hub).

library/nginx · ghcr.io/github/github-mcp-server

GitHub MCP Registry

publisher/repository

Get from the MCP's URL (e.g., github.com/mcp/upstash/context7 → upstash/context7).

upstash/context7

MCP Registry (registry.modelcontextprotocol.io)

{publisher-namespace}/{server-name}

The server.name field from the registry entry (publisher-namespace is the part before the first /).

io.github.modelcontextprotocol/fetch

Claude Desktop Extensions

Extension id

The id field from the extension's manifest, listed at anthropic.com/engineering/desktop-extensions.

anthropic/file-reader

Agent Plugins (Cursor Plugins / Claude Code Plugins)

Plugin source + plugin name

Agent Plugins are identified by the plugin source plus the plugin name. For example:

GitHub-hosted plugin — source is the repository URL, https://github.com/{owner}/{repo}.

URL / Git-subdir plugin — source is the URL the plugin was pulled from.

Cursor marketplace plugin — source is the Cursor marketplace name.

Source: https://github.com/anthropics/example-plugin
Name: code-reviewer

Git Repositories (GitHub / GitLab / Bitbucket)

owner/repository

The {owner}/{repo} path from the repository URL.

placeholder-security/Koi

Installed Software – macOS

Bundle identifier

macOS application bundle identifier (CFBundleIdentifier) reported by the MDM agent.

com.docker.docker

Installed Software – Windows

Application display name or SHA256

Either the display name from Windows Apps & Features (Uninstall registry) or the binary SHA256 — both forms are accepted. You can find either in Koi's Inventory page.

Google Chrome
SHA256 – 06323a9accaac79b855f2348602fc259764c49dcba91103a89410dc8d42d58a2

Installed Software – Linux

Package name or SHA256

Either the package name reported by the system package manager (dpkg, rpm, etc.) or the binary SHA256 — both forms are accepted.

git
SHA256 – 06323a9accaac79b855f2348602fc259764c49dcba91103a89410dc8d42d58a2

Binaries – macOS

SHA256, Team ID and Signing ID

Get the identifiers directly from Koi's platform UI, either in the Inventory page or the Runtime page.

SHA256 – 06323a9accaac79b855f2348602fc259764c49dcba91103a89410dc8d42d58a2
Signing ID – platform:com.apple.sbd
Team ID – Y5PE65HELJ

Previous
Request approval workflow
Next
End-user notifications

Last updated 3 months ago
