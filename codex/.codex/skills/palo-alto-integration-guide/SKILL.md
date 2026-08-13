---
name: palo-alto-integration-guide
description: Produce vetted, exact, step-by-step guides using the project's official Palo Alto Networks and KOI corpus. Use whenever the user requests a guide, steps, walkthrough, "how do I", setup, configuration, integration, deployment, connection, installation, onboarding, migration, enablement, implementation, or validation for Cortex, Strata, Prisma SASE/Access, Identity/Idira, AI security, KOI, EDR, MDM, SSO, APIs, proxies, certificates, endpoints, or third-party systems.
---

# Palo Alto Integration Guide

Use a strict evidence chain. Do not assemble a plausible procedure from memory.

## Scope before steps

Identify both sides of the integration, product versions, management plane, deployment mode, operating system, tenant/region, and desired traffic or data flow. Ask one focused clarification if any missing value changes the steps. Never mix Panorama with Strata Cloud Manager, tunnel-only with explicit proxy, or different OS procedures.

## Build the evidence set

1. Run `python scripts/search.py "<both products + integration name>" --mode integration --json`.
2. Open the primary integration page and every directly relevant page it references for prerequisites, certificates/trust, networking, permissions, deployment, verification, and removal/rollback.
3. Run focused searches for gaps, such as `<integration> prerequisites`, `<integration> verify`, `<integration> uninstall`, or an exact UI label.
4. Require at least one primary official procedure. Corroborate prerequisites and compatibility with a second official page when available.
5. Apply `references/integration-gate.md`. Stop and disclose the gap if a required step is not documented.

If no verified primary procedure exists, do not construct a guide from related pages or memory. Say: `I'm sorry, I don't know. I couldn't verify this in the available official documentation.` Name the missing procedure or scope and stop before presenting steps.

## Write the guide

Use this order:

1. **Applies to** — products, versions, management plane, OS, deployment mode.
2. **Prerequisites** — licenses, roles, credentials, network, certificates, dependencies.
3. **Data/traffic flow** — one compact paragraph when it prevents configuration mistakes.
4. **Steps** — atomic numbered actions using exact UI labels, paths, commands, and values from evidence.
5. **Verify** — expected observable result for each important layer.
6. **Rollback** — documented uninstall/reversal steps; otherwise state that rollback is not documented.
7. **Cautions** — Preview status, workflow interruption, routing/certificate impact, or known limitations.
8. **Sources and freshness** — official URLs and content dates.

Do not invent secrets, IDs, ports, domains, API fields, timing, defaults, or menu labels. Use placeholders only when the source says the customer must obtain a tenant-specific value.

Always use numbered steps, even if the user only says "guide" without explicitly requesting step-by-step formatting. Cite the applicable source beside each step or tightly related group of steps. Keep published instructions separate from any support-derived workaround; label the latter and include it only when relevant to the user's symptoms.
